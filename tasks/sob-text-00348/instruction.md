{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAeroport, Oymyakonsky District, Sakha Republic: Aeroport (Russian: Аэропорт ) is a rural locality (a \"selo\"), and one of four settlements in Second Borogonsky Rural Okrug of Oymyakonsky District in the Sakha Republic, Russia, in addition to Tomtor, the administrative center of the Rural Okrug, Agayakan and Kuydusun.  It is located 572 km from Ust-Nera, the administrative center of the district and 2 km from Tomtor.  Its population as of the 2002 Census was 61.\n\nKhara-Tumul: Khara-Tumul (Russian: Хара-Тумул ) is a rural locality (a \"selo\") in Borogonsky 1-y Rural Okrug of Oymyakonsky District in the Sakha Republic, Russia, located 615 km from Ust-Nera, the administrative center of the district and 3 km from Oymyakon, the administrative center of the rural okrug.  Its population as of the 2002 Census was 244.\n\nKyubeme: Kyubeme (Russian: Кюбеме ) is a rural locality (a \"selo\") in Yuchyugeysky Rural Okrug of Oymyakonsky District in the Sakha Republic, Russia, located 635 km from Ust-Nera, the administrative center of the district and 94 km from Yuchyugey, the administrative center of the rural okrug.  Its population as of the 2002 Census was 46.\n\nOymyakon: Oymyakon (Russian: Оймяко́н , ] ; Yakut: Өймөкөөн , \"Öymököön\", ] ) is a rural locality (a \"selo\") in Oymyakonsky District of the Sakha Republic, Russia, located along the Indigirka River, 30 km northwest of Tomtor on the Kolyma Highway.  It is one of the coldest permanently inhabited locales on Earth.\n\nAgayakan: Agayakan (Russian: Агаякан ) is a rural locality (a \"selo\"), and one of four settlements in Second Borogonsky Rural Okrug of Oymyakonsky District in the Sakha Republic, Russia, in addition to Tomtor, the administrative center of the Rural Okrug, Aeroport and Kuydusun.  It is located 660 km from Ust-Nera, the administrative center of the district and 90 km from Tomtor.  Its population as of the 2002 Census was 0.\n\nTeryut: Teryut (Russian: Терют ) is a rural locality (a \"selo\"), the only inhabited locality, and the administrative center of Teryutsky Rural Okrug of Oymyakonsky District in the Sakha Republic, Russia, located 120 km from Ust-Nera, the administrative center of the district.  Its population as of the 2010 Census was 355, of whom 164 were male and 158 female, down from 411 as recorded during the 2002 Census.\n\nKuydusun: Kuydusun (Russian: Куйдусун ) is a rural locality (a \"selo\") in Borogonsky 2-y Rural Okrug of Oymyakonsky District in the Sakha Republic, Russia, located 567 km from Ust-Nera, the administrative center of the district, and 3 km from Tomtor, the administrative center of the rural okrug.  Its population as of the 2002 Census was 139.\n\nKuranakh-Sala: Kuranakh-Sala (Russian: Куранах-Сала ) is a rural locality (a \"selo\") in Sordonnokhsky Rural Okrug of Oymyakonsky District in the Sakha Republic, Russia, located 619 km from Ust-Nera, the administrative center of the district, and 36 km from Orto-Balagan, the administrative center of the rural okrug.  Its population as of the 2002 Census was 19.\n\nTomtor, Oymyakonsky District, Sakha Republic: Tomtor (Russian: Томтор ) is a rural locality (a \"selo\"), the administrative centre of, and one of four settlements in addition to Aeroport, Agayakan and Kuydusun in Sordonnokhsky Rural Okrug of Oymyakonsky District in the Sakha Republic, Russia.  It is located 570 km from Ust-Nera, the administrative center of the district.  Its population as of the 2002 Census was 1,256.\n\nBereg-Yurdya: Bereg-Yurdya (Russian: Берег-Юрдя ) is a rural locality (a \"selo\"), and one of three settlements in First Borogonsky Rural Okrug of Oymyakonsky District in the Sakha Republic, Russia, in addition to Oymyakon, the administrative center of the Rural Okrug and Khara-Tumul.  It is located 605 km from Ust-Nera, the administrative center of the district and 7 km from Oymyakon.  Its population as of the 2002 Census was 299.\n\nQuestion: What rural locality located 3 km away from Khara-Tumul is in the Oymyakonsky District?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"identified_locality_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the rural locality identified by the question.\"\n    },\n    \"locality_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of the identified locality (e.g., 'selo', 'rural locality').\"\n    },\n    \"district\": {\n      \"type\": \"string\",\n      \"description\": \"The district where the identified locality is located.\"\n    },\n    \"distance_from_reference_locality_km\": {\n      \"type\": \"integer\",\n      \"description\": \"The distance in kilometers from the reference locality.\"\n    },\n    \"reference_locality_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the locality used as a reference point for distance.\"\n    },\n    \"role_in_rural_okrug\": {\n      \"type\": \"string\",\n      \"description\": \"The role of the identified locality within the rural okrug of the reference locality, if specified.\"\n    }\n  },\n  \"required\": [\n    \"identified_locality_name\",\n    \"locality_type\",\n    \"district\",\n    \"distance_from_reference_locality_km\",\n    \"reference_locality_name\",\n    \"role_in_rural_okrug\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "identified_locality_name": {
        "type": "string",
        "description": "The name of the rural locality identified by the question."
      },
      "locality_type": {
        "type": "string",
        "description": "The type of the identified locality (e.g., 'selo', 'rural locality')."
      },
      "district": {
        "type": "string",
        "description": "The district where the identified locality is located."
      },
      "distance_from_reference_locality_km": {
        "type": "integer",
        "description": "The distance in kilometers from the reference locality."
      },
      "reference_locality_name": {
        "type": "string",
        "description": "The name of the locality used as a reference point for distance."
      },
      "role_in_rural_okrug": {
        "type": "string",
        "description": "The role of the identified locality within the rural okrug of the reference locality, if specified."
      }
    },
    "required": [
      "identified_locality_name",
      "locality_type",
      "district",
      "distance_from_reference_locality_km",
      "reference_locality_name",
      "role_in_rural_okrug"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
