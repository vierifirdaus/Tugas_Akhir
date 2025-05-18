'use client';

import React, { useEffect, useRef, useState } from 'react';
import Editor from '@monaco-editor/react';
import { Timestamp } from '../utils/Timestamp';

declare global {
  interface Window {
    $: any;
  }
}

export default function VisualizerPage() {
  const [sourceCode, setSourceCode] = useState("print('Hello, world!')");
  const [svgContent, setSvgContent] = useState<string | null>(null);
  const [editorTheme, setEditorTheme] = useState<'light' | 'vs-dark'>('vs-dark');
  const [leftWidth, setLeftWidth] = useState(600);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [showInputPanel, setShowInputPanel] = useState(true);
  const [scriptsLoaded, setScriptsLoaded] = useState(false);
  const [scriptError, setScriptError] = useState<string | null>(null);
  
  const graphContainerRef = useRef<HTMLDivElement>(null);
  const isDraggingResize = useRef(false);
  const startX = useRef(0);
  const startWidth = useRef(0);

  // Load scripts dynamically
  useEffect(() => {
    if (typeof window === 'undefined' || window.$) return;

    const loadScript = (src: string): Promise<void> => {
      return new Promise((resolve, reject) => {
        const script = document.createElement('script');
        script.src = src;
        script.async = true;
        
        script.onload = () => {
          console.log(`Successfully loaded: ${src}`);
          resolve();
        };
        
        script.onerror = () => {
          console.error(`Failed to load: ${src}`);
          reject(new Error(`Failed to load script: ${src}`));
        };

        document.body.appendChild(script);
      });
    };

    const loadGraphviz = async () => {
      try {
        console.log('Starting script loading...');
        
        // Load jQuery first
        await loadScript('https://code.jquery.com/jquery-2.1.3.min.js');
        console.log('jQuery loaded successfully');
        
        // Load dependencies
        await Promise.all([
          loadScript('https://cdnjs.cloudflare.com/ajax/libs/jquery-mousewheel/3.1.13/jquery.mousewheel.min.js'),
          loadScript('https://cdnjs.cloudflare.com/ajax/libs/jquery-color/2.1.2/jquery.color.min.js')
        ]);
        console.log('Dependencies loaded successfully');
        
        // Load Graphviz plugin
        
        await loadScript('/js/jquery.graphviz.svg.js');
        console.log('Graphviz plugin loaded successfully');
        
        setScriptsLoaded(true);
        setScriptError(null);
        
        // Initialize if SVG content is already available
        if (svgContent) {
          initializeGraphviz();
        }
      } catch (error) {
        console.error('Script loading error:', error);
        setScriptError(`Failed to load required scripts: ${error instanceof Error ? error.message : 'Unknown error'}`);
      }
    };

    loadGraphviz();

    return () => {
      // Cleanup if needed
    };
  }, []);

  // Initialize Graphviz when SVG content changes or scripts load
  useEffect(() => {
    if (scriptsLoaded && svgContent) {
      initializeGraphviz();
    }
  }, [svgContent, scriptsLoaded]);

  const initializeGraphviz = () => {
    if (!window.$ || !graphContainerRef.current) {
      console.error('jQuery or container not available');
      return;
    }

    try {
      console.log('Initializing Graphviz...');
      $(graphContainerRef.current).empty().graphviz({
        svg: svgContent,
        ready: function(this: any) {
          console.log('Graphviz initialized successfully');
          const gv = this;
          
          // Node click highlighting
          gv.nodes().click(function(this: any) {
            let $set = $(this);
            $set = $set.add(gv.linkedFrom(this, true));
            $set = $set.add(gv.linkedTo(this, true));
            gv.highlight($set, true);
            gv.bringToFront($set);
          });
          
          // ESC key to clear highlights
          $(document).keydown(function(evt: any) {
            if (evt.key === 'Escape') {
              gv.highlight();
            }
          });
        }
      });
    } catch (error) {
      console.error('Graphviz initialization error:', error);
      setError('Failed to initialize visualization');
    }
  };

  const handleVisualize = async () => {
    setIsLoading(true);
    setError(null);
    setScriptError(null);
    
    try {
      const response = await fetch('http://localhost:5000/source', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ code: sourceCode })
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const result = await response.json();
      
      if (result.error) {
        throw new Error(result.error);
      }

      setSvgContent(result.svg);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An unknown error occurred');
    } finally {
      setIsLoading(false);
    }
  };

  const handleFileUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    if (!file.name.endsWith('.py')) {
      alert('Hanya file .py yang diperbolehkan!');
      return;
    }

    const reader = new FileReader();
    reader.onload = (event) => {
      const text = event.target?.result as string;
      setSourceCode(text);
    };
    reader.readAsText(file);
  };

  const toggleTheme = () => {
    setEditorTheme(prev => (prev === 'vs-dark' ? 'light' : 'vs-dark'));
  };

  const handleResizeMouseDown = (e: React.MouseEvent) => {
    isDraggingResize.current = true;
    startX.current = e.clientX;
    startWidth.current = leftWidth;
    document.addEventListener('mousemove', handleResizeMouseMove);
    document.addEventListener('mouseup', handleResizeMouseUp);
  };

  const handleResizeMouseMove = (e: MouseEvent) => {
    if (!isDraggingResize.current) return;
    const newWidth = startWidth.current + (e.clientX - startX.current);
    setLeftWidth(Math.max(300, Math.min(newWidth, window.innerWidth - 300)));
  };

  const handleResizeMouseUp = () => {
    isDraggingResize.current = false;
    document.removeEventListener('mousemove', handleResizeMouseMove);
    document.removeEventListener('mouseup', handleResizeMouseUp);
  };

  const toggleInputPanel = () => {
    setShowInputPanel(!showInputPanel);
    if (!showInputPanel) {
      setLeftWidth(600);
    }
  };

  useEffect(() => {
    return () => {
      document.removeEventListener('mousemove', handleResizeMouseMove);
      document.removeEventListener('mouseup', handleResizeMouseUp);
    };
  }, []);

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col md:flex-row">
      {/* Header for mobile */}
      <div className="md:hidden bg-white p-4 shadow-md">
        <h1 className="text-xl font-bold text-gray-800">Python Visualizer</h1>
      </div>

      {/* Input Area */}
      {showInputPanel && (
        <>
          <div 
            style={{ width: `${leftWidth}px` }} 
            className="flex-1 bg-white shadow-lg rounded-lg m-2 md:m-4 p-4 md:p-6 overflow-hidden flex flex-col transition-all duration-200"
          >
            <div className="flex flex-col sm:flex-row sm:items-center justify-between mb-4 gap-2">
              <h2 className="text-xl md:text-2xl font-bold text-gray-800">Masukkan Kode Program</h2>
              <div className="flex gap-2">
                <label className="flex items-center px-3 py-1 bg-gray-100 hover:bg-gray-200 text-gray-700 rounded-lg cursor-pointer transition-colors">
                  <span className="mr-2 text-sm">Upload File</span>
                  <input
                    type="file"
                    accept=".py"
                    onChange={handleFileUpload}
                    className="hidden"
                  />
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
                  </svg>
                </label>
                <button
                  onClick={toggleTheme}
                  className="px-3 py-1 text-sm bg-gray-100 hover:bg-gray-200 text-gray-700 rounded-lg transition-colors flex items-center"
                >
                  <span className="mr-1">Tema:</span>
                  {editorTheme === 'vs-dark' ? (
                    <span className="flex items-center">
                      <span>Gelap</span>
                      <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 ml-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" />
                      </svg>
                    </span>
                  ) : (
                    <span className="flex items-center">
                      <span>Terang</span>
                      <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 ml-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
                      </svg>
                    </span>
                  )}
                </button>
              </div>
            </div>

            <div className="flex-1 overflow-hidden border border-gray-200 rounded-lg">
              <Editor
                height="100%"
                language="python"
                theme={editorTheme}
                value={sourceCode}
                onChange={(value) => setSourceCode(value || '')}
                options={{
                  fontSize: 14,
                  minimap: { enabled: false },
                  lineNumbers: 'on',
                  scrollBeyondLastLine: false,
                }}
              />
            </div>

            <button
              onClick={handleVisualize}
              disabled={isLoading}
              className={`mt-4 px-6 py-2 text-white rounded-lg shadow-md transition-colors flex items-center justify-center gap-2 ${
                isLoading ? 'bg-blue-400 cursor-not-allowed' : 'bg-blue-600 hover:bg-blue-700'
              }`}
            >
              {isLoading ? (
                <>
                  <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  Processing...
                </>
              ) : (
                <>
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                  </svg>
                  <span>Visualisasikan</span>
                </>
              )}
            </button>

            {error && (
              <div className="mt-2 text-red-500 text-sm">
                {error}
              </div>
            )}
          </div>

          {/* Resizer */}
          <div
            onMouseDown={handleResizeMouseDown}
            className="hidden md:block w-2 cursor-col-resize bg-gray-300 hover:bg-gray-400 active:bg-gray-500 transition-colors"
          />
        </>
      )}

      {/* Output Area */}
      <div className={`bg-white shadow-lg rounded-lg m-2 md:m-4 p-4 md:p-6 overflow-hidden flex flex-col ${
        showInputPanel ? 'flex-1' : 'w-full'
      }`}>
        <div className="flex justify-between items-center mb-4">
          <div className="flex items-center gap-4">
            <button
              onClick={toggleInputPanel}
              className="p-2 rounded hover:bg-gray-100 transition-colors"
              title={showInputPanel ? "Hide code panel" : "Show code panel"}
            >
              {showInputPanel ? (
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
                </svg>
              ) : (
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                </svg>
              )}
            </button>
            <h2 className="text-xl md:text-2xl font-bold text-gray-800">Visualisasi</h2>
          </div>
          
          <div className="text-sm text-gray-500">
            <Timestamp />
          </div>
        </div>

        {scriptError && (
          <div className="text-red-500 p-4 mb-4 border border-red-200 bg-red-50 rounded">
            <p className="font-bold">Script Loading Error:</p>
            <p>{scriptError}</p>
            <p className="mt-2 text-sm">Please refresh the page or check your network connection.</p>
          </div>
        )}
        
        <div 
          ref={graphContainerRef}
          className="flex-1 border-2 border-dashed border-gray-200 rounded-lg bg-gray-50 overflow-auto relative"
          style={{ minHeight: '500px' }}
        >
          {!svgContent && !scriptError && (
            <div className="absolute inset-0 flex items-center justify-center text-gray-500">
              <div className="text-center">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-12 w-12 mx-auto mb-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1} d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
                </svg>
                <p className="text-lg">Visualisasi akan muncul di sini</p>
                <p className="text-sm mt-1">Klik tombol "Visualisasikan" untuk melihat hasil</p>
              </div>
            </div>
          )}
        </div>
        <div className="text-sm text-gray-600 mt-2">
          Click node to highlight; Shift-scroll to zoom; Esc to unhighlight
        </div>
      </div>
    </div>
  );
}