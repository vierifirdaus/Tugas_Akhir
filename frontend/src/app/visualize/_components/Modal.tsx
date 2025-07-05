import { X } from "lucide-react";
import { JSX } from "react";

interface LegendModalProps {
  onClose: () => void;
}

// Data untuk item legenda
const containerItems = [
  { color: 'bg-green-200 border-green-400', text: 'Class Container' },
  { color: 'bg-blue-200 border-blue-400', text: 'Method Container' },
  { color: 'bg-yellow-200 border-yellow-400', text: 'Function Container' },
  { color: 'bg-gray-800 border-gray-500', text: 'Main Code Container' },
];

const nodeItems = [
  { shape: 'if', text: 'If Statement' },
  { shape: 'for', text: 'For Loop' },
  { shape: 'while', text: 'While Loop' },
  { shape: 'try', text: 'Try-Except Block' },
  { shape: 'input', text: 'Input/Assignment' },
  { shape: 'return', text: 'Return Statement' },
  { shape: 'raise', text: 'Raise Exception' },
  { shape: 'call', text: 'Function/Method Call' },
  { shape: 'default', text: 'Default Statement' },
];

const edgeItems = [
  { color: 'border-green-500', style: 'solid', text: 'Program Dependency Graph (PDG)' },
  { color: 'border-blue-500', style: 'solid', text: 'Call Graph (CG)' },
  { color: 'border-black', style: 'solid', text: 'Control Flow (CFG)' },
  { color: 'border-red-500', style: 'solid', text: 'False Branch (CFG)' },
];


// Komponen untuk merepresentasikan bentuk node
const NodeShape = ({ shape }: { shape: string }) => {
    // Style dasar untuk semua bentuk
    const baseStyle = "w-10 h-6 border-2 border-black flex items-center justify-center text-xs font-semibold";
    
    // SVG inline untuk bentuk kustom
    const shapes: { [key: string]: JSX.Element } = {
        'if': <div className={`${baseStyle} bg-red-200 -skew-x-20 -skew-y-20 rotate-45 transform scale-75`}><span className="-rotate-45 skew-x-20 skew-y-20">if</span></div>,
        'for': <div className={`${baseStyle} bg-orange-200`} style={{clipPath: "polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%)"}}>for</div>,
        'while': <div className={`${baseStyle} bg-orange-200`} style={{clipPath: "polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%)"}}>while</div>,
        'try': <div className={`${baseStyle} bg-orange-300 transform scale-90`} style={{clipPath: "polygon(0% 50%, 15% 0%, 85% 0%, 100% 50%, 85% 100%, 15% 100%)"}}>try</div>,
        'input': <div className={`${baseStyle} bg-cyan-200 -skew-x-20`}></div>,
        'return': <div className={`${baseStyle} bg-green-300 -skew-x-20`}></div>,
        'raise': <div className={`${baseStyle} bg-green-200`} style={{clipPath: "polygon(0% 0%, 100% 0%, 100% 75%, 50% 100%, 0% 75%)"}}></div>,
        'call': <div className={`${baseStyle} bg-purple-300`}><div className="w-3 h-2 bg-purple-300 border-2 border-black absolute -top-1 -left-1"></div></div>,
        'default': <div className={`${baseStyle} bg-yellow-200`}></div>,
    };
    
    return shapes[shape] || null;
}


export const LegendModal: React.FC<LegendModalProps> = ({ onClose }) => {
  return (
    <div 
      className="fixed inset-0 bg-black/30 backdrop-blur-sm z-50 flex justify-center items-center p-4"
      onClick={onClose}
    >
      <div 
        className="bg-white rounded-lg shadow-xl max-w-md w-full p-6 relative"
        onClick={(e) => e.stopPropagation()}
      >
        <button 
          onClick={onClose} 
          className="absolute top-3 right-3 text-slate-500 hover:text-slate-800 p-1 rounded-full hover:bg-slate-100"
          aria-label="Tutup"
        >
          <X size={24} />
        </button>

        <h3 className="text-2xl font-bold text-slate-800 mb-6 border-b pb-2">Legenda</h3>
        
        {/* Bagian Kontainer */}
        <div className="mb-6">
            <h4 className="font-bold text-slate-700 mb-3">Container</h4>
            <div className="grid grid-cols-2 gap-x-4 gap-y-2">
                {containerItems.map((item, index) => (
                    <div key={index} className="flex items-center space-x-3">
                        <div className={`w-5 h-5 rounded-sm border-2 ${item.color}`}></div>
                        <span className="text-sm text-slate-600">{item.text}</span>
                    </div>
                ))}
            </div>
        </div>
        
        {/* Bagian Node */}
        <div className="mb-6">
            <h4 className="font-bold text-slate-700 mb-3">Node</h4>
            <div className="grid grid-cols-2 gap-x-4 gap-y-3">
                {nodeItems.map((item, index) => (
                    <div key={index} className="flex items-center space-x-3">
                        <div className="w-12 flex justify-center"><NodeShape shape={item.shape} /></div>
                        <span className="text-sm text-slate-600">{item.text}</span>
                    </div>
                ))}
            </div>
        </div>

        {/* Bagian Edge */}
        <div>
            <h4 className="font-bold text-slate-700 mb-3">Edge (Garis Penghubung)</h4>
            <div className="space-y-3">
                {edgeItems.map((item, index) => (
                    <div key={index} className="flex items-center space-x-3">
                        <div className="w-8 flex items-center">
                            <div className={`w-full border-t-2 ${item.color} ${item.style === 'dashed' ? 'border-dashed' : 'border-solid'}`}></div>
                        </div>
                        <span className="text-sm text-slate-600">{item.text}</span>
                    </div>
                ))}
            </div>
        </div>

      </div>
    </div>
  );
};