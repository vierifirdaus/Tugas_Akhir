// src/app/method/_components/SVGMethodNode.tsx
import React from 'react';
import { Handle, Position, NodeProps } from '@xyflow/react';
import {
  DEFAULT_SVG_WIDTH_PX,
  DEFAULT_SVG_HEIGHT_PX,
  PT_TO_PX_FACTOR,
  SVG_NODE_EXTRA_WIDTH_PADDING,
  SVG_NODE_EXTRA_HEIGHT_PADDING
} from '@/constants/flowConstants';

// Props untuk SVGMethodNode, menggunakan NodeProps dari @xyflow/react
const SVGMethodNode: React.FC<NodeProps> = ({ data, selected, type, id }) => {
  const svgWidthMatch = typeof data.svg === 'string' ? data.svg.match(/width="(\d+(\.\d+)?)pt/) : null;
  const svgHeightMatch = typeof data.svg === 'string' ? data.svg.match(/height="(\d+(\.\d+)?)pt/) : null;

  let originalSvgWidth = DEFAULT_SVG_WIDTH_PX;
  if (svgWidthMatch && svgWidthMatch[1]) {
    const parsed = parseFloat(svgWidthMatch[1]);
    if (!isNaN(parsed)) {
      originalSvgWidth = Math.ceil(parsed * PT_TO_PX_FACTOR);
    }
  }

  let originalSvgHeight = DEFAULT_SVG_HEIGHT_PX;
  if (svgHeightMatch && svgHeightMatch[1]) {
    const parsed = parseFloat(svgHeightMatch[1]);
    if (!isNaN(parsed)) {
      originalSvgHeight = Math.ceil(parsed * PT_TO_PX_FACTOR);
    }
  }

  // Dimensi keseluruhan komponen node
  const componentWidth = originalSvgWidth + SVG_NODE_EXTRA_WIDTH_PADDING;
  const componentHeight = originalSvgHeight + SVG_NODE_EXTRA_HEIGHT_PADDING;

  return (
    <div
      className={`bg-white rounded-md border p-1.5 flex flex-col shadow-sm box-border
                  border-blue-300 ring-2 ring-blue-500`}
      style={{
        width: componentWidth,
        height: componentHeight,
      }}
    >
      {/* Kontainer untuk SVG */}
      <div
        dangerouslySetInnerHTML={{ __html: data.svg || "" }}
        className="overflow-visible" // Sesuai style asli
        style={{
          width: originalSvgWidth,
          height: originalSvgHeight,
        }}
      />
      {/* Label Metode */}
      <div
        className="mt-1 text-center font-medium text-xs py-1 px-0.5 bg-blue-300 rounded w-full truncate"
        title={String(data.label)} // Tooltip untuk teks panjang
      >
        {String(data.label)}
      </div>
      {/* Handles untuk koneksi */}
      <Handle type="source" position={Position.Bottom} id="out" className="!bg-slate-400 !w-3 !h-3" />
      <Handle type="target" position={Position.Top} id="in" className="!bg-slate-400 !w-3 !h-3" />
    </div>
  );
};

export default React.memo(SVGMethodNode); // Gunakan React.memo untuk optimasi jika props tidak sering berubah
