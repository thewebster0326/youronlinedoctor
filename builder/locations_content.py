"""Location landing page content.

Google treats city pages that are find-and-replace on a place name as doorway
pages and demotes them. So each page below carries genuinely local substance -
the actual geography, the actual reason travelling to a practice is difficult
in that specific place - rather than the same paragraph with the city swapped.

Accuracy rules followed:
  - the service is remote; nothing here implies rooms or staff in a city
  - suburb lists describe where patients are, not where we have premises
  - no invented statistics
"""

LOCATION_PAGES = [
    {
        "slug": "online-doctor-johannesburg",
        "image": "city-johannesburg",
        "image_alt": "The Johannesburg skyline",
        "nav_label": "Johannesburg",
        "place": "Johannesburg",
        "region": "Gauteng",
        "eyebrow": "Online Doctor Johannesburg",
        "h1": "Online doctor in ",
        "h1_tail": "Johannesburg",
        "title": "Online Doctor Johannesburg | Your Online Doctor",
        "description": "Consult a doctor online from anywhere in Johannesburg. Remote "
                       "consultations, prescriptions and referrals without the commute.",
        "lede": "Consultations from Sandton to Soweto, without giving up half a day to "
                "traffic.",
        "intro": [
            "Johannesburg is a city built around driving, and that is exactly the problem "
            "when you are unwell. A GP appointment that takes fifteen minutes can cost two "
            "hours once you add the drive across town, parking and the wait.",
            "The city's sprawl makes this worse than in a denser city. Someone living in "
            "Fourways and working in the CBD may be nowhere near their usual practice during "
            "the hours it is open, and the M1 at the wrong time of day turns a short trip "
            "into a long one.",
            "A remote consultation removes the journey entirely. You speak to a doctor from "
            "home, from the office, or from wherever you happen to be, and the outcome - "
            "advice, a prescription, a certificate, a referral - is the same as it would be "
            "in a consulting room, where that is clinically appropriate.",
        ],
        "areas_title": "Patients across Johannesburg",
        "areas": [
            "Sandton", "Rosebank", "Randburg", "Fourways", "Midrand", "Soweto",
            "Roodepoort", "Bryanston", "Melville", "Parktown", "Johannesburg CBD",
            "Northcliff", "Greenside", "Edenvale", "Bedfordview", "Lenasia",
        ],
        "angle_title": "Why remote care suits this city",
        "angle": [
            "Distance and traffic are the practical barriers in Johannesburg, not a shortage "
            "of doctors. Removing the journey solves most of it.",
            "It also helps with the hours. Work in this city often does not release people "
            "during standard consulting times, and a remote consultation can be arranged "
            "around that rather than against it.",
        ],
        "faqs": [
            ("Do I need to be in Johannesburg to use the service?",
             "No. Consultations are conducted remotely and are available to patients "
             "anywhere in South Africa. Johannesburg is simply where many of our patients "
             "are."),
            ("Is there a practice I can visit in Johannesburg?",
             "Your Online Doctor is a digital platform and consultations take place "
             "remotely. Where an in-person examination is needed, you will be referred "
             "appropriately."),
            ("Can I collect a prescription from a pharmacy near me?",
             "Yes. A prescription issued after a consultation can be taken to the pharmacy "
             "of your choice."),
        ],
        "services": ["online-doctor-consultation", "sick-note-online", "prescriptions-online"],
        "locations": ["online-doctor-pretoria", "online-doctor-gauteng", "online-doctor-cape-town"],
    },
    {
        "slug": "online-doctor-pretoria",
        "image": "city-pretoria",
        "image_alt": "The Union Buildings in Pretoria",
        "nav_label": "Pretoria",
        "place": "Pretoria",
        "region": "Gauteng",
        "eyebrow": "Online Doctor Pretoria",
        "h1": "Online doctor in ",
        "h1_tail": "Pretoria",
        "title": "Online Doctor Pretoria | Your Online Doctor",
        "description": "Consult a doctor online anywhere in Pretoria and Tshwane. Remote "
                       "consultations, prescriptions and referrals, wherever you are.",
        "lede": "Consultations across Tshwane, from Centurion to Mamelodi, without leaving "
                "your desk.",
        "intro": [
            "Pretoria is where Your Online Doctor is registered, and a large share of our "
            "patients are here. It is a city with a particular working rhythm: a great many "
            "people are employed in government departments, at the universities, or in the "
            "office parks around Menlyn and Centurion, in roles that do not make it easy to "
            "disappear for a mid-morning appointment.",
            "Tshwane is also geographically wide. A patient in Soshanguve and a patient in "
            "Centurion are a long way apart, and public transport between the outer areas "
            "and the practices concentrated in the older suburbs is not quick.",
            "Consulting remotely removes that gap. The assessment, and whatever follows from "
            "it, happens wherever you are.",
        ],
        "areas_title": "Patients across Tshwane",
        "areas": [
            "Pretoria CBD", "Hatfield", "Arcadia", "Brooklyn", "Menlyn", "Centurion",
            "Silverton", "Waterkloof", "Lynnwood", "Mamelodi", "Soshanguve",
            "Atteridgeville", "Montana", "Wonderboom", "Akasia", "Garsfontein",
        ],
        "angle_title": "Why remote care suits this city",
        "angle": [
            "Pretoria's working population is heavily concentrated in offices and "
            "institutions with fixed hours. Appointments that do not require travel fit that "
            "pattern far better.",
            "Our registered address is at G16 Barclays Square Shopping Centre, Celliers Street, "
            "Pretoria. It "
            "is a business address rather than a walk-in clinic - consultations are conducted "
            "remotely.",
        ],
        "faqs": [
            ("Are you based in Pretoria?",
             "Our registered business address is in Pretoria. It is not a walk-in clinic - "
             "consultations are conducted remotely."),
            ("Can I be seen in person in Pretoria?",
             "Where an examination is required you will be referred appropriately. Mobile "
             "doctor services are also available subject to location and availability."),
            ("Do you serve Centurion and the wider Tshwane area?",
             "Yes. Consultations are remote, so the whole of Tshwane is covered, along with "
             "the rest of South Africa."),
        ],
        "services": ["online-doctor-consultation", "mobile-doctor", "driver-pdp-medicals"],
        "locations": ["online-doctor-johannesburg", "online-doctor-gauteng", "online-doctor-durban"],
    },
    {
        "slug": "online-doctor-cape-town",
        "image": "city-cape-town",
        "image_alt": "Cape Town beneath Table Mountain",
        "nav_label": "Cape Town",
        "place": "Cape Town",
        "region": "Western Cape",
        "eyebrow": "Online Doctor Cape Town",
        "h1": "Online doctor in ",
        "h1_tail": "Cape Town",
        "title": "Online Doctor Cape Town | Your Online Doctor",
        "description": "Consult a doctor online anywhere in Cape Town and the Western Cape. "
                       "Remote consultations, prescriptions and referrals.",
        "lede": "From the City Bowl to the Cape Flats and out to the Northern Suburbs.",
        "intro": [
            "Cape Town is shaped by its geography in a way few South African cities are. The "
            "mountain and the coastline divide it into areas that are close as the crow flies "
            "and slow to travel between in practice, and the N1 and N2 concentrate most of "
            "that movement into a few corridors.",
            "The result is that where you live determines how easy it is to reach a doctor. "
            "Someone in Khayelitsha or Mitchells Plain may face a considerably longer journey "
            "to a private practice than someone in Claremont, for the same appointment.",
            "Remote consultations do not depend on any of that. The doctor assesses you from "
            "wherever you are, and the outcome does not change according to which side of the "
            "mountain you happen to live on.",
        ],
        "areas_title": "Patients across the Cape Peninsula",
        "areas": [
            "Cape Town CBD", "Sea Point", "Green Point", "Claremont", "Rondebosch",
            "Wynberg", "Constantia", "Bellville", "Durbanville", "Brackenfell",
            "Parow", "Goodwood", "Mitchells Plain", "Khayelitsha", "Muizenberg",
            "Table View", "Milnerton", "Somerset West",
        ],
        "angle_title": "Why remote care suits this city",
        "angle": [
            "Cape Town's travel times are driven by geography and by a small number of "
            "congested routes. A consultation that requires no journey sidesteps both.",
            "It also matters for the outer areas. Where private practices are unevenly "
            "distributed, remote access narrows the gap between one suburb and the next.",
        ],
        "faqs": [
            ("Do you have doctors in Cape Town?",
             "Consultations are conducted remotely by healthcare professionals registered to "
             "practise in South Africa, and are available to patients in Cape Town along with "
             "the rest of the country."),
            ("Can I get a prescription filled at a Cape Town pharmacy?",
             "Yes. A prescription issued after a consultation can be taken to the pharmacy of "
             "your choice."),
            ("What if I need to be examined?",
             "The doctor will tell you and refer you to appropriate in-person care. That "
             "judgement is made in every consultation."),
        ],
        "services": ["online-doctor-consultation", "prescriptions-online", "mental-health"],
        "locations": ["online-doctor-johannesburg", "online-doctor-durban", "telehealth-south-africa"],
    },
    {
        "slug": "online-doctor-durban",
        "image": "city-durban",
        "image_alt": "The Umhlanga lighthouse near Durban",
        "nav_label": "Durban",
        "place": "Durban",
        "region": "KwaZulu-Natal",
        "eyebrow": "Online Doctor Durban",
        "h1": "Online doctor in ",
        "h1_tail": "Durban",
        "title": "Online Doctor Durban | Your Online Doctor",
        "description": "Consult a doctor online anywhere in Durban and KwaZulu-Natal. Remote "
                       "consultations, prescriptions and referrals.",
        "lede": "Across eThekwini and the KwaZulu-Natal coast, without the drive.",
        "intro": [
            "Durban spreads a long way along the coast and inland, and the distance between "
            "where people live and where private practices cluster can be substantial. The "
            "journey from the outer areas into Berea or Umhlanga for a short appointment is "
            "a real deterrent.",
            "It is also a city where a great deal of work happens around the port, in "
            "logistics and in shift-based industries. Those hours rarely line up neatly with "
            "standard consulting times.",
            "A remote consultation solves both problems at once: no journey, and a time that "
            "can be arranged around a shift rather than in spite of it.",
        ],
        "areas_title": "Patients across eThekwini and the coast",
        "areas": [
            "Durban CBD", "Berea", "Umhlanga", "Westville", "Pinetown", "Hillcrest",
            "Kloof", "Chatsworth", "Phoenix", "Amanzimtoti", "Glenwood", "Morningside",
            "Musgrave", "Queensburgh", "Verulam", "Ballito", "Umdloti", "Bluff",
        ],
        "angle_title": "Why remote care suits this city",
        "angle": [
            "Shift work and long travel distances are the two practical barriers here. "
            "Neither applies to a consultation conducted remotely.",
            "The same is true of the wider KwaZulu-Natal coast and the inland areas, where "
            "the distance to a private practice can be considerably greater than it is in "
            "the metro.",
        ],
        "faqs": [
            ("Is the service available across KwaZulu-Natal?",
             "Yes. Consultations are remote and available anywhere in South Africa, including "
             "the wider KwaZulu-Natal province."),
            ("Can I consult outside normal working hours?",
             "Your Online Doctor is designed to provide convenient and extended access, "
             "subject to service availability and clinical suitability."),
            ("What happens if I need a specialist?",
             "The doctor can refer you into the network of healthcare professionals, "
             "including medical specialists, where that is clinically indicated."),
        ],
        "services": ["online-doctor-consultation", "sick-note-online", "womens-health"],
        "locations": ["online-doctor-cape-town", "online-doctor-johannesburg", "telehealth-south-africa"],
    },
    {
        "slug": "online-doctor-gauteng",
        "image": "city-gauteng",
        "image_alt": "A Gauteng skyline at sunset",
        "nav_label": "Gauteng",
        "place": "Gauteng",
        "region": "Gauteng",
        "eyebrow": "Online Doctor Gauteng",
        "h1": "Online doctor in ",
        "h1_tail": "Gauteng",
        "title": "Online Doctor Gauteng | Your Online Doctor",
        "description": "Consult a doctor online anywhere in Gauteng - Johannesburg, Tshwane, "
                       "Ekurhuleni, the West Rand and Sedibeng.",
        "lede": "One province, three metros, and a great deal of commuting between them.",
        "intro": [
            "Gauteng is the smallest South African province by area and the most populous, "
            "which produces a particular pattern: enormous numbers of people moving daily "
            "between the places they live and the places they work.",
            "For healthcare that creates an awkward mismatch. Your home may be in Ekurhuleni, "
            "your office in Sandton and your usual GP somewhere near neither, and the "
            "practice's opening hours may fall entirely within the part of the day you spend "
            "on the other side of the province.",
            "Consulting remotely removes the geography from the equation. It does not matter "
            "which of the three metros you are in, or whether you are in the West Rand or "
            "Sedibeng - the consultation happens where you are.",
        ],
        "areas_title": "Across the province",
        "areas": [
            "City of Johannesburg", "City of Tshwane", "Ekurhuleni", "West Rand",
            "Sedibeng", "Sandton", "Centurion", "Benoni", "Boksburg", "Kempton Park",
            "Krugersdorp", "Roodepoort", "Vereeniging", "Vanderbijlpark", "Springs",
            "Alberton",
        ],
        "angle_title": "Why remote care suits this province",
        "angle": [
            "Gauteng's defining healthcare problem is not distance to a city - it is the "
            "daily separation between home, work and the practice you are registered with.",
            "A remote consultation is indifferent to all three. For a province built on "
            "commuting, that is the point.",
        ],
        "faqs": [
            ("Which parts of Gauteng do you cover?",
             "All of it. Consultations are remote, so Johannesburg, Tshwane, Ekurhuleni, the "
             "West Rand and Sedibeng are equally covered, as is the rest of South Africa."),
            ("Is there a difference between your Johannesburg and Pretoria service?",
             "No. The service is identical wherever you are; those pages simply speak to the "
             "particular circumstances of each city."),
            ("Can I be referred to a specialist in Gauteng?",
             "Specialist referral is available through the network where it is clinically "
             "indicated."),
        ],
        "services": ["online-doctor-consultation", "weight-management", "mens-health"],
        "locations": ["online-doctor-johannesburg", "online-doctor-pretoria", "telehealth-south-africa"],
    },
    {
        "slug": "telehealth-south-africa",
        "image": "telehealth",
        "image_alt": "A stethoscope beside a mobile phone",
        "nav_label": "Telehealth South Africa",
        "place": "South Africa",
        "region": "South Africa",
        "eyebrow": "Telehealth",
        "h1": "Telehealth in ",
        "h1_tail": "South Africa",
        "title": "Telehealth South Africa | Your Online Doctor",
        "description": "What telehealth is, how remote consultations work in South Africa, "
                       "and what they can and cannot do.",
        "lede": "Healthcare delivered remotely - what that actually means, and where its "
                "limits are.",
        "intro": [
            "Telehealth is the delivery of healthcare using communications technology instead "
            "of an in-person visit. In practice that usually means a consultation conducted "
            "over a call or a video link, with the same history-taking and clinical reasoning "
            "that would happen in a consulting room.",
            "In South Africa remote consultation moved from the margins to the mainstream "
            "quickly, and the Health Professions Council of South Africa has published "
            "guidance on how practitioners should conduct it. The professional and legal "
            "obligations are the same as for any consultation: registration, confidentiality, "
            "record-keeping and scope of practice all apply unchanged.",
            "What differs is the absence of a physical examination. That is the real "
            "boundary, and it is what determines whether a given concern can be handled "
            "remotely or needs to be seen.",
        ],
        "areas_title": "What telehealth handles well",
        "areas": [
            "Common conditions and everyday illness", "Follow-up consultations",
            "Repeat and chronic medication review", "Questions about medication",
            "Mental health consultations", "Sexual health and contraception",
            "Weight and lifestyle management", "Test results and next steps",
            "Specialist referral", "Laboratory test requests",
        ],
        "angle_title": "Where it stops",
        "angle": [
            "Anything requiring hands-on examination, imaging or urgent intervention is not "
            "suited to remote consultation. Nor is an emergency - in an emergency, go to your "
            "nearest emergency department or call your local emergency services immediately.",
            "A responsible telehealth service says so plainly and refers you on. Every "
            "consultation includes that judgement, and being told you need to be seen in "
            "person is a normal outcome rather than a failure of the process.",
        ],
        "faqs": [
            ("Is telehealth legal in South Africa?",
             "Yes. Remote consultation is an accepted mode of practice, and the HPCSA has "
             "published guidance for practitioners on conducting it."),
            ("Is a telehealth consultation as good as seeing a doctor in person?",
             "For many concerns it is equivalent. For anything needing physical examination "
             "or imaging it is not, and in those cases you are referred for in-person care."),
            ("Do the same confidentiality rules apply?",
             "Yes. The same professional and legal obligations apply as to an in-person "
             "consultation."),
            ("Can telehealth be used in an emergency?",
             "No. In an emergency, go to your nearest emergency department or call your local "
             "emergency services immediately."),
        ],
        "services": ["online-doctor-consultation", "prescriptions-online", "mental-health"],
        "locations": ["online-doctor-johannesburg", "online-doctor-cape-town", "online-doctor-durban"],
    },
]

BY_SLUG = {p["slug"]: p for p in LOCATION_PAGES}
