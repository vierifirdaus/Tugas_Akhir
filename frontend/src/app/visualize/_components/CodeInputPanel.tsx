// src/app/method/_components/CodeInputPanel.tsx
'use client';

import React, { useState, useCallback, useEffect, useRef, ChangeEvent } from 'react';
import Editor, { Monaco, OnChange } from '@monaco-editor/react';
import { ChevronLeftIcon, ChevronRightIcon } from 'lucide-react';
import { editor } from 'monaco-editor';
import { toast } from 'react-toastify';

// Definisikan tipe untuk jenis graf yang dipilih
export type SelectedGraphTypes = Record<string, boolean>;

interface CodeInputPanelProps {
  defaultCode?: string;
  onVisualizeClick: (code: string, selectedGraphTypes: SelectedGraphTypes) => void; // Diperbarui
  isVisualizing: boolean;
  visualizationError: string | null;
  initialPanelWidth?: number;
  minPanelWidth?: number;
  maxPanelWidth?: number;
}

const MIN_PANEL_WIDTH_DEFAULT = 300;
const DEFAULT_PANEL_WIDTH_DEFAULT = 400;
const MAX_PANEL_WIDTH_DEFAULT = 700;

const AVAILABLE_GRAPH_TYPES = [
  { id: 'CFG', label: 'Control Flow Graph (CFG)' },
  { id: 'CG', label: 'Call Graph (CG)' },
  { id: 'PDG', label: 'Program Dependency Graph (PDG)' },
];

const CodeInputPanel: React.FC<CodeInputPanelProps> = ({
  defaultCode = '',
  onVisualizeClick,
  isVisualizing,
  visualizationError,
  initialPanelWidth = DEFAULT_PANEL_WIDTH_DEFAULT,
  minPanelWidth = MIN_PANEL_WIDTH_DEFAULT,
  maxPanelWidth = MAX_PANEL_WIDTH_DEFAULT,
}) => {
  const [pythonCode, setPythonCode] = useState<string>(defaultCode);
  const [panelWidth, setPanelWidth] = useState<number>(initialPanelWidth);
  const [isPanelCollapsed, setIsPanelCollapsed] = useState<boolean>(false);
  const [isResizing, setIsResizing] = useState<boolean>(false);
  const [selectedGraphTypes, setSelectedGraphTypes] = useState<SelectedGraphTypes>(() => {
    // Inisialisasi semua jenis graf sebagai tidak terpilih (false)
    const initialTypes: SelectedGraphTypes = {};
    AVAILABLE_GRAPH_TYPES.forEach(type => {
      initialTypes[type.id] = false;
    });
    return initialTypes;
  });

  const sidebarRef = useRef<HTMLDivElement>(null);
  const monacoInstanceRef = useRef<Monaco | null>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);

  const startResizing = useCallback((e: React.MouseEvent) => {
    e.preventDefault();
    setIsResizing(true);
  }, []);

  const stopResizing = useCallback(() => {
    setIsResizing(false);
  }, []);

  const resizePanel = useCallback((e: MouseEvent) => {
    if (isResizing) {
      const newWidth = e.clientX;
      if (newWidth >= minPanelWidth && newWidth <= maxPanelWidth) {
        setPanelWidth(newWidth);
      } else if (newWidth < minPanelWidth) {
        setPanelWidth(minPanelWidth);
      } else {
        setPanelWidth(maxPanelWidth);
      }
    }
  }, [isResizing, minPanelWidth, maxPanelWidth]);

  useEffect(() => {
    if (isResizing) {
      document.body.style.cursor = 'col-resize';
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

  const togglePanelCollapse = () => {
    setIsPanelCollapsed(!isPanelCollapsed);
    if (isPanelCollapsed && panelWidth < minPanelWidth) {
      setPanelWidth(initialPanelWidth);
    }
  };

  const handleEditorChange: OnChange = (value) => {
    setPythonCode(value || '');
  };

  const handleGraphTypeChange = (graphTypeId: string) => {
    setSelectedGraphTypes(prev => ({
      ...prev,
      [graphTypeId]: !prev[graphTypeId],
    }));
  };

  const handleSubmit = () => {
    // Pastikan setidaknya satu jenis graf dipilih
    const GraphTerpilih = Object.values(selectedGraphTypes).some(isSelected => isSelected);
    if (!GraphTerpilih) {
        toast.error('Harap pilih setidaknya satu jenis graf!', {
          position: "top-center",
          autoClose: 5000,
          hideProgressBar: false,
          closeOnClick: true,
          pauseOnHover: true,
          draggable: true,
          progress: undefined,
          theme: "light",
        });
        return;
    }
    onVisualizeClick(pythonCode, selectedGraphTypes);
  };

  function checkSelectedGraphTypes() {
    return selectedGraphTypes['CFG'] || selectedGraphTypes['CG'] || selectedGraphTypes['PDG'];
  }
  function isNullPythonCode() {
    return pythonCode === null || pythonCode.trim() === '';
  }
  const handleFileUpload = (event: ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (file) {
      if (!file.name.endsWith('.py')) {
        alert('Please upload a Python file (.py)');
        if(fileInputRef.current) fileInputRef.current.value = "";
        return;
      }
      const reader = new FileReader();
      reader.onload = (e) => {
        const text = e.target?.result as string;
        setPythonCode(text);
      };
      reader.readAsText(file);
      if(fileInputRef.current) fileInputRef.current.value = "";
    }
  };

  const triggerFileInput = () => {
    fileInputRef.current?.click();
  };

  const editorOptions = {
    minimap: { enabled: true },
    wordWrap: 'on' as const,
    fontSize: 13,
    scrollBeyondLastLine: false,
    automaticLayout: true,
    padding: { top: 10, bottom: 10 },
    tabSize: 2,
  };

  function handleEditorDidMount(editor:editor.IStandaloneCodeEditor, monaco: Monaco) {
    monacoInstanceRef.current = monaco;
  }

  return (
    <>
      {isPanelCollapsed && (
        <button
          onClick={togglePanelCollapse}
          className="fixed top-3 left-3 z-20 p-2 bg-blue-600 text-white rounded-md shadow-lg hover:bg-blue-700 transition-colors focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50"
          title="Show Code Panel"
        >
          <ChevronRightIcon size={20} />
        </button>
      )}
      <div
        ref={sidebarRef}
        className={`bg-white flex flex-col transition-all duration-200 ease-in-out relative
                    ${isPanelCollapsed ? 'w-0 p-0 border-none overflow-hidden' : 'p-5 border-r border-slate-300 shadow-lg'}`}
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

            <div className="flex items-center mb-2 flex-shrink-0">
              <label htmlFor="pythonCodeInput" className="text-sm font-medium text-slate-600">
                Paste code or
              </label>
              <input
                type="file"
                ref={fileInputRef}
                onChange={handleFileUpload}
                accept=".py"
                className="hidden"
              />
              <button
                type="button"
                onClick={triggerFileInput}
                className="ml-2 text-sm text-blue-600 hover:text-blue-800 font-medium focus:outline-none underline"
              >
                upload a .py file
              </button>
            </div>

            <div className="flex flex-col flex-grow min-h-0">
              <div className="flex-grow border border-slate-300 rounded-md shadow-sm overflow-hidden relative">
                <Editor
                  height="100%"
                  language="python"
                  theme="vs"
                  value={pythonCode}
                  options={editorOptions}
                  onChange={handleEditorChange}
                  onMount={handleEditorDidMount}
                  loading={<div className="p-4 text-slate-500">Loading editor...</div>}
                />
              </div>
            </div>

            {/* Pilihan Jenis Graf */}
            <div className="mt-4 flex-shrink-0">
              <h3 className="text-sm font-medium text-slate-700 mb-2">Pilih Jenis Graf (bisa lebih dari satu):</h3>
              <div className="space-y-2">
                {AVAILABLE_GRAPH_TYPES.map((graphType) => (
                  <label key={graphType.id} className="flex items-center space-x-2 cursor-pointer">
                    <input
                      type="checkbox"
                      className="form-checkbox h-4 w-4 text-blue-600 border-slate-300 rounded focus:ring-blue-500"
                      checked={selectedGraphTypes[graphType.id]}
                      onChange={() => handleGraphTypeChange(graphType.id)}
                    />
                    <span className="text-sm text-slate-600">{graphType.label}</span>
                  </label>
                ))}
              </div>
            </div>

            <button
              type="button"
              onClick={handleSubmit}
              className={`mt-4 w-full py-2.5 px-4 rounded-md font-semibold text-white flex-shrink-0
                          bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2
                          focus:ring-blue-500 focus:ring-opacity-50 transition-colors duration-150
                          disabled:bg-slate-400 disabled:cursor-not-allowed`}
              disabled={isVisualizing || checkSelectedGraphTypes() === false || isNullPythonCode() === true}
            >
              {isVisualizing ? 'Visualizing...' : 'Visualize'}
            </button>
            {visualizationError && (
              <div className="mt-3 p-2.5 bg-red-100 border border-red-300 text-red-700 rounded-md text-sm flex-shrink-0">
                <strong>Error:</strong> {visualizationError}
              </div>
            )}
            <p className="text-xs text-slate-500 mt-auto pt-4 flex-shrink-0">
              Enter Python code to see its class and method structure visualized.
            </p>
          </>
        )}
      </div>
      {!isPanelCollapsed && (
        <div
          onMouseDown={startResizing}
          className="w-1.5 cursor-col-resize bg-slate-200 hover:bg-blue-500 active:bg-blue-600 transition-colors duration-150 flex-shrink-0"
          title="Resize panel"
        />
      )}
    </>
  );
};

export default CodeInputPanel;