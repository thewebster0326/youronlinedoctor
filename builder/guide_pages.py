"""Renders guide pages from builder/guides_content.py.

Also the template the blog will use, so it stays generic: hero, intro,
sections, a checklist, FAQs and two sets of internal links.
"""

from . import components as c
from .config import BRAND
from .guides_content import BY_SLUG, GUIDE_PAGES
from .icons import icon
from .services_content import BY_SLUG as SERVICE_BY_SLUG


def _faq_schema(guide):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in guide["faqs"]
        ],
    }


def _article_schema(guide):
    return {
        "@context": "https://schema.org",
        "@type": "MedicalWebPage",
        "name": guide["nav_label"],
        "headline": guide["title"],
        "url": "{}/{}.html".format(BRAND["domain"], guide["slug"]),
        "description": guide["description"],
        "provider": {"@id": BRAND["domain"] + "/#organization"},
        "publisher": {"@id": BRAND["domain"] + "/#organization"},
        "audience": {"@type": "Patient"},
        "lastReviewed": "2026-11-06",
    }


def _sections(guide):
    out = ""
    for sec in guide["sections"]:
        body = "".join("<p>{}</p>".format(p) for p in sec.get("p", []))
        if sec.get("list"):
            body += '<ul class="card__list check-list">{}</ul>'.format(
                "".join("<li>{}</li>".format(i) for i in sec["list"]))
        out += "<h2>{}</h2>{}".format(sec["h"], body)
    return c.band('<div class="narrow reveal prose-body">{}</div>'.format(out),
                  tone="light")


def _checklist(guide):
    items = "".join("<li>{}</li>".format(i) for i in guide["checklist"])
    return c.band(
        '<div class="split">'
        '<div class="reveal">'
        + "<h2>{}</h2>".format(guide["checklist_title"])
        + '<div class="rule"></div>'
        + '<ul class="card__list check-list">{}</ul>'.format(items)
        + "</div>"
        '<div class="reveal">'
        + "<h2>Arranging it</h2>"
        + '<div class="rule"></div>'
        + '<p class="lede">Send a WhatsApp message with your area and we will confirm '
          "a time and a place. Where mobile doctor services cover your location, the "
          "assessment can be arranged where you are.</p>"
        + '<p class="disclaimer">Application steps, fees and how recent a certificate '
          "must be are set by the licensing authorities and can change. Confirm the "
          "current requirements with your Driving Licence Testing Centre.</p>"
        + "</div></div>",
        tone="light2",
    )


def _related(guide):
    cards = ""
    for slug in guide["related_guides"]:
        g = BY_SLUG.get(slug)
        if g:
            cards += (
                '<a class="card card--link reveal" href="/{slug}.html">'
                "<h3>{label}</h3><p>{lede}</p>"
                '<span class="card__more">Read more{arrow}</span></a>'
            ).format(slug=slug, label=g["nav_label"], lede=g["lede"], arrow=icon("arrow"))
    for slug in guide["related_services"]:
        s = SERVICE_BY_SLUG.get(slug)
        if s:
            cards += (
                '<a class="card card--link reveal" href="/{slug}.html">'
                "<h3>{label}</h3><p>{lede}</p>"
                '<span class="card__more">Read more{arrow}</span></a>'
            ).format(slug=slug, label=s["nav_label"], lede=s["lede"], arrow=icon("arrow"))
    if not cards:
        return ""
    return c.band(
        c.heading("Related", "More on ", gold_tail="driver medicals", center=True)
        + '<div class="grid grid--3">{}</div>'.format(cards),
        tone="dark",
    )


def build(guide):
    body = "".join([
        c.page_hero(guide["eyebrow"], guide["h1"], guide["h1_tail"], guide["lede"],
                    image=guide["image"], image_alt=guide["image_alt"]),
        c.media_split(
            guide["image"], guide["image_alt"],
            "".join("<p>{}</p>".format(p) for p in guide["intro"]),
            tone="light", flip=True,
        ),
        _sections(guide),
        _checklist(guide),
        c.faq_section(guide["faqs"]),
        _related(guide),
        c.cta_band(
            title="Arrange a driver medical",
            lede="Send a WhatsApp message with your area and we will confirm a time "
                 "and a place.",
        ),
    ])
    return {
        "path": "{}.html".format(guide["slug"]),
        "breadcrumb": guide["nav_label"],
        "title": guide["title"],
        "description": guide["description"],
        "schema": [_article_schema(guide), _faq_schema(guide)],
        "body": body,
    }


def all_guide_pages():
    return [(lambda g=g: build(g)) for g in GUIDE_PAGES]
