{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nIshtar Gate: The Ishtar Gate (Arabic: بوابة عشتار‎ ‎ , Persian: دروازه ایشتار‎ ‎ ) was the eighth gate to the inner city of Babylon.  It was constructed in about 575 BCE by order of King Nebuchadnezzar II on the north side of the city.  It was excavated in the early 20th century and a reconstruction using original bricks is now shown in the Pergamon Museum, Berlin.\n\nPergamon (album): Pergamon (1986), originally simply released as Tangerine Dream (1980) with two parts \"Quichotte\" - Part one and two, is the third live album and fourteenth overall by Tangerine Dream.  It is a selection from the two live concerts held on 31 January 1980 at the Palast der Republik in East Berlin.  The second of the two original concerts is available as \"Tangerine Tree Volume 17: East Berlin 1980\".  The original title \"Quichotte\" is a reference to Don Quixote, a film version of which was being screened in a nearby cinema as one of the concerts was performed, while the retitle is a reference to the Pergamon Museum located in East Berlin near the Palast der Republik.\n\nMshatta Facade: The Mshatta Facade is the decorated part of the facade of the 8th century Umayyad residential palace of Qasr Mshatta, one of the Desert Castles of Jordan, which is now installed in the south wing of the Pergamon Museum in Berlin, Germany.  It is part of the permanent exhibition of the Pergamon Museum of Islamic Art dedicated to Islamic art from the 8th to the 19th centuries.  This was only a relatively small section of the full length of the facade, surrounding the main entrance; most of the wall was undecorated and remains \"in situ\".\n\nStefan Weber (Orientalist): Stefan Weber (October 17, 1967, in Aachen) is a German Orientalist and director of the Museum of Islamic Art (\"Museum für Islamische Kunst\") at the Pergamon Museum in Berlin, Germany.  Previously, he was assistant professor of material history at the Institute for the Study of Muslim Civilisations of Aga Khan University in London.\n\nEdmund de Unger: Edmund Robert Anthony de Unger (Hungarian: \"Odon Antal Robert de Unger\" , b 6 August 1918, Budapest - d 25 January 2011, Ham, Surrey) was a Hungarian-born property developer and art collector.  In London he built up the Keir Collection, one of the greatest post-war collections of Islamic art, bequeathed in 2008 to the Pergamon Museum of Islamic Art in Berlin.  The arrangement for the museum to curate the collection came to an end in July 2012.  The collection is now hosted by the Dallas Museum of Art as of May 2014 for a 15-year renewable loan.\n\nAntikensammlung Berlin: The Antikensammlung Berlin (Berlin antiquities collection) is one of the most important collections of classical art in the world, now held in the Altes Museum and Pergamon Museum in Berlin, Germany.  It contains thousands of ancient archaeological artefacts from the ancient Greek, Roman, Etruscan and Cypriot civilizations.  Its main attraction is the Pergamon Altar and Greek and Roman architectural elements from Priene, Magnesia, Baalbek and Falerii.  In addition, the collection includes a large number of ancient sculptures, vases, terracottas, bronzes, sarcophagi, engraved gems and metalwork.\n\nVorderasiatisches Museum Berlin: The Vorderasiatisches Museum (] , \"Near East Museum\") is an archaeological museum in Berlin.  It is in the basement of the south wing of the Pergamon Museum and has one of the world's largest collections of Southwest Asian art. 14 halls distributed across 2,000 square meters of exhibition surface display southwest Asian culture spanning six millennia.  The exhibits cover a period from the 6th millennium BCE into the time of the Muslim conquests.  They originate particularly from today's states of Iraq, Syria and Turkey, with singular finds also from other areas.  Starting with the Neolithic finds, the emphasis of the collection is of finds from Sumer, Babylonia and Assyria, as well as northern Syria and eastern Anatolia.\n\nMarket Gate of Miletus: The Market Gate of Miletus (German: \"das Markttor von Milet\" ) is a large marble monument in the Pergamon Museum in Berlin, Germany.  It was built in Miletus in the 2nd century AD and destroyed in an earthquake in the 10th or 11th century.  In the early 1900s, it was excavated, rebuilt, and placed on display in the museum.  Only fragments had survived and reconstruction involved significant new material, a practice which generated criticism of the museum.  The gate was damaged in World War II and underwent restoration in the 1950s.  Further restoration work took place in the first decade of the 21st century.\n\nPergamon Museum: The Pergamon Museum (German: \"Pergamonmuseum\" ) is situated on the Museum Island in Berlin.  The building was designed by Alfred Messel and Ludwig Hoffmann and was constructed over a period of twenty years, from 1910 to 1930.  The Pergamon Museum houses monumental buildings such as the Pergamon Altar, the Ishtar Gate of Babylon, and the Market Gate of Miletus reconstructed from the ruins found in ancient Middle East.\n\nSam'al lions: The Sam'al lions are four lion-shaped statues which are currently located in the Vorderasiatisches Museum Berlin (Pergamon Museum).\n\nQuestion: What is the name of the eighth gate to the city of Babylon, currently housed at Pergamon Museum?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"gate_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the gate.\"\n    },\n    \"original_city\": {\n      \"type\": \"string\",\n      \"description\": \"The city to which the gate originally belonged.\"\n    },\n    \"gate_number\": {\n      \"type\": \"integer\",\n      \"description\": \"The numerical designation of the gate within its original city.\"\n    },\n    \"current_museum_location\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the museum where the gate is currently housed.\"\n    },\n    \"original_construction_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"construction_year_bce\": {\n          \"type\": \"integer\",\n          \"description\": \"The approximate year of construction in BCE.\"\n        },\n        \"builder_king\": {\n          \"type\": \"string\",\n          \"description\": \"The king who ordered the construction of the gate.\"\n        },\n        \"original_side_of_city\": {\n          \"type\": \"string\",\n          \"description\": \"The side of the city where the gate was originally located.\"\n        }\n      },\n      \"required\": [\n        \"construction_year_bce\",\n        \"builder_king\",\n        \"original_side_of_city\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"gate_name\",\n    \"original_city\",\n    \"gate_number\",\n    \"current_museum_location\",\n    \"original_construction_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "gate_name": {
        "type": "string",
        "description": "The name of the gate."
      },
      "original_city": {
        "type": "string",
        "description": "The city to which the gate originally belonged."
      },
      "gate_number": {
        "type": "integer",
        "description": "The numerical designation of the gate within its original city."
      },
      "current_museum_location": {
        "type": "string",
        "description": "The name of the museum where the gate is currently housed."
      },
      "original_construction_details": {
        "type": "object",
        "properties": {
          "construction_year_bce": {
            "type": "integer",
            "description": "The approximate year of construction in BCE."
          },
          "builder_king": {
            "type": "string",
            "description": "The king who ordered the construction of the gate."
          },
          "original_side_of_city": {
            "type": "string",
            "description": "The side of the city where the gate was originally located."
          }
        },
        "required": [
          "construction_year_bce",
          "builder_king",
          "original_side_of_city"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "gate_name",
      "original_city",
      "gate_number",
      "current_museum_location",
      "original_construction_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
