{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nFilitelnic gas field: The Filitelnic gas field is a natural gas field in the Filitelnic village of Bălăuşeri commune, Mureş County, Romania lying in the center of the Transylvanian Basin, a major natural gas producing region.  It was discovered in 1958 and is developed by Romgaz.  It began production in 1961 and produces natural gas and condensates.  The total proven reserves of the Filitelnic gas field are around 2.145 e12cuft , and production is around 143 e6cuft/d .  The Filitelnic gas field is the second largest natural gas field in Romania.\n\nKangan gas field: The Kangan gas field is an Iranian natural gas field that was discovered in 1967.  It began production in 1980 and produces natural gas and condensates.  The total proven reserves of the Kangan gas field are around 29 trillion cubic feet (829×10m) and production is slated to be around 800 million cubic feet/day (23×10m).  Nar gas field is located a few kilometers away from kangan gas field.  That's why Nar & Kangan appear together most of the time.  The produced gas from Nar & Kangan fields delivers to Fajr gas refinery in the downstream.  Nar & Kangan is the major onshore natural gas provider for domestic consumption.  The two fields together hold the record of maximum gas production rate from onshore fields in Iran, 120 million cubic meter/day (MMSCMD).\n\nFrigg gas field: Frigg gas field is a natural gas field on Norwegian block 25/1 in the North Sea, on the boundary between the United Kingdom and Norway.  The field is named after the goddess Frigg.  King Olav V of Norway officially opened production on 8 May 1978.  Production was closed on 26 October 2004.  The field is situated 230 km northwest of Stavanger.  Operator for the field was the French oil company Elf Aquitaine, which merged and changed name to Total S.A.\n\nLa Goleta Gas Field: The La Goleta Gas Field (also known as the Goleta Gas Field and La Goleta Storage Field) is a natural gas field in unincorporated Santa Barbara County, California, adjacent to the city of Goleta.  Discovered in 1929, and first put into production in 1932, it has been in continuous use ever since, producing approximately 12 billion cubic feet of gas.  With production declining, the field was converted into a gas storage reservoir in 1941.  As of 2016 it remains one of the four gas storage facilities maintained by Southern California Gas Company (SoCalGas), a division of Sempra Energy, with the others being Aliso Canyon, Honor Rancho and Playa del Rey.  It is the oldest storage facility of the four and the third largest, with a maximum capacity of 21.5 billion cubic feet.  The storage facilities are necessary to balance load for the over ten million customers of SoCalGas: during summer months, when gas usage is at a minimum, gas is pumped into the reservoirs; and in the winter when usage is high, gas is withdrawn.  The La Goleta field serves the northern portion of SoCalGas's geographic range.\n\nLira gas field: The Lira gas field natural gas field is located on the continental shelf of the Black Sea.  It was discovered in 2016 and developed by Lukoil and Romgaz.  The total proven reserves of the Lira gas field are around 1.11 trillion cubic feet (32 km).  This gas discovery is the second largest in the Romanian sector of the Black Sea after Petrom and ExxonMobil's Domino gas field.\n\nBovanenkovo gas field: The Bovanenkovo gas field is a natural gas field located in the Yamalo-Nenets Autonomous Okrug.  It was discovered in 1972 and developed by Gazprom.  It began production in 2012 and produces natural gas and condensates.  The total proven reserves of the Bovanenkovo gas field are around 171.5 trillion cubic feet (4900×10m³), and production is stated to be around 11 billion cubic feet/day (314×10m³) in 2010.  The Bovanenkovo gas field is part of the Yamal project.\n\nLeviathan gas field: The Leviathan gas field is a large natural gas field located in the Mediterranean Sea off the coast of Israel, 47 km south-west of the Tamar gas field.  The gas field is located roughly 130 km west of Haifa in waters 1500 m deep in the Levantine basin, a rich hydrocarbon area in one of the world's larger offshore gas finds of the past decade.  According to some commentators, the gas find has the potential to change Israel's foreign relations with neighboring countries Turkey, and Egypt.  Together with the nearby Tamar gas field, the Leviathan field is seen as an opportunity for Israel to become a major energy player in the Middle East.  As of 2017, even by conservative estimates, Leviathan holds enough gas to meet Israel's domestic needs for 40 years.\n\nZohr Field: The Zohr gas field is an offshore natural gas field located in the Egyptian sector of the Mediterranean Sea.  The field is located in the Shorouk concession, a concession with an area of 3765 km2 , which was won by Eni in 2013 The field is estimated to lie in an area of 100 km2 and it is located at a depth of 1450 m .  The field was discovered in 2015 by the Italian energy company Eni and is the largest ever natural gas find in the Mediterranean Sea, almost twice the size of the nearby Leviathan gas field.  The total gas in place of the Zohr gas field is around 850 e9m3 .  If true, Zohr will almost double Egypt's gas reserves.\n\nNatural gas in Romania: Romania has proven natural gas reserves of 726 billion cubic meters (25.94 trillion cubic feet) and is ranked 30th among countries with proved reserves of natural gas.  About 75% of Romania's natural gas resources are located in Transylvania, especially in Mureş and Sibiu counties.  The largest natural gas field in Romania is the Deleni gas field discovered in 1912 and located in the Băgaciu commune in Mureş County with proven reserves of 85 billion cubic meters or 3 trillion cubic feet.  Other important gas fields include the Filitelnic gas field (40 bcm - 1,430 bcft), the Roman-Secuieni gas field (24 bcm - 850 bcft), the Voitinel gas field (11.8 bcm - 415 bcft), the Gherceşti gas field (11 bcm - 400 bcft) and the Sărmaşel gas field (10 bcm - 354 bcft) all with reserves larger than 10 billion cubic meters or 350 billion cubic feet.  Currently Romania has the third largest natural gas reserves in the European Union just after the Netherlands and United Kingdom.\n\nOlav V of Norway: Olav V (born Prince Alexander of Denmark; 2 July 1903 – 17 January 1991) was King of Norway from 1957 until his death.\n\nQuestion: Which King of Norway, born in 1903 officially opened Frigg Gas Field?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"king_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the King of Norway.\"\n        },\n        \"birth_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The birth year of the King.\"\n        },\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title held by the individual.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"birth_year\",\n        \"title\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"gas_field_event\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"field_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the gas field involved in the event.\"\n        },\n        \"event_description\": {\n          \"type\": \"string\",\n          \"description\": \"Description of the event related to the gas field.\"\n        },\n        \"event_date\": {\n          \"type\": \"string\",\n          \"description\": \"The date when the event occurred.\"\n        }\n      },\n      \"required\": [\n        \"field_name\",\n        \"event_description\",\n        \"event_date\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"final_answer\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the King who officially opened the Frigg Gas Field.\"\n    }\n  },\n  \"required\": [\n    \"king_details\",\n    \"gas_field_event\",\n    \"final_answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "king_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the King of Norway."
          },
          "birth_year": {
            "type": "integer",
            "description": "The birth year of the King."
          },
          "title": {
            "type": "string",
            "description": "The title held by the individual."
          }
        },
        "required": [
          "name",
          "birth_year",
          "title"
        ],
        "additionalProperties": false
      },
      "gas_field_event": {
        "type": "object",
        "properties": {
          "field_name": {
            "type": "string",
            "description": "The name of the gas field involved in the event."
          },
          "event_description": {
            "type": "string",
            "description": "Description of the event related to the gas field."
          },
          "event_date": {
            "type": "string",
            "description": "The date when the event occurred."
          }
        },
        "required": [
          "field_name",
          "event_description",
          "event_date"
        ],
        "additionalProperties": false
      },
      "final_answer": {
        "type": "string",
        "description": "The name of the King who officially opened the Frigg Gas Field."
      }
    },
    "required": [
      "king_details",
      "gas_field_event",
      "final_answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
