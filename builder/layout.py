"""The page shell: head, header, footer, tracking and structured data."""

import json

from .config import BRAND, CONTACT, FOUNDER, NAV, TRACKING
from .icons import icon

ASSET_VERSION = "1"


# ----------------------------------------------------------------- helpers

def whatsapp_url():
    from urllib.parse import quote
    return "https://wa.me/{}?text={}".format(
        CONTACT["whatsapp"], quote(CONTACT["whatsapp_message"])
    )


def consult_buttons(dark=True, primary_label="Consult With a Doctor"):
    """Primary WhatsApp CTA plus a call fallback. Both fire dataLayer events."""
    ghost = "btn--ghost"
    return (
        '<div class="btn-row">'
        '<a class="btn btn--gold" href="{wa}" target="_blank" rel="noopener" '
        'data-track="whatsapp_click" data-location="cta">{wa_icon}{label}</a>'
        '<a class="btn {ghost}" href="tel:{tel}" data-track="call_click" '
        'data-location="cta">{ph_icon}{phone}</a>'
        "</div>"
    ).format(
        wa=whatsapp_url(),
        wa_icon=icon("whatsapp"),
        label=primary_label,
        ghost=ghost,
        tel=CONTACT["phone_tel"],
        ph_icon=icon("phone"),
        phone=CONTACT["phone_display"],
    )


# -------------------------------------------------------------- structured

def _organization_schema():
    node = {
        "@context": "https://schema.org",
        "@type": "MedicalBusiness",
        "@id": BRAND["domain"] + "/#organization",
        "name": BRAND["name"],
        "legalName": BRAND["legal_name"],
        "url": BRAND["domain"] + "/",
        "logo": BRAND["domain"] + "/assets/logo.png",
        "image": BRAND["domain"] + "/assets/logo.png",
        "description": (
            "South African digital healthcare platform connecting patients with a "
            "growing network of healthcare professionals and healthcare services."
        ),
        "telephone": CONTACT["phone_tel"],
        "email": CONTACT["email"],
        "foundingDate": BRAND["founded"],
        "areaServed": {"@type": "Country", "name": "South Africa"},
        "address": {
            "@type": "PostalAddress",
            "streetAddress": CONTACT["address_lines"][0],
            "addressLocality": CONTACT["address_locality"],
            "addressRegion": CONTACT["address_region"],
            "postalCode": CONTACT["address_postal"],
            "addressCountry": CONTACT["country"],
        },
        "founder": _physician_schema(),
        "medicalSpecialty": [
            "PrimaryCare", "PublicHealth", "Psychiatric", "Dietetics", "Physiotherapy",
        ],
    }
    return node


def _physician_schema():
    node = {
        "@type": "Physician",
        "@id": BRAND["domain"] + "/our-founder.html#founder",
        "name": FOUNDER["name"],
        "jobTitle": FOUNDER["role"],
        "worksFor": {"@id": BRAND["domain"] + "/#organization"},
    }
    if FOUNDER["hpcsa_number"]:
        node["identifier"] = {
            "@type": "PropertyValue",
            "name": "HPCSA registration number",
            "value": FOUNDER["hpcsa_number"],
        }
    return node


def _breadcrumbs(page):
    trail = [{"name": "Home", "url": BRAND["domain"] + "/"}]
    if page.get("breadcrumb"):
        trail.append({
            "name": page["breadcrumb"],
            "url": BRAND["domain"] + "/" + page["path"],
        })
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": i + 1,
                "name": item["name"],
                "item": item["url"],
            }
            for i, item in enumerate(trail)
        ],
    }


def _schema_blocks(page):
    blocks = []
    if page["path"] == "index.html":
        blocks.append({
            "@context": "https://schema.org",
            "@type": "WebSite",
            "@id": BRAND["domain"] + "/#website",
            "url": BRAND["domain"] + "/",
            "name": BRAND["name"],
            "publisher": {"@id": BRAND["domain"] + "/#organization"},
        })
        blocks.append(_organization_schema())
    if page.get("breadcrumb"):
        blocks.append(_breadcrumbs(page))
    blocks.extend(page.get("schema", []))
    return "\n".join(
        '<script type="application/ld+json">{}</script>'.format(
            json.dumps(b, ensure_ascii=False, separators=(",", ":"))
        )
        for b in blocks
    )


# ------------------------------------------------------------------ chrome

def _nav_markup(current_path):
    out = []
    for item in NAV:
        href = item["href"]
        active = ""
        if href.endswith(current_path) or (current_path == "index.html" and href == "/"):
            active = ' aria-current="page"'
        if item.get("children"):
            kids = "".join(
                '<li><a href="{}">{}</a></li>'.format(c["href"], c["label"])
                for c in item["children"]
            )
            child_active = any(c["href"].endswith(current_path) for c in item["children"])
            out.append(
                '<li class="has-sub"><a href="{href}"{aria}>{label}</a>'
                '<ul class="sub">{kids}</ul></li>'.format(
                    href=href,
                    aria=' aria-current="page"' if child_active else "",
                    label=item["label"],
                    kids=kids,
                )
            )
        else:
            out.append(
                '<li><a href="{}"{}>{}</a></li>'.format(href, active, item["label"])
            )
    return "".join(out)


def _header(current_path):
    return (
        '<header class="site-header" id="site-header">'
        '<div class="shell site-header__inner">'
        '<a class="brand-link" href="/" aria-label="{name} home">'
        '<img src="/assets/logo.png" alt="{name}" width="592" height="227">'
        "</a>"
        '<button class="nav-toggle" id="nav-toggle" aria-expanded="false" '
        'aria-controls="site-nav" aria-label="Open menu">{menu}</button>'
        '<nav class="site-nav" id="site-nav"><ul>{nav}</ul></nav>'
        '<div class="header-cta">'
        '<a class="btn btn--gold" href="{wa}" target="_blank" rel="noopener" '
        'data-track="whatsapp_click" data-location="header">Consult Now</a>'
        "</div>"
        "</div></header>"
    ).format(
        name=BRAND["name"],
        menu=icon("menu"),
        nav=_nav_markup(current_path),
        wa=whatsapp_url(),
    )


def _footer():
    reg_bits = []
    if FOUNDER["hpcsa_number"]:
        reg_bits.append("HPCSA " + FOUNDER["hpcsa_number"])
    if FOUNDER["practice_number"]:
        reg_bits.append("Practice no. " + FOUNDER["practice_number"])
    registration = (
        '<p class="disclaimer">{}</p>'.format(" &nbsp;|&nbsp; ".join(reg_bits))
        if reg_bits else ""
    )

    return (
        '<footer class="site-footer"><div class="shell">'
        '<div class="footer-grid">'

        '<div class="footer-brand">'
        '<img src="/assets/logo.png" alt="{name}" width="592" height="227">'
        "<p>{supporting}</p>"
        "</div>"

        "<div><h4>Explore</h4><ul>"
        '<li><a href="/who-we-are.html">Who We Are</a></li>'
        '<li><a href="/our-story.html">Our Story</a></li>'
        '<li><a href="/our-founder.html">Our Founder</a></li>'
        '<li><a href="/our-network.html">Our Network</a></li>'
        "</ul></div>"

        "<div><h4>Care</h4><ul>"
        '<li><a href="/services.html">Services</a></li>'
        '<li><a href="/why-your-online-doctor.html">Why Us</a></li>'
        '<li><a href="/contact.html">Contact</a></li>'
        "</ul></div>"

        "<div><h4>Contact</h4><ul>"
        '<li><a href="tel:{tel}" data-track="call_click" data-location="footer">{phone}</a></li>'
        '<li><a href="{wa}" target="_blank" rel="noopener" data-track="whatsapp_click" '
        'data-location="footer">WhatsApp</a></li>'
        '<li><a href="mailto:{email}" data-track="email_click" data-location="footer">{email}</a></li>'
        "<li>{addr}</li>"
        "</ul></div>"

        "</div>"

        '<p class="disclaimer">The information on this website is for general '
        "information and does not constitute medical advice. It is not a substitute for "
        "a consultation with a registered healthcare professional. All services are "
        "subject to clinical assessment, professional scope of practice and clinical "
        "suitability. In an emergency, go to your nearest emergency department or call "
        "your local emergency services immediately.</p>"
        "{registration}"

        '<div class="footer-legal">'
        "<span>&copy; {year} {legal}. All rights reserved.</span>"
        "<span>"
        '<a href="/privacy-policy.html">Privacy Policy</a> &nbsp;&middot;&nbsp; '
        '<a href="/terms.html">Terms</a> &nbsp;&middot;&nbsp; '
        '<a href="/telemedicine-disclaimer.html">Telemedicine Disclaimer</a>'
        "</span>"
        "</div>"

        "</div></footer>"
    ).format(
        name=BRAND["name"],
        supporting=BRAND["supporting"],
        tel=CONTACT["phone_tel"],
        phone=CONTACT["phone_display"],
        wa=whatsapp_url(),
        email=CONTACT["email"],
        addr="<br>".join(CONTACT["address_lines"]),
        registration=registration,
        year=2026,
        legal=BRAND["legal_name"],
    )


def _floating_actions():
    return (
        '<div class="fab">'
        '<a class="fab__wa" href="{wa}" target="_blank" rel="noopener" '
        'aria-label="Chat on WhatsApp" data-track="whatsapp_click" data-location="fab">{wa_i}</a>'
        '<a class="fab__call" href="tel:{tel}" aria-label="Call {phone}" '
        'data-track="call_click" data-location="fab">{ph_i}</a>'
        "</div>"
    ).format(
        wa=whatsapp_url(), wa_i=icon("whatsapp"),
        tel=CONTACT["phone_tel"], ph_i=icon("phone"), phone=CONTACT["phone_display"],
    )


def _consent_bar():
    return (
        '<div class="consent-bar" id="consent-bar" role="dialog" aria-live="polite" '
        'aria-label="Cookie consent">'
        "<p>We use cookies to understand how this site is used and to improve it. "
        'See our <a href="/privacy-policy.html">Privacy Policy</a>.</p>'
        '<button class="btn btn--ghost" data-consent="reject" type="button">Essential only</button>'
        '<button class="btn btn--gold" data-consent="accept" type="button">Accept</button>'
        "</div>"
    )


# ------------------------------------------------------------------ tagging

def _gtm_head():
    if not TRACKING["enabled"]:
        return (
            "<!-- Google Tag Manager is scaffolded but disabled. Set a real container "
            "ID and TRACKING['enabled'] = True in builder/config.py to switch it on. -->"
        )
    return (
        "<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':"
        "new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],"
        "j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src="
        "'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);"
        "})(window,document,'script','dataLayer','%s');</script>" % TRACKING["gtm_container"]
    )


def _gtm_body():
    if not TRACKING["enabled"]:
        return ""
    return (
        '<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=%s" '
        'height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>'
        % TRACKING["gtm_container"]
    )


# -------------------------------------------------------------------- page

def render(page):
    """Render a full HTML document from a page dict."""
    url = BRAND["domain"] + "/" + ("" if page["path"] == "index.html" else page["path"])
    body_class = page.get("body_class", "")
    scripts = ""
    if page.get("three_d"):
        scripts = (
            '<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js" '
            'defer></script>\n'
            '<script src="/static/js/network.js?v={v}" defer></script>'.format(v=ASSET_VERSION)
        )

    return """<!DOCTYPE html>
<html lang="en-ZA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{url}">
<meta name="robots" content="{robots}">
<meta name="theme-color" content="#07070a">

<meta property="og:type" content="website">
<meta property="og:site_name" content="{brand}">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{domain}/assets/logo.png">
<meta property="og:locale" content="en_ZA">
<meta name="twitter:card" content="summary_large_image">

<link rel="icon" href="/assets/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="/assets/favicon.png">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Marcellus&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/static/css/site.css?v={v}">

{gtm_head}
{schema}
</head>
<body class="{body_class}">
{gtm_body}
{header}
<main id="main">
{body}
</main>
{footer}
{fab}
{consent}
<script src="/static/js/site.js?v={v}" defer></script>
{scripts}
</body>
</html>
""".format(
        title=page["title"],
        description=page["description"],
        og_title=page.get("og_title", page["title"]),
        url=url,
        domain=BRAND["domain"],
        brand=BRAND["name"],
        robots=page.get("robots", "index, follow"),
        v=ASSET_VERSION,
        gtm_head=_gtm_head(),
        gtm_body=_gtm_body(),
        schema=_schema_blocks(page),
        body_class=body_class,
        header=_header(page["path"]),
        body=page["body"],
        footer=_footer(),
        fab=_floating_actions(),
        consent=_consent_bar(),
        scripts=scripts,
    )
