"""Page definitions. Each returns a dict the layout renders into a document."""

from . import components as c
from .config import BRAND, CONTACT, FOUNDER, SERVICE_GROUPS, SERVICES_DISCLAIMER
from .icons import icon
from .layout import consult_buttons, whatsapp_url

BRANDN = BRAND["name"]


# --------------------------------------------------------------------- home

def home():
    body = "".join([
        c.hero(),
        c.band(
            '<div class="split">'
            '<div class="reveal">'
            + c.heading("Who We Are",
                        "More than an ",
                        gold_tail="online consultation")
            + "<p>Your Online Doctor is a South African digital healthcare platform "
              "connecting patients with a growing network of healthcare professionals and "
              "healthcare services through one convenient digital platform.</p>"
            + "<p>The platform was founded by " + FOUNDER["name"] + " with a simple "
              "vision: to use technology to make quality healthcare more accessible, "
              "convenient and affordable.</p>"
            + '<div class="btn-row"><a class="btn btn--ghost" href="/who-we-are.html">'
              "Read more about us" + icon("arrow") + "</a></div>"
            + "</div>"
            '<div class="reveal">'
            + "<p class=\"lede\">We recognise that accessing healthcare is not always easy. "
              "Patients may live far from healthcare facilities, struggle to find convenient "
              "appointment times, have demanding work or family responsibilities, spend "
              "significant time travelling and waiting, or need healthcare outside "
              "traditional consulting hours.</p>"
            + "<p class=\"lede\">Technology creates an opportunity to remove some of those "
              "barriers.</p>"
            + "</div>"
            "</div>",
            tone="light",
        ),
        c.stats_band(),
        c.network_teaser(),
        c.services_grid(limit=4, tone="light"),
        c.reasons_grid(tone="light2"),
        c.extended_access(),
        c.ecosystem_flow(),
        c.founder_block(tone="dark"),
        c.cta_band(),
    ])
    return {
        "path": "index.html",
        "title": "Online Doctor South Africa | {}".format(BRANDN),
        "og_title": "{} - Care at Your Fingertips".format(BRANDN),
        "description": (
            "Consult a doctor online in South Africa. A growing network of healthcare "
            "professionals - consultations, prescriptions, sick notes and referrals."
        ),
        "three_d": True,
        "body": body,
    }


# -------------------------------------------------------------- who we are

def who_we_are():
    body = "".join([
        c.page_hero(
            "Who We Are",
            "More than an ", "online consultation",
            "A South African digital healthcare platform connecting patients with a growing "
            "network of healthcare professionals and healthcare services.",
        ),
        c.prose([
            "<p>Your Online Doctor is a South African digital healthcare platform "
            "connecting patients with a growing network of healthcare professionals and "
            "healthcare services through one convenient digital platform.</p>",
            "<p>The platform was founded by " + FOUNDER["name"] + " with a simple vision: "
            "to use technology to make quality healthcare more accessible, convenient and "
            "affordable.</p>",
            "<h2>The barriers we set out to remove</h2>",
            "<p>We recognise that accessing healthcare is not always easy. Patients may "
            "live far from healthcare facilities, struggle to find convenient appointment "
            "times, have demanding work or family responsibilities, spend significant time "
            "travelling and waiting, or require healthcare outside traditional consulting "
            "hours.</p>",
            "<p>Technology creates an opportunity to remove some of these barriers. Through "
            "Your Online Doctor, patients can access healthcare remotely while being "
            "connected to the appropriate healthcare professional or service for their "
            "needs.</p>",
        ], tone="light"),
        c.band(
            '<div class="split">'
            '<div class="reveal">'
            + c.heading("Our Mission", "Our ", gold_tail="mission")
            + '<p class="lede">To make quality healthcare more accessible, convenient and '
              "affordable while connecting patients with the healthcare professionals and "
              "services they need.</p>"
            + "</div>"
            '<div class="reveal">'
            + c.heading("Our Vision", "Our ", gold_tail="vision")
            + '<p class="lede">To build one of Africa&rsquo;s leading digital healthcare '
              "networks, connecting patients with a diverse network of trusted healthcare "
              "professionals and healthcare services through a single platform.</p>"
            + "</div>"
            "</div>",
            tone="dark",
        ),
        c.stats_band(),
        c.cta_band(),
    ])
    return {
        "path": "who-we-are.html",
        "breadcrumb": "Who We Are",
        "title": "Who We Are | {}".format(BRANDN),
        "description": (
            "Your Online Doctor is a South African digital healthcare platform connecting "
            "patients with a growing network of healthcare professionals and services."
        ),
        "body": body,
    }


# ---------------------------------------------------------------- our story

def our_story():
    body = "".join([
        c.page_hero(
            "Our Story",
            "From a consultation to a ", "connected platform",
            "Your Online Doctor was created around a simple question: what if accessing "
            "healthcare could be easier?",
        ),
        c.prose([
            "<p>Traditional healthcare often requires patients to travel to a "
            "doctor&rsquo;s rooms, wait for an appointment, and spend valuable time "
            "travelling and waiting.</p>",
            "<p>Your Online Doctor uses digital technology to bring healthcare closer to "
            "patients.</p>",
            "<h2>What began as a consultation</h2>",
            "<p>What began with online medical consultations is evolving into something "
            "much bigger &mdash; a connected digital healthcare network.</p>",
            "<p>The platform is designed to bring together different healthcare "
            "professionals and services so that patients can access multiple healthcare "
            "pathways through one digital platform.</p>",
            "<h2>Where it is going</h2>",
            "<p>Our long-term goal is to make the healthcare journey more connected, "
            "convenient and patient-centred.</p>",
        ], tone="light"),
        c.ecosystem_flow(),
        c.cta_band(),
    ])
    return {
        "path": "our-story.html",
        "breadcrumb": "Our Story",
        "title": "Our Story | {}".format(BRANDN),
        "description": (
            "From online medical consultations to a connected digital healthcare network - "
            "the story behind Your Online Doctor."
        ),
        "body": body,
    }


# -------------------------------------------------------------- our founder

def our_founder():
    body = "".join([
        c.page_hero(
            "Our Founder",
            "Meet ", FOUNDER["short_name"],
            FOUNDER["role"] + ", " + BRANDN + ".",
        ),
        c.founder_block(tone="light", show_heading=False),
        c.band(
            '<div class="narrow center reveal" style="margin-inline:auto">'
            + c.heading("The Vision", "Technology should ",
                        gold_tail="reach people, not replace them", center=True)
            + "<p>Your Online Doctor is being built as a network rather than a practice. "
              "The intention is that a patient entering with one healthcare need can, where "
              "clinically appropriate, be connected onward to the professionals and services "
              "their journey requires.</p>"
            + "</div>",
            tone="dark",
        ),
        c.cta_band(),
    ])
    return {
        "path": "our-founder.html",
        "breadcrumb": "Our Founder",
        "title": "{} | {}".format(FOUNDER["name"], BRANDN),
        "description": (
            "{} is the founder and clinical lead of Your Online Doctor, a South African "
            "digital healthcare platform.".format(FOUNDER["name"])
        ),
        "body": body,
    }


# ------------------------------------------------------------- our network

def our_network():
    body = "".join([
        c.page_hero(
            "Our Healthcare Network",
            "One platform. A network of ", "healthcare professionals.",
            "Your Online Doctor is designed to connect patients with a growing network of "
            "healthcare professionals across multiple disciplines.",
        ),
        c.network_teaser(show_heading=False),
        c.network_services_grid(),
        c.ecosystem_flow(),
        c.band(
            '<div class="narrow center reveal" style="margin-inline:auto">'
            + c.heading("A Growing Network", "An expanding ",
                        gold_tail="healthcare ecosystem", center=True)
            + "<p>This allows Your Online Doctor to operate as a digital healthcare "
              "ecosystem rather than simply an online doctor&rsquo;s consultation service. "
              "As the network expands, additional professionals and healthcare service "
              "providers are added to the platform.</p>"
            + '<p class="disclaimer" style="margin-inline:auto">{}</p>'.format(SERVICES_DISCLAIMER)
            + "</div>",
            tone="light",
        ),
        c.cta_band(),
    ])
    return {
        "path": "our-network.html",
        "breadcrumb": "Our Network",
        "title": "Our Healthcare Network | {}".format(BRANDN),
        "description": (
            "GPs, specialists, psychologists, dietitians, physiotherapists and "
            "biokineticists - one platform connecting patients to a growing network of "
            "healthcare professionals."
        ),
        "body": body,
    }


# ----------------------------------------------------------------- services

def services():
    faq = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": "Can I get a prescription from an online doctor in South Africa?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": ("A prescription may be issued where it is clinically "
                             "appropriate following an assessment by the doctor. It is "
                             "never guaranteed in advance of a consultation."),
                },
            },
            {
                "@type": "Question",
                "name": "Can I get a sick note or medical certificate online?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": ("A medical certificate may be issued where it is clinically "
                             "appropriate following a consultation and assessment."),
                },
            },
            {
                "@type": "Question",
                "name": "What happens if I need to see a specialist?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": ("Your Online Doctor can refer you into its network of "
                             "healthcare professionals, including medical specialists, "
                             "psychologists, dietitians, physiotherapists and "
                             "biokineticists."),
                },
            },
        ],
    }

    body = "".join([
        c.page_hero(
            "What We Offer",
            "Care across ", "many disciplines",
            "Every service is delivered by an appropriate healthcare professional through "
            "one digital platform.",
        ),
        c.services_grid(tone="light", show_heading=False),
        c.extended_access(),
        c.cta_band(
            title="Not sure which service you need?",
            lede="Send us a message and we will point you to the right healthcare "
                 "professional for your situation.",
        ),
    ])
    return {
        "path": "services.html",
        "breadcrumb": "Services",
        "title": "Online Doctor Services & Consultations | {}".format(BRANDN),
        "description": (
            "Online doctor consultations, telehealth, prescriptions, sick notes, women's "
            "and men's health, PrEP, weight management, mental health and more."
        ),
        "schema": [faq],
        "body": body,
    }


# ------------------------------------------------------------------ why us

def why_us():
    body = "".join([
        c.page_hero(
            "Why Your Online Doctor",
            "Healthcare designed ", "around you",
            "Seven reasons patients choose a connected digital platform over a single "
            "provider.",
        ),
        c.reasons_grid(tone="light", show_heading=False),
        c.stats_band(),
        c.extended_access(),
        c.cta_band(),
    ])
    return {
        "path": "why-your-online-doctor.html",
        "breadcrumb": "Why Us",
        "title": "Why Choose {} | Connected Care".format(BRANDN),
        "description": (
            "Accessible, convenient, connected and private healthcare - why patients use "
            "Your Online Doctor rather than a single healthcare provider."
        ),
        "body": body,
    }


# ----------------------------------------------------------------- contact

def contact():
    details = (
        '<div class="grid grid--3" style="margin-top:0">'
        '<article class="card reveal"><div class="card__icon">{ph_i}</div>'
        "<h3>Call us</h3><p>Speak to us directly during operating hours.</p>"
        '<p><a class="btn btn--ghost" href="tel:{tel}" data-track="call_click" '
        'data-location="contact">{phone}</a></p></article>'

        '<article class="card reveal"><div class="card__icon">{wa_i}</div>'
        "<h3>WhatsApp</h3><p>The fastest way to start a consultation.</p>"
        '<p><a class="btn btn--gold" href="{wa}" target="_blank" rel="noopener" '
        'data-track="whatsapp_click" data-location="contact">Message us</a></p></article>'

        '<article class="card reveal"><div class="card__icon">{mail_i}</div>'
        "<h3>Email</h3><p>For general enquiries and administration.</p>"
        '<p><a class="btn btn--ghost" href="mailto:{email}" data-track="email_click" '
        'data-location="contact">{email}</a></p></article>'
        "</div>"
    ).format(
        ph_i=icon("phone"), tel=CONTACT["phone_tel"], phone=CONTACT["phone_display"],
        wa_i=icon("whatsapp"), wa=whatsapp_url(),
        mail_i=icon("mail"), email=CONTACT["email"],
    )

    address = (
        '<div class="split" style="margin-top:56px">'
        '<div class="reveal">'
        + c.heading("Registered Address", "Where to ", gold_tail="find us")
        + '<p class="lede">{}</p>'.format("<br>".join(CONTACT["address_lines"]))
        + "<p>Your Online Doctor is a digital platform &mdash; consultations take place "
          "remotely. This address is our registered business address, not a walk-in "
          "clinic.</p>"
        + "</div>"
        '<div class="reveal">'
        + c.heading("Operating Notes", "Before you ", gold_tail="get in touch")
        + "<p>Please do not use this website, WhatsApp or email for emergencies. "
          "In an emergency, go to your nearest emergency department or call your local "
          "emergency services immediately.</p>"
        + "<p>Consultations are subject to clinical assessment, professional scope of "
          "practice and clinical suitability.</p>"
        + "</div></div>"
    )

    body = "".join([
        c.page_hero(
            "Contact",
            "Speak to ", "Your Online Doctor",
            "Start a WhatsApp conversation, give us a call, or send an email &mdash; and we "
            "will connect you with the right healthcare professional.",
        ),
        c.band(details + address, tone="light"),
        c.cta_band(),
    ])
    return {
        "path": "contact.html",
        "breadcrumb": "Contact",
        "title": "Contact | {} | WhatsApp, Call or Email".format(BRANDN),
        "description": (
            "Contact Your Online Doctor on WhatsApp, by phone on {} or by email to book an "
            "online consultation.".format(CONTACT["phone_display"])
        ),
        "body": body,
    }


# ------------------------------------------------------------------- legal

def _legal_page(path, breadcrumb, title, description, eyebrow, head, tail, blocks):
    body = "".join([
        c.page_hero(eyebrow, head, tail, description),
        c.prose(blocks, tone="light"),
    ])
    return {
        "path": path,
        "breadcrumb": breadcrumb,
        "title": title,
        "description": description,
        "body": body,
    }


def privacy_policy():
    return _legal_page(
        "privacy-policy.html", "Privacy Policy",
        "Privacy Policy | {}".format(BRANDN),
        "How Your Online Doctor collects, uses and protects your personal information "
        "under POPIA.",
        "Legal", "Privacy ", "Policy",
        [
            "<p><strong>This policy is a draft and requires legal review before "
            "launch.</strong></p>",
            "<h2>Who we are</h2>",
            "<p>{} (&ldquo;we&rdquo;, &ldquo;us&rdquo;) operates "
            "www.youronlinedoctor.co.za. We are the responsible party for the personal "
            "information described in this policy, as contemplated by the Protection of "
            "Personal Information Act, 2013 (POPIA).</p>".format(BRAND["legal_name"]),
            "<h2>What we collect</h2>",
            "<p>We collect the information you give us directly &mdash; your name, contact "
            "details, and whatever you choose to tell us about your healthcare needs when "
            "you contact us by WhatsApp, telephone or email. We also collect technical "
            "information automatically, such as your device type, browser, approximate "
            "location and how you moved through this website.</p>",
            "<h2>Health information</h2>",
            "<p>Information about your health is special personal information under POPIA. "
            "We process it only for the purpose of providing or arranging healthcare, only "
            "with your consent or as otherwise permitted by law, and only by people who need "
            "it to do that.</p>",
            "<h2>Why we process it</h2>",
            "<p>To respond to your enquiry, to provide or arrange a consultation, to connect "
            "you with an appropriate healthcare professional or service, to meet our legal "
            "and professional obligations, and to understand and improve how this website "
            "performs.</p>",
            "<h2>Who we share it with</h2>",
            "<p>With the healthcare professionals and healthcare service providers involved "
            "in your care, and with service providers who help us operate (for example "
            "hosting and communications providers). We do not sell your personal "
            "information.</p>",
            "<h2>Cookies and analytics</h2>",
            "<p>This website uses cookies to understand how it is used. Non-essential "
            "cookies are only set once you accept them. You can change your choice at any "
            "time by clearing this site&rsquo;s data in your browser.</p>",
            "<h2>Your rights</h2>",
            "<p>You may ask us what personal information we hold about you, ask us to "
            "correct or delete it, object to processing, or lodge a complaint with the "
            "Information Regulator of South Africa. Contact us at "
            "<a href=\"mailto:{email}\">{email}</a>.</p>".format(email=CONTACT["email"]),
            "<h2>Retention</h2>",
            "<p>We keep health records for the periods required by South African law and "
            "professional guidelines, and other information for no longer than we need "
            "it.</p>",
        ],
    )


def terms():
    return _legal_page(
        "terms.html", "Terms",
        "Terms of Use | {}".format(BRANDN),
        "The terms on which you may use the Your Online Doctor website and services.",
        "Legal", "Terms of ", "Use",
        [
            "<p><strong>These terms are a draft and require legal review before "
            "launch.</strong></p>",
            "<h2>About this website</h2>",
            "<p>This website is operated by {}. By using it you agree to these "
            "terms.</p>".format(BRAND["legal_name"]),
            "<h2>Not medical advice</h2>",
            "<p>The content on this website is general information only. It is not medical "
            "advice and is not a substitute for a consultation with a registered healthcare "
            "professional.</p>",
            "<h2>Services are subject to assessment</h2>",
            "<p>All services described on this website are subject to appropriate clinical "
            "assessment, professional scope of practice and clinical suitability. No "
            "prescription, medical certificate, referral or other outcome is guaranteed in "
            "advance of a consultation.</p>",
            "<h2>Emergencies</h2>",
            "<p>This website and our messaging channels are not monitored for emergencies. "
            "In an emergency, go to your nearest emergency department or call your local "
            "emergency services immediately.</p>",
            "<h2>Availability</h2>",
            "<p>We aim to provide convenient and extended access to healthcare, but access "
            "is subject to service availability. We do not guarantee that a healthcare "
            "professional is available at any given moment.</p>",
            "<h2>Intellectual property</h2>",
            "<p>The content, branding and design of this website belong to us and may not be "
            "reproduced without permission.</p>",
            "<h2>Changes</h2>",
            "<p>We may update these terms. The version published on this page applies.</p>",
        ],
    )


def telemedicine_disclaimer():
    return _legal_page(
        "telemedicine-disclaimer.html", "Telemedicine Disclaimer",
        "Telemedicine Disclaimer | {}".format(BRANDN),
        "The limits of remote consultations, and when you should be seen in person.",
        "Legal", "Telemedicine ", "Disclaimer",
        [
            "<p><strong>This disclaimer is a draft and requires review by the practice "
            "before launch.</strong></p>",
            "<h2>What telemedicine can and cannot do</h2>",
            "<p>A remote consultation does not include a physical examination. That places "
            "real limits on what can be assessed. The treating healthcare professional "
            "decides, in each case, whether a condition can be managed remotely or whether "
            "you need to be seen in person.</p>",
            "<h2>You may be referred for in-person care</h2>",
            "<p>If your condition cannot be appropriately assessed or managed remotely, you "
            "will be advised to attend an in-person consultation or an appropriate "
            "healthcare facility. This is a clinical decision and is made in your "
            "interest.</p>",
            "<h2>Prescriptions and certificates</h2>",
            "<p>Prescriptions, medical certificates and referrals are issued only where "
            "clinically appropriate, at the discretion of the treating healthcare "
            "professional, and in line with South African law and professional "
            "guidelines.</p>",
            "<h2>Emergencies</h2>",
            "<p>Telemedicine is not suitable for emergencies. If you are experiencing chest "
            "pain, difficulty breathing, severe bleeding, a suspected stroke, thoughts of "
            "harming yourself, or any other emergency, go to your nearest emergency "
            "department or call your local emergency services immediately.</p>",
            "<h2>Confidentiality</h2>",
            "<p>Consultations are confidential and subject to the same professional and "
            "legal obligations as an in-person consultation. Please consult from a private "
            "space where you are comfortable speaking freely.</p>",
        ],
    )


def not_found():
    body = "".join([
        c.page_hero(
            "404",
            "Page ", "not found",
            "The page you were looking for has moved or does not exist.",
        ),
        c.band(
            '<div class="narrow center reveal" style="margin-inline:auto">'
            '<div class="btn-row" style="justify-content:center">'
            '<a class="btn btn--gold" href="/">Back to home</a>'
            '<a class="btn btn--ghost" href="/services.html">See our services</a>'
            "</div></div>",
            tone="light",
        ),
    ])
    return {
        "path": "404.html",
        "title": "Page not found | {}".format(BRANDN),
        "description": "The page you were looking for has moved or does not exist.",
        "robots": "noindex, follow",
        "body": body,
    }


from .service_pages import all_service_pages  # noqa: E402

ALL_PAGES = [
    home, who_we_are, our_story, our_founder, our_network, services, why_us,
    contact, privacy_policy, terms, telemedicine_disclaimer, not_found,
] + all_service_pages()
