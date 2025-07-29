import { CallGraphResponse, CustomEdge } from "@/types";
import { MarkerType } from "@xyflow/react";

// Fungsi bantuan untuk membuat ID node dari string source/target
function generateNodeId(part: string): string {
  const subParts = part.split(".");
  // Kasus: "hitung_total_bayar.hitung_total_bayar" -> subParts[0] == subParts[1]
  if (subParts.length === 2 && subParts[0] === subParts[1]) {
    return `group-${subParts[0]}`;
  }
  // Kasus lain (misal: "module.function" atau "main") akan digabungkan
  return `group-${part.replace(/\./g, '-')}`;
}


export function parseCallGraph(
  callGraphResponse: CallGraphResponse
): CustomEdge[] {
  console.log("Parsing call graph response:", callGraphResponse);
  if (
    !callGraphResponse ||
    !callGraphResponse.call_graph ||
    !Array.isArray(callGraphResponse.call_graph)
  ) {
    console.error("Invalid call graph response format:", callGraphResponse);
    return [];
  }

  return callGraphResponse.call_graph
    .map((call, index) => {
      const parts = call.split(" -> ");
      if (parts.length !== 2) {
        console.warn(`Invalid call graph entry at index ${index}: "${call}"`);
        return null;
      }

      const [sourcePart, targetPart] = parts;

      // Gunakan fungsi bantuan untuk mendapatkan ID node
      const sourceNodeId = generateNodeId(sourcePart);
      const targetNodeId = generateNodeId(targetPart);

      // Ambil nama fungsi terakhir untuk label (bagian setelah titik terakhir)
      const callerName = sourcePart.split(".").pop() || sourcePart;
      const calleeName = targetPart.split(".").pop() || targetPart;

      return {
        id: `cg-edge-${index}-${sourceNodeId}-to-${targetNodeId}`,
        source: sourceNodeId,
        target: targetNodeId,
        type: "bezier",
        animated: false,
        zIndex: 1000,
        markerEnd: {
          type: MarkerType.ArrowClosed,
          width: 15,
          height: 15,
          color: "#3b82f6",
        },
        style: {
          strokeWidth: 2,
          stroke: "#3b82f6",
        },
        label: `Call from ${callerName} to ${calleeName}`,
        labelStyle: {
          fill: "#333",
          fontWeight: 500,
        },
        labelBgStyle: {
          fill: "transparent",
          stroke: "none",
        },
      };
    })
    .filter((edge) => edge !== null); // Filter out any null entries
}