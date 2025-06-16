// src/app/method/_components/FlowDisplay.tsx
'use client';

import React, { useRef, useCallback } from 'react';
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
import { toPng, toSvg } from 'html-to-image'; // Impor dari html-to-image
import { DownloadIcon } from 'lucide-react'; // Ikon untuk tombol download
import { CustomNode, CustomEdge } from '@/types';

interface FlowDisplayProps {
  nodes: CustomNode[];
  edges: CustomEdge[];
  onNodesChange: OnNodesChange<CustomNode>;
  onEdgesChange: OnEdgesChange<CustomEdge>;
  nodeTypes: NodeTypes;
  isFlowLoading?: boolean;
  fitViewOptions?: FitViewOptions;
  proOptions?: ProOptions;
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
}) => {
  const reactFlowWrapperRef = useRef<HTMLDivElement>(null); // Ref untuk wrapper React Flow

  const handleDownload = useCallback(async (format: 'png' | 'svg') => {
    if (!reactFlowWrapperRef.current) {
      console.error('Flow area ref not available');
      return;
    }

    const viewportElement = reactFlowWrapperRef.current.querySelector('.react-flow__viewport') as HTMLElement;
    console.log('Viewport Element:', viewportElement);
    if (!viewportElement) {
        console.error('React Flow viewport element not found.');
        return;
    }
    
    let dataUrl;
    const filename = `visualization-${new Date().toISOString().slice(0,10)}.${format}`;
    console.log("cek 1")
    try {
      if (format === 'png') {
        dataUrl = await toPng(viewportElement, { 
            cacheBust: true, 
            backgroundColor: '#f7f9fc', // Sesuaikan dengan warna background graph-paper
            pixelRatio: 2 // Untuk kualitas lebih baik
        });
        console.log("cek 2")
      } else if (format === 'svg') {
        dataUrl = await toSvg(viewportElement, { 
            cacheBust: true,
        });
      } else {
        return;
      }

      const link = document.createElement('a');
      link.download = filename;
      link.href = dataUrl;
      document.body.appendChild(link); 
      link.click();
      document.body.removeChild(link);

    } catch (error) {
      console.error(`Could not generate ${format.toUpperCase()}:`, error);
      alert(`Failed to download as ${format.toUpperCase()}. Check console for details.`);
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
      >
        <MiniMap
          nodeStrokeWidth={3}
          zoomable
          pannable
          className="!bg-white !border !border-slate-300 !rounded-md !shadow-sm"
        />
        <Controls className="!shadow-lg" />
        {isFlowLoading && (
          <Panel position="top-center">
            <div className="px-3 py-1.5 bg-blue-500 text-white rounded-md shadow-lg text-sm">
              Processing...
            </div>
          </Panel>
        )}
        {/* Panel untuk tombol Download */}
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
            </div>
        </Panel>
      </ReactFlow>
    </div>
  );
};

export default FlowDisplay;