#!/usr/bin/env python3
"""
Generate 15 high-resolution campaign posters/leaflets (1080x1350 px, 4:5 aspect ratio).
- 10 Islamic foundation posters (Qur'an & Hadith with Pango-shaped Arabic typography + bilingual commentary)
- 5 Creative campaign posters (Malaysian sovereignty, European exit, 6-level roadmap, FOSS matrix, tech workers)
Outputs SVG, PNG, and JPEG to both campaign/posters/ and website/media/posters/.
"""

import os
import sys
import subprocess
import html
import textwrap

CAMPAIGN_DIR = "/home/ben/Opensource/campaign/posters"
WEBSITE_DIR = "/home/ben/Opensource/website/media/posters"

os.makedirs(CAMPAIGN_DIR, exist_ok=True)
os.makedirs(WEBSITE_DIR, exist_ok=True)

def esc(s):
    return html.escape(str(s))

def render_arabic_snippet(lines, output_png, font_size=32):
    """
    Renders multi-line Arabic text using ImageMagick's pango engine with full HarfBuzz
    shaping, BiDi connectivity, and authentic harakat / diacritics.
    lines is a list of tuples: (text, color)
    """
    spans = []
    for text, color in lines:
        spans.append(f'<span font="IBM Plex Sans Arabic Semi-Bold {font_size}" foreground="{color}">{text}</span>')
    markup = "\n".join(spans)
    
    cmd = [
        "convert",
        "-background", "none",
        f"pango:{markup}",
        output_png
    ]
    subprocess.run(cmd, check=True)

def composite_image(base_png, overlay_png, offset_y, output_png):
    """Composites an overlay image onto base_png centered horizontally with y offset."""
    cmd = [
        "convert",
        base_png,
        overlay_png,
        "-gravity", "North",
        "-geometry", f"+0+{offset_y}",
        "-composite",
        output_png
    ]
    subprocess.run(cmd, check=True)

def convert_to_jpeg(png_path, jpg_path):
    subprocess.run(["convert", "-quality", "95", png_path, jpg_path], check=True)

# -----------------------------------------------------------------------------
# ISLAMIC POSTERS DATA (1 - 10)
# -----------------------------------------------------------------------------
ISLAMIC_POSTERS = [
    {
        "id": "poster_01_quran_5_2",
        "num": "01",
        "category": "SHARIAH PRINCIPLE • COMPLICITY",
        "title": "Forbidding Complicity in Sin",
        "subtitle": "Surah Al-Ma'idah (5:2) & Cloud Infrastructure Divestment",
        "arabic": [
            ("وَتَعَاوَنُوا عَلَى الْبِرِّ وَالتَّقْوَىٰ", "#fef08a"),
            ("وَلَا تَعَاوَنُوا عَلَى الْإِثْمِ وَالْعُدْوَانِ", "#f87171")
        ],
        "ref": "AL-QUR'AN AL-KAREEM • SURAH AL-MA'IDAH (5:2)",
        "en": [
            "\"And cooperate in righteousness and piety, but do not cooperate in",
            "sin and aggression. And fear Allah; indeed, Allah is severe in penalty.\""
        ],
        "bm": [
            "\"Dan tolong-menolonglah kamu dalam kebajikan dan ketaqwaan, dan janganlah",
            "kamu tolong-menolong dalam berbuat dosa dan permusuhan / pencerobohan.\""
        ],
        "why_title": "WHY MUSLIM TECH LEADERS & ENTERPRISES MUST BOYCOTT",
        "points": [
            ("Cloud Subscriptions Directly Fund Weaponized Infrastructure:",
             "Enterprise cloud spend on Google Cloud and AWS directly finances joint military AI surveillance ecosystems (e.g. Project Nimbus), used for automated warfare and oppression."),
            ("Commercial Contracts Constitute Direct Cooperation ('I'anah):",
             "Classical jurisprudence (Al-Qurtubi, Ibn Taymiyyah) dictates that financial dealings which strengthen an oppressor's capacity to commit violence are strictly prohibited (Haram).")
        ],
        "directive_label": "ACTIONABLE DIRECTIVE FOR CTOs & LEADERS",
        "directive": "Audit third-party cloud dependencies • Migrate workloads to Sovereign / FOSS infrastructure"
    },
    {
        "id": "poster_02_hadith_bukhari_2444",
        "num": "02",
        "category": "SUNNAH DIRECTIVE • BOYCOTT PRESSURE",
        "title": "Restraining Oppressors is Helping Them",
        "subtitle": "Sahih al-Bukhari (2444) & Halting Corporate Harm",
        "arabic": [
            ("انْصُرْ أَخَاكَ ظَالِمًا أَوْ مَظْلُومًا", "#fef08a"),
            ("تَحْجُزُهُ أَوْ تَمْنَعُهُ مِنَ الظُّلْمِ فَإِنَّ ذَلِكَ نَصْرُهُ", "#38bdf8")
        ],
        "ref": "HADITH SHARIF • SAHIH AL-BUKHARI (2444)",
        "en": [
            "\"Help your brother whether he is an oppressor or oppressed.\" A man said: \"I help",
            "him if he is oppressed, but how if he is an oppressor?\" The Prophet (s.a.w.) said:",
            "\"By preventing him from oppressing others; that is how you help him.\""
        ],
        "bm": [
            "Sabda Rasulullah (s.a.w.): \"Tolonglah saudaramu yang zalim atau yang dizalimi.\"",
            "Sahabat bertanya: \"Bagaimanakah menolongnya jika dia zalim?\" Sabda baginda:",
            "\"Kamu menghalangnya daripada melakukan kezaliman; itulah cara membantunya.\""
        ],
        "why_title": "WHY CORPORATE SANCTION HALTS UNCHECKED VIOLENCE",
        "points": [
            ("Boycott as the Primary Restraining Mechanism:",
             "Big Tech giants operate purely on commercial leverage. Withdrawing institutional subscriptions and public contracts strips away the financial incentive to serve military apartheid."),
            ("Preventing Complicity Protects the Entire Ecosystem:",
             "Allowing tech monopolies to weaponize cloud computing unchecked normalizes global authoritarian surveillance. Halting capital flow forces corporate policy reversal.")
        ],
        "directive_label": "ACTIONABLE DIRECTIVE FOR CTOs & LEADERS",
        "directive": "De-fund complicit ad exchanges • Cancel enterprise suite renewals with complicit giants"
    },
    {
        "id": "poster_03_hadith_muslim_2577",
        "num": "03",
        "category": "HADITH QUDSI • UNIVERSAL BAN ON ZULM",
        "title": "Oppression is Mutually Forbidden",
        "subtitle": "Sahih Muslim (2577) & The Absolute Ban on Weaponized Tech",
        "arabic": [
            ("يَا عِبَادِي إِنِّي حَرَّمْتُ الظُّلْمَ عَلَىٰ نَفْسِي", "#fef08a"),
            ("وَجَعَلْتُهُ بَيْنَكُمْ مُحَرَّمًا فَلَا تَظَالَمُوا", "#f87171")
        ],
        "ref": "HADITH QUDSI • SAHIH MUSLIM (2577)",
        "en": [
            "Allah the Almighty says: \"O My servants! I have forbidden oppression for",
            "Myself and have made it forbidden amongst you, so do not oppress one another.\""
        ],
        "bm": [
            "Firman Allah Taala: \"Wahai hamba-hamba-Ku, sesungguhnya Aku telah mengharamkan",
            "kezaliman ke atas diri-Ku dan menjadikannya haram di antara kamu, maka janganlah kamu saling menzalimi.\""
        ],
        "why_title": "WHY DIGITAL SYSTEMS ARE NOT MORALLY NEUTRAL",
        "points": [
            ("Technology Built for Tyranny is Inherently Corrupt:",
             "Facial recognition checkpoints, biometric databases of occupied populations, and autonomous target generation systems directly implement systemic, automated zulm (oppression)."),
            ("The Developer's Moral Boundary:",
             "Muslim tech founders, engineers, and procurement committees cannot remain indifferent. Deploying code or paying servers that power oppression violates divine law.")
        ],
        "directive_label": "ACTIONABLE DIRECTIVE FOR CTOs & LEADERS",
        "directive": "Refuse software engineering and data contracts connected to military occupation and apartheid"
    },
    {
        "id": "poster_04_quran_11_113",
        "num": "04",
        "category": "DIVINE WARNING • REJECTING LOCK-IN",
        "title": "Do Not Incline Toward Oppressors",
        "subtitle": "Surah Hud (11:113) & Severing Big Tech Dependency",
        "arabic": [
            ("وَلَا تَرْكَنُوا إِلَى الَّذِينَ ظَلَمُوا فَتَمَسَّكُمُ النَّارُ", "#f87171"),
            ("وَمَا لَكُم مِّن دُونِ اللَّهِ مِنْ أَوْلِيَاءَ", "#fef08a")
        ],
        "ref": "AL-QUR'AN AL-KAREEM • SURAH HUD (11:113)",
        "en": [
            "\"And do not incline toward those who do wrong, lest you be touched by",
            "the Fire, and you would not have other than Allah any protectors.\""
        ],
        "bm": [
            "\"Dan janganlah kamu cenderung kepada orang-orang yang berlaku zalim,",
            "maka kamu akan disambar oleh api neraka, dan tiadalah bagi kamu penolong selain Allah.\""
        ],
        "why_title": "WHY PLATFORM LOCK-IN IS MORAL & STRATEGIC SUBMISSION",
        "points": [
            ("Normalizing Big Tech Entrenches Complicity:",
             "When Muslim universities, governments, and enterprises make Microsoft 365 or Google Workspace their default foundation, they legitimize monopolies that arm oppressors."),
            ("Digital Reliance Erode Ethical Independence:",
             "The Arabic term 'tarkanu' signifies subtle leaning, compromise, and dependency. We must build independent, sovereign alternatives rather than lean upon unjust empires.")
        ],
        "directive_label": "ACTIONABLE DIRECTIVE FOR CTOs & LEADERS",
        "directive": "Transition enterprise communication to Nextcloud, Matrix, and Proton to sever dependency"
    },
    {
        "id": "poster_05_hadith_bukhari_2447",
        "num": "05",
        "category": "SPIRITUAL WARNING • MORAL ACCOUNTABILITY",
        "title": "The Cry of the Oppressed",
        "subtitle": "Sahih al-Bukhari (2447) & The Reality of Divine Justice",
        "arabic": [
            ("وَاتَّقِ دَعْوَةَ الْمَظْلُومِ", "#f87171"),
            ("فَإِنَّهُ لَيْسَ بَيْنَهَا وَبَيْنَ اللَّهِ حِجَابٌ", "#fef08a")
        ],
        "ref": "HADITH SHARIF • SAHIH AL-BUKHARI (2447) / MUSLIM (2584)",
        "en": [
            "The Prophet (s.a.w.) instructed Mu'adh: \"And beware of the supplication of the",
            "oppressed, for indeed there is no barrier between it and Allah.\""
        ],
        "bm": [
            "Sabda Rasulullah (s.a.w.) kepada Mu'adh: \"Dan takutilah doa orang yang dizalimi,",
            "kerana sesungguhnya tidak ada sebarang hijab (penghalang) antaranya dengan Allah.\""
        ],
        "why_title": "WHY NO TECH EXECUTIVE CAN ESCAPE DIVINE ACCOUNTABILITY",
        "points": [
            ("The Prayers of Victims Pierce Every Cloud Firewall:",
             "Thousands of innocent families in Gaza crushed under algorithmic drone campaigns pray day and night. Their prayers pierce the heavens. No corporate liability shield protects against Allah."),
            ("Blood-Stained Balance Sheets:",
             "Every cloud compute invoice paid to vendors facilitating mass civilian slaughter carries moral contamination. Ethical leadership requires total divestment from blood tech.")
        ],
        "directive_label": "ACTIONABLE DIRECTIVE FOR CTOs & LEADERS",
        "directive": "Divest corporate reserve funds and pension assets from complicit Big Tech stock indices"
    },
    {
        "id": "poster_06_quran_4_75",
        "num": "06",
        "category": "QUR'ANIC MANDATE • DEFENDING THE WEAK",
        "title": "Duty to Defend the Weak (Mustad'afin)",
        "subtitle": "Surah An-Nisa' (4:75) & Digital Solidarity as Jihad",
        "arabic": [
            ("وَمَا لَكُمْ لَا تُقَاتِلُونَ فِي سَبِيلِ اللَّهِ", "#38bdf8"),
            ("وَالْمُسْتَضْعَفِينَ مِنَ الرِّجَالِ وَالنِّسَاءِ وَالْوِلْدَانِ", "#fef08a")
        ],
        "ref": "AL-QUR'AN AL-KAREEM • SURAH AN-NISA' (4:75)",
        "en": [
            "\"And what is with you that you fight not in the cause of Allah and for the oppressed",
            "among men, women, and children who cry: 'Our Lord, take us out of this city of oppressors'?\""
        ],
        "bm": [
            "\"Dan apakah yang menghalang kamu daripada berjuang pada jalan Allah dan membela orang-orang",
            "yang tertindas daripada lelaki, wanita serta kanak-kanak yang berdoa meminta pertolongan?\""
        ],
        "why_title": "WHY MODERN STRUGGLE IS ECONOMIC & ARCHITECTURAL",
        "points": [
            ("Economic & Digital Struggle is an Obligation:",
             "Modern warfare relies on cloud data centers, fiber cables, and AI target banks. Boycotting big tech is a primary non-violent frontline to dismantle the architecture of oppression."),
            ("Building Sovereign Open-Source Protects Human Lives:",
             "When we replace proprietary Western big tech with sovereign, decentralized infrastructure, we protect human rights defenders and journalists from targeted censorship and tracking.")
        ],
        "directive_label": "ACTIONABLE DIRECTIVE FOR CTOs & LEADERS",
        "directive": "Contribute developer hours and corporate sponsorship to secure, privacy-preserving FOSS projects"
    },
    {
        "id": "poster_07_quran_4_135",
        "num": "07",
        "category": "ETHICAL PRINCIPLE • UNCOMPROMISING JUSTICE",
        "title": "Stand Firm for Justice",
        "subtitle": "Surah An-Nisa' (4:135) & Ethics Over Commercial Convenience",
        "arabic": [
            ("كُونُوا قَوَّامِينَ بِالْقِسْطِ شُهَدَاءَ لِلَّهِ", "#fef08a"),
            ("وَلَوْ عَلَىٰ أَنفُسِكُمْ أَوِ الْوَالِدَيْنِ وَالْأَقْرَبِينَ", "#38bdf8")
        ],
        "ref": "AL-QUR'AN AL-KAREEM • SURAH AN-NISA' (4:135)",
        "en": [
            "\"O you who have believed, be persistently standing firm in justice, witnesses",
            "to Allah, even if it be against yourselves or parents and relatives.\""
        ],
        "bm": [
            "\"Wahai orang-orang yang beriman, jadilah kamu penegak keadilan yang teguh,",
            "menjadi saksi kerana Allah sekalipun terhadap diri kamu sendiri.\""
        ],
        "why_title": "WHY CONVENIENCE CAN NEVER JUSTIFY COMPROMISE",
        "points": [
            ("Migration Friction is a Worthy Sacrifice:",
             "Switching from AWS or Microsoft to sovereign Linux and OpenStack takes engineering effort. But true justice demands that technical ease cannot be bought with the blood of our brothers."),
            ("Integrity Over Short-Term Vendor Incentives:",
             "Free cloud credits and subsidized enterprise programs are bait designed to secure vendor lock-in. Principled leadership rejects handouts from complicit empires.")
        ],
        "directive_label": "ACTIONABLE DIRECTIVE FOR CTOs & LEADERS",
        "directive": "Establish an Ethical Technology Procurement Policy with mandatory human rights compliance audits"
    },
    {
        "id": "poster_08_hadith_muslim_78",
        "num": "08",
        "category": "CALL TO ACTION • THE DEVELOPER'S HAND",
        "title": "Changing Wrong with Hand & Code",
        "subtitle": "Sahih Muslim (78) & The Actionable Duty of Technologists",
        "arabic": [
            ("مَنْ رَأَى مِنْكُمْ مُنْكَرًا فَلْيُغَيِّرْهُ بِيَدِهِ", "#fef08a"),
            ("فَإِنْ لَمْ يَسْتَطِعْ فَبِلِسَانِهِ ، فَإِنْ لَمْ يَسْتَطِعْ فَبِقَلْبِهِ", "#f87171")
        ],
        "ref": "HADITH SHARIF • SAHIH MUSLIM (78)",
        "en": [
            "The Prophet (s.a.w.) said: \"Whoever among you sees an evil, let him change it with his hand;",
            "if he cannot, then with his tongue; if he cannot, then with his heart — and that is the weakest of faith.\""
        ],
        "bm": [
            "Sabda Rasulullah (s.a.w.): \"Sesiapa antara kamu melihat kemungkaran, ubahlah dengan tangannya;",
            "jika tidak mampu, dengan lidahnya; jika tidak mampu, dengan hatinya — dan itulah selemah-lemah iman.\""
        ],
        "why_title": "THE 'HAND' OF THE ENGINEER IS THE CODE HE COMMITS",
        "points": [
            ("Procurement Authority is Direct Power ('Yad'):",
             "For system architects, DevOps engineers, and CIOs, 'changing with the hand' means canceling cloud instances, refactoring away from proprietary APIs, and deploying sovereign stacks."),
            ("Boycott is Active Resistance, Not Mere Sentiment:",
             "Merely disliking genocide in one's heart while continuing to wire millions in tech subscriptions is the weakest state. Real faith manifests in architectural decisions.")
        ],
        "directive_label": "ACTIONABLE DIRECTIVE FOR CTOs & LEADERS",
        "directive": "Deprovision proprietary Big Tech SaaS; redeploy workloads onto self-hosted open-source clusters"
    },
    {
        "id": "poster_09_quran_4_58_amanah",
        "num": "09",
        "category": "SACRED TRUST • DATA SOVEREIGNTY",
        "title": "Data as a Sacred Trust (Amanah)",
        "subtitle": "Surah An-Nisa' (4:58) & Guarding Ummah Infrastructure",
        "arabic": [
            ("إِنَّ اللَّهَ يَأْمُرُكُمْ أَن تُؤَدُّوا الْأَمَانَاتِ إِلَىٰ أَهْلِهَا", "#fef08a"),
            ("وَإِذَا حَكَمْتُم بَيْنَ النَّاسِ أَن تَحْكُمُوا بِالْعَدْلِ", "#38bdf8")
        ],
        "ref": "AL-QUR'AN AL-KAREEM • SURAH AN-NISA' (4:58)",
        "en": [
            "\"Indeed, Allah commands you to render trusts to whom they are due and",
            "when you judge between people to judge with justice. Excellent is that which Allah instructs you.\""
        ],
        "bm": [
            "\"Sesungguhnya Allah menyuruh kamu menyampaikan amanah kepada pemiliknya yang berhak,",
            "dan apabila kamu menetapkan hukum antara manusia hendaklah kamu menghukum dengan adil.\""
        ],
        "why_title": "WHY SURRENDERING DATA TO FOREIGN CLOUDS BREACHES AMANAH",
        "points": [
            ("Citizen & Customer Privacy is a Sacred Trust:",
             "Enterprise user data, healthcare records, and national communications are an Amanah. Entrusting them to US tech firms subject to the foreign CLOUD Act violates this trust."),
            ("The Risk of Foreign Surveillance Subpoenas:",
             "US statutes permit warrantless seizure of offshore data hosted with American firms. True custody requires cryptographic encryption keys and sovereign, local hosting.")
        ],
        "directive_label": "ACTIONABLE DIRECTIVE FOR CTOs & LEADERS",
        "directive": "Migrate national and enterprise databases to local, sovereign data centres (TM One, AIMS, MyKRIS)"
    },
    {
        "id": "poster_10_fiqh_dar_al_mafasid",
        "num": "10",
        "category": "FIQH MAXIM • PRECEDENCE OF HARM REDUCTION",
        "title": "Warding Off Harm Precedes Profit",
        "subtitle": "Dar' al-mafasid muqaddam 'ala jalb al-masalih & Tech Procurement",
        "arabic": [
            ("دَرْءُ الْمَفَاسِدِ", "#f87171"),
            ("مُقَدَّمٌ عَلَىٰ جَلْبِ الْمَصَالِحِ", "#fef08a")
        ],
        "ref": "USUL AL-FIQH • FOUNDATIONAL LEGAL MAXIM (AL-QAWA'ID AL-FIQHIYYAH)",
        "en": [
            "\"Warding off harm takes precedence over acquiring benefits.\"",
            "— Universal legal maxim affirmed across all major schools of Islamic jurisprudence."
        ],
        "bm": [
            "\"Menolak kemudaratan didahulukan daripada mengambil kemaslahatan atau keuntungan.\"",
            "— Kaedah fiqhiyyah asas yang disepakati oleh ijma' para ulama dan sarjana syariah."
        ],
        "why_title": "COMMERCIAL CONVENIENCE IS NULLIFIED BY LETHAL HARM",
        "points": [
            ("Convenience is Maslahah; Genocide is Mafsadah:",
             "Integrated office tools or cheap cloud pricing are minor conveniences (masalih). Providing capital to corporations enabling genocide is catastrophic harm (mafsadah 'uzma)."),
            ("The Shariah Ruling is Definite:",
             "Whenever a commercial benefit facilitates severe real-world violence, the legal obligation to avert the harm unconditionally overrides any commercial advantage.")
        ],
        "directive_label": "ACTIONABLE DIRECTIVE FOR CTOs & LEADERS",
        "directive": "Cancel contracts with complicit providers immediately; no discount justifies complicity in violence"
    }
]

# -----------------------------------------------------------------------------
# SVG TEMPLATE BUILDERS
# -----------------------------------------------------------------------------

def build_islamic_poster_svg(data):
    """Builds base SVG for Islamic poster (Arabic text composited via Pango)."""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1350" viewBox="0 0 1080 1350">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070a13" />
      <stop offset="45%" stop-color="#0b1326" />
      <stop offset="100%" stop-color="#041d1a" />
    </linearGradient>
    <linearGradient id="cardGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#131c31" stop-opacity="0.95" />
      <stop offset="100%" stop-color="#0c1322" stop-opacity="0.95" />
    </linearGradient>
    <linearGradient id="emeraldGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#059669" />
      <stop offset="100%" stop-color="#10b981" />
    </linearGradient>
    <linearGradient id="blueHeader" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0369a1" stop-opacity="0.6" />
      <stop offset="100%" stop-color="#0284c7" stop-opacity="0.6" />
    </linearGradient>
  </defs>

  <!-- Background -->
  <rect width="1080" height="1350" fill="url(#bgGrad)" />

  <!-- Grid decoration -->
  <path d="M 0,200 L 1080,200 M 0,400 L 1080,400 M 0,600 L 1080,600 M 0,800 L 1080,800 M 0,1000 L 1080,1000" stroke="#1e293b" stroke-width="1" stroke-opacity="0.25" />
  <path d="M 200,0 L 200,1350 M 400,0 L 400,1350 M 600,0 L 600,1350 M 800,0 L 800,1350 M 1000,0 L 1000,1350" stroke="#1e293b" stroke-width="1" stroke-opacity="0.25" />

  <!-- Ambient Glow -->
  <circle cx="950" cy="180" r="280" fill="#059669" opacity="0.10" />
  <circle cx="100" cy="1150" r="320" fill="#0284c7" opacity="0.08" />

  <!-- Top Header Bar -->
  <rect x="70" y="55" width="940" height="42" rx="8" fill="#1e293b" fill-opacity="0.65" stroke="#334155" stroke-width="1" />
  <text x="95" y="82" font-family="IBM Plex Sans, sans-serif" font-size="14" font-weight="700" fill="#10b981" letter-spacing="2">CAMPAIGN LEAFLET #{data['num']}</text>
  <text x="985" y="82" font-family="IBM Plex Sans, sans-serif" font-size="13" font-weight="600" fill="#94a3b8" text-anchor="end" letter-spacing="1">{esc(data['category'])}</text>

  <!-- Title Section -->
  <text x="70" y="150" font-family="IBM Plex Sans, sans-serif" font-size="38" font-weight="800" fill="#f8fafc">{esc(data['title'])}</text>
  <text x="70" y="188" font-family="IBM Plex Sans, sans-serif" font-size="19" font-weight="600" fill="#38bdf8">{esc(data['subtitle'])}</text>

  <!-- Arabic Box (Arabic rendered on top via Pango composite at y=285) -->
  <rect x="70" y="222" width="940" height="225" rx="16" fill="url(#cardGrad)" stroke="#10b981" stroke-width="1.8" stroke-opacity="0.4" />
  <text x="980" y="260" font-family="IBM Plex Sans, sans-serif" font-size="13" font-weight="700" fill="#10b981" text-anchor="end" letter-spacing="1.5">{esc(data['ref'])}</text>

  <!-- Translations Box -->
  <rect x="70" y="468" width="940" height="262" rx="14" fill="#0f172a" fill-opacity="0.85" stroke="#334155" stroke-width="1.5" />
  
  <!-- English -->
  <text x="100" y="504" font-family="IBM Plex Sans, sans-serif" font-size="13" font-weight="700" fill="#38bdf8" letter-spacing="1.5">ENGLISH TRANSLATION</text>
  <text x="100" y="538" font-family="IBM Plex Sans, sans-serif" font-size="20" font-weight="500" fill="#f8fafc">{esc(data['en'][0])}</text>
  <text x="100" y="568" font-family="IBM Plex Sans, sans-serif" font-size="20" font-weight="700" fill="#f43f5e">{esc(data['en'][1])}</text>
  {f'<text x="100" y="598" font-family="IBM Plex Sans, sans-serif" font-size="20" font-weight="500" fill="#f8fafc">{esc(data["en"][2])}</text>' if len(data['en']) > 2 else ''}

  <!-- Divider -->
  <line x1="100" y1="610" x2="980" y2="610" stroke="#1e293b" stroke-width="1" />

  <!-- Malay -->
  <text x="100" y="638" font-family="IBM Plex Sans, sans-serif" font-size="13" font-weight="700" fill="#10b981" letter-spacing="1.5">TERJEMAHAN BAHASA MELAYU</text>
  <text x="100" y="668" font-family="IBM Plex Sans, sans-serif" font-size="18" font-weight="400" fill="#cbd5e1">{esc(data['bm'][0])}</text>
  <text x="100" y="696" font-family="IBM Plex Sans, sans-serif" font-size="18" font-weight="700" fill="#fb7185">{esc(data['bm'][1])}</text>
  {f'<text x="100" y="722" font-family="IBM Plex Sans, sans-serif" font-size="18" font-weight="400" fill="#cbd5e1">{esc(data["bm"][2])}</text>' if len(data['bm']) > 2 else ''}

  <!-- Strategic Tech Context Box -->
  <rect x="70" y="750" width="940" height="395" rx="16" fill="#082f49" fill-opacity="0.35" stroke="#0284c7" stroke-width="1.8" />
  <rect x="70" y="750" width="940" height="44" rx="16" fill="url(#blueHeader)" />
  <text x="100" y="778" font-family="IBM Plex Sans, sans-serif" font-size="15" font-weight="800" fill="#ffffff" letter-spacing="1.5">{esc(data['why_title'])}</text>

  <!-- Point 1 -->
  <circle cx="105" cy="825" r="5" fill="#38bdf8" />
  <text x="125" y="830" font-family="IBM Plex Sans, sans-serif" font-size="18" font-weight="700" fill="#f8fafc">{esc(data['points'][0][0])}</text>
  <text x="125" y="858" font-family="IBM Plex Sans, sans-serif" font-size="16" fill="#cbd5e1">{esc(textwrap.wrap(data['points'][0][1], width=88)[0])}</text>
  <text x="125" y="883" font-family="IBM Plex Sans, sans-serif" font-size="16" fill="#cbd5e1">{esc(textwrap.wrap(data['points'][0][1], width=88)[1] if len(textwrap.wrap(data['points'][0][1], width=88)) > 1 else '')}</text>

  <!-- Point 2 -->
  <circle cx="105" cy="925" r="5" fill="#38bdf8" />
  <text x="125" y="930" font-family="IBM Plex Sans, sans-serif" font-size="18" font-weight="700" fill="#f8fafc">{esc(data['points'][1][0])}</text>
  <text x="125" y="958" font-family="IBM Plex Sans, sans-serif" font-size="16" fill="#cbd5e1">{esc(textwrap.wrap(data['points'][1][1], width=88)[0])}</text>
  <text x="125" y="983" font-family="IBM Plex Sans, sans-serif" font-size="16" fill="#cbd5e1">{esc(textwrap.wrap(data['points'][1][1], width=88)[1] if len(textwrap.wrap(data['points'][1][1], width=88)) > 1 else '')}</text>

  <!-- Directive Banner -->
  <rect x="95" y="1030" width="890" height="92" rx="12" fill="#064e3b" stroke="#10b981" stroke-width="1.5" />
  <text x="120" y="1060" font-family="IBM Plex Sans, sans-serif" font-size="14" font-weight="800" fill="#34d399" letter-spacing="1">{esc(data['directive_label'])}</text>
  <text x="120" y="1094" font-family="IBM Plex Sans, sans-serif" font-size="18" font-weight="600" fill="#ffffff">{esc(data['directive'])}</text>

  <!-- Footer -->
  <line x1="70" y1="1170" x2="1010" y2="1170" stroke="#334155" stroke-width="1" />
  <text x="70" y="1210" font-family="IBM Plex Sans, sans-serif" font-size="16" font-weight="800" fill="#f8fafc" letter-spacing="1">MALAYSIA OPEN-SOURCE &amp; TECH BOYCOTT COALITION</text>
  <text x="70" y="1238" font-family="IBM Plex Sans, sans-serif" font-size="14" fill="#94a3b8">Digital Sovereignty • Ethical Computing • Islamic Accountability</text>
  
  <rect x="770" y="1190" width="240" height="42" rx="8" fill="url(#emeraldGrad)" />
  <text x="890" y="1217" font-family="IBM Plex Sans, sans-serif" font-size="14" font-weight="800" fill="#ffffff" text-anchor="middle" letter-spacing="1">DOWNLOAD &amp; SHARE</text>
  
  <text x="70" y="1290" font-family="IBM Plex Mono, monospace" font-size="13" fill="#64748b">http://localhost:9191 • campaign/posters/{data['id']}.png</text>
</svg>"""

# -----------------------------------------------------------------------------
# CREATIVE POSTER 11: MALAYSIA DIGITAL SOVEREIGNTY
# -----------------------------------------------------------------------------
def build_poster_11_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1350" viewBox="0 0 1080 1350">
  <defs>
    <linearGradient id="bg11" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050b14" />
      <stop offset="50%" stop-color="#0a192f" />
      <stop offset="100%" stop-color="#022c22" />
    </linearGradient>
    <linearGradient id="redGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#450a0a" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#1f0707" stop-opacity="0.8" />
    </linearGradient>
    <linearGradient id="greenGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#064e3b" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#022c22" stop-opacity="0.8" />
    </linearGradient>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#d97706" />
      <stop offset="100%" stop-color="#fbbf24" />
    </linearGradient>
  </defs>

  <rect width="1080" height="1350" fill="url(#bg11)" />

  <!-- Top Header -->
  <rect x="70" y="55" width="940" height="42" rx="8" fill="#1e293b" fill-opacity="0.7" stroke="#334155" stroke-width="1" />
  <text x="95" y="82" font-family="IBM Plex Sans, sans-serif" font-size="14" font-weight="700" fill="#fbbf24" letter-spacing="2">CAMPAIGN LEAFLET #11</text>
  <text x="985" y="82" font-family="IBM Plex Sans, sans-serif" font-size="13" font-weight="600" fill="#94a3b8" text-anchor="end" letter-spacing="1">NATIONAL SOVEREIGNTY • AWAN MALAYSIA</text>

  <!-- Title Section -->
  <text x="70" y="150" font-family="IBM Plex Sans, sans-serif" font-size="44" font-weight="800" fill="#f8fafc">MERDEKAKAN AWAN KITA!</text>
  <text x="70" y="190" font-family="IBM Plex Sans, sans-serif" font-size="21" font-weight="600" fill="#38bdf8">Malaysian Digital Sovereignty: Escaping the US CLOUD Act</text>

  <!-- Subtitle Summary Box -->
  <rect x="70" y="225" width="940" height="90" rx="12" fill="#0f172a" fill-opacity="0.9" stroke="#334155" stroke-width="1.5" />
  <text x="95" y="260" font-family="IBM Plex Sans, sans-serif" font-size="17" fill="#e2e8f0">Hosting Malaysian government and corporate records with American Big Tech (AWS, GCP, Azure)</text>
  <text x="95" y="290" font-family="IBM Plex Sans, sans-serif" font-size="17" font-weight="700" fill="#f43f5e">exposes sovereign Malaysian data to foreign extraterritorial subpoenas without local court warrants.</text>

  <!-- Side-by-Side Comparison: US CLOUD Act vs Sovereign Malaysia -->
  <!-- LEFT: The Risk (US CLOUD Act) -->
  <rect x="70" y="340" width="455" height="440" rx="14" fill="url(#redGrad)" stroke="#ef4444" stroke-width="1.5" />
  <rect x="70" y="340" width="455" height="42" rx="14" fill="#7f1d1d" />
  <text x="95" y="367" font-family="IBM Plex Sans, sans-serif" font-size="15" font-weight="800" fill="#fee2e2" letter-spacing="1">THE RISK: US CLOUD ACT (2018)</text>

  <circle cx="95" cy="415" r="4" fill="#f87171" />
  <text x="115" y="420" font-family="IBM Plex Sans, sans-serif" font-size="16" font-weight="700" fill="#fecaca">Extraterritorial Jurisdiction:</text>
  <text x="115" y="445" font-family="IBM Plex Sans, sans-serif" font-size="15" fill="#cbd5e1">US law compels American tech firms to</text>
  <text x="115" y="468" font-family="IBM Plex Sans, sans-serif" font-size="15" fill="#cbd5e1">surrender data stored anywhere globally.</text>

  <circle cx="95" cy="510" r="4" fill="#f87171" />
  <text x="115" y="515" font-family="IBM Plex Sans, sans-serif" font-size="16" font-weight="700" fill="#fecaca">Bypasses Malaysian Courts:</text>
  <text x="115" y="540" font-family="IBM Plex Sans, sans-serif" font-size="15" fill="#cbd5e1">No Malaysian judicial warrant or notice</text>
  <text x="115" y="563" font-family="IBM Plex Sans, sans-serif" font-size="15" fill="#cbd5e1">is required before data is seized.</text>

  <circle cx="95" cy="605" r="4" fill="#f87171" />
  <text x="115" y="610" font-family="IBM Plex Sans, sans-serif" font-size="16" font-weight="700" fill="#fecaca">Strategic Hostage Risk:</text>
  <text x="115" y="635" font-family="IBM Plex Sans, sans-serif" font-size="15" fill="#cbd5e1">Sanctions or unilateral policy changes</text>
  <text x="115" y="658" font-family="IBM Plex Sans, sans-serif" font-size="15" fill="#cbd5e1">can lock Malaysia out of its own systems.</text>

  <circle cx="95" cy="700" r="4" fill="#f87171" />
  <text x="115" y="705" font-family="IBM Plex Sans, sans-serif" font-size="16" font-weight="700" fill="#fecaca">Breaches PDPA 2010 Spirit:</text>
  <text x="115" y="730" font-family="IBM Plex Sans, sans-serif" font-size="15" fill="#cbd5e1">Transfers sensitive citizen data abroad.</text>

  <!-- RIGHT: The Sovereign Alternative -->
  <rect x="555" y="340" width="455" height="440" rx="14" fill="url(#greenGrad)" stroke="#10b981" stroke-width="1.5" />
  <rect x="555" y="340" width="455" height="42" rx="14" fill="#065f46" />
  <text x="580" y="367" font-family="IBM Plex Sans, sans-serif" font-size="15" font-weight="800" fill="#d1fae5" letter-spacing="1">SOVEREIGN MALAYSIAN CLOUD</text>

  <circle cx="580" cy="415" r="4" fill="#34d399" />
  <text x="600" y="420" font-family="IBM Plex Sans, sans-serif" font-size="16" font-weight="700" fill="#a7f3d0">100% On-Soil Data Residency:</text>
  <text x="600" y="445" font-family="IBM Plex Sans, sans-serif" font-size="15" fill="#cbd5e1">Hosted in Malaysian data centres</text>
  <text x="600" y="468" font-family="IBM Plex Sans, sans-serif" font-size="15" fill="#cbd5e1">(TM One, AIMS, MyKRIS, Extreme BB).</text>

  <circle cx="580" cy="510" r="4" fill="#34d399" />
  <text x="600" y="515" font-family="IBM Plex Sans, sans-serif" font-size="16" font-weight="700" fill="#a7f3d0">Subject Exclusively to Local Law:</text>
  <text x="600" y="540" font-family="IBM Plex Sans, sans-serif" font-size="15" fill="#cbd5e1">Only Malaysian courts possess subpoena</text>
  <text x="600" y="563" font-family="IBM Plex Sans, sans-serif" font-size="15" fill="#cbd5e1">power under PDPA 2010 regulations.</text>

  <circle cx="580" cy="605" r="4" fill="#34d399" />
  <text x="600" y="610" font-family="IBM Plex Sans, sans-serif" font-size="16" font-weight="700" fill="#a7f3d0">Open Infrastructure (FOSS):</text>
  <text x="600" y="635" font-family="IBM Plex Sans, sans-serif" font-size="15" fill="#cbd5e1">Built on OpenNebula, Proxmox VE, Ceph,</text>
  <text x="600" y="658" font-family="IBM Plex Sans, sans-serif" font-size="15" fill="#cbd5e1">and Debian Linux without licensing ransom.</text>

  <circle cx="580" cy="700" r="4" fill="#34d399" />
  <text x="600" y="705" font-family="IBM Plex Sans, sans-serif" font-size="16" font-weight="700" fill="#a7f3d0">Stimulates Domestic Economy:</text>
  <text x="600" y="730" font-family="IBM Plex Sans, sans-serif" font-size="15" fill="#cbd5e1">Retains billions of ringgit within Malaysia.</text>

  <!-- Strategic Roadmap for Malaysia Box -->
  <rect x="70" y="805" width="940" height="340" rx="16" fill="#0c1a30" stroke="#0284c7" stroke-width="1.8" />
  <rect x="70" y="805" width="940" height="42" rx="16" fill="#0369a1" fill-opacity="0.6" />
  <text x="95" y="832" font-family="IBM Plex Sans, sans-serif" font-size="15" font-weight="800" fill="#ffffff" letter-spacing="1.5">3-POINT SOVEREIGNTY BLUEPRINT FOR MALAYSIAN ENTERPRISES</text>

  <text x="95" y="885" font-family="IBM Plex Sans, sans-serif" font-size="18" font-weight="800" fill="#fbbf24">1. DATA CLASSIFICATION &amp; AUDIT</text>
  <text x="95" y="912" font-family="IBM Plex Sans, sans-serif" font-size="16" fill="#e2e8f0">Audit all cloud repositories. Forbid hosting Level 3 (Confidential) and Level 4 (Top Secret)</text>
  <text x="95" y="935" font-family="IBM Plex Sans, sans-serif" font-size="16" fill="#cbd5e1">government or banking data on AWS, Azure, or Google Cloud.</text>

  <text x="95" y="980" font-family="IBM Plex Sans, sans-serif" font-size="18" font-weight="800" fill="#fbbf24">2. SOVEREIGN PROCUREMENT MANDATE</text>
  <text x="95" y="1007" font-family="IBM Plex Sans, sans-serif" font-size="16" fill="#e2e8f0">Require GLICs (Khazanah, KWSP, PNB) and public ministries to prioritize Tier-3/4 Malaysian data centres</text>
  <text x="95" y="1030" font-family="IBM Plex Sans, sans-serif" font-size="16" fill="#cbd5e1">powered by open-source virtualization stacks.</text>

  <text x="95" y="1075" font-family="IBM Plex Sans, sans-serif" font-size="18" font-weight="800" fill="#fbbf24">3. COMMUNITY ENCRYPTED ARCHITECTURE</text>
  <text x="95" y="1102" font-family="IBM Plex Sans, sans-serif" font-size="16" fill="#e2e8f0">Implement zero-knowledge encryption where master keys are held exclusively within Malaysia,</text>
  <text x="95" y="1125" font-family="IBM Plex Sans, sans-serif" font-size="16" fill="#cbd5e1">rendering foreign subpoena demands mathematically impossible to fulfill.</text>

  <!-- Footer -->
  <line x1="70" y1="1170" x2="1010" y2="1170" stroke="#334155" stroke-width="1" />
  <text x="70" y="1210" font-family="IBM Plex Sans, sans-serif" font-size="16" font-weight="800" fill="#f8fafc" letter-spacing="1">MALAYSIA OPEN-SOURCE &amp; TECH BOYCOTT COALITION</text>
  <text x="70" y="1238" font-family="IBM Plex Sans, sans-serif" font-size="14" fill="#94a3b8">Digital Sovereignty • Ethical Computing • Islamic Accountability</text>
  
  <rect x="770" y="1190" width="240" height="42" rx="8" fill="url(#goldGrad)" />
  <text x="890" y="1217" font-family="IBM Plex Sans, sans-serif" font-size="14" font-weight="800" fill="#0f172a" text-anchor="middle" letter-spacing="1">DOWNLOAD &amp; SHARE</text>
  
  <text x="70" y="1290" font-family="IBM Plex Mono, monospace" font-size="13" fill="#64748b">http://localhost:9191 • campaign/posters/poster_11_creative_malaysia_sovereignty.png</text>
</svg>"""

# -----------------------------------------------------------------------------
# CREATIVE POSTER 12: EUROPE IS DITCHING AMERICAN TECH
# -----------------------------------------------------------------------------
def build_poster_12_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1350" viewBox="0 0 1080 1350">
  <defs>
    <linearGradient id="bg12" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a0e1a" />
      <stop offset="50%" stop-color="#0f1f3d" />
      <stop offset="100%" stop-color="#061b2e" />
    </linearGradient>
    <linearGradient id="euroGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1d4ed8" />
      <stop offset="100%" stop-color="#3b82f6" />
    </linearGradient>
  </defs>

  <rect width="1080" height="1350" fill="url(#bg12)" />

  <!-- Top Header -->
  <rect x="70" y="55" width="940" height="42" rx="8" fill="#1e293b" fill-opacity="0.7" stroke="#334155" stroke-width="1" />
  <text x="95" y="82" font-family="IBM Plex Sans, sans-serif" font-size="14" font-weight="700" fill="#38bdf8" letter-spacing="2">CAMPAIGN LEAFLET #12</text>
  <text x="985" y="82" font-family="IBM Plex Sans, sans-serif" font-size="13" font-weight="600" fill="#94a3b8" text-anchor="end" letter-spacing="1">GLOBAL RESEARCH • WIRED REPORT ANALYSIS</text>

  <!-- Title Section -->
  <text x="70" y="145" font-family="IBM Plex Sans, sans-serif" font-size="40" font-weight="800" fill="#f8fafc">EUROPE IS DITCHING US BIG TECH</text>
  <text x="70" y="185" font-family="IBM Plex Sans, sans-serif" font-size="21" font-weight="600" fill="#f59e0b">"Why Are We Still Paying Monopolies That Arm Oppression?"</text>

  <!-- Wired Quote Box -->
  <rect x="70" y="220" width="940" height="110" rx="12" fill="#1e293b" fill-opacity="0.75" stroke="#f59e0b" stroke-width="1.5" />
  <text x="95" y="255" font-family="IBM Plex Sans, sans-serif" font-size="14" font-weight="800" fill="#fbbf24" letter-spacing="1.5">WIRED INVESTIGATION HEADLINE</text>
  <text x="95" y="285" font-family="IBM Plex Sans, sans-serif" font-size="20" font-weight="600" fill="#f8fafc">"All the Ways Europe Is Ditching American Technology"</text>
  <text x="95" y="312" font-family="IBM Plex Sans, sans-serif" font-size="15" fill="#94a3b8">— WIRED Magazine • European states are abandoning Microsoft, Google, &amp; AWS for sovereign FOSS.</text>

  <!-- 4 Milestone Cards (2x2 Grid) -->
  <!-- Card 1: Germany -->
  <rect x="70" y="355" width="455" height="230" rx="14" fill="#0f172a" stroke="#3b82f6" stroke-width="1.5" />
  <rect x="70" y="355" width="455" height="38" rx="14" fill="#1e3a8a" fill-opacity="0.7" />
  <text x="90" y="380" font-family="IBM Plex Sans, sans-serif" font-size="14" font-weight="800" fill="#93c5fd" letter-spacing="1">GERMANY (SCHLESWIG-HOLSTEIN)</text>
  <text x="90" y="420" font-family="IBM Plex Sans, sans-serif" font-size="20" font-weight="700" fill="#f8fafc">30,000 PCs Migrated to Linux</text>
  <text x="90" y="450" font-family="IBM Plex Sans, sans-serif" font-size="15" fill="#cbd5e1">The German state government formally dumped</text>
  <text x="90" y="475" font-family="IBM Plex Sans, sans-serif" font-size="15" fill="#cbd5e1">Microsoft Windows &amp; Office for Linux,</text>
  <text x="90" y="500" font-family="IBM Plex Sans, sans-serif" font-size="15" fill="#cbd5e1">LibreOffice, Nextcloud, and Matrix open stack.</text>
  <text x="90" y="545" font-family="IBM Plex Sans, sans-serif" font-size="14" font-weight="700" fill="#34d399">✓ 100% Free of US Licensing Fees</text>

  <!-- Card 2: France -->
  <rect x="555" y="355" width="455" height="230" rx="14" fill="#0f172a" stroke="#3b82f6" stroke-width="1.5" />
  <rect x="555" y="355" width="455" height="38" rx="14" fill="#1e3a8a" fill-opacity="0.7" />
  <text x="575" y="380" font-family="IBM Plex Sans, sans-serif" font-size="14" font-weight="800" fill="#93c5fd" letter-spacing="1">FRANCE (EDUCATION &amp; MINISTRIES)</text>
  <text x="575" y="420" font-family="IBM Plex Sans, sans-serif" font-size="20" font-weight="700" fill="#f8fafc">Banned Office 365 in Schools</text>
  <text x="575" y="450" font-family="IBM Plex Sans, sans-serif" font-size="15" fill="#cbd5e1">French Ministry of Education outlawed MS 365</text>
  <text x="575" y="475" font-family="IBM Plex Sans, sans-serif" font-size="15" fill="#cbd5e1">and Google Workspace across all schools. Built</text>
  <text x="575" y="500" font-family="IBM Plex Sans, sans-serif" font-size="15" fill="#cbd5e1">Tchap (sovereign Matrix chat) for 350k civil servants.</text>
  <text x="575" y="545" font-family="IBM Plex Sans, sans-serif" font-size="14" font-weight="700" fill="#34d399">✓ Sovereign National Chat Deployed</text>

  <!-- Card 3: Denmark -->
  <rect x="70" y="605" width="455" height="230" rx="14" fill="#0f172a" stroke="#3b82f6" stroke-width="1.5" />
  <rect x="70" y="605" width="455" height="38" rx="14" fill="#1e3a8a" fill-opacity="0.7" />
  <text x="90" y="630" font-family="IBM Plex Sans, sans-serif" font-size="14" font-weight="800" fill="#93c5fd" letter-spacing="1">DENMARK (DATATILSYNET RULING)</text>
  <text x="90" y="670" font-family="IBM Plex Sans, sans-serif" font-size="20" font-weight="700" fill="#f8fafc">Google Chromebook Ban</text>
  <text x="90" y="700" font-family="IBM Plex Sans, sans-serif" font-size="15" fill="#cbd5e1">Danish Data Protection Agency banned Google</text>
  <text x="90" y="725" font-family="IBM Plex Sans, sans-serif" font-size="15" fill="#cbd5e1">Chromebooks and Workspace in municipalities</text>
  <text x="90" y="750" font-family="IBM Plex Sans, sans-serif" font-size="15" fill="#cbd5e1">due to illegal telemetry and data transfers to US.</text>
  <text x="90" y="795" font-family="IBM Plex Sans, sans-serif" font-size="14" font-weight="700" fill="#34d399">✓ Child Privacy Protected from Ad Tech</text>

  <!-- Card 4: European Commission -->
  <rect x="555" y="605" width="455" height="230" rx="14" fill="#0f172a" stroke="#3b82f6" stroke-width="1.5" />
  <rect x="555" y="605" width="455" height="38" rx="14" fill="#1e3a8a" fill-opacity="0.7" />
  <text x="575" y="630" font-family="IBM Plex Sans, sans-serif" font-size="14" font-weight="800" fill="#93c5fd" letter-spacing="1">EUROPEAN COMMISSION (EDPS)</text>
  <text x="575" y="670" font-family="IBM Plex Sans, sans-serif" font-size="20" font-weight="700" fill="#f8fafc">Microsoft 365 Violates GDPR</text>
  <text x="575" y="700" font-family="IBM Plex Sans, sans-serif" font-size="15" fill="#cbd5e1">European Data Protection Supervisor ruled that</text>
  <text x="575" y="725" font-family="IBM Plex Sans, sans-serif" font-size="15" fill="#cbd5e1">EU Commission's use of Microsoft 365 broke</text>
  <text x="575" y="750" font-family="IBM Plex Sans, sans-serif" font-size="15" fill="#cbd5e1">privacy laws, ordering strict remedial action.</text>
  <text x="575" y="795" font-family="IBM Plex Sans, sans-serif" font-size="14" font-weight="700" fill="#34d399">✓ Legally Mandated Cloud Divestment</text>

  <!-- The Strategic Conclusion Box -->
  <rect x="70" y="855" width="940" height="290" rx="16" fill="#082f49" fill-opacity="0.4" stroke="#0284c7" stroke-width="2" />
  <rect x="70" y="855" width="940" height="42" rx="16" fill="#0369a1" fill-opacity="0.6" />
  <text x="95" y="882" font-family="IBM Plex Sans, sans-serif" font-size="15" font-weight="800" fill="#ffffff" letter-spacing="1.5">THE LESSON FOR MALAYSIA &amp; THE MUSLIM WORLD</text>

  <text x="95" y="930" font-family="IBM Plex Sans, sans-serif" font-size="22" font-weight="700" fill="#38bdf8">If Europe exits Big Tech for privacy alone,</text>
  <text x="95" y="960" font-family="IBM Plex Sans, sans-serif" font-size="22" font-weight="800" fill="#f43f5e">we have 10x the moral and strategic imperative to divest.</text>

  <circle cx="105" cy="1005" r="4" fill="#38bdf8" />
  <text x="125" y="1010" font-family="IBM Plex Sans, sans-serif" font-size="16" fill="#e2e8f0">European states are protecting civil data from commercial surveillance and antitrust abuses.</text>

  <circle cx="105" cy="1040" r="4" fill="#38bdf8" />
  <text x="125" y="1045" font-family="IBM Plex Sans, sans-serif" font-size="16" fill="#e2e8f0">Our money is directly co-funding automated AI targeting systems (Project Nimbus) killing our people.</text>

  <circle cx="105" cy="1075" r="4" fill="#38bdf8" />
  <text x="125" y="1080" font-family="IBM Plex Sans, sans-serif" font-size="16" fill="#e2e8f0">Proven European FOSS stacks (Nextcloud, Matrix, LibreOffice, Linux) are fully mature and ready.</text>

  <text x="95" y="1122" font-family="IBM Plex Sans, sans-serif" font-size="16" font-weight="700" fill="#34d399">➔ Take action: Begin your organization's European-style FOSS migration today.</text>

  <!-- Footer -->
  <line x1="70" y1="1170" x2="1010" y2="1170" stroke="#334155" stroke-width="1" />
  <text x="70" y="1210" font-family="IBM Plex Sans, sans-serif" font-size="16" font-weight="800" fill="#f8fafc" letter-spacing="1">MALAYSIA OPEN-SOURCE &amp; TECH BOYCOTT COALITION</text>
  <text x="70" y="1238" font-family="IBM Plex Sans, sans-serif" font-size="14" fill="#94a3b8">Digital Sovereignty • Ethical Computing • Islamic Accountability</text>
  
  <rect x="770" y="1190" width="240" height="42" rx="8" fill="url(#euroGrad)" />
  <text x="890" y="1217" font-family="IBM Plex Sans, sans-serif" font-size="14" font-weight="800" fill="#ffffff" text-anchor="middle" letter-spacing="1">DOWNLOAD &amp; SHARE</text>
  
  <text x="70" y="1290" font-family="IBM Plex Mono, monospace" font-size="13" fill="#64748b">http://localhost:9191 • campaign/posters/poster_12_creative_europe_exit.png</text>
</svg>"""

# -----------------------------------------------------------------------------
# CREATIVE POSTER 13: THE 6-LEVEL EXIT ROADMAP
# -----------------------------------------------------------------------------
def build_poster_13_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1350" viewBox="0 0 1080 1350">
  <defs>
    <linearGradient id="bg13" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070a13" />
      <stop offset="50%" stop-color="#0e172a" />
      <stop offset="100%" stop-color="#02201b" />
    </linearGradient>
    <linearGradient id="stepGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#059669" />
      <stop offset="100%" stop-color="#10b981" />
    </linearGradient>
  </defs>

  <rect width="1080" height="1350" fill="url(#bg13)" />

  <!-- Top Header -->
  <rect x="70" y="55" width="940" height="42" rx="8" fill="#1e293b" fill-opacity="0.7" stroke="#334155" stroke-width="1" />
  <text x="95" y="82" font-family="IBM Plex Sans, sans-serif" font-size="14" font-weight="700" fill="#10b981" letter-spacing="2">CAMPAIGN LEAFLET #13</text>
  <text x="985" y="82" font-family="IBM Plex Sans, sans-serif" font-size="13" font-weight="600" fill="#94a3b8" text-anchor="end" letter-spacing="1">MIGRATION ROADMAP • PRACTICAL EXECUTION</text>

  <!-- Title Section -->
  <text x="70" y="145" font-family="IBM Plex Sans, sans-serif" font-size="40" font-weight="800" fill="#f8fafc">THE 6-LEVEL TECH EXIT ROADMAP</text>
  <text x="70" y="185" font-family="IBM Plex Sans, sans-serif" font-size="20" font-weight="600" fill="#38bdf8">A Systematic Path from Big Tech Complicity to Total Sovereign Autonomy</text>

  <!-- 6 Horizontal Step Rows -->
  <!-- Level 1 -->
  <rect x="70" y="225" width="940" height="125" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="1.5" />
  <rect x="85" y="240" width="130" height="34" rx="6" fill="#065f46" />
  <text x="150" y="262" font-family="IBM Plex Sans, sans-serif" font-size="13" font-weight="800" fill="#a7f3d0" text-anchor="middle">LEVEL 1 • 1 DAY</text>
  <text x="235" y="264" font-family="IBM Plex Sans, sans-serif" font-size="20" font-weight="800" fill="#f8fafc">DNS, Browsing &amp; Private Search</text>
  <text x="85" y="305" font-family="IBM Plex Sans, sans-serif" font-size="16" fill="#cbd5e1">Replace Google Chrome &amp; Google Search with Brave / Firefox + SearXNG / Kagi.</text>
  <text x="85" y="330" font-family="IBM Plex Sans, sans-serif" font-size="15" font-weight="700" fill="#34d399">Deploy NextDNS or AdGuard Home to block 100% of telemetry and tracker pings.</text>

  <!-- Level 2 -->
  <rect x="70" y="365" width="940" height="125" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="1.5" />
  <rect x="85" y="380" width="130" height="34" rx="6" fill="#065f46" />
  <text x="150" y="402" font-family="IBM Plex Sans, sans-serif" font-size="13" font-weight="800" fill="#a7f3d0" text-anchor="middle">LEVEL 2 • 1 WEEK</text>
  <text x="235" y="404" font-family="IBM Plex Sans, sans-serif" font-size="20" font-weight="800" fill="#f8fafc">Communications &amp; Team Chat</text>
  <text x="85" y="445" font-family="IBM Plex Sans, sans-serif" font-size="16" fill="#cbd5e1">Migrate personal chat from WhatsApp to Signal. Replace Slack &amp; MS Teams with</text>
  <text x="85" y="470" font-family="IBM Plex Sans, sans-serif" font-size="15" font-weight="700" fill="#34d399">self-hosted Matrix / Element or Mattermost with zero US-based server logging.</text>

  <!-- Level 3 -->
  <rect x="70" y="505" width="940" height="125" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="1.5" />
  <rect x="85" y="520" width="130" height="34" rx="6" fill="#065f46" />
  <text x="150" y="542" font-family="IBM Plex Sans, sans-serif" font-size="13" font-weight="800" fill="#a7f3d0" text-anchor="middle">LEVEL 3 • 2 WEEKS</text>
  <text x="235" y="544" font-family="IBM Plex Sans, sans-serif" font-size="20" font-weight="800" fill="#f8fafc">Cloud Storage &amp; Office Collaboration</text>
  <text x="85" y="585" font-family="IBM Plex Sans, sans-serif" font-size="16" fill="#cbd5e1">Replace Google Drive / OneDrive with Nextcloud or Proton Drive.</text>
  <text x="85" y="610" font-family="IBM Plex Sans, sans-serif" font-size="15" font-weight="700" fill="#34d399">Adopt CryptPad and LibreOffice for collaborative documents with end-to-end encryption.</text>

  <!-- Level 4 -->
  <rect x="70" y="645" width="940" height="125" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="1.5" />
  <rect x="85" y="660" width="130" height="34" rx="6" fill="#065f46" />
  <text x="150" y="682" font-family="IBM Plex Sans, sans-serif" font-size="13" font-weight="800" fill="#a7f3d0" text-anchor="middle">LEVEL 4 • 1 MONTH</text>
  <text x="235" y="684" font-family="IBM Plex Sans, sans-serif" font-size="20" font-weight="800" fill="#f8fafc">Cloud Virtualization &amp; Hosting</text>
  <text x="85" y="725" font-family="IBM Plex Sans, sans-serif" font-size="16" fill="#cbd5e1">Migrate backend services from AWS / GCP / Azure to local sovereign data centres</text>
  <text x="85" y="750" font-family="IBM Plex Sans, sans-serif" font-size="15" font-weight="700" fill="#34d399">(TM One, AIMS) or independent ethical clouds (Hetzner, OVH) with Proxmox VE.</text>

  <!-- Level 5 -->
  <rect x="70" y="785" width="940" height="125" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="1.5" />
  <rect x="85" y="800" width="130" height="34" rx="6" fill="#065f46" />
  <text x="150" y="822" font-family="IBM Plex Sans, sans-serif" font-size="13" font-weight="800" fill="#a7f3d0" text-anchor="middle">LEVEL 5 • 2 MONTHS</text>
  <text x="235" y="824" font-family="IBM Plex Sans, sans-serif" font-size="20" font-weight="800" fill="#f8fafc">Artificial Intelligence &amp; Local Inference</text>
  <text x="85" y="865" font-family="IBM Plex Sans, sans-serif" font-size="16" fill="#cbd5e1">Replace proprietary OpenAI / Google Vertex APIs with local open-weight models</text>
  <text x="85" y="890" font-family="IBM Plex Sans, sans-serif" font-size="15" font-weight="700" fill="#34d399">(Ollama, DeepSeek, vLLM, Hugging Face) hosted on your own server hardware.</text>

  <!-- Level 6 -->
  <rect x="70" y="925" width="940" height="125" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="1.5" />
  <rect x="85" y="940" width="130" height="34" rx="6" fill="#065f46" />
  <text x="150" y="962" font-family="IBM Plex Sans, sans-serif" font-size="13" font-weight="800" fill="#a7f3d0" text-anchor="middle">LEVEL 6 • ONGOING</text>
  <text x="235" y="964" font-family="IBM Plex Sans, sans-serif" font-size="20" font-weight="800" fill="#f8fafc">Operating Systems &amp; Hardware Freedom</text>
  <text x="85" y="1005" font-family="IBM Plex Sans, sans-serif" font-size="16" fill="#cbd5e1">De-commission Windows &amp; macOS desktops in favor of Linux (Ubuntu, Debian, Pop!_OS).</text>
  <text x="85" y="1030" font-family="IBM Plex Sans, sans-serif" font-size="15" font-weight="700" fill="#34d399">De-Google mobile devices using GrapheneOS; achieve 100% digital autonomy.</text>

  <!-- Bottom Message -->
  <rect x="70" y="1065" width="940" height="75" rx="10" fill="#064e3b" stroke="#10b981" stroke-width="1.5" />
  <text x="100" y="1108" font-family="IBM Plex Sans, sans-serif" font-size="18" font-weight="700" fill="#ffffff">"You do not need to execute everything in one night. Begin Level 1 today, and keep progressing."</text>

  <!-- Footer -->
  <line x1="70" y1="1170" x2="1010" y2="1170" stroke="#334155" stroke-width="1" />
  <text x="70" y="1210" font-family="IBM Plex Sans, sans-serif" font-size="16" font-weight="800" fill="#f8fafc" letter-spacing="1">MALAYSIA OPEN-SOURCE &amp; TECH BOYCOTT COALITION</text>
  <text x="70" y="1238" font-family="IBM Plex Sans, sans-serif" font-size="14" fill="#94a3b8">Digital Sovereignty • Ethical Computing • Islamic Accountability</text>
  
  <rect x="770" y="1190" width="240" height="42" rx="8" fill="url(#stepGrad)" />
  <text x="890" y="1217" font-family="IBM Plex Sans, sans-serif" font-size="14" font-weight="800" fill="#ffffff" text-anchor="middle" letter-spacing="1">DOWNLOAD &amp; SHARE</text>
  
  <text x="70" y="1290" font-family="IBM Plex Mono, monospace" font-size="13" fill="#64748b">http://localhost:9191 • campaign/posters/poster_13_creative_6_level_roadmap.png</text>
</svg>"""

# -----------------------------------------------------------------------------
# CREATIVE POSTER 14: BIG TECH VS FOSS MATRIX
# -----------------------------------------------------------------------------
def build_poster_14_svg():
    rows = [
        ("Cloud Storage & Sync", "Google Drive / OneDrive", "Nextcloud / Seafile", "Sovereign file sync, E2E encryption, full self-hosting"),
        ("Team Communication", "Slack / Microsoft Teams", "Matrix / Element / Mattermost", "Federated protocols, decentralized servers, no spying"),
        ("Compute & Cloud VMs", "AWS / GCP / MS Azure", "Proxmox / OpenNebula / Hetzner", "Bare-metal performance, 60% lower cost, zero CLOUD Act"),
        ("Web & App Analytics", "Google Analytics 4", "Plausible / Umami Analytics", "Cookieless, GDPR-compliant, privacy-first analytics"),
        ("Email & Productivity", "Google Workspace / M365", "Proton Mail + CryptPad", "Zero-knowledge mailbox, real-time encrypted docs"),
        ("Code Repository & Git", "GitHub (Microsoft)", "Codeberg / Self-Hosted Forgejo", "Community-owned non-profit, zero telemetry, full control")
    ]
    
    row_svgs = []
    y = 280
    for category, bigtech, foss, desc in rows:
        row_svgs.append(f"""
  <!-- Row -->
  <rect x="70" y="{y}" width="940" height="112" rx="10" fill="#0f172a" stroke="#334155" stroke-width="1" />
  
  <!-- Category -->
  <text x="95" y="{y+26}" font-family="IBM Plex Sans, sans-serif" font-size="12" font-weight="800" fill="#38bdf8" letter-spacing="1.5">{esc(category.upper())}</text>
  
  <!-- Big Tech (Red) -->
  <rect x="95" y="{y+36}" width="345" height="40" rx="6" fill="#450a0a" stroke="#ef4444" stroke-width="1.2" />
  <text x="110" y="{y+61}" font-family="IBM Plex Sans, sans-serif" font-size="14" font-weight="700" fill="#fca5a5">{esc(bigtech)}</text>
  
  <!-- Sleek SVG Vector Arrow -->
  <path d="M 458,{y+56} L 492,{y+56} M 484,{y+48} L 492,{y+56} L 484,{y+64}" stroke="#10b981" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none" />
  
  <!-- FOSS (Green) -->
  <rect x="510" y="{y+36}" width="480" height="40" rx="6" fill="#064e3b" stroke="#10b981" stroke-width="1.2" />
  <text x="525" y="{y+61}" font-family="IBM Plex Sans, sans-serif" font-size="15" font-weight="800" fill="#86efac">{esc(foss)}</text>
  
  <text x="95" y="{y+98}" font-family="IBM Plex Sans, sans-serif" font-size="13" fill="#94a3b8">{esc(desc)}</text>
""")
        y += 125

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1350" viewBox="0 0 1080 1350">
  <defs>
    <linearGradient id="bg14" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070a13" />
      <stop offset="50%" stop-color="#0b1329" />
      <stop offset="100%" stop-color="#041d1a" />
    </linearGradient>
    <linearGradient id="emerald14" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#059669" />
      <stop offset="100%" stop-color="#10b981" />
    </linearGradient>
  </defs>

  <rect width="1080" height="1350" fill="url(#bg14)" />

  <!-- Top Header -->
  <rect x="70" y="55" width="940" height="42" rx="8" fill="#1e293b" fill-opacity="0.7" stroke="#334155" stroke-width="1" />
  <text x="95" y="82" font-family="IBM Plex Sans, sans-serif" font-size="14" font-weight="700" fill="#10b981" letter-spacing="2">CAMPAIGN LEAFLET #14</text>
  <text x="985" y="82" font-family="IBM Plex Sans, sans-serif" font-size="13" font-weight="600" fill="#94a3b8" text-anchor="end" letter-spacing="1">REPLACEMENT MATRIX • FOSS ALTERNATIVES</text>

  <!-- Title Section -->
  <text x="70" y="145" font-family="IBM Plex Sans, sans-serif" font-size="40" font-weight="800" fill="#f8fafc">BIG TECH vs ETHICAL OPEN-SOURCE</text>
  <text x="70" y="185" font-family="IBM Plex Sans, sans-serif" font-size="20" font-weight="600" fill="#38bdf8">Direct Enterprise Replacement Cheat Sheet • 100% Sovereign &amp; Complicity-Free</text>

  <!-- Table Header Bar -->
  <rect x="70" y="225" width="940" height="40" rx="8" fill="#1e293b" />
  <text x="95" y="250" font-family="IBM Plex Sans, sans-serif" font-size="13" font-weight="800" fill="#94a3b8" letter-spacing="1">SERVICE CATEGORY</text>
  <text x="350" y="250" font-family="IBM Plex Sans, sans-serif" font-size="13" font-weight="800" fill="#f87171" letter-spacing="1">COMPLICIT BIG TECH</text>
  <text x="650" y="250" font-family="IBM Plex Sans, sans-serif" font-size="13" font-weight="800" fill="#34d399" letter-spacing="1">SOVEREIGN OPEN-SOURCE ALTERNATIVE</text>

  <!-- Rows -->
  {"".join(row_svgs)}

  <!-- Summary Callout -->
  <rect x="70" y="1040" width="940" height="95" rx="12" fill="#064e3b" stroke="#10b981" stroke-width="1.8" />
  <text x="95" y="1075" font-family="IBM Plex Sans, sans-serif" font-size="16" font-weight="800" fill="#34d399" letter-spacing="1">100% PRIVACY • 0% GENOCIDE COMPLICITY • TOTAL DATA FREEDOM</text>
  <text x="95" y="1108" font-family="IBM Plex Sans, sans-serif" font-size="17" font-weight="600" fill="#ffffff">Every alternative above is production-tested, scalable to millions of users, and free of foreign surveillance.</text>

  <!-- Footer -->
  <line x1="70" y1="1170" x2="1010" y2="1170" stroke="#334155" stroke-width="1" />
  <text x="70" y="1210" font-family="IBM Plex Sans, sans-serif" font-size="16" font-weight="800" fill="#f8fafc" letter-spacing="1">MALAYSIA OPEN-SOURCE &amp; TECH BOYCOTT COALITION</text>
  <text x="70" y="1238" font-family="IBM Plex Sans, sans-serif" font-size="14" fill="#94a3b8">Digital Sovereignty • Ethical Computing • Islamic Accountability</text>
  
  <rect x="770" y="1190" width="240" height="42" rx="8" fill="url(#emerald14)" />
  <text x="890" y="1217" font-family="IBM Plex Sans, sans-serif" font-size="14" font-weight="800" fill="#ffffff" text-anchor="middle" letter-spacing="1">DOWNLOAD &amp; SHARE</text>
  
  <text x="70" y="1290" font-family="IBM Plex Mono, monospace" font-size="13" fill="#64748b">http://localhost:9191 • campaign/posters/poster_14_creative_foss_matrix.png</text>
</svg>"""

# -----------------------------------------------------------------------------
# CREATIVE POSTER 15: ETHICS ABOVE PROFIT (FIRED TECH WORKERS)
# -----------------------------------------------------------------------------
def build_poster_15_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1350" viewBox="0 0 1080 1350">
  <defs>
    <linearGradient id="bg15" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080811" />
      <stop offset="50%" stop-color="#1a0f24" />
      <stop offset="100%" stop-color="#0a1424" />
    </linearGradient>
    <linearGradient id="roseGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#e11d48" />
      <stop offset="100%" stop-color="#f43f5e" />
    </linearGradient>
  </defs>

  <rect width="1080" height="1350" fill="url(#bg15)" />

  <!-- Top Header -->
  <rect x="70" y="55" width="940" height="42" rx="8" fill="#1e293b" fill-opacity="0.7" stroke="#334155" stroke-width="1" />
  <text x="95" y="82" font-family="IBM Plex Sans, sans-serif" font-size="14" font-weight="700" fill="#f43f5e" letter-spacing="2">CAMPAIGN LEAFLET #15</text>
  <text x="985" y="82" font-family="IBM Plex Sans, sans-serif" font-size="13" font-weight="600" fill="#94a3b8" text-anchor="end" letter-spacing="1">TECH WORKER RESISTANCE • PROJECT NIMBUS</text>

  <!-- Title Section -->
  <text x="70" y="145" font-family="IBM Plex Sans, sans-serif" font-size="40" font-weight="800" fill="#f8fafc">ETHICS ABOVE PROFIT</text>
  <text x="70" y="185" font-family="IBM Plex Sans, sans-serif" font-size="20" font-weight="600" fill="#fda4af">"We Refuse to Build Weapons of Apartheid" — Stand with Tech Workers</text>

  <!-- Hero Worker Quote Box -->
  <rect x="70" y="225" width="940" height="185" rx="16" fill="#1f142e" stroke="#e11d48" stroke-width="2" />
  <text x="100" y="265" font-family="IBM Plex Sans, sans-serif" font-size="14" font-weight="800" fill="#f43f5e" letter-spacing="2">HISTORIC STATEMENT BY WHISTLEBLOWERS</text>
  <text x="100" y="305" font-family="IBM Plex Sans, sans-serif" font-size="23" font-weight="700" fill="#ffffff">"When engineers refuse to write the code of oppression,</text>
  <text x="100" y="338" font-family="IBM Plex Sans, sans-serif" font-size="23" font-weight="700" fill="#fda4af">the surveillance machine halts. Technology must liberate,</text>
  <text x="100" y="371" font-family="IBM Plex Sans, sans-serif" font-size="23" font-weight="700" fill="#f43f5e">never slaughter."</text>
  <text x="980" y="390" font-family="IBM Plex Sans, sans-serif" font-size="14" font-weight="600" fill="#94a3b8" text-anchor="end">— Google &amp; Amazon Tech Worker Coalition</text>

  <!-- The Facts Card: Over 50+ Workers Fired -->
  <rect x="70" y="435" width="940" height="355" rx="16" fill="#0f172a" stroke="#334155" stroke-width="1.5" />
  <rect x="70" y="435" width="940" height="42" rx="16" fill="#312e81" fill-opacity="0.6" />
  <text x="95" y="462" font-family="IBM Plex Sans, sans-serif" font-size="15" font-weight="800" fill="#c7d2fe" letter-spacing="1.5">THE UNTOLD STORY OF TECH WORKER COURAGE (APRIL 2024)</text>

  <!-- Fact 1 -->
  <circle cx="95" cy="515" r="5" fill="#f43f5e" />
  <text x="115" y="520" font-family="IBM Plex Sans, sans-serif" font-size="18" font-weight="700" fill="#ffffff">50+ Google Engineers Summarily Fired:</text>
  <text x="115" y="548" font-family="IBM Plex Sans, sans-serif" font-size="16" fill="#cbd5e1">Google fired over 50 software engineers and staff who staged peaceful sit-in protests</text>
  <text x="115" y="573" font-family="IBM Plex Sans, sans-serif" font-size="16" fill="#cbd5e1">in New York and Sunnyvale demanding the cancellation of Project Nimbus.</text>

  <!-- Fact 2 -->
  <circle cx="95" cy="615" r="5" fill="#f43f5e" />
  <text x="115" y="620" font-family="IBM Plex Sans, sans-serif" font-size="18" font-weight="700" fill="#ffffff">What is Project Nimbus? ($1.2 Billion Military Contract):</text>
  <text x="115" y="648" font-family="IBM Plex Sans, sans-serif" font-size="16" fill="#cbd5e1">A joint cloud computing agreement between Google, AWS, and the Israeli military</text>
  <text x="115" y="673" font-family="IBM Plex Sans, sans-serif" font-size="16" fill="#cbd5e1">providing AI computer vision, facial tracking, and data processing for military defense.</text>

  <!-- Fact 3 -->
  <circle cx="95" cy="715" r="5" fill="#f43f5e" />
  <text x="115" y="720" font-family="IBM Plex Sans, sans-serif" font-size="18" font-weight="700" fill="#ffffff">Retaliation &amp; Blacklisting Across the Valley:</text>
  <text x="115" y="748" font-family="IBM Plex Sans, sans-serif" font-size="16" fill="#cbd5e1">Workers speaking up for Palestinian human rights face algorithmic suppression,</text>
  <text x="115" y="773" font-family="IBM Plex Sans, sans-serif" font-size="16" fill="#cbd5e1">doxxing, and career blacklisting by corporate leadership.</text>

  <!-- Call to Action Box -->
  <rect x="70" y="815" width="940" height="330" rx="16" fill="#18181b" stroke="#e11d48" stroke-width="1.8" />
  <rect x="70" y="815" width="940" height="42" rx="16" fill="#881337" />
  <text x="95" y="842" font-family="IBM Plex Sans, sans-serif" font-size="15" font-weight="800" fill="#ffe4e6" letter-spacing="1.5">HOW THE GLOBAL TECH COMMUNITY RESPONDS</text>

  <text x="95" y="890" font-family="IBM Plex Sans, sans-serif" font-size="18" font-weight="800" fill="#fb7185">1. HIRE COURAGEOUS ETHICAL TALENT</text>
  <text x="95" y="915" font-family="IBM Plex Sans, sans-serif" font-size="16" fill="#e2e8f0">Malaysian and international ethical startups are actively recruiting whistleblowers</text>
  <text x="95" y="938" font-family="IBM Plex Sans, sans-serif" font-size="16" fill="#cbd5e1">and principled developers fired from Big Tech to build sovereign open-source platforms.</text>

  <text x="95" y="980" font-family="IBM Plex Sans, sans-serif" font-size="18" font-weight="800" fill="#fb7185">2. BOYCOTT IS WORKER SOLIDARITY</text>
  <text x="95" y="1005" font-family="IBM Plex Sans, sans-serif" font-size="16" fill="#e2e8f0">When you cancel enterprise contracts with Google and AWS, you validate the courage</text>
  <text x="95" y="1028" font-family="IBM Plex Sans, sans-serif" font-size="16" fill="#cbd5e1">of the 50+ engineers who sacrificed their high-paying careers for human rights.</text>

  <text x="95" y="1070" font-family="IBM Plex Sans, sans-serif" font-size="18" font-weight="800" fill="#fb7185">3. ORGANIZE INSIDE &amp; OUTSIDE</text>
  <text x="95" y="1095" font-family="IBM Plex Sans, sans-serif" font-size="16" fill="#e2e8f0">Support movements like 'No Tech for Apartheid' and build software that serves humanity,</text>
  <text x="95" y="1118" font-family="IBM Plex Sans, sans-serif" font-size="16" fill="#cbd5e1">not autonomous military machines.</text>

  <!-- Footer -->
  <line x1="70" y1="1170" x2="1010" y2="1170" stroke="#334155" stroke-width="1" />
  <text x="70" y="1210" font-family="IBM Plex Sans, sans-serif" font-size="16" font-weight="800" fill="#f8fafc" letter-spacing="1">MALAYSIA OPEN-SOURCE &amp; TECH BOYCOTT COALITION</text>
  <text x="70" y="1238" font-family="IBM Plex Sans, sans-serif" font-size="14" fill="#94a3b8">Digital Sovereignty • Ethical Computing • Islamic Accountability</text>
  
  <rect x="770" y="1190" width="240" height="42" rx="8" fill="url(#roseGrad)" />
  <text x="890" y="1217" font-family="IBM Plex Sans, sans-serif" font-size="14" font-weight="800" fill="#ffffff" text-anchor="middle" letter-spacing="1">DOWNLOAD &amp; SHARE</text>
  
  <text x="70" y="1290" font-family="IBM Plex Mono, monospace" font-size="13" fill="#64748b">http://localhost:9191 • campaign/posters/poster_15_creative_worker_resistance.png</text>
</svg>"""

# -----------------------------------------------------------------------------
# MAIN GENERATION PIPELINE
# -----------------------------------------------------------------------------
def main():
    print(f"[*] Starting generation of 15 Campaign Posters...")
    
    # 1. Generate 10 Islamic Posters
    for i, data in enumerate(ISLAMIC_POSTERS):
        poster_id = data["id"]
        print(f"  [{i+1}/15] Generating Islamic Poster: {poster_id}...")
        
        # Build SVG base
        svg_content = build_islamic_poster_svg(data)
        base_svg = f"/tmp/{poster_id}_base.svg"
        base_png = f"/tmp/{poster_id}_base.png"
        arabic_png = f"/tmp/{poster_id}_arabic.png"
        final_png = f"{CAMPAIGN_DIR}/{poster_id}.png"
        final_jpg = f"{CAMPAIGN_DIR}/{poster_id}.jpg"
        final_svg = f"{CAMPAIGN_DIR}/{poster_id}.svg"
        
        with open(base_svg, "w") as f:
            f.write(svg_content)
            
        with open(final_svg, "w") as f:
            f.write(svg_content)
            
        # Render base PNG
        subprocess.run(["convert", base_svg, base_png], check=True)
        
        # Render Arabic text via Pango
        render_arabic_snippet(data["arabic"], arabic_png, font_size=34)
        
        # Composite Arabic text onto base PNG at North offset +285
        composite_image(base_png, arabic_png, 285, final_png)
        
        # Render high quality JPEG
        convert_to_jpeg(final_png, final_jpg)
        
        # Copy to website media directory
        subprocess.run(["cp", final_png, f"{WEBSITE_DIR}/{poster_id}.png"], check=True)
        subprocess.run(["cp", final_jpg, f"{WEBSITE_DIR}/{poster_id}.jpg"], check=True)
        subprocess.run(["cp", final_svg, f"{WEBSITE_DIR}/{poster_id}.svg"], check=True)

    # 2. Generate 5 Creative Posters
    creative_posters = [
        ("poster_11_creative_malaysia_sovereignty", build_poster_11_svg),
        ("poster_12_creative_europe_exit", build_poster_12_svg),
        ("poster_13_creative_6_level_roadmap", build_poster_13_svg),
        ("poster_14_creative_foss_matrix", build_poster_14_svg),
        ("poster_15_creative_worker_resistance", build_poster_15_svg)
    ]
    
    for i, (poster_id, builder_fn) in enumerate(creative_posters):
        idx = i + 11
        print(f"  [{idx}/15] Generating Creative Poster: {poster_id}...")
        
        svg_content = builder_fn()
        final_png = f"{CAMPAIGN_DIR}/{poster_id}.png"
        final_jpg = f"{CAMPAIGN_DIR}/{poster_id}.jpg"
        final_svg = f"{CAMPAIGN_DIR}/{poster_id}.svg"
        
        with open(final_svg, "w") as f:
            f.write(svg_content)
            
        # Convert SVG directly to PNG and JPG
        subprocess.run(["convert", final_svg, final_png], check=True)
        convert_to_jpeg(final_png, final_jpg)
        
        # Copy to website media directory
        subprocess.run(["cp", final_png, f"{WEBSITE_DIR}/{poster_id}.png"], check=True)
        subprocess.run(["cp", final_jpg, f"{WEBSITE_DIR}/{poster_id}.jpg"], check=True)
        subprocess.run(["cp", final_svg, f"{WEBSITE_DIR}/{poster_id}.svg"], check=True)

    print("\n[SUCCESS] All 15 Posters generated in SVG, PNG, and JPEG!")
    print(f"Campaign directory: {CAMPAIGN_DIR}")
    print(f"Website directory:  {WEBSITE_DIR}")

if __name__ == "__main__":
    main()
