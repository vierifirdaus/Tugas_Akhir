import { X } from "lucide-react";

interface LegendModalProps {
  onClose: () => void;
}

export const LegendModal: React.FC<LegendModalProps> = ({ onClose }) => {
  // Daftar item legenda. Anda bisa mengisinya sesuai dengan jenis node/edge yang Anda miliki.
  const legendItems = [
    { color: 'bg-sky-200', text: 'Node Tipe A: Representasi Awal Proses' },
    { color: 'bg-emerald-200', text: 'Node Tipe B: Tahapan Proses' },
    { color: 'bg-amber-200', text: 'Node Tipe C: Hasil atau Output' },
    { symbol: 'Garis Penuh', text: 'Edge Solid: Alur data langsung' },
    { symbol: 'Garis Putus-putus', text: 'Edge Dashed: Alur data opsional' },
  ];

  return (
    // Overlay latar belakang
    <div 
        className="fixed inset-0 bg-black/20 backdrop-blur-sm z-50 flex justify-center items-center p-4"
        onClick={onClose}
    >
      {/* Kontainer konten modal */}
      <div 
        className="bg-white rounded-lg shadow-xl max-w-lg w-full p-6 relative"
        onClick={(e) => e.stopPropagation()} // Mencegah penutupan modal saat mengklik di dalam konten
      >
        {/* Tombol Close di pojok kanan atas */}
        <button 
          onClick={onClose} 
          className="absolute top-3 right-3 text-slate-500 hover:text-slate-800"
          aria-label="Tutup"
        >
          <X size={24} />
        </button>

        <h3 className="text-xl font-bold text-slate-800 mb-4">Legenda</h3>
        
        <div className="space-y-3">
          {legendItems.map((item, index) => (
            <div key={index} className="flex items-center space-x-3">
              {item.color && (
                <div className={`w-5 h-5 rounded-sm border border-slate-300 ${item.color}`}></div>
              )}
              {item.symbol === 'Garis Penuh' && (
                <div className="w-5 h-px bg-black"></div>
              )}
               {item.symbol === 'Garis Putus-putus' && (
                 <div className="w-5 border-t-2 border-dashed border-black"></div>
              )}
              <span className="text-sm text-slate-600">{item.text}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};