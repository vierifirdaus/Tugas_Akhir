// src/app/method/_components/DetailsSidebar.tsx
'use client';

import React from 'react';
import { CustomNode } from '@/types';
import { XIcon } from 'lucide-react';

interface DetailsSidebarProps {
  node: CustomNode | null;
  onClose: () => void;
}

const DetailsSidebar: React.FC<DetailsSidebarProps> = ({ node, onClose }) => {
  const { id, type, data } = node || {};
  const { label, category } = data || {};

  return (
    <div
      className={`fixed top-0 right-0 h-full bg-white shadow-2xl transition-transform duration-300 ease-in-out z-30
                  ${node ? 'translate-x-0' : 'translate-x-full'}`}
      style={{ width: '350px' }}
    >
      <div className="flex items-center justify-between p-4 border-b border-slate-200 bg-slate-50">
        <h2 className="text-lg font-semibold text-slate-700 truncate">
          {label || 'Node Details'}
        </h2>
        <button
          onClick={onClose}
          className="p-1.5 text-slate-500 hover:bg-slate-200 rounded-full transition-colors"
          title="Close"
        >
          <XIcon size={20} />
        </button>
      </div>

      {node ? (
        <div className="p-4 space-y-4 overflow-y-auto h-[calc(100vh-65px)]">
          <div className="bg-slate-100 p-3 rounded-md">
            <h3 className="font-bold text-slate-800 mb-2 border-b pb-1">General Info</h3>
            <p className="text-sm"><strong className="w-20 inline-block">ID:</strong> <code className="break-all">{id}</code></p>
            <p className="text-sm"><strong className="w-20 inline-block">Label:</strong> {label}</p>
            {category && (
              <p className="text-sm"><strong className="w-20 inline-block">Category:</strong> 
                <span className="font-mono bg-slate-200 px-2 py-0.5 rounded">{category}</span>
              </p>
            )}
            <p className="text-sm"><strong className="w-20 inline-block">Type:</strong> 
              <span className="font-mono bg-slate-200 px-2 py-0.5 rounded">{type}</span>
            </p>
          </div>

          <div className="bg-gray-800 text-white p-3 rounded-md">
            <h3 className="font-bold mb-2 border-b border-gray-600 pb-1">Raw Node Data</h3>
            <pre className="text-xs whitespace-pre-wrap overflow-x-auto">
              {JSON.stringify(node, null, 2)}
            </pre>
          </div>
        </div>
      ) : (
        <div className="p-4 text-center text-slate-500">
          <p>Click on a node to see its details.</p>
        </div>
      )}
    </div>
  );
};

export default DetailsSidebar;