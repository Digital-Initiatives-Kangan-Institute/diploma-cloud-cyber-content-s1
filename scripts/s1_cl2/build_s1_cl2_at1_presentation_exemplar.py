#!/usr/bin/env python3
"""Build the AT1 Part C design-approval presentation EXEMPLAR (.pptx) — assessor model.

A worked model of the AT1 Part C presentation: the student (as MTS Consultant) walks the
YAT ICT Manager through the Solution Design (Part A) and the Disaster Recovery Plan (Part B)
and seeks approval to implement. This is the design-approval gate — it evidences ICTCLD501
element 5 (PC 5.1 verbal walkthrough, 5.2 feedback, 5.3 lodgement, 5.4 sign-off) and FS Oral
communication.

The verbal contextual knowledge-evidence Q&A happens at the end of this presentation, but the
assessor's KE *questions* live in the AT1 assessment task / instrument (not in this deck); the
closing slide is simply where that Q&A takes place.

Pure to the cluster's division of concerns: the design (web-scale + microservice) is presented
as the Solution Design; recovery is presented as the DR Plan; data residency appears only as an
input the design answers — DR stays onshore and separate from compliance. The website is a
public, anonymous-traffic site, so the web-scale story includes edge security (WAF / Shield /
bot rules) and discoverability, not only latency.

Reuses the shared pptx brand helpers (pptx_brand).

Usage:  python scripts/build_at1_presentation_exemplar.py [output.pptx]
Default: S1-CL2-Cloud-Disaster-Recovery/assessments/AT1/AT1-exemplar-presentation.pptx
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import pptx_brand as b  # noqa: E402


def build(path):
    prs = b.new_deck()

    b.add_title_slide(
        prs, "Design & Disaster Recovery Plan", "YAT Website Global Expansion",
        ["MTS Consulting", "Design approval — presented to YAT ICT Management"])

    b.add_content_slide(prs, "Agenda", [
        ("Why now — the India expansion", 0),
        ("What we're designing", 0),
        ("Web-scale design — serving a global public audience", 0),
        ("The audit-log microservice", 0),
        ("Disaster recovery — risks and objectives", 0),
        ("Disaster recovery — the recovery plan", 0),
        ("What stays onshore", 0),
        ("Cost and proportionality", 0),
        ("The decision we're asking for", 0),
    ])

    b.add_content_slide(prs, "Why now — the India expansion", [
        ("YAT's GIFT City partnership makes the public website the global enrolment front-door — a partner institution's intake now depends on it.", 0),
        ("That means the website must now: serve a global, anonymous public audience, survive the loss of a whole region, and be provisioned as code.", 0),
        ("Today's design is single-region high availability — right for the Australian audience, not for this.", 0),
        ("So this engagement delivers two things: a Solution Design for the changes, and a Disaster Recovery Plan.", 0),
    ])

    b.add_content_slide(prs, "What we're designing", [
        ("Solution Design (Part A) — scale the website for a global public audience, plus an audit-log microservice.", 0),
        ("Disaster Recovery Plan (Part B) — recover the website if the primary region is lost.", 0),
        ("Recovery objectives: RTO ≤ 4 hours, RPO ≤ 1 hour.", 1),
        ("This is the design. Approval today is the gate to building it in Phase 2.", 0),
    ])

    b.add_content_slide(prs, "Web-scale design — serving a global public audience", [
        ("CloudFront edge delivery + Route 53 latency routing — anonymous India visitors served from the nearest edge, not Sydney; fast and search-discoverable.", 0),
        ("ElastiCache caches sessions and hot reads, absorbing a larger, spikier public load off the database.", 0),
        ("The existing multi-AZ load balancer, Auto Scaling and database are retained; scaling policies retuned.", 0),
        ("Public exposure handled at the edge — WAF for web exploits, Shield + rate / bot rules for scraping and DDoS, origin locked to CloudFront, TLS throughout.", 0),
    ])

    b.add_content_slide(prs, "The audit-log microservice", [
        ("A small serverless service: webhook → API Gateway → SQS → Lambda → DynamoDB, hosted in the India region.", 0),
        ("Its one job: record India-cohort access events, and keep those logs in India (the residency requirement).", 0),
        ("Loosely coupled — the website only calls a webhook; the service can change independently behind it.", 0),
        ("The contract is generic — any event producer that meets it can reuse the same service; only the payload differs.", 0),
    ])

    b.add_statement_slide(
        prs, "The design in one line",
        "Serve globally at the edge; keep the India logs in India; leave the core data in Sydney.",
        "The simplest change that meets the requirements — no data replication, no over-provisioning.")

    b.add_content_slide(prs, "Disaster recovery — risks and objectives", [
        ("Three major risk events: loss of the primary region, destructive data loss, and a cyber-security compromise.", 0),
        ("RPO ≤ 1 hour — a disaster loses at most the last hour of data.", 0),
        ("RTO ≤ 4 hours — the website is back in service within four hours of an incident being declared.", 0),
        ("The existing HA design already covers component / Availability-Zone failure; this plan covers losing the whole region.", 0),
    ])

    b.add_content_slide(prs, "Disaster recovery — the recovery plan", [
        ("Strategy: back up and restore into a second Australian region (Melbourne).", 0),
        ("An hourly cross-region snapshot copy meets the RPO; the infrastructure-as-code templates rebuild the stack to meet the RTO.", 0),
        ("The runbook: detect → declare → rebuild from code → restore the database → verify → cut CDN / DNS over → confirm.", 0),
        ("A tabletop run of the region-loss scenario confirmed the steps complete inside the four-hour window.", 0),
    ])

    b.add_content_slide(prs, "What stays onshore", [
        ("Recovery is into a second Australian region — the website's Australian-held data never leaves the country, even during a disaster.", 0),
        ("Data residency for the India access logs is handled in the design (the microservice), not in the DR plan.", 0),
        ("Disaster recovery and regulatory residency are kept separate — each stays simple and does one job.", 0),
    ])

    b.add_content_slide(prs, "Cost and proportionality", [
        ("Backup-and-restore is the lowest-cost DR tier that still meets 4 hours / 1 hour — no idle standby to pay for.", 0),
        ("Edge delivery and caching scale on demand; the microservice scales to zero when idle.", 0),
        ("No replication of the main database into another region, and no over-provisioned capacity.", 0),
    ])

    b.add_statement_slide(
        prs, "The decision we're asking for",
        "Approve the Solution Design and the Disaster Recovery Plan, so we can build.",
        "Approved → lodged and registered for change management → Phase 2 implementation (the Deployment Report).")

    b.add_closing_slide(prs, "Questions", "MTS Consulting  ·  YAT Website Global Expansion")

    Path(path).parent.mkdir(parents=True, exist_ok=True)
    prs.save(path)
    print(f"Wrote {path} ({len(prs.slides)} slides)")


if __name__ == "__main__":
    default = "S1-CL2-Cloud-Disaster-Recovery/assessments/AT1/AT1-exemplar-presentation.pptx"
    out = sys.argv[1] if len(sys.argv) > 1 else default
    build(out)
