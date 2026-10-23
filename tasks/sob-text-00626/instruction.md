{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nType 91 surface-to-air missile: The Type 91 surface-to-air missile (91式携帯地対空誘導弾 , 91-shiki Keitai Chitaikū Yūdōdan ) is a Japanese man-portable surface-to-air missile system.  Its appearance is similar to the US-made FIM-92 Stinger anti-aircraft missile.  It was created in order to replace its stock of American-made Stinger MANPADS, since the Type 91 has a better guidance system, which consist of both light and infrared system options.  The Stinger, on the other hand, uses a passive infrared homing guidance system.\n\nHigh-leg delta: High-leg delta (also known as wild-leg, stinger leg, bastard leg, high-leg, orange-leg, or red-leg delta) is a type of electrical service connection for three-phase electric power installations.  It is used when both single and three-phase power is desired to be supplied from a three phase transformer (or transformer bank).  The three-phase power is connected in the delta configuration, and the center point of one phase is grounded.  This creates both a split-phase single phase supply (L1 or L2 to neutral on diagram at right) and three-phase (L1-L2-L3 at right).  It is called \"orange leg\" because when it is connected per the NEC, the high leg is marked with orange \"outer finish...or other effective means\" (usually tape).  By convention, the high leg is usually set in the center (B phase) lug in the involved panel, regardless of the L1-L2-L3 designation at the transformer.\n\nMargarita: A margarita is a cocktail consisting of tequila, triple sec, and lime or lemon juice, often served with salt or sugar on the rim of the glass.  The drink is served shaken with ice (on the rocks), blended with ice (frozen margarita), or without ice (straight up).  Although it has become acceptable to serve a margarita in a wide variety of glass types, ranging from cocktail and wine glasses to pint glasses and even large schooners, the drink is traditionally served in the eponymous margarita glass, a stepped-diameter variant of a cocktail glass or champagne coupe.\n\nCafe Royal Cocktail Book: The Cafe Royal Cocktail Book is a collection of cocktail recipes compiled by William J. Tarling, published by the United Kingdom Bartenders Guild in 1937.  It contains a number of pioneering recipes, including the 20th Century and what later became the Margarita.\n\nTommy's Margarita: Tommy's Margarita is an all-day cocktail and variant of the Margarita cocktail.  It is recognised by the IBA as a New Era Drink.\n\nMexican martini: The Mexican martini is a cocktail variation of a Margarita served straight up in a cocktail glass like a Martini.  It is a popular drink in Austin, Texas.\n\nStinger (cocktail): A stinger is a duo cocktail made by adding crème de menthe to a spirit.\n\nSpike strip: A spike strip (also known as traffic spikes, tire shredders, one-way traffic treadles, stingers, stop sticks, a stinger in police slang, and formally known as a tire deflation device) is a device used to impede or stop the movement of wheeled vehicles by puncturing their tires. Generally, the strip is composed of a collection of 35 to 75 mm (1.5 to 3 inches) long metal barbs, teeth or spikes pointing upward.  The spikes are designed to puncture and flatten tires when a vehicle is driven over them; they may be detachable, with new spikes fitted to the strip after use.  The spikes may be hollow or solid; hollow ones are designed to detach and become embedded in the tires, allowing air to escape at a steady rate to reduce the risk of the driver losing control and crashing.  One type was co-invented by Donald Kilgrow, a retired Utah Highway Patrol trooper, along with a design engineer.  They are historically a development of the caltrop, anti-cavalry and anti-personnel versions being used as early as 331 BC by Darius III against Alexander the Great at the Battle of Gaugamela in Persia.\n\nSynanceiidae: Synanceiidae is a family of Actinopterygii, ray-finned fish, found in the Indo-Pacific oceans.  They are primarily marine, though some species are known to live in fresh or brackish waters.  The various species of this family are known informally as stonefish, stinger, stingfish and ghouls.  The most prominent genus of the family is \"Synanceia\", which is sometimes placed in the family Scorpaenidae.  Its species are known to have the most potent neurotoxins of all the fish venoms, secreted from glands at the base of their needle-like dorsal fin spines.  The vernacular name of the species derives from their behaviour of camouflaging as rocks.  The type species of the family is the stonefish, \"Synanceia verrucosa\".\n\nTatsu (film): Tatsu (Russian: Тацу ) (alternative title: Hound Dogs (Russian: Гончие псы )) is a 1994 Russian film directed by Vera Yakovenko and starring Margarita Pushkina, Nastia Poleva, Krematorij, Molotov Cocktail bands and others.\n\nQuestion: Stinger and Margarita, are a type of cocktail?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"is_cocktail_type\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates whether both 'Stinger' and 'Margarita' are types of cocktails.\"\n    },\n    \"cocktail_names\": {\n      \"type\": \"array\",\n      \"description\": \"List of names identified as cocktails from the context.\",\n      \"items\": {\n        \"type\": \"string\"\n      }\n    },\n    \"non_cocktail_mentions\": {\n      \"type\": \"array\",\n      \"description\": \"Other mentions of 'Stinger' or 'Margarita' that are not cocktails, with their descriptions.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name mentioned (e.g., Stinger, Margarita).\"\n          },\n          \"type\": {\n            \"type\": \"string\",\n            \"description\": \"The type of entity it refers to (e.g., missile, electrical connection, person, fish, device).\"\n          },\n          \"description\": {\n            \"type\": \"string\",\n            \"description\": \"A brief description from the context.\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"type\",\n          \"description\"\n        ],\n        \"additionalProperties\": false\n      }\n    }\n  },\n  \"required\": [\n    \"is_cocktail_type\",\n    \"cocktail_names\",\n    \"non_cocktail_mentions\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "is_cocktail_type": {
        "type": "boolean",
        "description": "Indicates whether both 'Stinger' and 'Margarita' are types of cocktails."
      },
      "cocktail_names": {
        "type": "array",
        "description": "List of names identified as cocktails from the context.",
        "items": {
          "type": "string"
        }
      },
      "non_cocktail_mentions": {
        "type": "array",
        "description": "Other mentions of 'Stinger' or 'Margarita' that are not cocktails, with their descriptions.",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name mentioned (e.g., Stinger, Margarita)."
            },
            "type": {
              "type": "string",
              "description": "The type of entity it refers to (e.g., missile, electrical connection, person, fish, device)."
            },
            "description": {
              "type": "string",
              "description": "A brief description from the context."
            }
          },
          "required": [
            "name",
            "type",
            "description"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": [
      "is_cocktail_type",
      "cocktail_names",
      "non_cocktail_mentions"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
