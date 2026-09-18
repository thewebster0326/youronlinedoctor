"""Per-service landing page content.

One entry per page. Everything here is written to be genuinely distinct -
Google treats near-duplicate landing pages as thin content, and thin pages
drag down Ads Quality Score.

Copy rules followed throughout:
  - describes the service, never gives clinical instruction
  - no guaranteed outcomes (prescriptions, certificates, results)
  - every page carries the clinical-suitability qualifier
  - no superlatives or comparative claims (HPCSA ethical rules on advertising)
"""

SERVICE_PAGES = [
    # ------------------------------------------------------------------ core
    {
        "slug": "online-doctor-consultation",
        "nav_label": "Online Doctor Consultation",
        "group": "Medical",
        "eyebrow": "Online Doctor Consultation",
        "h1": "Consult a doctor ",
        "h1_tail": "online",
        "title": "Online Doctor Consultation South Africa | Your Online Doctor",
        "description": "Consult a registered doctor online from anywhere in South Africa. "
                       "Assessment, advice, and prescriptions or referrals where appropriate.",
        "lede": "Speak to a doctor without travelling to a waiting room. Consultations happen "
                "remotely, wherever you are in South Africa.",
        "intro": [
            "An online consultation is a conversation with a doctor conducted remotely rather "
            "than in a consulting room. You describe your symptoms and history, the doctor "
            "asks the questions a consultation requires, and you agree on what happens next.",
            "For a great many everyday concerns this works well. It removes the travel, the "
            "waiting room, and the difficulty of finding an appointment that fits around work "
            "or family. What it cannot do is replace a physical examination, and that "
            "shapes which concerns are suitable.",
        ],
        "covers_title": "What a consultation can include",
        "covers": [
            "A structured assessment of your symptoms and medical history",
            "Advice on managing the condition",
            "A prescription, where clinically appropriate",
            "A medical certificate, where appropriate",
            "A referral to a specialist or another healthcare professional",
            "A request for laboratory tests where these are indicated",
        ],
        "suitability": "Common conditions, follow-ups, repeat concerns and questions about "
                       "medication are often well suited to a remote consultation. Anything "
                       "needing hands-on examination, imaging, or urgent attention is not - "
                       "and in those cases the doctor will tell you so and direct you to "
                       "in-person care.",
        "faqs": [
            ("How does an online doctor consultation work?",
             "You get in touch, we arrange a time, and the consultation takes place remotely. "
             "The doctor takes your history, assesses your symptoms and discusses the "
             "appropriate next step with you."),
            ("Is an online consultation with a real doctor?",
             "Yes. Consultations are conducted by healthcare professionals registered to "
             "practise in South Africa."),
            ("What if my condition cannot be handled online?",
             "The doctor will tell you and direct you to appropriate in-person care. That is "
             "a clinical judgement made in every consultation."),
            ("Can I use this for an emergency?",
             "No. Telemedicine is not suitable for emergencies. Go to your nearest emergency "
             "department or call your local emergency services immediately."),
        ],
        "related": ["prescriptions-online", "sick-note-online", "mobile-doctor"],
    },
    {
        "slug": "prescriptions-online",
        "nav_label": "Online Prescriptions",
        "group": "Medical",
        "eyebrow": "Online Prescriptions",
        "h1": "Prescriptions, where ",
        "h1_tail": "clinically appropriate",
        "title": "Online Prescription South Africa | Your Online Doctor",
        "description": "Get a prescription online in South Africa where it is clinically "
                       "appropriate, following an assessment by a registered doctor.",
        "lede": "A prescription follows an assessment. It is never issued on request alone.",
        "intro": [
            "A prescription is a clinical decision, not a product. The doctor assesses your "
            "symptoms, your history and any medication you already take, and prescribes only "
            "where doing so is appropriate and safe for your situation.",
            "That means a consultation comes first, every time. Some concerns can be resolved "
            "and prescribed for remotely. Others need examination or testing before anyone can "
            "responsibly prescribe, and in those cases you will be told what is needed instead.",
        ],
        "covers_title": "What this covers",
        "covers": [
            "Assessment of your current symptoms and medical history",
            "Review of medication you are already taking",
            "A prescription issued where clinically appropriate",
            "Repeat medication review, where suitable",
            "Advice on how and when to take what is prescribed",
            "Referral or testing where a prescription is not appropriate yet",
        ],
        "suitability": "Schedule and prescribing rules in South Africa apply exactly as they "
                       "would in a consulting room. Certain medicines cannot be prescribed "
                       "remotely, and no prescription is guaranteed in advance of a "
                       "consultation.",
        "faqs": [
            ("Can I get a prescription online in South Africa?",
             "A prescription may be issued where it is clinically appropriate following an "
             "assessment by the doctor. It is not guaranteed in advance."),
            ("Can I get a repeat of my chronic medication?",
             "Repeat medication can often be reviewed remotely. The doctor will decide whether "
             "a repeat is appropriate or whether you need review or testing first."),
            ("Where do I collect the medication?",
             "A prescription can be taken to the pharmacy of your choice."),
            ("Will I definitely get what I ask for?",
             "No. The doctor prescribes what is clinically appropriate, which may differ from "
             "what you expected, or may be nothing at all."),
        ],
        "related": ["online-doctor-consultation", "sick-note-online", "contraception"],
    },
    {
        "slug": "sick-note-online",
        "nav_label": "Sick Notes & Certificates",
        "group": "Medical",
        "eyebrow": "Medical Certificates",
        "h1": "Sick notes and ",
        "h1_tail": "medical certificates",
        "title": "Online Sick Note South Africa | Your Online Doctor",
        "description": "Obtain a medical certificate online in South Africa where clinically "
                       "appropriate, following a consultation with a registered doctor.",
        "lede": "A medical certificate follows a consultation and an assessment - it is a "
                "clinical document, not an administrative one.",
        "intro": [
            "A medical certificate records a doctor's professional opinion that you were unfit "
            "for work or study. It carries the doctor's name and registration, which is why it "
            "can only follow an actual consultation and assessment.",
            "If you are unwell and cannot get to a practice, a remote consultation is often a "
            "practical way to be assessed. Whether a certificate is issued, and for what "
            "period, is the doctor's clinical judgement.",
        ],
        "covers_title": "What this covers",
        "covers": [
            "A consultation and assessment of your condition",
            "A medical certificate issued where clinically appropriate",
            "Advice on managing the condition and on returning to work",
            "A referral where your condition needs further attention",
        ],
        "suitability": "A certificate cannot be issued for a period before the consultation "
                       "took place unless the doctor is clinically satisfied that is "
                       "justified. Certificates are not issued on request without an "
                       "assessment.",
        "faqs": [
            ("Can I get a sick note from an online doctor?",
             "A medical certificate may be issued where it is clinically appropriate following "
             "a consultation and assessment."),
            ("Will my employer accept it?",
             "A certificate issued by a registered healthcare professional following a "
             "consultation is a valid medical certificate."),
            ("Can I get a certificate for days I was already off?",
             "Backdating is a clinical decision and is only possible where the doctor is "
             "satisfied it is justified."),
            ("Can I get a certificate without a consultation?",
             "No. An assessment always comes first."),
        ],
        "related": ["online-doctor-consultation", "prescriptions-online", "driver-pdp-medicals"],
    },

    # --------------------------------------------------------------- women's
    {
        "slug": "womens-health",
        "nav_label": "Women's Health",
        "group": "Women's Health",
        "eyebrow": "Women&rsquo;s Health",
        "h1": "Women&rsquo;s health, ",
        "h1_tail": "discussed privately",
        "title": "Women's Health Online Consultation | Your Online Doctor",
        "description": "Private online consultations for women's health in South Africa - "
                       "contraception, sexual health and general women's health concerns.",
        "lede": "Consultations you can have from your own space, without a waiting room.",
        "intro": [
            "Women's health covers a wide range of concerns, and many of them are easier to "
            "raise from somewhere private than across a reception desk. A remote consultation "
            "removes that barrier.",
            "The doctor takes a full history, discusses your concern properly, and either "
            "manages it remotely or connects you with the right professional - which may be a "
            "specialist, a dietitian, or a psychologist, depending on what you need.",
        ],
        "covers_title": "What this covers",
        "covers": [
            "General women's health consultations",
            "Contraception advice, initiation and review",
            "Sexual health concerns",
            "Menstrual and cycle-related concerns",
            "Referral to a specialist where indicated",
            "Laboratory test requests where appropriate",
        ],
        "suitability": "Some concerns need a physical examination, a scan, or a screening test "
                       "that cannot be done remotely. Where that is the case you will be told "
                       "clearly and referred appropriately.",
        "faqs": [
            ("Do I need to be examined?",
             "It depends entirely on the concern. Many can be assessed through history and "
             "discussion; some cannot, and you will be referred for examination."),
            ("Is the consultation confidential?",
             "Yes. The same professional and legal confidentiality obligations apply as in an "
             "in-person consultation."),
            ("Can I be referred to a gynaecologist?",
             "Yes. Specialist referral is available where it is clinically indicated."),
        ],
        "related": ["contraception", "sti-consultation", "mental-health"],
    },
    {
        "slug": "contraception",
        "nav_label": "Contraception",
        "group": "Women's Health",
        "eyebrow": "Contraception",
        "h1": "Contraception ",
        "h1_tail": "advice and review",
        "title": "Contraception Online Consultation | Your Online Doctor",
        "description": "Online contraception consultations in South Africa - discuss options, "
                       "start or review a method with a registered doctor.",
        "lede": "A conversation about what suits your circumstances, not a menu.",
        "intro": [
            "Choosing contraception is a decision that depends on your health history, your "
            "circumstances and what you want from a method. It is worth a proper conversation.",
            "In a consultation the doctor takes your history, talks through the options that "
            "are appropriate for you, and either prescribes where that is suitable or arranges "
            "what needs to happen in person.",
        ],
        "covers_title": "What this covers",
        "covers": [
            "Discussion of contraceptive options appropriate to your history",
            "Starting a method, where clinically appropriate",
            "Review of a method you are already using",
            "Managing side effects or switching methods",
            "Referral for methods that must be fitted or administered in person",
        ],
        "suitability": "Methods that must be inserted, fitted or injected require an in-person "
                       "appointment. A remote consultation can still cover the assessment and "
                       "the decision, with the procedure arranged separately.",
        "faqs": [
            ("Can contraception be prescribed online?",
             "Some methods can be prescribed remotely where clinically appropriate following "
             "an assessment. Others require an in-person appointment."),
            ("Can I switch to a different method?",
             "Yes, that is a common reason for a consultation. The doctor will discuss why the "
             "current method is not working and what might suit better."),
            ("What if I am having side effects?",
             "Raise it in a consultation. Side effects are a clinical matter and may mean a "
             "review, a change, or further assessment."),
        ],
        "related": ["womens-health", "sti-consultation", "prep-online"],
    },

    # ----------------------------------------------------------------- men's
    {
        "slug": "mens-health",
        "nav_label": "Men's Health",
        "group": "Men's Health",
        "eyebrow": "Men&rsquo;s Health",
        "h1": "Men&rsquo;s health, ",
        "h1_tail": "without the waiting room",
        "title": "Men's Health Online Consultation | Your Online Doctor",
        "description": "Discreet online consultations for men's health in South Africa - "
                       "sexual health, erectile dysfunction and general health concerns.",
        "lede": "The concerns men most often put off are usually the ones worth raising "
                "soonest.",
        "intro": [
            "Men delay seeing a doctor more than they should, and sexual health concerns get "
            "delayed longest of all. A consultation you can have privately, without booking "
            "time off or sitting in a waiting room, removes most of the reasons for putting "
            "it off.",
            "The doctor assesses the concern properly. Some of what presents as a standalone "
            "problem turns out to be a sign of something else worth checking, which is exactly "
            "why the assessment matters.",
        ],
        "covers_title": "What this covers",
        "covers": [
            "General men's health consultations",
            "Sexual health concerns",
            "Erectile dysfunction-related consultations",
            "Assessment of related health risks",
            "Laboratory test requests where indicated",
            "Referral to a specialist where appropriate",
        ],
        "suitability": "Erectile difficulty can be related to cardiovascular health, blood "
                       "pressure, diabetes, medication or stress. An assessment looks at the "
                       "whole picture rather than the symptom alone, and may lead to testing "
                       "or referral.",
        "faqs": [
            ("Is the consultation private?",
             "Yes. It is subject to the same confidentiality obligations as any consultation, "
             "and you can have it from wherever you are comfortable speaking freely."),
            ("Can erectile dysfunction be treated after an online consultation?",
             "Treatment may be prescribed where clinically appropriate following an "
             "assessment. Assessment comes first, because the cause matters."),
            ("Will I need blood tests?",
             "Possibly. Where testing is indicated the doctor can issue a laboratory request."),
        ],
        "related": ["sti-consultation", "weight-management", "online-doctor-consultation"],
    },

    # ------------------------------------------------- sexual & reproductive
    {
        "slug": "sti-consultation",
        "nav_label": "STI Consultations",
        "group": "Sexual & Reproductive Health",
        "eyebrow": "STI Consultations",
        "h1": "STI consultations, ",
        "h1_tail": "handled discreetly",
        "title": "STI Consultation Online South Africa | Your Online Doctor",
        "description": "Private online STI consultations in South Africa. Assessment, testing "
                       "requests and treatment where clinically appropriate.",
        "lede": "Discreet assessment, testing where indicated, and treatment where "
                "appropriate.",
        "intro": [
            "Concern about a sexually transmitted infection is a common reason to want a "
            "consultation you can have privately. The consultation itself is straightforward: "
            "the doctor takes a history, assesses the risk and symptoms, and decides what "
            "testing or treatment is appropriate.",
            "Testing usually means a laboratory request you take to a lab. Some infections can "
            "be treated on clinical grounds; others need a result first. Partner notification "
            "and follow-up form part of the discussion where relevant.",
        ],
        "covers_title": "What this covers",
        "covers": [
            "Assessment of symptoms and risk",
            "Laboratory test requests where indicated",
            "Treatment where clinically appropriate",
            "Discussion of partner notification and follow-up",
            "Advice on prevention, including PrEP where relevant",
            "Referral where examination or specialist input is needed",
        ],
        "suitability": "Some presentations need physical examination or swabs that cannot be "
                       "taken remotely. Where that applies you will be referred for in-person "
                       "assessment.",
        "faqs": [
            ("Can I be tested for STIs after an online consultation?",
             "The doctor can issue a laboratory request where testing is indicated, which you "
             "take to a laboratory."),
            ("Can an STI be treated without a test?",
             "Some infections can be treated on clinical grounds. That is a decision for the "
             "doctor based on your symptoms and risk."),
            ("Is this confidential?",
             "Yes, subject to the same confidentiality obligations as any consultation."),
        ],
        "related": ["prep-online", "mens-health", "womens-health"],
    },
    {
        "slug": "prep-online",
        "nav_label": "HIV Prevention & PrEP",
        "group": "Sexual & Reproductive Health",
        "eyebrow": "HIV Prevention",
        "h1": "PrEP and ",
        "h1_tail": "HIV prevention",
        "title": "PrEP Online South Africa | Your Online Doctor",
        "description": "Online PrEP consultations in South Africa - assessment, required "
                       "testing and prescription where clinically appropriate.",
        "lede": "PrEP requires assessment and ongoing monitoring. Both can start with a "
                "remote consultation.",
        "intro": [
            "PrEP is medication taken to reduce the risk of acquiring HIV. It is prescribed "
            "within a structured framework: testing before starting, a prescription where "
            "appropriate, and regular monitoring while you continue.",
            "A remote consultation handles the assessment and the discussion of whether PrEP "
            "suits your circumstances, and can issue the laboratory requests the framework "
            "requires. The testing itself happens at a laboratory.",
        ],
        "covers_title": "What this covers",
        "covers": [
            "Assessment of whether PrEP is appropriate for your circumstances",
            "The laboratory tests required before starting",
            "Prescription where clinically appropriate",
            "Monitoring and repeat testing while you continue",
            "Advice on adherence and on stopping safely",
            "Broader sexual health and STI assessment alongside",
        ],
        "suitability": "PrEP cannot be started without the required testing, including an HIV "
                       "test, because starting it with undiagnosed HIV causes harm. That "
                       "testing is not optional and cannot be skipped.",
        "faqs": [
            ("Can I get PrEP online in South Africa?",
             "An assessment and prescription can follow a remote consultation where clinically "
             "appropriate, but the required laboratory testing must be completed first."),
            ("What tests are needed before starting PrEP?",
             "An HIV test is required, along with other tests the doctor considers necessary. "
             "The doctor will issue the requests."),
            ("Do I need ongoing appointments?",
             "Yes. PrEP involves regular monitoring and repeat testing for as long as you "
             "continue taking it."),
        ],
        "related": ["sti-consultation", "contraception", "mens-health"],
    },

    # ------------------------------------------------------ weight & wellness
    {
        "slug": "weight-management",
        "nav_label": "Weight Management",
        "group": "Weight & Wellness",
        "eyebrow": "Weight Management",
        "h1": "Weight management, ",
        "h1_tail": "clinically guided",
        "title": "Weight Management Doctor Online | Your Online Doctor",
        "description": "Clinically guided weight management in South Africa - medical "
                       "assessment, nutritional support and ongoing review.",
        "lede": "Assessment first, then a plan that accounts for your health, not just your "
                "weight.",
        "intro": [
            "Weight is a clinical matter as much as a lifestyle one. Thyroid function, "
            "medication, insulin resistance, sleep and mental health all affect it, which is "
            "why an assessment comes before any plan.",
            "Through the platform a medical assessment can be combined with nutritional "
            "support from a dietitian and, where useful, exercise-based input from a "
            "biokineticist. That is the advantage of a network over a single provider.",
        ],
        "covers_title": "What this covers",
        "covers": [
            "Medical assessment relevant to weight and metabolic health",
            "Laboratory test requests where indicated",
            "Body composition assessment",
            "Nutritional support through the dietitian network",
            "Exercise-based support through the biokineticist network",
            "Ongoing review and adjustment",
        ],
        "suitability": "Any medication used in weight management is prescribed only where "
                       "clinically appropriate, after assessment, and alongside the rest of "
                       "the plan rather than instead of it.",
        "faqs": [
            ("Do you prescribe weight loss medication?",
             "Medication may be prescribed where it is clinically appropriate following a full "
             "assessment. It is not prescribed on request and not in isolation."),
            ("Will I see a dietitian as well?",
             "Nutritional support is available through the network where it would help, "
             "alongside the medical assessment."),
            ("Do I need blood tests?",
             "Often yes, because several treatable conditions affect weight. The doctor will "
             "issue requests where testing is indicated."),
        ],
        "related": ["dietitian", "biokinetics", "mens-health"],
    },
    {
        "slug": "dietitian",
        "nav_label": "Dietitian",
        "group": "Weight & Wellness",
        "eyebrow": "Dietitian",
        "h1": "Nutritional support from a ",
        "h1_tail": "dietitian",
        "title": "Online Dietitian South Africa | Your Online Doctor",
        "description": "Connect with a registered dietitian in South Africa for nutritional "
                       "assessment and eating plans, through one digital platform.",
        "lede": "Eating plans built around your health and your circumstances.",
        "intro": [
            "A dietitian works with what you actually eat, what your health requires and what "
            "is realistic in your life. It is practical work rather than generic advice.",
            "Through the platform you can be connected with a dietitian in the network, either "
            "directly or as part of a wider plan involving medical assessment and other "
            "professionals.",
            "Dietetic input matters most where nutrition and a medical condition interact - "
            "diabetes, high blood pressure, raised cholesterol, digestive conditions, "
            "pregnancy, or recovery after illness. In those situations general advice is not "
            "enough, because what you should be eating depends on what is happening "
            "clinically.",
            "It also matters where previous attempts have not worked. A dietitian looks at why "
            "an approach failed rather than prescribing a stricter version of the same thing.",
        ],
        "covers_title": "What this covers",
        "covers": [
            "Nutritional assessment",
            "Eating plans suited to your circumstances",
            "Support for weight management goals",
            "Nutrition alongside chronic conditions",
            "Ongoing review and adjustment",
        ],
        "suitability": "Dietitians work within their own scope of practice. Where a concern is "
                       "medical rather than nutritional, it is referred to a doctor.",
        "faqs": [
            ("Do I need a doctor's referral first?",
             "Not necessarily. You can be connected with a dietitian directly, though a "
             "medical assessment sometimes comes first where it would be useful."),
            ("Are dietitian consultations remote too?",
             "Yes, dietetic consultations can generally be conducted remotely."),
            ("What is the difference between a dietitian and a nutritionist?",
             "In South Africa dietitians are healthcare professionals registered with the "
             "HPCSA and can work clinically alongside medical treatment. The network uses "
             "registered dietitians."),
            ("Will I be given a strict diet to follow?",
             "The aim is a plan you can sustain given your health, your budget and how you "
             "actually live. A plan abandoned in a fortnight helps nobody."),
        ],
        "related": ["weight-management", "biokinetics", "mental-health"],
    },
    {
        "slug": "biokinetics",
        "nav_label": "Biokinetics",
        "group": "Weight & Wellness",
        "eyebrow": "Biokinetics",
        "h1": "Exercise-based ",
        "h1_tail": "rehabilitation",
        "title": "Biokineticist South Africa | Your Online Doctor",
        "description": "Connect with a biokineticist in South Africa for exercise-based "
                       "rehabilitation and conditioning through one digital platform.",
        "lede": "Structured exercise as treatment, not as a gym programme.",
        "intro": [
            "Biokineticists use exercise clinically - for rehabilitation after injury, for "
            "managing chronic conditions, and for conditioning where that is the appropriate "
            "intervention.",
            "The platform connects you with a biokineticist in the network, often alongside a "
            "medical assessment or physiotherapy where the two work together.",
            "Biokineticists are registered with the HPCSA and work largely in the final phase "
            "of rehabilitation: the point where pain has settled but strength, movement and "
            "confidence have not yet returned. Skipping that phase is a common reason "
            "injuries come back.",
            "The same applies to chronic conditions. Structured exercise is an established "
            "part of managing diabetes, hypertension and cardiac rehabilitation, and it works "
            "best when it is prescribed and progressed deliberately rather than guessed at.",
        ],
        "covers_title": "What this covers",
        "covers": [
            "Exercise-based rehabilitation",
            "Conditioning and functional assessment",
            "Support for chronic condition management",
            "Programmes coordinated with medical or physiotherapy input",
        ],
        "suitability": "Where an injury needs medical assessment or imaging first, that is "
                       "arranged before exercise-based rehabilitation begins.",
        "faqs": [
            ("What is the difference between a biokineticist and a physiotherapist?",
             "Physiotherapy generally addresses the acute phase of injury and pain; "
             "biokinetics generally addresses the rehabilitation and conditioning that "
             "follows. They often work in sequence."),
            ("Can this be done remotely?",
             "Assessment and programme guidance can often be handled remotely, with in-person "
             "sessions arranged where they are needed."),
            ("Do I need to be injured to see a biokineticist?",
             "No. Biokineticists also work on chronic condition management, conditioning, and "
             "preventing an old injury from recurring."),
            ("How long does rehabilitation take?",
             "It depends on the injury, how long it has been there, and how consistently the "
             "programme is followed. The biokineticist will set expectations after assessing "
             "you rather than beforehand."),
        ],
        "related": ["physiotherapy", "weight-management", "dietitian"],
    },

    # ----------------------------------------------------------- mental health
    {
        "slug": "mental-health",
        "nav_label": "Mental Health",
        "group": "Mental Health",
        "eyebrow": "Mental Health",
        "h1": "Mental health ",
        "h1_tail": "consultations",
        "title": "Online Mental Health Consultation | Your Online Doctor",
        "description": "Online mental health consultations in South Africa, with referral into "
                       "psychology services through a connected network.",
        "lede": "A first conversation is often the hardest part. It does not have to happen "
                "in a waiting room.",
        "intro": [
            "Mental health concerns are among the most common reasons people avoid seeking "
            "care, and the practical barriers - travel, time, being seen walking in - make it "
            "worse. A remote consultation removes most of them.",
            "A consultation covers assessment and a discussion of what would help. That may be "
            "management by the doctor, referral to a psychologist in the network, or referral "
            "to a psychiatrist where that is indicated.",
        ],
        "covers_title": "What this covers",
        "covers": [
            "Assessment of mental health concerns",
            "Discussion of appropriate next steps",
            "Referral into psychology services",
            "Specialist referral where indicated",
            "Management and follow-up where appropriate",
        ],
        "suitability": "If you are in crisis or at risk of harming yourself, this is not the "
                       "right channel. Go to your nearest emergency department or contact "
                       "emergency services immediately.",
        "faqs": [
            ("Can I speak to a psychologist through the platform?",
             "Yes. Psychology services are available through the network, either directly or "
             "following a consultation."),
            ("Is it confidential?",
             "Yes, subject to the same professional and legal obligations as any consultation."),
            ("What if I am in crisis?",
             "Do not use this platform. Go to your nearest emergency department or call your "
             "local emergency services immediately."),
        ],
        "related": ["psychology", "weight-management", "online-doctor-consultation"],
    },
    {
        "slug": "psychology",
        "nav_label": "Psychology",
        "group": "Mental Health",
        "eyebrow": "Psychology",
        "h1": "Psychology ",
        "h1_tail": "services",
        "title": "Online Psychologist South Africa | Your Online Doctor",
        "description": "Connect with a registered psychologist in South Africa for assessment "
                       "and talking therapy through one digital platform.",
        "lede": "Talking therapy with a registered psychologist, arranged through the network.",
        "intro": [
            "Psychologists provide assessment and talking therapy. The work is ongoing rather "
            "than a single appointment, and the relationship matters, which is why being "
            "matched appropriately is part of the process.",
            "Through the platform you can be connected with a psychologist in the network, "
            "either directly or following a consultation with a doctor.",
            "People come to psychology for a wide range of reasons: anxiety, low mood, grief, "
            "trauma, difficulty in a relationship, burnout, or simply a period where things "
            "stopped feeling manageable. You do not need a diagnosis to justify an "
            "appointment.",
            "A first session is largely about understanding the situation and agreeing what "
            "the work should focus on. From there it becomes a course of sessions rather than "
            "a single appointment, because change of this kind takes time.",
        ],
        "covers_title": "What this covers",
        "covers": [
            "Psychological assessment",
            "Talking therapy",
            "Support alongside medical management where relevant",
            "Onward referral where a different discipline is indicated",
        ],
        "suitability": "Psychologists and psychiatrists do different work. Where medication "
                       "assessment is indicated, referral to a psychiatrist is arranged.",
        "faqs": [
            ("Do psychologists prescribe medication?",
             "No. Psychologists provide assessment and therapy. Where medication needs to be "
             "considered, referral to a doctor or psychiatrist is arranged."),
            ("Can therapy be done remotely?",
             "Yes. Remote psychology sessions are well established and work well for many "
             "presentations."),
            ("How many sessions will I need?",
             "It varies considerably. The psychologist will discuss a likely range with you "
             "after the first session rather than committing you in advance."),
            ("Do I need a diagnosis to see a psychologist?",
             "No. Many people seek psychological support for a difficult period rather than "
             "for a diagnosed condition."),
        ],
        "related": ["mental-health", "dietitian", "online-doctor-consultation"],
    },

    # ------------------------------------------------------------------ other
    {
        "slug": "physiotherapy",
        "nav_label": "Physiotherapy",
        "group": "Other Services",
        "eyebrow": "Physiotherapy",
        "h1": "Physiotherapy and ",
        "h1_tail": "pain management",
        "title": "Physiotherapist South Africa | Your Online Doctor",
        "description": "Connect with a physiotherapist in South Africa for movement, "
                       "rehabilitation and pain management through one digital platform.",
        "lede": "Movement, rehabilitation and pain, assessed by the right professional.",
        "intro": [
            "Physiotherapists treat pain, injury and movement problems, and are often the "
            "right first professional for a musculoskeletal complaint.",
            "The platform connects you with a physiotherapist in the network. Where a "
            "complaint needs medical assessment or imaging first, that is arranged.",
            "Back and neck pain, sports injuries, joint problems, recovery after surgery, and "
            "pain that has not settled on its own are all common reasons to see one. So is "
            "pain that has been managed with painkillers for longer than it should have been.",
            "Assessment establishes what is actually driving the problem, which is often not "
            "where the pain is felt. Treatment then combines hands-on work with an exercise "
            "programme you continue between sessions, and it is usually that programme doing "
            "most of the long-term work.",
        ],
        "covers_title": "What this covers",
        "covers": [
            "Assessment of pain and movement problems",
            "Rehabilitation after injury",
            "Management of ongoing musculoskeletal conditions",
            "Coordination with medical assessment or biokinetics where useful",
        ],
        "suitability": "Hands-on treatment happens in person. Initial assessment and exercise "
                       "guidance can often be handled remotely.",
        "faqs": [
            ("Can physiotherapy be done online?",
             "Assessment and exercise guidance can often be conducted remotely. Hands-on "
             "treatment requires an in-person appointment."),
            ("Do I need a referral?",
             "Not necessarily, though a medical assessment is arranged first where the "
             "complaint warrants it."),
            ("How soon should I be seen after an injury?",
             "Generally sooner rather than later. Problems left alone tend to change how you "
             "move to compensate, and that creates further problems."),
            ("Will I need a scan?",
             "Usually not. Where imaging would genuinely change the treatment plan, a medical "
             "assessment is arranged to request it."),
        ],
        "related": ["biokinetics", "online-doctor-consultation", "weight-management"],
    },
    {
        "slug": "mobile-doctor",
        "nav_label": "Mobile Doctor",
        "group": "Other Services",
        "eyebrow": "Mobile Doctor Services",
        "h1": "Mobile ",
        "h1_tail": "doctor services",
        "title": "Mobile Doctor Service | Your Online Doctor",
        "description": "Mobile doctor services through Your Online Doctor, for situations "
                       "where a remote consultation is not enough.",
        "lede": "For when an assessment needs to happen in person, but getting to a practice "
                "is the problem.",
        "intro": [
            "Not everything can be done remotely, and not everyone can travel. Mobile doctor "
            "services cover the gap - an in-person assessment arranged where you are, rather "
            "than at a practice.",
            "Availability depends on location and on the nature of what is needed. The "
            "starting point is usually a conversation about whether this is the right option "
            "for your situation.",
        ],
        "covers_title": "What this covers",
        "covers": [
            "In-person assessment where a remote consultation is not sufficient",
            "Situations where travel to a practice is difficult",
            "Follow-up after a remote consultation where examination is needed",
            "Arrangements coordinated through the platform",
        ],
        "suitability": "Mobile services are subject to availability, location and clinical "
                       "suitability, and are not an emergency service. In an emergency, "
                       "contact emergency services.",
        "faqs": [
            ("Where is the mobile service available?",
             "Availability depends on location. Get in touch and we will tell you whether it "
             "covers your area."),
            ("Is this an emergency service?",
             "No. In an emergency, go to your nearest emergency department or call your local "
             "emergency services immediately."),
        ],
        "related": ["online-doctor-consultation", "driver-pdp-medicals", "sick-note-online"],
    },
    {
        "slug": "driver-pdp-medicals",
        "nav_label": "Driver & PDP Medicals",
        "group": "Other Services",
        "eyebrow": "Medical Assessments",
        "h1": "Driver and ",
        "h1_tail": "PDP medicals",
        "title": "Driver & PDP Medical Assessment | Your Online Doctor",
        "description": "Driver and Professional Driving Permit medical assessments in South "
                       "Africa, arranged through Your Online Doctor.",
        "lede": "The medical assessment required for a Professional Driving Permit.",
        "intro": [
            "A Professional Driving Permit requires a medical assessment confirming you are "
            "medically fit to drive professionally. It covers vision, hearing, general health "
            "and conditions that could affect driving safely.",
            "This assessment includes physical examination and therefore happens in person. "
            "The platform arranges it, and the surrounding administration can be handled "
            "remotely.",
        ],
        "covers_title": "What this covers",
        "covers": [
            "Medical assessment for a Professional Driving Permit",
            "General driver fitness assessments",
            "Vision and hearing screening as part of the assessment",
            "Completion of the required certificate where you meet the criteria",
        ],
        "suitability": "The assessment is an examination with a defined standard. If you do "
                       "not meet the criteria the certificate cannot be issued, and you will "
                       "be told what would need to change.",
        "faqs": [
            ("Can a PDP medical be done online?",
             "No. It requires a physical examination, including vision and hearing checks, so "
             "it is conducted in person. The arrangements can be made through the platform."),
            ("What should I bring?",
             "Your identity document, your driving licence, any glasses or contact lenses you "
             "use, and details of medication you take."),
            ("What if I do not pass?",
             "The doctor will explain which criterion was not met and what, if anything, could "
             "change that."),
        ],
        "related": ["mobile-doctor", "online-doctor-consultation", "sick-note-online"],
    },
]

BY_SLUG = {s["slug"]: s for s in SERVICE_PAGES}


def grouped():
    """Service pages grouped by their `group`, preserving definition order."""
    out = []
    for page in SERVICE_PAGES:
        for entry in out:
            if entry[0] == page["group"]:
                entry[1].append(page)
                break
        else:
            out.append((page["group"], [page]))
    return out
