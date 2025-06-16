import { DEFAULT_SVG_HEIGHT_PX, DEFAULT_SVG_WIDTH_PX, PT_TO_PX_FACTOR } from "@/constants/flowConstants";

export const getSvgDimensions = (svgContent: string): { width: number; height: number } => {
    let width = DEFAULT_SVG_WIDTH_PX;
    const svgWidthMatch = svgContent.match(/width="(\d+(\.\d+)?)pt/);
    if (svgWidthMatch?.[1]) {
        width = Math.ceil(parseFloat(svgWidthMatch[1]) * PT_TO_PX_FACTOR);
    }
    
    let height = DEFAULT_SVG_HEIGHT_PX;
    const svgHeightMatch = svgContent.match(/height="(\d+(\.\d+)?)pt/);
    if (svgHeightMatch?.[1]) {
        height = Math.ceil(parseFloat(svgHeightMatch[1]) * PT_TO_PX_FACTOR);
    }
    return { width, height };
};