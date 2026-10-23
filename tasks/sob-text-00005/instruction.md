{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGeorge VI: George VI (Albert Frederick Arthur George; 14 December 1895 – 6 February 1952) was King of the United Kingdom and the Dominions of the British Commonwealth from 11 December 1936 until his death.  He was the last Emperor of India and the first Head of the Commonwealth.\n\n1965 Birthday Honours: The Queen's Birthday Honours 1965 were appointments in many of the Commonwealth realms of Queen Elizabeth II to various orders and honours to reward and highlight good works by citizens of those countries.  The appointments were made to celebrate the official birthday of The Queen.  The announcement date varies from year to year.  The 1965 Queen's Birthday Honours were announced on 12 June for the United Kingdom, Australia, New Zealand, Sierra Leone, Jamaica, Trinidad and Tobago, Malawi, and the Gambia.\n\n1951 Birthday Honours: The King's Birthday Honours 1951 were appointments in many of the Commonwealth realms of King George VI to various orders and honours to reward and highlight good works by citizens of those countries.  The appointments were made to celebrate the official birthday of the King, and were published on 1 June 1951 for the British Empire, Australia, New Zealand, Ceylon, and Pakistan.  These were the last Birthday Honours awarded by George VI, who died eight months later.\n\n2015 Birthday Honours: The 2015 Queen's Birthday Honours are appointments by some of the 16 Commonwealth realms of Queen Elizabeth II to various orders and honours to reward and highlight good works by citizens of those countries.  The Birthday Honours are awarded as part of the Queen's Official Birthday celebrations during the month of June.  The Queen's Birthday Honours were announced on 1 June 2015 in New Zealand, on 8 June in Australia, and on 12 June in the United Kingdom, in Grenada, Papua New Guinea, Solomon Islands, Tuvalu, Saint Lucia and Belize.\n\n2014 Birthday Honours: The 2014 Birthday Honours were appointments by some of the 16 Commonwealth realms of Queen Elizabeth II to various orders and honours to reward and highlight good works by citizens of those countries.  The Birthday Honours are awarded as part of the Queen's Official Birthday celebrations during the month of June.  The Queen's Birthday Honours were announced on 14 June 2014 in the United Kingdom, on 9 June 2014 in Australia, on 2 June 2014 in New Zealand, on 14 June 2014 in Grenada, Papua New Guinea, Solomon Islands, Tuvalu, Saint Lucia and Belize.\n\n1938 Birthday Honours: The King's Birthday Honours 1938 were appointments in many of the Commonwealth realms of King George VI to various orders and honours to reward and highlight the meritorious work of his subjects in those countries.  The appointments were made to celebrate the King's official birthday and for the United Kingdom and Colonies were announced on 7 June 1938.\n\n2013 Birthday Honours: The 2013 Birthday Honours were appointments by some of the 16 Commonwealth realms of Queen Elizabeth II to various orders and honours to reward and highlight good works by citizens of those countries.  The Birthday Honours are awarded as part of the Queen's Official Birthday celebrations during the month of June.  The Queen's Birthday Honours were announced on 15 June 2013 in the United Kingdom, on 10 June 2013 in Australia on 3 June 2013 in New Zealand, on 15 June 2013 in Grenada, Papua New Guinea, Solomon Islands, Tuvalu, Saint Lucia and Belize.\n\n2017 Birthday Honours: The 2017 Queen's Birthday Honours are appointments by some of the 16 Commonwealth realms of Queen Elizabeth II to various orders and honours to reward and highlight good works by citizens of those countries.  The Birthday Honours are awarded as part of the Queen's Official Birthday celebrations during the month of June.  The Queen's Birthday Honours for the United Kingdom were announced on 16 June; the honours for New Zealand were announced on 5 June and for Australia on 12 June.\n\n1941 Birthday Honours: The King's Birthday Honours 1941 were appointments in the British Empire of King George VI to various orders and honours to reward and highlight good works by citizens of various countries.  The appointments were made to celebrate the official birthday of The King, and were published on 6 June 1941.\n\n2016 Birthday Honours: The 2016 Queen's Birthday Honours are appointments by some of the 16 Commonwealth realms of Queen Elizabeth II to various orders and honours to reward and highlight good works by citizens of those countries.  The Birthday Honours are awarded as part of the Queen's Official Birthday celebrations during the month of June.  The Queen's Birthday Honours were announced on 6 June 2016 in New Zealand and 10 June in the United Kingdom.\n\nQuestion: Who was King of the United Kingdom and the Dominions of the British Commonwealth in 1941, when the King's Birthday Honours appointments were made?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"monarch_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the monarch.\"\n    },\n    \"honours_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the Birthday Honours were awarded.\"\n    },\n    \"honours_type\": {\n      \"type\": \"string\",\n      \"description\": \"The specific name of the honours event.\"\n    },\n    \"monarch_title\": {\n      \"type\": \"string\",\n      \"description\": \"The primary title held by the monarch at the time of the honours.\"\n    }\n  },\n  \"required\": [\n    \"monarch_name\",\n    \"honours_year\",\n    \"honours_type\",\n    \"monarch_title\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "monarch_name": {
        "type": "string",
        "description": "The name of the monarch."
      },
      "honours_year": {
        "type": "integer",
        "description": "The year the Birthday Honours were awarded."
      },
      "honours_type": {
        "type": "string",
        "description": "The specific name of the honours event."
      },
      "monarch_title": {
        "type": "string",
        "description": "The primary title held by the monarch at the time of the honours."
      }
    },
    "required": [
      "monarch_name",
      "honours_year",
      "honours_type",
      "monarch_title"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
