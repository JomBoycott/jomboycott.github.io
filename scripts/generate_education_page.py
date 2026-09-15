#!/usr/bin/env python3
"""
Generate website/education.html for Malaysian Open-Source Tech Accountability Campaign
"""
import os

HTML_CONTENT = """<!DOCTYPE html>
<html lang="ms" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The Free-to-Lock-In Pipeline | Amanah Digital Malaysia</title>
  <meta name="description" content="Siasatan Khas: Bagaimana Google, Microsoft, dan AWS Menguasai Ekosistem Pendidikan Malaysia dari K-12 hingga Universiti.">
  <link rel="stylesheet" href="styles.css">
  <style>
    .pipeline-step {
      display: flex;
      gap: 1.5rem;
      margin-bottom: 2rem;
      align-items: flex-start;
    }
    .pipeline-number {
      width: 3.5rem;
      height: 3.5rem;
      border-radius: 50%;
      background: linear-gradient(135deg, var(--accent-primary), var(--accent-purple));
      color: white;
      font-weight: 800;
      font-size: 1.5rem;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      box-shadow: var(--shadow-md);
    }
    .pipeline-content {
      background-color: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 1.75rem;
      flex-grow: 1;
      box-shadow: var(--shadow-sm);
    }
    .stat-badge-danger {
      background: rgba(244, 63, 94, 0.15);
      color: var(--accent-rose);
      border: 1px solid rgba(244, 63, 94, 0.3);
      padding: 0.25rem 0.6rem;
      border-radius: var(--radius-sm);
      font-size: 0.8125rem;
      font-weight: 700;
    }
    .quote-box {
      border-left: 4px solid var(--accent-purple);
      background: rgba(168, 85, 247, 0.06);
      padding: 1rem 1.25rem;
      border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
      margin: 1rem 0;
      font-style: italic;
    }
    .table-container {
      overflow-x: auto;
      margin-top: 1.5rem;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
    }
    .data-table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.9375rem;
    }
    .data-table th, .data-table td {
      padding: 1rem 1.25rem;
      border-bottom: 1px solid var(--border-color);
    }
    .data-table th {
      background-color: var(--bg-surface-elevated);
      font-weight: 700;
      color: var(--text-primary);
    }
    .data-table tr:hover {
      background-color: rgba(56, 189, 248, 0.04);
    }
  </style>
</head>
<body>

  <!-- Header Navigation -->
  <header class="site-header">
    <div class="container nav-wrapper">
      <a href="index.html" class="brand-link">
        <span class="brand-badge">MOTAC</span>
        <span>Amanah Digital Malaysia</span>
      </a>
      <nav>
        <ul class="nav-links">
          <li><a href="index.html"><span class="lang-bm">Utama</span><span class="lang-en" style="display: none;">Home</span></a></li>
          <li><a href="evidence.html"><span class="lang-bm">Pangkalan Bukti</span><span class="lang-en" style="display: none;">Evidence Base</span></a></li>
          <li><a href="companies.html"><span class="lang-bm">Syarikat</span><span class="lang-en" style="display: none;">Companies</span></a></li>
          <li><a href="alternatives.html"><span class="lang-bm">Alternatif FOSS</span><span class="lang-en" style="display: none;">FOSS Alternatives</span></a></li>
          <li><a href="education.html" class="active"><span class="lang-bm">Siasatan Pendidikan</span><span class="lang-en" style="display: none;">Education Pipeline</span></a></li>
          <li><a href="migrate.html"><span class="lang-bm">Laluan Migrasi</span><span class="lang-en" style="display: none;">Migration Guide</span></a></li>
          <li><a href="islam.html"><span class="lang-bm">Asas Islam</span><span class="lang-en" style="display: none;">Islamic Ethics</span></a></li>
          <li><a href="malaysia.html"><span class="lang-bm">Kedaulatan Malaysia</span><span class="lang-en" style="display: none;">Malaysian Sovereignty</span></a></li>
          <li><a href="media.html"><span class="lang-bm">Galeri Risalah</span><span class="lang-en" style="display: none;">Leaflets</span></a></li>
          <li><a href="about.html"><span class="lang-bm">Tentang Kami</span><span class="lang-en" style="display: none;">About</span></a></li>
        </ul>
      </nav>
      <div class="nav-actions">
        <button id="lang-toggle" class="btn-icon" aria-label="Tukar Bahasa">🌐 English</button>
        <button id="theme-toggle" class="btn-icon" aria-label="Tukar Tema">🌙 Gelap</button>
      </div>
    </div>
  </header>

  <main class="container section">
    <!-- Page Header -->
    <div class="section-header">
      <div class="hero-pill" style="border-color: var(--accent-rose); color: var(--accent-rose);">
        <span>🎓</span>
        <span class="lang-bm">Dosier Siasatan Khas MOTAC</span>
        <span class="lang-en" style="display: none;">Special Investigative Dossier</span>
      </div>
      <h1 class="section-title">
        <span class="lang-bm">The Free-to-Lock-In Pipeline: Bagaimana Big Tech Menguasai Ekosistem Pendidikan Malaysia</span>
        <span class="lang-en" style="display: none;">The Free-to-Lock-In Pipeline: How Big Tech Seeds Malaysia Educational Ecosystems</span>
      </h1>
      <p class="section-subtitle">
        <span class="lang-bm">
          Siasatan forensik mengenai penawanan berstruktur bilik darjah, TVET, dan universiti awam Malaysia oleh Google, Microsoft, dan AWS—daripada 5.3 juta akaun DELIMa sehinggalah krisis kuota storan, pemansuhan autonomi silibus, dan imuniti Seksyen 3(1) APDP.
        </span>
        <span class="lang-en" style="display: none;">
          A forensic investigation into the structural capture of Malaysian classrooms, TVET polytechnics, and public universities by Google, Microsoft, and AWS—from 5.3 million DELIMa accounts to predatory storage caps, curricular enclosure, and Section 3(1) PDPA immunity.
        </span>
      </p>
    </div>

    <!-- 4 Key Stat Metric Cards -->
    <div class="grid-4" style="margin-bottom: 3rem;">
      <div class="card" style="border-top: 4px solid var(--accent-primary);">
        <div style="font-size: 2rem; font-weight: 800; color: var(--accent-primary);">5.3 Juta</div>
        <div style="font-weight: 700; margin-top: 0.25rem;">
          <span class="lang-bm">Akaun Murid &amp; Guru DELIMa</span>
          <span class="lang-en" style="display: none;">DELIMa Student &amp; Teacher Accounts</span>
        </div>
        <p style="font-size: 0.8125rem; color: var(--text-secondary); margin-top: 0.5rem;">
          <span class="lang-bm">99.5% guru dan 4.1 juta murid dihubungkan terus ke Google Workspace &amp; MS 365 melalui domain <code>@moe-dl.edu.my</code>.</span>
          <span class="lang-en" style="display: none;">99.5% of teachers and 4.1M pupils tied directly to Google Workspace &amp; MS 365 via <code>@moe-dl.edu.my</code>.</span>
        </p>
      </div>

      <div class="card" style="border-top: 4px solid var(--accent-amber);">
        <div style="font-size: 2rem; font-weight: 800; color: var(--accent-amber);">140,000</div>
        <div style="font-weight: 700; margin-top: 0.25rem;">
          <span class="lang-bm">Pelajar TVET Terkunci AWS</span>
          <span class="lang-en" style="display: none;">TVET Students Bound to AWS</span>
        </div>
        <p style="font-size: 0.8125rem; color: var(--text-secondary); margin-top: 0.5rem;">
          <span class="lang-bm">36 politeknik &amp; 105 kolej komuniti bawah JPPKK distandardkan dengan silibus AWS; sistem CIDOS dihoskan di awan Amazon.</span>
          <span class="lang-en" style="display: none;">36 polytechnics &amp; 105 community colleges standardized on AWS; CIDOS LMS hosted directly on Amazon cloud.</span>
        </p>
      </div>

      <div class="card" style="border-top: 4px solid var(--accent-rose);">
        <div style="font-size: 2rem; font-weight: 800; color: var(--accent-rose);">100 TB</div>
        <div style="font-weight: 700; margin-top: 0.25rem;">
          <span class="lang-bm">Siling Storan Kumpulan (Rug-Pull)</span>
          <span class="lang-en" style="display: none;">Pooled Storage Cap (Rug-Pull)</span>
        </div>
        <p style="font-size: 0.8125rem; color: var(--text-secondary); margin-top: 0.5rem;">
          <span class="lang-bm">Google (2022) &amp; Microsoft (2024) menarik balik storan percuma tanpa had; UTM terpaksa hadkan pelajar kepada 6 GB sahaja.</span>
          <span class="lang-en" style="display: none;">Google (2022) &amp; Microsoft (2024) ended unmetered storage; UTM forced to cap students at a severe 6 GB.</span>
        </p>
      </div>

      <div class="card" style="border-top: 4px solid var(--accent-purple);">
        <div style="font-size: 2rem; font-weight: 800; color: var(--accent-purple);">Seksyen 3(1)</div>
        <div style="font-weight: 700; margin-top: 0.25rem;">
          <span class="lang-bm">Vakum Privasi APDP 2010</span>
          <span class="lang-en" style="display: none;">PDPA 2010 Legal Vacuum</span>
        </div>
        <p style="font-size: 0.8125rem; color: var(--text-secondary); margin-top: 0.5rem;">
          <span class="lang-bm">Kerajaan dikecualikan dari Akta 709; data 5 juta anak Malaysia tiada perlindungan statutori tetapi tertakluk kepada Akta CLOUD AS.</span>
          <span class="lang-en" style="display: none;">Government is exempt from PDPA; 5M minors' data has zero statutory protection yet faces US CLOUD Act search.</span>
        </p>
      </div>
    </div>

    <!-- The 4 Pipeline Phases -->
    <div class="card" style="margin-bottom: 3rem; background: var(--bg-surface-elevated); border: 1px solid var(--border-color);">
      <h2 style="font-size: 1.5rem; margin-bottom: 1.5rem; display: flex; align-items: center; gap: 0.75rem;">
        <span>🔄</span>
        <span class="lang-bm">4 Fasa Saluran Penawanan: Bagaimana 'Percuma' Menjadi Monopoli</span>
        <span class="lang-en" style="display: none;">The 4 Pipeline Phases: How 'Free' Converts into Perpetual Monopoly</span>
      </h2>

      <!-- Phase 1 -->
      <div class="pipeline-step">
        <div class="pipeline-number">1</div>
        <div class="pipeline-content">
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 0.5rem;">
            <h3 style="color: var(--accent-primary); font-size: 1.2rem;">
              <span class="lang-bm">Fasa 1: Umpan 'Percuma' &amp; Penyusupan Tanpa Kos (The Zero-Cost Hook)</span>
              <span class="lang-en" style="display: none;">Phase 1: Zero-Cost Ingress (The Philanthropic Hook)</span>
            </h3>
            <span class="badge badge-verified">Umpan Kemasukan</span>
          </div>
          <p style="color: var(--text-secondary); font-size: 0.9375rem; line-height: 1.6;">
            <span class="lang-bm">
              Gergasi teknologi menawarkan lesen pendidikan secara percuma (Google Workspace Fundamentals, Office 365 A1, kredit makmal AWS Academy). Di bawah kekangan belanjawan awam, Kementerian Pendidikan (KPM) dan Jabatan Politeknik (JPPKK) memilih penyelesaian ini kerana kos pelesenan sifar serta-merta, menyingkirkan sebarang peluang pembangunan perisian berdaulat tempatan atau platform sumber terbuka (FOSS).
            </span>
            <span class="lang-en" style="display: none;">
              Hyperscalers offer free educational tiers (Google Workspace Fundamentals, Office 365 A1, AWS Academy cloud credits). Facing budget constraints, ministries and institutions adopt these turnkeys for immediate zero-cost licensing, effectively crowding out domestic software developers and open-source infrastructure.
            </span>
          </p>
        </div>
      </div>

      <!-- Phase 2 -->
      <div class="pipeline-step">
        <div class="pipeline-number">2</div>
        <div class="pipeline-content">
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 0.5rem;">
            <h3 style="color: var(--accent-emerald); font-size: 1.2rem;">
              <span class="lang-bm">Fasa 2: Pembiasaan Kognitif &amp; Enkapsulasi Silibus (Cognitive Habituation)</span>
              <span class="lang-en" style="display: none;">Phase 2: Cognitive Habituation &amp; Curricular Enclosure</span>
            </h3>
            <span class="badge badge-supported">Pembentukan Tabiat</span>
          </div>
          <p style="color: var(--text-secondary); font-size: 0.9375rem; line-height: 1.6;">
            <span class="lang-bm">
              Anak-anak Malaysia seawal Darjah 1 (umur 7 tahun) dibekalkan identiti Google/Microsoft. Format proprietari (<code>.docx</code>, <code>.pptx</code>, Google Docs) menjadi sinonim dengan konsep literasi komputer. 420,000 guru dilatih dan diinsentifkan melalui program pensijilan korporat (<em>Google Certified Educator</em>, <em>Microsoft MIEE</em>) untuk menjadi jurujual sukarela. Di politeknik, subjek sains komputer ditukar daripada pengkomputeran sistem terbuka kepada pembelajaran konsol proprietari AWS (S3, EC2, IAM).
            </span>
            <span class="lang-en" style="display: none;">
              Malaysian children from Standard 1 (age 7) are issued Google/Microsoft IDs. Proprietary formats become synonymous with computing literacy. 420,000 public school teachers are incentivized via corporate badges (GCE, MIEE) to act as unsalaried evangelists. In polytechnics, foundational computer systems engineering is replaced with proprietary AWS console operations (S3, EC2, IAM).
            </span>
          </p>
        </div>
      </div>

      <!-- Phase 3 -->
      <div class="pipeline-step">
        <div class="pipeline-number">3</div>
        <div class="pipeline-content">
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 0.5rem;">
            <h3 style="color: var(--accent-amber); font-size: 1.2rem;">
              <span class="lang-bm">Fasa 3: Jerangkap 'Bait-and-Switch' &amp; Pemerasan Sewa (Rent Extraction)</span>
              <span class="lang-en" style="display: none;">Phase 3: The Bait-and-Switch (Monopoly Rent Extraction)</span>
            </h3>
            <span class="stat-badge-danger">Penarikan Semula Kuota</span>
          </div>
          <p style="color: var(--text-secondary); font-size: 0.9375rem; line-height: 1.6;">
            <span class="lang-bm">
              Setelah pelayan mel tempatan, storan sandaran pita, dan arkib di universiti awam dimansuhkan, Big Tech membatalkan janji "storan percuma tanpa had". Google memperkenalkan had 100 TB kumpulan pada Julai 2022, diikuti Microsoft pada Ogos 2024. Universiti penyelidikan seperti UTM, UM, dan UKM terperangkap dalam krisis kapasiti, memaksa catuan kejam (6 GB untuk pelajar) atau pembayaran berjuta-juta Ringgit untuk melanggan lesen berbayar Google Workspace Plus dan Microsoft A3/A5.
            </span>
            <span class="lang-en" style="display: none;">
              Once on-premise email servers and local storage arrays were decommissioned, vendors revoked 'unlimited' promises. Google imposed a 100 TB pooled limit in July 2022; Microsoft followed in August 2024. Public universities (UTM, UM, UKM) suffered storage crises, forcing severe rationing (6 GB for UTM students) or spending millions in foreign exchange for paid Plus/A3/A5 tiers.
            </span>
          </p>
        </div>
      </div>

      <!-- Phase 4 -->
      <div class="pipeline-step">
        <div class="pipeline-number">4</div>
        <div class="pipeline-content">
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 0.5rem;">
            <h3 style="color: var(--accent-rose); font-size: 1.2rem;">
              <span class="lang-bm">Fasa 4: Penuaian Korporat Sektor Swasta &amp; GLC (Enterprise Capture)</span>
              <span class="lang-en" style="display: none;">Phase 4: Downstream Corporate Capture &amp; Capital Flight</span>
            </h3>
            <span class="stat-badge-danger">Penirisan Modal Nasional</span>
          </div>
          <p style="color: var(--text-secondary); font-size: 0.9375rem; line-height: 1.6;">
            <span class="lang-bm">
              Apabila graduan menamatkan pengajian, akaun universiti dipadamkan, memaksa mereka melanggan perkhidmatan komersial peribadi (Google One / Microsoft 365). Apabila melangkah ke alam pekerjaan di GLC (Petronas, TNB, Maybank) dan PKS, memori otot kognitif selama 15 tahun menyebabkan mereka menuntut perisian Big Tech. Majikan Malaysia terpaksa membayar lesen korporat gergasi (E3/E5), mencetuskan penirisan ekonomi tahunan ke Silicon Valley.
            </span>
            <span class="lang-en" style="display: none;">
              Upon graduation, student accounts are purged, funnelling alumni into paid Google One and Microsoft 365 consumer plans. Entering Malaysian GLCs (Petronas, TNB, Maybank) and SMEs, their 15-year cognitive conditioning compels them to demand Big Tech stacks. Malaysian enterprise employers are forced into recurring enterprise subscriptions (E3/E5), driving massive capital flight to Silicon Valley.
            </span>
          </p>
        </div>
      </div>
    </div>

    <!-- Historical Deep Dive: 1BestariNet to DELIMa -->
    <div class="card" style="margin-bottom: 2.5rem;">
      <h2 style="font-size: 1.35rem; color: var(--accent-primary); margin-bottom: 1rem;">
        <span class="lang-bm">1. Konteks Sejarah: Daripada Kegagalan 1BestariNet ke Oligopoli Global</span>
        <span class="lang-en" style="display: none;">1. Historical Context: From the 1BestariNet Failure to Global Hyperscalers</span>
      </h2>
      <p style="font-size: 0.9375rem; color: var(--text-secondary); line-height: 1.7; margin-bottom: 1rem;">
        <span class="lang-bm">
          Penawanan bilik darjah Malaysia tidak bermula dengan niat jahat, tetapi berpunca daripada kegagalan projek mega domestik. Pada tahun 2011, Kementerian Pendidikan memulakan projek <strong>1BestariNet</strong> bersama YTL Communications dengan peruntukan melebihi <strong>RM4.07 bilion</strong> untuk menghubungkan 10,000 sekolah dengan internet 4G dan perisian <strong>Frog VLE</strong>.
        </span>
        <span class="lang-en" style="display: none;">
          The capture of Malaysian classrooms originated from the collapse of a domestic megaproject. In 2011, MOE initiated the <strong>1BestariNet</strong> project with YTL Communications, budgeted at <strong>over RM4.07 billion</strong> across three phases to connect 10,000 schools with 4G and the <strong>Frog VLE</strong> platform.
        </span>
      </p>

      <div class="quote-box">
        <span class="lang-bm">
          "Laporan Ketua Audit Negara (2013 &amp; 2018) dan siasatan Jawatankuasa Kira-Kira Wang Negara (PAC) mendapati kadar capaian harian Frog VLE di sekolah luar bandar Sabah dan Sarawak berada di bawah 1%, dengan majoriti guru terbeban dengan sambungan yang perlahan dan perkakasan proprietari yang tidak berfungsi."
        </span>
        <span class="lang-en" style="display: none;">
          "Auditor-General Reports (2013 &amp; 2018) and PAC investigations revealed daily active usage of Frog VLE in rural Sabah and Sarawak schools hovered below 1%, with teachers burdened by bandwidth bottlenecks and defective proprietary hardware."
        </span>
      </div>

      <p style="font-size: 0.9375rem; color: var(--text-secondary); line-height: 1.7;">
        <span class="lang-bm">
          Pada Jun 2019, Menteri Pendidikan ketika itu Dr. Maszlee Malik menamatkan kontrak Frog VLE dan mengumumkan pertukaran kepada <strong>Google Classroom</strong> untuk menjimatkan kos awam. Walau bagaimanapun, langkah ini menukar monopoli swasta tempatan kepada monopoli transnasional asing yang kebal daripada liabiliti undang-undang tempatan.
        </span>
        <span class="lang-en" style="display: none;">
          In June 2019, then-Education Minister Dr. Maszlee Malik ended the Frog VLE contract, switching to <strong>Google Classroom</strong> to realize immediate cost savings. However, this trade-off replaced a domestic contractor with transnational monopolies immune to domestic legal sanctions.
        </span>
      </p>
    </div>

    <!-- TVET & AWS Capture -->
    <div class="card" style="margin-bottom: 2.5rem;">
      <h2 style="font-size: 1.35rem; color: var(--accent-amber); margin-bottom: 1rem;">
        <span class="lang-bm">2. Penawanan TVET: 140,000 Pelajar Politeknik Ditundukkan Kepada AWS</span>
        <span class="lang-en" style="display: none;">2. TVET Enclosure: 140,000 Polytechnic Students Bound to AWS</span>
      </h2>
      <p style="font-size: 0.9375rem; color: var(--text-secondary); line-height: 1.7; margin-bottom: 1rem;">
        <span class="lang-bm">
          Pada September 2024, Jabatan Pendidikan Politeknik dan Kolej Komuniti (<strong>JPPKK</strong>) di bawah Kementerian Pendidikan Tinggi (KPT) menandatangani perjanjian rasmi menjadikan JPPKK sebagai <em>AWS Authorized Training Partner</em>. Inisiatif ini merangkumi:
        </span>
        <span class="lang-en" style="display: none;">
          In September 2024, the Department of Polytechnic and Community College Education (<strong>JPPKK</strong>) under the Ministry of Higher Education signed an agreement becoming an <em>AWS Authorized Training Partner</em>, encompassing:
        </span>
      </p>

      <ul style="margin-left: 1.5rem; margin-bottom: 1rem; color: var(--text-secondary); line-height: 1.7;">
        <li><span class="lang-bm"><strong>140,000 Pelajar:</strong> Mengikuti silibus kurikulum komputasi awan dan AI yang direka khusus mengikut ekosistem proprietari AWS.</span><span class="lang-en" style="display: none;"><strong>140,000 Students:</strong> Enrolled in cloud and AI curricula tailored strictly around proprietary AWS architectures.</span></li>
        <li><span class="lang-bm"><strong>Penyusupan Infrastruktur CIDOS:</strong> Sistem Pengurusan Dokumen dan Pembelajaran Berpusat Politeknik (CIDOS) dipindahkan untuk dihoskan terus di pelayan awan AWS. Kerajaan Malaysia membayar Amazon untuk melatih anak watan menggunakan servis berbayar Amazon.</span><span class="lang-en" style="display: none;"><strong>CIDOS Ingestion:</strong> The Centralized Information Document Online System (CIDOS) LMS was migrated directly onto AWS cloud hosting. The Malaysian government pays Amazon to run the platform that trains students to use Amazon.</span></li>
        <li><span class="lang-bm"><strong>49 Universiti Tempatan:</strong> Universiti awam dan swasta (UTM, APU, TAR UMT, UiTM, UniMAP) memasukkan modul AWS Academy ke dalam kurikulum ijazah sarjana muda.</span><span class="lang-en" style="display: none;"><strong>49 Universities:</strong> Public and private universities (UTM, APU, TAR UMT, UiTM) embedded AWS Academy modules directly into bachelor degree curricula.</span></li>
      </ul>
    </div>

    <!-- The Storage Rug-Pull Comparison Table -->
    <div class="card" style="margin-bottom: 2.5rem;">
      <h2 style="font-size: 1.35rem; color: var(--accent-rose); margin-bottom: 1rem;">
        <span class="lang-bm">3. Anatomi 'Bait-and-Switch': Dari Percuma Kepada Jutaan Ringgit</span>
        <span class="lang-en" style="display: none;">3. The Bait-and-Switch Anatomy: From Free Onboarding to Rent Extraction</span>
      </h2>
      <p style="font-size: 0.9375rem; color: var(--text-secondary); line-height: 1.6;">
        <span class="lang-bm">
          Jadual perbandingan di bawah menunjukkan bagaimana janji kemurahan hati Google dan Microsoft bertukar menjadi jerangkap kewangan sebaik sahaja universiti Malaysia menutup prasarana storan tempatan mereka:
        </span>
        <span class="lang-en" style="display: none;">
          The comparison matrix below reveals how Google and Microsoft philanthropic overtures transformed into financial traps once Malaysian universities dismantled internal storage servers:
        </span>
      </p>

      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>Dimensi</th>
              <th>Google Workspace for Education</th>
              <th>Microsoft 365 Education</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Umpan Awal (2012–2021)</strong></td>
              <td>Storan awan Google Drive <strong>PERCUMA TANPA HAD</strong> untuk semua pelajar &amp; staf.</td>
              <td>Pakej Office 365 A1 Plus <strong>PERCUMA</strong> merangkumi aplikasi desktop Word, Excel, PowerPoint.</td>
            </tr>
            <tr>
              <td><strong>Tarikh Penarikan Balik</strong></td>
              <td><strong>Julai 2022</strong> (Tamat era storan tanpa had).</td>
              <td><strong>1 Ogos 2024</strong> (A1 Plus dimansuhkan; had storan dikuatkuasakan).</td>
            </tr>
            <tr>
              <td><strong>Had Baharu Yang Dikenakan</strong></td>
              <td>Had asas <strong>100 TB storan kumpulan</strong> (pooled storage) untuk keseluruhan universiti.</td>
              <td>Had asas <strong>100 TB kumpulan</strong>; akaun percuma A1 dihadkan maksimum 100 GB.</td>
            </tr>
            <tr>
              <td><strong>Kesan di Universiti Tempatan</strong></td>
              <td>UTM terpaksa hadkan staf ke <strong>30 GB</strong> dan pelajar ke <strong>6 GB</strong>; penyelidikan data besar terganggu.</td>
              <td>Universiti awam terpaksa menaik taraf ke lesen berbayar <strong>A3/A5</strong> bernilai jutaan Ringgit.</td>
            </tr>
            <tr>
              <td><strong>Alternatif Yang Ditawarkan IT</strong></td>
              <td>IT menyuruh pengguna pindahkan fail ke <strong>Microsoft OneDrive</strong> (terperangkap dalam jerangkap kedua).</td>
              <td>IT menyuruh pengguna membeli langganan Google One atau cakera keras peribadi sendiri.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Legal & Sovereignty Vacuum: PDPA & CLOUD Act -->
    <div class="card" style="margin-bottom: 2.5rem; border-left: 5px solid var(--accent-rose);">
      <h2 style="font-size: 1.35rem; color: var(--accent-rose); margin-bottom: 1rem;">
        <span class="lang-bm">4. Vakum Undang-Undang: Seksyen 3(1) APDP &amp; Ancaman Akta CLOUD AS</span>
        <span class="lang-en" style="display: none;">4. The Legal Void: PDPA Section 3(1) Exemption vs US CLOUD Act Jurisdiction</span>
      </h2>

      <div class="grid-2">
        <div>
          <h3 style="font-size: 1.05rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.5rem;">
            <span class="lang-bm">Pengecualian Seksyen 3(1) Akta 709</span>
            <span class="lang-en" style="display: none;">Section 3(1) Act 709 Exemption</span>
          </h3>
          <p style="font-size: 0.875rem; color: var(--text-secondary); line-height: 1.6;">
            <span class="lang-bm">
              Di bawah <strong>Seksyen 3(1) Akta Perlindungan Data Peribadi 2010 (APDP)</strong>, akta ini <em>"tidak terpakai kepada Kerajaan Persekutuan dan Kerajaan Negeri"</em>. Ini bermakna KPM, JPN, PPD, dan sekolah kebangsaan tidak tertakluk kepada prinsip keselamatan data, notis persetujuan, atau penalti kebocoran data. Data 5.3 juta anak Malaysia diuruskan tanpa sebarang payung perlindungan undang-undang statutori tempatan.
            </span>
            <span class="lang-en" style="display: none;">
              Under <strong>Section 3(1) of the Personal Data Protection Act 2010 (PDPA)</strong>, the Act <em>"shall not apply to the Federal Government and State Governments"</em>. Consequently, MOE, state education departments, and public schools are exempt from mandatory breach notices and statutory data principles. 5.3 million children's profiles exist in a domestic legal void.
            </span>
          </p>
        </div>

        <div>
          <h3 style="font-size: 1.05rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.5rem;">
            <span class="lang-bm">Cengkaman Akta CLOUD AS (2018)</span>
            <span class="lang-en" style="display: none;">The US CLOUD Act Threat</span>
          </h3>
          <p style="font-size: 0.875rem; color: var(--text-secondary); line-height: 1.6;">
            <span class="lang-bm">
              Walaupun Google dan Microsoft membina pusat data fizikal di Elmina atau Greater KL, <strong>Akta CLOUD AS (18 U.S.C. § 2713)</strong> memberi kuasa kepada agensi undang-undang dan perisikan Amerika Syarikat untuk menuntut data pengguna daripada syarikat induk AS tanpa mengira lokasi fizikal pelayan. Data demografi, tugasan, dan telemetri tingkah laku pelajar Malaysia kekal di bawah bayang-bayang bidang kuasa Washington.
            </span>
            <span class="lang-en" style="display: none;">
              Even with hyperscalers constructing data centers in Elmina or Greater KL, the <strong>US CLOUD Act (18 U.S.C. § 2713)</strong> compels US corporations to hand over customer data regardless of physical server location. The behavioural telemetry, demographics, and assignments of Malaysian pupils remain legally subservient to US extraterritorial warrants.
            </span>
          </p>
        </div>
      </div>
    </div>

    <!-- The Next Frontier: Generative AI Ingestion -->
    <div class="card" style="margin-bottom: 2.5rem;">
      <h2 style="font-size: 1.35rem; color: var(--accent-purple); margin-bottom: 1rem;">
        <span class="lang-bm">5. Barisan Hadapan Baharu: Pencerobohan AI Penjana (Gemini &amp; Copilot)</span>
        <span class="lang-en" style="display: none;">5. The Next Enclosure: Generative AI Ingestion (Gemini &amp; Copilot)</span>
      </h2>
      <p style="font-size: 0.9375rem; color: var(--text-secondary); line-height: 1.7;">
        <span class="lang-bm">
          Sejajar dengan pelaburan berbilion dolar mereka di Malaysia, Google dan Microsoft kini melancarkan gelombang penawanan seterusnya melalui <strong>Kecerdasan Buatan (AI)</strong> di bilik darjah:
        </span>
        <span class="lang-en" style="display: none;">
          Alongside their multi-billion-dollar datacenter announcements, Google and Microsoft are executing their next capture cycle via <strong>Generative AI</strong> in Malaysian schools:
        </span>
      </p>
      <ul style="margin-left: 1.5rem; margin-top: 0.75rem; color: var(--text-secondary); line-height: 1.7;">
        <li><span class="lang-bm"><strong>Google Gemini Academy &amp; Experience AI:</strong> Diserapkan terus ke dalam portal DELIMa pada tahun 2024. Guru digalakkan menggunakan Gemini untuk merangka rancangan pengajaran harian (RPH) dan soalan ujian, menyerahkan data kurikulum Malaysia untuk melatih model AI komersial AS secara percuma.</span><span class="lang-en" style="display: none;"><strong>Google Gemini Academy &amp; Experience AI:</strong> Embedded directly into DELIMa in 2024. Teachers are trained to generate lesson plans and rubrics inside Gemini, feeding localized curricular content into US proprietary foundation models without compensation.</span></li>
        <li><span class="lang-bm"><strong>Microsoft Education AI Toolkit &amp; Reading Coach:</strong> Mengintegrasikan sistem AI analitik suara dan pembacaan ke dalam bilik darjah kebangsaan.</span><span class="lang-en" style="display: none;"><strong>Microsoft Education AI Toolkit &amp; Reading Coach:</strong> Ingesting student voice telemetry and reading behavior inside national classrooms.</span></li>
        <li><span class="lang-bm"><strong>Hierarki Baharu:</strong> Apabila pergantungan kepada ciri AI ini telah mutlak, penyedia akan mengenakan yuran langganan bulanan per murid untuk ciri 'AI lanjutan', mengulangi kitaran storan berbayar sekali lagi.</span><span class="lang-en" style="display: none;"><strong>The Looming Paywall:</strong> Once pedagogical dependence is absolute, vendors will gate premium AI agents behind per-student monthly fees, replicating the storage rug-pull.</span></li>
      </ul>
    </div>

    <!-- Sovereign Exit Strategy -->
    <div class="card" style="margin-bottom: 3rem; background: linear-gradient(135deg, rgba(16, 185, 129, 0.06), rgba(56, 189, 248, 0.06)); border: 1px solid var(--accent-emerald);">
      <h2 style="font-size: 1.35rem; color: var(--accent-emerald); margin-bottom: 1rem;">
        <span class="lang-bm">6. Pelan Tindakan Berdaulat: 4 Langkah Menamatkan Monopoli Pendidikan</span>
        <span class="lang-en" style="display: none;">6. Sovereign Exit Roadmap: 4 Steps to Dismantle the Educational Pipeline</span>
      </h2>

      <div class="grid-2">
        <div style="margin-bottom: 1rem;">
          <strong style="color: var(--accent-emerald); display: block; margin-bottom: 0.25rem;">1. Pinda Seksyen 3(1) APDP 2010</strong>
          <p style="font-size: 0.875rem; color: var(--text-secondary); line-height: 1.6;">
            <span class="lang-bm">Mansuhkan pengecualian kerajaan terhadap data peribadi murid. Wajibkan audit data bebas dan larang penggunaan data sekolah untuk melatih model AI komersial swasta asing.</span>
            <span class="lang-en" style="display: none;">Repeal government immunity for student personal data. Mandate statutory data audits and ban using educational records to train foreign commercial AI models.</span>
          </p>
        </div>

        <div style="margin-bottom: 1rem;">
          <strong style="color: var(--accent-emerald); display: block; margin-bottom: 0.25rem;">2. Beralih Kepada LMS Terbuka (Moodle / Canvas FOSS)</strong>
          <p style="font-size: 0.875rem; color: var(--text-secondary); line-height: 1.6;">
            <span class="lang-bm">Bangunkan semula portal DELIMa berasaskan perisian sumber terbuka <strong>Moodle</strong> atau <strong>Canvas FOSS</strong>, dihoskan pada pelayan awan milik kerajaan di Cyberjaya (MIMOS / TM One).</span>
            <span class="lang-en" style="display: none;">Re-platform DELIMa on sovereign open-source <strong>Moodle</strong> or <strong>Canvas FOSS</strong>, hosted on domestic government infrastructure in Cyberjaya (MIMOS / TM One).</span>
          </p>
        </div>

        <div style="margin-bottom: 1rem;">
          <strong style="color: var(--accent-emerald); display: block; margin-bottom: 0.25rem;">3. Cipta 'Awan Akademik Malaysia' (Nextcloud Hub)</strong>
          <p style="font-size: 0.875rem; color: var(--text-secondary); line-height: 1.6;">
            <span class="lang-bm">Gunakan <strong>Nextcloud Enterprise + Collabora Online (LibreOffice)</strong> untuk menyediakan storan selamat, penyuntingan dokumen terbuka, dan sandaran tanpa had untuk semua 20 universiti awam dan politeknik.</span>
            <span class="lang-en" style="display: none;">Deploy <strong>Nextcloud Hub + Collabora Online (LibreOffice)</strong> across all 20 public universities, restoring sovereign unmetered storage and collaborative document editing.</span>
          </p>
        </div>

        <div style="margin-bottom: 1rem;">
          <strong style="color: var(--accent-emerald); display: block; margin-bottom: 0.25rem;">4. Rombak Silibus TVET &amp; Sains Komputer Bebas Vendor</strong>
          <p style="font-size: 0.875rem; color: var(--text-secondary); line-height: 1.6;">
            <span class="lang-bm">Ajar asas kejuruteraan sistem sebenar: Linux (LPIC/RHCSA), Kubernetes, sistem fail teragih Ceph, dan pangkalan data PostgreSQL berbanding konsol proprietari AWS atau Azure.</span>
            <span class="lang-en" style="display: none;">Mandate vendor-neutral systems engineering: Linux (LPIC), Kubernetes, Ceph, and PostgreSQL over proprietary AWS or Azure proprietary console mechanics.</span>
          </p>
        </div>
      </div>
    </div>

    <!-- Raw Research Paper Link -->
    <div style="text-align: center; margin-top: 2rem;">
      <a href="https://github.com/JomBoycott/jomboycott.github.io/blob/main/research/malaysia/education_lockin_pipeline.md" target="_blank" rel="noopener noreferrer" class="btn btn-outline" style="border-color: var(--accent-primary); color: var(--accent-primary); margin-right: 1rem;">
        <span class="lang-bm">Baca Laporan Lengkap (Markdown) ↗</span>
        <span class="lang-en" style="display: none;">Read Full Paper (Markdown) ↗</span>
      </a>
      <a href="alternatives.html" class="btn btn-primary">
        <span class="lang-bm">Terokai Alternatif Pendidikan FOSS 💡</span>
        <span class="lang-en" style="display: none;">Explore FOSS Education Alternatives 💡</span>
      </a>
    </div>
  </main>

  <!-- Footer -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <h4 class="footer-title">Amanah Digital Malaysia</h4>
          <p style="font-size: 0.8125rem; line-height: 1.6; margin-bottom: 1rem;">
            <span class="lang-bm">Kempen penyelidikan awam sumber terbuka mengenai akauntabiliti korporat teknologi, hak asasi manusia, dan kedaulatan digital nasional.</span>
            <span class="lang-en" style="display: none;">Open-source public research campaign on tech corporate accountability, human rights, and national digital sovereignty.</span>
          </p>
          <span class="badge badge-verified">Lesen CC BY-SA 4.0 &amp; MIT</span>
        </div>
        <div>
          <h4 class="footer-title">Penyelidikan</h4>
          <ul class="footer-links">
            <li><a href="education.html">Siasatan Pendidikan</a></li>
            <li><a href="evidence.html">Pangkalan Data Bukti</a></li>
            <li><a href="companies.html">Dosier Syarikat</a></li>
            <li><a href="malaysia.html">Kedaulatan Digital</a></li>
          </ul>
        </div>
        <div>
          <h4 class="footer-title">Alternatif</h4>
          <ul class="footer-links">
            <li><a href="alternatives.html">Direktori Sumber Terbuka</a></li>
            <li><a href="migrate.html">Panduan Migrasi</a></li>
            <li><a href="media.html">Galeri Risalah &amp; Poster</a></li>
            <li><a href="islam.html">Etika Islam</a></li>
          </ul>
        </div>
        <div>
          <h4 class="footer-title">Dokumentasi</h4>
          <ul class="footer-links">
            <li><a href="about.html">Tentang Kami</a></li>
            <li><a href="faq.html">Soalan Lazim (FAQ)</a></li>
            <li><a href="../CAMPAIGN_MASTER_REPORT.md">Laporan Induk</a></li>
            <li><a href="https://github.com/JomBoycott/jomboycott.github.io">GitHub</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>© 2024–2026 Kempen Akauntabiliti Teknologi Sumber Terbuka Malaysia. Dilindungi di bawah Lesen Terbuka CC BY-SA 4.0 &amp; MIT.</p>
      </div>
    </div>
  </footer>

  <script src="app.js"></script>
</body>
</html>
"""

output_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "website", "education.html"))
with open(output_path, "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)
print(f"Successfully generated {output_path} ({len(HTML_CONTENT)} bytes)")
