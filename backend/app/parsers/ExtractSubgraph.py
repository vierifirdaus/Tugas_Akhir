def extract_subgraph(konten_file):
    hasil = []
    level_kurawal = 0
    dalam_kutipan = False
    i = 0
    panjang_konten = len(konten_file)

    while i < panjang_konten:
        char = konten_file[i]

        if char == '"' and (i == 0 or konten_file[i-1] != '\\'):
            dalam_kutipan = not dalam_kutipan
        
        if not dalam_kutipan:
            if konten_file[i:i+9] == "subgraph " and level_kurawal == 1:
                indeks_awal_blok = i
                try:
                    indeks_kurawal_buka = konten_file.find('{', indeks_awal_blok)
                except ValueError:
                    i += 1
                    continue

                level_kurawal_lokal = 1
                for j in range(indeks_kurawal_buka + 1, panjang_konten):
                    char_lokal = konten_file[j]
                    if char_lokal == '"' and (j == 0 or konten_file[j-1] != '\\'):
                        dalam_kutipan = not dalam_kutipan
                    
                    if not dalam_kutipan:
                        if char_lokal == '{':
                            level_kurawal_lokal += 1
                        elif char_lokal == '}':
                            level_kurawal_lokal -= 1
                    
                    if level_kurawal_lokal == 0:
                        indeks_akhir_blok = j
                        blok_ditemukan = konten_file[indeks_awal_blok : indeks_akhir_blok + 1]
                        hasil.append(blok_ditemukan) # Perhatikan: tidak ada .strip() agar replace presisi
                        i = indeks_akhir_blok
                        break
                dalam_kutipan = False

            elif char == '{':
                level_kurawal += 1
            elif char == '}':
                level_kurawal -= 1
        
        i += 1
    return hasil