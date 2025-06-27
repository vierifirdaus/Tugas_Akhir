// src/app/method/page.tsx
'use client';

import React, { useState, useMemo, useCallback } from 'react';
import {
  useNodesState,
  useEdgesState,
  OnNodesChange,
  OnEdgesChange,
  Node,
} from '@xyflow/react';
import '@xyflow/react/dist/style.css';

import CodeInputPanel, { SelectedGraphTypes } from './_components/CodeInputPanel';
import FlowDisplay from './_components/FlowDisplay';
import SVGMethodNode from './_components/SVGMethodNode';
import ClassGroupNode from './_components/ClassGroupNode';

import { fetchAttributes, fetchCFG, fetchCallGraph, fetchPDG } from '@/lib/api';
import { CustomNode, CustomEdge} from '@/types';
import { INITIAL_PYTHON_CODE } from '@/constants/codePythonConstants';
import { parseCFG } from './CFG';
import { parseCallGraph } from './CallGraph';
import { parsePDG } from './PDG';
import DetailsSidebar from './_components/DetailSidebar';

import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

const DEFAULT_PANEL_WIDTH = 400;
const MIN_PANEL_WIDTH = 300;
const MAX_PANEL_WIDTH = 700;

export default function MethodVisualizationPage() {
  const [nodes, setNodes, onNodesChange] = useNodesState<CustomNode>([]);
  const [edges, setEdges, onEdgesChange] = useEdgesState<CustomEdge>([]);
  const [isLoadingApi, setIsLoadingApi] = useState<boolean>(false);
  const [apiError, setApiError] = useState<string | null>(null);
  const [selectedNode, setSelectedNode] = useState<CustomNode | null>(null);

  const nodeTypes = useMemo(() => ({
    svgMethod: SVGMethodNode,
    classGroup: ClassGroupNode,
  }), []);

  const handleVisualize = useCallback(async (code: string, selectedGraphTypes: SelectedGraphTypes) => {
    setIsLoadingApi(true);
    setApiError(null);
    setSelectedNode(null);
    
    try {
      const [cfgResponse, attributesResponse] = await Promise.all([
        fetchCFG({ code }).catch(err => {
          throw new Error(err.message === 'error connection' ? 
            'Failed to connect to server. Please check your connection.' : 
            'Failed to fetch control flow graph');
        }),
        fetchAttributes({ code }).catch(err => {
          throw new Error(err.message === 'error connection' ? 
            'Failed to connect to server. Please check your connection.' : 
            'Failed to fetch attributes');
        })
      ]);

      if (!cfgResponse || !attributesResponse) {
        toast.error('Failed to fetch required data');
        throw new Error('Failed to fetch required data');
      }

      const { nodes: parsedNodes, edges: parsedEdges } = parseCFG(
        cfgResponse.class, 
        cfgResponse.function, 
        cfgResponse.mainCode, 
        attributesResponse
      );

      const combinedEdges = [...parsedEdges];

      // Fetch additional graph data in parallel if selected
      const graphRequests = [];
      if (selectedGraphTypes['CG']) {
        graphRequests.push(
          fetchCallGraph({ code })
            .then(parseCallGraph)
            .catch(err => {
              toast.error(err.message === 'error connection' ? 
                'Connection error while fetching call graph' : 
                'Failed to parse call graph');
              return []; // Return empty array to prevent Promise.all from failing
            })
        );
      }
      if (selectedGraphTypes['PDG']) {
        graphRequests.push(
          fetchPDG({ code })
            .then(parsePDG)
            .catch(err => {
              toast.error(err.message === 'error connection' ? 
                'Connection error while fetching PDG' : 
                'Failed to parse PDG');
              return []; // Return empty array to prevent Promise.all from failing
            })
        );
      }

      const additionalEdges = await Promise.all(graphRequests);
      combinedEdges.push(...additionalEdges.flat());

      setNodes(parsedNodes);
      setEdges(combinedEdges);

    } catch (err) {
      console.error("Failed to visualize code:", err);
      const errorMessage = err instanceof Error ? err.message : 'An unknown error occurred';
      setApiError(errorMessage);
      toast.error(errorMessage);
    } finally {
      setIsLoadingApi(false);
    }
  }, [setNodes, setEdges]);

  const handleNodeClick = useCallback((_event: React.MouseEvent, node: Node) => {
    setSelectedNode(node as CustomNode);
  }, []);

  const handleCloseSidebar = useCallback(() => {
    setSelectedNode(null);
  }, []);

  return (
    <div className="flex h-screen w-screen bg-slate-100 font-sans overflow-hidden">
      <ToastContainer 
      />
      <CodeInputPanel
        defaultCode={INITIAL_PYTHON_CODE}
        onVisualizeClick={handleVisualize}
        isVisualizing={isLoadingApi}
        visualizationError={apiError}
        initialPanelWidth={DEFAULT_PANEL_WIDTH}
        minPanelWidth={MIN_PANEL_WIDTH}
        maxPanelWidth={MAX_PANEL_WIDTH}
      />
      <FlowDisplay
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange as OnNodesChange<CustomNode>}
        onEdgesChange={onEdgesChange as OnEdgesChange<CustomEdge>}
        nodeTypes={nodeTypes}
        isFlowLoading={isLoadingApi}
        onNodeClick={handleNodeClick}
      />
      <DetailsSidebar
        node={selectedNode}
        onClose={handleCloseSidebar}
      />
    </div>
  );
}