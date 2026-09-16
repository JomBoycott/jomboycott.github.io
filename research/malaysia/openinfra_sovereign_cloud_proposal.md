# Penyelidikan OpenInfra & Cadangan Konsortium Awan Berdaulat Terbuka Malaysia (GLC: TNB, PETRONAS, TM)
## OpenInfra Research & Proposal for the Malaysian Sovereign Open Cloud Consortium

> **Klasifikasi Dokumen:** Kertas Penyelidikan Dasar & Seni Bina Teknologi Kebangsaan  
> **Sasaran Pembuat Dasar:** Kementerian Digital Malaysia, Jabatan Digital Negara (JDN), Unit Perancang Ekonomi (EPU), Pengurusan Tertinggi GLC (TNB, PETRONAS, TM)  
> **Status:** Cadangan Advokasi Awam Berasaskan Bukti (September 2026)  
> **Pautan Komuniti Sumber Terbuka Global:** [OpenInfra Foundation (openinfra.org)](https://openinfra.org/)

---

## Dual-Language Executive Summary / Ringkasan Eksekutif Dwi-Bahasa

### Ringkasan Eksekutif (Bahasa Melayu)
Kertas kerja ini mengemukakan pelan strategik menyeluruh untuk membebaskan infrastruktur data dan pengkomputeran awan Malaysia daripada monopoli gergasi teknologi asing (**AWS, Google Cloud, Microsoft Azure**) serta krisis kenaikan harga melampau perisian virtualisasi proprietari (**VMware oleh Broadcom**). 

Penyelesaian yang dicadangkan berteraskan dua tonggak utama:
1. **Pemanfaatan Komuniti & Ekosistem Perisian OpenInfra Foundation (`openinfra.org`):** Melaksanakan komponen perisian sumber terbuka bertaraf dunia yang terbukti di peringkat global—termasuk **OpenStack** (pengganti IaaS penuh AWS/GCP/Azure dan VMware vSphere), **StarlingX** (awan pinggir / *edge cloud* untuk grid elektrik dan telekomunikasi), **Kata Containers** (pengasingan keselamatan kontena berasaskan *microVM*), **Zuul** (enjin CI/CD berskala mega), dan sistem storan teragih **Ceph**.
2. **Penubuhan Badan Telus Kebangsaan — Konsortium Awan Berdaulat Terbuka Malaysia (Malaysian Sovereign Open Infrastructure Consortium - MSOIC):** Menggabungkan kekuatan tiga Syarikat Berkaitan Kerajaan (GLC) terkemuka negara:
   * **Telekom Malaysia (TM):** Menyediakan tulang belakang gentian optik nasional, kabel dasar laut, dan fasiliti pusat data Tier III/IV (KVDC & CJDC).
   * **Tenaga Nasional Berhad (TNB):** Menyediakan bekalan tenaga hijau boleh baharu (solar/hidro) berkarbon rendah, laluan gentian optik OPGW (*Optical Ground Wire*) Allo Technology di sepanjang grid transmisi elektrik ke seluruh pelosok negara, serta ribuan nod pencawang elektrik untuk *edge cloud*.
   * **PETRONAS:** Menyumbang keupayaan modal pelaburan jangka panjang, tadbir urus projek mega, serta membawa beban kerja industri berprestasi tinggi (*High-Performance Computing - HPC* & AI industri).
3. **Penyatuan Dana & Pembangunan Bakat Tempatan:** Mengalihkan sebahagian daripada berbilion Ringgit yuran pelesenan USD yang kini mengalir keluar ke Silicon Valley kepada dana modal tempatan, di samping menubuhkan **Akademi Kejuruteraan Awan Terbuka Kebangsaan** bagi melatih ribuan jurutera tempatan menjadi pembina dan penyumbang kod sumber terbuka global, bukan sekadar pembeli lesen asing.

---

### Executive Summary (English)
This dossier presents an actionable, evidence-based strategic blueprint to liberate Malaysia's digital and cloud infrastructure from foreign hyperscaler monopolies (**AWS, Google Cloud, Microsoft Azure**) and the escalating licensing crisis of proprietary virtualization platforms (**VMware by Broadcom**).

The proposal establishes a two-pronged solution:
1. **Harnessing the OpenInfra Foundation Ecosystem (`openinfra.org`):** Deploying battle-tested, carrier-grade open-source software components—principally **OpenStack** (complete IaaS replacement for AWS/GCP/Azure and VMware vSphere/VCF), **StarlingX** (mission-critical distributed edge cloud), **Kata Containers** (hardware-isolated microVM container runtime), **Zuul** (hyperscale multi-repo CI/CD gating), and **Ceph** (massively scalable distributed storage).
2. **Establishing the Malaysian Sovereign Open Infrastructure Consortium (MSOIC):** A transparent, public-governed entity uniting Malaysia's three industrial giants:
   * **Telekom Malaysia (TM):** National fiber backbone, carrier-neutral interconnects, and established Tier III/IV datacenters (KVDC & CJDC).
   * **Tenaga Nasional Berhad (TNB):** Dedicated green renewable energy (solar, hydro) powering datacenter clusters, extensive nationwide Optical Ground Wire (OPGW) dark fiber via Allo Technology, and thousands of electrical substations acting as StarlingX edge nodes.
   * **PETRONAS:** Sovereign capital capability, mega-project governance, mission-critical High-Performance Computing (HPC) and industrial AI workloads (seismic modeling, reservoir simulation, chemical engineering).
3. **Pooled Sovereign Funding & Local Talent Engine:** Reallocating billions in annual foreign USD licensing fees into a domestic Ringgit-denominated infrastructure fund, complemented by the **National Open Cloud Engineering Academy** to upskill thousands of Malaysian engineers into upstream open-source contributors and kernel-level cloud architects.

---

## Bahagian 1: Latar Belakang & Ekosistem OpenInfra Foundation (`openinfra.org`)

### 1.1 Apakah OpenInfra Foundation?
**OpenInfra Foundation** (dahulunya dikenali sebagai *OpenStack Foundation* sebelum penjenamaan semula pada 2021) ialah sebuah konsortium sumber terbuka antarabangsa yang menaungi pembangunan perisian infrastruktur terbuka untuk dekad akan datang.

* **Skala Komuniti:** Lebih daripada **110,000 ahli individu** merentasi **187 negara**, disokong oleh lebih **700 organisasi korporat dan akademik global**.
* **Jejak Penggunaan Global:** Menjana lebih **45 juta teras CPU (cores)** dalam operasi pengeluaran sebenar di seluruh dunia, termasuk agensi penyelidikan saintifik terbesar dunia (CERN), gergasi telekomunikasi (AT&T, Verizon, China Mobile, Deutsche Telekom, Telstra), bank pusat, dan institusi keselamatan negara.
* **Prinsip Teras "The 4 Opens":**
  1. **Open Source:** Kod dilesenkan di bawah lesen sumber terbuka yang tidak diskriminatif (kebanyakannya Apache 2.0). Tiada perangkap lesen proprietari atau lesen bersyarat (bukan BSL/SSPL).
  2. **Open Design:** Reka bentuk seni bina dan pelan tindakan perisian dirancang secara telus melalui persidangan awam (*Design Summits*) dan undian komuniti.
  3. **Open Development:** Semua semakan kod (*code review*), penjejakan pepijat, dan sejarah pembangunan boleh diakses dan diaudit oleh sesiapa sahaja di seluruh dunia.
  4. **Open Community:** Kepimpinan teknikal dipilih secara demokratik oleh penyumbang aktif; tiada satu syarikat pun boleh memonopoli hala tuju projek.

---

## Bahagian 2: Komponen Perisian OpenInfra & Penggantian AWS, Google, Microsoft, dan VMware

Berikut merupakan pemetaan teknikal terperinci bagaimana perisian di bawah naungan OpenInfra Foundation menggantikan sepenuhnya perkhidmatan komersial proprietari:

### 2.1 Matriks Penggantian Komponen Perisian

| Perkhidmatan Proprietari Asing | Komponen Sumber Terbuka OpenInfra | Huraian Teknikal & Mod Operasi | Kelebihan Kedaulatan & Kebebasan |
| :--- | :--- | :--- | :--- |
| **VMware vSphere / ESXi / vCenter** | **OpenStack Nova (KVM) + Proxmox VE** | Pengurusan virtualisasi hipervisor penuh bagi mesin maya (VM) berskala ribuan nod dengan penjadualan automatik. | Menghapuskan kenaikan kos lesen 300%–1,000% akibat pengambilalihan Broadcom. Kos pelesenan RM0. |
| **VMware NSX / AWS VPC / GCP VPC** | **OpenStack Neutron + OVN (Open Virtual Network)** | Rangkaian Ditakrifkan Perisian (*Software-Defined Networking - SDN*), penghalaan maya, keselamatan kumpulan (*security groups*), dan pengimbang beban (*Octavia*). | Pengasingan trafik rangkaian tanpa perkakasan rangkaian proprietari mahal; pematuhan piawaian IETF terbuka. |
| **VMware vSAN / AWS EBS / Azure Disks** | **OpenStack Cinder + Ceph RBD** | Storan blok teragih (*distributed block storage*) berprestasi tinggi dengan keupayaan replikasi automatik dan *snapshots*. | Tiada risiko penguncian vendor storan perkakasan (SAN/NAS proprietari); boleh beroperasi atas cakera NVMe komoditi. |
| **AWS S3 / Google Cloud Storage / Azure Blob** | **OpenStack Swift / Ceph RADOS Gateway (RGW)** | Storan objek teragih berskala exabyte yang menyokong API S3 standard industri secara serasi (*drop-in replacement*). | Data kekal dalam sempadan Malaysia; tiada caj pemindahan data (*zero egress fees*) yang melampau. |
| **AWS Outposts / GCP Edge / Azure Stack Edge** | **StarlingX** | Platform awan pinggir (*distributed edge cloud*) berkependaman ultra-rendah (< 1 milisaat) berasaskan kernel Linux masa nyata (*real-time kernel*). | Sangat sesuai untuk automasi pencawang elektrik TNB, telekomunikasi 5G TM (O-RAN), dan loji luar pesisir PETRONAS. |
| **AWS Firecracker / Google gVisor** | **Kata Containers** | *Runtime* kontena selamat yang menjalankan setiap pod/kontena dalam *microVM* terasing menggunakan teknologi perkakasan (VT-x/AMD-V). | Menjamin keselamatan *Zero-Trust*: kontena tidak berkongsi kernel hos, menghalang serangan pencerobohan antara penyewa (*container escape*). |
| **GitHub Actions / AWS CodePipeline / GitLab SaaS** | **Zuul** | Sistem *project-gating* dan CI/CD berbilang repositori yang menguji kebolehfungsian kod merentasi puluhan sistem serentak sebelum cantuman (*merge*). | Mengelakkan kebergantungan saluran pembangunan kepada platform awan asing; membolehkan pengauditan kod secara berpusat. |
| **AWS CloudFormation / HashiCorp Terraform** | **OpenStack Heat + OpenTofu (Linux Foundation)** | Enjin orkestrasi infrastruktur berasaskan kod (*Infrastructure-as-Code - IaC*) deklaratif. | Kod automasi awan tidak tertakluk kepada perubahan lesen komersial; menjamin kebebasan migrasi infrastruktur. |
| **AWS IAM / Azure Active Directory / Google IAM** | **OpenStack Keystone + FreeIPA / Keycloak** | Pengesahan identiti terpusat, pengurusan token, kawalan akses berasaskan peranan (*RBAC*), dan federasi identiti kerajaan. | Kunci keselamatan dan pangkalan data identiti penjawat awam serta warganegara kekal dalam bidang kuasa undang-undang Malaysia. |

---

### 2.2 Penjelasan Terperinci 4 Komponen Teras Strategik

#### 1. OpenStack: Sistem Pengendalian Awan Berdaulat (The Sovereign Cloud OS)
OpenStack bukan sekadar satu program kecil, tetapi himpunan modul perisian pengkomputeran awan paling lengkap di dunia:
* **Nova (Compute):** Mengawal ribuan pelayan fizikal dan mesin maya menggunakan hipervisor Linux KVM (*Kernel-based Virtual Machine*).
* **Ironic (Bare-Metal as a Service):** Keupayaan memprogram dan memasang sistem operasi terus pada pelayan fizikal tanpa lapisan virtualisasi. Ini merupakan komponen **paling kritikal untuk kluster AI & GPU masa kini**, membolehkan pelayan superkomputer AI (seperti pelayan Nvidia H100/B200) dipacu pada kelajuan perkakasan mentah maksimum tanpa kerugian prestasi.
* **Manila (Shared Filesystems):** Menyediakan sistem fail kongsi (NFS/CIFS) berdaulat yang menggantikan AWS EFS atau Azure Files.
* **Skyline & Horizon:** Papan pemuka pengurusan web moden dan mesra pengguna yang memberikan pengalaman seumpama konsol AWS atau Azure kepada pentadbir sistem kerajaan.

#### 2. StarlingX: Enjin Awan Pinggir Telekomunikasi & Utiliti Negara (Distributed Edge Cloud)
Dihoskan bersama oleh OpenInfra Foundation dan Linux Foundation, StarlingX direka khas untuk persekitaran yang menuntut keandalan tahap ketenteraan dan telekomunikasi (*carrier-grade 99.9999% availability*):
* **Ciri-Ciri Utama:** Penyegerakan masa tepat IEEE 1588 PTP, naik taraf perisian tanpa henti (*hitless in-service software upgrade*), pengurusan kerosakan automatik (*self-healing* dalam tempoh milisaat), dan saiz pemasangan ringan (*low-footprint*) yang boleh beroperasi pada pelayan kecil satu nod di kawasan terpencil.
* **Aplikasi Khusus Malaysia:**
  * **TNB:** Automasi sistem pengagihan elektrik SCADA di lebih 80,000 pencawang pengagihan di seluruh negara; pemprosesan data meter pintar (*smart meters*) secara setempat tanpa membebani pusat data pusat.
  * **TM:** Menggerakkan nod *Open Radio Access Network* (O-RAN) bagi rangkaian 5G nasional serta membolehkan pengkomputeran kependaman ultra-rendah untuk pemanduan autonomi dan tele-perubatan.
  * **PETRONAS:** Pemantauan penderia IoT dan kawalan keselamatan masa nyata di platform minyak dan gas luar pesisir (contohnya di perairan Terengganu, Sabah, dan Sarawak) yang mempunyai sambungan internet terhad.

#### 3. Kata Containers: Perisai Pengasingan Keselamatan Multi-Penyewa (Hardware-Isolated Containers)
Dalam persekitaran awan awam standard, kontena (Docker/Kubernetes) berkongsi kernel sistem operasi hos yang sama. Jika terdapat kerentanan keselamatan (*zero-day kernel vulnerability*), sebuah kontena yang diceroboh boleh menembusi sempadan dan membaca memori kontena lain pada pelayan fizikal yang sama.
* **Bagaimana Kata Containers Menyelesaikannya?** Kata Containers membungkus setiap kontena di dalam *microVM* ringan yang mempunyai kernel tersendiri dan diasingkan secara fizikal oleh cip pemproses (Intel VT-x atau AMD-V).
* **Impak untuk Sektor Awam Malaysia:** Membolehkan Kementerian Kesihatan (data pesakit), Kementerian Pertahanan (data ketenteraan), dan Lembaga Hasil Dalam Negeri (data percukaian) berkongsi infrastruktur perkakasan fizikal awan yang sama secara selamat tanpa risiko kebocoran silang (*cross-tenant data leakage*).

#### 4. Ceph: Storan Teragih Kebangsaan Tanpa Titik Kegagalan Tunggal
Ceph merupakan tulang belakang storan perisian sumber terbuka yang diiktiraf di seluruh dunia:
* Menyediakan tiga jenis storan serentak daripada satu kluster pelayan fizikal: Storan Objek (S3-compatible), Storan Blok (untuk cakera VM), dan Storan Fail (POSIX CephFS).
* Menggunakan algoritma matematik CRUSH yang menghapuskan keperluan jadual carian pusat, membolehkan storan berkembang sehingga ke tahap ratusan petabyte tanpa degradasi prestasi.
* Membolehkan pembinaan zon ketersediaan (*Availability Zones - AZ*) merentasi Cyberjaya, Lembah Klang, dan Johor dengan replikasi aktif-aktif.

---

## Bahagian 3: Mengapa Penggantian VMware & Hyperscaler Menjadi Darurat Kebangsaan?

### 3.1 Krisis Pelesenan VMware (The Broadcom Pricing Shock)
Pada hujung tahun 2023, Broadcom memuktamadkan pengambilalihan gergasi perisian virtualisasi VMware dengan nilai \$69 bilion. Sejurus selepas itu, Broadcom melaksanakan penstrukturan radikal:
1. **Penghapusan Lesen Kekal (*Perpetual Licenses*):** Semua pelanggan dipaksa beralih kepada model langganan tahunan wajib.
2. **Pakej Paksaan (*Forced Bundling*):** Menamatkan jualan produk berasingan (seperti vSphere standard) dan memaksa pelanggan membeli pakej penuh *VMware Cloud Foundation (VCF)* yang mengandungi modul yang tidak diperlukan.
3. **Kenaikan Kos Mendadak 300% hingga 1,000%:** Agensi kerajaan, universiti, dan syarikat korporat di Malaysia kini berdepan kenaikan yuran pembaharuan lesen tahunan bernilai jutaan Ringgit secara tiba-tiba.
4. **Iktibar:** Bergantung kepada perisian proprietari meletakkan kedaulatan belanjawan negara di bawah belas kasihan keputusan lembaga pengarah syarikat asing. Beralih kepada OpenStack dan Proxmox VE membebaskan Malaysia daripada peras ugut pelesenan ini secara kekal.

### 3.2 Risiko Kedaulatan Undang-Undang: Akta CLOUD AS 2018 (18 U.S.C. § 2713)
* Di bawah undang-undang Amerika Syarikat, mahkamah persekutuan AS boleh mengeluarkan perintah menggeledah data yang disimpan oleh syarikat berpangkalan di AS (AWS, Google, Microsoft), **tanpa mengira di mana data tersebut disimpan secara geografi**.
* Walaupun AWS melancarkan rantau `ap-southeast-5` di Cyberjaya atau Google melabur di Elmina, data agensi kerajaan dan perniagaan Malaysia yang disimpan di situ **masih tertakluk kepada bidang kuasa undang-undang Washington**.
* Infrastruktur awan berdaulat yang dikendalikan oleh konsortium tempatan menggunakan perisian sumber terbuka OpenInfra memastikan data negara dilindungi sepenuhnya di bawah perlembagaan dan undang-undang Malaysia semata-mata.

---

## Bahagian 4: Cadangan Dasar: Menubuhkan Konsortium Awan Berdaulat Terbuka Malaysia

Kerajaan Malaysia disarankan melalui **Kementerian Digital**, **Kementerian Kewangan (MOF)**, dan **Unit Perancang Ekonomi (EPU)** untuk menubuhkan sebuah badan amanah industri berkanun:

> **Konsortium Awan Berdaulat Terbuka Malaysia (Malaysian Sovereign Open Infrastructure Consortium - MSOIC)**  
> *(Atau: Badan Infrastruktur Awan Terbuka Kebangsaan)*

```
                       ┌────────────────────────────────────────────────────────┐
                       │                   KEMENTERIAN DIGITAL                  │
                       │           (Dasar, Perundangan & Piawaian Terbuka)      │
                       └───────────────────────────┬────────────────────────────┘
                                                   │
                       ┌───────────────────────────▼────────────────────────────┐
                       │          KONSORTIUM AWAN BERDAULAT TERBUKA             │
                       │            MALAYSIA (MSOIC / BADAN AWAN)               │
                       │   - Tadbir Urus Telus   - Reka Bentuk Terbuka (Open)   │
                       │   - Audit Keselamatan   - Bebas Pintu Belakang         │
                       └─────┬─────────────────────┬──────────────────────┬─────┘
                             │                     │                      │
             ┌───────────────▼────────┐  ┌─────────▼────────────┐  ┌──────▼─────────────────┐
             │ TELEKOM MALAYSIA (TM)  │  │ TENAGA NASIONAL (TNB)│  │   PETRONAS (DIGITAL)   │
             │ - Rangkaian Gentian    │  │ - Tenaga Hijau/Suria │  │ - Modal Pelaburan      │
             │ - Pusat Data KVDC/CJDC │  │ - Gentian OPGW Allo  │  │ - Pengkomputeran HPC/AI│
             │ - Pengendali Awan CFA  │  │ - Edge Node (80k Sub)│  │ - Keselamatan Tenaga   │
             └────────────────────────┘  └──────────────────────┘  └────────────────────────┘
                             │                     │                      │
                       ┌─────┴─────────────────────┴──────────────────────┴─────┐
                       │      TIMBUNAN TEKNOLOGI SUMBER TERBUKA OPENINFRA       │
                       │  OpenStack (IaaS) | StarlingX (Edge) | Kata (Security) │
                       │    Ceph (Storan)  | Kubernetes (PaaS)| Zuul (CI/CD)    │
                       └───────────────────────────┬────────────────────────────┘
                                                   │
                       ┌───────────────────────────▼────────────────────────────┐
                       │         ENJIN KEDAULATAN DATA & BAKAT TEMPATAN         │
                       │  - MyGovCloud Berdaulat      - Data Rahsia Industri    │
                       │  - Akademi Bakat Tempatan    - Penyumbang Upstream FOSS│
                       └────────────────────────────────────────────────────────┘
```

---

### 4.1 Sinergi Strategik Tiga Gergasi GLC Utama

Malaysia mempunyai kelebihan unik berbanding banyak negara lain: tiga syarikat berkaitan kerajaan kita menguasai tiga komponen fizikal paling kritikal untuk membina awan berdaulat:

#### 1. Telekom Malaysia (TM / TM One): Tulang Belakang Ketersambungan & Pengendali Awan
* **Aset:** Rangkaian kabel dasar laut antarabangsa, tulang belakang optik gentian DWDM berkelajuan terabit, pusat data bertaraf dunia Tier III / Tier IV di Cyberjaya (CJDC) dan Enstek (KVDC).
* **Peranan dalam Konsortium:** Bertindak sebagai penyedia infrastruktur fizikal dan hos utama bagi nod pusat awan OpenStack. TM One telah pun mempunyai pengalaman berharga sebagai satu-satunya penyedia tempatan dalam Perjanjian Rangka Kerja Awan (CFA) kerajaan.

#### 2. Tenaga Nasional Berhad (TNB / Allo Technology): Kuasa Hijau & Grid Gentian Nasional
* **Aset 1: Kedaulatan Tenaga Boleh Baharu (RE):** Pusat data moden menggunakan kapasiti elektrik yang sangat besar. TNB mempunyai ladang solar berskala besar (LSS), stesen jana kuasa hidroelektrik di Perak dan Terengganu, serta tarif elektrik hijau (GET). TNB dapat menjamin bahawa awan berdaulat Malaysia dijana oleh tenaga hijau mampan, memenuhi piawaian ESG global.
* **Aset 2: Gentian Optik OPGW Allo Technology:** Anak syarikat TNB, Allo Technology, menguruskan rangkaian kabel gentian optik *Optical Ground Wire* (OPGW) yang dipasang di puncak menara transmisi grid elektrik nasional TNB merentasi Semenanjung Malaysia. Ini memberikan laluan gentian optik alternatif yang sangat kukuh, terlindung daripada gangguan penggalian jalan, dan menjangkau hingga ke pekan-pekan kecil serta kawasan luar bandar.
* **Aset 3: Rangkaian Pinggir (Edge Infrastructure):** TNB memiliki lebih 80,000 pencawang elektrik yang boleh dinaik taraf dengan kabinet pelayan lasak mini yang menjalankan **StarlingX**, mencipta rangkaian pengkomputeran pinggir (*edge cloud network*) paling padat di Asia Tenggara.

#### 3. PETRONAS (Petronas Digital): Modal Pelaburan & Pengkomputeran Berprestasi Tinggi
* **Aset 1: Keupayaan Kewangan:** PETRONAS mempunyai kunci kira-kira yang kukuh dan keupayaan memperuntukkan perbelanjaan modal (capex) jangka panjang tanpa tertekan oleh turun naik pasaran jangka pendek.
* **Aset 2: Keperluan Pengkomputeran Skala Mega:** PETRONAS memerlukan kuasa pengkomputeran berprestasi tinggi (*High-Performance Computing - HPC*) untuk simulasi medan minyak, visualisasi seismik 3D dasar laut, dan analitik loji penapisan kimia. Beban kerja ini boleh dihoskan terus di atas pelayan *OpenStack Ironic (bare-metal GPU)* berdaulat, memastikan data geologi dan sumber tenaga strategik negara tidak bocor kepada pihak luar.
* **Aset 3: Keselamatan Operasi Industri (OT/IT):** Menjadi tapak ujian bagi pelaksanaan *Kata Containers* dan *StarlingX* di persekitaran ekstrem loji perindustrian (contohnya di Pengerang Integrated Petroleum Complex - PIPC).

---

### 4.2 Struktur Tadbir Urus yang Telus & Terbuka
Bagi mengelakkan kepincangan agensi IT masa lalu, konsortium ini mesti ditadbir secara telus mengikut prinsip tadbir urus moden:
1. **Reka Bentuk Berasaskan Standard Terbuka (*Open Architecture*):** Semua spesifikasi seni bina perkakasan, panduan pemasangan, dan integrasi API didokumenkan secara awam (berpandukan konsep *Open Compute Project - OCP*).
2. **Pengauditan Bebas Tanpa Rahsia:** Perisian dan konfigurasi rangkaian diaudit secara berkala oleh **CyberSecurity Malaysia (CSM)** dan badan penyelidik bebas universiti bagi memastikan tiada pintu belakang (*backdoors*).
3. **Penyertaan Komuniti & Industri Tempatan:** Konsortium membuka ruang kepada syarikat teknologi PKS tempatan (seperti ahli PIKOM dan komuniti pembangun Linux Malaysia) untuk membina modul perkhidmatan nilai tambah di atas platform terbuka ini, bukan memonopolinya untuk segelintir vendor kroni.

---

### 4.3 Model Penyatuan Dana (Pooled Sovereign Funding)
* **Status Semasa:** Kerajaan persekutuan, kerajaan negeri, universiti awam, dan GLC membelanjakan anggaran **RM2 bilion hingga RM4 bilion setiap tahun** untuk yuran lesen proprietari (VMware, Microsoft 365, Oracle, SAP) dan langganan pengkomputeran awan hyperscaler (AWS, Google, Azure). Wang ini mengalir keluar dalam mata wang Dolar AS (USD).
* **Mekanisme Cadangan:**
  1. Tubuhkan **Tabung Infrastruktur Awan Terbuka Kebangsaan (National Open Infrastructure Fund)**.
  2. Kerajaan dan GLC mengalihkan **15% hingga 20%** daripada perbelanjaan tahunan lesen asing ke dalam tabung ini.
  3. Dana digunakan untuk membeli pelayan fizikal komoditi tempatan, membiayai peluasan pusat data TM/TNB, dan membayar gaji jurutera perisian tempatan dalam Ringgit Malaysia (MYR).
  4. Dalam tempoh 3 tahun, kos operasi IT negara akan menurun sekurang-kurangnya 40% hingga 60% kerana ketiadaan bayaran royalti lesen perisian berulang.

---

### 4.4 Enjin Pembangunan Bakat Tempatan (Local Talents Engine)
Cabaran utama peralihan sumber terbuka bukan isu teknologi, tetapi jurang kemahiran tenaga kerja. Selama beberapa dekad, universiti dan syarikat tempatan melatih graduan menjadi "juruurus perisian proprietari" (*Microsoft certified / AWS certified*) yang hanya tahu menekan butang produk asing.

Konsortium ini akan menggerakkan revolusi pembangunan modal insan:
1. **Penubuhan Akademi Kejuruteraan Awan Terbuka Kebangsaan:**
   * Ditubuhkan dengan kerjasama rasmi OpenInfra Foundation dan Linux Foundation.
   * Menyediakan program pensijilan profesional standard global:
     * *Certified OpenStack Administrator (COA)*
     * *Certified Kubernetes Administrator (CKA / CKS)*
     * *Ceph Storage Architect & Linux Kernel Engineering*
2. **Integrasi Silibus Universiti Awam & TVET:**
   * Bekerjasama dengan universiti penyelidikan tempatan (UTM, UM, UiTM, USM, UTeM) dan politeknik KPT untuk memasukkan seni bina pengkomputeran awan terbuka ke dalam silibus sains komputer dan kejuruteraan perisian tahun akhir.
3. **Program Felo Jurutera Sumber Terbuka Kebangsaan (*National Open Source Engineering Fellowship*):**
   * Menaja 100 jurutera perisian tempatan paling berbakat untuk bekerja sepenuh masa sebagai penyumbang kod teras (*upstream core contributors*) kepada projek OpenStack, Kata Containers, dan StarlingX.
   * Langkah ini menaikkan taraf jurutera Malaysia daripada pengguna hiliran (*downstream users*) kepada pencipta teknologi di persada dunia, sekaligus memberi Malaysia hak suara dalam tadbir urus komuniti teknologi antarabangsa.

---

## Bahagian 5: Pelan Pelaksanaan Strategik 5-Tahun (Roadmap)

```text
TAHUN 1 (Asas & Pembuktian Konsep)
├── Penubuhan rasmi Konsortium MSOIC di bawah Kementerian Digital & GLC (TM, TNB, PETRONAS).
├── Pemasangan Kluster Ujian Perintis OpenStack & Ceph merentasi TM KVDC dan hab Allo TNB.
└── Pelancaran kohort pertama 500 jurutera pensijilan OpenStack/Kubernetes tempatan.

TAHUN 2–3 (Penyahpasangan VMware & Migrasi Beban Kerja Awal)
├── Penggantian sistem virtualisasi VMware lama kepada OpenStack/Proxmox di TM, TNB, dan PETRONAS.
├── Perpindahan data arkib dan storan pendidikan (contoh: LMS CIDOS dan repositori universiti) ke Ceph S3 berdaulat.
├── Pelaksanaan fasa pertama StarlingX di 1,000 pencawang elektrik TNB bagi projek Grid Pintar.
└── Pewartaan dasar perolehan awam "FOSS & Open Standards First" untuk agensi kerajaan persekutuan.

TAHUN 4–5 (Kedaulatan Penuh & Ekosistem Komersial)
├── MyGovCloud beralih sepenuhnya kepada infrastruktur awan berdaulat OpenStack/Kubernetes.
├── Pelancaran superkomputer AI berdaulat nasional dipacu oleh OpenStack Ironic bare-metal GPU clusters.
├── Pembukaan perkhidmatan awan berdaulat MSOIC kepada PKS dan sektor korporat tempatan pada kadar RM yang kompetitif.
└── Malaysia muncul sebagai hab rujukan kecemerlangan OpenInfra di rantau Asia Tenggara (ASEAN).
```

---

## Bahagian 6: Kesimpulan & Syor Tindakan Segera

Pengalaman global (seperti inisiatif kedaulatan digital di Jerman, Perancis, dan Kesatuan Eropah) membuktikan bahawa pergantungan mutlak kepada segelintir konglomerat teknologi asing melemahkan daya tahan ekonomi, mendedahkan data warganegara kepada risikan luar, dan menindas pembangunan bakat kejuruteraan tempatan.

Dengan memanfaatkan projek matang **OpenInfra Foundation** dan menyatukan aset fizikal tiga gergasi GLC kebangsaan—**Telekom Malaysia (ketersambungan)**, **Tenaga Nasional Berhad (kuasa hijau & gentian OPGW)**, dan **PETRONAS (modal & pengkomputeran industri)**—Malaysia memiliki semua ramuan yang diperlukan untuk membina enjin infrastruktur awan berdaulat yang paling disegani di Asia Tenggara.

### Tiga Tindakan Segera Untuk Kerajaan:
1. **Kementerian Digital:** Mengadakan sesi meja bulat kebangsaan bersama kepimpinan OpenInfra Foundation, TM, TNB, PETRONAS, dan MAMPU untuk merangka Memorandum Persefahaman (MoU) penubuhan Konsortium.
2. **Kementerian Kewangan (MOF):** Mengarahkan moratorium serta audit perolehan terhadap kenaikan mendadak lesen pembaharuan VMware/Broadcom merentasi semua agensi awam dan GLC, serta membuka laluan perintis migrasi OpenStack/Proxmox.
3. **Kementerian Pendidikan Tinggi (KPT) & Kementerian Digital:** Memulakan geran pembiayaan bakat awan terbuka kebangsaan untuk melatih kohort pertama 1,000 jurutera awan sumber terbuka bertauliah menjelang 2027.

---
**Kempen Akauntabiliti Teknologi Sumber Terbuka Malaysia**  
*Membina Alternatif. Menjamin Kedaulatan. Memperkasa Bakat Tempatan.*
