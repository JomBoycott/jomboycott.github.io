#!/usr/bin/env python3
"""
Automated Test & Validation Suite
Malaysian Open-Source Tech Accountability Campaign
"""

import os
import sys
import json
import re

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

ALLOWED_STATUSES = {
    "VERIFIED",
    "STRONGLY_SUPPORTED",
    "REPORTED",
    "DISPUTED",
    "UNVERIFIED",
    "FALSE",
    "OUTDATED"
}

ALLOWED_COMPANIES = {
    "Google",
    "Amazon",
    "Microsoft",
    "Meta",
    "General/Cross-Platform"
}

def validate_json_file(rel_path):
    full_path = os.path.join(ROOT_DIR, rel_path)
    if not os.path.exists(full_path):
        raise FileNotFoundError(f"Missing required file: {rel_path}")
    with open(full_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            print(f"✅ [JSON Valid] {rel_path}")
            return data
        except json.JSONDecodeError as e:
            raise ValueError(f"JSON syntax error in {rel_path}: {e}")

def validate_evidence(evidence_data):
    print("🔍 Validating evidence records...")
    ids = set()
    for idx, record in enumerate(evidence_data):
        rec_id = record.get("id")
        if not rec_id or rec_id in ids:
            raise ValueError(f"Record #{idx} has invalid or duplicate ID: {rec_id}")
        ids.add(rec_id)

        company = record.get("company")
        if company not in ALLOWED_COMPANIES:
            raise ValueError(f"Record {rec_id} has invalid company: {company}")

        status = record.get("status")
        if status not in ALLOWED_STATUSES:
            raise ValueError(f"Record {rec_id} has invalid status '{status}'. Must be one of {ALLOWED_STATUSES}")

        # Check required fields
        required_fields = [
            "topic", "claim", "source_tier", "source_type",
            "source_title", "source_url", "publication_date",
            "quote_or_evidence", "counterclaim_or_nuance", "last_verified"
        ]
        for field in required_fields:
            if not record.get(field):
                raise ValueError(f"Record {rec_id} missing non-empty field: {field}")

        # Date format check
        if not re.match(r"^\d{4}(-\d{2}(-\d{2})?)?$", record["publication_date"]):
            raise ValueError(f"Record {rec_id} invalid publication_date: {record['publication_date']}")
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", record["last_verified"]):
            raise ValueError(f"Record {rec_id} invalid last_verified: {record['last_verified']}")

    print(f"✅ [Evidence Records Valid] {len(evidence_data)} claims verified across {len(ids)} unique IDs.")

def validate_alternatives(alternatives_data):
    print("🔍 Validating open-source alternatives directory...")
    ids = set()
    categories = set()
    for idx, alt in enumerate(alternatives_data):
        alt_id = alt.get("id")
        if not alt_id or alt_id in ids:
            raise ValueError(f"Alternative #{idx} has invalid or duplicate ID: {alt_id}")
        ids.add(alt_id)

        required_fields = [
            "project", "category", "replaces", "license", "website",
            "github", "self_hosting_requirements", "difficulty",
            "cost_model", "privacy_rating", "maturity",
            "malaysian_suitability_summary"
        ]
        for field in required_fields:
            if not alt.get(field):
                raise ValueError(f"Alternative {alt_id} missing non-empty field: {field}")

        if not isinstance(alt["replaces"], list) or len(alt["replaces"]) == 0:
            raise ValueError(f"Alternative {alt_id} 'replaces' must be a non-empty array of strings")

        categories.add(alt["category"])

    print(f"✅ [Alternatives Valid] {len(alternatives_data)} tools verified across {len(categories)} categories.")

def validate_pamphlet_word_counts():
    print("🔍 Validating pamphlet word counts (must be <= 500 words)...")
    pamphlets = [
        ("campaign/pamphlets/pamphlet_bm.md", 500),
        ("campaign/pamphlets/pamphlet_en.md", 500)
    ]
    for rel_path, max_words in pamphlets:
        full_path = os.path.join(ROOT_DIR, rel_path)
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()
        word_count = len(content.split())
        if word_count > max_words:
            raise ValueError(f"Pamphlet {rel_path} exceeds word limit: {word_count} > {max_words}")
        print(f"✅ [Pamphlet Word Count OK] {rel_path}: {word_count} words (Limit: {max_words})")

def validate_required_files():
    print("🔍 Checking required file paths...")
    expected_files = [
        "README.md",
        "LICENSE",
        "todo.md",
        "CAMPAIGN_MASTER_REPORT.md",
        "islamic-foundation/quran.md",
        "islamic-foundation/hadith.md",
        "islamic-foundation/tafsir.md",
        "islamic-foundation/ethics.md",
        "research/google/dossier.md",
        "research/amazon/dossier.md",
        "research/microsoft/dossier.md",
        "research/meta/dossier.md",
        "research/malaysia/dossier.md",
        "research/malaysia/openinfra_sovereign_cloud_proposal.md",
        "research/israel-palestine/tech_context.md",
        "research/global-precedents/europe_ditching_big_tech.md",
        "evidence/schema.json",
        "evidence/evidence.json",
        "alternatives/schema.json",
        "alternatives/alternatives.json",
        "alternatives/directory.md",
        "alternatives/migration_guide.md",
        "campaign/branding.md",
        "campaign/audiences.md",
        "campaign/pamphlets/pamphlet_bm.md",
        "campaign/pamphlets/pamphlet_en.md",
        "campaign/leaflets/leaflet_bm.md",
        "campaign/leaflets/leaflet_en.md",
        "campaign/factsheets/google_factsheet.md",
        "campaign/factsheets/amazon_factsheet.md",
        "campaign/factsheets/microsoft_factsheet.md",
        "campaign/factsheets/meta_factsheet.md",
        "campaign/factsheets/europe_precedents_factsheet.md",
        "campaign/social/10_slide_carousel_bm.md",
        "campaign/social/10_slide_carousel_en.md",
        "campaign/infographics/infographic_series.md",
        "sources/bibliography.md",
        "website/index.html",
        "website/about.html",
        "website/evidence.html",
        "website/companies.html",
        "website/alternatives.html",
        "website/migrate.html",
        "website/islam.html",
        "website/malaysia.html",
        "website/research.html",
        "website/sources.html",
        "website/faq.html",
        "website/styles.css",
        "website/app.js"
    ]

    missing = []
    for f in expected_files:
        if not os.path.exists(os.path.join(ROOT_DIR, f)):
            missing.append(f)

    if missing:
        raise FileNotFoundError(f"Missing required project files: {missing}")

    print(f"✅ [All Files Present] All {len(expected_files)} essential files exist in repository.")

def main():
    print("=" * 60)
    print("🚀 RUNNING AUTOMATED VALIDATION SUITE")
    print("=" * 60)

    validate_required_files()
    evidence_data = validate_json_file("evidence/evidence.json")
    validate_evidence(evidence_data)
    alternatives_data = validate_json_file("alternatives/alternatives.json")
    validate_alternatives(alternatives_data)
    validate_pamphlet_word_counts()

    print("=" * 60)
    print("🎉 ALL VALIDATION TESTS PASSED SUCCESSFULLY!")
    print("=" * 60)

if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(f"\n❌ VALIDATION FAILED: {err}", file=sys.stderr)
        sys.exit(1)
