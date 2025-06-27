// src/app/method/_components/FlowDisplay.tsx
'use client';

// MODIFIKASI: Impor useEffect dan useRef dari React
import React, { useRef, useCallback, useState, useEffect } from 'react'; 
import {
  ReactFlow,
  MiniMap,
  Controls,
  Panel,
  NodeTypes,
  OnNodesChange,
  OnEdgesChange,
  FitViewOptions,
  ProOptions,
} from '@xyflow/react';
import { toPng, toSvg } from 'html-to-image';
import { BookText, DownloadIcon } from 'lucide-react';
import { CustomNode, CustomEdge } from '@/types';
import { LegendModal } from './Modal';

// BARU: Impor toast dari react-toastify
import { toast } from 'react-toastify';
// Pastikan Anda sudah mengimpor CSS-nya di file layout utama Anda, contoh:
// import 'react-toastify/dist/ReactToastify.css';


interface FlowDisplayProps {
  nodes: CustomNode[];
  edges: CustomEdge[];
  onNodesChange: OnNodesChange<CustomNode>;
  onEdgesChange: OnEdgesChange<CustomEdge>;
  nodeTypes: NodeTypes;
  isFlowLoading?: boolean;
  fitViewOptions?: FitViewOptions;
  proOptions?: ProOptions;
  onNodeClick?: (event: React.MouseEvent, node: CustomNode) => void;
}

const FlowDisplay: React.FC<FlowDisplayProps> = ({
  nodes,
  edges,
  onNodesChange,
  onEdgesChange,
  nodeTypes,
  isFlowLoading = false,
  fitViewOptions = { padding: 0.1, duration: 800 },
  proOptions = { hideAttribution: true },
  onNodeClick,
}) => {

  const [isLegendOpen, setIsLegendOpen] = useState(false);
  const reactFlowWrapperRef = useRef<HTMLDivElement>(null);
  
  // BARU: Ref untuk menyimpan ID dari toast yang sedang aktif
  const toastId = useRef<string | number | null>(null);

  // BARU: useEffect untuk menampilkan dan menyembunyikan toast
  useEffect(() => {
    if (isFlowLoading) {
      // Jika proses dimulai, tampilkan toast loading dan simpan ID-nya
      // saya ingin toast nya ditengah
      toastId.current = toast.loading("Processing flow visualization...", {
        position: "top-center",
        autoClose: false, // Jangan tutup otomatis
        closeButton: true,
      });
      } else {
      // Jika proses selesai, dan ada toast yang aktif
      if (toastId.current !== null) {
        // Update toast tersebut menjadi pesan sukses
        toast.update(toastId.current, { 
          position: "top-center",
          render: "Process completed successfully!", 
          type: "success", 
          isLoading: false,
          autoClose: 3000, // Tutup otomatis setelah 3 detik
          closeButton: true,
        });
        // Reset ref
        toastId.current = null;
      }
    }
  }, [isFlowLoading]);


  const handleDownload = useCallback(async (format: 'png' | 'svg') => {
    if (!reactFlowWrapperRef.current) {
        toast.error('Flow area not available.');
        return;
    }

    const viewportElement = reactFlowWrapperRef.current.querySelector('.react-flow__viewport') as HTMLElement;
    if (!viewportElement) {
        toast.error('React Flow viewport element not found.');
        return;
    }
    
    const toastDownloadId = toast.loading(`Generating ${format.toUpperCase()} file...`);

    try {
        let dataUrl;
        const filename = `visualization-${new Date().toISOString().slice(0,10)}.${format}`;

        if (format === 'png') {
            dataUrl = await toPng(viewportElement, { 
                cacheBust: true, 
                backgroundColor: '#f7f9fc',
                pixelRatio: 2
            });
        } else {
            dataUrl = await toSvg(viewportElement, { 
                cacheBust: true,
            });
        }

        const link = document.createElement('a');
        link.download = filename;
        link.href = dataUrl;
        document.body.appendChild(link); 
        link.click();
        document.body.removeChild(link);

        toast.update(toastDownloadId, {
            render: "Download successful!",
            type: "success",
            isLoading: false,
            autoClose: 3000,
        });

    } catch (error) {
        console.error(`Could not generate ${format.toUpperCase()}:`, error);
        toast.update(toastDownloadId, {
            position: "top-center",
            render: `Failed to download as ${format.toUpperCase()}.`,
            type: "error",
            isLoading: false,
            autoClose: 5000,
        });
    }
  }, []);


  return (
    <div className="flex-1 min-w-0 relative bg-graph-paper" ref={reactFlowWrapperRef}>
      <ReactFlow
        minZoom={0.2}
        maxZoom={4}
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        nodeTypes={nodeTypes}
        fitView
        fitViewOptions={fitViewOptions}
        proOptions={proOptions}
        onNodeClick={onNodeClick}
      >
        <MiniMap
          nodeStrokeWidth={3}
          zoomable
          pannable
          className="!bg-white !border !border-slate-300 !rounded-md !shadow-sm"
        />
        <Controls className="!shadow-lg" />
        <Panel position="top-right" className="!m-2">
            <div className="flex flex-col space-y-2 bg-white p-2 rounded-md shadow-lg border border-slate-200">
                <button 
                    onClick={() => handleDownload('png')}
                    className="flex items-center justify-center px-3 py-1.5 text-sm text-slate-700 bg-slate-100 hover:bg-slate-200 rounded-md transition-colors focus:outline-none focus:ring-2 focus:ring-blue-500"
                    title="Download as PNG"
                >
                    <DownloadIcon size={16} className="mr-2"/> PNG
                </button>
                <button 
                    onClick={() => handleDownload('svg')}
                    className="flex items-center justify-center px-3 py-1.5 text-sm text-slate-700 bg-slate-100 hover:bg-slate-200 rounded-md transition-colors focus:outline-none focus:ring-2 focus:ring-blue-500"
                    title="Download as SVG"
                >
                    <DownloadIcon size={16} className="mr-2"/> SVG
                </button>
                <button 
                    onClick={() => setIsLegendOpen(true)}
                    className="flex items-center justify-center px-3 py-1.5 text-sm text-slate-700 bg-slate-100 hover:bg-slate-200 rounded-md transition-colors focus:outline-none focus:ring-2 focus:ring-blue-500"
                    title="Tampilkan Legenda"
                >
                    <BookText size={16} className="mr-2"/> Legenda
                </button>
            </div>
        </Panel>
      </ReactFlow>
      {isLegendOpen && <LegendModal onClose={() => setIsLegendOpen(false)} />}
    </div>
  );
};

export default FlowDisplay;