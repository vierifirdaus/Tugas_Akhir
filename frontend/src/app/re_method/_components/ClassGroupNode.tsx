// src/app/method/_components/ClassGroupNode.tsx
import React from 'react';
import { NodeProps, Handle, Position } from '@xyflow/react'; // React Flow V11+
import { ClassGroupNodeData } from '@/types';
import { CLASS_LABEL_HEADER_HEIGHT } from '@/constants/flowConstants';

// Props untuk ClassGroupNode
const ClassGroupNode: React.FC<NodeProps> = ({ data, selected, id }) => {
  // Ambil width dan height dari data, fallback ke default jika tidak ada
  const nodeWidth = typeof data?.width === 'number' ? data.width : 300;
  const nodeHeight = typeof data?.height === 'number' ? data.height : 150;
  console.log("data classgroup node", data);
  return (
    <div
      className={`border rounded-lg bg-slate-50 flex flex-col box-border shadow-md
                  ${selected ? 'border-blue-600 ring-2 ring-blue-600' : 'border-slate-300'}`}
      style={{
        width: nodeWidth,
        height: nodeHeight, // Tinggi keseluruhan node grup
      }}
    >
      {/* Header Grup Kelas */}
      <div
        className="px-2.5 bg-slate-200 border-b border-slate-300
                   flex items-center justify-center font-bold text-base text-slate-800 box-border
                   rounded-t-md" // rounded-t-md jika border radius parent 8px, sesuaikan
        style={{ height: `${CLASS_LABEL_HEADER_HEIGHT}px` }} // Tinggi header tetap
      >
        {String(data.label)}
      </div>
      {/* Area untuk child nodes (metode) akan di-render secara otomatis oleh React Flow di dalam grup ini */}
      {/* Tidak perlu Handle di sini jika grup hanya sebagai kontainer visual dan layout,
          kecuali jika Anda ingin menghubungkan grup itu sendiri dengan node lain.
          Jika metode di dalamnya yang punya Handle, itu sudah cukup.
      */}
      {/* <Handle type="source" position={Position.Bottom} className="!bg-gray-400" /> */}
      {/* <Handle type="target" position={Position.Top} className="!bg-gray-400" /> */}
    </div>
  );
};

export default React.memo(ClassGroupNode);
