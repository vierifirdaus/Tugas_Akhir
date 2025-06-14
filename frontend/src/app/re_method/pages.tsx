'use client'; 
import React, { useState, useMemo, useCallback, FormEvent, useEffect, useRef } from 'react';
import Editor, { Monaco } from '@monaco-editor/react'; // Import Monaco Editor
import {
  ReactFlow,
  MiniMap,
  Controls,
  useNodesState,
  useEdgesState,
  OnNodesChange,
  OnEdgesChange,
  Panel, // Untuk UI tambahan di atas flow
} from '@xyflow/react';
import { ChevronLeftIcon, SidebarIcon } from 'lucide-react'; // Menggunakan Lucide icons
import '@xyflow/react/dist/style.css'; // Style dasar React Flow

// Import komponen custom node
import SVGMethodNode from './_components/SVGMethodNode';
import ClassGroupNode from './_components/ClassGroupNode';

// Import utilitas dan tipe
import { parseBackendResultToFlow } from '@/lib/flowUtils';
import { visualizePythonCode } from '@/lib/api';
import { CustomNode, CustomEdge, VisualizeCodeResponse, BackendResultType } from '@/types';
import { DEFAULT_PANEL_WIDTH, MAX_PANEL_WIDTH, MIN_PANEL_WIDTH } from '@/constants/pageConstants';

// Komponen Utama Halaman
export default function MethodVisualizationPage() {
  // State untuk input kode Python
  const [pythonCode, setPythonCode] = useState<string>('class MyClass:\n  def my_method(self, param1):\n    print(f"Hello {param1}")\n    return True'); // Contoh kode awal
  // State untuk nodes dan edges React Flow
  const [nodes, setNodes, onNodesChange] = useNodesState<CustomNode>([]);
  const [edges, setEdges, onEdgesChange] = useEdgesState<CustomEdge>([]);
  // State untuk loading dan error
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  // State untuk panel resizable
  const [panelWidth, setPanelWidth] = useState<number>(DEFAULT_PANEL_WIDTH);
  const [isPanelCollapsed, setIsPanelCollapsed] = useState<boolean>(false);
  const [isResizing, setIsResizing] = useState<boolean>(false);
  const sidebarRef = useRef<HTMLDivElement>(null); // Ref untuk sidebar
  const monacoInstanceRef = useRef<Monaco | null>(null); // Ref untuk instance Monaco

  // Mendefinisikan tipe node kustom untuk React Flow
  const nodeTypes = useMemo(() => ({
    svgMethod: SVGMethodNode,
    classGroup: ClassGroupNode,
  }), []);

  // Fungsi untuk memulai resizing panel
  const startResizing = useCallback((e: React.MouseEvent) => {
    e.preventDefault();
    setIsResizing(true);
  }, []);

  // Fungsi untuk menghentikan resizing panel
  const stopResizing = useCallback(() => {
    setIsResizing(false);
  }, []);

  // Fungsi untuk mengubah ukuran panel saat mouse bergerak
  const resizePanel = useCallback((e: MouseEvent) => {
    if (isResizing && sidebarRef.current) {
      // Hitung lebar baru berdasarkan posisi mouse relatif terhadap sisi kiri viewport
      // Ini lebih stabil jika panel itu sendiri adalah anak langsung dari elemen yang lebarnya dihitung
      const newWidth = e.clientX;
      if (newWidth >= MIN_PANEL_WIDTH && newWidth <= MAX_PANEL_WIDTH) {
        setPanelWidth(newWidth);
      } else if (newWidth < MIN_PANEL_WIDTH) {
        setPanelWidth(MIN_PANEL_WIDTH);
      } else {
        setPanelWidth(MAX_PANEL_WIDTH);
      }
    }
  }, [isResizing]);

  // Efek untuk menambahkan dan menghapus event listener global untuk resizing
  useEffect(() => {
    if (isResizing) {
      document.body.style.cursor = 'col-resize'; // Ubah cursor saat resizing
      window.addEventListener('mousemove', resizePanel);
      window.addEventListener('mouseup', stopResizing);
    } else {
      document.body.style.cursor = 'default';
      window.removeEventListener('mousemove', resizePanel);
      window.removeEventListener('mouseup', stopResizing);
    }
    return () => {
      document.body.style.cursor = 'default';
      window.removeEventListener('mousemove', resizePanel);
      window.removeEventListener('mouseup', stopResizing);
    };
  }, [isResizing, resizePanel, stopResizing]);

  // Fungsi untuk toggle collapse/expand panel
  const togglePanelCollapse = () => {
    setIsPanelCollapsed(!isPanelCollapsed);
    if (isPanelCollapsed && panelWidth < MIN_PANEL_WIDTH) {
        setPanelWidth(DEFAULT_PANEL_WIDTH);
    }
  };

  // Handler untuk perubahan pada Monaco Editor
  const handleEditorChange = (value: string | undefined) => {
    setPythonCode(value || '');
  };

  // Fungsi untuk menangani submit form
  const handleSubmitCode = useCallback(async (event?: FormEvent<HTMLFormElement>) => { // Event opsional karena bisa dipanggil dari tombol
    event?.preventDefault();
    setIsLoading(true);
    setError(null);

    try {
      const response: VisualizeCodeResponse = await visualizePythonCode({ code: pythonCode });
      if (response.result) {
        const { nodes: parsedNodes, edges: parsedEdges } = parseBackendResultToFlow(response.result as BackendResultType);
        setNodes(parsedNodes);
        setEdges(parsedEdges);
      } else {
        setError('No result found in API response.');
        setNodes([]);
        setEdges([]);
      }
    } catch (err: any) {
      console.error("Failed to visualize code:", err);
      setError(err.message || 'An unknown error occurred.');
      setNodes([]);
      setEdges([]);
    } finally {
      setIsLoading(false);
    }
  }, [pythonCode, setNodes, setEdges]);

  // Opsi untuk Monaco Editor
  const editorOptions = {
    minimap: { enabled: true },
    wordWrap: 'on' as const, // 'on' | 'off' | 'wordWrapColumn' | 'bounded'
    fontSize: 13,
    scrollBeyondLastLine: false,
    automaticLayout: true, // Penting untuk editor di dalam kontainer yang bisa berubah ukuran
    padding: {
        top: 10,
        bottom: 10
    },
    tabSize: 2,
  };

  // Handler ketika editor selesai mounting
  function handleEditorDidMount(editor: any, monaco: Monaco) {
    monacoInstanceRef.current = monaco;
    // Anda bisa melakukan kustomisasi lebih lanjut di sini, misalnya tema
    // monaco.editor.defineTheme('myCustomTheme', {
    //   base: 'vs', // can be vs, vs-dark, hc-black
    //   inherit: true, // can also be false to define everything from scratch
    //   rules: [],
    //   colors: {
    //     'editor.foreground': '#000000',
    //   },
    // });
    // monaco.editor.setTheme('myCustomTheme');
  }


  return (
    <div className="flex h-screen w-screen bg-slate-100 font-sans overflow-hidden">
      {/* Tombol untuk toggle panel jika collapsed */}
      {isPanelCollapsed && (
        <button
          onClick={togglePanelCollapse}
          className="fixed top-3 left-3 z-20 p-2 bg-blue-600 text-white rounded-md shadow-lg hover:bg-blue-700 transition-colors focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50"
          title="Show Code Panel"
        >
          <SidebarIcon size={20} />
        </button>
      )}

      {/* Panel Input Kode (Sidebar Kiri) */}
      <div
        ref={sidebarRef}
        className={`bg-white flex flex-col transition-all duration-200 ease-in-out relative
                    ${isPanelCollapsed ? 'w-0 p-0 border-none' : 'p-5 border-r border-slate-300 shadow-lg'}`}
        style={{ width: isPanelCollapsed ? 0 : panelWidth }}
      >
        {!isPanelCollapsed && (
          <>
            <div className="flex items-center justify-between mb-4 flex-shrink-0">
              <h1 className="text-xl font-semibold text-slate-700">Python Code Visualizer</h1>
              <button
                onClick={togglePanelCollapse}
                className="p-1.5 text-slate-600 hover:bg-slate-200 rounded-md focus:outline-none focus:ring-1 focus:ring-slate-400"
                title="Hide Code Panel"
              >
                <ChevronLeftIcon size={20} />
              </button>
            </div>

            {/* Kontainer untuk Editor agar flex-grow bekerja dengan baik */}
            <div className="flex flex-col flex-grow min-h-0">
              <label htmlFor="pythonCodeInput" className="text-sm font-medium text-slate-600 mb-1 flex-shrink-0">
                Paste your Python code here:
              </label>
              {/* Wrapper untuk Monaco Editor dengan border dan shadow */}
              <div className="flex-grow border border-slate-300 rounded-md shadow-sm overflow-hidden relative">
                <Editor
                  height="100%" // Editor akan mengisi tinggi wrapper
                  language="python"
                  theme="vs" // Tema default: 'vs' (light), 'vs-dark', 'hc-black'
                  value={pythonCode}
                  options={editorOptions}
                  onChange={handleEditorChange}
                  onMount={handleEditorDidMount}
                  loading={<div className="p-4 text-slate-500">Loading editor...</div>}
                />
              </div>
            </div>

            <button
              type="button" // Ganti type menjadi button jika tidak di dalam form, atau biarkan submit jika form masih ada
              onClick={() => handleSubmitCode()} // Panggil handleSubmitCode tanpa event form
              className={`mt-4 w-full py-2.5 px-4 rounded-md font-semibold text-white flex-shrink-0
                          bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2
                          focus:ring-blue-500 focus:ring-opacity-50 transition-colors duration-150
                          disabled:bg-slate-400 disabled:cursor-not-allowed`}
              disabled={isLoading}
            >
              {isLoading ? 'Visualizing...' : 'Visualize'}
            </button>
            {error && (
              <div className="mt-3 p-2.5 bg-red-100 border border-red-300 text-red-700 rounded-md text-sm flex-shrink-0">
                <strong>Error:</strong> {error}
              </div>
            )}
            <p className="text-xs text-slate-500 mt-auto pt-4 flex-shrink-0">
              Enter Python code to see its class and method structure visualized.
            </p>
          </>
        )}
      </div>

      {/* Resizer Handle */}
      {!isPanelCollapsed && (
        <div
          onMouseDown={startResizing}
          className="w-1.5 cursor-col-resize bg-slate-200 hover:bg-blue-500 active:bg-blue-600 transition-colors duration-150 flex-shrink-0"
          title="Resize panel"
        />
      )}

      {/* Area React Flow (Konten Utama) */}
      <div className="flex-1 min-w-0 relative bg-graph-paper">
        <ReactFlow
          nodes={nodes}
          edges={edges}
          onNodesChange={onNodesChange as OnNodesChange<CustomNode>}
          onEdgesChange={onEdgesChange as OnEdgesChange<CustomEdge>}
          nodeTypes={nodeTypes}
          fitView
          fitViewOptions={{ padding: 0.1, duration: 800 }}
          proOptions={{ hideAttribution: true }}
        >
          <MiniMap
            nodeStrokeWidth={3}
            zoomable
            pannable
            className="!bg-white !border !border-slate-300 !rounded-md !shadow-sm"
          />
          <Controls className="!shadow-lg" />
          {isLoading && (
            <Panel position="top-center">
              <div className="px-3 py-1.5 bg-blue-500 text-white rounded-md shadow-lg text-sm">
                Processing...
              </div>
            </Panel>
          )}
        </ReactFlow>
      </div>
    </div>
  );
}
