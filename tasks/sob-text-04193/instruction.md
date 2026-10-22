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
Hospital: A hospital is a health care institution providing patient treatment with specialized medical and nursing staff and medical equipment.  The best-known type of hospital is the general hospital, which typically has an emergency department to treat urgent health problems ranging from fire and accident victims to a heart attack.  A district hospital typically is the major health care facility in its region, with large numbers of beds for intensive care and additional beds for patients who need long-term care.  Specialised hospitals include trauma centres, rehabilitation hospitals, children's hospitals, seniors' (geriatric) hospitals, and hospitals for dealing with specific medical needs such as psychiatric treatment (see psychiatric hospital) and certain disease categories.  Specialised hospitals can help reduce health care costs compared to general hospitals.

Moccasin Bend Mental Health Institute: Moccasin Bend is the site of the Moccasin Bend Mental Health Institute.  It is located on a private area of land on the Tennessee River.  It was founded in 1961 by the Tennessee State Legislature.  "Moccasin Bend Mental Health Institute is a psychiatric hospital in Chattanooga, Tennessee, with 150 beds.  Survey data for the latest year available shows that the hospital had a total of 2,340 admissions." .  The hospital was built into five different buildings.  The first building was built in 1961.  "A local architect, Mario Bianculli, designed the majority of the buildings at the Moccasin Bend Mental Health Institute.  Considered “Chattanooga’s First Modernist,” Bianculli was a pioneer of modern architecture in Tennessee and the southeastern United States."  The hospital specializes in psychiatric care.

Providence Hospital (Washington, D.C.): Providence Hospital is a 408 bed hospital located in the District of Columbia.  Founded in 1861, it is the longest continuously operating hospital in the District.  Providence Hospital is a member of Ascension Health, the largest non-profit health care organization in the United States.

Varberg Hospital: Varberg Hospital (Swedish: "Sjukhuset i Varberg", literally "The Hospital in Varberg") is a hospital in Varberg, Sweden.  The hospital was completed in 1972, as a replacement of the old hospital in the city.  After that, the old hospital was demolished.  Varberg Hospital has 450 beds for general medical care and 350 beds for psychiatric treatment.

New York State Psychiatric Institute: The New York State Psychiatric Institute, located in the Columbia University Medical Center in the Washington Heights neighborhood of Manhattan, New York City, was established in 1895 as one of the first institutions in the United States to integrate teaching, research and therapeutic approaches to the care of patients with mental illnesses.  In 1925, the Institute affiliated with Presbyterian Hospital, now New York-Presbyterian Hospital, adding general hospital facilities to the Institute's psychiatric services and research laboratories.

John Markowitz: John C. Markowitz (born 1954 in New York City) is an American physician, a Professor of Clinical Psychiatry at the Columbia University College of Physicians & Surgeons and a Psychiatric Researcher at the New York State Psychiatric Institute.  For several decades he has conducted research on psychotherapies and medications as treatments for mood disorders (major depressive disorder and dysthymic disorder), anxiety disorders, and personality disorders.  He is currently conducting an outcome study of three psychotherapies for Posttraumatic Stress Disorder (PTSD) thanks to a five year grant from the National Institute of Mental Health.  He is most widely published in the area of interpersonal psychotherapy or IPT, a manualized form of treatment, in which he was trained by the late Gerald L. Klerman, M.D. Dr. Markowitz is a graduate of Columbia University and Columbia University College of Physicians and Surgeons and received his psychiatric residency training at the Payne Whitney Psychiatric Clinic of Cornell University Medical School/New York-Presbyterian Hospital.

Legacy Holladay Park Medical Center: Legacy Holladay Park Medical Center is a hospital located in Portland, Oregon, United States.  It was founded in 1893 as Hahnemann Hospital.  By 1947 the hospital had 100 beds, and that year it changed its name to Holladay Park Hospital with plans to expand to 200 beds.  With a 1985 merger with Physicians & Surgeons Hospital (which had been known as Coffey Memorial Hospital until 1945), the name was changed to Holladay Park Medical Center.  At that time both hospitals were part of Metropolitan Hospitals, Inc. that had been formed by Physicians & Surgeons Hospital and Emanuel Hospital.  After becoming part of Legacy Health when it was formed in 1989, Legacy closed the then 171-bed hospital in 1994.  As of 2014, the former hospital was used by Legacy as the Legacy Research Institute.  Legacy proposed converting the building into an emergency room for psychiatric patients in 2014 after the Legacy Research Institute moved to a new building.  Legacy, Oregon Health & Science University, Adventist Health, and Kaiser Permanente agreed to operate the ER, with a planned opening in 2016.

Psychiatric Institute of Washington: The Psychiatric Institute of Washington (PIW) is an acute (104 bed) psychiatric hospital in Washington, D.C. Opened in 1967, PIW is a short-term, private hospital.  It offers behavioral healthcare to patients suffering from mental and addictive illnesses, including children, adolescents, adults and the elderly.  Services offered by PIW include inpatient, partial and intensive outpatient hospitalization, and group treatment programs for substance abuse and addiction.

St. Brendan's Hospital, Dublin: St. Brendan's Hospital was a psychiatric facility located in the north Dublin suburb of Grangegorman.  It formed part of the HSE mental health services of Dublin North East.  Its catchment area is North West Dublin.  Since the official opening of the Richmond Lunatic Asylum in 1815 the Grangegorman site has continuously provided institutional facilities for the reception of the mentally ill until the present day.  The majority of the buildings historically associated with the hospital have been either demolished, fallen into disrepair or closed down.  There are currently five wards still in use in the facility which are all situated in old buildings and which provide eighty-four beds for psychiatric patients.  In the 2008 "Report" of the Inspector of Mental Health Services it was recommended that acute admissions to the secure units 3A and 3B should cease due to their unsuitability and all admissions should be redirected to the new purpose built unit at Connolly Hospital, Blanchardstown, Dublin.  This new acute psychiatric unit was finally opened in Connolly Hospital on 29 November 2010 allowing for the commencement of the transfer of patients from St. Brendan's to Blanchardstown.  This is part of a process that will see all the old units at St. Brendan's retired as psychiatric facilities.  However, this does not signal the end of the use of the site for the provision of mental health services.  As part of the Grangegorman Development Plan, where a large portion of the site of the old hospital will be used to develop a new Dublin Institute of Technology campus, new modern psychiatric facilities are to be provided for the HSE mental health services for the region.

Providence St. Peter Hospital: Providence St. Peter Hospital, located in the Lilly Road Medical District of Olympia, Washington is Providence Health & Services’s second largest Washington state hospital.  Providence St. Peter features 390 beds in the medical/surgical tower with 42 private rooms in the emergency department (including a four-bed locked mental health evaluation unit), 18 beds in the Psychiatry Building, and 32 beds in the Critical Care Unit.  This facility is a non-profit teaching hospital founded by the Sisters of Providence in 1887.  Providence St. Peter Hospital offers comprehensive medical, surgical and behavioral health services.

Question: Which hospital has more beds, Providence Hospital or Psychiatric Institute of Washington?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "hospital_comparison": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "hospital_name": {
            "type": "string"
          },
          "number_of_beds": {
            "type": "integer"
          }
        },
        "required": [
          "hospital_name",
          "number_of_beds"
        ],
        "additionalProperties": false
      }
    },
    "hospital_with_more_beds": {
      "type": "string"
    },
    "bed_difference": {
      "type": "integer"
    }
  },
  "required": [
    "hospital_comparison",
    "hospital_with_more_beds",
    "bed_difference"
  ],
  "additionalProperties": false
}
