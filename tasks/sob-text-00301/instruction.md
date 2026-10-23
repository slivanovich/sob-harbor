{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nUnited States Senate election in Hawaii, 1992: The 1992 United States Senate election in Hawaii took place on November 3, 1992 alongside other elections to the United States Senate in other states as well as elections to the United States House of Representatives and various state and local elections.  Incumbent Democrat U.S. Senator Daniel Inouye won re-election to a sixth term.\n\nBrian Schatz: Brian Emanuel Schatz (pronounced ; born October 20, 1972) is an American politician who is the senior United States Senator for Hawaii.  Schatz was appointed by Governor Neil Abercrombie to replace Senator Daniel Inouye after his death in 2012.\n\nLorraine Inouye: Lorraine Rodero Inouye (born June 22, 1940) is an American politician from the state of Hawaii.  A member of the Democratic Party, she serves in the Hawaii State Senate, representing District 4.  She is of no relation to prominent U.S. senator from Hawaii Daniel Inouye.\n\nElectoral history of Daniel Inouye: This is a list of results for elections in which Daniel Inouye, a Democrat.  He was elected Hawaii's first U.S. Representative in 1959, and was first elected to the U.S. Senate in 1962.  He served until his death in 2012.  Inouye is the 2nd longest-serving senator in history.\n\nUnited States Senate election in Hawaii, 1998: The 1998 United States Senate election in Hawaii took place on November 3, 1998 alongside other elections to the United States Senate in other states as well as elections to the United States House of Representatives and various state and local elections.  Incumbent Democrat U.S. Senator Daniel Inouye won re-election to a seventh term.\n\nOren E. Long: Oren Ethelbirt Long (March 4, 1889 – May 6, 1965), was the tenth Territorial Governor of Hawaii and served from 1951 to 1953.  A member of the Democratic Party of Hawaii, Long was appointed to the office after the term of Ingram Stainback.  After statehood was achieved he served in the United States Senate, one of the first two, along with Hiram Fong, to represent Hawaii in that body.  Long was the only non-Asian American U.S. Senator from Hawaii until the appointment of Brian Schatz to the position in 2012.\n\nUSS Daniel Inouye: USS \"Daniel Inouye\" (DDG-118) will be an \"Arleigh Burke\"-class destroyer of the United States Navy.  The ship will be named to honor former United States Senator Daniel Inouye of Hawaii.  Inouye was awarded the Medal of Honor for his actions in Tuscany, Italy, during World War II.\n\nPatrick H. DeLeon: Patrick Henry (Pat) DeLeon (born January 6, 1943) is an American psychologist, former chief of staff for United States Senator Daniel Inouye and past president of the American Psychological Association (APA).  He became an aide for Senator Inouye in 1973, when Inouye served on a committee investigating the Watergate scandal, and remained on the senator's staff for 38 years.  After DeLeon's daughter survived meningitis in 1984, he was involved in the establishment of the Emergency Medical Services for Children program.  DeLeon helped to create the nursing and pharmacy schools at the University of Hawaii at Hilo.\n\nUnited States Senate election in Hawaii, 2004: The 2004 United States Senate election in Hawaii took place on November 2, 2004 alongside other elections to the United States Senate in other states as well as elections to the United States House of Representatives and various state and local elections.  Incumbent Democrat U.S. Senator Daniel Inouye won re-election to an eighth term.\n\nInouye Marksmanship Center: The Inouye Marksmanship Center is a 12,000 square foot shooting range located on the campus of The Citadel, The Military College of South Carolina in Charleston, South Carolina.  It is home to NCAA Division I The Citadel Bulldogs rifle team, as well as the club pistol team, The Citadel's ROTC programs, and the South Carolina National Guard.  The range is named for Senator Daniel Inouye, who secured federal funding for the facility in 2002.\n\nQuestion: What non-Asian American U.S. Senator from Hawaii was appointed to replace Senator Daniel Inouye after his death?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"replaced_senator_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the senator who was replaced.\"\n        },\n        \"state_represented\": {\n          \"type\": \"string\",\n          \"description\": \"The state the replaced senator represented.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"state_represented\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"successor_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the senator who succeeded the replaced senator.\"\n        },\n        \"appointment_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the successor was appointed.\"\n        },\n        \"ethnicity_descriptor\": {\n          \"type\": \"string\",\n          \"description\": \"A descriptor for the successor's ethnicity as mentioned in the context.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"appointment_year\",\n        \"ethnicity_descriptor\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"succession_type\": {\n      \"type\": \"string\",\n      \"description\": \"The method by which the successor took office (e.g., 'appointed').\"\n    }\n  },\n  \"required\": [\n    \"replaced_senator_details\",\n    \"successor_details\",\n    \"succession_type\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "replaced_senator_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the senator who was replaced."
          },
          "state_represented": {
            "type": "string",
            "description": "The state the replaced senator represented."
          }
        },
        "required": [
          "name",
          "state_represented"
        ],
        "additionalProperties": false
      },
      "successor_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the senator who succeeded the replaced senator."
          },
          "appointment_year": {
            "type": "integer",
            "description": "The year the successor was appointed."
          },
          "ethnicity_descriptor": {
            "type": "string",
            "description": "A descriptor for the successor's ethnicity as mentioned in the context."
          }
        },
        "required": [
          "name",
          "appointment_year",
          "ethnicity_descriptor"
        ],
        "additionalProperties": false
      },
      "succession_type": {
        "type": "string",
        "description": "The method by which the successor took office (e.g., 'appointed')."
      }
    },
    "required": [
      "replaced_senator_details",
      "successor_details",
      "succession_type"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
