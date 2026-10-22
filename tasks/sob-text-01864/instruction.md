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
Gladiolus: Gladiolus (from Latin, the diminutive of "gladius", a sword,) is a genus of perennial cormous flowering plants in the iris family (Iridaceae).

List of Gladiolus cultivars: This is a list of cultivars of the Gladiolus genus of flowering plants.

Aptenia: Aptenia is a small genus of flowering plants in the family Aizoaceae.  They are native to southern Africa.  The genus name is from the Greek "a-" (not) and "ptenos" (winged), and refers to the wingless fruit capsules.

Question: Are Aptenia and Gladiolus both flowering plants?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_asked": {
      "type": "string",
      "description": "The original question posed."
    },
    "genus_1": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "Name of the first genus."
        },
        "is_flowering_plant": {
          "type": "boolean",
          "description": "Indicates if the genus is a flowering plant."
        },
        "family": {
          "type": "string",
          "description": "The plant family to which the genus belongs."
        }
      },
      "required": [
        "name",
        "is_flowering_plant",
        "family"
      ],
      "additionalProperties": false
    },
    "genus_2": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "Name of the second genus."
        },
        "is_flowering_plant": {
          "type": "boolean",
          "description": "Indicates if the genus is a flowering plant."
        },
        "family": {
          "type": "string",
          "description": "The plant family to which the genus belongs."
        }
      },
      "required": [
        "name",
        "is_flowering_plant",
        "family"
      ],
      "additionalProperties": false
    },
    "both_are_flowering_plants": {
      "type": "boolean",
      "description": "True if both genera are flowering plants, false otherwise."
    }
  },
  "required": [
    "question_asked",
    "genus_1",
    "genus_2",
    "both_are_flowering_plants"
  ],
  "additionalProperties": false
}
