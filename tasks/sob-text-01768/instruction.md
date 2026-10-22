Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Universal health care: Universal health care, (also referred to as universal health coverage, universal coverage, universal care or socialized health care) usually refers to a health care system that provides health care and financial protection to all citizens of a particular country.  It is organized around providing a specified package of benefits to all members of a society with the end goal of providing financial risk protection, improved access to health services, and improved health outcomes.  Universal health care is not one-size-fits-all and does not imply coverage for all people for everything.  Universal health care can be determined by three critical dimensions: who is covered, what services are covered, and how much of the cost is covered.  It is described by the World Health Organization as a situation where citizens can access health services without incurring financial hardship.  U.N. member states have agreed to work toward worldwide universal health coverage by 2030.

GeoAccess, Inc.: GeoAccess, Inc. was the company that pioneered the use of geographic data to analyze the accessibility of health care networks.  Prior to GeoAccess’ work in the early 1990s, the accessibility of health care networks was estimated by comparing zip codes of health care providers and consumers.  GeoAccess developed software applications which allowed the accessibility of health care networks to be accurately measured based on the geographic coordinates of health care provider locations.  For the first time, employers and government-sponsored programs could establish access standards to take the actual accessibility of health care providers into account when selecting health care networks.  By the mid-1990s, GeoAccess-based analysis was the industry standard for measuring the accessibility of health care networks.

Covenant Health System: Covenant Health System is an American health care provider which serves West Texas and Eastern New Mexico.  It has about 1,300 beds in its five primary acute-care and specialty hospitals; it also manages about a dozen affiliated community hospitals.  Covenant Health System, part of the St. Joseph Health System, also maintains a network of family health care and medical clinics.  Covenant Health System's major facilities are Covenant Medical Center, Covenant Specialty Hospital, and Covenant Women's and Children's Hospital.  The health system also includes some 20 clinics and 50 physician practices, and its extensive outreach programs target isolated rural communities with mobile services.  Covenant Health was founded in 1998 through the merger of two of Lubbock's health care facilities, St. Mary of the Plains Hospital and the Lubbock Methodist Hospital System.

Paul M. Ellwood Jr.: Paul M. Ellwood Jr. (born 16 July 1926) is a prominent figure in American health care.  Often referred to as the "father of the health maintenance organization," he not only coined the term, he also played a role in bringing about structural changes to the American health care system to simultaneously control cost and promote health by replacing fee-for-service with prepaid, comprehensive care.  The term "HMO" was coined by Dr. Paul M. Ellwood Jr. in a January 1970 Fortune Magazine article.  More recently, he has advanced an agenda for monitoring health outcomes, so that patients, providers, and payers can make health care decisions based on real information about what treatments and providers are actually effective.

American Health Line: American Health Line is a daily health care policy briefing which "covers the coverage".  It is published by the Advisory Board Company from its headquarters in Washington, DC.  It was previously under the auspices of "National Journal".

Margot Sanger-Katz: Margot Sanger-Katz is an American health care journalist who currently works for "the New York Times", where she is a domestic correspondent, and covers health care for the Times' Upshot blog.  Prior to joining the Times, she worked for "National Journal" and the "Concord Monitor".  She has also worked at "Yale Alumni Magazine" as a senior staff editor, and at "Legal Affairs" as an associate editor.

Health Net: Health Net, Inc. is an American health care insurance provider.  HMO, POS, insured PPO and government contracts subsidiaries provide health benefits to approximately 5.9 million individuals in all 50 states and the District of Columbia through group, individual, Medicare, Medicaid, Tricare and Veterans Affairs programs.  Health Net's behavioral health services subsidiary, MHN, provides behavioral health, substance abuse and employee assistance programs (EAPs) to approximately 7.3 million individuals in various states, including the company's own health plan members.  The company's subsidiaries also offer managed health care products related to prescription drugs, and offer managed health care product coordination for multi-region employers and administrative services for medical groups and self-funded benefits programs.  St. Louis-based Centene announced in July that it plans to buy Health Net for $6.8 billion.

Primary Care Behavioral health: Primary Care Behavioral Health Consultation model (PCBH) is a psychological approach to population-based clinical health care that is simultaneously co-located, collaborative, and integrated within the primary care clinic.  The goal of PCBH is to improve and promote overall health within the general population.  This approach is important because approximately half of all patients in primary care present with psychiatric comorbidities, and 60% of psychiatric illness is treated in primary care.  Primary Care practice has traditionally adopted a generalist approach whereby physicians are trained in the medical model and solutions to problems typically involve medications, procedures, and advice.  Appointment times are short, with the goal of seeing a large number of patients in a day.  Many patients present with mental health care needs whose symptomology may overlap with medical disorders and which may exacerbate, complicate, or masquerade as physical symptoms.  In addition, many medical problems present with associated psychological sequelae (e.g. stress, emotional reactions, dysfunctional lifestyle behaviors), that are amenable to change, through behavioral intervention, that can improve outcomes for these health problems.  Over 50% of medical visits to primary care clinics today are related to chronic medical conditions (e.g. chronic pain, diabetes, COPD, hypertension, obesity).  As we learn more and more about the contributing factors to the development and maintenance of these medical problems, there is growing evidence that the PCBH model affords us the opportunity for early identification and behavioral/medical intervention that can prevent some acute problems from becoming chronic health care problems.  Behavioral Health Consultants (BHCs) work side-by-side with all members of the clinical care team (including primary care providers (PCPs) and nursing staff) to enhance preventive and clinical care for mental health problems that have traditionally been treated solely by physicians.  The role of the BHC is to facilitate systemic change within primary care that facilitates a multidisciplinary approach both from a treatment and reimbursement standpoint.  BHCs typically collaborate with physicians to develop treatment plans, monitor patient progress, and flexibly provide care to meet patients’ changing needs In this review the terms Primary Care Behavioral Health Consultation and Behavioral Health Consultation will be used interchangeably.

Concord Monitor: The Concord Monitor is the daily newspaper for Concord, the state capital of New Hampshire.  It also covers surrounding towns in Merrimack, most of Belknap county, as well as portions of Grafton, Rockingham and Hillsborough counties.  The "Monitor" has several times been named as one of the best small papers in America and in April 2008, the "Monitor" became a Pulitzer Prize winning paper, when photographer Preston Gannaway was honored for feature photography.

Lives at Risk: Lives at Risk is a book about modern health care systems.  It examines the flaws of current health care systems and proposes reforms for the American health care system.  In doing so it examines twenty common assumptions about government involvement in health care systems which they argue are myths.  The book continues on to discuss the economics and politics behind health care in the United States, and proposes market based reforms.

Question: Margot Sanger-Katz is an American health care journalist who currently works for which organization, prior to joining the Times, she worked for "National Journal" and the "Concord Monitor"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "journalist_name": {
      "type": "string",
      "description": "The name of the health care journalist."
    },
    "profession": {
      "type": "string",
      "description": "The profession of the individual."
    },
    "current_employer": {
      "type": "string",
      "description": "The organization the journalist currently works for."
    },
    "previous_employers": {
      "type": "array",
      "description": "A list of organizations the journalist worked for prior to their current role.",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "journalist_name",
    "profession",
    "current_employer",
    "previous_employers"
  ],
  "additionalProperties": false
}
