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
    # ------------------------------------------------------- sick notes
    {
        "slug": "sick-note-online-south-africa",
        "nav_label": "Sick Notes Explained",
        "cluster": "medical-admin",
        "image": "remote-care",
        "image_alt": "A laptop and a stethoscope on a desk",
        "eyebrow": "Guide",
        "h1": "Can you get a sick note ",
        "h1_tail": "online in South Africa?",
        "title": "Can You Get a Sick Note Online in SA? | Your Online Doctor",
        "description": "What a medical certificate actually is under South African law, "
                       "when a doctor can issue one, and whether employers must accept it.",
        "lede": "Short answer: yes, where it is clinically appropriate. The longer answer "
                "is worth reading, because most of the confusion is about what a "
                "certificate actually is.",
        "intro": [
            "A medical certificate is not an administrative receipt for having been ill. "
            "It is a registered healthcare professional putting their name, their "
            "registration and their professional judgement behind a statement that you "
            "were unfit to work. That is why it cannot simply be requested.",
            "It is also why the question \u201ccan I get one online\u201d has a slightly "
            "different answer than people expect. The channel is not the issue. The "
            "assessment is. If a doctor can properly assess your condition remotely, a "
            "certificate can follow. If they cannot, it should not.",
        ],
        "sections": [
            {
                "h": "What the law actually requires",
                "p": ["South African employment law deals with sick leave through the Basic "
                      "Conditions of Employment Act. In broad terms, an employer may "
                      "require a medical certificate where an employee is absent for more "
                      "than two consecutive days, or on more than two occasions in an "
                      "eight-week period.",
                      "The Act is concerned with the certificate being issued by a person "
                      "registered with a professional council and legally entitled to "
                      "practise. It is not concerned with whether the consultation happened "
                      "in a room or over a video call."],
            },
            {
                "h": "What has to happen before one is issued",
                "p": ["A consultation and an assessment. The doctor needs enough information "
                      "to form a view about whether you were unfit to work, and for how "
                      "long. For many everyday illnesses that can be established through "
                      "history and discussion.",
                      "For others it cannot. Anything that turns on physical examination "
                      "findings may need you to be seen, and the doctor will say so."],
            },
            {
                "h": "Will my employer accept it?",
                "p": ["A certificate issued by a registered healthcare professional "
                      "following a consultation is a valid medical certificate. Some "
                      "employers have internal policies that go further than the law "
                      "requires, so if yours has a specific form or requirement, it is "
                      "worth knowing that before rather than after.",
                      "What makes a certificate questionable is not the channel. It is "
                      "being incomplete, or issued without an assessment."],
            },
            {
                "h": "Backdating",
                "p": ["This is where most requests fall over. A doctor can only certify "
                      "what they are satisfied of, and certifying a period before they "
                      "assessed you is a clinical judgement, not a courtesy.",
                      "Sometimes it is justified and the doctor will say so. Often it is "
                      "not. Asking for a backdated certificate as a favour puts a "
                      "practitioner's registration at risk, which is why the answer is "
                      "frequently no."],
            },
        ],
        "checklist_title": "What helps the consultation go quickly",
        "checklist": [
            "When your symptoms started",
            "What the symptoms actually are, in your own words",
            "Any medication you have already taken for it",
            "Whether you have had the same thing before",
            "What your work involves - some roles matter more than others",
            "Any specific form your employer requires",
        ],
        "faqs": [
            ("Is an online sick note legal in South Africa?",
             "A medical certificate issued by a registered healthcare professional following "
             "a consultation and assessment is valid. The law is concerned with who issued "
             "it, not whether the consultation was remote."),
            ("Can I get a sick note without a consultation?",
             "No. An assessment always comes first."),
            ("How many days can a certificate cover?",
             "That is a clinical judgement based on your condition, not a fixed number."),
            ("Can a certificate be backdated?",
             "Only where the doctor is clinically satisfied that it is justified."),
        ],
        "related_guides": ["prescribe-online-south-africa", "see-doctor-in-person"],
        "related_services": ["sick-note-online", "online-doctor-consultation", "mobile-doctor"],
    },

    # ------------------------------------------------------ prescriptions
    {
        "slug": "prescribe-online-south-africa",
        "nav_label": "Prescriptions Explained",
        "cluster": "medical-admin",
        "image": "pharmacy",
        "image_alt": "Shelves in a pharmacy dispensary",
        "eyebrow": "Guide",
        "h1": "Can a doctor prescribe ",
        "h1_tail": "online in South Africa?",
        "title": "Can a Doctor Prescribe Online in SA? | Your Online Doctor",
        "description": "When a doctor can prescribe after a remote consultation, what "
                       "cannot be prescribed that way, and how repeat medication works.",
        "lede": "Yes, where it is clinically appropriate. What that phrase actually means "
                "is the useful part.",
        "intro": [
            "A prescription is a clinical decision. The doctor is weighing what is wrong, "
            "what you already take, what you are allergic to, and whether the medicine in "
            "question is the right answer for you specifically. None of that changes "
            "because the consultation happened over a call.",
            "What does change is the information available. Without a physical "
            "examination, some conditions cannot be assessed well enough to prescribe "
            "safely, and in those cases the honest answer is that you need to be seen.",
        ],
        "sections": [
            {
                "h": "What usually can be prescribed remotely",
                "p": ["Common conditions where history and symptoms give the doctor enough "
                      "to work with, continuation of treatment that is already established, "
                      "and many chronic medicines where you are stable and being "
                      "monitored."],
            },
            {
                "h": "What usually cannot",
                "p": ["Anything where the diagnosis depends on examination findings. "
                      "Anything needing a test result first. And certain categories of "
                      "medicine that carry prescribing restrictions regardless of the "
                      "consultation channel, including controlled substances.",
                      "Schedule rules in South Africa apply exactly as they would in a "
                      "consulting room. A remote consultation does not create a different "
                      "set of rules, and any service suggesting otherwise is one to avoid."],
            },
            {
                "h": "Repeat and chronic medication",
                "p": ["Repeats are one of the better uses of remote consultation. If you "
                      "are stable on a chronic medicine, a review can often be done without "
                      "travelling anywhere.",
                      "That review is not a formality. The doctor is checking that the "
                      "medicine is still appropriate, still working, and still safe given "
                      "anything that has changed. Sometimes the answer is that you need "
                      "bloods, or a blood pressure check, before the repeat continues."],
            },
            {
                "h": "Where you fill it",
                "p": ["A prescription issued after a consultation can be taken to the "
                      "pharmacy of your choice. You are not tied to a particular dispensary."],
            },
        ],
        "checklist_title": "What to have ready",
        "checklist": [
            "The names and doses of everything you currently take",
            "Any allergies or past reactions to medication",
            "What you have already tried for this problem",
            "Any chronic condition and who manages it",
            "Recent test results, if you have them",
        ],
        "faqs": [
            ("Will I definitely get a prescription?",
             "No. The doctor prescribes what is clinically appropriate, which may differ "
             "from what you expected, or may be nothing at all."),
            ("Can I get antibiotics after an online consultation?",
             "Where they are clinically indicated. A great many infections do not need "
             "them, and prescribing them anyway causes harm at a population level."),
            ("Can controlled medicines be prescribed remotely?",
             "Prescribing restrictions apply the same way as they would in person. Certain "
             "medicines cannot be prescribed this way."),
            ("Can I get a repeat of my chronic medication?",
             "Often yes, following a review. The doctor decides whether a repeat is "
             "appropriate or whether testing is needed first."),
        ],
        "related_guides": ["sick-note-online-south-africa", "see-doctor-in-person"],
        "related_services": ["prescriptions-online", "online-doctor-consultation"],
    },

    # ---------------------------------------------------------------- PrEP
    {
        "slug": "how-to-get-prep-south-africa",
        "nav_label": "Getting PrEP in SA",
        "cluster": "sexual-health",
        "image": "diagnostics",
        "image_alt": "Microscope work in a laboratory",
        "eyebrow": "Guide",
        "h1": "How to get ",
        "h1_tail": "PrEP in South Africa",
        "title": "How to Get PrEP in South Africa | Your Online Doctor",
        "description": "What PrEP is, the testing required before starting, how monitoring "
                       "works, and how to begin the process.",
        "lede": "PrEP is straightforward to take and slightly less straightforward to "
                "start, for one good reason.",
        "intro": [
            "PrEP is medication taken by someone who is HIV negative to reduce the risk of "
            "acquiring HIV. Taken as prescribed, it is highly effective, and it has been "
            "available in South Africa for years through both public and private channels.",
            "The part that trips people up is that you cannot simply be handed it. PrEP "
            "sits inside a framework: testing before you start, a prescription if it is "
            "appropriate, and repeat testing while you continue. That framework exists for "
            "a specific clinical reason, not as bureaucracy.",
        ],
        "sections": [
            {
                "h": "Why the HIV test is not optional",
                "p": ["PrEP uses medicines that are also part of HIV treatment, but at a "
                      "dose intended for prevention rather than treatment. Starting it "
                      "while already living with undiagnosed HIV risks the virus developing "
                      "resistance to those medicines.",
                      "That is a serious outcome, and it is the whole reason a test comes "
                      "first. Any service offering to supply PrEP without testing is "
                      "putting you at risk."],
            },
            {
                "h": "What the process looks like",
                "p": ["An assessment of whether PrEP suits your circumstances, the required "
                      "testing, a prescription where appropriate, and then regular review "
                      "while you continue taking it.",
                      "The consultation part can be done remotely. The testing happens at a "
                      "laboratory, on a request the doctor issues."],
            },
            {
                "h": "Staying on it",
                "p": ["PrEP is not a once-off. Continuing on it means repeat testing at "
                      "intervals, which is both a safety check and an opportunity to review "
                      "whether it is still the right choice for your situation.",
                      "Adherence matters. PrEP works when it is taken as prescribed, and "
                      "the protection is not instant on day one. The doctor will explain "
                      "the specifics for the regimen you are given."],
            },
            {
                "h": "Stopping safely",
                "p": ["There is a correct way to stop, and it is worth asking about rather "
                      "than simply discontinuing. If your circumstances change, raise it in "
                      "a consultation."],
            },
        ],
        "checklist_title": "Worth thinking about beforehand",
        "checklist": [
            "Whether you have tested for HIV recently, and when",
            "Any other medication you take",
            "Any kidney or liver condition you know of",
            "Whether you are also due for broader sexual health screening",
            "How you will manage taking it consistently",
        ],
        "faqs": [
            ("Can I get PrEP online in South Africa?",
             "The assessment and prescription can follow a remote consultation where "
             "clinically appropriate, but the required testing must be completed first."),
            ("What tests are needed before starting?",
             "An HIV test is required, along with any other tests the doctor considers "
             "necessary. The doctor issues the requests."),
            ("Does PrEP protect against other STIs?",
             "No. PrEP is specific to HIV. Other infections need their own prevention and "
             "testing."),
            ("How often do I need to be reviewed?",
             "At regular intervals for as long as you continue. The doctor will set out the "
             "schedule."),
        ],
        "related_guides": ["see-doctor-in-person"],
        "related_services": ["prep-online", "sti-consultation", "contraception"],
    },

    # ------------------------------------------------- in person vs online
    {
        "slug": "see-doctor-in-person",
        "nav_label": "Online or In Person?",
        "cluster": "telehealth",
        "image": "telehealth",
        "image_alt": "A stethoscope beside a mobile phone",
        "eyebrow": "Guide",
        "h1": "When you should see a doctor ",
        "h1_tail": "in person",
        "title": "Online or In Person? When to See a Doctor | Your Online Doctor",
        "description": "Which concerns suit a remote consultation, which need examination, "
                       "and which need emergency care rather than either.",
        "lede": "A telehealth service that cannot tell you when not to use it is not worth "
                "much.",
        "intro": [
            "Remote consultation covers a great deal of ordinary medicine well. It also "
            "has a hard boundary, and knowing where that boundary sits is more useful than "
            "any list of what telehealth can do.",
            "The boundary is the physical examination. A doctor on a video call can see "
            "you, hear you and question you thoroughly. They cannot palpate your abdomen, "
            "listen to your chest, look in your ear, or take your blood pressure.",
        ],
        "sections": [
            {
                "h": "Go to an emergency department, not a consultation",
                "p": ["Some things should not go through any kind of appointment process. "
                      "If any of the following apply, go to your nearest emergency "
                      "department or call emergency services now."],
                "list": [
                    "Chest pain, pressure or tightness",
                    "Difficulty breathing or severe shortness of breath",
                    "Sudden weakness, facial droop or difficulty speaking",
                    "Severe or uncontrolled bleeding",
                    "Loss of consciousness, or a first seizure",
                    "Severe abdominal pain that came on suddenly",
                    "Thoughts of harming yourself",
                    "A serious injury, burn or suspected fracture",
                ],
            },
            {
                "h": "Usually needs an in-person examination",
                "p": ["These are not emergencies, but they turn on findings a camera cannot "
                      "produce."],
                "list": [
                    "Abdominal pain requiring examination",
                    "Ear, throat or chest symptoms needing to be looked at or listened to",
                    "A lump, swelling or breast change",
                    "An injury needing assessment of movement or stability",
                    "A skin lesion where the texture matters, not only the appearance",
                    "Anything requiring blood pressure, imaging or an internal examination",
                ],
            },
            {
                "h": "Generally well suited to a remote consultation",
                "p": ["This is the large middle ground where most consultations actually "
                      "sit."],
                "list": [
                    "Common everyday illness",
                    "Follow-up after a previous consultation",
                    "Repeat and chronic medication review",
                    "Mental health consultations",
                    "Sexual health, contraception and PrEP discussions",
                    "Questions about medication or test results",
                    "Weight, nutrition and lifestyle consultations",
                    "Deciding whether you need to be seen at all",
                ],
            },
            {
                "h": "Being referred on is a normal outcome",
                "p": ["If a doctor tells you during a remote consultation that you need to "
                      "be examined, that is the process working rather than failing. The "
                      "assessment of whether you can be managed remotely is itself a "
                      "clinical judgement, and it is made in every single consultation."],
            },
        ],
        "checklist_title": "If you are unsure which you need",
        "checklist": [
            "Describe the symptom, not your theory about the cause",
            "Say when it started and whether it is getting worse",
            "Mention anything that makes it better or worse",
            "Say if you have had it before and what happened then",
            "Mention any chronic condition and current medication",
        ],
        "faqs": [
            ("How do I know if my problem can be handled online?",
             "Often you do not, and that is fine. Deciding is part of what the consultation "
             "is for."),
            ("Will I be charged if I am told to go in person?",
             "That depends on the service. The assessment itself is a consultation, which "
             "is why being referred on is not a wasted appointment."),
            ("Can telehealth be used in an emergency?",
             "No. In an emergency, go to your nearest emergency department or call your "
             "local emergency services immediately."),
        ],
        "related_guides": ["sick-note-online-south-africa", "after-hours-medical-care-sa"],
        "related_services": ["online-doctor-consultation", "mobile-doctor", "specialist-referrals"],
    },

    # ---------------------------------------------------------- after hours
    {
        "slug": "after-hours-medical-care-sa",
        "nav_label": "After-Hours Care",
        "cluster": "telehealth",
        "image": "video-consult",
        "image_alt": "A remote consultation on screen",
        "eyebrow": "Guide",
        "h1": "After-hours medical care ",
        "h1_tail": "in South Africa",
        "title": "After-Hours Medical Care in South Africa | Your Online Doctor",
        "description": "What your options are when you need a doctor outside consulting "
                       "hours, and how to decide which one you actually need.",
        "lede": "Illness has no respect for consulting hours. Knowing your options before "
                "you need them saves a bad decision at eleven at night.",
        "intro": [
            "Most people only work out what is available after hours while they are already "
            "worried, which is the worst possible moment to be researching it. The options "
            "in South Africa are reasonably clear once you have seen them laid out.",
            "The first question is never \u201cwho is open\u201d. It is how urgent this "
            "actually is, because that determines which of the options is right and the "
            "wrong choice costs either money or time you do not have.",
        ],
        "sections": [
            {
                "h": "If it is an emergency",
                "p": ["Go to the nearest emergency department or call emergency services. "
                      "Do not wait for an appointment, and do not start with a phone "
                      "consultation. Chest pain, breathing difficulty, stroke symptoms, "
                      "severe bleeding, loss of consciousness and thoughts of self-harm all "
                      "belong here."],
            },
            {
                "h": "If it is urgent but not an emergency",
                "p": ["Private hospital emergency units and after-hours clinics handle a "
                      "great deal of this. So do casualty departments at state hospitals, "
                      "though waiting times vary considerably.",
                      "This is the category where cost and waiting time pull in opposite "
                      "directions, and where it is worth knowing in advance what is near "
                      "you and what it is likely to cost."],
            },
            {
                "h": "If it can wait but you want advice tonight",
                "p": ["This is the largest category and the one people most often escalate "
                      "unnecessarily. A remote consultation can establish whether you need "
                      "to be seen now, in the morning, or at all.",
                      "That triage is genuinely valuable. A great many late-night hospital "
                      "trips are made by people who would have been reassured, or given a "
                      "safer plan, by a fifteen-minute conversation."],
            },
            {
                "h": "If it is a prescription you have run out of",
                "p": ["Running out of chronic medication over a weekend is common and "
                      "usually solvable. A pharmacist can sometimes assist in an emergency "
                      "depending on the medicine, and a consultation can address the repeat "
                      "properly.",
                      "The better fix is upstream: review repeats before they run out "
                      "rather than after."],
            },
        ],
        "checklist_title": "Worth having written down before you need it",
        "checklist": [
            "Your nearest emergency department and how long it takes to reach",
            "Your nearest after-hours or urgent care clinic",
            "Your medical aid's emergency number, if you have one",
            "A current list of your medication and doses",
            "Any chronic conditions and allergies",
            "Who to call for someone who may need to come with you",
        ],
        "faqs": [
            ("Is Your Online Doctor available 24 hours?",
             "Your Online Doctor is designed to provide convenient and extended access to "
             "healthcare beyond traditional consulting hours, subject to service "
             "availability and clinical suitability."),
            ("Should I go to casualty or wait until morning?",
             "If it is an emergency, go now. If you are unsure, that uncertainty is itself "
             "a good reason to speak to someone rather than to guess."),
            ("Can I get medication at night?",
             "Some pharmacies operate extended hours. Whether a prescription can be issued "
             "depends on an assessment and on what the medicine is."),
        ],
        "related_guides": ["see-doctor-in-person", "sick-note-online-south-africa"],
        "related_services": ["online-doctor-consultation", "mobile-doctor", "prescriptions-online"],
    },
    # ------------------------------------------------- is a biokineticist a doctor
    {
        "slug": "is-a-biokineticist-a-doctor",
        "nav_label": "Is a Biokineticist a Doctor?",
        "cluster": "allied-health",
        "image": "biokinetics",
        "image_alt": "Exercise-based rehabilitation",
        "eyebrow": "Guide",
        "h1": "Is a biokineticist ",
        "h1_tail": "a doctor?",
        "title": "Is a Biokineticist a Doctor? | Your Online Doctor",
        "description": "What a biokineticist is, how they are registered in South Africa, "
                       "and how they differ from a doctor and a physiotherapist.",
        "lede": "No - and the honest answer is more interesting than the short one.",
        "intro": [
            "A biokineticist is not a medical doctor. They do not diagnose disease, they "
            "do not prescribe medication, and they are not trained in medicine. The "
            "question comes up constantly though, and usually because someone has been "
            "referred to one and is trying to work out what they are walking into.",
            "What a biokineticist is: a healthcare professional registered with the Health "
            "Professions Council of South Africa, who uses exercise clinically. The "
            "qualification is a four-year degree plus an internship, and the registration "
            "sits alongside physiotherapy, dietetics and psychology rather than alongside "
            "personal training.",
        ],
        "sections": [
            {
                "h": "What they actually do",
                "p": ["Biokineticists prescribe and supervise exercise as a form of "
                      "treatment. That covers the final phase of rehabilitation after "
                      "injury or surgery, and the ongoing management of chronic "
                      "conditions."],
                "list": [
                    "Rehabilitation after injury, once the acute phase has settled",
                    "Recovery and conditioning after surgery",
                    "Exercise programmes for diabetes and hypertension",
                    "Cardiac rehabilitation",
                    "Functional and postural assessment",
                    "Preventing an old injury from recurring",
                ],
            },
            {
                "h": "The distinction that matters",
                "p": ["A doctor diagnoses and treats disease, and can prescribe. A "
                      "biokineticist works within a scope defined by exercise, and refers "
                      "back to a doctor when something falls outside it.",
                      "That boundary is not a limitation so much as the point. A "
                      "biokineticist is the person you want once a diagnosis exists and the "
                      "question has become how to rebuild strength and function safely."],
            },
            {
                "h": "Why people confuse the two",
                "p": ["Partly the title - \u201cbiokineticist\u201d sounds medical in a "
                      "way \u201cpersonal trainer\u201d does not, and it should, because "
                      "the registration is real. Partly because they work in clinical "
                      "settings and take referrals from doctors.",
                      "The practical consequence is that a biokineticist is an appropriate "
                      "person to be referred to, and not an appropriate person to diagnose "
                      "the problem in the first place."],
            },
        ],
        "checklist_title": "When a biokineticist is the right person",
        "checklist": [
            "You have a diagnosis and need to rebuild strength or function",
            "An old injury keeps returning",
            "You have been told exercise is part of managing a chronic condition",
            "You are recovering from surgery and past the acute phase",
            "You want structured conditioning rather than a gym programme",
        ],
        "faqs": [
            ("Is a biokineticist a doctor?",
             "No. A biokineticist is a healthcare professional registered with the HPCSA "
             "who uses exercise clinically. They do not diagnose disease or prescribe "
             "medication."),
            ("Are biokineticists registered in South Africa?",
             "Yes, with the Health Professions Council of South Africa."),
            ("Do I need a referral to see one?",
             "Not necessarily, though a medical assessment often comes first where the "
             "underlying problem has not been diagnosed."),
            ("Is a biokineticist the same as a personal trainer?",
             "No. The training, registration and scope are different, and biokineticists "
             "work clinically with injury and chronic disease."),
        ],
        "related_guides": ["biokineticist-or-physiotherapist"],
        "related_services": ["biokinetics", "physiotherapy", "weight-management"],
    },

    # --------------------------------------------- biokineticist vs physio
    {
        "slug": "biokineticist-or-physiotherapist",
        "nav_label": "Biokineticist or Physio?",
        "cluster": "allied-health",
        "image": "physiotherapy",
        "image_alt": "A physiotherapy treatment session",
        "eyebrow": "Guide",
        "h1": "Biokineticist or physiotherapist &mdash; ",
        "h1_tail": "which do you need?",
        "title": "Biokineticist or Physiotherapist? | Your Online Doctor",
        "description": "The practical difference between a physiotherapist and a "
                       "biokineticist, and which one to see for your situation.",
        "lede": "They are not competitors. Most of the time they are sequential.",
        "intro": [
            "Both are HPCSA-registered healthcare professionals. Both work with movement, "
            "injury and function. People treat it as a choice between them, when in "
            "practice the two tend to come one after the other.",
            "The simplest way to think about it: physiotherapy generally handles pain and "
            "the acute phase, biokinetics generally handles the rebuilding that follows. "
            "Skipping the second part is one of the more common reasons an injury keeps "
            "coming back.",
        ],
        "sections": [
            {
                "h": "See a physiotherapist when",
                "p": ["The problem is recent, painful, or limiting your movement right now."],
                "list": [
                    "You have just injured yourself",
                    "You are in pain and need it managed",
                    "Movement is restricted and you need hands-on treatment",
                    "You are immediately post-surgery",
                    "You need an assessment of what is actually wrong",
                ],
            },
            {
                "h": "See a biokineticist when",
                "p": ["The pain has settled and the question has become strength, function "
                      "and not doing it again."],
                "list": [
                    "You have finished the acute phase of treatment",
                    "You are strong enough to work but not back to normal",
                    "The same injury keeps returning",
                    "Exercise is part of managing a chronic condition",
                    "You need a structured, progressive programme",
                ],
            },
            {
                "h": "When the answer is neither, yet",
                "p": ["If nobody has established what is actually wrong, a medical "
                      "assessment should come first. Treating a problem that has not been "
                      "diagnosed is how people spend months on the wrong thing.",
                      "That is particularly true for pain that came on without an injury, "
                      "pain that wakes you at night, or anything accompanied by numbness, "
                      "weakness or weight loss."],
            },
            {
                "h": "They often work together",
                "p": ["A good outcome frequently involves both, in sequence, sometimes with "
                      "a doctor coordinating. Through a connected platform the handover "
                      "between them carries the history, rather than you repeating it."],
            },
        ],
        "checklist_title": "Quick way to decide",
        "checklist": [
            "In pain right now - start with physiotherapy",
            "Pain settled, strength not back - biokinetics",
            "No diagnosis yet - medical assessment first",
            "Chronic condition, told to exercise - biokinetics",
            "Night pain, numbness or weakness - see a doctor first",
        ],
        "faqs": [
            ("What is the difference between a biokineticist and a physiotherapist?",
             "Physiotherapy generally addresses the acute phase of injury and pain; "
             "biokinetics generally addresses the rehabilitation and conditioning that "
             "follows. They often work in sequence."),
            ("Can I see both?",
             "Yes, and often that is the right answer, with physiotherapy first and "
             "biokinetics once the acute phase has settled."),
            ("Do I need a doctor first?",
             "Where the problem has not been diagnosed, or where there are warning signs "
             "like night pain or numbness, yes."),
        ],
        "related_guides": ["is-a-biokineticist-a-doctor", "see-doctor-in-person"],
        "related_services": ["physiotherapy", "biokinetics", "specialist-referrals"],
    },

    # ------------------------------------------------------ public holidays
    {
        "slug": "doctors-public-holidays-south-africa",
        "nav_label": "Doctors on Public Holidays",
        "cluster": "telehealth",
        "image": "remote-care",
        "image_alt": "A laptop and a stethoscope on a desk",
        "eyebrow": "Guide",
        "h1": "Do doctors work on ",
        "h1_tail": "public holidays?",
        "title": "Do Doctors Work on Public Holidays in SA? | Your Online Doctor",
        "description": "What is open on a South African public holiday, what is not, and "
                       "how to plan around the long weekends.",
        "lede": "Some do, most practices do not, and the gap is predictable enough to plan "
                "around.",
        "intro": [
            "South Africa has twelve public holidays a year, and several of them cluster "
            "into long weekends. General practices overwhelmingly close on those days, "
            "which produces an entirely foreseeable problem that catches people out "
            "anyway.",
            "What stays open: hospital emergency departments, always. Many private "
            "after-hours and urgent care clinics. Some pharmacies, often on reduced hours. "
            "And remote consultation services, subject to their own availability.",
        ],
        "sections": [
            {
                "h": "What is actually open",
                "p": ["Emergency departments operate continuously, public and private. "
                      "After-hours clinics attached to private hospitals usually run, "
                      "though not always on normal hours.",
                      "Retail pharmacies in shopping centres often open for part of the "
                      "day, following centre trading hours rather than their own."],
            },
            {
                "h": "The predictable problem",
                "p": ["Chronic medication. A long weekend is four days, and a repeat that "
                      "was always going to run out on the Saturday becomes a crisis on the "
                      "Friday night.",
                      "This is worth a diary note rather than a plan. Check your repeats "
                      "before a long weekend, not during one."],
            },
            {
                "h": "If something happens anyway",
                "p": ["Decide first whether it is an emergency. If it is, go to an "
                      "emergency department and do not wait for anything else.",
                      "If it is not, a remote consultation can establish whether you need "
                      "to be seen now or whether it can safely wait until practices "
                      "reopen. That question is often the only thing you actually need "
                      "answered."],
            },
        ],
        "checklist_title": "Before a long weekend",
        "checklist": [
            "Check whether any chronic repeat falls due",
            "Know where your nearest emergency department is",
            "Know which pharmacy near you opens on holidays",
            "Keep your medication list somewhere findable",
            "Have your medical aid details accessible",
        ],
        "faqs": [
            ("Are GP practices open on public holidays in South Africa?",
             "Most are closed. Emergency departments operate continuously, and many "
             "after-hours clinics run on reduced hours."),
            ("Can I get a prescription on a public holiday?",
             "Where a consultation is available and it is clinically appropriate. Whether "
             "you can have it dispensed depends on pharmacy trading hours."),
            ("What if I run out of chronic medication?",
             "Speak to a pharmacist, who may be able to assist in an emergency depending on "
             "the medicine. The better answer is to review repeats before the weekend."),
        ],
        "related_guides": ["after-hours-medical-care-sa", "prescribe-online-south-africa"],
        "related_services": ["online-doctor-consultation", "prescriptions-online"],
    },

    # ------------------------------------- psychologist vs psychiatrist
    {
        "slug": "psychologist-psychiatrist-counsellor",
        "nav_label": "Psychologist or Psychiatrist?",
        "cluster": "mental-health",
        "image": "therapy",
        "image_alt": "Two people in conversation",
        "eyebrow": "Guide",
        "h1": "Psychologist, psychiatrist or counsellor &mdash; ",
        "h1_tail": "who should you see?",
        "title": "Psychologist, Psychiatrist or Counsellor? | Your Online Doctor",
        "description": "The difference between a psychologist, a psychiatrist and a "
                       "counsellor in South Africa, and how to work out who you need.",
        "lede": "The titles get used interchangeably. They are three different jobs.",
        "intro": [
            "Deciding to get help is usually the hard part. Then comes a second obstacle "
            "nobody warns you about: working out which kind of professional you are "
            "actually looking for, with three titles that sound similar and mean different "
            "things.",
            "The shortest version: psychiatrists are medical doctors and can prescribe. "
            "Psychologists provide assessment and therapy and cannot prescribe. "
            "Counsellors provide support and counselling within a narrower scope. All "
            "three are registered, and all three are legitimate - for different things.",
        ],
        "sections": [
            {
                "h": "Psychiatrist",
                "p": ["A medical doctor who has specialised in psychiatry. They diagnose "
                      "mental illness and can prescribe medication, and they are the right "
                      "person where medication is likely to be central to treatment.",
                      "Typically involved in more severe or complex presentations, or where "
                      "a diagnosis is unclear and needs medical assessment."],
            },
            {
                "h": "Psychologist",
                "p": ["A registered professional providing psychological assessment and "
                      "talking therapy. They do not prescribe.",
                      "This is who most people picture when they imagine therapy, and it is "
                      "where the bulk of ongoing work happens - anxiety, depression, "
                      "trauma, relationships, burnout."],
            },
            {
                "h": "Counsellor",
                "p": ["Registered counsellors work within a defined scope, providing "
                      "supportive counselling and containment rather than the full range of "
                      "psychological intervention. They refer on where something falls "
                      "outside that scope.",
                      "Often more accessible and more affordable, and entirely appropriate "
                      "for many situations."],
            },
            {
                "h": "A reasonable starting point",
                "p": ["If you genuinely do not know, starting with a doctor is sensible. A "
                      "consultation can establish what is going on and point you to the "
                      "right discipline, rather than you guessing and possibly spending "
                      "months with the wrong fit.",
                      "That is also the honest answer to the cost question. Getting matched "
                      "correctly first time is cheaper than three false starts."],
            },
            {
                "h": "If you are in crisis",
                "p": ["None of this applies. If you are having thoughts of harming "
                      "yourself, go to your nearest emergency department or contact "
                      "emergency services immediately. Do not wait for an appointment with "
                      "anyone."],
            },
        ],
        "checklist_title": "Rough guide",
        "checklist": [
            "Medication likely needed - psychiatrist",
            "Ongoing talking therapy - psychologist",
            "Support through a difficult period - counsellor",
            "Not sure what is happening - start with a doctor",
            "In crisis - emergency department, now",
        ],
        "faqs": [
            ("Do psychologists prescribe medication in South Africa?",
             "No. Psychologists provide assessment and therapy. Where medication needs "
             "considering, referral to a doctor or psychiatrist is arranged."),
            ("Is a psychiatrist a medical doctor?",
             "Yes. A psychiatrist is a medical doctor who has specialised in psychiatry and "
             "can prescribe."),
            ("Do I need a diagnosis before seeing a psychologist?",
             "No. Many people seek psychological support for a difficult period rather than "
             "for a diagnosed condition."),
            ("Can any of this be done remotely?",
             "Remote psychology sessions are well established and work well for many "
             "presentations."),
        ],
        "related_guides": ["see-doctor-in-person"],
        "related_services": ["mental-health", "psychology", "specialist-referrals"],
    },
]

BY_SLUG = {g["slug"]: g for g in GUIDE_PAGES}


def in_cluster(name):
    return [g for g in GUIDE_PAGES if g["cluster"] == name]
