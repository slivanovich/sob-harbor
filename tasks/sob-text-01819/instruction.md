{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDuke of Aosta: In the mid-13th century the Hohenstaufen Holy Roman Emperor Frederick II made the County of Aosta a duchy; its arms were carried in the Savoyard coat of arms until the unification of Italy in 1870.  The region remained part of Savoy lands, with the exception of a French occupation, 1539—1563.  The title Duke of Aosta was given to various princes of the dynasty of Sardinia, second sons of the reigning monarch.  It can be compared to the English Duke of York, French Duke of Orléans, Swedish Duke of Södermanland and the Scottish Duke of Albany.  It remained in the branch of Prince Amedeo of Savoia, the second son of king Victor Emanuel II of Italy, as he was the first ever cadet prince Duke of Aosta who left male heirs.  The subsidiary titles of the Duke of Aosta are, from the heritage of Maria Vittoria dal Pozzo, the mother of Duke Emanuele Filiberto, Prince della Cisterna and of Belriguardo, Marquess of Voghera, and Count of Ponderano.  Ponderano was created in 1559, Voghera in 1618; Cisterna and Belriguardo as princely in 1670.  The title has been used since July 2006 by Amedeo's son Prince Aimone, Duke of Apulia (born 1967), who is married to Princess Olga of Greece, younger daughter of Prince Michael of Greece and Denmark.\n\nVernadsky Research Base: The Vernadsky Research Base (Ukrainian: Академік Вернадський ) is a Ukrainian Antarctic Station at Marina Point on Galindez Island in the Argentine Islands, Antarctica.  It is named after Soviet and Ukrainian mineralogist Vladimir Vernadsky (1863–1945).\n\nGrand Duchess Alexandra Georgievna of Russia: Grand Duchess Alexandra Georgievna of Russia (Russian: Алекса́ндра Гео́ргиевна ); \"née\" Princess Alexandra of Greece and Denmark (Greek: Πριγκίπισσα Αλεξάνδρα της Ελλάδας και της Δανίας ); 30 August 1870 – 24 September 1891) was the third child and firstborn daughter of King George I and Queen Olga of Greece, who herself was a daughter of a Russian grand duke, and was also a grandchild of Denmark's King Christian IX and Queen Louise.  She was a sister to Constantine I of Greece, and thus aunt of three kings and two queens, Constantine's three sons, who all became kings of Greece, and two of his daughters, who were queens, in name, of Romania and Croatia, respectively.  She was also first cousin of Tsar Nicholas II of Russia, King George V of the United Kingdom, and both King Haakon VII and Queen Maud of Norway, as well as a paternal aunt of Prince Philip, Duke of Edinburgh.\n\nPrincess Olga, Duchess of Apulia: Princess Olga, Duchess of Apulia (\"née\": Princess Olga Isabelle of Greece, Greek: Πριγκίπισσα Όλγα της Ελλάδας ; born 17 November 1971) is the daughter of author Prince Michael of Greece and Denmark and his wife, Marina Karella, an artist and daughter of the Greek business magnate Theodore Karella.  Princess Olga is the wife of Prince Aimone of Savoy-Aosta, Duke of Apulia.\n\nGreek royal family: The Greek royal family (Greek: Ελληνική Βασιλική Οικογένεια) is a branch of the House of Glücksburg that reigned in Greece from 1863 to 1924 and again from 1935 to 1973.  Its first monarch was George I, the second son of King Christian IX of Denmark.  He and his successors styled themselves \"Kings of the Hellenes\".  Most members of the dynasty (aside from the last king to reign, Constantine II and his queen consort, Anne-Marie of Denmark) hold the title \"Prince or Princess of Greece and Denmark\" with the style \"Royal Highness\", except Marina, Consort of Prince Michael, and their daughters Princess Alexandra and Princess Olga.\n\nPrincess Eugénie of Greece and Denmark: Princess Eugénie of Greece and Denmark (Greek: Πριγκίπισσα Ευγενία της Ελλάδας και Δανίας ) (10 February 1910 – 13 February 1989) was the youngest child and only daughter of Prince George of Greece and Denmark and his wife, Marie Bonaparte, daughter of Prince Roland Bonaparte, a great-nephew of Napoleon I.  Her father was the second son of George I of Greece and Olga Constantinovna of Russia.\n\nPrincess Maria-Olympia of Greece and Denmark: Princess Maria-Olympia of Greece and Denmark (born 25 July 1996 in New York City) is the oldest child and only daughter of Pavlos, Crown Prince of Greece and Marie-Chantal, Crown Princess of Greece.  Her paternal grandparents are Constantine II and Anne-Marie of Denmark, who were the last King and Queen of the Hellenes.\n\nMarina Point: Marina Point ( ) is a low rocky point which forms the northwestern tip of Galindez Island in the Argentine Islands of the Wilhelm Archipelago.  It was first surveyed in 1935-36 by the British Graham Land Expedition under Rymill and named by members of the expedition for Princess Marina, later Duchess of Kent, who was married in November 1934, while the ship \"Penola\" was en route to the Argentine Islands.\n\nPrincess Marina of Greece and Denmark: Princess Marina of Greece and Denmark, {'1': \", '2': \", '3': \", '4': \"} (Greek: Πριγκίπισσα Μαρίνα της Ελλάδας και Δανίας ; 13 December [O.S. 30 November] 1906 27 August 1968) was the daughter of Prince Nicholas of Greece and Denmark and Grand Duchess Elena Vladimirovna of Russia.\n\nNavy Point: Navy Point ( ) is the northeast entrance point to Chiriguano Bay in southeast Brabant Island, Palmer Archipelago.  The feature was charted in 1954 by the Argentine Antarctic Expedition and, in 1978, named \"Punta Marina\" (Navy Point) in honor of the Argentine Navy.  A complete translation of the name has been approved to avoid a duplication of Marina Point in the Argentine Islands.\n\nQuestion: Marina Point was named for the daughter of which Prince of Greece and Denmark?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"named_feature\": {\n      \"type\": \"string\",\n      \"description\": \"The geographical feature that was named.\"\n    },\n    \"named_after_person\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"person_name\": {\n          \"type\": \"string\",\n          \"description\": \"The full name of the person for whom the feature was named.\"\n        },\n        \"person_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the person for whom the feature was named.\"\n        },\n        \"father_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the father of the person for whom the feature was named.\"\n        },\n        \"father_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the father of the person for whom the feature was named.\"\n        }\n      },\n      \"required\": [\n        \"person_name\",\n        \"person_title\",\n        \"father_name\",\n        \"father_title\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"naming_event\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"expedition_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the expedition that named the feature.\"\n        },\n        \"survey_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the feature was first surveyed.\"\n        }\n      },\n      \"required\": [\n        \"expedition_name\",\n        \"survey_year\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"named_feature\",\n    \"named_after_person\",\n    \"naming_event\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "named_feature": {
        "type": "string",
        "description": "The geographical feature that was named."
      },
      "named_after_person": {
        "type": "object",
        "properties": {
          "person_name": {
            "type": "string",
            "description": "The full name of the person for whom the feature was named."
          },
          "person_title": {
            "type": "string",
            "description": "The title of the person for whom the feature was named."
          },
          "father_name": {
            "type": "string",
            "description": "The name of the father of the person for whom the feature was named."
          },
          "father_title": {
            "type": "string",
            "description": "The title of the father of the person for whom the feature was named."
          }
        },
        "required": [
          "person_name",
          "person_title",
          "father_name",
          "father_title"
        ],
        "additionalProperties": false
      },
      "naming_event": {
        "type": "object",
        "properties": {
          "expedition_name": {
            "type": "string",
            "description": "The name of the expedition that named the feature."
          },
          "survey_year": {
            "type": "integer",
            "description": "The year the feature was first surveyed."
          }
        },
        "required": [
          "expedition_name",
          "survey_year"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "named_feature",
      "named_after_person",
      "naming_event"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
