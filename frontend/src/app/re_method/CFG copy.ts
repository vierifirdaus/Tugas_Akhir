// src/lib/flowUtils.ts
import {
  CLASS_LABEL_HEADER_HEIGHT,
  GROUP_INTERNAL_PADDING_VERTICAL,
  GROUP_INTERNAL_PADDING_HORIZONTAL,
  METHOD_SPACING_HORIZONTAL,
  CLASS_SPACING_VERTICAL,
  MIN_GROUP_WIDTH,
  MIN_METHOD_AREA_HEIGHT_EMPTY_CLASS,
  DEFAULT_SVG_WIDTH_PX,
  DEFAULT_SVG_HEIGHT_PX,
  PT_TO_PX_FACTOR,
  SVG_NODE_EXTRA_WIDTH_PADDING,
  SVG_NODE_EXTRA_HEIGHT_PADDING,
} from '@/constants/flowConstants';
import { getSvgDimensions } from '@/lib/svgDimension';
import { ParsedFlowResult, CustomNode, MethodNodeInfo, BackendClassItem, BackendMethodObject, BackendClassResultType, BackendFunctionResultType, BackendFunctionItem } from '@/types';

export function parseCFG(classResult: BackendClassResultType, functionResult: BackendFunctionResultType, mainResult: string): ParsedFlowResult {
  const nodesArray: CustomNode[] = [];
  const edgesArray: any[] = [];
  let currentYPosition = 50; 

  classResult.forEach((classItem: BackendClassItem) => {
    const className = Object.keys(classItem)[0];
    const methods: BackendMethodObject[] = classItem[className] || [];

    let totalMethodsContentWidth = 0;
    let maxMethodNodeHeight = 0;

    // Memproses informasi untuk setiap node metode
    const methodNodesInfo: MethodNodeInfo[] = methods.map((methodObj: BackendMethodObject, methodIdx: number) => {
      const methodName = Object.keys(methodObj)[0];
      const svgContent = methodObj[methodName] || "";

      let originalSvgWidth = DEFAULT_SVG_WIDTH_PX;
      const svgWidthMatch = svgContent.match(/width="(\d+(\.\d+)?)pt/); // Update regex untuk float
      if (svgWidthMatch && svgWidthMatch[1]) {
        const parsed = parseFloat(svgWidthMatch[1]);
        if (!isNaN(parsed)) {
          originalSvgWidth = Math.ceil(parsed * PT_TO_PX_FACTOR);
        } else {
          console.warn(`[${className}-${methodName}] Gagal parse lebar SVG: "${svgWidthMatch[1]}". Menggunakan default: ${DEFAULT_SVG_WIDTH_PX}px.`);
        }
      } else if (svgContent) {
        console.warn(`[${className}-${methodName}] Tidak ditemukan format lebar="<angka>pt" di SVG. Menggunakan default: ${DEFAULT_SVG_WIDTH_PX}px.`);
      }

      let originalSvgHeight = DEFAULT_SVG_HEIGHT_PX;
      const svgHeightMatch = svgContent.match(/height="(\d+(\.\d+)?)pt/); // Update regex untuk float
      if (svgHeightMatch && svgHeightMatch[1]) {
        const parsed = parseFloat(svgHeightMatch[1]);
        if (!isNaN(parsed)) {
          originalSvgHeight = Math.ceil(parsed * PT_TO_PX_FACTOR);
        } else {
          console.warn(`[${className}-${methodName}] Gagal parse tinggi SVG: "${svgHeightMatch[1]}". Menggunakan default: ${DEFAULT_SVG_HEIGHT_PX}px.`);
        }
      } else if (svgContent) {
        console.warn(`[${className}-${methodName}] Tidak ditemukan format tinggi="<angka>pt" di SVG. Menggunakan default: ${DEFAULT_SVG_HEIGHT_PX}px.`);
      }

      // Lebar dan tinggi komponen node SVG, termasuk padding dan label
      const methodNodeComponentWidth = originalSvgWidth + SVG_NODE_EXTRA_WIDTH_PADDING;
      const methodNodeComponentHeight = originalSvgHeight + SVG_NODE_EXTRA_HEIGHT_PADDING;

      if (methodIdx > 0) {
        totalMethodsContentWidth += METHOD_SPACING_HORIZONTAL;
      }
      totalMethodsContentWidth += methodNodeComponentWidth;
      maxMethodNodeHeight = Math.max(maxMethodNodeHeight, methodNodeComponentHeight);

      return {
        methodName,
        svgContent,
        nodeWidth: methodNodeComponentWidth,
        nodeHeight: methodNodeComponentHeight,
        _debug_originalSvgWidth: originalSvgWidth,
        _debug_originalSvgHeight: originalSvgHeight,
      };
    });

    // Menghitung dimensi grup kelas
    const groupContentWidth = methods.length > 0 ? totalMethodsContentWidth : (MIN_GROUP_WIDTH - (GROUP_INTERNAL_PADDING_HORIZONTAL * 2));
    const finalGroupWidth = Math.max(MIN_GROUP_WIDTH, groupContentWidth + (GROUP_INTERNAL_PADDING_HORIZONTAL * 2));
    
    const methodsAreaActualHeight = methods.length > 0 ? maxMethodNodeHeight : MIN_METHOD_AREA_HEIGHT_EMPTY_CLASS;
    const finalGroupHeight = CLASS_LABEL_HEADER_HEIGHT + methodsAreaActualHeight + (GROUP_INTERNAL_PADDING_VERTICAL * 2) ;


    // Membuat node untuk grup kelas
    const groupId = `group-${className}`;
    const groupNodeObject: CustomNode = {
      id: groupId,
      type: 'classGroup',
      position: { x: 100, y: currentYPosition },
      style: {
        width: finalGroupWidth,
        height: finalGroupHeight,
      },
      draggable: true, // Sesuai kode asli, bisa diubah jika perlu
      data: { 
        category: 'class',
        label: className,
        width: finalGroupWidth,
        height: finalGroupHeight,
       },
    };
    nodesArray.push(groupNodeObject);

    // Membuat node untuk setiap metode di dalam grup kelas
    let currentXMethodPosition = GROUP_INTERNAL_PADDING_HORIZONTAL;
    const methodsYOffsetInGroup = CLASS_LABEL_HEADER_HEIGHT + GROUP_INTERNAL_PADDING_VERTICAL;

    methodNodesInfo.forEach((methodInfo) => {
      nodesArray.push({
        id: `${groupId}-${methodInfo.methodName}`,
        type: 'svgMethod',
        parentId: groupId, // Menetapkan parentId agar node metode berada di dalam grup
        extent: 'parent',  // Membatasi pergerakan node metode di dalam parent
        position: { x: currentXMethodPosition, y: methodsYOffsetInGroup },
        data: {
          label: methodInfo.methodName,
          category: 'method',
          svg: methodInfo.svgContent,
        },
        // Style width/height untuk SVGMethodNode akan dihandle di dalam komponennya
        // berdasarkan data.svg, jadi tidak perlu di set di sini lagi kecuali ada override.
        // Namun, karena SVGMethodNode di kode asli menghitung width/height dari data.svg,
        // dan React Flow butuh style.width/height untuk layout internal parent,
        // kita tetap pass di sini agar React Flow bisa menghitung bounds parent dengan benar.
        style: {
            width: methodInfo.nodeWidth,
            height: methodInfo.nodeHeight,
        }
      });
      currentXMethodPosition += methodInfo.nodeWidth + METHOD_SPACING_HORIZONTAL;
    });

    // Memperbarui posisi Y untuk grup kelas berikutnya
    currentYPosition += finalGroupHeight + CLASS_SPACING_VERTICAL;
  });

  // 2. Process Standalone Functions
  functionResult.forEach((funcItem:BackendFunctionItem) => {
      console.log("Processing function item:", Object.keys(funcItem)[0]);
      const funcName = Object.keys(funcItem)[0]; // Ambil nama fungsi dari key pertama
      const svgContent = funcItem[funcName] || "";
      // console.log(`Processing function: ${funcName}, SVG content length: ${svgContent}`);
      const { width: svgWidth, height: svgHeight } = getSvgDimensions(svgContent);

      const contentNodeWidth = svgWidth + SVG_NODE_EXTRA_WIDTH_PADDING;
      const contentNodeHeight = svgHeight + SVG_NODE_EXTRA_HEIGHT_PADDING;

      const groupWidth = contentNodeWidth + (GROUP_INTERNAL_PADDING_HORIZONTAL * 2);
      const groupHeight = CLASS_LABEL_HEADER_HEIGHT + contentNodeHeight + (GROUP_INTERNAL_PADDING_VERTICAL * 2);

      const funcGroupId = `group-func-${funcName}`;
      nodesArray.push({
          id: funcGroupId,
          type: 'classGroup',
          position: { x: 100, y: currentYPosition },
          style: { width: groupWidth, height: groupHeight },
          data: { label: funcName, category: 'function', svg: svgContent, width: groupWidth, height: groupHeight },
      });
      currentYPosition += groupHeight + CLASS_SPACING_VERTICAL;
  });

  console.log('main ressss ', typeof mainResult);
  if(mainResult){
    console.log("Processing main result:", mainResult);
    const mainSvgContent = mainResult || "";
    const { width: mainSvgWidth, height: mainSvgHeight } = getSvgDimensions(mainSvgContent);

    const contentNodeWidth = mainSvgWidth + SVG_NODE_EXTRA_WIDTH_PADDING;
    const contentNodeHeight = mainSvgHeight + SVG_NODE_EXTRA_HEIGHT_PADDING;

    const groupWidth = contentNodeWidth + (GROUP_INTERNAL_PADDING_HORIZONTAL * 2);
    const groupHeight = CLASS_LABEL_HEADER_HEIGHT + contentNodeHeight + (GROUP_INTERNAL_PADDING_VERTICAL * 2);

    const mainGroupId = `group-main`;
    nodesArray.push({
        id: mainGroupId,
        type: 'classGroup',
        position: { x: 100, y: currentYPosition },
        style: { width: groupWidth, height: groupHeight },
        data: { label: 'Main', category: 'main', svg: mainSvgContent, width: groupWidth, height: groupHeight },
    });
    currentYPosition += groupHeight + CLASS_SPACING_VERTICAL;
  }

  return { nodes: nodesArray, edges: edgesArray };
}
