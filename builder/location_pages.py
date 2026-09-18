"""Generates one landing page per location from builder/locations_content.py."""

from . import components as c
from .config import BRAND
from .icons import icon
from .locations_content import BY_SLUG, LOCATION_PAGES
from .services_content import BY_SLUG as SERVICE_BY_SLUG


def _faq_schema(loc):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in loc["faqs"]
        ],
    }


def _service_schema(loc):
    area = ("Country" if loc["place"] == "South Africa"
            else "State" if loc["place"] == "Gauteng" else "City")
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": "Online doctor consultations in {}".format(loc["place"]),
        "serviceType": "Telehealth consultation",
        "url": "{}/{}.html".format(BRAND["domain"], loc["slug"]),
        "description": loc["description"],
        "provider": {"@id": BRAND["domain"] + "/#organization"},
        "areaServed": {"@type": area, "name": loc["place"]},
        "availableChannel": {
            "@type": "ServiceChannel",
            "serviceUrl": BRAND["domain"] + "/contact.html",
            "servicePhone": BRAND["domain"],
        },
    }


def _areas_block(loc):
    chips = "".join(
        '<li><span>{}</span></li>'.format(a) for a in loc["areas"]
    )
    angle = "".join('<p class="lede">{}</p>'.format(p) for p in loc["angle"])
    return c.band(
        '<div class="split">'
        '<div class="reveal">'
        + "<h2>{}</h2>".format(loc["areas_title"])
        + '<div class="rule"></div>'
        + '<ul class="area-list">{}</ul>'.format(chips)
        + "</div>"
        '<div class="reveal">'
        + "<h2>{}</h2>".format(loc["angle_title"])
        + '<div class="rule"></div>'
        + angle
        + "</div></div>",
        tone="light",
    )


def _services_block(loc):
    cards = ""
    for slug in loc["services"]:
        s = SERVICE_BY_SLUG.get(slug)
        if not s:
            continue
        cards += (
            '<a class="card card--link reveal" href="/{slug}.html">'
            "<h3>{label}</h3><p>{lede}</p>"
            '<span class="card__more">Read more{arrow}</span></a>'
        ).format(slug=slug, label=s["nav_label"], lede=s["lede"], arrow=icon("arrow"))

    return c.band(
        c.heading("Services", "Popular with patients in ",
                  gold_tail=loc["place"], center=True)
        + '<div class="grid grid--3">{}</div>'.format(cards)
        + '<div class="btn-row center reveal" style="justify-content:center">'
          '<a class="btn btn--ghost" href="/services.html">See all services{}</a></div>'.format(
              icon("arrow"))
        ,
        tone="dark",
    )


def _nearby_block(loc):
    cards = ""
    for slug in loc["locations"]:
        o = BY_SLUG.get(slug)
        if not o:
            continue
        cards += (
            '<a class="card card--link reveal" href="/{slug}.html">'
            "<h3>{label}</h3><p>{lede}</p>"
            '<span class="card__more">Read more{arrow}</span></a>'
        ).format(slug=slug, label=o["nav_label"], lede=o["lede"], arrow=icon("arrow"))
    if not cards:
        return ""
    return c.band(
        c.heading("Elsewhere", "Also serving ", gold_tail="these areas", center=True)
        + '<div class="grid grid--3">{}</div>'.format(cards),
        tone="light2",
    )


def build(loc):
    body = "".join([
        c.page_hero(loc["eyebrow"], loc["h1"], loc["h1_tail"], loc["lede"]),
        c.prose(["<p>{}</p>".format(p) for p in loc["intro"]], tone="light"),
        _areas_block(loc),
        _services_block(loc),
        c.steps_section(),
        c.faq_section(loc["faqs"]),
        _nearby_block(loc),
        c.cta_band(
            title="Speak to a doctor from {}".format(loc["place"]),
            lede="Send a WhatsApp message and we will connect you with the right "
                 "healthcare professional for your situation.",
        ),
    ])
    return {
        "path": "{}.html".format(loc["slug"]),
        "breadcrumb": loc["nav_label"],
        "title": loc["title"],
        "description": loc["description"],
        "schema": [_service_schema(loc), _faq_schema(loc)],
        "body": body,
    }


def all_location_pages():
    return [(lambda l=l: build(l)) for l in LOCATION_PAGES]
