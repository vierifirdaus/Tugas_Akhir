def extract_subgraph(file_content):
    result = []
    brace_level = 0
    in_quotes = False
    i = 0
    content_length = len(file_content)

    while i < content_length:
        char = file_content[i]

        if char == '"' and (i == 0 or file_content[i-1] != '\\'):
            in_quotes = not in_quotes
        
        if not in_quotes:
            if file_content[i:i+9] == "subgraph " and brace_level == 1:
                block_start_index = i
                try:
                    open_brace_index = file_content.find('{', block_start_index)
                except ValueError:
                    i += 1
                    continue

                local_brace_level = 1
                for j in range(open_brace_index + 1, content_length):
                    local_char = file_content[j]
                    if local_char == '"' and (j == 0 or file_content[j-1] != '\\'):
                        in_quotes = not in_quotes
                    
                    if not in_quotes:
                        if local_char == '{':
                            local_brace_level += 1
                        elif local_char == '}':
                            local_brace_level -= 1
                    
                    if local_brace_level == 0:
                        block_end_index = j
                        found_block = file_content[block_start_index : block_end_index + 1]
                        result.append(found_block) 
                        i = block_end_index
                        break
                in_quotes = False

            elif char == '{':
                brace_level += 1
            elif char == '}':
                brace_level -= 1
        
        i += 1
    return result

def hapus_subgraph_dan_cetak(konten_asli):
    """
    Fungsi utama yang membaca file, menghapus subgraph terluar, 
    dan mencetak hasilnya.
    """
    try:
        # 1. Temukan semua blok subgraph terluar
        blok_untuk_dihapus = extract_subgraph(konten_asli)
        konten_telah_dimodifikasi = konten_asli
        
        # 2. Hapus setiap blok yang ditemukan dari konten asli
        for blok in blok_untuk_dihapus:
            konten_telah_dimodifikasi = konten_telah_dimodifikasi.replace(blok, "")
            
        # 3. Membersihkan baris kosong yang mungkin tersisa setelah penghapusan
        baris_bersih = []
        for baris in konten_telah_dimodifikasi.splitlines():
            # Hanya tambahkan baris yang tidak kosong (setelah di-strip)
            if baris.strip():
                baris_bersih.append(baris)
        
        hasil_akhir = "\n".join(baris_bersih)
        return hasil_akhir

    except FileNotFoundError:
        print(f"Error: File dengan nama tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi error: {e}")