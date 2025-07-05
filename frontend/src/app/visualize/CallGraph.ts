import { CallGraphResponse, CustomEdge } from "@/types";
import { MarkerType } from "@xyflow/react";

export function parseCallGraph(
  callGraphResponse: CallGraphResponse
): CustomEdge[] {
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

      const sourceParts = parts[0].split(".");
      const targetParts = parts[1].split(".");

      if (sourceParts.length < 2 || targetParts.length < 2) {
        console.warn(
          `Invalid source or target format at index ${index}: "${call}"`
        );
        return null;
      }

      const sourceNodeId = `group-${sourceParts[0]}-${sourceParts[1]}`;
      const targetNodeId = `group-${targetParts[0]}-${targetParts[1]}`;

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
          color: "#3b82f6", // Biru
        },
        style: {
          strokeWidth: 2,
          stroke: "#3b82f6",
        },
        label: `Call from ${sourceParts[1]} to ${targetParts[1]}`,
      };
    })
    .filter((edge) => edge !== null); // Filter out any null entries
};
