{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nKingu (magazine): Kingu (キング , meaning \"King\" in English) was a Japanese monthly general interest and entertainment magazine published in Tokyo, Japan.  The magazine existed between 1925 and 1957.  It was the first popular best-selling Japanese magazine.  It was also one of two most significant magazines in mid-twentieth century Japan, the other one being \"Ie no Hikari\".\n\nKalima (magazine): Kalima (meaning both \"Word\" and \"the act of Speaking\" in English) was a French language monthly women's magazine and news magazine published in Morocco between 1986 and 1989.  The magazine was a feminist publication.\n\nJane (magazine): Jane was an American magazine created to appeal to the women who grew up reading \"Sassy Magazine\"; Jane Pratt was the founding editor of each.  Its original target audience (pitched to advertisers) was aged 18–34, and was designed to appeal to women who did not like the typical women's magazine format.  Pratt originally intended the magazine to be named \"Betty\", but she was voted down by everyone else involved in the making of the magazine.\n\nInvestir: Investir was a French language monthly business magazine published in Paris, France, between 1974 and 2011.\n\nMieux Vivre Votre Argent: Mieux Vivre Votre Argent (also known as \"MVVA\") is a French language monthly business magazine published in Paris, France.\n\nGael (magazine): Gael is a French language monthly women's and lifestyle magazine published monthly in Mechelen, Belgium.\n\nPleine Vie: Pleine Vie (meaning \"Full Life\" in English) is a French language monthly general interest and women's magazine published in Paris, France.\n\nModes &amp; Travaux: Modes & Travaux is a French language monthly general interest women's magazine based in Paris, France.  Founded in 1919 it is one of the oldest magazines in the country.\n\nLe Monde mensuel: Le Monde mensuel was a French language monthly news magazine published in Paris, France, from 2010 to 2014.  It mostly covered selected articles from \"Le Monde\" published in the preceding month.\n\nContenido: Contenido is a Mexican monthly general interest magazine covering articles on the experience of people.  The magazine was founded in 1963.  The headquarters of the magazine, which is published by Editorial Contenido S.A. DE C.V., is in Mexico City.  The magazine is similar to \"Reader's Digest\".\n\nQuestion: What is is a French language monthly general interest and women's magazine published in Paris, France, Jane or Pleine Vie?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"magazine_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the magazine.\"\n    },\n    \"language\": {\n      \"type\": \"string\",\n      \"description\": \"The primary language of the magazine.\"\n    },\n    \"frequency\": {\n      \"type\": \"string\",\n      \"description\": \"How often the magazine is published (e.g., monthly, weekly).\"\n    },\n    \"categories\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of categories or interests the magazine covers.\"\n    },\n    \"publication_city\": {\n      \"type\": \"string\",\n      \"description\": \"The city where the magazine is published.\"\n    },\n    \"publication_country\": {\n      \"type\": \"string\",\n      \"description\": \"The country where the magazine is published.\"\n    },\n    \"is_correct_answer\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if this magazine is the correct answer to the question, false otherwise.\"\n    }\n  },\n  \"required\": [\n    \"magazine_name\",\n    \"language\",\n    \"frequency\",\n    \"categories\",\n    \"publication_city\",\n    \"publication_country\",\n    \"is_correct_answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "magazine_name": {
        "type": "string",
        "description": "The name of the magazine."
      },
      "language": {
        "type": "string",
        "description": "The primary language of the magazine."
      },
      "frequency": {
        "type": "string",
        "description": "How often the magazine is published (e.g., monthly, weekly)."
      },
      "categories": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of categories or interests the magazine covers."
      },
      "publication_city": {
        "type": "string",
        "description": "The city where the magazine is published."
      },
      "publication_country": {
        "type": "string",
        "description": "The country where the magazine is published."
      },
      "is_correct_answer": {
        "type": "boolean",
        "description": "True if this magazine is the correct answer to the question, false otherwise."
      }
    },
    "required": [
      "magazine_name",
      "language",
      "frequency",
      "categories",
      "publication_city",
      "publication_country",
      "is_correct_answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
