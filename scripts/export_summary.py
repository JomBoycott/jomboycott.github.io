#!/usr/bin/env python3
"""
Statistical Summary Generator
Malaysian Open-Source Tech Accountability Campaign
"""

import os
import json
from collections import Counter

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def main():
    evid_path = os.path.join(ROOT_DIR, "evidence/evidence.json")
    alt_path = os.path.join(ROOT_DIR, "alternatives/alternatives.json")

    with open(evid_path, "r", encoding="utf-8") as f:
        evidence = json.load(f)

    with open(alt_path, "r", encoding="utf-8") as f:
        alternatives = json.load(f)

    print("=" * 60)
    print("📊 MALAYSIAN TECH ACCOUNTABILITY CAMPAIGN STATS")
    print("=" * 60)

    print(f"\n📁 Total Documented Evidence Claims: {len(evidence)}")
    comp_counter = Counter(item["company"] for item in evidence)
    for comp, count in comp_counter.most_common():
        print(f"  • {comp:<24}: {count} claims")

    status_counter = Counter(item["status"] for item in evidence)
    print("\n🔍 Claim Status Breakdown:")
    for stat, count in status_counter.most_common():
        print(f"  • {stat:<24}: {count} records")

    tier_counter = Counter(item["source_tier"] for item in evidence)
    print("\n📑 Source Tier Distribution:")
    for tier, count in tier_counter.most_common():
        print(f"  • {tier:<24}: {count} citations")

    print(f"\n💡 Total Open-Source Alternative Stacks: {len(alternatives)}")
    cat_counter = Counter(item["category"] for item in alternatives)
    for cat, count in cat_counter.most_common():
        print(f"  • {cat:<26}: {count} projects")

    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
