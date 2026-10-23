{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJessie Burton: Jessie Burton (born 1982) is an English author and actress.  As of February 2017 she has published two novels, \"The Miniaturist\" and \"The Muse\".\n\nThe Miniaturist: The Miniaturist is the 2014 debut novel of English actress and author Jessie Burton.  An international bestseller, it was the focus of a publishers bidding war at the 2013 London Book Fair.  Set in Amsterdam in 1686/7, the novel was inspired by Petronella Oortman's doll's house on display at the Rijksmuseum.  It does not otherwise attempt to be a biographical novel.\n\nQuestion: When was the author of \"The Miniaturist\" born? \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"author_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the author.\"\n    },\n    \"book_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the book mentioned in the question.\"\n    },\n    \"author_birth_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth year of the author.\"\n    }\n  },\n  \"required\": [\n    \"author_name\",\n    \"book_title\",\n    \"author_birth_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "author_name": {
        "type": "string",
        "description": "The name of the author."
      },
      "book_title": {
        "type": "string",
        "description": "The title of the book mentioned in the question."
      },
      "author_birth_year": {
        "type": "integer",
        "description": "The birth year of the author."
      }
    },
    "required": [
      "author_name",
      "book_title",
      "author_birth_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
