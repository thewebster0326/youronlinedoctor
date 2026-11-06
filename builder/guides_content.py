"""Guide and supporting-landing-page content.

This is the template the blog will also use. Each entry renders as a full page
with an intro, structured sections, FAQs and internal links.

The PDP cluster is the first use. Search Console showed driver-pdp-medicals
sitting at position 9.1 with the whole query cluster at 9-11, so these three
pages exist to push that cluster onto page one.

Accuracy rule applied throughout: these pages describe the MEDICAL EXAMINATION,
which is the practice's own service. Application steps, fees and validity
periods are set by the authorities and change, so the copy points readers at
their DLTC rather than stating figures that could go stale or be wrong.
"""

GUIDE_PAGES = [
    # ---------------------------------------------------------- Pretoria
    {
        "slug": "pdp-medical-pretoria",
        "nav_label": "PDP Medical Pretoria",
        "cluster": "pdp",
        "image": "driving",
        "image_alt": "A driver at the wheel of a commercial vehicle",
        "eyebrow": "PDP Medical Pretoria",
        "h1": "PDP medicals in ",
        "h1_tail": "Pretoria",
        "title": "PDP Medical Pretoria | Driver Medical | Your Online Doctor",
        "description": "PDP and driver medical assessments for professional drivers in "
                       "Pretoria and Tshwane, by a registered medical practitioner.",
        "lede": "The medical assessment you need before a Driving Licence Testing Centre "
                "will process your Professional Driving Permit.",
        "intro": [
            "A Professional Driving Permit is what allows you to drive for a living rather "
            "than only for yourself, and a medical assessment is part of getting one. The "
            "Driving Licence Testing Centre will not process the application without a "
            "certificate from a registered medical practitioner confirming you are "
            "medically fit to drive professionally.",
            "Pretoria has a large professional driving population. Freight moving through "
            "the N1 and N4 corridors, minibus taxi and bus operators across Tshwane, "
            "delivery and e-hailing drivers, and the many fleets attached to government "
            "departments and the industrial areas around Silverton and Rosslyn. For most of "
            "those drivers the medical is an errand that costs a working morning.",
            "That is the part worth fixing. The examination itself is short. It is the "
            "waiting, and the trip to find somewhere that does them, that takes the day.",
        ],
        "sections": [
            {
                "h": "Who needs a PDP medical",
                "p": ["A Professional Driving Permit is required for drivers who carry "
                      "goods or passengers professionally, and for drivers of dangerous "
                      "goods. The permit falls into categories covering goods, passengers "
                      "and dangerous goods, and the medical assessment applies across them."],
                "list": [
                    "Truck and freight drivers",
                    "Minibus taxi, bus and shuttle drivers",
                    "E-hailing and metered taxi drivers",
                    "Delivery and courier drivers",
                    "Drivers of dangerous or hazardous goods",
                    "Fleet drivers whose employer requires a current permit",
                ],
            },
            {
                "h": "This one has to happen in person",
                "p": ["Most of what Your Online Doctor does is remote. A driver medical is "
                      "the exception, and it has to be: it includes a vision check, a "
                      "hearing check and a physical examination, none of which can be done "
                      "over a video call.",
                      "What the platform does is take the arranging out of it. Message us "
                      "and we will confirm a time and a location rather than you phoning "
                      "around. Where mobile doctor services cover your area, the assessment "
                      "can be arranged where you are."],
            },
            {
                "h": "Where you apply",
                "p": ["The medical certificate is one document in a larger application. The "
                      "application itself is made at a Driving Licence Testing Centre, and "
                      "Tshwane has several, including Centurion, Waltloo and Akasia.",
                      "Requirements, fees and how recent your medical certificate has to be "
                      "are set by the authorities and do change, so confirm the current "
                      "position with your DLTC before you go. What we can tell you with "
                      "certainty is what happens at the medical."],
            },
        ],
        "checklist_title": "What to bring to the assessment",
        "checklist": [
            "Your identity document",
            "Your current driving licence",
            "Glasses or contact lenses, if you use them",
            "A list of any medication you take regularly",
            "Details of any chronic condition you are being treated for",
            "Hearing aids, if you use them",
        ],
        "faqs": [
            ("Can a PDP medical be done online?",
             "No. It includes vision and hearing checks and a physical examination, so it "
             "has to be done in person. The arrangements can be made through the platform."),
            ("Where in Pretoria can I have it done?",
             "Message us with your area and we will confirm where and when. Where mobile "
             "doctor services cover your location, it can be arranged where you are."),
            ("How long does the assessment take?",
             "The examination itself is usually short. Allow time for the paperwork to be "
             "completed properly, because an incomplete certificate gets rejected at the "
             "DLTC."),
            ("What if I wear glasses?",
             "Bring them. Vision is assessed with the correction you normally drive in, so "
             "turning up without your glasses makes the result meaningless."),
            ("What happens if I do not meet a criterion?",
             "The doctor will explain which standard was not met and what, if anything, "
             "could change it. Some findings are temporary and reversible; some are not. "
             "The certificate cannot be issued where the standard is not met."),
        ],
        "related_guides": ["pdp-medical-what-to-expect", "code-10-code-14-driver-medical"],
        "related_services": ["driver-pdp-medicals", "mobile-doctor", "online-doctor-consultation"],
    },

    # ------------------------------------------------------- what to expect
    {
        "slug": "pdp-medical-what-to-expect",
        "nav_label": "What Happens at a PDP Medical",
        "cluster": "pdp",
        "image": "eye-test",
        "image_alt": "An eye chart used in a vision assessment",
        "eyebrow": "Driver Medicals",
        "h1": "What happens at a ",
        "h1_tail": "PDP medical",
        "title": "What Happens at a PDP Medical | Your Online Doctor",
        "description": "What a PDP driver medical actually involves - vision, hearing, "
                       "blood pressure, general health - and what to bring with you.",
        "lede": "It is a short, structured examination against a defined standard. Here is "
                "exactly what it covers.",
        "intro": [
            "Most people arrive at a driver medical with no idea what is about to be "
            "checked, which makes a routine twenty minutes feel like an exam you might "
            "fail. It is not that. It is a set assessment against published criteria, and "
            "knowing what they are removes most of the worry.",
            "It is also not a general health check-up. The doctor is answering one narrow "
            "question: is there anything that would make it unsafe for you to drive "
            "professionally? Plenty of conditions that sound serious do not affect that "
            "answer at all, provided they are properly controlled.",
        ],
        "sections": [
            {
                "h": "Vision",
                "p": ["Your eyesight is tested, with glasses or contact lenses if you "
                      "normally wear them to drive. Both distance vision and your field of "
                      "vision matter, because professional driving depends on seeing what "
                      "is beside you as well as ahead.",
                      "If you need correction to meet the standard, that is recorded on the "
                      "certificate. It does not stop you driving; it means you must drive "
                      "wearing it."],
            },
            {
                "h": "Hearing",
                "p": ["Hearing is checked because you need to be aware of sirens, horns and "
                      "the vehicle itself. As with vision, if you use a hearing aid, it is "
                      "assessed with the aid in place."],
            },
            {
                "h": "Blood pressure and general health",
                "p": ["Blood pressure is measured, and your general physical condition is "
                      "assessed. High blood pressure is the single most common reason a "
                      "driver is surprised at a medical, and it is usually the most "
                      "treatable.",
                      "If your reading is high on the day, that is not automatically the end "
                      "of it. It may mean a recheck, or it may mean treatment and a "
                      "follow-up. Either way it is worth knowing, because it matters a great "
                      "deal more to your life than to your permit."],
            },
            {
                "h": "Chronic conditions and medication",
                "p": ["You will be asked about conditions that can affect driving safely, "
                      "including diabetes, epilepsy, heart conditions and anything causing "
                      "blackouts or loss of consciousness, and about medication that causes "
                      "drowsiness.",
                      "Declaring a condition is not the same as failing. Most well-controlled "
                      "conditions are compatible with professional driving. Concealing one "
                      "is the real risk, both to the certificate and to you."],
            },
            {
                "h": "The certificate",
                "p": ["Where you meet the criteria, the doctor completes and signs the "
                      "certificate, which you then submit with the rest of your application "
                      "at the Driving Licence Testing Centre.",
                      "Check before you leave that every section is completed and that the "
                      "practitioner's details and signature are there. An incomplete form is "
                      "the most common reason a driver has to come back and do this twice."],
            },
            {
                "h": "If you do not meet a criterion",
                "p": ["The doctor will tell you which standard was not met and what would "
                      "need to change. Sometimes that is straightforward, like getting the "
                      "right glasses or bringing blood pressure under control. Sometimes it "
                      "is not.",
                      "A certificate cannot be issued where the standard is not met. That is "
                      "not an administrative obstacle - the standards exist because a "
                      "professional driver carries other people's safety as well as their "
                      "own."],
            },
        ],
        "checklist_title": "What to bring",
        "checklist": [
            "Your identity document",
            "Your current driving licence",
            "Glasses or contact lenses, if you use them",
            "Hearing aids, if you use them",
            "A list of medication you take regularly",
            "Details of any chronic condition and who treats you for it",
        ],
        "faqs": [
            ("How long does a PDP medical take?",
             "The examination itself is usually short. Most of the time is paperwork, so "
             "arriving with your documents ready is the quickest way through it."),
            ("Do I need to fast beforehand?",
             "No. A driver medical is not a fasting test."),
            ("Is blood taken?",
             "Not routinely. If the doctor considers testing necessary based on what the "
             "assessment finds, that is discussed with you."),
            ("What if my blood pressure is high on the day?",
             "The doctor will decide whether to recheck it, treat it, or ask you to return. "
             "A single high reading is not necessarily representative."),
            ("Can I be refused?",
             "A certificate is only issued where the criteria are met. If they are not, the "
             "doctor explains which one and what could change it."),
        ],
        "related_guides": ["pdp-medical-pretoria", "code-10-code-14-driver-medical"],
        "related_services": ["driver-pdp-medicals", "online-doctor-consultation", "mobile-doctor"],
    },

    # --------------------------------------------------- code 10 / code 14
    {
        "slug": "code-10-code-14-driver-medical",
        "nav_label": "Code 10 & Code 14 Medicals",
        "cluster": "pdp",
        "image": "truck",
        "image_alt": "A heavy goods vehicle on the road",
        "eyebrow": "Driver Medicals",
        "h1": "Code 10 and Code 14 ",
        "h1_tail": "driver medicals",
        "title": "Code 10 & Code 14 Driver Medical | Your Online Doctor",
        "description": "The difference between your licence code and a Professional Driving "
                       "Permit, and when a driver medical is required for each.",
        "lede": "Your licence code and your Professional Driving Permit are two different "
                "things. The confusion between them costs drivers a lot of wasted trips.",
        "intro": [
            "Drivers routinely use “code 10”, “code 14” and "
            "“PDP” as if they were the same thing. They are not, and the "
            "difference decides whether you need a medical.",
            "Your licence code describes what size and type of vehicle you are licensed to "
            "drive. A Professional Driving Permit is a separate authorisation that allows "
            "you to drive professionally - carrying goods or passengers for reward, or "
            "carrying dangerous goods. You can hold a code 14 licence and still not be "
            "permitted to drive that vehicle for a living without the permit.",
            "The medical assessment attaches to the permit, not to the licence code. So the "
            "question is not really “does code 14 need a medical” - it is whether "
            "you are driving professionally.",
        ],
        "sections": [
            {
                "h": "Licence code versus permit",
                "p": ["In broad terms, the heavier the vehicle, the higher the code. Code 10 "
                      "covers larger goods vehicles, and code 14 covers the heaviest "
                      "combinations including articulated vehicles.",
                      "The permit sits on top of that. It is what makes driving those "
                      "vehicles for an employer or for reward lawful, and it is the permit "
                      "application that requires the medical certificate."],
            },
            {
                "h": "Who ends up needing a medical",
                "p": ["If you are driving professionally, you need the permit, and the "
                      "permit needs the medical. That covers most drivers of heavy vehicles, "
                      "because very few people hold a code 14 licence for personal use."],
                "list": [
                    "Long-haul and distribution truck drivers",
                    "Articulated and abnormal load drivers",
                    "Bus, coach and shuttle drivers",
                    "Tanker and dangerous goods drivers",
                    "Plant and construction vehicle drivers on public roads",
                    "Any driver whose employer requires a current permit",
                ],
            },
            {
                "h": "What the assessment covers",
                "p": ["The same examination applies regardless of the code you hold: vision, "
                      "hearing, blood pressure and general health, together with questions "
                      "about chronic conditions and medication that could affect driving "
                      "safely. There is no separate, harsher medical for code 14."],
            },
            {
                "h": "Fleet and employer assessments",
                "p": ["Employers running fleets often need several drivers assessed at once, "
                      "and need the certificates to be consistent and correctly completed.",
                      "If you are arranging assessments for a group of drivers rather than "
                      "for yourself, get in touch and we will work out the most practical "
                      "way to do it, including where mobile services can come to the depot."],
            },
            {
                "h": "Renewals",
                "p": ["A permit does not last indefinitely, and a fresh medical is part of "
                      "renewing it. Drivers most often get caught out by leaving it until "
                      "the permit has already lapsed, which can mean time off the road.",
                      "Renewal periods and how recent your certificate must be are set by "
                      "the authorities and can change. Check the current position with your "
                      "Driving Licence Testing Centre, and book the medical before the "
                      "deadline rather than after it."],
            },
        ],
        "checklist_title": "What to bring",
        "checklist": [
            "Your identity document",
            "Your current driving licence showing the code",
            "Your existing permit, if you are renewing",
            "Glasses or contact lenses, if you use them",
            "A list of medication you take regularly",
        ],
        "faqs": [
            ("Is a code 10 licence the same as a PDP?",
             "No. The licence code is what you are licensed to drive. The Professional "
             "Driving Permit is a separate authorisation to drive professionally, and it is "
             "the permit that requires a medical certificate."),
            ("Do I need a medical for a code 14 licence?",
             "The medical attaches to the Professional Driving Permit rather than the "
             "licence code. In practice almost every code 14 driver is driving "
             "professionally and therefore needs one."),
            ("Can my employer arrange medicals for several drivers?",
             "Yes. Get in touch and we will work out the most practical arrangement, "
             "including depot visits where mobile services cover the area."),
            ("Can this be done online?",
             "No. It involves a physical examination including vision and hearing, so it is "
             "conducted in person."),
        ],
        "related_guides": ["pdp-medical-what-to-expect", "pdp-medical-pretoria"],
        "related_services": ["driver-pdp-medicals", "mobile-doctor", "online-doctor-consultation"],
    },
]

BY_SLUG = {g["slug"]: g for g in GUIDE_PAGES}


def in_cluster(name):
    return [g for g in GUIDE_PAGES if g["cluster"] == name]
