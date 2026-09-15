# Direktori Alternatif Perisian Sumber Terbuka
## Open-Source Alternative Directory

Direktori ini menyediakan alternatif perisian sumber terbuka (*Free and Open Source Software - FOSS*) yang matang, selamat, dan berdaya saing untuk menggantikan perkhidmatan monopoli Big Tech (Google, Amazon, Microsoft, Meta). 

Setiap cadangan dinilai berdasarkan tahap kematangan, tahap kesukaran pelaksanaan, privasi, dan kesesuaian bagi individu, PKS, serta institusi awam di Malaysia.

---

## Ringkasan 17 Kategori Perisian

| Kategori | Perkhidmatan Big Tech Diganti | Alternatif Sumber Terbuka Utama | Tahap Kesukaran | Privasi & Kedaulatan |
| :--- | :--- | :--- | :--- | :--- |
| **1. Carian (Search)** | Google Search, Bing | **SearXNG** | Mudah (Beginner) | Sifar Penjejakan (*Zero Tracking*) |
| **2. E-mel** | Gmail Workspace, Outlook 365 | **Mailcow, Thunderbird** | Sederhana (Intermediate) | Kedaulatan Premis Penuh |
| **3. Storan Awan** | Google Drive, OneDrive, S3 | **Nextcloud Hub, MinIO** | Sederhana (Intermediate) | Enkripsi Hujung-ke-Hujung |
| **4. Suite Pejabat** | Google Docs/Sheets, MS 365 | **LibreOffice, OnlyOffice** | Mudah (Beginner) | Format Terbuka ODF, Luar Talian |
| **5. Sidang Video** | Zoom, Google Meet, Teams | **Jitsi Meet** | Sederhana (Intermediate) | Tanpa Akaun, E2EE |
| **6. Pemesejan** | WhatsApp, Slack, Teams Chat | **Matrix / Element, Signal** | Sederhana (Intermediate) | Protokol Terbuka Terdesentralisasi |
| **7. Media Sosial** | X, Facebook, Instagram, YouTube | **Mastodon, PeerTube** | Sederhana (Intermediate) | Tiada Algoritma Manipulasi |
| **8. Sistem Operasi** | Windows 11, macOS, ChromeOS | **Debian, Ubuntu LTS, Linux Mint** | Mudah (Beginner) | Bebas Telemetri, Tiada Yuran Lesen |
| **9. Infrastruktur Awan** | AWS EC2, GCP Compute, Azure VMs | **OpenStack, Proxmox VE** | Lanjutan (Advanced) | Kedaulatan Pusat Data Tempatan |
| **10. Orkestrasi K8s** | AWS EKS, Google GKE, Terraform | **Kubernetes, K3s, OpenTofu** | Lanjutan (Advanced) | Piawaian Terbuka CNCF |
| **11. Kecerdasan Buatan (AI)** | ChatGPT, Google Gemini, Copilot | **Ollama, LocalAI, vLLM** | Mudah (Beginner) | 100% Data Kekal Dalam Memori Tempatan |
| **12. Penjanaan Imej** | Midjourney, DALL-E 3, Imagen | **ComfyUI, Stable Diffusion** | Sederhana (Intermediate) | Luar Talian, Hak Cipta Bebas |
| **13. Penjanaan Video** | Runway Gen-3, OpenAI Sora | **CogVideoX, AnimateDiff** | Lanjutan (Advanced) | Model Terbuka (*Open Weights*) |
| **14. Pangkalan Data** | AWS Aurora, Cloud SQL, MS SQL | **PostgreSQL, MariaDB** | Sederhana (Intermediate) | Standard Emas SQL, Bebas Lesen |
| **15. DevOps & CI/CD** | GitHub Enterprise, Azure DevOps | **Forgejo, Woodpecker CI** | Sederhana (Intermediate) | Perlindungan Harta Intelek Kod |
| **16. Pemantauan (Monitoring)**| Datadog, AWS CloudWatch | **Prometheus, Grafana (OSS)** | Sederhana (Intermediate) | Telemetri Tertutup Dalam Rangkaian |
| **17. Pengesahan (Auth)** | Okta, Azure AD / Entra ID | **Keycloak, Authelia** | Lanjutan (Advanced) | Sedia MyDigital ID, FIDO2 |

---

## Huraian Terperinci Mengikut Domain Penggunaan

### 1. Komunikasi & Pejabat Harian (Untuk Semua Rakyat & PKS)
* **LibreOffice:** Pengganti Microsoft Office paling stabil di dunia. Berjalan sepenuhnya di komputer tanpa memerlukan sambungan internet atau langganan bulanan. Mendukung format `.docx`, `.xlsx`, dan `.pdf`.
* **Thunderbird:** Klien e-mel sumber terbuka daripada Yayasan Mozilla. Membolehkan pengurusan pelbagai akaun e-mel secara selamat tanpa imbasan pengiklanan.
* **Signal & Element (Matrix):** Mengurangkan kebergantungan kepada WhatsApp. Signal menawarkan privasi perbualan tertinggi untuk individu, manakala Matrix membolehkan syarikat dan jabatan menubuhkan pelayan pemesejan dalaman sendiri.

### 2. Penggantian Google Workspace & Microsoft 365 (Institusi & Sekolah)
* **Nextcloud Hub:** Ekosistem lengkap yang merangkumi storan fail, kalendar, kenalan, borang bancian, sembang pasukan, dan penyuntingan dokumen langsung melalui integrasi OnlyOffice/Collabora.
* **Kelebihan untuk Malaysia:** Satu pelayan Nextcloud di pusat data tempatan (seperti AIMS atau TM One) mampu menyokong ribuan staf jabatan kerajaan dengan kos pelayan tetap dalam mata wang Ringgit Malaysia, mengelakkan bayaran \$6–\$18 USD setiap pengguna sebulan kepada Google/Microsoft.

### 3. Kecerdasan Buatan (AI) Berdaulat & Privasi Data
* **Ollama:** Membolehkan model bahasa raya (LLM) seperti Llama 3, DeepSeek, dan Mistral dijalankan secara tempatan di komputer riba atau pelayan organisasi.
* **Mengapa ini kritikal?** Peguam, doktor, dan penjawat awam yang memasukkan dokumen sulit, rekod pesakit, atau draf rang undang-undang ke dalam ChatGPT atau Gemini mendedahkan data tersebut ke pelayan asing. Dengan Ollama, data tidak pernah keluar dari komputer pengguna.

### 4. Infrastruktur Awan & Pusat Data (Jurutera & DevOps)
* **Proxmox VE & OpenStack:** Menghapuskan kebergantungan kepada VMware dan perkhidmatan mesin maya AWS. Menyokong penskalaan daripada pelayan tunggal di pejabat kecil sehingga ke ratusan nod di pusat data nasional.
* **OpenTofu:** Cabang sumber terbuka tulen kepada Terraform di bawah naungan Linux Foundation, menjamin kebebasan kod infrastruktur tanpa risiko perubahan lesen proprietari.
