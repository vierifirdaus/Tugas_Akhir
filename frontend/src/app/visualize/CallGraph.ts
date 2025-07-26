import { CallGraphResponse, CustomEdge } from "@/types";
import { MarkerType } from "@xyflow/react";

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
      console.log(`Processing call graph entry at index ${index}:`, call);
      const parts = call.split(" -> ");
      if (parts.length !== 2) {
        console.warn(`Invalid call graph entry at index ${index}: "${call}"`);
        return null;
      }
      console.log(`Parsed parts at index ${index}:`, parts);

      let callerSource,calleeTarget;
      const sourceParts = parts[0].split(".");
      const targetParts = parts[1].split(".");
      let sourceNodeId, targetNodeId;
      if (sourceParts.length < 2 || targetParts.length < 2) {
        console.warn(
          `Invalid source or target format at index ${index}: "${call}"`
        );
        sourceNodeId = `group-${parts[0]}`;
        targetNodeId = `group-${parts[1]}`;
        callerSource = parts[0];
        calleeTarget = parts[1];
      }
      else{
        sourceNodeId = `group-${sourceParts[0]}-${sourceParts[1]}`;
        targetNodeId = `group-${targetParts[0]}-${targetParts[1]}`;
        callerSource = sourceParts[1];
        calleeTarget = targetParts[1];

      }
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
        label: `Call from ${callerSource} to ${calleeTarget}`,
        labelStyle: {
          fill: "#333",
          fontWeight: 500,
        },
        labelBgStyle: {
            fill: 'transparent',
            stroke: 'none' 
          },
      };
    })
    .filter((edge) => edge !== null); // Filter out any null entries
}
