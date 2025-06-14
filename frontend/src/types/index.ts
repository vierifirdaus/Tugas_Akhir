// src/types/index.ts
import { Node as RFNode, Edge as RFEdge } from '@xyflow/react';


// Tipe data untuk SVGMethodNode
export interface SVGMethodNodeData {
  svg?: string;
  label: string;
  [key: string]: unknown; // Ditambahkan untuk memenuhi constraint Record<string, unknown>
}

// Tipe data untuk ClassGroupNode
export interface ClassGroupNodeData {
  label: string;
  [key: string]: unknown; // Ditambahkan untuk memenuhi constraint Record<string, unknown>
}

// Tipe untuk custom node Anda, bisa diperluas
export type CustomNode = RFNode<SVGMethodNodeData | ClassGroupNodeData>;
export type CustomEdge = RFEdge;


// Sesuaikan tipe ini dengan struktur data yang sebenarnya dari backend Anda
export interface BackendClassItem {
  [className: string]: BackendMethodObject[];
}

export interface BackendMethodObject {
  [methodName: string]: string; // svgContent
}

export type BackendResultType = BackendClassItem[];

// Tipe untuk hasil parsing dari backend ke format React Flow
export interface ParsedFlowResult {
  nodes: CustomNode[];
  edges: CustomEdge[];
}

// Tipe untuk payload request ke API
export interface VisualizeCodePayload {
  code: string;
  // types?: SelectedGraphTypes; // Opsional jika API Anda mendukung ini
}

// Tipe untuk response dari API (sesuaikan dengan struktur API Anda)
export interface VisualizeCodeResponse {
  result: BackendResultType;
  // error?: string; // Opsional, untuk error dari backend
}

// --- Tipe Baru untuk Call Graph API ---
export interface CallGraphResponse {
  call_graph: string[]; // Contoh: ["ClassA.method1 -> ClassB.method2"]
}

// Tipe untuk informasi node metode internal di parser
export interface MethodNodeInfo {
  methodName: string;
  svgContent: string;
  nodeWidth: number;
  nodeHeight: number;
  _debug_originalSvgWidth: number;
  _debug_originalSvgHeight: number;
}