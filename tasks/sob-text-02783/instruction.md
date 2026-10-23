{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe British School – Al Khubairat: The British School Al Khubairat, formerly called \"Al Khubairat Community School\", now commonly known and referred to as \"Al Khubairat\", \"BSAK\", \"The British School\" is a non-profit school for English speaking children in Abu Dhabi, United Arab Emirates.  The school roll is some 1,800 students.\n\nBritish School Muscat: British School Muscat (BSM) is a non-profit, co-educational, British international day school in Muscat, Oman, that provides a comprehensive education to English-speaking expatriate pupils aged 3–18.  The school follows an enhanced version of the English National Curriculum.  British School Muscat was established in 1971 when it was granted a Royal Charter by His Majesty Sultan Qaboos bin Said.\n\nThe British School, Panchkula: The British School in Panchkula near Chandigarh, India is an international school, affiliated to the University of Cambridge International Examination.  The second extension of this school in Chandigarh Tricity is located at Sector 70, Mohali.  The British School was offering International General Certificate of Secondary education certification till 2015.  Now the school has switched over to CBSE pattern till class Xth =.  The IGCSE Examination is conducted by the University of Cambridge International Examination (CIE).  Students prepare for the IB Diploma Programme.\n\nInternational British School of Bucharest: International British School of Bucharest (abbreviated IBSB; formerly Fundatia International British School of Bucharest) is a British school in Bucharest, Romania.  The school was established in September 2000.\n\nAndrew Ballard: He was educated at Rossall School, St John's College, Durham and Westcott House, Cambridge.  He was ordained in 1969.  After curacies at St Mary's, Bryanston Square and St Mary's Portsea, the largest parish in that city, he held incumbencies in Haslingden, Walkden, Little Hulton and Farnworth before his appointment as Archdeacon.\n\nBritish School of Ulaanbaatar: The British School of Ulaanbaatar (BSU) in Ulaanbaatar, Mongolia is a private international school, which offers an educational program from Pre-school to Year 13 (UK) for students of all nationalities wishing to study a British school curriculum.\n\nThe British School Warsaw: The British School Warsaw is an international school in Warsaw, Poland.  It was established in 1992 and currently has over 1200 students with 60 different nationalities.  The British School, Warsaw is part of Nord Anglia Education Group.  The school follows the English National Curriculum, adapted to the needs of the international student community, from Early Years to the Primary and Secondary Key Stages, the IGCSE examinations and a well established International Baccalaureate (IB) Diploma Programme.  The Principal of the school is Alun Yorath.  The teaching staff are recruited from overseas and are primarily UK trained.  The British School offers education to students aged 2 ½ to 18 years.\n\nBritish School Jakarta: The British School of Jakarta (BSJ) is an independent school in Pondok Aren, South Tangerang in Greater Jakarta, Indonesia.  The British School of Jakarta is an international member of the Headmasters' and Headmistresses' Conference.  It was established in Jakarta in 1973 under the auspices of the British Embassy.  The main campus was relocated to Bintaro in 1994 to accommodate increasing numbers of students, and an early years centre was opened in Pondok Indah in 1999.  The school offers classes for students from pre-school to year 13 based on a British curriculum, with the final two years covered by the International Baccalaureate diploma program.\n\nRossall School: Rossall School is a British, fee paying co-educational, independent school, between Cleveleys and Fleetwood, Lancashire.  Rossall was founded in 1844 by St. Vincent Beechey as a sister school to Marlborough College which had been founded the previous year.  Its establishment was \"to provide, at a moderate cost, for the sons of Clergymen and others, a classical, mathematical and general education of the highest class, and to do all things necessary, incidental, or conducive to the attainment of the above objects.\"\n\nBritish School of Beijing: The British School of Beijing, Shunyi () is an international school in Shunyi District, Beijing, China.  Nord Anglia Education operates this school, situated in the residential area of Shunyi and taking pupils from 18 months through to 18 years of age (Pre-Nursery students through to Sixth form college), along with its sister school, The British School of Beijing, Sanlitun (), based in the central Embassy district of Sanlitun and caters for students from the age of 2 to 11 years old.\n\nQuestion: Which British school was founded in 1844 and attended by Andrew Ballard?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"school_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the school.\"\n        },\n        \"founding_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the school was founded.\"\n        },\n        \"school_type\": {\n          \"type\": \"string\",\n          \"description\": \"A description of the school's type or characteristics.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"founding_year\",\n        \"school_type\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"person_attended\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the person who attended the school.\"\n        },\n        \"attended_school_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the school the person attended.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"attended_school_name\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"identified_school_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the British school that matches both criteria.\"\n    }\n  },\n  \"required\": [\n    \"school_details\",\n    \"person_attended\",\n    \"identified_school_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "school_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the school."
          },
          "founding_year": {
            "type": "integer",
            "description": "The year the school was founded."
          },
          "school_type": {
            "type": "string",
            "description": "A description of the school's type or characteristics."
          }
        },
        "required": [
          "name",
          "founding_year",
          "school_type"
        ],
        "additionalProperties": false
      },
      "person_attended": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the person who attended the school."
          },
          "attended_school_name": {
            "type": "string",
            "description": "The name of the school the person attended."
          }
        },
        "required": [
          "name",
          "attended_school_name"
        ],
        "additionalProperties": false
      },
      "identified_school_name": {
        "type": "string",
        "description": "The name of the British school that matches both criteria."
      }
    },
    "required": [
      "school_details",
      "person_attended",
      "identified_school_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
