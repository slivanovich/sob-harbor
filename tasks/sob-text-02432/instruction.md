Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Jessie Burton: Jessie Burton (born 1982) is an English author and actress.  As of February 2017 she has published two novels, "The Miniaturist" and "The Muse".

The Miniaturist: The Miniaturist is the 2014 debut novel of English actress and author Jessie Burton.  An international bestseller, it was the focus of a publishers bidding war at the 2013 London Book Fair.  Set in Amsterdam in 1686/7, the novel was inspired by Petronella Oortman's doll's house on display at the Rijksmuseum.  It does not otherwise attempt to be a biographical novel.

Question: When was the author of "The Miniaturist" born? 

Respond with JSON matching this schema:
{
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
}
