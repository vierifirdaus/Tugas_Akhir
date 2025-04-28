'use client';

import React, { useEffect, useRef, useState } from 'react';
import Editor from '@monaco-editor/react';

function Timestamp() {
  const [date, setDate] = useState('');

  useEffect(() => {
    setDate(new Date().toLocaleString());
  }, []);

  return <div className="text-sm text-gray-500">{date}</div>;
}

export default function VisualizerPage() {
  const [sourceCode, setSourceCode] = useState("print('Hello, world!')");
  const [svgOutput, setSvgOutput] = useState("<svg><text x='10' y='20'>Visualisasi akan tampil di sini</text></svg>");
  const [editorTheme, setEditorTheme] = useState<'light' | 'vs-dark'>('vs-dark');
  const [leftWidth, setLeftWidth] = useState(600); // Default width for input panel
  const isDragging = useRef(false);

  const handleVisualize = () => {
    setSvgOutput(`<svg width='400' height='200'><text x='10' y='20'>${sourceCode}</text></svg>`);
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

  const handleMouseDown = () => {
    isDragging.current = true;
    document.addEventListener('mousemove', handleMouseMove);
    document.addEventListener('mouseup', handleMouseUp);
  };

  const handleMouseMove = (e: MouseEvent) => {
    if (!isDragging.current) return;
    setLeftWidth(Math.max(300, Math.min(e.clientX, window.innerWidth - 300))); // min 300px, max avoid overflow
  };

  const handleMouseUp = () => {
    isDragging.current = false;
    document.removeEventListener('mousemove', handleMouseMove);
    document.removeEventListener('mouseup', handleMouseUp);
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col md:flex-row">
      {/* Header for mobile */}
      <div className="md:hidden bg-white p-4 shadow-md">
        <h1 className="text-xl font-bold text-gray-800">Python Visualizer</h1>
      </div>

      {/* Input Area */}
      <div 
        style={{ width: `${leftWidth}px` }} 
        className="flex-1 bg-white shadow-lg rounded-lg m-2 md:m-4 p-4 md:p-6 overflow-hidden flex flex-col"
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
          className="mt-4 px-6 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg shadow-md transition-colors flex items-center justify-center gap-2"
        >
          <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
          </svg>
          <span>Visualisasikan</span>
        </button>
      </div>

      {/* Resizer */}
      <div
        onMouseDown={handleMouseDown}
        className="hidden md:block w-2 cursor-col-resize bg-gray-300 hover:bg-gray-400 active:bg-gray-500 transition-colors"
      />

      {/* Output Area */}
      <div className="flex-1 bg-white shadow-lg rounded-lg m-2 md:m-4 p-4 md:p-6 overflow-hidden flex flex-col">
        <div className="flex justify-between items-center mb-4">
          <h2 className="text-xl md:text-2xl font-bold text-gray-800">Visualisasi</h2>
          <div className="text-sm text-gray-500">
            <Timestamp />
          </div>
        </div>
        
        <div className="flex-1 border-2 border-dashed border-gray-200 rounded-lg bg-gray-50 flex items-center justify-center p-4 overflow-auto">
          {svgOutput.includes('Visualisasi akan tampil di sini') ? (
            <div className="text-center text-gray-500">
              <svg xmlns="http://www.w3.org/2000/svg" className="h-12 w-12 mx-auto mb-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1} d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
              </svg>
              <p className="text-lg">Visualisasi akan muncul di sini</p>
              <p className="text-sm mt-1">Klik tombol "Visualisasikan" untuk melihat hasil</p>
            </div>
          ) : (
            <div 
              className="w-full h-full flex items-center justify-center"
              dangerouslySetInnerHTML={{ __html: svgOutput }} 
            />
          )}
        </div>
      </div>
    </div>
  );
}