// src/app/method/PDG.ts
import { PDGResponse, CustomEdge } from "@/types";
import { MarkerType, Position } from "@xyflow/react";

/**
 * Mem-parsing respons PDG dari backend menjadi array edge untuk React Flow.
 * @param pdgResponse - Objek respons dari API /pdg.
 * @returns Array dari CustomEdge untuk ditampilkan.
 */
export function parsePDG(pdgResponse: PDGResponse): CustomEdge[] {
  const edges: CustomEdge[] = [];

  if (!pdgResponse) {
    return edges;
  }

  // Iterasi melalui setiap kelas dalam respons (misalnya, "Product", "ShoppingCart")
  for (const className in pdgResponse) {
    if (Object.prototype.hasOwnProperty.call(pdgResponse, className)) {
      const dependencies = pdgResponse[className];

      dependencies.forEach((dep, index) => {
        const parts = dep.split(" -> ");
        if (parts.length !== 2) {
          console.warn(`Invalid PDG dependency format: "${dep}"`);
          return; // Lanjut ke dependensi berikutnya
        }

        const sourceMethod = parts[0];
        const targetAttribute = parts[1];

        // Buat ID node sumber (metode) dan target (atribut)
        const sourceNodeId = `group-${className}-${sourceMethod}`;
        const targetNodeId = `group-${className}-attribute-${targetAttribute}`;

        edges.push({
          id: `pdg-edge-${className}-${index}`,
          source: sourceNodeId,
          target: targetNodeId,
          type: "bezier",
            animated: false,
            zIndex: 1000,
            markerEnd: {
            type: MarkerType.ArrowClosed,
            width: 15,
            height: 15,
            color: "#40ff00", 
            },
            style: {  
            strokeWidth: 2,
            stroke: "#40ff00",
            },
          label: `Dependency from ${sourceMethod} \n to ${targetAttribute}`,
        });
      });
    }
  }

  return edges;
}
