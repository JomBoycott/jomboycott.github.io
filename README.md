# Kempen Akauntabiliti Teknologi Sumber Terbuka Malaysia
## Malaysian Open-Source Tech Accountability Campaign

> **"Dan hendaklah kamu tolong-menolong untuk membuat kebajikan dan bertakwa, dan janganlah kamu tolong-menolong pada melakukan dosa dan pencerobohan."**  
> — *Surah Al-Ma'idah 5:2*

> **"Help your brother, whether he is an oppressor or he is oppressed." A man said: "O Messenger of Allah, I help him when he is oppressed, but how can I help him when he is an oppressor?" The Prophet ﷺ said: "By stopping him from oppressing others."**  
> — *Sahih al-Bukhari 2444*

---

### Dual Language / Dwi-Bahasa
* [Bahasa Melayu](#ringkasan-eksekutif-bm)
* [English](#executive-summary-en)

---

<a name="ringkasan-eksekutif-bm"></a>
## Ringkasan Eksekutif (Bahasa Melayu)

Kempen Akauntabiliti Teknologi Sumber Terbuka Malaysia ialah sebuah inisiatif penyelidikan awam berasaskan bukti dan beretika yang meneliti hubungan antara gergasi teknologi global (khususnya Google/Alphabet, Amazon/AWS, Microsoft, dan Meta) dengan aparatus ketenteraan, risikan, dan pentadbiran Israel dalam konteks pendudukan dan peperangan di Palestin.

Kempen ini digerakkan di atas dua tunjang utama:
1. **Keadilan & Akauntabiliti Teknologi Global:** Menuntut ketelusan dan menolak keterlibatan infrastruktur digital, perkhidmatan awan (*cloud*), dan kecerdasan buatan (*AI*) dalam penindasan terhadap rakyat Palestin.
2. **Kedaulatan Digital Malaysia (*Malaysian Digital Sovereignty*):** Membebaskan infrastruktur digital, sektor awam, universiti, PKS, dan rakyat Malaysia daripada kebergantungan melampau kepada monopoli syarikat teknologi asing melalui penggunaan dan pembangunan perisian sumber terbuka (*Free and Open Source Software - FOSS*), pusat data tempatan, dan infrastruktur berdaulat.

### Disiplin Penyelidikan yang Ketat
Kempen ini berpegang teguh pada prinsip **TIDAK MEREKA KEPASTIAN (*Do not manufacture certainty*)**. Kami membezakan secara tegas antara:
* **Fakta Disahkan (*Verified Fact*):** Disokong secara langsung oleh dokumen rasmi kerajaan, keputusan mahkamah antarabangsa (ICJ/ICC), laporan PBB, pemfailan korporat, atau kontrak perolehan yang sah.
* **Laporan Berasas Kukuh (*Strongly Supported Reporting*):** Disokong oleh pelbagai sumber kewartawanan penyiasatan bebas yang berwibawa (*The Guardian, Reuters, AP, FT, Bloomberg, +972 Magazine*).
* **Dakwaan (*Allegation*):** Dakwaan oleh organisasi hak asasi yang berwibawa di mana fakta dasar masih dipertikaikan atau belum lengkap.
* **Tafsiran (*Interpretation*):** Analisis berhujah berasaskan fakta yang kukuh.
* **Pendapat Kempen (*Campaign Opinion*):** Kesimpulan etika dan advokasi kempen.

Kami menolak sekeras-kerasnya sebarang bentuk antisemitisme, perkauman, kebencian kaum atau agama. Kami membezakan secara jelas antara:
* Kerajaan ≠ Rakyat
* Tentera ≠ Etnik
* Perbadanan ≠ Pekerja
* Penganut Yahudi ≠ Kerajaan Israel
* Orang Awam ≠ Pasukan Tentera

---

<a name="executive-summary-en"></a>
## Executive Summary (English)

The Malaysian Open-Source Tech Accountability Campaign is an independent, open-source, evidence-driven public inquiry into the relationships connecting multinational technology corporations (specifically Google, Amazon/AWS, Microsoft, and Meta) to the Israeli state, military, and intelligence infrastructure.

The campaign is built on two interlinked pillars:
1. **Ethical Technology & Palestine:** Documenting corporate complicity, cloud hosting, AI services, surveillance contracts, and content suppression impacting Palestinians, in light of universal human rights and Islamic ethics.
2. **Malaysian Digital Sovereignty:** Fostering practical resilience, local data sovereignty, and technological autonomy by transitioning public institutions, SMEs, students, and citizens away from foreign Big Tech monopolies toward verifiable open-source software and domestic infrastructure.

---

## Struktur Repositori / Repository Structure

```text
.
├── README.md                              # Dokumentasi utama / Main overview (BM & EN)
├── LICENSE                                # CC-BY-SA 4.0 (Kandungan) & MIT (Kod)
├── CAMPAIGN_MASTER_REPORT.md              # Laporan Induk Kempen (Master Report)
│
├── research/                              # Dosier Penyelidikan Mendalam
│   ├── google/dossier.md                  # Project Nimbus, kontrak kementerian pertahanan, pekerja
│   ├── amazon/dossier.md                  # AWS Nimbus, rantau Tel Aviv, infrastruktur awan
│   ├── microsoft/dossier.md               # Azure, sekatan teknologi pengawasan 2025, semakan bebas
│   ├── meta/dossier.md                    # Penyederhanaan kandungan, laporan HRW & BSR, Lembaga Pengawasan
│   ├── malaysia/dossier.md                # Dasar Cloud First, kebergantungan, Akta CLOUD AS, kedaulatan data
│   └── israel-palestine/tech_context.md   # Ekosistem teknologi risikan, AI tentera, konteks undang-undang
│
├── islamic-foundation/                    # Asas & Hujah Syariah Ahli Sunnah Wal Jamaah
│   ├── quran.md                           # Surah Al-Ma'idah 5:2, An-Nisa' 4:75 & 4:135
│   ├── hadith.md                          # Sahih al-Bukhari 2444 (Tolong saudaramu yang zalim/dizalimi)
│   ├── tafsir.md                          # Tafsir Ibn Kathir, As-Sa'di, Al-Qurtubi
│   └── ethics.md                          # Prinsip etika, fiqh muamalat, larangan bersubahat, tolak perkauman
│
├── evidence/                              # Pangkalan Data Bukti Berstruktur
│   ├── schema.json                        # Skema pengesahan JSON (7 status piawai)
│   └── evidence.json                      # Rekod bukti disahkan dengan petikan sumber primer
│
├── alternatives/                          # Direktori Alternatif Sumber Terbuka & Laluan Migrasi
│   ├── schema.json                        # Skema direktori perisian
│   ├── alternatives.json                  # 17 kategori perisian sumber terbuka & penarafan kesesuaian Malaysia
│   ├── directory.md                       # Panduan direktori perisian
│   └── migration_guide.md                 # Laluan 6-Tahap Keluar dari Big Tech (Exit Big Tech)
│
├── campaign/                              # Bahan Kempen & Advokasi Awam (BM & EN)
│   ├── branding.md                        # Penilaian 20+ nama kempen, tanda dagang, analisis domain
│   ├── audiences.md                       # Strategi pemesejan untuk 5 kumpulan sasaran (A hingga E)
│   ├── pamphlets/                         # Risalah satu halaman ringkas (≤ 500 patah perkataan)
│   ├── leaflets/                          # Risalah lipat dua halaman (depan & belakang)
│   ├── factsheets/                        # Lembaran fakta syarikat (Google, Amazon, Microsoft, Meta)
│   ├── social/                            # Skrip karusel media sosial 10 slaid
│   └── infographics/                      # Spesifikasi susun atur Infografik 01 hingga 08
│
├── sources/                               # Hierarki Sumber & Bibliografi
│   └── bibliography.md                    # Rujukan Tahap 1, 2, 3, dan 4
│
├── scripts/                               # Skrip Pengesahan Automatik
│   ├── validate.py                        # Ujian integriti skema JSON, status bukti, dan pautan markdown
│   └── export_summary.py                  # Penjanaan ringkasan statistik
│
└── website/                               # Laman Web Statik Responsif Sumber Terbuka
    ├── index.html                         # Halaman Utama
    ├── about.html                         # Misi, falsafah, dan etika
    ├── evidence.html                      # Penjelajah pangkalan data bukti interaktif
    ├── companies.html                     # Ringkasan syarikat
    ├── islam.html                         # Asas etika Islam
    ├── malaysia.html                      # Kedaulatan Digital Malaysia
    ├── alternatives.html                  # Direktori alternatif interaktif
    ├── migrate.html                       # Panduan migrasi interaktif
    ├── research.html                      # Metodologi penyelidikan
    ├── sources.html                       # Bibliografi lengkap
    ├── faq.html                           # Soalan Lazim & Jawapan Hujah Lawan
    ├── styles.css                         # CSS moden, bersih & mesra mod gelap
    └── app.js                             # Logik carian, penapisan & pertukaran bahasa
```

---

## Cara Menjalankan Ujian Pengesahan / How to Run Validation

Projek ini dilengkapi dengan skrip pengesahan automatik untuk memastikan tiada bukti yang tidak berdaftar dan format fail kekal mematuhi skema:

```bash
# Menjalankan ujian pengesahan penuh
python3 scripts/validate.py
```

---

## Sumbangan / Contributing

Kami mengalu-alukan sumbangan daripada penyelidik, jurutera perisian, peguam, dan aktivis masyarakat. Sila pastikan setiap bukti baharu yang dicadangkan disertakan dengan pautan sumber Tahap 1 atau Tahap 2 yang sah dan tidak melanggar tataetika penyelidikan kempen ini.
