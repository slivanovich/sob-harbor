{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAhmad A'zam: Ahmad A'zam \"(Аҳмад Аъзам)\" (28 June 1949 – 4 January 2014) was an Uzbek writer, author, journalist, scriptwriter and literature critic.\n\nPalor people: The Palors also known as Serer-Palor, (or Waro in their own language) among other names, are an ethnic group found in Senegal around the west central, west southwest of Thiès.  They are a sub-group of the Serer ethnic group found in Senegal, the Gambia and Mauritania.  Although ethnically Serers, they do not speak the Serer language but one of the Cangin languages.  Their language is Palor.\n\nZaramo people: The Zaramo people, also referred to as Dzalamo or Saramo, are an East African ethnic group found along the coast of Tanzania, particularly in its Pwani Region.  They are the largest ethnic group in and around Dar es Salaam, the capital of Tanzania.  Estimated to be about 0.7 million, over 98% of them are Muslims, more specifically the Shafi'i school of Sunni Islam.\n\nTalaote tribe: BaTalaote are an ethnic group found in the central district of Botswana and south-western parts of Zimbabwe.  They are part of a large group of ethnic groups called Bakalanga.  Over the years Batalaote lost their language and adopted Kalanga for those in Zimbabwe and Sengwato, which is spoken by the Bangwato, for those in Botswana.  The Talaunda and the Wadoma could share a common ancestor.  Both tribes have significantly high cases of ectrodactyly.\n\nLun Bawang: The Lun Bawang (formerly known as Trusan Murut or Southern Murut) is an ethnic group found in Central Northern Borneo.  They are indigenous to the highlands of North Kalimantan (Krayan, Malinau, Mentarang and Long Bawan), Brunei (Temburong District), southwest of Sabah (Interior Division) and northern region of Sarawak (Limbang Division).  In the Malaysian state of Sarawak, the Lun Bawang (through the term \"Murut\") are officially recognised by the Constitution as native of Sarawak and are categorised under the Orang Ulu people; whilst in the neighbouring state of Sabah and Krayan highland in Kalimantan, they are sometimes named \"Lundayeh\" or \"Lun Daye\".  In Brunei, they are also identified by law as one of the 7 natives (indigenous people) of Brunei, through the term \"Murut\".  Nevertheless, in Sabah, Kalimantan and Brunei, the term Lun Bawang is gaining popularity as a unifying term for this ethnic across all region.  There are also other alternative names such as Lun Lod, Lun Baa' and Lun Tana Luun.\n\nUkrainians: Ukrainians (Ukrainian: українці , \"ukrayintsi\", ] ) are an East Slavic ethnic group native to Ukraine, which is by total population the sixth-largest nation in Europe.  The Constitution of Ukraine applies the term 'Ukrainians' to all its citizens.  Also among historical names of the people of Ukraine, Rusyns (Ruthenians), Cossacks, etc. can be found.  According to most dictionary definitions, a descriptive name for the \"inhabitants of Ukraine\" is \"Ukrainian\" or \"Ukrainian people\".  Rusyns are another related group found in western Ukraine, which are frequently referred to as being an ethnic subgroup of Ukrainians.  The Rusyns are also further divided into subgroups of tribes consisiting of the Hutsuls, Boykos, and Lemkos.\n\nWolof people: The Wolof people ( ) are a West African ethnic group found in northwestern Senegal, The Gambia, and southwestern coastal Mauritania.  In Senegal, the Wolof are the largest ethnic group (~ 39%), while elsewhere they are a minority.  They refer to themselves as Wolof, and speak the Wolof language – a West Atlantic branch of the Niger-Congo family of languages.\n\nBalanta people: The Balanta (Guinea-Bissau Creole and Portuguese: \"balanta\"; French: \"balante\" ; lit.  “those who resist” in Balanta) are an ethnic group found in Guinea-Bissau, Senegal and The Gambia.  They are the largest ethnic group of Guinea-Bissau, representing more than one-quarter of the population.  Despite their numbers, they have remained outside the colonial and postcolonial state because of their social organisation.  The Balanta can be divided into four subgroups, three of which are Balanta Kentohe, Balanta Ganja and Balanta Brassa, the largest of which are the Balanta Brassa.\n\nUzbeks: The Uzbeks (\"Oʻzbek/Ўзбек\", pl.  \"Oʻzbeklar/Ўзбеклар\") are a Turkic ethnic group; the largest Turkic ethnic group in Central Asia.  They comprise the majority population of Uzbekistan but are also found as a minority group in Afghanistan, Tajikistan, Kyrgyzstan, Kazakhstan, Turkmenistan, Russia and China.  Uzbek diaspora communities also exist in Turkey, Saudi Arabia, and Pakistan.\n\nFang people: The Fang people, also known as Fãn or Pahouin, are a Central African ethnic group found in Equatorial Guinea, northern Gabon, and southern Cameroon.  Representing about 85% of the total population of Equatorial Guinea, concentrated in the Rio Muni region, the Fang people are its largest ethnic group.  In other countries, in the regions they live, they are one of the most significant and influential ethnic groups.\n\nQuestion: How many places are Ahmad A'zam's ethnic group found?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"ethnic_group\": {\n      \"type\": \"string\",\n      \"description\": \"The ethnic group of Ahmad A'zam.\"\n    },\n    \"found_countries\": {\n      \"type\": \"array\",\n      \"description\": \"List of countries where the ethnic group is found as a minority group.\",\n      \"items\": {\n        \"type\": \"string\"\n      }\n    },\n    \"number_of_countries\": {\n      \"type\": \"integer\",\n      \"description\": \"The total count of countries where the ethnic group is found as a minority group.\"\n    }\n  },\n  \"required\": [\n    \"ethnic_group\",\n    \"found_countries\",\n    \"number_of_countries\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "ethnic_group": {
        "type": "string",
        "description": "The ethnic group of Ahmad A'zam."
      },
      "found_countries": {
        "type": "array",
        "description": "List of countries where the ethnic group is found as a minority group.",
        "items": {
          "type": "string"
        }
      },
      "number_of_countries": {
        "type": "integer",
        "description": "The total count of countries where the ethnic group is found as a minority group."
      }
    },
    "required": [
      "ethnic_group",
      "found_countries",
      "number_of_countries"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
