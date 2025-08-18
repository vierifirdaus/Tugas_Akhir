// src/lib/flowUtils.ts
import {
  CLASS_LABEL_HEADER_HEIGHT,
  GROUP_INTERNAL_PADDING_VERTICAL,
  GROUP_INTERNAL_PADDING_HORIZONTAL,
  METHOD_SPACING_HORIZONTAL,
  CLASS_SPACING_VERTICAL,
  MIN_GROUP_WIDTH,
  DEFAULT_SVG_WIDTH_PX,
  DEFAULT_SVG_HEIGHT_PX,
  PT_TO_PX_FACTOR,
  SVG_NODE_EXTRA_WIDTH_PADDING,
  SVG_NODE_EXTRA_HEIGHT_PADDING,
  CLASS_SPACING_HORIZONTAL 
} from '@/constants/flowConstants';
import { getSvgDimensions } from '@/lib/svgDimension';
import {
  ParsedFlowResult,
  CustomNode,
  MethodNodeInfo,
  BackendMethodObject,
  BackendClassResultType,
  BackendFunctionResultType,
  CustomEdge,
  AttributesResponse,
} from '@/types';

type ProcessedClassInfo = {
  className: string;
  groupId: string;
  finalGroupWidth: number;
  finalGroupHeight: number;
  methodRows: MethodNodeInfo[][];
  rowMaxHeights: number[];
};

type ProcessedFunctionInfo = {
  funcName: string;
  groupId: string;
  groupWidth: number;
  groupHeight: number;
  svgContent: string;
};


export function parseCFG(
  classResult: BackendClassResultType,
  functionResult: BackendFunctionResultType,
  mainResult: string,
  attributes: AttributesResponse
): ParsedFlowResult {
  const nodesArray: CustomNode[] = [];
  const edgesArray: CustomEdge[] = [];
  let yOffset = 50;

  // 1. Proses Kelas dalam layout grid
  yOffset = processClasses(classResult, nodesArray, yOffset, attributes);

  // 2. Proses Fungsi dalam layout grid, di bawah kelas
  yOffset = processFunctions(functionResult, nodesArray, yOffset);

  // 3. Proses Main result di bawah semuanya\
  console.log("mainresulttt ",mainResult)
  if( mainResult != '' && mainResult != null) {
    console.log("masuk pak eko")
    processMainResult(mainResult, nodesArray, yOffset);
  }

  return { nodes: nodesArray, edges: edgesArray };
}

function processClasses(
  classResult: BackendClassResultType,
  nodesArray: CustomNode[],
  currentYPosition: number,
  attributes: AttributesResponse
): number {
  if (classResult.length === 0) {
    return currentYPosition;
  }

  const processedClasses: ProcessedClassInfo[] = classResult.map((classItem) => {
    const className = Object.keys(classItem)[0];
    const methods: BackendMethodObject[] = classItem[className] || [];
    const methodNodesInfo = processMethods(className, methods);
    const methodRows = createMethodRows(methodNodesInfo);
    const { rowWidths, rowMaxHeights } = calculateRowDimensions(methodRows);
    const { finalGroupWidth, finalGroupHeight } = calculateGroupDimensions(
      rowWidths, 
      rowMaxHeights,
      attributes[className] || []
    );
    return {
      className,
      groupId: `group-${className}`,
      finalGroupWidth,
      finalGroupHeight,
      methodRows,
      rowMaxHeights,
    };
  });

  const numClasses = processedClasses.length;
  const itemsPerRow = Math.ceil(Math.sqrt(numClasses)); 
  const numRows = Math.ceil(numClasses / itemsPerRow);

  const columnWidths: number[] = new Array(itemsPerRow).fill(0);
  for (let i = 0; i < numRows; i++) {
    for (let j = 0; j < itemsPerRow; j++) {
      const index = i * itemsPerRow + j;
      if (index < numClasses) {
        const classInfo = processedClasses[index];
        if (classInfo.finalGroupWidth > columnWidths[j]) {
          columnWidths[j] = classInfo.finalGroupWidth;
        }
      }
    }
  }
  
  let currentX = 100;
  let yForRow = currentYPosition;
  let maxRowHeight = 0;
  
  for (let i = 0; i < numClasses; i++) {
    const classInfo = processedClasses[i];
    const colIndex = i % itemsPerRow;

    if (colIndex === 0) {
      currentX = 100;
    } else {
      currentX += columnWidths[colIndex - 1] + CLASS_SPACING_HORIZONTAL;
    }
    
    nodesArray.push({
      id: classInfo.groupId,
      type: 'classGroup',
      position: { x: currentX, y: yForRow },
      style: { width: classInfo.finalGroupWidth, height: classInfo.finalGroupHeight },
      draggable: true,
      data: { 
        category: 'class',
        label: classInfo.className,
        width: classInfo.finalGroupWidth,
        height: classInfo.finalGroupHeight,
      },
    });

    processAttributes(nodesArray, classInfo.groupId, classInfo.className, attributes);
    processMethodRows(nodesArray, classInfo.groupId, classInfo.methodRows, classInfo.rowMaxHeights);

    if (classInfo.finalGroupHeight > maxRowHeight) {
      maxRowHeight = classInfo.finalGroupHeight;
    }

    if ((i + 1) % itemsPerRow === 0 || i === numClasses - 1) {
      yForRow += maxRowHeight + CLASS_SPACING_VERTICAL;
      maxRowHeight = 0;
    }
  }

  return yForRow;
}
function processMethods(className: string, methods: BackendMethodObject[]): MethodNodeInfo[] {
  return methods.map((methodObj: BackendMethodObject) => {
    const methodName = Object.keys(methodObj)[0];
    const svgContent = methodObj[methodName] || "";

    const originalSvgWidth = extractSvgDimension(
      svgContent,
      /width="(\d+(\.\d+)?)pt/,
      DEFAULT_SVG_WIDTH_PX,
      `${className}-${methodName}`,
      'lebar'
    );

    const originalSvgHeight = extractSvgDimension(
      svgContent,
      /height="(\d+(\.\d+)?)pt/,
      DEFAULT_SVG_HEIGHT_PX,
      `${className}-${methodName}`,
      'tinggi'
    );

    const methodNodeComponentWidth = originalSvgWidth + SVG_NODE_EXTRA_WIDTH_PADDING;
    const methodNodeComponentHeight = originalSvgHeight + SVG_NODE_EXTRA_HEIGHT_PADDING;

    return {
      methodName,
      svgContent,
      nodeWidth: methodNodeComponentWidth,
      nodeHeight: methodNodeComponentHeight,
      _debug_originalSvgWidth: originalSvgWidth,
      _debug_originalSvgHeight: originalSvgHeight,
    };
  });
}

function extractSvgDimension(
  svgContent: string,
  regex: RegExp,
  defaultValue: number,
  context: string,
  dimensionName: string
): number {
  const match = svgContent.match(regex);
  if (match && match[1]) {
    const parsed = parseFloat(match[1]);
    if (!isNaN(parsed)) {
      return Math.ceil(parsed * PT_TO_PX_FACTOR);
    }
    console.warn(`[${context}] Gagal parse ${dimensionName} SVG: "${match[1]}". Menggunakan default: ${defaultValue}px.`);
  } else if (svgContent) {
    console.warn(`[${context}] Tidak ditemukan format ${dimensionName}="<angka>pt" di SVG. Menggunakan default: ${defaultValue}px.`);
  }
  return defaultValue;
}

function createMethodRows(methodNodesInfo: MethodNodeInfo[]): MethodNodeInfo[][] {
  const rows: MethodNodeInfo[][] = [];
  const itemsPerRow = Math.ceil(Math.sqrt(methodNodesInfo.length));
  
  for (let i = 0; i < methodNodesInfo.length; i += itemsPerRow) {
    rows.push(methodNodesInfo.slice(i, i + itemsPerRow));
  }
  
  return rows;
}

function calculateRowDimensions(rows: MethodNodeInfo[][]) {
  const rowWidths = rows.map(row => 
    row.reduce((sum, method) => sum + method.nodeWidth, 0) + 
    (row.length > 1 ? METHOD_SPACING_HORIZONTAL * (row.length - 1) : 0) // Perbaikan kecil di sini
  );
  
  const rowMaxHeights = rows.map(row => 
    Math.max(...row.map(method => method.nodeHeight))
  );
  
  return { rowWidths, rowMaxHeights };
}

function calculateGroupDimensions(
  rowWidths: number[],
  rowMaxHeights: number[],
  attributes: string[] = []
) {
  // Calculate max row width from methods
  const maxMethodRowWidth = Math.max(...rowWidths, 0);
  
  // Calculate attributes row width (attributes are displayed horizontally)
  const attributeItemWidth = 230; // Same as your attribute node width + spacing
  const attributesRowWidth = attributes.length * attributeItemWidth;
  
  // The group width should be the maximum between:
  // 1. The widest method row
  // 2. The total attributes width
  // 3. The minimum group width
  const maxRowWidth = Math.max(maxMethodRowWidth, attributesRowWidth);
  const finalGroupWidth = Math.max(MIN_GROUP_WIDTH, maxRowWidth + (GROUP_INTERNAL_PADDING_HORIZONTAL * 2));
  
  // Calculate content height (methods + attributes)
  const totalContentHeight = rowMaxHeights.reduce((sum, height) => sum + height, 0) + 
    (rowMaxHeights.length > 1 ? (rowMaxHeights.length - 1) * CLASS_SPACING_VERTICAL / 2 : 0) +
    (attributes.length > 0 ? 50 : 0); // Add fixed height for attributes row
  
  const finalGroupHeight = CLASS_LABEL_HEADER_HEIGHT + totalContentHeight + 
    (GROUP_INTERNAL_PADDING_VERTICAL * 2) + 75;
  
  return { finalGroupWidth, finalGroupHeight };
}


function processAttributes(
  nodesArray: CustomNode[],
  groupId: string,
  className: string,
  attributes: AttributesResponse
) {
  let xOffsetAttributes = GROUP_INTERNAL_PADDING_HORIZONTAL;
  
  attributes[className]?.forEach((attribute) => {
    const attributeName = attribute;
    const attributeSvgContent = createAttributeSvg(attributeName);
    const { width: attrSvgWidth} = getSvgDimensions(attributeSvgContent);
    
    const attrNodeWidth = attrSvgWidth + SVG_NODE_EXTRA_WIDTH_PADDING;
    // const attrNodeHeight = attrSvgHeight + SVG_NODE_EXTRA_HEIGHT_PADDING;
    
    nodesArray.push({
      id: `${groupId}-attribute-${attributeName}`,
      type: 'svgMethod',
      parentId: groupId,
      extent: 'parent',
      position: { 
        x: xOffsetAttributes, 
        y: CLASS_LABEL_HEADER_HEIGHT + GROUP_INTERNAL_PADDING_VERTICAL 
      },
      data: {
        label: attributeName,
        category: 'attribute',
        svg: attributeSvgContent,
      },
      style: {
        width: attrNodeWidth,
        height: 50,
      }
    });

    xOffsetAttributes += 230;
  });
}

function createAttributeSvg(attributeName: string, maxWidth: number = 180, lineHeight: number = 20): string {
  const words = attributeName.split(' ');
  const lines: string[] = [];
  let currentLine = words[0];

  for (let i = 1; i < words.length; i++) {
    const word = words[i];
    if ((currentLine.length + word.length) * 10 > maxWidth) {
      lines.push(currentLine);
      currentLine = word;
    } else {
      currentLine += ' ' + word;
    }
  }
  lines.push(currentLine);

  const height = Math.max(120, 40 + (lines.length * lineHeight));
  
  const tspans = lines.map((line, index) => 
    `<tspan x="10" dy="${index === 0 ? '0' : lineHeight}">${line}</tspan>`
  ).join('');

  return `<svg xmlns="http://www.w3.org/2000/svg" width="200" height="${height}">
    <text x="10" y="20" font-size="16">${tspans}</text>
  </svg>`;
}

function processMethodRows(
  nodesArray: CustomNode[],
  groupId: string,
  rows: MethodNodeInfo[][],
  rowMaxHeights: number[]
) {
  let yOffsetForRow = CLASS_LABEL_HEADER_HEIGHT + GROUP_INTERNAL_PADDING_VERTICAL + 75;
  
  rows.forEach((row, rowIndex) => {
    let xOffset = GROUP_INTERNAL_PADDING_HORIZONTAL;

    row.forEach((methodInfo) => {
      nodesArray.push({
        id: `${groupId}-${methodInfo.methodName}`,
        type: 'svgMethod',
        parentId: groupId,
        extent: 'parent',
        position: { x: xOffset, y: yOffsetForRow },
        data: {
          label: methodInfo.methodName,
          category: 'method',
          svg: methodInfo.svgContent,
        },
        style: {
          width: methodInfo.nodeWidth,
          height: methodInfo.nodeHeight,
        }
      });
      xOffset += methodInfo.nodeWidth + METHOD_SPACING_HORIZONTAL;
    });

    yOffsetForRow += rowMaxHeights[rowIndex] + (CLASS_SPACING_VERTICAL / 2);
  });
}

function processFunctions(
  functionResult: BackendFunctionResultType,
  nodesArray: CustomNode[],
  currentYPosition: number
): number {
  if (functionResult.length === 0) {
    return currentYPosition;
  }

  // --- Tahap 1: Pra-pemrosesan semua fungsi untuk mendapatkan dimensinya ---
  const processedFunctions: ProcessedFunctionInfo[] = functionResult.map((funcItem) => {
    const funcName = Object.keys(funcItem)[0];
    const svgContent = funcItem[funcName] || "";
    const { width: svgWidth, height: svgHeight } = getSvgDimensions(svgContent);

    const contentNodeWidth = svgWidth + SVG_NODE_EXTRA_WIDTH_PADDING;
    const contentNodeHeight = svgHeight + SVG_NODE_EXTRA_HEIGHT_PADDING;

    const groupWidth = contentNodeWidth + (GROUP_INTERNAL_PADDING_HORIZONTAL * 2);
    const groupHeight = CLASS_LABEL_HEADER_HEIGHT + contentNodeHeight + (GROUP_INTERNAL_PADDING_VERTICAL * 2);

    return {
      funcName,
      groupId: `group-${funcName}`,
      groupWidth,
      groupHeight,
      svgContent,
    };
  });
  const numFunctions = processedFunctions.length;
  const itemsPerRow = Math.ceil(Math.sqrt(numFunctions));
  const numRows = Math.ceil(numFunctions / itemsPerRow);

  const columnWidths: number[] = new Array(itemsPerRow).fill(0);
  for (let i = 0; i < numRows; i++) {
    for (let j = 0; j < itemsPerRow; j++) {
      const index = i * itemsPerRow + j;
      if (index < numFunctions) {
        const funcInfo = processedFunctions[index];
        if (funcInfo.groupWidth > columnWidths[j]) {
          columnWidths[j] = funcInfo.groupWidth;
        }
      }
    }
  }

  let currentX = 100;
  let yForRow = currentYPosition;
  let maxRowHeight = 0;

  for (let i = 0; i < numFunctions; i++) {
    const funcInfo = processedFunctions[i];
    const colIndex = i % itemsPerRow;

    if (colIndex === 0) {
      currentX = 100;
    } else {
      currentX += columnWidths[colIndex - 1] + CLASS_SPACING_HORIZONTAL;
    }

    nodesArray.push({
      id: funcInfo.groupId,
      type: 'classGroup',
      position: { x: currentX, y: yForRow },
      style: { width: funcInfo.groupWidth, height: funcInfo.groupHeight },
      data: {
        label: funcInfo.funcName,
        category: 'function',
        svg: funcInfo.svgContent,
        width: funcInfo.groupWidth,
        height: funcInfo.groupHeight
      },
    });

    if (funcInfo.groupHeight > maxRowHeight) {
      maxRowHeight = funcInfo.groupHeight;
    }

    if ((i + 1) % itemsPerRow === 0 || i === numFunctions - 1) {
      yForRow += maxRowHeight + CLASS_SPACING_VERTICAL;
      maxRowHeight = 0;
    }
  }

  return yForRow;
}

function processMainResult(
  mainResult: string,
  nodesArray: CustomNode[],
  currentYPosition: number
) {
  const mainSvgContent = mainResult || "";
  const { width: mainSvgWidth, height: mainSvgHeight } = getSvgDimensions(mainSvgContent);

  const contentNodeWidth = mainSvgWidth + SVG_NODE_EXTRA_WIDTH_PADDING;
  const contentNodeHeight = mainSvgHeight + SVG_NODE_EXTRA_HEIGHT_PADDING;

  const groupWidth = contentNodeWidth + (GROUP_INTERNAL_PADDING_HORIZONTAL * 2);
  const groupHeight = CLASS_LABEL_HEADER_HEIGHT + contentNodeHeight + 
    (GROUP_INTERNAL_PADDING_VERTICAL * 2);

  const mainGroupId = `group-main`;
  nodesArray.push({
    id: mainGroupId,
    type: 'classGroup',
    position: { x: 100, y: currentYPosition },
    style: { width: groupWidth, height: groupHeight },
    data: { 
      label: 'Main', 
      category: 'main', 
      svg: mainSvgContent, 
      width: groupWidth, 
      height: groupHeight 
    },
  });
}