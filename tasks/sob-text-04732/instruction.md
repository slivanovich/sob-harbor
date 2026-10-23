{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSalvia indica: Salvia indica is a species of herbaceous perennial plant belonging to the family Lamiaceae.  It is native to a wide region of Western Asia that includes Israel, Iraq, Iran and Turkey.  It was first described by the taxonomist Carl Linnaeus in 1753.  It is unknown why he gave it the specific epithet \"indica\", since the plant is not from India.  While \"Salvia indica\" is classified as a herbaceous perennial, in cultivation individual plants often live no longer than two years.\n\nTrichophorum cespitosum: Trichophorum cespitosum, commonly known as deergrass or tufted bulrush, is a species of flowering plant in the sedge family.  It was originally described by Carl Linnaeus in 1753 as \"Scirpus cespitosus\", but was changed to \"Trichophorum cespitosum\" by Carl Johan Hartman in 1849.\n\nIsolepis fluitans: Isolepis fluitans (syn.  \"Scirpus fluitans\") is a species of flowering plant in the sedge family.  It is native to Africa, Australasia, Europe, and Pacific.  It was first described by Carl Linnaeus in 1753, and later transferred to \"Isolepis\" by the botanist Robert Brown in 1810.\n\nArgentina anserina: Argentina anserina is a synonym of \"Potentilla anserina\" L., the accepted name of a perennial flowering plant in the rose family Rosaceae.  It is known by the common names \"silverweed\", common silverweed or silverweed cinquefoil.  It is native throughout the temperate Northern Hemisphere, often on river shores and in grassy habitats such as meadows and road-sides.  The plant was originally placed in the genus \"Potentilla\" by Carl Linnaeus in his Species plantarum, edition 1, (1753) but was reclassified into the resurrected genus \"Argentina\" by research conducted in the 1990s.  It is a species aggregate which has frequently been divided into multiple species.  The reclassification remains controversial and is not accepted by some authorities.\n\nCannabis sativa: Cannabis sativa is an annual herbaceous plant in the \"Cannabis\" genus.  It is a member of a small, but diverse family of flowering plants of the Cannabaceae family.  It has been cultivated throughout recorded history, used as a source of industrial fibre, seed oil, food, recreation, religious and spiritual moods and medicine.  Each part of the plant is harvested differently, depending on the purpose of its use.  The species was first classified by Carl Linnaeus in 1753.\n\nPotentilla bifurca: Potentilla bifurca () is a species of flowering plant in the Rosaceae family which can be found in Russian, Korean, and Mongolian steppes, grasslands and various slopes on an elevation of 400 - .  It is also found on sandy coasts of North and Northeast China.  It was described by Carl Linnaeus in 1753 in his book Species Plantarum.\n\nPenicillium scabrosum: Penicillium scabrosum is a species of fungus in the family Trichocomaceae.  Described as new to science in 1990, it was first isolated from soil associated with corn in Denmark.  It has also been found in soil samples from other temperate areas of the world, including Canada.  The fungus is a spoilage organism for foods, particularly those with lipid- and cereal-containing feed.  It produces several mycotoxins, including fumagillin, viridicatin, and viridicatol.  \"P. scabrosum\" is classified in \"Penicillium\" subgenus \"Penicillium\", section \"Divaricatum\", series \"Atroveneta\".\n\nGenera Plantarum: Genera Plantarum is a publication of Swedish naturalist Carl Linnaeus (1707–1778).  The first edition was issued in Leiden, 1737.  The fifth edition served as a complementary volume to \"Species Plantarum\" (1753).  Article 13 of the International Code of Nomenclature for algae, fungi, and plants states that \"\"Generic names that appear in Linnaeus' \"Species Plantarum\" ed.  1 (1753) and ed.  2 (1762–63) are associated with the first subsequent description given under those names in Linnaeus' \"Genera Plantarum\" ed.  5 (1754) and ed.  6 (1764)\".\"  This defines the starting point for nomenclature of most groups of plants.\n\nDigitalis thapsi: Digitalis thapsi, known commonly as Spanish foxglove, Spanish digitalis, and fingerhut foxglove, is a flowering plant in the genus \"Digitalis\" that is native to Spain.  It was first described by Carl Linnaeus in 1753.  It is of commercial importance as an ornamental plant.  Hybrids with \"D. purpurea\" have proved successful and are fertile.\n\nPenicillium copticola: Penicillium copticola is a species of the genus of \"Penicillium\" which was isolated from the twigs, leaves, and apical and lateral buds of the plant Cannabis sativa L..\n\nQuestion: What flowering plant, first classified by Carl Linnaeus in 1753, produces   Penicillium copticola?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"flowering_plant_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the flowering plant.\"\n    },\n    \"classification_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"classifier\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the taxonomist who first classified the plant.\"\n        },\n        \"classification_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the plant was first classified.\"\n        }\n      },\n      \"required\": [\n        \"classifier\",\n        \"classification_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"associated_fungus\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the fungus isolated from the plant.\"\n    },\n    \"plant_family\": {\n      \"type\": \"string\",\n      \"description\": \"The family to which the plant belongs.\"\n    }\n  },\n  \"required\": [\n    \"flowering_plant_name\",\n    \"classification_details\",\n    \"associated_fungus\",\n    \"plant_family\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "flowering_plant_name": {
        "type": "string",
        "description": "The name of the flowering plant."
      },
      "classification_details": {
        "type": "object",
        "properties": {
          "classifier": {
            "type": "string",
            "description": "The name of the taxonomist who first classified the plant."
          },
          "classification_year": {
            "type": "integer",
            "description": "The year the plant was first classified."
          }
        },
        "required": [
          "classifier",
          "classification_year"
        ],
        "additionalProperties": false
      },
      "associated_fungus": {
        "type": "string",
        "description": "The name of the fungus isolated from the plant."
      },
      "plant_family": {
        "type": "string",
        "description": "The family to which the plant belongs."
      }
    },
    "required": [
      "flowering_plant_name",
      "classification_details",
      "associated_fungus",
      "plant_family"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
