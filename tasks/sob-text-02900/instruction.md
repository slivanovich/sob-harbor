{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAgnes Body: Agnes Body (29 April, 1866 – 31 March, 1952) was a British headmistress.  She was the founding head of Lincoln Christ's Hospital Girls' High School and Queen Margaret's School, then in Scarborough.\n\nBrisbane State High School: Brisbane State High School (BSHS or often commonly State High or High) is a partially selective, co-educational, state secondary school, located in South Brisbane, Queensland, Australia.  It is a member of the Great Public Schools' Association of Queensland, and the Queensland Girls' Secondary Schools Sports Association.  It was the first state secondary school established in Brisbane, as well as the first academic state high school to be founded in Queensland.  The school employs a variety of selection criteria for prospective students, maintaining a quota for local area enrolments, however also using academic, sporting, cultural and artistic talents as means of determining the annual intake.  In 2017, there were 3,190 students in Years 7–12.\n\nDr James Burty David SSS: Dr James Burty David State Secondary School is a state secondary school based in Bell Village, Port Louis, Mauritius.  Students are prepared for the School Certificate and the Higher School Certificate.  The school was previously known as the Bell Village SSS.\n\nQueen Margaret Academy: Queen Margaret Academy (Scottish Gaelic: \"àrd-sgoil/Acadamh banrigh Maighread\" ) is a Roman Catholic secondary school in the south of Ayr in southwest Scotland.  Queen Margaret is state-run by South Ayrshire Council and takes children aged 11 to 18 from the whole of South Ayrshire and parts of East Ayrshire.\n\nLincoln Christ's Hospital School: Lincoln Christ's Hospital School is a state secondary school with academy status located on \"Wragby Road\" in Lincoln, Lincolnshire, England.\n\nOxford Academy, Oxfordshire: The Oxford Academy is a co-educational state secondary school in Littlemore, Oxford, England.  Formerly Peers School, it was re-opened as an Academy in September 2008 and is the state secondary school for The Leys, Rose Hill and Littlemore.  It has specialist status in mathematics, computing, and sport.\n\nCambridge High School (New Zealand): Cambridge High School is a state secondary school in the Waikato town of Cambridge.  Cambridge High School is a co-educational state secondary school, students from the town and surrounding rural areas attend the school.  The school is a large part of the Cambridge community, participating in a wide network of formal and informal relationships with other agencies and groups.\n\nIES Jaume Vicens Vives: Jaume Vicens Vives Secondary School (\"Institut Jaume Vicens Vives\" in catalan) is a Catalan state secondary school located in the city of Girona (Spain).  It has around of 900 pupils from ages 12 to 18 studying the Spanish secondary education programs (ESO from 12 to 16, and LOE Baccalaureate from 16 to 18).  It is the only state secondary school in Catalonia to offer the International Baccalaureate.\n\nAdolphe de Plevitz SSS: Adolphe de Plevitz State Secondary School is a state secondary school based in Grand-Baie, Mauritius.  Students are prepared for the School Certificate and the Higher School Certificate.\n\nCastlemaine Secondary College: Castlemaine Secondary College is a state secondary school located in the town of Castlemaine in central Victoria, Australia.  It was attended by Sean Finning, gold medallist of the 2006 Melbourne Commonwealth Games.  It is the only state secondary school in the Mount Alexander Shire.\n\nQuestion: Where is the location of the state secondary school Agnes Body was the founding head of (Apart from Queen Margaret's School)?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"school_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the state secondary school.\"\n    },\n    \"founding_head_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the founding head of the school.\"\n    },\n    \"location\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"street_address\": {\n          \"type\": \"string\",\n          \"description\": \"The specific street address of the school.\"\n        },\n        \"city\": {\n          \"type\": \"string\",\n          \"description\": \"The city where the school is located.\"\n        },\n        \"county_or_region\": {\n          \"type\": \"string\",\n          \"description\": \"The county or region where the school is located.\"\n        },\n        \"country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the school is located.\"\n        }\n      },\n      \"required\": [\n        \"street_address\",\n        \"city\",\n        \"county_or_region\",\n        \"country\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"school_name\",\n    \"founding_head_name\",\n    \"location\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "school_name": {
        "type": "string",
        "description": "The name of the state secondary school."
      },
      "founding_head_name": {
        "type": "string",
        "description": "The name of the founding head of the school."
      },
      "location": {
        "type": "object",
        "properties": {
          "street_address": {
            "type": "string",
            "description": "The specific street address of the school."
          },
          "city": {
            "type": "string",
            "description": "The city where the school is located."
          },
          "county_or_region": {
            "type": "string",
            "description": "The county or region where the school is located."
          },
          "country": {
            "type": "string",
            "description": "The country where the school is located."
          }
        },
        "required": [
          "street_address",
          "city",
          "county_or_region",
          "country"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "school_name",
      "founding_head_name",
      "location"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
