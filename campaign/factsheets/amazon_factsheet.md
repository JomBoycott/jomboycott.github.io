# Lembaran Fakta Syarikat: Amazon / AWS
## Company Fact Sheet: Amazon / AWS

**Entiti:** Amazon.com, Inc. / Amazon Web Services (AWS) (Seattle, Washington, USA)  
**Skop Penyelidikan:** AWS Cloud Infrastructure, Amazon SageMaker, AWS Tel Aviv Region (`il-central-1`), Project Nimbus  
**Penilaian Status:** Pembekal Infrastruktur Awan & Kuasa Komputasi Utama Rejim (Tier 1)

---

### 1. Hubungan Yang Didokumenkan (The Documented Relationship)
* **Pemenang Bersama Project Nimbus:** AWS berkongsi kontrak awan bernilai **\$1.2 bilion** bersama Google untuk membekalkan infrastruktur awan kerajaan Israel.
* **Pelaburan Rantau Tel Aviv (\$7.2 Bilion):** Pada 1 Ogos 2023, AWS melancarkan Wilayah Awan Tel Aviv (`il-central-1`) dengan 3 Zon Ketersediaan (*Availability Zones*), mengumumkan komitmen pelaburan jangka panjang sebanyak \$7.2 bilion sehingga tahun 2037.
* **Infrastruktur Keselamatan & Pertahanan:** AWS membekalkan perkhidmatan storan data (S3), pangkalan data berskala mega, kuasa pemprosesan grafik (GPU clusters), dan model pembelajaran mesin (Amazon SageMaker) kepada agensi keselamatan, polis, dan kementerian pertahanan Israel.

---

### 2. Terma Kontrak & Kesinambungan Perkhidmatan
* Di bawah syarat tender Nimbus, AWS diwajibkan menyediakan perkhidmatan secara berterusan melalui anak syarikat tempatan yang berdaftar di Israel.
* Struktur ini direka khusus oleh peguam kerajaan Israel untuk memastikan sebarang sekatan ekonomi, perintah mahkamah antarabangsa, atau perubahan polisi korporat di Seattle tidak boleh memutuskan bekalan kuasa pengkomputeran kepada tentera.

---

### 3. Kontroversi Penghantaran di Penempatan Haram Tebing Barat
* Pada tahun 2020, siasatan mendedahkan Amazon menawarkan penghantaran percuma ke penempatan haram Yahudi di Tebing Barat tetapi mengenakan bayaran tinggi kepada penduduk Palestin berdekatan melainkan mereka menyenaraikan negara mereka sebagai "Israel".
* Selepas desakan antarabangsa dan bantahan pertubuhan hak asasi, Amazon memperluas dasar penghantaran percuma tersebut kepada alamat pos Palestin.

---

### 4. Fakta Terbukti vs. Dakwaan Tidak Sah

| Aspek | Fakta Sah Disahkan (*Verified*) | Dakwaan Belum Terbukti / Salah (*Unverified/False*) |
| :--- | :--- | :--- |
| **Kontrak Awan** | Disahkan memenangi Nimbus ($1.2B) dan melabur $7.2B di zon Tel Aviv. | Dakwaan bahawa Amazon mengeluarkan dan mengendalikan dron tempur fizikal (senjata dron dibina oleh kontraktor pertahanan seperti Elbit Systems). |
| **Pelanggan Pertahanan** | Disahkan bahawa kementerian pertahanan dan polis Israel menggunakan infrastruktur AWS. | — |
| **Bantahan Pekerja** | Disahkan ratusan jurutera AWS menandatangani surat terbuka menolak Nimbus (2021). | — |

---

### 5. Signifikan Kepada Malaysia
* Pada Ogos 2024, AWS membuka **Wilayah Awan Malaysia (`ap-southeast-5`)** dengan komitmen pelaburan \$6.2 bilion dan memeterai Perjanjian Rangka Kerja Awan (CFA) bersama kerajaan Malaysia.
* Situasi ini mendedahkan risiko dwi-kebergantungan: data sektor awam Malaysia dihoskan oleh syarikat yang sama yang membekalkan prasarana teras kepada jentera ketenteraan Israel.

---

### 6. Alternatif Sumber Terbuka Yang Boleh Digunakan Rakyat Malaysia
* **Storan Objek Awan (Ganti AWS S3):** Gunakan **MinIO** (storan objek sumber terbuka serasi API S3 berprestasi tinggi yang boleh dihoskan di pelayan tempatan).
* **Pengkomputeran Awan (Ganti AWS EC2):** Gunakan **OpenStack** atau **Proxmox VE** di pusat data domestik (TM One, AIMS).
* **Saluran CI/CD (Ganti AWS CodePipeline):** Gunakan **Woodpecker CI** atau **Forgejo**.
