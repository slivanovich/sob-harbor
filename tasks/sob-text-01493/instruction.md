{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nHM Prison Pentonville: HM Prison Pentonville (informally \"The Ville\") is an English Category B/C men's prison, operated by Her Majesty's Prison Service.  Pentonville Prison is not in Pentonville, but is located further north, on the Caledonian Road in the Barnsbury area of the London Borough of Islington, north London.\n\nHM Prison Rye Hill: HM Prison Rye Hill is a Category B men's private prison, operated by G4S.  Rye Hill has exclusively housed sex offenders since 2014.  The prison is situated next to HMP Onley, in the parish of Barby, Northamptonshire, England.  However, the postal address of the prison is Willoughby, Warwickshire; therefore, most sources list the prison as in Willoughby, Warwickshire.\n\nHM Prison Bure: Her Majesty's Prison Bure, more commonly known as HM Prison Bure, and often abbreviated to HMP Bure, is a Category C men's prison, located in the parish of Scottow in Norfolk, England.  The prison is operated by Her Majesty's Prison Service, and became operational in November 2009.\n\nHM Prison Wormwood Scrubs: HM Prison Wormwood Scrubs (informally \"The Scrubs\") is a Category B men's prison, located in the Wormwood Scrubs area of the London Borough of Hammersmith and Fulham, in inner west London, England.  The prison is operated by Her Majesty's Prison Service.\n\nKirkham, Lancashire: Kirkham (originally Kirkam-in-Amounderness) is a small town and civil parish in the Borough of Fylde in Lancashire, England, midway between Blackpool and Preston (11 miles west of Preston) and adjacent to the smaller town of Wesham.  It owes its existence to Carr Hill upon which it was built and which was the location of a Roman fort.  It has a population of 7,127, increasing to 7,194 at the Census 2011.\n\nHM Prison Kirkham: HM Prison Kirkham is a Category D men's prison, located southwest of Kirkham in Lancashire, England.  The prison is operated by Her Majesty's Prison Service.\n\nHM Prison Acklington: HM Prison Acklington was a Category C men's prison, located near the village of Acklington a few miles from Amble), in Northumberland, England.  Acklington Prison was operated by Her Majesty's Prison Service.  In 2011 Acklington was merged into the newly named HM Prison Northumberland.\n\nHM Prison Isis: HM Prison Isis is a Category C male Young Offenders Institution, located in the Thamesmead area of the Royal Borough of Greenwich, in south-east London, England.  Isis Prison is operated by Her Majesty's Prison Service, and is situated next to Belmarsh Prison and Thameside Prison.\n\nHM Prison Moorland: HM Prison Moorland (formerly HM Prison Moorland Closed) is a Category C men's prison and Young Offenders Institution, near Hatfield Woodhouse in South Yorkshire, England.  The prison is operated by Her Majesty's Prison Service, and is jointly managed with the nearby Hatfield Prison.\n\nHM Prison Kennet: HM Prison Kennet is a Category C men's prison, located in Parkbourn, Maghull, in the Metropolitan Borough of Sefton in Merseyside, England.  The prison is operated by Her Majesty's Prison Service.  The prison is due to close in 2017.\n\nQuestion: HM Prison Kirkham is a Category D men's prison, located southwest of which small town, and civil parish in the Borough of Fylde?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"prison_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the prison.\"\n    },\n    \"prison_category\": {\n      \"type\": \"string\",\n      \"description\": \"The category of the prison (e.g., Category D).\"\n    },\n    \"located_relative_to\": {\n      \"type\": \"string\",\n      \"description\": \"Description of the prison's location relative to the town.\"\n    },\n    \"town_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"town_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the small town.\"\n        },\n        \"is_civil_parish\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the town is also a civil parish.\"\n        },\n        \"borough\": {\n          \"type\": \"string\",\n          \"description\": \"The borough the town is located in.\"\n        },\n        \"county\": {\n          \"type\": \"string\",\n          \"description\": \"The county the town is located in.\"\n        }\n      },\n      \"required\": [\n        \"town_name\",\n        \"is_civil_parish\",\n        \"borough\",\n        \"county\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"prison_name\",\n    \"prison_category\",\n    \"located_relative_to\",\n    \"town_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "prison_name": {
        "type": "string",
        "description": "The name of the prison."
      },
      "prison_category": {
        "type": "string",
        "description": "The category of the prison (e.g., Category D)."
      },
      "located_relative_to": {
        "type": "string",
        "description": "Description of the prison's location relative to the town."
      },
      "town_details": {
        "type": "object",
        "properties": {
          "town_name": {
            "type": "string",
            "description": "The name of the small town."
          },
          "is_civil_parish": {
            "type": "boolean",
            "description": "Indicates if the town is also a civil parish."
          },
          "borough": {
            "type": "string",
            "description": "The borough the town is located in."
          },
          "county": {
            "type": "string",
            "description": "The county the town is located in."
          }
        },
        "required": [
          "town_name",
          "is_civil_parish",
          "borough",
          "county"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "prison_name",
      "prison_category",
      "located_relative_to",
      "town_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
