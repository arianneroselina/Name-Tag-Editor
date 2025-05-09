
basket_putra_key = "basket_putra"
bulu_tangkis_ganda_putra_key = "bulu_tangkis_ganda_putra"
bulu_tangkis_ganda_campuran_key = "bulu_tangkis_ganda_campuran"
futsal_key = "futsal"
voli_key = "voli"

cabor_keys = [basket_putra_key, bulu_tangkis_ganda_campuran_key, bulu_tangkis_ganda_putra_key, futsal_key, voli_key]

pdf_key = "pdf"

panitia_key = "panitia"
panitia_eng_key = "panitia_eng"

empty_key = "kosong"
empty_participants_key = "kosong_peserta"
empty_committees_key = "kosong_panitia"

ketua_ppi_frada_key = "Ketua PPI Frada"
wakil_ketua_ppi_frada_key = "Wakil Ketua PPI Frada"
ketua_pelaksana_key = "Ketua Pelaksana"
bendahara_key = "Bendahara"
sekretaris_key = "Sekretaris"

acara_key = "Acara"
konsumsi_key = "Konsumsi"
pendaftaran_key = "Pendaftaran"
publikasi_key = "Humas/Publikasi"
kesehatan_key = "Kesehatan"
perlengkapan_key = "Perlengkapan"
keamanan_key = "Keamanan"
lomba_key = "Lomba"
kemitraan_key = "Kemitraan"
bazaar_key = "Bazaar"
medkom_key = "Medkom"
wasit_key = "Wasit"

part_of_dict = {
    basket_putra_key: "MEN'S BASKETBALL",
    bulu_tangkis_ganda_putra_key: "MEN'S DOUBLE BADMINTON",
    bulu_tangkis_ganda_campuran_key: "MIXED DOUBLE BADMINTON",
    futsal_key: "FUTSAL",
    voli_key: "VOLLEYBALL",
    "Basket": lomba_key.upper(),
    "Badminton": lomba_key.upper(),
    "Futsal": lomba_key.upper(),
    "Voli": lomba_key.upper(),
    "Wasit Basket": wasit_key.upper(),
    "Wasit Badminton": wasit_key.upper(),
    "Wasit Futsal": wasit_key.upper(),
    "Wasit Voli": wasit_key.upper(),
    wasit_key: wasit_key.upper(),
    empty_key: empty_key.upper(),
    empty_participants_key: "EMPTY PARTICIPANTS",
    empty_committees_key: "EMPTY COMMITTEES",
}
