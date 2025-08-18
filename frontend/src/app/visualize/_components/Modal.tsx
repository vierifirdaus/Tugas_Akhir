import { X } from "lucide-react";
import { JSX } from "react";

interface LegendModalProps {
  onClose: () => void;
}

/* ========= Data ========= */
const containerItems = [
  { color: "bg-green-200 border-green-400", text: "Class Container" },
  { color: "bg-blue-200 border-blue-400", text: "Method Container" },
  { color: "bg-yellow-200 border-yellow-400", text: "Function Container" },
  { color: "bg-slate-800 border-slate-500", text: "Main Code Container" },
];

const nodeItems: { shape: NodeKind; text: string }[] = [
  { shape: "if", text: "If Statement" },
  { shape: "for", text: "For Loop" },
  { shape: "while", text: "While Loop" },
  { shape: "try", text: "Try-Except Block" },
  { shape: "input", text: "Input/Assignment" },
  { shape: "return", text: "Return Statement" },
  { shape: "raise", text: "Raise Exception" },
  { shape: "default", text: "Default Statement" },
];

const edgeItems = [
  { stroke: "#22c55e", dash: false, text: "Program Dependency Graph (PDG)" }, // green-500
  { stroke: "#3b82f6", dash: false, text: "Call Graph (CG)" },               // blue-500
  { stroke: "#0f172a", dash: false, text: "Control Flow (CFG)" },            // slate-900
  { stroke: "#ef4444", dash: true,  text: "False Branch (CFG)" },            // red-500
];

/* ========= Node Shapes (SVG) ========= */
type NodeKind =
  | "if" | "for" | "while" | "try"
  | "input" | "return" | "raise"
  | "call" | "default";

const labelStyle =
  "font-semibold text-[10px] leading-none fill-slate-800 pointer-events-none";

function NodeShape({ kind }: { kind: NodeKind }) {
  // semua ikon 56x28 agar konsisten
  const W = 56, H = 28, stroke = "#0f172a";

  const common = { stroke, strokeWidth: 2 } as const;

  switch (kind) {
    case "if": // diamond
      return (
        <svg width={W} height={H} viewBox="0 0 56 28">
          <polygon
            points="28,2 54,14 28,26 2,14"
            fill="#fecaca" /* red-200 */
            {...common}
          />
          <text x="28" y="16" textAnchor="middle" className={labelStyle}>if</text>
        </svg>
      );

    case "for": // hexagon
      return (
        <svg width={W} height={H} viewBox="0 0 56 28">
          <polygon
            points="10,2 46,2 54,14 46,26 10,26 2,14"
            fill="#fed7aa" /* orange-200 */
            {...common}
          />
          <text x="28" y="16" textAnchor="middle" className={labelStyle}>for</text>
        </svg>
      );

    case "while": // hexagon
      return (
        <svg width={W} height={H} viewBox="0 0 56 28">
          <polygon
            points="10,2 46,2 54,14 46,26 10,26 2,14"
            fill="#fed7aa"
            {...common}
          />
          <text x="28" y="16" textAnchor="middle" className={labelStyle}>while</text>
        </svg>
      );

    case "try": // hexagon (warna berbeda)
      return (
        <svg width={W} height={H} viewBox="0 0 56 28">
          <polygon
            points="10,2 46,2 54,14 46,26 10,26 2,14"
            fill="#fbbf24" /* amber-400-ish */
            {...common}
          />
          <text x="28" y="16" textAnchor="middle" className={labelStyle}>try</text>
        </svg>
      );

    case "input": // parallelogram
      return (
        <svg width={W} height={H} viewBox="0 0 56 28">
          <polygon
            points="8,2 56,2 48,26 0,26"
            fill="#bae6fd" /* sky-200 */
            {...common}
          />
        </svg>
      );

    case "return": // parallelogram (hijau)
      return (
        <svg width={W} height={H} viewBox="0 0 56 28">
          <polygon
            points="8,2 56,2 48,26 0,26"
            fill="#86efac" /* green-300 */
            {...common}
          />
        </svg>
      );

    case "raise": // pentagon
      return (
        <svg width={W} height={H} viewBox="0 0 56 28">
          <polygon
            points="2,2 54,2 54,18 28,26 2,18"
            fill="#bbf7d0" /* green-200 */
            {...common}
          />
        </svg>
      );

    case "call": // rectangle with tab
      return (
        <svg width={W} height={H} viewBox="0 0 56 28">
          <rect x="2" y="6" width="52" height="20" rx="2" ry="2"
                fill="#e9d5ff" /* purple-200 */ {...common} />
          <rect x="6" y="2" width="12" height="8" rx="1" ry="1"
                fill="#e9d5ff" {...common} />
        </svg>
      );

    case "default": // plain rectangle
      return (
        <svg width={W} height={H} viewBox="0 0 56 28">
          <rect x="2" y="2" width="52" height="24" rx="3" ry="3"
                fill="#fef08a" /* yellow-200 */ {...common} />
        </svg>
      );
  }
}

/* ========= Edge legend (SVG) ========= */
function EdgeSample({ stroke, dash = false }: { stroke: string; dash?: boolean }) {
  return (
    <svg width="64" height="14" viewBox="0 0 64 14">
      <defs>
        <marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3"
          orient="auto" markerUnits="strokeWidth">
          <path d="M0,0 L0,6 L9,3 z" fill={stroke} />
        </marker>
      </defs>
      <line
        x1="2" y1="7" x2="58" y2="7"
        stroke={stroke}
        strokeWidth="2.5"
        strokeDasharray={dash ? "6 4" : "0"}
      />
    </svg>
  );
}

/* ========= Modal ========= */
export const LegendModal: React.FC<LegendModalProps> = ({ onClose }) => {
  return (
    <div
      className="fixed inset-0 bg-black/30 backdrop-blur-sm z-50 flex justify-center items-center p-4"
      onClick={onClose}
    >
      <div
        className="bg-white rounded-xl shadow-2xl w-full max-w-lg p-6 relative max-h-[90vh] overflow-auto"
        onClick={(e) => e.stopPropagation()}
      >
        <button
          onClick={onClose}
          className="absolute top-3 right-3 text-slate-500 hover:text-slate-800 p-1 rounded-full hover:bg-slate-100"
          aria-label="Tutup"
        >
          <X size={22} />
        </button>

        <h3 className="text-2xl font-bold text-slate-900 mb-6 border-b pb-3">Legenda</h3>

        {/* Container */}
        <section className="mb-6">
          <h4 className="font-semibold text-slate-800 mb-3">Container</h4>
          <div className="grid grid-cols-2 gap-x-4 gap-y-2">
            {containerItems.map((it, i) => (
              <div key={i} className="flex items-center gap-3">
                <div className={`w-5 h-5 rounded-sm border-2 ${it.color}`} />
                <span className="text-sm text-slate-700">{it.text}</span>
              </div>
            ))}
          </div>
        </section>

        {/* Node */}
        <section className="mb-6">
          <h4 className="font-semibold text-slate-800 mb-3">Node</h4>
          <div className="grid grid-cols-2 gap-x-4 gap-y-3">
            {nodeItems.map((n, i) => (
              <div key={i} className="flex items-center gap-3">
                <NodeShape kind={n.shape} />
                <span className="text-sm text-slate-700">{n.text}</span>
              </div>
            ))}
          </div>
        </section>

        {/* Edge */}
        <section>
          <h4 className="font-semibold text-slate-800 mb-3">Edge (Garis Penghubung)</h4>
          <div className="space-y-3">
            {edgeItems.map((e, i) => (
              <div key={i} className="flex items-center gap-3">
                <EdgeSample stroke={e.stroke} dash={e.dash} />
                <span className="text-sm text-slate-700">{e.text}</span>
              </div>
            ))}
          </div>
        </section>
      </div>
    </div>
  );
};
