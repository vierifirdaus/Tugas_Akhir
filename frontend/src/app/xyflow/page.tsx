'use client';
import React, { useCallback, useEffect, useState } from 'react';
import {
  ReactFlow,
  MiniMap,
  Controls,
  Handle,
  Position,
  addEdge,
  useNodesState,
  useEdgesState,
  ReactFlowInstance,
} from '@xyflow/react';
import '@xyflow/react/dist/style.css';

// Node dengan SVG Image
const ImageNode = ({ data }: any) => (
  <div style={{ padding: 6, background: '#fff', borderRadius: 8, border: '1px solid #222' }}>
    <img
      src={data.src}
      alt={data.label}
      width={60}
      height={60}
      style={{ display: 'block' }}
    />
    <Handle type="source" position={Position.Bottom} id="out" />
    <Handle type="target" position={Position.Top} id="in" />
  </div>
);

// Komponen utama
export default function Page() {
  const [nodes, setNodes, onNodesChange] = useNodesState<any>([]);
  const [edges, setEdges, onEdgesChange] = useEdgesState<any>([]);
  const [reactFlowInstance, setReactFlowInstance] = useState<ReactFlowInstance | null>(null);

  const nodeTypes = {
    imageNode: ImageNode,
  };

  useEffect(() => {
    const engineId = 'group-engine';
    const carId = 'group-car';

    setNodes([
      // GROUP ENGINE
      {
        id: engineId,
        type: 'group',
        position: { x: 100, y: 50 },
        style: {
          width: 420,
          height: 220,
          backgroundColor: 'rgba(0,0,0,0.05)',
          border: '2px dashed #555',
        },
        draggable: true,
      },
      {
        id: 'engine-init',
        type: 'imageNode',
        data: { src: '/svg/engine_init.svg', label: 'Engine Init' },
        position: { x: 20, y: 20 },
        parentId: engineId,
        extent: 'parent',
      },
      {
        id: 'engine-start',
        type: 'imageNode',
        data: { src: '/svg/engine_start.svg', label: 'Engine Start' },
        position: { x: 150, y: 20 },
        parentId: engineId,
        extent: 'parent',
      },
      {
        id: 'engine-stop',
        type: 'imageNode',
        data: { src: '/svg/engine_stop.svg', label: 'Engine Stop' },
        position: { x: 280, y: 20 },
        parentId: engineId,
        extent: 'parent',
      },

      // GROUP CAR
      {
        id: carId,
        type: 'group',
        position: { x: 100, y: 320 },
        style: {
          width: 420,
          height: 220,
          backgroundColor: 'rgba(0,64,128,0.05)',
          border: '2px dashed #007',
        },
        draggable: true,
      },
      {
        id: 'car-init',
        type: 'imageNode',
        data: { src: '/svg/car_init.svg', label: 'Car Init' },
        position: { x: 20, y: 20 },
        parentId: carId,
        extent: 'parent',
      },
      {
        id: 'car-start',
        type: 'imageNode',
        data: { src: '/svg/car_start.svg', label: 'Car Start' },
        position: { x: 150, y: 20 },
        parentId: carId,
        extent: 'parent',
      },
      {
        id: 'car-stop',
        type: 'imageNode',
        data: { src: '/svg/car_stop.svg', label: 'Car Stop' },
        position: { x: 280, y: 20 },
        parentId: carId,
        extent: 'parent',
      },
    ]);

    setEdges([
      {
        id: 'e-carInit-engineInit',
        source: 'car-init',
        target: 'engine-init',
        sourceHandle: 'out',
        targetHandle: 'in',
        animated: true,
        style: { stroke: '#f40', strokeWidth: 2 },
        label: 'call graph',
        labelBgStyle: { fill: 'white', fillOpacity: 0.7 },
        labelBgPadding: [4, 2],
        labelStyle: { fontWeight: 'bold', fontSize: 12 },
      },
    ]);

  }, [setNodes, setEdges]);

  const onConnect = useCallback(
    (params: any) =>
      setEdges((eds) =>
        addEdge(
          {
            ...params,
            animated: true,
            style: { stroke: '#222' },
          },
          eds
        )
      ),
    [setEdges]
  );

  const onReactFlowInstanceReady = useCallback(
    (instance: ReactFlowInstance) => {
      setReactFlowInstance(instance);
    },
    []
  );

  return (
    <div style={{ height: 800 }}>
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onConnect={onConnect}
        onInit={onReactFlowInstanceReady}
        nodeTypes={nodeTypes}
        snapToGrid
        fitView
      >
        <MiniMap
          nodeStrokeColor={(n) => '#555'}
          nodeColor={() => '#fff'}
        />
        <Controls />
      </ReactFlow>
    </div>
  );
}
