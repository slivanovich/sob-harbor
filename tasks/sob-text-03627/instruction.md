{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPseudomonas salomonii: Pseudomonas salomonii is a Gram-negative bacterium that infects garlic (\"Allium sativum\").  The type strain is CFBP 2022.\n\nBlack garlic: Black garlic is a type of \"caramelized\" garlic (in reality, browned by the Maillard reaction rather than truly caramelized) first used as a food ingredient in Asian cuisine.  It is made by heating whole bulbs of garlic (\"Allium sativum\") over the course of several weeks, a process that results in black cloves.  The taste is sweet and syrupy with hints of balsamic vinegar or tamarind.\n\nVan herbed cheese: Van herbed cheese (Turkish: \"Van otlu peyniri\" ) is a type of cheese made out of sheep's or cow's milk.  Ripened cheese varieties containing herbs are traditional in Turkey and have been manufactured for more than 200 years in the east and southeast of the country.  They are manufactured from raw milk, semi-hard in texture and salty in taste and have the aroma of garlic or thyme due to added herbs.  Twenty-five types of herb, including \"Allium\", \"Thymus\", \"Silene\" and \"Ferula\" species which are most popular, are used individually or as appropriate mixtures.  The most popular of these cheeses is Otlu which is produced mainly in the Van Province of Turkey in small dairies and villages, but now is produced in other cities of the eastern region of Turkey and its popularity increases continuously throughout Turkey.\n\nHyssopus (plant): Hyssopus (hyssop) is a genus of herbaceous or semi-woody plants in the family Lamiaceae, native from the east Mediterranean to central Asia as far east as Mongolia.  They are aromatic, with erect branched stems up to 60 cm long covered with fine hairs at the tips.  The leaves are narrow oblong, 2–5 cm long.  The small blue flowers are borne on the upper part of the branches during summer.  By far the best-known species is the herb hyssop (\"H. officinalis\"), widely cultivated outside its native area in the Mediterranean.\n\nAllium: Allium is a genus of monocotyledonous flowering plants that includes hundreds of species, including the cultivated onion, garlic, scallion, shallot, leek, and chives.  The generic name \"Allium\" is the Latin word for garlic, and the type species for the genus is \"Allium sativum\" which means \"cultivated garlic\".\n\nAllium gilgiticum: Allium gilgiticum is an Asian species of onion, a rare and quite possibly extinct species.  It is known only from the type collection, gathered in the 1930s in Gilgit District in Pakistan, high in the Himalayas, part of the Kashmir region long disputed with India.  The plant is about 50 cm tall, with a hemispheric umbel of purple flowers.\n\nAllioideae: Allioideae is a subfamily of monocot flowering plants in the family Amaryllidaceae, order Asparagales.  It was formerly treated as a separate family, Alliaceae.  The subfamily name is derived from the generic name of the type genus, \"Allium\".  It is composed of approximately eighteen genera.\n\nArabis serotina: Arabis serotina is a rare species of flowering plant in the mustard family known by the common name shale barren rockcress.  It is native to eastern West Virginia and western Virginia in and around the Shenandoah Valley, where it is known from fewer than 60 populations.  It is endemic to the shale barrens, a type of habitat characterized by steep slopes of bare shale, an exposed, rocky habitat type that is subject to very dry and hot conditions.  Shale barrens host a number of endemics, such as \"Allium oxyphilum\" and \"Taenidia montana\", and this rockcress is among the rarest.  It is a federally listed endangered species.\n\nShallot: The shallot is a type of onion, specifically a botanical variety of the species \"Allium cepa\".\n\nQuestion: Allium and Hyssopus, are a type of what?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"entities_analyzed\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the entity from the question.\"\n          },\n          \"contextual_description_of_type\": {\n            \"type\": \"string\",\n            \"description\": \"How the entity is described in the context regarding its type.\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"contextual_description_of_type\"\n        ],\n        \"additionalProperties\": false\n      },\n      \"description\": \"A list of entities from the question and their descriptions from the context.\"\n    },\n    \"shared_classification\": {\n      \"type\": \"string\",\n      \"description\": \"The common classification that both entities belong to.\"\n    },\n    \"classification_level\": {\n      \"type\": \"string\",\n      \"description\": \"The general level of the shared classification (e.g., 'biological_kingdom', 'organism_type').\"\n    }\n  },\n  \"required\": [\n    \"entities_analyzed\",\n    \"shared_classification\",\n    \"classification_level\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "entities_analyzed": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the entity from the question."
            },
            "contextual_description_of_type": {
              "type": "string",
              "description": "How the entity is described in the context regarding its type."
            }
          },
          "required": [
            "name",
            "contextual_description_of_type"
          ],
          "additionalProperties": false
        },
        "description": "A list of entities from the question and their descriptions from the context."
      },
      "shared_classification": {
        "type": "string",
        "description": "The common classification that both entities belong to."
      },
      "classification_level": {
        "type": "string",
        "description": "The general level of the shared classification (e.g., 'biological_kingdom', 'organism_type')."
      }
    },
    "required": [
      "entities_analyzed",
      "shared_classification",
      "classification_level"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
