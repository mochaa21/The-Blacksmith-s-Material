from typing import List

def cari_material_tempa(material: List[int], target: int) -> List[int]:
    seen = {}
    for i, materi in enumerate(material):
        compliment = target - materi
        if compliment in seen:
            return [seen[compliment], i]
        seen[materi] = i

# --- EKSEKUSI ---
tas_material = [4, 9, 11, 6]
target_elemen = 15
print(cari_material_tempa(tas_material, target_elemen))