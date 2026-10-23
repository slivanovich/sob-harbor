{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGynaephora groenlandica: Gynaephora groenlandica, the arctic woolly bear moth, is an erebid moth found within the Arctic Circle, in Greenland and Canada.  It is best known for its very slow rate of development.  It was once estimated that it had a 14-year lifecycle from egg to adult moth, unique among the Lepidoptera with the ability to withstand temperatures below −60°C.  The larvae degrade their mitochondria in preparation for overwintering and resynthesize them in the spring, and each instar of the caterpillar takes about a year.  Subsequent studies have revised the lifecycle duration to be 7 years.\n\nEast Antarctica: East Antarctica, also called Greater Antarctica, constitutes the majority (two-thirds) of the Antarctic continent, lying on the Indian Ocean side of the continent, separated from West Antarctica by the Transantarctic Mountains.  It lies almost entirely within the Eastern Hemisphere and its name has been accepted for more than a century.  It is generally higher than West Antarctica and includes the Gamburtsev Mountain Range in the centre.\n\nCinnabar moth: The cinnabar moth (\"Tyria jacobaeae\") is a brightly coloured arctiid moth found in Europe and western and central Asia.  It has been introduced into New Zealand, Australia and North America to control poisonous ragwort, on which its larvae feed.  The moth is named after the red mineral cinnabar because of the red patches on its predominantly black wings.  Cinnabar moths are about 20mm long and have a wingspan of 32 – .\n\nYellowtail moth: The yellowtail moth or ashen moth (\"Hylesia metabus\") is a species of moth found in northeastern South America, and contact with the urticating hairs of adult female moths is known to cause a cutaneous condition called the Caripito itch.\n\nColeotechnites blastovora: Coleotechnites blastovora is a moth of the Gelechiidae family.  It is found in North America, where it has been recorded from Quebec, Alberta, British Columbia, New Brunswick and Saskatchewan.\n\nCoscinocera hercules: Coscinocera hercules (Hercules moth) is a moth of the family Saturniidae, endemic to New Guinea and northern Australia.  It has a wingspan of 27 cm , making it the largest moth found in Australia, and its wings have the largest documented surface area (300 square centimeters) of any living insect.  The larvae feed on \"Polyscias elegans\", \"Glochidion ferdinandi\", \"Dysoxylum muelleri\", \"Prunus serotina\", \"Timonius rumphii\", but also eat other plants in captivity.\n\nNyctemera coleta: Nyctemera coleta, commonly known as the Marbled white moth,White tiger moth, is a species of moth found from India to the Philippines, and from Japan to Papua New Guinea.  It is classified under the subgenus \"Coleta\" of the genus \"Nyctemera\" in the family Arctiidae.  It contains four subspecies:\n\nColeotechnites albicostata: Coleotechnites albicostata, the white-edged coleotechnites moth, is a moth of the Gelechiidae family.  It is found in North America, where it has been recorded from Alabama, Maryland, Mississippi, New Jersey, North Carolina, Ontario and Tennessee.\n\nColeotechnites florae: Coleotechnites florae, the coleotechnites flower moth, is a moth of the Gelechiidae family.  It is found in North America, where it has been recorded from Alabama, Alberta, Arkansas, British Columbia, Florida, Georgia, Indiana, Louisiana, Maryland, Massachusetts, Michigan, Minnesota, Mississippi, Montana, North Carolina, Oklahoma, Saskatchewan, South Carolina, Tennessee, Texas and Washington.\n\nNorth America: North America is a continent entirely within the Northern Hemisphere and almost all within the Western Hemisphere; it is also considered by some to be a northern subcontinent of the Americas.  It is bordered to the north by the Arctic Ocean, to the east by the Atlantic Ocean, to the west and south by the Pacific Ocean, and to the southeast by South America and the Caribbean Sea.\n\nQuestion: Coleotechnites blastovora is a moth found in a continent entirely within what Hemisphere?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"moth_name\": {\n      \"type\": \"string\",\n      \"description\": \"The scientific name of the moth.\"\n    },\n    \"continent_found\": {\n      \"type\": \"string\",\n      \"description\": \"The continent where the moth is found.\"\n    },\n    \"hemisphere\": {\n      \"type\": \"string\",\n      \"description\": \"The hemisphere the continent is entirely within.\"\n    }\n  },\n  \"required\": [\n    \"moth_name\",\n    \"continent_found\",\n    \"hemisphere\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "moth_name": {
        "type": "string",
        "description": "The scientific name of the moth."
      },
      "continent_found": {
        "type": "string",
        "description": "The continent where the moth is found."
      },
      "hemisphere": {
        "type": "string",
        "description": "The hemisphere the continent is entirely within."
      }
    },
    "required": [
      "moth_name",
      "continent_found",
      "hemisphere"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
