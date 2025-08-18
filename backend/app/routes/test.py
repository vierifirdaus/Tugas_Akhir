# routes/test.py
import re
from pathlib import Path

PURPLE_HEX = "#e552ff"

def _extract_subgraphs(dot_text: str):
    """Kembalikan list blok subgraph lengkap (start, end, text) dgn brace-balancing."""
    items, i, n = [], 0, len(dot_text)
    while True:
        m = re.search(r'\bsubgraph\b', dot_text[i:])
        if not m:
            break
        start_kw = i + m.start()
        m2 = re.search(r'\{', dot_text[start_kw:])
        if not m2:
            break
        brace_start = start_kw + m2.start()
        depth, j = 0, brace_start
        while j < n:
            ch = dot_text[j]
            if ch == '{': depth += 1
            elif ch == '}':
                depth -= 1
                if depth == 0:
                    end = j + 1
                    items.append((start_kw, end, dot_text[start_kw:end]))
                    i = end
                    break
            j += 1
    return items

def _collect_node_ids(block_text: str):
    """Ambil semua ID node yg didefinisikan di dalam block DOT."""
    ids = set()
    for m in re.finditer(r'^\s*(?P<id>"[^"]+"|[A-Za-z0-9_]+)\s*\[.*?\];', block_text, flags=re.S | re.M):
        nid = m.group('id')
        if nid.startswith('"') and nid.endswith('"'):
            nid = nid[1:-1]
        ids.add(nid)
    return ids

def _find_nodes_by_attr(dot_text: str, predicate):
    """Temukan ID node yang memenuhi predicate(attrs_text_lower)."""
    ids = set()
    pat = re.compile(r'^\s*(?P<id>"[^"]+"|[A-Za-z0-9_]+)\s*\[(?P<attrs>.*?)\];', flags=re.S | re.M)
    for m in pat.finditer(dot_text):
        nid = m.group('id')
        attrs = m.group('attrs')
        if predicate(attrs.lower()):
            if nid.startswith('"') and nid.endswith('"'):
                nid = nid[1:-1]
            ids.add(nid)
    return ids

def _remove_nodes_edges_and_blocks(dot_text: str) -> str:
    # 1) Hapus seluruh subgraph berwarna purple
    subgraphs = _extract_subgraphs(dot_text)
    to_delete_spans = []
    purple_nodes = set()
    for s, e, text in subgraphs:
        if re.search(r'\bcolor\s*=\s*purple\b', text, flags=re.I):
            to_delete_spans.append((s, e))
            purple_nodes |= _collect_node_ids(text)

    # 2) Node dgn warna ungu (#E552FF) atau label=call
    colored_nodes = _find_nodes_by_attr(dot_text, lambda a: PURPLE_HEX in a)
    label_call_nodes = _find_nodes_by_attr(dot_text, lambda a: re.search(r'label\s*=\s*"?call"?\b', a, flags=re.I))

    remove_nodes = purple_nodes | colored_nodes | label_call_nodes

    # 3) Potong blok subgraph purple
    if to_delete_spans:
        for s, e in sorted(to_delete_spans, reverse=True):
            dot_text = dot_text[:s] + dot_text[e:]

    # 4) Hapus node & edge yang menyentuh node yang dihapus
    statements = re.split(r'(?<=;)\s*\n', dot_text)
    out = []
    node_stmt = re.compile(r'^\s*(?P<id>"[^"]+"|[A-Za-z0-9_]+)\s*\[.*?\];\s*$', flags=re.S | re.M)
    edge_stmt = re.compile(r'\s*"?(?P<src>[^"\s\[]+)"?\s*->\s*"?(?P<dst>[^"\s\[]+)"?')
    def _stripq(x): return x[1:-1] if x.startswith('"') and x.endswith('"') else x

    for st in statements:
        if not st.strip():
            continue
        m = node_stmt.match(st.strip())
        if m:
            nid = _stripq(m.group('id'))
            if nid in remove_nodes:
                continue  # drop node
        em = edge_stmt.search(st)
        if em:
            if em.group('src') in remove_nodes or em.group('dst') in remove_nodes:
                continue  # drop edge
        out.append(st)
    return "\n".join(out)

def clean_dot_calls(in_path: str, out_path: str) -> None:
    """Baca DOT dari in_path, hapus node ungu/call-graph, tulis ke out_path."""
    src = Path(in_path)
    dst = Path(out_path)
    dot_text = src.read_text(encoding="utf-8")
    cleaned = _remove_nodes_edges_and_blocks(dot_text)
    dst.write_text(cleaned, encoding="utf-8")
    print(f"✅ Bersih. Output ditulis ke: {dst.resolve()}")

if __name__ == "__main__":
    # Jalankan: python routes/test.py
    # Input:  routes/tes.dot
    # Output: routes/out.dot
    clean_dot_calls("routes/tes.dot", "routes/out.dot")
