// src/app/method/_components/ClassGroupNode.tsx
import React from "react";
import { NodeProps, Handle, Position } from "@xyflow/react"; // React Flow V11+
import { ClassGroupNodeData } from "@/types";
import { CLASS_LABEL_HEADER_HEIGHT } from "@/constants/flowConstants";

const categoryColorClasses = {
  class: {
    border: "border-green-400",
    bg: "bg-white",
    headerBg: "bg-green-200",
    headerText: "text-green-800",
    ring: "ring-green-600",
  },
  function: {
    border: "border-yellow-400",
    bg: "bg-white",
    headerBg: "bg-yellow-200",
    headerText: "text-yellow-800",
    ring: "ring-yellow-600",
  },
  main: {
    border: "border-gray-500",
    bg: "bg-white",
    headerBg: "bg-gray-800",
    headerText: "text-white",
    ring: "ring-gray-900",
  },
  method: {
    border: "border-gray-300",
    bg: "bg-white",
    headerBg: "bg-gray-200",
    headerText: "text-gray-800",
    ring: "ring-gray-500",
  },
};

const ClassGroupNode: React.FC<NodeProps> = ({ data, selected, id }) => {
  const nodeWidth = typeof data?.width === "number" ? data.width : 300;
  const nodeHeight = typeof data?.height === "number" ? data.height : 150;

  const colors =
    categoryColorClasses[data.category as keyof typeof categoryColorClasses] ||
    categoryColorClasses.class;

  const containerClasses = `
    ${colors.border} ${colors.bg}
    rounded-lg border-2 flex flex-col box-border shadow-md
    ${selected ? `ring-2 ${colors.ring}` : ""}
  `;

  const headerClasses = `
    ${colors.headerBg} ${colors.headerText}
    px-2.5 border-b-2 ${colors.border}
    flex items-center justify-center font-bold text-base box-border
    rounded-t-md
  `;

  console.log("data classgroup node", data);
  return (
    <div
      className={containerClasses}
      style={{
        width: nodeWidth,
        height: nodeHeight,
      }}
    >
      <div
        className={headerClasses}
        style={{ height: `${CLASS_LABEL_HEADER_HEIGHT}px` }}
      >
        {String(data.label)}
      </div>

      {/* Kontainer untuk SVG */}
      {(data.category == "main" || data.category == "function") && (
        <div
          dangerouslySetInnerHTML={{ __html: data.svg || "" }}
          className="overflow-visible p-7" // Sesuai style asli
          style={{
            width: nodeWidth,
            height: nodeHeight,
          }}
        />
      )}

      {/* Child nodes akan di-render secara otomatis oleh React Flow di sini */}
    </div>
  );
};

export default React.memo(ClassGroupNode);
