"""Global site data. Everything the client is likely to change lives here."""

# ---------------------------------------------------------------- brand

BRAND = {
    "name": "Your Online Doctor",
    "legal_name": "Your Online Doctor 0922 (Pty) Ltd",
    "tagline": "Care at Your Fingertips",
    "supporting": "Quality healthcare. Wherever you are.",
    "domain": "https://www.youronlinedoctor.co.za",
    "founded": "2024",
}

FOUNDER = {
    "name": "Dr Ngoanatsomane Tony Moukangwe",
    "short_name": "Dr Moukangwe",
    "role": "Founder & Clinical Lead",
    # TODO(client): HPCSA registration number and practice number
    "hpcsa_number": None,
    "practice_number": None,
    # TODO(client): a real photograph. No stock photo for a named person.
    "photo": None,
    "quote": (
        "Healthcare should be accessible wherever you are, and technology gives us "
        "the opportunity to connect patients with the right healthcare professional "
        "when they need care."
    ),
}

CONTACT = {
    "phone_display": "064 519 1021",
    "phone_tel": "+27645191021",
    "whatsapp": "27645191021",
    "whatsapp_message": "Hi Your Online Doctor, I would like to book a consultation.",
    "email": "info@youronlinedoctor.co.za",
    "address_lines": [
        "G16 Barclays Square Shopping Centre",
        "Pretoria, 0001",
    ],
    "address_locality": "Pretoria",
    "address_region": "Gauteng",
    "address_postal": "0001",
    "country": "ZA",
}

# ------------------------------------------------------------- tracking
# Placeholders. Swap the GTM container ID and every downstream tag
# (GA4, Google Ads, Meta Pixel) lights up without touching a template.

TRACKING = {
    "gtm_container": "GTM-XXXXXXX",
    "enabled": False,  # flip to True once a real container ID is in place
}

# ------------------------------------------------------------ navigation

NAV = [
    {"label": "Home", "href": "/"},
    {
        "label": "About",
        "href": "/who-we-are.html",
        "children": [
            {"label": "Who We Are", "href": "/who-we-are.html"},
            {"label": "Our Story", "href": "/our-story.html"},
            {"label": "Our Founder", "href": "/our-founder.html"},
            {"label": "Our Network", "href": "/our-network.html"},
        ],
    },
    {
        "label": "Services",
        "href": "/services.html",
        "wide": True,
        "children": None,  # filled from services_content at import time, below
    },
    {
        "label": "Locations",
        "href": "/online-doctor-johannesburg.html",
        "children": None,  # filled from locations_content at import time, below
    },
    {"label": "Why Us", "href": "/why-your-online-doctor.html"},
    {"label": "Contact", "href": "/contact.html"},
]

# -------------------------------------------------------------- services
# Phase 2 gives each group its own landing page; `slug` is reserved now so
# links and the sitemap will not have to be rewritten later.

SERVICE_GROUPS = [
    {
        "slug": "medical",
        "title": "Medical",
        "icon": "stethoscope",
        "blurb": "Everyday medical care, assessed and managed remotely by a doctor.",
        "items": [
            "Online Doctor Consultations",
            "Telehealth",
            "Medical Assessments",
            "Prescriptions, where clinically appropriate",
            "Medical Certificates and Sick Notes, where appropriate",
            "Specialist Referrals",
            "Laboratory Test Requests",
        ],
    },
    {
        "slug": "womens-health",
        "title": "Women&rsquo;s Health",
        "icon": "womens",
        "blurb": "Confidential consultations covering contraception and sexual health.",
        "items": [
            "Contraception",
            "Women&rsquo;s Health Consultations",
            "Sexual Health",
        ],
    },
    {
        "slug": "mens-health",
        "title": "Men&rsquo;s Health",
        "icon": "mens",
        "blurb": "Discreet consultations for the concerns men most often delay raising.",
        "items": [
            "Men&rsquo;s Health Consultations",
            "Sexual Health",
            "Erectile dysfunction-related consultations",
        ],
    },
    {
        "slug": "sexual-reproductive-health",
        "title": "Sexual &amp; Reproductive Health",
        "icon": "shield",
        "blurb": "Private consultations for STIs, HIV prevention and contraception.",
        "items": [
            "STI Consultations",
            "HIV Prevention and PrEP",
            "Contraception",
        ],
    },
    {
        "slug": "weight-wellness",
        "title": "Weight &amp; Wellness",
        "icon": "pulse",
        "blurb": "Clinically guided weight management and lifestyle support.",
        "items": [
            "Weight Management",
            "Lifestyle and Wellness",
            "Body Composition Assessments",
            "Nutritional support",
        ],
    },
    {
        "slug": "mental-health",
        "title": "Mental Health",
        "icon": "mind",
        "blurb": "Consultations and referral into psychology services.",
        "items": [
            "Mental Health Consultations",
            "Psychology services and referrals",
        ],
    },
    {
        "slug": "other-services",
        "title": "Other Services",
        "icon": "plus",
        "blurb": "Further services available through the platform and its network.",
        "items": [
            "Acne and dermatology-related consultations",
            "Hair Loss Consultations",
            "Chronic Disease Support",
            "Driver and PDP Medical Assessments",
            "Mobile Doctor Services",
        ],
    },
]

SERVICES_DISCLAIMER = (
    "All services are subject to appropriate clinical assessment, professional scope "
    "of practice and clinical suitability."
)

# --------------------------------------------------------------- network

NETWORK_PROFESSIONALS = [
    ("General Practitioners",
     "Everyday medical care, and the usual first point of contact."),
    ("Medical Specialists",
     "Referral into specialist disciplines where a case calls for it."),
    ("Psychologists",
     "Mental health assessment and talking therapies."),
    ("Dietitians",
     "Nutritional assessment and eating plans."),
    ("Physiotherapists",
     "Movement, rehabilitation and pain management."),
    ("Biokineticists",
     "Exercise-based rehabilitation and conditioning."),
    ("Allied Healthcare Professionals",
     "Further disciplines as the network continues to grow."),
]

NETWORK_SERVICES = [
    ("Pharmacies", "Dispensing, where a prescription is clinically appropriate."),
    ("Laboratories", "Pathology and testing against a doctor&rsquo;s request."),
    ("Diagnostic Services", "Imaging and diagnostics where indicated."),
]

# ----------------------------------------------------------------- stats
# Client-supplied figures. These are advertising claims under the HPCSA
# ethical rules and must be substantiable. See docs/2026-09-18-platform-site-design.md

STATS = [
    ("10,000+", "Online consultations"),
    ("9 Provinces", "Patients reached across South Africa"),
    ("Since 2024", "Providing digital healthcare"),
    ("Growing Network", "Professionals across multiple disciplines"),
]

# ---------------------------------------------------------------- why us

REASONS = [
    ("Accessible", "signal",
     "Access healthcare remotely, without unnecessarily travelling to a healthcare facility."),
    ("Convenient", "clock",
     "Connect with healthcare professionals from home, from work, or from wherever you are."),
    ("Affordable", "wallet",
     "We aim to provide accessible healthcare options while maintaining professional standards."),
    ("Connected", "network",
     "Reach a growing network of healthcare professionals rather than a single provider."),
    ("Private", "lock",
     "Consult from the privacy of your own environment."),
    ("Digital First", "device",
     "A healthcare experience designed around how people actually communicate today."),
    ("Patient Centred", "heart",
     "A healthcare journey built to be simpler, more connected and more convenient."),
]


# The Services dropdown lists every service landing page. Populated here rather
# than by hand so adding a service to services_content.py is the only edit.
from .services_content import SERVICE_PAGES as _SERVICE_PAGES  # noqa: E402

from .locations_content import LOCATION_PAGES as _LOCATION_PAGES  # noqa: E402

for _item in NAV:
    if _item["label"] == "Locations":
        _item["children"] = [
            {"label": _l["nav_label"], "href": "/{}.html".format(_l["slug"])}
            for _l in _LOCATION_PAGES
        ]
    if _item["label"] == "Services":
        _item["children"] = (
            [{"label": "All Services", "href": "/services.html"}]
            + [
                {"label": _s["nav_label"], "href": "/{}.html".format(_s["slug"])}
                for _s in _SERVICE_PAGES
            ]
        )
