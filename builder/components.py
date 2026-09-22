"""Reusable section builders. Every page is assembled from these."""

from .config import (
    CONTACT, FOUNDER, NETWORK_PROFESSIONALS, NETWORK_SERVICES, REASONS,
    SERVICE_GROUPS, SERVICES_DISCLAIMER, STATS,
)
from .icons import icon
from .layout import consult_buttons, whatsapp_url


def band(inner, tone="dark", shell="shell", extra=""):
    return '<section class="band band--{tone}{extra}"><div class="{shell}">{inner}</div></section>'.format(
        tone=tone, extra=(" " + extra if extra else ""), shell=shell, inner=inner
    )


def heading(eyebrow, title, lede=None, center=False, gold_tail=None):
    """Section heading. `gold_tail` renders the final words in the gold gradient."""
    if gold_tail:
        title_html = '{}<span class="gold-text">{}</span>'.format(title, gold_tail)
    else:
        title_html = title
    parts = ['<p class="eyebrow">{}</p>'.format(eyebrow)] if eyebrow else []
    parts.append("<h2>{}</h2>".format(title_html))
    parts.append('<div class="rule"></div>')
    if lede:
        parts.append('<p class="lede">{}</p>'.format(lede))
    wrapper = '<div class="reveal{}">{}</div>'.format(" center" if center else "", "".join(parts))
    return wrapper


# ------------------------------------------------------------------- hero

def hero():
    return """<section class="hero">
  <div class="hero__fallback"></div>
  <canvas id="network-canvas" aria-hidden="true"></canvas>
  <div class="hero__veil"></div>
  <div class="shell">
    <div class="hero__copy reveal is-in">
      <h1><span>Your Doctor.</span><span>Your Phone.</span><span class="gold-text">Your Healthcare.</span></h1>
      <p class="hero__sub">Access healthcare from wherever you are.</p>
      <p class="lede">Connect with healthcare professionals through a convenient digital
      healthcare platform designed around your needs.</p>
      {cta}
      <p class="hero__support">Healthcare professionals &nbsp;&middot;&nbsp; Multiple services
      &nbsp;&middot;&nbsp; One digital platform</p>
    </div>
  </div>
  <div class="scroll-hint">Scroll</div>
</section>""".format(cta=consult_buttons())


# ------------------------------------------------------------------ stats

def stats_band():
    cells = "".join(
        '<div class="stat"><p class="stat__figure gold-text">{}</p>'
        '<p class="stat__label">{}</p></div>'.format(fig, label)
        for fig, label in STATS
    )
    return band(
        heading("Healthcare Without Borders",
                "Reaching patients ",
                gold_tail="across South Africa",
                center=True)
        + '<div class="stats reveal">{}</div>'.format(cells),
        tone="dark2",
    )


# --------------------------------------------------------------- services

def _normalise(text):
    """Strip entities so hub group titles match services_content group names."""
    return (text.replace("&rsquo;", "’").replace("&amp;", "&")
                .replace("’", "'").strip().lower())


def _service_card(group):
    from .services_content import SERVICE_PAGES

    items = "".join("<li>{}</li>".format(i) for i in group["items"])

    # Link through to any landing page belonging to this group.
    pages = [s for s in SERVICE_PAGES
             if _normalise(s["group"]) == _normalise(group["title"])]
    links = ""
    if pages:
        links = '<div class="card__links">{}</div>'.format("".join(
            '<a href="/{slug}.html">{label}</a>'.format(
                slug=s["slug"], label=s["nav_label"])
            for s in pages
        ))

    return (
        '<article class="card reveal">'
        '<div class="card__icon">{icon}</div>'
        "<h3>{title}</h3>"
        "<p>{blurb}</p>"
        '<ul class="card__list">{items}</ul>'
        "{links}"
        "</article>"
    ).format(icon=icon(group["icon"]), title=group["title"],
             blurb=group["blurb"], items=items, links=links)


def services_grid(limit=None, tone="light", show_heading=True):
    groups = SERVICE_GROUPS[:limit] if limit else SERVICE_GROUPS
    cards = "".join(_service_card(g) for g in groups)
    tail = ""
    if limit and limit < len(SERVICE_GROUPS):
        tail = (
            '<div class="btn-row center reveal" style="justify-content:center">'
            '<a class="btn btn--ghost" href="/services.html">See all services{}</a></div>'
        ).format(icon("arrow"))
    head = heading("What We Offer",
                   "Care across ",
                   gold_tail="many disciplines",
                   lede="Every service is delivered by an appropriate healthcare "
                        "professional through one digital platform.",
                   center=True) if show_heading else ""
    return band(
        head
        + '<div class="grid grid--3">{}</div>'.format(cards)
        + '<p class="disclaimer reveal" style="margin-top:34px">{}</p>'.format(SERVICES_DISCLAIMER)
        + tail,
        tone=tone,
    )


# ---------------------------------------------------------------- network

def network_teaser(show_heading=True):
    cards = "".join(
        '<article class="card reveal"><h3>{}</h3><p>{}</p></article>'.format(name, blurb)
        for name, blurb in NETWORK_PROFESSIONALS
    )
    head = heading("Our Healthcare Network",
                   "One platform. A network of ",
                   gold_tail="healthcare professionals.",
                   lede="Depending on their healthcare needs, patients may be connected "
                        "to professionals across a range of disciplines &mdash; and the "
                        "network continues to grow.",
                   center=True) if show_heading else ""
    return band(
        head + '<div class="grid grid--3">{}</div>'.format(cards),
        tone="dark",
    )


def ecosystem_flow():
    def row(label, detail, cls=""):
        return (
            '<div class="flow__row {cls} reveal"><strong>{label}</strong>'
            "<span>{detail}</span></div>"
        ).format(cls=cls, label=label, detail=detail)

    arrow = '<div class="flow__arrow" aria-hidden="true"></div>'

    return band(
        heading("The Bigger Vision",
                "How the ",
                gold_tail="ecosystem connects",
                lede="A patient can enter through one healthcare need and, where "
                     "appropriate, be connected onward as their healthcare journey develops.",
                center=True)
        + '<div class="flow">'
        + row("Patient", "Enters with a healthcare need", "flow__row--patient")
        + arrow
        + row("Your Online Doctor", "Assesses and connects to the right professional", "flow__row--hub")
        + arrow
        + row(
            "Healthcare Professionals",
            "GPs &nbsp;&middot;&nbsp; Specialists &nbsp;&middot;&nbsp; Psychologists "
            "&nbsp;&middot;&nbsp; Dietitians &nbsp;&middot;&nbsp; Physiotherapists "
            "&nbsp;&middot;&nbsp; Biokineticists",
        )
        + arrow
        + row(
            "Healthcare Services",
            "Pharmacies &nbsp;&middot;&nbsp; Laboratories &nbsp;&middot;&nbsp; "
            "Diagnostics &nbsp;&middot;&nbsp; Other healthcare services",
        )
        + "</div>",
        tone="dark2",
    )


NETWORK_SERVICE_IMAGES = {
    "Pharmacies": ("pharmacy", "Shelves in a pharmacy dispensary"),
    "Laboratories": ("laboratory", "Analysers on a laboratory bench"),
    "Diagnostic Services": ("diagnostics", "A diagnostic laboratory"),
}


def network_services_grid():
    cards = ""
    for name, blurb in NETWORK_SERVICES:
        img, alt = NETWORK_SERVICE_IMAGES.get(name, (None, ""))
        media = ""
        if img:
            media = (
                '<div class="card__media"><img src="/assets/img/{img}.webp" alt="{alt}" '
                'width="1333" height="1000" loading="lazy" decoding="async"></div>'
            ).format(img=img, alt=alt)
        cards += (
            '<article class="card card--photo reveal">{media}'
            '<div class="card__body"><h3>{name}</h3><p>{blurb}</p></div></article>'
        ).format(media=media, name=name, blurb=blurb)
    return band(
        heading("Connected Services",
                "Beyond the ",
                gold_tail="consultation",
                lede="Where appropriate, the platform can facilitate connections to the "
                     "healthcare services a patient needs next.",
                center=True)
        + '<div class="grid grid--3">{}</div>'.format(cards),
        tone="light",
    )


# ----------------------------------------------------------------- why us

def reasons_grid(tone="light", show_heading=True):
    cards = "".join(
        '<article class="card reveal"><div class="card__icon">{ic}</div>'
        "<h3>{title}</h3><p>{body}</p></article>".format(
            ic=icon(ic), title=title, body=body
        )
        for title, ic, body in REASONS
    )
    head = heading("Why Your Online Doctor",
                   "Healthcare designed ",
                   gold_tail="around you",
                   center=True) if show_heading else ""
    return band(
        head + '<div class="grid grid--3">{}</div>'.format(cards),
        tone=tone,
    )


# ------------------------------------------------------------ extended access

def extended_access():
    return band(
        '<div class="reveal narrow center" style="margin-inline:auto">'
        + heading("Extended Access",
                  "Healthcare designed around ",
                  gold_tail="your life",
                  center=True)
        + "<p>Illness does not always happen during traditional office hours. "
          "Your Online Doctor is designed to provide convenient and extended access to "
          "healthcare, allowing patients to seek medical assistance beyond traditional "
          "doctor&rsquo;s-room hours, subject to service availability and clinical "
          "suitability.</p>"
        + "</div>",
        tone="light2",
    )


# ---------------------------------------------------------------- founder

def founder_block(tone="dark", show_heading=True):
    if FOUNDER["photo"]:
        media = '<img src="{}" alt="{}" width="800" height="1000">'.format(
            FOUNDER["photo"], FOUNDER["name"]
        )
    else:
        media = (
            '<div class="portrait-placeholder">{ic}<span>Portrait of {name}<br>'
            "to be supplied</span></div>"
        ).format(ic=icon("user"), name=FOUNDER["short_name"])

    return band(
        '<div class="split">'
        '<div class="split__media reveal">{media}</div>'
        '<div class="reveal">'
        + (heading("Our Founder", FOUNDER["name"]) if show_heading
           else '<h2>{}</h2><div class="rule"></div>'.format(FOUNDER["name"]))
        + '<p class="lede">{role}</p>'.format(role=FOUNDER["role"])
        + "<p>Dr Moukangwe founded Your Online Doctor with the vision of using technology "
          "to bridge the gap between patients and healthcare professionals. His belief is "
          "that technology should not replace healthcare professionals &mdash; it should "
          "make it easier for patients to reach them.</p>"
        + "<p>Your Online Doctor is therefore being developed beyond a single-practitioner "
          "model into a broader healthcare network, where patients can connect with "
          "professionals across different disciplines.</p>"
        + '<blockquote class="quote">&ldquo;{quote}&rdquo;<cite>{name}</cite></blockquote>'.format(
            quote=FOUNDER["quote"], name=FOUNDER["name"]
        )
        + "</div></div>",
        tone=tone,
    )


# -------------------------------------------------------------- cta band

def cta_band(title="Ready to speak to a doctor?",
             lede="Start a WhatsApp conversation and we will guide you to the right "
                  "healthcare professional for your needs."):
    return (
        '<section class="cta-band"><div class="shell narrow center reveal">'
        '<h2>{title}</h2><div class="rule"></div>'
        '<p class="lede">{lede}</p>{cta}'
        "</div></section>"
    ).format(title=title, lede=lede, cta=consult_buttons())


# ---------------------------------------------------------------- page top

def page_hero(eyebrow, title, gold_tail, lede, image=None, image_alt=""):
    """Light hero for inner pages - no Three.js, keeps LCP fast.

    `image` names a file in assets/img without its extension. It loads eagerly,
    because where it is used it is the page's largest contentful paint element.
    """
    if image:
        backdrop = (
            '<img class="page-hero__img" src="/assets/img/{img}.webp" alt="{alt}" '
            'width="1500" height="843" fetchpriority="high">'
            '<div class="page-hero__veil"></div>'
        ).format(img=image, alt=image_alt)
        extra = " has-photo"
    else:
        backdrop = '<div class="hero__fallback" style="opacity:.55"></div>'
        extra = ""

    return (
        '<section class="band band--dark page-hero{extra}" '
        'style="padding-top:clamp(132px,15vw,188px)">'
        "{backdrop}"
        '<div class="shell narrow center" style="position:relative;z-index:2">'
        '<p class="eyebrow">{eyebrow}</p>'
        '<h1>{title}<span class="gold-text">{tail}</span></h1>'
        '<div class="rule"></div>'
        '<p class="lede">{lede}</p>'
        "</div></section>"
    ).format(extra=extra, backdrop=backdrop, eyebrow=eyebrow, title=title,
             tail=gold_tail, lede=lede)


def image_band(image, alt, caption=None, tone="light"):
    """Wide editorial strip. Lazy - it is never the first thing on a page."""
    cap = '<figcaption>{}</figcaption>'.format(caption) if caption else ""
    return band(
        '<figure class="strip reveal">'
        '<img src="/assets/img/{img}.webp" alt="{alt}" width="1500" height="843" '
        'loading="lazy" decoding="async">{cap}</figure>'.format(
            img=image, alt=alt, cap=cap),
        tone=tone,
    )


def media_split(image, alt, inner, tone="light", flip=False):
    """Photograph beside a block of content."""
    media = (
        '<div class="split__media split__media--wide reveal">'
        '<img src="/assets/img/{img}.webp" alt="{alt}" width="1500" height="843" '
        'loading="lazy" decoding="async"></div>'
    ).format(img=image, alt=alt)
    text = '<div class="reveal">{}</div>'.format(inner)
    order = (text + media) if flip else (media + text)
    return band('<div class="split split--media">{}</div>'.format(order), tone=tone)


# ---------------------------------------------------------------- prose

def prose(blocks, tone="light"):
    return band('<div class="narrow reveal">{}</div>'.format("".join(blocks)), tone=tone)


# ------------------------------------------------------------ service pages

def steps_section(service_label="a consultation"):
    """How it works - four steps, worded around the service in question."""
    steps = [
        ("01", "Get in touch",
         "Message us on WhatsApp, call, or send an email. Tell us briefly what you need."),
        ("02", "We arrange a time",
         "We confirm a time for {} that fits around your day.".format(service_label)),
        ("03", "The consultation",
         "The healthcare professional takes your history, assesses the concern and discusses "
         "the appropriate next step with you."),
        ("04", "What happens next",
         "A prescription, certificate, test request or referral &mdash; whichever is "
         "clinically appropriate for your situation."),
    ]
    cards = "".join(
        '<article class="card step reveal"><span class="step__num">{n}</span>'
        "<h3>{t}</h3><p>{b}</p></article>".format(n=n, t=t, b=b)
        for n, t, b in steps
    )
    return band(
        heading("How It Works", "From first message to ",
                gold_tail="next step", center=True)
        + '<div class="grid grid--2">{}</div>'.format(cards),
        tone="dark",
    )


def faq_section(faqs):
    items = "".join(
        "<details class=\"faq reveal\"><summary>{q}</summary><div class=\"faq__a\">"
        "<p>{a}</p></div></details>".format(q=q, a=a)
        for q, a in faqs
    )
    return band(
        heading("Questions", "Common ", gold_tail="questions", center=True)
        + '<div class="faqs">{}</div>'.format(items),
        tone="light",
    )


def related_services(slugs, by_slug):
    cards = ""
    for slug in slugs:
        s = by_slug.get(slug)
        if not s:
            continue
        cards += (
            '<a class="card reveal card--link" href="/{slug}.html">'
            "<h3>{label}</h3><p>{lede}</p>"
            '<span class="card__more">Read more{arrow}</span></a>'
        ).format(slug=slug, label=s["nav_label"], lede=s["lede"], arrow=icon("arrow"))
    if not cards:
        return ""
    return band(
        heading("Related", "You may also ", gold_tail="be looking for", center=True)
        + '<div class="grid grid--3">{}</div>'.format(cards),
        tone="light2",
    )


def covers_block(title, items, suitability):
    lis = "".join("<li>{}</li>".format(i) for i in items)
    return band(
        '<div class="split">'
        '<div class="reveal">'
        + "<h2>{}</h2>".format(title)
        + '<div class="rule"></div>'
        + '<ul class="card__list check-list">{}</ul>'.format(lis)
        + "</div>"
        '<div class="reveal">'
        + "<h2>Good to know</h2>"
        + '<div class="rule"></div>'
        + '<p class="lede">{}</p>'.format(suitability)
        + '<p class="disclaimer">{}</p>'.format(SERVICES_DISCLAIMER)
        + "</div></div>",
        tone="light",
    )
