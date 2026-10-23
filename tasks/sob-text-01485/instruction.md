{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nStyrian Coarse-haired Hound: The Styrian Coarse-haired Hound (FCI No. 62), (German: \"Steirische Rauhhaarbracke\") is a breed of medium-sized hound dog originated in the Austrian province of Styria.  It is bred as a scenthound, for hunting boar in mountainous terrain.  The breed is one of the large Austrian Bracke.\n\nCape Vakop: Cape Vakop ( ) is a headland between Hound Bay and Luisa Bay on the north coast of South Georgia.  It was charted by the Second German Antarctic Expedition, 1911–12, under Wilhelm Filchner.  The name appears on a chart based upon surveys of South Georgia in 1926–30 by DI personnel, but may represent an earlier naming.\n\nDer Hund von Baskerville: Der Hund von Baskerville is a 1914 German silent film adaptation of Arthur Conan Doyle's \"The Hound of the Baskervilles\".  This was the first film adaptation of the famed Conan Doyle novel.  According to the website silentera.com, the film was considered lost, but has been rediscovered; the Russian Gosfilmofond film archive possesses a print, while the Filmmuseum München has a 35mm positive print.\n\nDrever: The Drever is a breed of dog, a short-legged scenthound from Sweden used for hunting deer and other game.  The Drever is descended from the Westphalian Dachsbracke, a type of German hound called \"Bracke\".  The breed name Drever was chosen through a contest in 1947.\n\nThe Hound of the Baskervilles (1937 film): The Hound of the Baskervilles (German:Der Hund von Baskerville ) is a 1937 German mystery film directed by Carl Lamac and starring Bruno Güttner, Fritz Odemar and Peter Voß.  It is an adaptation of the Sherlock Holmes's story \"The Hound of the Baskervilles\" by Arthur Conan Doyle.\n\nThe Hound of the Baskervilles (1929 film): (German: Der Hund von Baskerville) is a 1929 German silent mystery film directed by Richard Oswald and starring Carlyle Blackwell, Alexander Murski, Livio Pavanelli.  The film is an adaptation of the Sherlock Holmes novel \"The Hound of the Baskervilles\" by Arthur Conan Doyle.  It was the last Sherlock Holmes adaptation in the silent film era.\n\nBavarian Mountain Hound: The Bavarian Mountain Hound (German = \"Bayerischer Gebirgsschweißhund\") is a breed of dog from Germany.  As a scent hound, it has been used in Germany since the early 20th century to trail wounded game.  It is a cross between the Bavarian Hound and the Hanover Hound.\n\nGerman Hound: The German Hound (\"Deutsche Bracke\") (FCI No. 299) is a breed of dog originating in Westphalia, a region of Germany.  The German Hound is of the scenthound type, used for hunting both large and small game.  The breed is normally referred to as the \"Deutsche Bracke\" in English, rather than by the translation of the name, German Hound.\n\nSamoyed (dog): The Samoyed ( or ; Russian: Самоедская собака or Самоед ) is a breed of large herding dog, from the spitz group, with a thick, white, double-layer coat.  It takes its name from the Samoyedic peoples of Siberia.  These nomadic reindeer herders bred the fluffy white dogs to help with the herding, and to pull sleds when they moved.  An alternate name for the breed, especially in Europe, is Bjelkier.\n\nThe Brothel in Rosenstrasse: The Brothel in Rosenstrasse is a 1982 novel by Michael Moorcock.  The main character is Rickhardt von Bek, a member of the family of Ulrich von Bek which is central to some of Moorcock's other fantasy novels, notably \"The War Hound and the World's Pain\", \"The City in the Autumn Stars\", and \"The Dragon in the Sword\".  The novel is written as Bek's memoir of a dying, demented man, in which he recalls his time with a bi-sexual teenage nymphet girl and how they take refuge in an superior brothel in a German city under siege during a 19th-century war.  The standard German spelling of the name in the novel's title is \"Rosenstraße\" (Street of Roses).\n\nQuestion: German Hound and Samoyed are both what?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"entity_type\": {\n      \"type\": \"string\",\n      \"description\": \"The general type of items being compared.\"\n    },\n    \"entities\": {\n      \"type\": \"array\",\n      \"description\": \"A list of the specific entities mentioned in the question.\",\n      \"items\": {\n        \"type\": \"string\"\n      }\n    },\n    \"common_category\": {\n      \"type\": \"string\",\n      \"description\": \"The common category or classification that both entities belong to.\"\n    }\n  },\n  \"required\": [\n    \"entity_type\",\n    \"entities\",\n    \"common_category\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "entity_type": {
        "type": "string",
        "description": "The general type of items being compared."
      },
      "entities": {
        "type": "array",
        "description": "A list of the specific entities mentioned in the question.",
        "items": {
          "type": "string"
        }
      },
      "common_category": {
        "type": "string",
        "description": "The common category or classification that both entities belong to."
      }
    },
    "required": [
      "entity_type",
      "entities",
      "common_category"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
