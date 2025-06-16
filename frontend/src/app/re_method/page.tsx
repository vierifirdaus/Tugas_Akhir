// src/app/method/page.tsx
'use client';

import React, { useState, useMemo, useCallback } from 'react';
import {
  useNodesState,
  useEdgesState,
  OnNodesChange,
  OnEdgesChange,
  MarkerType,
} from '@xyflow/react';
import '@xyflow/react/dist/style.css';

import CodeInputPanel, { SelectedGraphTypes } from './_components/CodeInputPanel';
import FlowDisplay from './_components/FlowDisplay';
import SVGMethodNode from './_components/SVGMethodNode';
import ClassGroupNode from './_components/ClassGroupNode';

import { fetchCFG, fetchCallGraph } from '@/lib/api'; // Import fetchCallGraph
import { CustomNode, CustomEdge, VisualizeCodeResponse, CallGraphResponse, BackendClassItem, BackendClassResultType } from '@/types';
import { INITIAL_PYTHON_CODE } from '@/constants/codePythonConstants';
import { parseCFG } from './CFG';
import { parseCallGraph } from './CallGraph';

const DEFAULT_PANEL_WIDTH_CONST = 400;
const MIN_PANEL_WIDTH_CONST = 300;
const MAX_PANEL_WIDTH_CONST = 700;


export default function MethodVisualizationPage() {
  const [nodes, setNodes, onNodesChange] = useNodesState<CustomNode>([]);
  const [edges, setEdges, onEdgesChange] = useEdgesState<CustomEdge>([]);
  const [isLoadingApi, setIsLoadingApi] = useState<boolean>(false);
  const [apiError, setApiError] = useState<string | null>(null);

  const nodeTypes = useMemo(() => ({
    svgMethod: SVGMethodNode,
    classGroup: ClassGroupNode,
  }), []);

  const handleVisualize = useCallback(async (code: string, selectedGraphTypes: SelectedGraphTypes) => {
    setIsLoadingApi(true);
    setApiError(null);
    try {
      // 1. Ambil data visualisasi utama (node dan edge dasar)
      const response: VisualizeCodeResponse = await fetchCFG({ code });
      
      if (!response) {
        throw new Error('No result found in main API response.');
      }

      console.log("Response from main API:", response);
      
      const { nodes: parsedNodes, edges: parsedEdges } = parseCFG(response.class, response.function, response.mainCode);
      let combinedEdges = [...parsedEdges];

      if (selectedGraphTypes['CG']) {
        const callGraphResponse: CallGraphResponse = await fetchCallGraph({ code });
        const callGraphEdges = parseCallGraph(callGraphResponse);
        combinedEdges = [...combinedEdges, ...callGraphEdges];
      }

      console.log("Parsed Nodes:", parsedNodes);

      setNodes(parsedNodes);
      setEdges(combinedEdges);

    } catch (err: any) {
      console.error("Failed to visualize code:", err);
      setApiError(err.message || 'An unknown error occurred.');
      setNodes([]);
      setEdges([]);
    } finally {
      setIsLoadingApi(false);
    }
  }, [setNodes, setEdges]);

  return (
    <div className="flex h-screen w-screen bg-slate-100 font-sans overflow-hidden">
      <CodeInputPanel
        defaultCode={INITIAL_PYTHON_CODE}
        onVisualizeClick={handleVisualize}
        isVisualizing={isLoadingApi}
        visualizationError={apiError}
        initialPanelWidth={DEFAULT_PANEL_WIDTH_CONST}
        minPanelWidth={MIN_PANEL_WIDTH_CONST}
        maxPanelWidth={MAX_PANEL_WIDTH_CONST}
      />
      <FlowDisplay
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange as OnNodesChange<CustomNode>}
        onEdgesChange={onEdgesChange as OnEdgesChange<CustomEdge>}
        nodeTypes={nodeTypes}
        isFlowLoading={isLoadingApi}
      />
    </div>
  );
}