{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nHoward University Hospital: Howard University Hospital, previously known as Freedmen's Hospital, is a major hospital lcated in Washington, D.C., built on the site of the previous Griffith Stadium.  The hospital has served the African American community in the area for over 150 years, having been established in 1862 to cater for the medical needs of the thousands of African Americans who came to Washington during the Civil War, seeking their freedom.  The first hospital of its kind to provide medical treatment for former slaves, it later became the major hospital for the area's African-American community.  Following the closure of D.C. General Hospital, As of 2016, the hospital has the highest rate of wrongful death lawsuits of any health facility in Washington D.C. over the previous decade.\n\nPsychiatric Institute of Washington: The Psychiatric Institute of Washington (PIW) is an acute (104 bed) psychiatric hospital in Washington, D.C. Opened in 1967, PIW is a short-term, private hospital.  It offers behavioral healthcare to patients suffering from mental and addictive illnesses, including children, adolescents, adults and the elderly.  Services offered by PIW include inpatient, partial and intensive outpatient hospitalization, and group treatment programs for substance abuse and addiction.\n\nThe New Freedmen's Clinic: The New Freedmen's Clinic (first opened in the summer of 2009) is a free student-run health care clinic affiliated with Howard University Hospital (HUH) and Howard University College of Medicine (HUCM).  It gets its name from HUH's original name - Freedmen's Hospital.  It is currently located in the heart of Washington, DC, within HUH.\n\nMartin University Hospital: The Martin University Hospital (Slovak: \"Univerzitná nemocnica Martin\" , abbreviated to UNM) is a Slovak public university hospital located in the Martin municipality, in the county of Zilina, north-east of the Slovak capital Bratislava.  It is a teaching hospital and it is the main university hospital affiliated with the Jessenius School of Medicine.  The hospital has over 1,700 employees.  Martin University Hospital has 900 beds in total including all sectors.\n\nNew York State Psychiatric Institute: The New York State Psychiatric Institute, located in the Columbia University Medical Center in the Washington Heights neighborhood of Manhattan, New York City, was established in 1895 as one of the first institutions in the United States to integrate teaching, research and therapeutic approaches to the care of patients with mental illnesses.  In 1925, the Institute affiliated with Presbyterian Hospital, now New York-Presbyterian Hospital, adding general hospital facilities to the Institute's psychiatric services and research laboratories.\n\nUniversity Hospital (Augusta, Georgia): University Hospital is a non-profit 581-bed private hospital located in downtown Augusta, Georgia.  Established in 1818, it is the second-oldest hospital in Georgia.  Although University Hospital is considered a teaching institution, it does not currently sponsor an academic program resulting in a degree.  University Hospital is no longer directly affiliated with the Medical College of Georgia or Augusta University.  University Hospital is a fully private hospital receiving no local or state funding.\n\nKamuzu Central Hospital: Kamuzu Central Hospital is a teritary referral hospital in the Lilongwe, Malawi.  It is estimated to have 600-1,000 beds, though the true number of patients always exceeds the number of beds.  It serves approximately 5 million people.  It has a partnership with the University of North Carolina in the United States and a partnership project, called MAGNET (Malawi German Networking for Capacity Building in Treatment, Training and Research at Kamuzu Central Hospital), with the Institute of Public Health of the University Hospital Heidelberg in Germany, the University Hospital Cologne and the University Hospital Bonn.\n\nSouthend University Hospital NHS Foundation Trust: Southend University Hospital NHS Foundation Trust (also known as Southend University Hospital and commonly referred to as Southend Hospital) is an NHS hospital located in Westcliff-on-Sea, Southend-on-Sea, Essex, England.  Southend University Hospital has 157 consultants providing various services, and serves a catchment area with a population of about 350,000.  It has officially been designated cancer centre status, and has also gained NHS Foundation Trust status under the name Southend University Hospital NHS Foundation Trust.  More importantly Southend University Hospital is home to Funky Towers, broadcasting across Southend and surrounding areas, 103.7 on your dial, keep it real, keep it funky.\n\nOslo University Hospital, Ullevål: Oslo University Hospital, Ullevål (Norwegian: \"Oslo universitetssykehus, Ullevål\" ), formerly Ullevål University Hospital (Norwegian: \"Ullevål universitetssykehus\" ) in Oslo, Norway is one of the four main campuses of Oslo University Hospital.  It was opened in 1887, and was an independent hospital owned by Oslo municipality and then by the state until it became part of Oslo University Hospital in 2009.  It is the largest hospital in Norway.\n\nJohn Markowitz: John C. Markowitz (born 1954 in New York City) is an American physician, a Professor of Clinical Psychiatry at the Columbia University College of Physicians & Surgeons and a Psychiatric Researcher at the New York State Psychiatric Institute.  For several decades he has conducted research on psychotherapies and medications as treatments for mood disorders (major depressive disorder and dysthymic disorder), anxiety disorders, and personality disorders.  He is currently conducting an outcome study of three psychotherapies for Posttraumatic Stress Disorder (PTSD) thanks to a five year grant from the National Institute of Mental Health.  He is most widely published in the area of interpersonal psychotherapy or IPT, a manualized form of treatment, in which he was trained by the late Gerald L. Klerman, M.D. Dr. Markowitz is a graduate of Columbia University and Columbia University College of Physicians and Surgeons and received his psychiatric residency training at the Payne Whitney Psychiatric Clinic of Cornell University Medical School/New York-Presbyterian Hospital.\n\nQuestion: Which hospital was establish almost a century before the other, Howard University Hospital or the Psychiatric Institute of Washington?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"hospital_comparison\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"hospital_name\": {\n            \"type\": \"string\"\n          },\n          \"establishment_year\": {\n            \"type\": \"integer\"\n          }\n        },\n        \"required\": [\n          \"hospital_name\",\n          \"establishment_year\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"earlier_hospital_name\": {\n      \"type\": \"string\"\n    },\n    \"year_difference\": {\n      \"type\": \"integer\",\n      \"description\": \"The difference in years between the establishment of the two hospitals.\"\n    },\n    \"is_almost_a_century_difference\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if the difference in years is approximately 100 years.\"\n    }\n  },\n  \"required\": [\n    \"hospital_comparison\",\n    \"earlier_hospital_name\",\n    \"year_difference\",\n    \"is_almost_a_century_difference\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
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
            "establishment_year": {
              "type": "integer"
            }
          },
          "required": [
            "hospital_name",
            "establishment_year"
          ],
          "additionalProperties": false
        }
      },
      "earlier_hospital_name": {
        "type": "string"
      },
      "year_difference": {
        "type": "integer",
        "description": "The difference in years between the establishment of the two hospitals."
      },
      "is_almost_a_century_difference": {
        "type": "boolean",
        "description": "True if the difference in years is approximately 100 years."
      }
    },
    "required": [
      "hospital_comparison",
      "earlier_hospital_name",
      "year_difference",
      "is_almost_a_century_difference"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
