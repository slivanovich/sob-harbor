{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMediterranean tropical-like cyclone: Mediterranean tropical-like cyclones, sometimes referred to as Mediterranean hurricanes or medicanes, are rare meteorological phenomena observed in the Mediterranean Sea.  Due to the dry nature of the Mediterranean region, formation of tropical cyclones is infrequent, with only 99 recorded tropical-like storms between 1948 and 2011.  No agency, however, is officially responsible for monitoring the formation and development of medicanes.  Tropical cyclogenesis typically occurs within two separate regions of the sea.  The first region, encompassing areas of the western Mediterranean, is more conducive for development than the other, the Ionian Sea to the east.  The rough mountainous geography of the region raises additional difficulties despite being favorable for the development of severe weather and convective activity in general, and only with abnormal meteorological circumstances can medicanes form.  Numerous studies have been conducted on the impact of global warming on Mediterranean tropical cyclone formation, generally concluding that fewer yet more intense storms would form.\n\nSpanish sparrow: The Spanish sparrow or willow sparrow (\"Passer hispaniolensis\") is a passerine bird of the sparrow family Passeridae.  It is found in the Mediterranean region and south-west and central Asia.  It is very similar to the closely related house sparrow, and the two species show their close relation in a \"biological mix-up\" of hybridisation in the Mediterranean region, which complicates the taxonomy of this species.\n\nMedcities: Medcities is a network of Mediterranean coastal cities created in Barcelona in 1991 at the initiative of the Mediterranean Technical Assistance Programmes (METAP).  The METAP, whose objective is environmental improvement in the Mediterranean region, was established in 1990 by the World Bank, the European Investment Bank and the United Nations Development Programme.\n\nRosemary: Rosmarinus officinalis, commonly known as rosemary, is a woody, perennial herb with fragrant, evergreen, needle-like leaves and white, pink, purple, or blue flowers, native to the Mediterranean region.\n\nQuesnelia: Quesnelia is a genus of the botanical family Bromeliaceae, subfamily Bromelioideae.  The genus is named For M. Quesnel, French consul to French Guiana.  Endemic to eastern Brazil, this genus contains 22 known species.  This genus has two recognized subgenera: the type subgenus and \"Billbergiopsis\" .\n\nMediterranean Basin: In biogeography, the Mediterranean Basin (also known as the Mediterranean region or sometimes Mediterranea) is the region of lands around the Mediterranean Sea that have a Mediterranean climate, with mild, rainy winters and hot, dry summers, which supports characteristic Mediterranean forests, woodlands, and scrub vegetation.\n\nMandragora officinarum: Mandragora officinarum is the type species of the plant genus \"Mandragora\".  It is often known as mandrake, although this name is also used for other plants.  s of 2015 , sources differ significantly in the species they use for \"Mandragora\" plants native to the Mediterranean region.  In the narrowest circumscription, \"M. officinarum\" is limited to small areas of northern Italy and the coast of former Yugoslavia, and the main species found around the Mediterranean is called \"Mandragora autumnalis\", the autumn mandrake.  In a broader circumscription, all the plants native to the countries around the Mediterranean Sea are placed in \"M. officinarum\", which thus includes \"M. autumnalis\".  The names autumn mandrake and Mediterranean mandrake are then used.  Whatever the circumscription, \"Mandragora officinarum\" is a perennial herbaceous plant with ovate leaves arranged in a rosette, a thick upright root, often branched, and bell-shaped flowers followed by yellow or orange berries.\n\nSalmo cettii: Salmo cettii, or the Mediterranean trout, is a species of trout, a freshwater fish in the Salmonidae family.  It lives in the Mediterranean region in Corsica, Sardinia, Sicily, and on the Italian mainland in the Magra drainage and further south.  It is a nonmigratory fish which lives in streams and in karstic resurgences.  It is smaller than 40 cm in length.  It is sometimes referred to \"Salmo trutta macrostigma\", which depending on concept is either a more widespread Mediterranean taxon, or a taxon endemic to Algeria.\n\nMediterranean Universities Union: The Mediterranean Universities Union (Italian: Unione delle Università del Mediterraneo, UNIMED) consists of 84 universities based in the Mediterranean basin (or that have a specific interest in the Mediterranean region).  The association has its head office in Rome.\n\nEriocephalus africanus: Eriocephalus africanus is a bushy shrublet indigenous to South Africa.  It has a wide distribution in the Western and Eastern Cape, and in Namaqualand.  The plant has several common names in various languages.  It is known as the Cape Snow Bush or Kapokbossie (the Afrikaans word for \"snow bush\"); other common names refer to its fancied resemblance to rosemary, for example \"African rosemary\" or \"Wild rosemary\" (Afrikaans \"(wilde) roosmaryn\").  The superficial resemblance is in the foliage, which, though softer and not glossy, grows in a habit similar to that of the common Mediterranean rosemary, although the two species are not related.\n\nQuestion: Does Rosemary or Quesnelia comes from the Mediterranean region\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"question_focus\": {\n      \"type\": \"string\",\n      \"description\": \"The main focus of the question, related to plant origins.\"\n    },\n    \"plants_evaluated\": {\n      \"type\": \"array\",\n      \"description\": \"A list of plants mentioned in the question and their native regions.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"plant_name\": {\n            \"type\": \"string\",\n            \"description\": \"The common name of the plant.\"\n          },\n          \"is_native_to_mediterranean\": {\n            \"type\": \"boolean\",\n            \"description\": \"True if the plant is native to the Mediterranean region, false otherwise.\"\n          },\n          \"native_region_description\": {\n            \"type\": \"string\",\n            \"description\": \"A description of the plant's native region as stated in the context.\"\n          }\n        },\n        \"required\": [\n          \"plant_name\",\n          \"is_native_to_mediterranean\",\n          \"native_region_description\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"mediterranean_native_plant_count\": {\n      \"type\": \"integer\",\n      \"description\": \"The number of plants from the evaluated list that are native to the Mediterranean region.\"\n    },\n    \"answer_statement\": {\n      \"type\": \"string\",\n      \"description\": \"A direct answer to the question about which plant comes from the Mediterranean region.\"\n    }\n  },\n  \"required\": [\n    \"question_focus\",\n    \"plants_evaluated\",\n    \"mediterranean_native_plant_count\",\n    \"answer_statement\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "question_focus": {
        "type": "string",
        "description": "The main focus of the question, related to plant origins."
      },
      "plants_evaluated": {
        "type": "array",
        "description": "A list of plants mentioned in the question and their native regions.",
        "items": {
          "type": "object",
          "properties": {
            "plant_name": {
              "type": "string",
              "description": "The common name of the plant."
            },
            "is_native_to_mediterranean": {
              "type": "boolean",
              "description": "True if the plant is native to the Mediterranean region, false otherwise."
            },
            "native_region_description": {
              "type": "string",
              "description": "A description of the plant's native region as stated in the context."
            }
          },
          "required": [
            "plant_name",
            "is_native_to_mediterranean",
            "native_region_description"
          ],
          "additionalProperties": false
        }
      },
      "mediterranean_native_plant_count": {
        "type": "integer",
        "description": "The number of plants from the evaluated list that are native to the Mediterranean region."
      },
      "answer_statement": {
        "type": "string",
        "description": "A direct answer to the question about which plant comes from the Mediterranean region."
      }
    },
    "required": [
      "question_focus",
      "plants_evaluated",
      "mediterranean_native_plant_count",
      "answer_statement"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
