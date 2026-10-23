{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nOrel VH2 Streamline: The Orel VH2 Streamline is a French ultralight aircraft that was designed by Jean-Francois Boudet and is under development by Orel Aircraft of Selles-Saint-Denis, introduced at the AERO Friedrichshafen show in 2015.  The aircraft will be supplied complete and ready-to-fly.\n\nAeroJames 01 Isatis: The AeroJames 01 Isatis (named for the flowering plant) is a French ultralight aircraft, designed and produced by AeroJames of Ajaccio, Corsica.  It was introduced at the Aero show held in Friedrichshafen in 2009.  The aircraft is supplied as a complete ready-to-fly-aircraft.\n\nHoude Bimax: The Houde Bimax is a French ultralight aircraft, designed and produced by Patrice Houde, introduced at the Blois homebuilt aircraft fly-in in September 2010.  The aircraft is supplied as a complete ready-to-fly-aircraft.\n\nHumbert La Moto Du Ciel: The Humbert La Moto Du Ciel (English: \"Motorbike of the Sky\" ) is a French ultralight aircraft, designed and produced by Humbert Aviation of Ramonchamp, introduced in the mid-1980s.  The aircraft is supplied as a complete ready-to-fly-aircraft.\n\nAirbus: Airbus SE ( , ] , ] , ] ) is a European multinational corporation that designs, manufactures, and sells civil and military aeronautical products worldwide.  In addition to its primary civil aeroplane business, the company has two divisions for other products and services: \"Defence and Space\" and \"Helicopters\", the latter being the largest in its industry in terms of revenues and turbine helicopter deliveries.\n\nAero Synergie Jodel D20: The Aero Synergie Jodel D20 is a French ultralight aircraft that was designed by Jean Délémontez and produced by Aero Synergie of Villefranche-de-Rouergue.  The aircraft was supplied as a kit for amateur construction or as a completed aircraft.\n\nSanstroem Friendship 3: The Friendship 3 is a French ultralight aircraft with tandem seats, engineered in France and Switzerland, and assembled in Czech Republic by Ivanov Aircraft for the manufacturer, R,S & Associes SAS Erik Sanstroem of Versailles, Yvelines.  Inspired by 1950s and 1960s light aircraft and motorgliders, the Friendship 3 is a two-place tandem-seat ultralight aircraft with dual controls, so that the rear seated passenger can also fly.\n\nAeroflying Sensation: The Aeroflying Sensation is a French ultralight aircraft, designed by former Airbus engineer Jose Verges and produced by Aeroflying of Saint-André-des-Eaux, Loire-Atlantique.  It was introduced at the French Hombuilders Rally in Blois in 2007.  The aircraft is supplied as a kit for amateur construction or as a complete ready-to-fly-aircraft.\n\nAero Synergie J300 Joker: The Aero Synergie J300 Joker is a French ultralight aircraft that was designed and produced by Sauper/ALMS and later by Aero Synergie.  The aircraft was supplied as a kit for amateur construction and also as a complete ready-to-fly aircraft.\n\nApollo Ultralight Aircraft: Apollo Ultralight Aircraft is a Hungarian aircraft manufacturer based in Eger.  The company specializes in the design and manufacture of ultralight aircraft, gyroplanes and ultralight trikes, in the form of kits for amateur construction and ready-to-fly aircraft for the European Fédération Aéronautique Internationale microlight and the American light-sport aircraft categories.\n\nQuestion: A European multinational corporation that designs, manufactures, and sells civil and military aeronautical products worldwide introduced a French ultralight aircraft that was designed by former employee?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"designer_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the aircraft designer.\"\n    },\n    \"aircraft_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"aircraft_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the ultralight aircraft.\"\n        },\n        \"aircraft_type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of aircraft.\"\n        },\n        \"manufacturer\": {\n          \"type\": \"string\",\n          \"description\": \"The company that produces the aircraft.\"\n        },\n        \"country_of_origin\": {\n          \"type\": \"string\",\n          \"description\": \"The country of origin of the aircraft.\"\n        }\n      },\n      \"required\": [\n        \"aircraft_name\",\n        \"aircraft_type\",\n        \"manufacturer\",\n        \"country_of_origin\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"former_employer_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"company_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the former employer.\"\n        },\n        \"company_description\": {\n          \"type\": \"string\",\n          \"description\": \"A description of the former employer's business.\"\n        }\n      },\n      \"required\": [\n        \"company_name\",\n        \"company_description\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"designer_name\",\n    \"aircraft_details\",\n    \"former_employer_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "designer_name": {
        "type": "string",
        "description": "The name of the aircraft designer."
      },
      "aircraft_details": {
        "type": "object",
        "properties": {
          "aircraft_name": {
            "type": "string",
            "description": "The name of the ultralight aircraft."
          },
          "aircraft_type": {
            "type": "string",
            "description": "The type of aircraft."
          },
          "manufacturer": {
            "type": "string",
            "description": "The company that produces the aircraft."
          },
          "country_of_origin": {
            "type": "string",
            "description": "The country of origin of the aircraft."
          }
        },
        "required": [
          "aircraft_name",
          "aircraft_type",
          "manufacturer",
          "country_of_origin"
        ],
        "additionalProperties": false
      },
      "former_employer_details": {
        "type": "object",
        "properties": {
          "company_name": {
            "type": "string",
            "description": "The name of the former employer."
          },
          "company_description": {
            "type": "string",
            "description": "A description of the former employer's business."
          }
        },
        "required": [
          "company_name",
          "company_description"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "designer_name",
      "aircraft_details",
      "former_employer_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
