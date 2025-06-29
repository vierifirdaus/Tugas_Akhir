// src/constants/flowConstants.ts

// Konstanta untuk layout dan parsing node
export const CLASS_LABEL_HEADER_HEIGHT = 40;
export const GROUP_INTERNAL_PADDING_VERTICAL = 20;
export const GROUP_INTERNAL_PADDING_HORIZONTAL = 20;
export const METHOD_SPACING_HORIZONTAL = 20;
export const CLASS_SPACING_VERTICAL = 60;
export const MIN_GROUP_WIDTH = 300;
export const MIN_METHOD_AREA_HEIGHT_EMPTY_CLASS = 30;

// Dimensi default untuk SVG jika tidak terdeteksi
export const DEFAULT_SVG_WIDTH_PX = 200;
export const DEFAULT_SVG_HEIGHT_PX = 100;

// Faktor konversi dari point (pt) ke pixel (px)
// (1pt = 1/72 inch, 1 inch = 96px => 1pt = 96/72 px = 4/3 px ≈ 1.33px)
export const PT_TO_PX_FACTOR = 4 / 3;

// Padding tambahan pada komponen SVGMethodNode
export const SVG_NODE_EXTRA_WIDTH_PADDING = 12; // 6 padding kiri + 6 padding kanan
export const SVG_NODE_EXTRA_HEIGHT_PADDING = 40; // 6 padding atas + 6 padding bawah + tinggi label
export const CLASS_SPACING_HORIZONTAL = 50;
// URL API (sebaiknya gunakan environment variable)
export const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://212.85.26.216:5001';
