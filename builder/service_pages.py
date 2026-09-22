"""Generates one landing page per service from builder/services_content.py."""

from . import components as c
from .config import BRAND
from .services_content import BY_SLUG, SERVICE_PAGES

BRANDN = BRAND["name"]


def _faq_schema(service):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in service["faqs"]
        ],
    }


def _service_schema(service):
    return {
        "@context": "https://schema.org",
        "@type": "MedicalWebPage",
        "name": service["nav_label"],
        "url": "{}/{}.html".format(BRAND["domain"], service["slug"]),
        "description": service["description"],
        "about": {"@type": "MedicalEntity", "name": service["nav_label"]},
        "provider": {"@id": BRAND["domain"] + "/#organization"},
        "audience": {"@type": "Patient"},
        "lastReviewed": "2026-09-18",
    }


def build(service):
    body = "".join([
        c.page_hero(
            service["eyebrow"],
            service["h1"],
            service["h1_tail"],
            service["lede"],
        ),
        c.media_split(
            service["image"], service["image_alt"],
            "".join("<p>{}</p>".format(p) for p in service["intro"]),
            tone="light",
        ),
        c.covers_block(service["covers_title"], service["covers"], service["suitability"]),
        c.steps_section(),
        c.faq_section(service["faqs"]),
        c.related_services(service["related"], BY_SLUG),
        c.cta_band(
            title="Speak to someone about {}".format(service["nav_label"].lower()),
            lede="Send a WhatsApp message and we will connect you with the right "
                 "healthcare professional for your situation.",
        ),
    ])
    return {
        "path": "{}.html".format(service["slug"]),
        "breadcrumb": service["nav_label"],
        "title": service["title"],
        "description": service["description"],
        "schema": [_service_schema(service), _faq_schema(service)],
        "body": body,
    }


def all_service_pages():
    """Page factories, one per service, for build.py."""
    return [(lambda s=s: build(s)) for s in SERVICE_PAGES]
