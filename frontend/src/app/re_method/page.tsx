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

import { parseBackendResultToFlow } from '@/lib/flowUtils';
import { visualizePythonCode, fetchCallGraph } from '@/lib/api'; // Import fetchCallGraph
import { CustomNode, CustomEdge, VisualizeCodeResponse, BackendResultType, CallGraphResponse } from '@/types';

// Asumsi Anda punya file constants
const INITIAL_PYTHON_CODE = `class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity=1):
        if not isinstance(product, Product):
            raise ValueError("Item yang ditambahkan harus berupa produk.")
        for _ in range(quantity):
            self.items.append(product)
        print(f"Added {quantity} x {product.get_name()} to cart.")

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.get_price()
        return total
`;
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
      const response: VisualizeCodeResponse = await visualizePythonCode({ code });
      
      if (!response.result) {
        throw new Error('No result found in main API response.');
      }
      
      const { nodes: parsedNodes, edges: parsedEdges } = parseBackendResultToFlow(response.result as BackendResultType);
      let combinedEdges = [...parsedEdges];

      // 2. Jika "Call Graph" dipilih, ambil data call graph dan buat edgenya
      if (selectedGraphTypes['CG']) {
        console.log("Fetching Call Graph data...");
        const callGraphResponse: CallGraphResponse = await fetchCallGraph({ code });
        const callGraphEdges: CustomEdge[] = callGraphResponse.call_graph.map((call, index) => {
          const parts = call.split(' -> ');
          const sourceParts = parts[0].split('.');
          const targetParts = parts[1].split('.');

          const sourceNodeId = `group-${sourceParts[0]}-${sourceParts[1]}`;
          const targetNodeId = `group-${targetParts[0]}-${targetParts[1]}`;

          return {
            id: `cg-edge-${index}-${sourceNodeId}-to-${targetNodeId}`,
            source: sourceNodeId,
            target: targetNodeId,
            type: 'smoothstep',
            animated: false,
            zIndex: 1000, 
            markerEnd: {
                type: MarkerType.ArrowClosed,
                width: 15,
                height: 15,
                color: '#3b82f6', // Biru
            },
            style: {
                strokeWidth: 2,
                stroke: '#3b82f6',
            },
            label: 'Call Graph',
          };
        });

        combinedEdges = [...combinedEdges, ...callGraphEdges];
      }

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