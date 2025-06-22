// src/types/index.ts
import { Node as RFNode, Edge as RFEdge } from '@xyflow/react';

/**
 * ======================
 * React Flow Node Types
 * ======================
 */

/** Data structure for SVG method nodes */
export interface SVGMethodNodeData {
  svg?: string;
  label: string;
  category?: 'method' | 'attribute' | 'function' | 'main';
  [key: string]: unknown; // Additional properties
}

/** Data structure for class group nodes */
export interface ClassGroupNodeData {
  label: string;
  category?: 'class' | 'function' | 'main';
  width?: number;
  height?: number;
  [key: string]: unknown; // Additional properties
}

/** Custom node type extending React Flow's Node */
export type CustomNode = RFNode<SVGMethodNodeData | ClassGroupNodeData>;

/** Custom edge type extending React Flow's Edge */
export type CustomEdge = RFEdge;

/**
 * ======================
 * Backend Response Types
 * ======================
 */

/** Structure for class items from backend */
export interface BackendClassItem {
  [className: string]: BackendMethodObject[];
}

/** Structure for function items from backend */
export interface BackendFunctionItem {
  [functionName: string]: string; // SVG content
}

/** Structure for method objects from backend */
export interface BackendMethodObject {
  [methodName: string]: string; // SVG content
}

/** Structure for main function response */
export interface BackendMainItem {
  mainCode: string; // SVG content for main function
}

/** Collections of backend responses */
export type BackendClassResultType = BackendClassItem[];
export type BackendFunctionResultType = BackendFunctionItem[];
export type BackendMainResultType = string; // Simplified from BackendMainItem

/** Attributes response structure */
export interface AttributesResponse {
  [className: string]: string[]; // List of attributes per class
}

/** PDG (Program Dependence Graph) response */
export interface PDGResponse {
  [className: string]: string[]; // Dependencies in format "source -> target"
}

/** Call graph response structure */
export interface CallGraphResponse {
  call_graph: string[]; // Call relationships in format "caller -> callee"
}

/**
 * ======================
 * API Communication Types
 * ======================
 */

/** Request payload for visualization API */
export interface VisualizeCodePayload {
  code: string;
  // Optional: types?: SelectedGraphTypes;
}

/** Response from visualization API */
export interface VisualizeCodeResponse {
  class: BackendClassResultType;
  function: BackendFunctionResultType;
  mainCode: string;
  // Optional: error?: string;
}

/**
 * ======================
 * Internal Processing Types
 * ======================
 */

/** Intermediate method node information during parsing */
export interface MethodNodeInfo {
  methodName: string;
  svgContent: string;
  nodeWidth: number;
  nodeHeight: number;
  _debug_originalSvgWidth: number;
  _debug_originalSvgHeight: number;
}

/** Final parsed flow result */
export interface ParsedFlowResult {
  nodes: CustomNode[];
  edges: CustomEdge[];
}