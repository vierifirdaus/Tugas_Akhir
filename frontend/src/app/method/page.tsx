'use client';
import React, { useState, useMemo } from 'react';
import {
  ReactFlow,
  MiniMap,
  Controls,
  Handle,
  Position,
  useNodesState,
  useEdgesState,
} from '@xyflow/react';
import '@xyflow/react/dist/style.css';

// Komponen Node Kustom untuk Metode SVG
const SVGMethodNode = ({ data }: any) => {
  const svgWidthMatch = data.svg?.match(/width="(\d+)pt/);
  const svgHeightMatch = data.svg?.match(/height="(\d+)pt/);
  
  let originalWidth = 200; // Default
  if (svgWidthMatch && svgWidthMatch[1]) {
    const parsed = parseInt(svgWidthMatch[1], 10);
    if (!isNaN(parsed)) {
      originalWidth = Math.ceil(parsed * 1.33);
    }
  }

  let originalHeight = 100; // Default
  if (svgHeightMatch && svgHeightMatch[1]) {
    const parsed = parseInt(svgHeightMatch[1], 10);
    if (!isNaN(parsed)) {
      originalHeight = Math.ceil(parsed * 1.33);
    }
  }

  return (
    <div style={{ 
      background: "#ffffff",
      borderRadius: 6,
      border: '1px solid #dfe4ea',
      padding: 6,
      width: originalWidth + 12, 
      height: originalHeight + 40, 
      display: 'flex',
      flexDirection: 'column',
      boxSizing: 'border-box',
      boxShadow: '0 2px 4px rgba(0,0,0,0.05)',
    }}>
      <div 
        dangerouslySetInnerHTML={{ __html: data.svg || "" }}
        style={{ 
          width: originalWidth, 
          height: originalHeight,
          overflow: 'visible'
        }} 
      />
      <div style={{ 
        marginTop: 4,
        textAlign: "center",
        fontWeight: 500,
        fontSize: '13px',
        padding: '5px 0',
        backgroundColor: '#f7f9fc',
        borderRadius: 4,
        width: '100%',
        color: '#343a40',
      }}>
        {data.label}
      </div>
      <Handle type="source" position={Position.Bottom} id="out" style={{ background: '#adb5bd' }} />
      <Handle type="target" position={Position.Top} id="in" style={{ background: '#adb5bd' }} />
    </div>
  );
};

// Komponen Node Kustom untuk Grup Kelas (dengan log tambahan)
const ClassGroupNode = ({ data, style: groupStyleProp, id: nodeId }: any) => {
  const headerHeight = 40;
  const padding = 10;

  const receivedWidth = groupStyleProp?.width;
  const receivedHeight = groupStyleProp?.height;
  const finalWidthToRender = receivedWidth || 300;
  const finalHeightToRender = receivedHeight || 150;

  console.groupCollapsed(`%c[Render Debug] ClassGroupNode ID: ${nodeId}, Label: ${data.label}`, "color: green; font-weight: bold;");
  console.log("Menerima groupStyleProp object:", groupStyleProp ? JSON.parse(JSON.stringify(groupStyleProp)) : groupStyleProp);
  console.log(`Nilai dari groupStyleProp?.width (receivedWidth): ${receivedWidth} (tipe: ${typeof receivedWidth})`);
  console.log(`Nilai dari groupStyleProp?.height (receivedHeight): ${receivedHeight} (tipe: ${typeof receivedHeight})`);
  console.log(`Final width yang akan dirender (setelah fallback): ${finalWidthToRender}`);
  console.log(`Final height yang akan dirender (setelah fallback): ${finalHeightToRender}`);
  console.groupEnd();

  return (
    <div 
      style={{
        border: '1px solid #ced4da', 
        borderRadius: '8px',
        backgroundColor: '#f8f9fa', 
        display: 'flex',
        flexDirection: 'column',
        boxSizing: 'border-box',
        boxShadow: '0 4px 8px rgba(0,0,0,0.05)',
      }}
    >
      <div 
        style={{
          padding: `0 ${padding}px`,
          backgroundColor: '#e9ecef',
          borderTopLeftRadius: '7px', 
          borderTopRightRadius: '7px',
          borderBottom: '1px solid #dee2e6', 
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center', 
          fontWeight: 'bold',
          fontSize: '16px',
          color: '#212529',
          boxSizing: 'border-box',
        }}
      >
        {data.label}
      </div>
    </div>
  );
};


export default function Page() {
  const [code, setCode] = useState('');
  const [nodes, setNodes, onNodesChange] = useNodesState<any>([]);
  const [edges, setEdges, onEdgesChange] = useEdgesState<any>([]);
  
  const nodeTypes = useMemo(() => ({ 
    svgMethod: SVGMethodNode,
    classGroup: ClassGroupNode 
  }), []);

  const handleSubmit = async (e: any) => {
    e.preventDefault();
    const resp = await fetch('http://127.0.0.1:5000/method', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ code }),
    });
    const data = await resp.json();
    
    if (data.result) {
      const { nodes: parsedNodes, edges: parsedEdges } = parseBackendResultToFlow(data.result);
      
      // --- LOG PARSEDNODES SETELAH DIKEMBALIKAN DARI FUNGSI ---
      const productNodeFromParsed = parsedNodes.find(n => n.id === 'group-Product');
      console.log(
        "%c[handleSubmit Debug] Detail Node 'Product' dalam parsedNodes (sebelum setNodes):", 
        "color: orange; font-weight: bold;", 
        productNodeFromParsed ? JSON.parse(JSON.stringify(productNodeFromParsed)) : "Node Product tidak ditemukan di parsedNodes"
      );
      const shoppingCartNodeFromParsed = parsedNodes.find(n => n.id === 'group-ShoppingCart'); // Tambahan untuk ShoppingCart
       console.log(
        "%c[handleSubmit Debug] Detail Node 'ShoppingCart' dalam parsedNodes (sebelum setNodes):", 
        "color: orange; font-weight: bold;", 
        shoppingCartNodeFromParsed ? JSON.parse(JSON.stringify(shoppingCartNodeFromParsed)) : "Node ShoppingCart tidak ditemukan di parsedNodes"
      );
      // --- AKHIR LOG ---

      setNodes(parsedNodes);
      setEdges(parsedEdges);
    }
  };

function parseBackendResultToFlow(result: any) {
  const nodesArray: any[] = [];
  const edgesArray: any[] = [];
  let currentYPosition = 50;

  const CLASS_LABEL_HEADER_HEIGHT = 40;
  const GROUP_INTERNAL_PADDING_VERTICAL = 20; 
  const GROUP_INTERNAL_PADDING_HORIZONTAL = 20;
  const METHOD_SPACING_HORIZONTAL = 20; 
  const CLASS_SPACING_VERTICAL = 60;
  const MIN_GROUP_WIDTH = 300;
  const MIN_METHOD_AREA_HEIGHT_EMPTY_CLASS = 30;
  const DEFAULT_SVG_WIDTH = 200;
  const DEFAULT_SVG_HEIGHT = 100;

  result.forEach((classItem: any) => {
    const className = Object.keys(classItem)[0];
    const methods = classItem[className] || [];

    let totalMethodsContentWidth = 0;
    let maxMethodNodeHeight = 0; 

    const methodNodesInfo = methods.map((methodObj: any, methodIdx: number) => {
      const methodName = Object.keys(methodObj)[0];
      const svgContent = methodObj[methodName] || "";

      const svgWidthMatch = svgContent.match(/width="(\d+)pt/);
      let originalSvgWidth = DEFAULT_SVG_WIDTH;
      if (svgWidthMatch && svgWidthMatch[1]) {
        const parsed = parseInt(svgWidthMatch[1], 10);
        if (!isNaN(parsed)) {
          originalSvgWidth = Math.ceil(parsed * 1.33);
        } else {
          console.warn(`[${className}-${methodName}] Gagal parse lebar SVG: "${svgWidthMatch[1]}". Menggunakan default: ${DEFAULT_SVG_WIDTH}px.`);
        }
      } else if (svgContent) {
        console.warn(`[${className}-${methodName}] Tidak ditemukan format lebar="<angka>pt" di SVG. Menggunakan default: ${DEFAULT_SVG_WIDTH}px.`);
      }
      
      const svgHeightMatch = svgContent.match(/height="(\d+)pt/);
      let originalSvgHeight = DEFAULT_SVG_HEIGHT;
      if (svgHeightMatch && svgHeightMatch[1]) {
        const parsed = parseInt(svgHeightMatch[1], 10);
        if (!isNaN(parsed)) {
          originalSvgHeight = Math.ceil(parsed * 1.33);
        } else {
          console.warn(`[${className}-${methodName}] Gagal parse tinggi SVG: "${svgHeightMatch[1]}". Menggunakan default: ${DEFAULT_SVG_HEIGHT}px.`);
        }
      } else if (svgContent) {
        console.warn(`[${className}-${methodName}] Tidak ditemukan format tinggi="<angka>pt" di SVG. Menggunakan default: ${DEFAULT_SVG_HEIGHT}px.`);
      }

      const methodNodeComponentWidth = originalSvgWidth + 12; 
      const methodNodeComponentHeight = originalSvgHeight + 40;

      if (methodIdx > 0) {
        totalMethodsContentWidth += METHOD_SPACING_HORIZONTAL;
      }
      totalMethodsContentWidth += methodNodeComponentWidth;
      maxMethodNodeHeight = Math.max(maxMethodNodeHeight, methodNodeComponentHeight);

      return { 
        methodName, 
        svgContent, 
        nodeWidth: methodNodeComponentWidth,
        nodeHeight: methodNodeComponentHeight,
        _debug_originalSvgWidth: originalSvgWidth,
        _debug_originalSvgHeight: originalSvgHeight
      };
    });

    const groupContentWidth = methods.length > 0 ? totalMethodsContentWidth : (MIN_GROUP_WIDTH - GROUP_INTERNAL_PADDING_HORIZONTAL); 
    const finalGroupWidth = Math.max(MIN_GROUP_WIDTH, groupContentWidth + GROUP_INTERNAL_PADDING_HORIZONTAL);
    
    const methodsAreaActualHeight = methods.length > 0 ? maxMethodNodeHeight : MIN_METHOD_AREA_HEIGHT_EMPTY_CLASS; 
    const finalGroupHeight = CLASS_LABEL_HEADER_HEIGHT + methodsAreaActualHeight + GROUP_INTERNAL_PADDING_VERTICAL;

    console.groupCollapsed(`%c[Layout Debug] Class: ${className}`, "color: blue; font-weight: bold;");
    console.log(`  Jumlah Metode: ${methods.length}`);
    console.log(`  Total Lebar Konten Metode (method widths + spacings): ${totalMethodsContentWidth.toFixed(2)}px`);
    console.log(`  Lebar Konten Grup (setelah min untuk kelas kosong): ${groupContentWidth.toFixed(2)}px`);
    console.log(`  Padding Horizontal Internal Grup: ${GROUP_INTERNAL_PADDING_HORIZONTAL}px`);
    console.log(`  ==> Final Lebar Grup (Node Style): ${finalGroupWidth.toFixed(2)}px`);
    console.log(`  Tinggi Node Metode Maksimum: ${maxMethodNodeHeight.toFixed(2)}px`);
    console.log(`  Actual Tinggi Area Metode (setelah min untuk kelas kosong): ${methodsAreaActualHeight.toFixed(2)}px`);
    console.log(`  Tinggi Header Label Kelas: ${CLASS_LABEL_HEADER_HEIGHT}px`);
    console.log(`  Padding Vertikal Internal Grup: ${GROUP_INTERNAL_PADDING_VERTICAL}px`);
    console.log(`  ==> Final Tinggi Grup (Node Style): ${finalGroupHeight.toFixed(2)}px`);
    if(methods.length > 0) {
      console.groupCollapsed("  Detail Node Metode:");
      methodNodesInfo.forEach(mInfo => {
        console.log(`    - ${mInfo.methodName}: nodeWidth=${mInfo.nodeWidth.toFixed(2)}, nodeHeight=${mInfo.nodeHeight.toFixed(2)} (SVG: ${mInfo._debug_originalSvgWidth.toFixed(2)}w x ${mInfo._debug_originalSvgHeight.toFixed(2)}h)`);
      });
      console.groupEnd();
    }
    console.groupEnd();

    const groupId = `group-${className}`;
    const groupNodeObject = {
      id: groupId,
      type: 'classGroup',
      position: { x: 100, y: currentYPosition },
      style: { 
        width: finalGroupWidth,
        height: finalGroupHeight,
      },
      draggable: true,
      data: { label: className },
    };

    console.log(
      `%c[Debug Push Node] Class: ${className} - Group Node Object SIAP DI-PUSH:`, 
      "color: purple; font-weight: bold;", 
      JSON.parse(JSON.stringify(groupNodeObject))
    );

    nodesArray.push(groupNodeObject);

    let currentXMethodPosition = GROUP_INTERNAL_PADDING_HORIZONTAL / 2;
    const methodsYOffsetInGroup = CLASS_LABEL_HEADER_HEIGHT + (GROUP_INTERNAL_PADDING_VERTICAL / 2);

    methodNodesInfo.forEach((methodInfo) => {
      console.log("method info ni ges",methodInfo)
      nodesArray.push({
        id: `${groupId}-${methodInfo.methodName}`,
        type: 'svgMethod',
        parentId: groupId,
        extent: 'parent',
        position: { x: currentXMethodPosition, y: methodsYOffsetInGroup },
        data: { 
          label: methodInfo.methodName, 
          svg: methodInfo.svgContent 
        },
        style: { 
          width: methodInfo.nodeWidth, 
          height: methodInfo.nodeHeight 
        }
      });
      currentXMethodPosition += methodInfo.nodeWidth + METHOD_SPACING_HORIZONTAL;
    });
    currentYPosition += finalGroupHeight + CLASS_SPACING_VERTICAL; 
  });
  console.log("nodes",nodesArray)
  return { nodes: nodesArray, edges: edgesArray };
}

  return (
    <div style={{ display: 'flex', height: '100vh', backgroundColor: '#f4f7f6' }}>
      <div style={{ width: 350, padding: 24, borderRight: "1px solid #e0e0e0", backgroundColor: '#ffffff', overflowY: 'auto' }}>
        <h3 style={{ marginTop: 0, marginBottom: 20, color: '#333' }}>Python Code Input</h3>
        <form onSubmit={handleSubmit}>
          <textarea
            rows={18}
            style={{ 
              width: "100%", 
              fontFamily: "monospace", 
              fontSize: 14,
              border: "1px solid #ccc",
              borderRadius: "4px",
              padding: "10px",
              boxSizing: "border-box",
            }}
            value={code}
            onChange={e => setCode(e.target.value)}
            placeholder="Paste your Python code here..."
          />
          <button 
            type="submit" 
            style={{ 
              marginTop: 16, 
              width: "100%", 
              fontWeight: 600,
              padding: "12px",
              backgroundColor: "#007bff",
              color: "white",
              border: "none",
              borderRadius: "4px",
              cursor: "pointer",
              fontSize: "16px",
            }}
          >
            Visualize
          </button>
        </form>
      </div>
      <div style={{ flex: 1, minWidth: 0 }}>
        <ReactFlow
          nodes={nodes}
          edges={edges}
          onNodesChange={onNodesChange}
          onEdgesChange={onEdgesChange}
          nodeTypes={nodeTypes}
          fitView
          fitViewOptions={{ padding: 0.15 }}
        >
          <MiniMap style={{ backgroundColor: '#ffffff', border: '1px solid #e0e0e0' }} nodeStrokeWidth={3} zoomable pannable />
          <Controls />
        </ReactFlow>
      </div>
    </div>
  );
}