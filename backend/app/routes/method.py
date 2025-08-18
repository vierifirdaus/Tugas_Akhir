from flask import Blueprint, request, jsonify
import uuid
import os
import re
import graphviz
from py2cfg import CFGBuilder
from ..parsers import GraphParser
import ast

method_bp = Blueprint('method', __name__)

# ===================== SAFE DOT cleaner =====================
PURPLE_HEX = "#e552ff"

_NODE_STMT = re.compile(
    r'^\s*(?P<id>"[^"]+"|[A-Za-z0-9_]+)\s*\[(?P<attrs>.*?)\];\s*$',
    flags=re.S | re.M
)
_EDGE_STMT = re.compile(
    r'^\s*"?(?P<src>[^"\s\[]+)"?\s*->\s*"?(?P<dst>[^"\s\[]+)"?\s*(?:\[(?P<attrs>.*?)\])?;\s*$',
    flags=re.S | re.M
)

def _split_statements(dot_text: str):
    # Pecah berdasarkan titik-koma penutup statement
    return re.split(r'(?<=;)\s*\n', dot_text)

def _stripq(x: str) -> str:
    return x[1:-1] if x and x.startswith('"') and x.endswith('"') else x

def _is_call_node(attrs: str) -> bool:
    """
    Node yang jelas milik call graph:
    - label=call (ikon legenda)
    - atau shape=tab + warna ungu (#E552FF) yang dipakai node 'fib', 'range', 'next'
    """
    a = (attrs or "").lower()
    return (
        re.search(r'\blabel\s*=\s*"?call"?\b', a) is not None or
        (re.search(r'\bshape\s*=\s*tab\b', a) is not None and PURPLE_HEX in a)
    )

def _is_call_edge(attrs: str) -> bool:
    """
    Edge call graph biasanya bertanda label=calls (sering juga dashed).
    """
    a = (attrs or "").lower()
    return re.search(r'\blabel\s*=\s*"?calls"?\b', a) is not None

def clean_dot_safe(dot_text: str) -> str:
    stmts = _split_statements(dot_text)

    # 1) kumpulkan node yang perlu dihapus
    to_remove = set()
    for st in stmts:
        m = _NODE_STMT.match(st.strip())
        if not m:
            continue
        nid   = _stripq(m.group('id'))
        attrs = m.group('attrs') or ""
        if _is_call_node(attrs):
            to_remove.add(nid)

    # 2) bangun ulang: buang node tsb, edge yang menyentuhnya, dan edge "calls"
    kept = []
    for st in stmts:
        s = st.strip()
        if not s:
            continue

        nm = _NODE_STMT.match(s)
        if nm:
            nid = _stripq(nm.group('id'))
            if nid in to_remove:
                continue  # drop node
            kept.append(st)
            continue

        em = _EDGE_STMT.match(s)
        if em:
            src  = em.group('src')
            dst  = em.group('dst')
            attrs = em.group('attrs') or ""
            if src in to_remove or dst in to_remove:
                continue  # drop edge yg menyentuh node call-graph
            if _is_call_edge(attrs):
                continue  # drop edge 'calls'
            kept.append(st)
            continue

        # statement lain (graph attrs, subgraph, dll) tetap
        kept.append(st)

    return "\n".join(kept)
# =================== end SAFE DOT cleaner ===================


def parse_code(code):
    """Parse Python code and extract class, function, and main code information."""
    tree = ast.parse(code)
    result = {'class': [], 'function': [], 'main': ''}
    main_code = []

    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            result['function'].append(node.name)
        elif isinstance(node, ast.ClassDef):
            class_data = {
                'classname': node.name,
                'method': [n.name for n in node.body if isinstance(n, ast.FunctionDef)]
            }
            result['class'].append(class_data)
        else:
            # membutuhkan Python 3.9+
            main_code.append(ast.unparse(node))

    result['main'] = "\n".join(main_code)
    return result


def generate_graphviz(code, base_filename, output_dir):
    """Bangun CFG (DOT) lalu bersihkan bagian call-graph sebelum dikembalikan."""
    os.makedirs(output_dir, exist_ok=True)

    cfg_builder = CFGBuilder()
    cfg = cfg_builder.build_from_src(base_filename, code)

    output_path = os.path.join(output_dir, base_filename)
    cfg.build_visual(output_path, 'dot', show=False)

    dot_file = output_path + '.dot'
    with open(dot_file, 'r', encoding='utf-8') as f:
        raw_dot = f.read()

    cleaned_dot = clean_dot_safe(raw_dot)

    # opsional: simpan yang sudah bersih supaya downstream konsisten
    with open(dot_file, 'w', encoding='utf-8') as f:
        f.write(cleaned_dot)

    return cleaned_dot


@method_bp.route('/method', methods=['POST'])
def method():
    try:
        data = request.get_json(silent=True) or {}
        code = data.get('code', '')
        if not code.strip():
            return jsonify({'error': 'No code provided'}), 400

        public_dir = os.path.join(os.getcwd(), "backend", "public")
        os.makedirs(public_dir, exist_ok=True)

        files_to_delete = []

        try:
            unique_id = uuid.uuid4().hex
            base_filename = f'cfg_{unique_id}'
            dot_file_path = os.path.join(public_dir, base_filename + '.dot')
            files_to_delete.append(dot_file_path)

            # DOT utama (sudah dibersihkan)
            dot_content = generate_graphviz(code, base_filename, public_dir)

            # Parse struktur class/function/main
            types = parse_code(code)

            # Build koleksi class & function
            parser = GraphParser.GraphParser(dot_content, types=types)
            collection_method = parser.collectionMethod()
            collection_function = parser.collectionFunction()

            # (opsional) build visual main code
            collection_main = None
            if types['main'].strip():
                main_filename_base = f'cfg_{uuid.uuid4().hex}'
                main_dot_path = os.path.join(public_dir, main_filename_base + '.dot')
                files_to_delete.append(main_dot_path)

                main_dot = generate_graphviz(types['main'], main_filename_base, public_dir)
                parser_main = GraphParser.GraphParser(main_dot, types=None)
                collection_main = graphviz.Source(parser_main.graphViz(), format='svg').pipe().decode('utf-8')

            return jsonify({
                'class': collection_method,
                'function': collection_function,
                'mainCode': collection_main,
            })

        except Exception as e:
            return jsonify({'error': 'Failed to process code', 'details': str(e)}), 400

        finally:
            # bersihkan file temp jika ada
            for file_path in files_to_delete:
                try:
                    if os.path.exists(file_path):
                        os.remove(file_path)
                except Exception as e:
                    print(f"Error deleting file {file_path}: {e}")

    except Exception as e:
        return jsonify({'error': str(e)}), 500
