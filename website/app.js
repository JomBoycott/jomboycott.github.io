/**
 * Kempen Akauntabiliti Teknologi Sumber Terbuka Malaysia
 * Client-Side Dynamic Search, Theme & Data Rendering
 */

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initLanguage();
  initNavigation();

  // If on evidence page, load evidence
  if (document.getElementById('evidence-container')) {
    initEvidenceExplorer();
  }

  // If on alternatives page, load alternatives
  if (document.getElementById('alternatives-container')) {
    initAlternativesDirectory();
  }
});

/* ================= Global State ================= */
let currentLang = localStorage.getItem('lang') || 'bm';
let activeRenderEvidence = null;
let activeRenderAlternatives = null;

/* ================= Theme Toggle ================= */
function initTheme() {
  const toggleBtn = document.getElementById('theme-toggle');
  const storedTheme = localStorage.getItem('theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  
  document.documentElement.setAttribute('data-theme', storedTheme);
  updateThemeButtonText(toggleBtn, storedTheme);

  if (toggleBtn) {
    toggleBtn.addEventListener('click', () => {
      const current = document.documentElement.getAttribute('data-theme') || 'light';
      const next = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('theme', next);
      updateThemeButtonText(toggleBtn, next);
    });
  }
}

function updateThemeButtonText(btn, theme) {
  if (!btn) return;
  const isEn = currentLang === 'en';
  if (isEn) {
    btn.textContent = theme === 'dark' ? '☀️ Light' : '🌙 Dark';
  } else {
    btn.textContent = theme === 'dark' ? '☀️ Cerah' : '🌙 Gelap';
  }
}

/* ================= Language Toggle ================= */
function initLanguage() {
  const langToggle = document.getElementById('lang-toggle');

  applyLanguage(currentLang);

  if (langToggle) {
    langToggle.addEventListener('click', () => {
      currentLang = currentLang === 'bm' ? 'en' : 'bm';
      localStorage.setItem('lang', currentLang);
      applyLanguage(currentLang);
    });
  }
}

function applyLanguage(lang) {
  currentLang = lang;
  document.documentElement.setAttribute('data-lang', lang);
  document.documentElement.setAttribute('lang', lang === 'bm' ? 'ms' : 'en');

  const langToggle = document.getElementById('lang-toggle');
  if (langToggle) {
    langToggle.textContent = lang === 'bm' ? '🌐 English' : '🌐 B. Melayu';
  }

  const themeToggle = document.getElementById('theme-toggle');
  if (themeToggle) {
    const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
    updateThemeButtonText(themeToggle, currentTheme);
  }

  // Update input placeholders
  const evidenceSearch = document.getElementById('evidence-search');
  if (evidenceSearch) {
    evidenceSearch.placeholder = lang === 'bm'
      ? 'Cari topik, syarikat, atau petikan bukti (cth: Nimbus, Lavender, BSR)...'
      : 'Search topic, company, or evidence quote (e.g. Nimbus, Lavender, BSR)...';
  }

  const altSearch = document.getElementById('alt-search');
  if (altSearch) {
    altSearch.placeholder = lang === 'bm'
      ? 'Cari alternatif (cth: Nextcloud, Linux, Signal)...'
      : 'Search alternatives (e.g. Nextcloud, Linux, Signal)...';
  }

  // Toggle .lang-bm and .lang-en
  const bmElements = document.querySelectorAll('.lang-bm');
  const enElements = document.querySelectorAll('.lang-en');

  if (lang === 'bm') {
    bmElements.forEach(el => el.style.display = '');
    enElements.forEach(el => el.style.display = 'none');
  } else {
    bmElements.forEach(el => el.style.display = 'none');
    enElements.forEach(el => el.style.display = '');
  }

  // Re-render active dynamic data views
  if (typeof activeRenderEvidence === 'function') {
    activeRenderEvidence();
  }
  if (typeof activeRenderAlternatives === 'function') {
    activeRenderAlternatives();
  }
}

/* ================= Active Navigation Link ================= */
function initNavigation() {
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('.nav-links a');
  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPath || (currentPath === '' && href === 'index.html')) {
      link.classList.add('active');
    }
  });
}

/* ================= Evidence Explorer ================= */
async function initEvidenceExplorer() {
  const container = document.getElementById('evidence-container');
  const searchInput = document.getElementById('evidence-search');
  const companyFilter = document.getElementById('company-filter');
  const statusFilter = document.getElementById('status-filter');
  const countBadge = document.getElementById('evidence-count');

  let evidenceData = [];

  try {
    let res = await fetch('data/evidence.json');
    if (!res.ok) {
      res = await fetch('../evidence/evidence.json');
    }
    if (!res.ok) throw new Error('Network error');
    evidenceData = await res.json();
  } catch (err) {
    console.warn('Loading fallback evidence data:', err);
    evidenceData = getFallbackEvidence();
  }

  function renderEvidence() {
    const isEn = currentLang === 'en';
    const query = (searchInput ? searchInput.value : '').toLowerCase().trim();
    const company = companyFilter ? companyFilter.value : 'ALL';
    const status = statusFilter ? statusFilter.value : 'ALL';

    const filtered = evidenceData.filter(item => {
      const matchCompany = company === 'ALL' || item.company === company;
      const matchStatus = status === 'ALL' || item.status === status;
      const matchText = !query || 
        item.claim.toLowerCase().includes(query) ||
        item.topic.toLowerCase().includes(query) ||
        item.quote_or_evidence.toLowerCase().includes(query) ||
        item.source_title.toLowerCase().includes(query);
      return matchCompany && matchStatus && matchText;
    });

    if (countBadge) {
      countBadge.textContent = isEn ? `${filtered.length} records` : `${filtered.length} rekod`;
    }

    if (filtered.length === 0) {
      container.innerHTML = `
        <div class="card" style="text-align: center; padding: 2rem;">
          <p class="card-desc">${isEn ? 'No evidence records match your search criteria.' : 'Tiada rekod bukti sepadan dengan kriteria carian anda.'}</p>
        </div>
      `;
      return;
    }

    container.innerHTML = filtered.map(item => `
      <div class="data-card">
        <div class="data-card-header">
          <div>
            <span class="badge ${getBadgeClass(item.status)}">${item.status}</span>
            <span style="font-weight: 700; margin-left: 0.5rem; color: var(--accent-primary);">${item.company}</span>
            <span style="color: var(--text-muted); font-size: 0.8125rem;">• ${item.id}</span>
          </div>
          <div class="data-card-meta">
            <span>${item.source_tier}</span>
            <span>•</span>
            <span>${item.publication_date}</span>
          </div>
        </div>
        <h3 class="data-card-title">${escapeHtml(item.topic)}</h3>
        <p style="font-size: 0.9375rem; color: var(--text-primary); font-weight: 500;">
          ${escapeHtml(item.claim)}
        </p>
        <div class="data-card-quote">
          "${escapeHtml(item.quote_or_evidence)}"
        </div>
        <p style="font-size: 0.875rem; color: var(--text-secondary);">
          <strong>${isEn ? 'Nuance / Response:' : 'Nuansa / Maklum Balas:'}</strong> ${escapeHtml(item.counterclaim_or_nuance)}
        </p>
        <div class="data-card-footer">
          <div>
            <strong>${isEn ? 'Source:' : 'Sumber:'}</strong> 
            <a href="${item.source_url}" target="_blank" rel="noopener noreferrer" style="color: var(--accent-primary); text-decoration: underline;">
              ${escapeHtml(item.source_title)}
            </a> (${item.source_type})
          </div>
          <div style="color: var(--text-muted); font-size: 0.75rem;">
            ${isEn ? 'Verified:' : 'Disahkan:'} ${item.last_verified}
          </div>
        </div>
      </div>
    `).join('');
  }

  activeRenderEvidence = renderEvidence;

  if (searchInput) searchInput.addEventListener('input', renderEvidence);
  if (companyFilter) companyFilter.addEventListener('change', renderEvidence);
  if (statusFilter) statusFilter.addEventListener('change', renderEvidence);

  renderEvidence();
}

/* ================= Alternatives Directory ================= */
async function initAlternativesDirectory() {
  const container = document.getElementById('alternatives-container');
  const searchInput = document.getElementById('alt-search');
  const categoryFilter = document.getElementById('category-filter');
  const countBadge = document.getElementById('alt-count');

  let alternativesData = [];

  try {
    let res = await fetch('data/alternatives.json');
    if (!res.ok) {
      res = await fetch('../alternatives/alternatives.json');
    }
    if (!res.ok) throw new Error('Network error');
    alternativesData = await res.json();
  } catch (err) {
    console.warn('Loading fallback alternatives data:', err);
    alternativesData = getFallbackAlternatives();
  }

  function renderAlternatives() {
    const isEn = currentLang === 'en';
    const query = (searchInput ? searchInput.value : '').toLowerCase().trim();
    const category = categoryFilter ? categoryFilter.value : 'ALL';

    const filtered = alternativesData.filter(item => {
      const matchCat = category === 'ALL' || item.category === category;
      const matchText = !query ||
        item.project.toLowerCase().includes(query) ||
        item.category.toLowerCase().includes(query) ||
        item.replaces.some(r => r.toLowerCase().includes(query)) ||
        item.malaysian_suitability_summary.toLowerCase().includes(query);
      return matchCat && matchText;
    });

    if (countBadge) {
      countBadge.textContent = isEn ? `${filtered.length} alternatives` : `${filtered.length} alternatif`;
    }

    if (filtered.length === 0) {
      container.innerHTML = `
        <div class="card" style="text-align: center; padding: 2rem;">
          <p class="card-desc">${isEn ? 'No software alternatives match your search criteria.' : 'Tiada perisian alternatif sepadan dengan carian anda.'}</p>
        </div>
      `;
      return;
    }

    container.innerHTML = filtered.map(item => `
      <div class="data-card">
        <div class="data-card-header">
          <div>
            <span class="badge badge-verified">${item.maturity}</span>
            <span style="font-weight: 700; margin-left: 0.5rem; color: var(--accent-purple);">${item.category}</span>
          </div>
          <div class="data-card-meta">
            <span>${isEn ? 'License:' : 'Lesen:'} ${item.license}</span>
            <span>•</span>
            <span>${isEn ? 'Difficulty:' : 'Tahap:'} ${item.difficulty}</span>
          </div>
        </div>
        <div style="display: flex; align-items: baseline; gap: 0.75rem; flex-wrap: wrap;">
          <h3 class="data-card-title" style="font-size: 1.35rem;">${escapeHtml(item.project)}</h3>
          <span style="font-size: 0.875rem; color: var(--text-muted);">
            ${isEn ? 'Replaces:' : 'Menggantikan:'} <strong>${item.replaces.join(', ')}</strong>
          </span>
        </div>
        <p style="font-size: 0.9375rem; color: var(--text-secondary);">
          <strong>${isEn ? 'Suitability for Malaysia:' : 'Kesesuaian Malaysia:'}</strong> ${escapeHtml(item.malaysian_suitability_summary)}
        </p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 0.5rem; font-size: 0.8125rem; background: var(--bg-surface-elevated); padding: 0.75rem; border-radius: var(--radius-sm);">
          <div><strong>${isEn ? 'Storage/RAM:' : 'Storan/RAM:'}</strong> ${escapeHtml(item.self_hosting_requirements)}</div>
          <div><strong>${isEn ? 'Cost Model:' : 'Model Kos:'}</strong> ${escapeHtml(item.cost_model)}</div>
          <div><strong>${isEn ? 'Privacy:' : 'Privasi:'}</strong> ${escapeHtml(item.privacy_rating)}</div>
        </div>
        <div class="data-card-footer">
          <div style="display: flex; gap: 1rem;">
            <a href="${item.website}" target="_blank" rel="noopener noreferrer" style="color: var(--accent-primary); font-weight: 600; text-decoration: underline;">
              ${isEn ? 'Project Website ↗' : 'Laman Web Projek ↗'}
            </a>
            <a href="${item.github}" target="_blank" rel="noopener noreferrer" style="color: var(--text-secondary); text-decoration: underline;">
              ${isEn ? 'Source Code ↗' : 'Kod Sumber (GitHub/Git) ↗'}
            </a>
          </div>
          <div style="color: var(--text-muted); font-size: 0.75rem;">
            ID: ${item.id}
          </div>
        </div>
      </div>
    `).join('');
  }

  activeRenderAlternatives = renderAlternatives;

  if (searchInput) searchInput.addEventListener('input', renderAlternatives);
  if (categoryFilter) categoryFilter.addEventListener('change', renderAlternatives);

  renderAlternatives();
}

function getBadgeClass(status) {
  switch (status) {
    case 'VERIFIED': return 'badge-verified';
    case 'STRONGLY_SUPPORTED': return 'badge-supported';
    default: return 'badge-disputed';
  }
}

function escapeHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

/* ================= Built-in Fallbacks for file:// Protocol ================= */
function getFallbackEvidence() {
  return [
    {
      id: "EVID-001",
      company: "Google",
      topic: "Project Nimbus Tender Award",
      claim: "Google and Amazon were jointly awarded the $1.2 billion Project Nimbus contract by the Israeli government.",
      status: "VERIFIED",
      source_tier: "Tier 1",
      source_type: "Government Tender",
      source_title: "Israel Ministry of Finance Nimbus Announcement",
      source_url: "https://www.gov.il/en/departments/news/press_21042021",
      publication_date: "2021-04-21",
      quote_or_evidence: "The tender committee headed by the Accountant General announced that Google and AWS are the winning providers for Project Nimbus.",
      counterclaim_or_nuance: "Google states the contract is for commercial workloads of civilian government ministries.",
      last_verified: "2026-09-15"
    },
    {
      id: "EVID-002",
      company: "Google",
      topic: "Ministry of Defense Cloud Access",
      claim: "Google negotiated direct cloud computing and consulting contracts with the Israeli Ministry of Defense.",
      status: "STRONGLY_SUPPORTED",
      source_tier: "Tier 2",
      source_type: "Investigative Journalism",
      source_title: "Time Magazine: Google's Project Nimbus Contract With Israel's Ministry of Defense Revealed",
      source_url: "https://time.com/6966102/google-contract-israel-defense-ministry-gaza/",
      publication_date: "2024-04-12",
      quote_or_evidence: "According to a company document viewed by TIME, the Israeli Ministry of Defense has its own landing zone into Google Cloud.",
      counterclaim_or_nuance: "Google states work is commercial and not directed at weapons development.",
      last_verified: "2026-09-15"
    },
    {
      id: "EVID-006",
      company: "Amazon",
      topic: "AWS Israel Region and $7.2B Investment",
      claim: "AWS launched the AWS Israel (Tel Aviv) Region committing $7.2 billion through 2037.",
      status: "VERIFIED",
      source_tier: "Tier 1",
      source_type: "Corporate SEC / Press Announcement",
      source_title: "AWS Launches Region in Israel (il-central-1)",
      source_url: "https://press.aboutamazon.com/2023/8/aws-launches-region-in-israel",
      publication_date: "2023-08-01",
      quote_or_evidence: "AWS today announced the launch of the AWS Israel (Tel Aviv) Region, investing an estimated $7.2 billion through 2037.",
      counterclaim_or_nuance: "AWS highlights customer demand across the enterprise, healthcare, and public sector.",
      last_verified: "2026-09-15"
    },
    {
      id: "EVID-009",
      company: "Microsoft",
      topic: "2025 Surveillance Access Restrictions",
      claim: "Microsoft terminated Israeli military access to specific surveillance tools in September 2025.",
      status: "VERIFIED",
      source_tier: "Tier 1",
      source_type: "Human Rights Compliance",
      source_title: "Business & Human Rights Resource Centre: Microsoft surveillance tools termination",
      source_url: "https://www.business-humanrights.org/en/latest-news/microsoft-surveillance-israel-military-cut-off/",
      publication_date: "2025-09-20",
      quote_or_evidence: "Microsoft took action to terminate access to specific cloud-based surveillance capabilities for Israeli military users.",
      counterclaim_or_nuance: "Demonstrates Microsoft enforcement of Acceptable Use Policies; general enterprise licensing remains active.",
      last_verified: "2026-09-15"
    },
    {
      id: "EVID-011",
      company: "Meta",
      topic: "BSR Human Rights Due Diligence Audit",
      claim: "An independent audit concluded Meta's content moderation had an adverse human rights impact on Palestinians.",
      status: "VERIFIED",
      source_tier: "Tier 1",
      source_type: "Independent Commissioned Audit",
      source_title: "BSR Human Rights Due Diligence of Meta's Impacts",
      source_url: "https://www.bsr.org/en/our-insights/reports/human-rights-due-diligence-meta-israel-palestine",
      publication_date: "2022-09-22",
      quote_or_evidence: "Meta's actions appear to have had an adverse human rights impact on Palestinian users' rights to freedom of expression.",
      counterclaim_or_nuance: "BSR found no intentional bias by Meta staff, attributing issues to algorithmic misclassification.",
      last_verified: "2026-09-15"
    },
    {
      id: "EVID-017",
      company: "General/Cross-Platform",
      topic: "European State Divestment & FOSS Migration (Wired Investigation)",
      claim: "European governments and public bodies are systematically replacing American Big Tech (Microsoft, Google, AWS) with open-source software and sovereign infrastructure due to CLOUD Act surveillance, surging license costs, and sovereignty risks.",
      status: "VERIFIED",
      source_tier: "Tier 2",
      source_type: "Investigative Journalism / Public Government Decrees",
      source_title: "Wired: All the Ways Europe Is Ditching American Technology",
      source_url: "https://www.wired.com/story/all-the-ways-europe-is-ditching-american-technology/",
      publication_date: "2026-06-10",
      quote_or_evidence: "From German states migrating 30,000 PCs to Linux and LibreOffice, to French ministries banning Microsoft 365 and Google Workspace in schools, European administrations are actively ditching US cloud giants in favor of sovereign, open source stacks.",
      counterclaim_or_nuance: "Transitioning large public administrations requires careful change management and legacy format compatibility.",
      last_verified: "2026-09-15"
    }
  ];
}

function getFallbackAlternatives() {
  return [
    {
      id: "ALT-001",
      project: "SearXNG",
      category: "Search",
      replaces: ["Google Search", "Microsoft Bing"],
      license: "AGPL-3.0",
      website: "https://searxng.org",
      github: "https://github.com/searxng/searxng",
      self_hosting_requirements: "1 vCPU, 512 MB RAM",
      difficulty: "Beginner",
      cost_model: "100% Free Open Source",
      privacy_rating: "Zero-tracking, strips IP headers",
      maturity: "Battle-Tested",
      malaysian_suitability_summary: "Sesuai untuk individu dan agensi yang mahukan carian bebas penjejakan."
    },
    {
      id: "ALT-003",
      project: "Nextcloud Hub",
      category: "Cloud Storage",
      replaces: ["Google Drive", "OneDrive"],
      license: "AGPL-3.0",
      website: "https://nextcloud.com",
      github: "https://github.com/nextcloud/server",
      self_hosting_requirements: "2 vCPU, 4 GB RAM",
      difficulty: "Intermediate",
      cost_model: "Free Community Edition",
      privacy_rating: "End-to-End Encryption, local data residency",
      maturity: "Battle-Tested",
      malaysian_suitability_summary: "Pengganti Google Workspace paling lengkap untuk sekolah dan pejabat kerajaan."
    },
    {
      id: "ALT-004",
      project: "LibreOffice",
      category: "Office & Productivity",
      replaces: ["Microsoft Office 365", "Google Docs"],
      license: "MPL-2.0",
      website: "https://www.libreoffice.org",
      github: "https://github.com/LibreOffice/core",
      self_hosting_requirements: "Standard desktop PC",
      difficulty: "Beginner",
      cost_model: "100% Free Open Source",
      privacy_rating: "Offline capability, zero cloud telemetry",
      maturity: "Battle-Tested",
      malaysian_suitability_summary: "Menjimatkan yuran pelesenan pejabat ratusan juta ringgit."
    },
    {
      id: "ALT-006",
      project: "Matrix & Element",
      category: "Messaging",
      replaces: ["WhatsApp", "Slack", "Teams"],
      license: "Apache-2.0",
      website: "https://matrix.org",
      github: "https://github.com/element-hq/element-web",
      self_hosting_requirements: "2 vCPU, 4 GB RAM",
      difficulty: "Intermediate",
      cost_model: "Free Open Source",
      privacy_rating: "End-to-End Encryption, federated",
      maturity: "Battle-Tested",
      malaysian_suitability_summary: "Protokol terbuka terbaik untuk pemesejan berdaulat sektor awam."
    },
    {
      id: "ALT-011",
      project: "Ollama",
      category: "Artificial Intelligence",
      replaces: ["ChatGPT", "Google Gemini API", "Copilot"],
      license: "MIT",
      website: "https://ollama.com",
      github: "https://github.com/ollama/ollama",
      self_hosting_requirements: "Modern CPU/GPU, 16 GB RAM",
      difficulty: "Beginner",
      cost_model: "100% Free Open Source",
      privacy_rating: "100% data remains in local memory",
      maturity: "Production-Ready",
      malaysian_suitability_summary: "Kritikal untuk hospital, bank, dan peguam menjaga rahsia dokumen."
    }
  ];
}
