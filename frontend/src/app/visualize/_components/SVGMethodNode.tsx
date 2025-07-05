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

const SVGMethodNode: React.FC<NodeProps> = ({ data }) => {
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

  let componentWidth = originalSvgWidth + SVG_NODE_EXTRA_WIDTH_PADDING;
  let componentHeight = originalSvgHeight + SVG_NODE_EXTRA_HEIGHT_PADDING;

  if(data.category === 'attribute') {
    componentHeight = 50; // Fixed height for attribute nodes
    componentWidth = Math.max(componentWidth, 150); // Ensure minimum width for attribute nodes
  }

  // Determine colors based on category
  const borderColor = data.category === 'attribute' ? 'border-orange-300' : 'border-blue-300';
  const ringColor = data.category === 'attribute' ? 'ring-orange-500' : 'ring-blue-500';
  const labelBgColor = data.category === 'attribute' ? 'bg-orange-300' : 'bg-blue-300';

  return (
    <div
      className={`bg-white rounded-md border p-1.5 flex flex-col shadow-sm box-border
                  ${borderColor} ${ringColor} ring-2`}
      style={{
        width: componentWidth,
        height: componentHeight,
      }}
    >
      {/* SVG Container */}
      {
        data.category != 'attribute' &&
        (
        <div      
          dangerouslySetInnerHTML={{ __html: data.svg || "" }}
          className="overflow-visible"
          style={{
            width: originalSvgWidth,
            height: originalSvgHeight,
          }}
      />
        )
      }
      
      {/* Label */}
      <div
        className={`mt-1 text-center font-medium text-xs py-1 px-0.5 ${labelBgColor} rounded w-full truncate`}
        title={String(data.label)}
      >
        {String(data.label)}
      </div>
      {/* Handles for connections */}
      <Handle type="source" position={Position.Top} id="out" className="!bg-slate-400 !w-3 !h-3" />
      <Handle type="target" position={Position.Bottom} id="in" className="!bg-slate-400 !w-3 !h-3" />
    </div>
  );
};

export default React.memo(SVGMethodNode);