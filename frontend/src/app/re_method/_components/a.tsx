// src/app/method/_components/FlowDisplay.tsx
'use client';

import React from 'react';
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
import { CustomNode, CustomEdge } from '@/types';

interface FlowDisplayProps {
  nodes: CustomNode[];
  edges: CustomEdge[];
  onNodesChange: OnNodesChange<CustomNode>;
  onEdgesChange: OnEdgesChange<CustomEdge>;
  nodeTypes: NodeTypes;
  isFlowLoading?: boolean; // Renamed from isLoading to be more specific
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
  return (
    <div className="flex-1 min-w-0 relative bg-graph-paper">
      <ReactFlow
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
      </ReactFlow>
    </div>
  );
};

export default FlowDisplay;
