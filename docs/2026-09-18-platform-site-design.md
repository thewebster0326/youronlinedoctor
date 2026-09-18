# Your Online Doctor — Platform Website Design

Date: 2026-09-18
Status: approved, Phase 1 in build

## Context

`www.youronlinedoctor.co.za` currently serves a single under-construction holding
page. This spec covers replacing it with the real site, built from the client's
written brief (Your Online Doctor 0922 (Pty) Ltd, founder Dr Ngoanatsomane Tony
Moukangwe).

The defining constraint from the brief: **this must not read as a private doctor's
practice site.** It is the digital front door to a healthcare platform intended to
scale to many professionals and services. Every design decision below serves that.

## Positioning

- Brand name in copy: **Your Online Doctor**. The logo lockup reads "Your Online Dr"
  and stays as-is — it is a mark, not a wordmark to be matched in body copy.
- Tagline: *Care at Your Fingertips*. Supporting: *Quality healthcare. Wherever you are.*
- Core idea to communicate above the fold: a **network**, not a person.

## Design direction

The logo is gold-on-black and reads luxury; healthcare needs to read trustworthy and
legible. Resolution: gold and black are the brand signature used as *premium
technology*, not boutique.

- Canvas `#07070A` near-black for hero and feature bands
- Gold `#E6B64C` as accent only — CTAs, rules, highlights, never large fills
- Content sections invert to warm off-white `#FAF8F5` for reading comfort
- Clinical cyan `#5FD4E4` used **only** inside the 3D/network visuals, so the
  technology reads medical-grade rather than decorative
- Type: high-contrast serif headlines (echoing the logo) over a clean grotesque body

## The 3D

Not decoration — the hero is a live Three.js **node network**: a patient node
connecting outward to professional nodes (GP, specialist, psychologist, dietitian,
physiotherapist, biokineticist), which connect onward to service nodes (pharmacy,
laboratory, diagnostics). Slow rotation, pulses travelling the connection paths.

This single object *is* the brief's section 12 ecosystem diagram, and it states
"network, not one doctor" before any copy is read. A second scroll-driven moment on
the Our Network page expands the same graph.

**3D is restricted to brand pages.** Google Ads landing pages get a light CSS/SVG
hero instead: Three.js hurts LCP, LCP hurts Quality Score, and Quality Score costs
real money per click.

All motion respects `prefers-reduced-motion` and falls back to a static gradient on
low-power devices.

## Architecture

Dependency-free Python generator (no Jinja2 — it is not installed and is not worth a
dependency here). Same template-and-data pattern as lisa-domestic-helpers, so the
20+ service and city pages in Phase 2/3 are a data edit rather than copy-paste.

```
build.py              renders every page, sitemap.xml, robots.txt
site/config.py        brand, contact, nav, services data, tracking IDs
site/layout.py        base shell: head, header, footer, GTM, JSON-LD
site/components.py    reusable section builders
site/pages.py         page definitions
static/css/site.css   design system
static/js/site.js     nav, scroll, dataLayer events
static/js/network.js  Three.js hero scene
*.html                generated output, served from repo root
```

`.cpanel.yml` extended to copy `static/` and every generated `.html`.

## Phase 1 pages

Home · Who We Are · Our Story · Our Founder · Our Network · Services hub ·
Why Your Online Doctor · Contact · Privacy Policy · Terms · Telemedicine
Disclaimer · 404

Navigation: Home, About (Our Story / Our Founder / Our Network), Services, Why Us,
Contact, plus a persistent **Consult With a Doctor** button. Floating call and
WhatsApp buttons bottom-right on mobile.

## Conversion

**There is no booking system.** "Consult With a Doctor" routes to WhatsApp with a
pre-filled message; phone is the secondary path. A real booking flow (Calendly or
custom) is a later phase and is explicitly out of scope here.

## Tracking

Google Tag Manager with a placeholder container ID, everything routed through it:
GA4, Google Ads conversions, Meta Pixel. `dataLayer` events on `whatsapp_click`,
`call_click`, `email_click`, `cta_click`, so the brief's
**AD → WEBSITE → WHATSAPP → CONSULTATION** funnel is measurable from launch.

A POPIA consent banner gates non-essential tags.

## SEO

Per-page title, description, canonical and Open Graph; generated `sitemap.xml` and
`robots.txt`; JSON-LD for `Organization`, `MedicalBusiness`, `Physician`
(Dr Moukangwe), `BreadcrumbList`, and `FAQPage` on service pages.

Phase 2 (service pages) and Phase 3 (city landing pages) are built on the same
templates once Phase 1 is live and proven.

## Compliance — flagged, not resolved

These are raised for the client's decision and are not the developer's to sign off:

- **HPCSA advertising rules.** The founder is a registered practitioner, so the site
  falls under the HPCSA's ethical rules on advertising. Specifically affected: the
  word "Affordable" as a selling point, anything reading as comparative superiority,
  and the "10,000+ consultations / 9 Provinces / Since 2024" figures, which must be
  substantiable. Built as briefed; requires Dr Moukangwe's sign-off before launch.
- **HPCSA registration number and practice number** to be displayed in the footer —
  awaiting the numbers from the client.
- **POPIA.** Any enquiry about a health matter is special-category personal
  information. Privacy policy, consent on forms and a telemedicine disclaimer are
  drafted here but need genuine legal review.
- **Founder photograph** awaited from the client. No stock photo will be used for a
  named real person.

## Out of scope

- Booking/scheduling system, payments, patient portal, EHR
- Practitioner onboarding/directory functionality (the network is described, not
  yet transactional)
- Phase 2 service pages and Phase 3 city landing pages
