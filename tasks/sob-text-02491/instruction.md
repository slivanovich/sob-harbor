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
Onoclea: Onoclea is a genus of plants in the Onocleaceae family, native to moist habitats in eastern Asia and eastern North America.  They are deciduous ferns with sterile fronds arising from creeping rhizomes in spring, dying down at first frost.  Fertile fronds appear in late summer.  Depending on the authority, the genus contains one to five species.

Bunchosia: Bunchosia is a genus in the Malpighiaceae, a family of about 75 genera of flowering plants in the order Malpighiales.  It contains roughly 75 species of trees and shrubs, which are native to dry woodlands, savannas, and wet forests.  Their range extends from Mexico and the Caribbean to southeastern Brazil and adjacent Argentina.  "Bunchosia" is one of three arborescent genera of Malpighiaceae with fleshy, bird-dispersed fruits.

Question: Are both Bunchosia and Onoclea genus of plants?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_context": {
      "type": "string",
      "description": "Describes the main subject of the question."
    },
    "onoclea_classification": {
      "type": "object",
      "properties": {
        "is_genus": {
          "type": "boolean",
          "description": "Indicates if Onoclea is classified as a genus."
        },
        "is_plant": {
          "type": "boolean",
          "description": "Indicates if Onoclea is a genus of plants."
        },
        "family": {
          "type": "string",
          "description": "The botanical family Onoclea belongs to."
        }
      },
      "required": [
        "is_genus",
        "is_plant",
        "family"
      ],
      "additionalProperties": false
    },
    "bunchosia_classification": {
      "type": "object",
      "properties": {
        "is_genus": {
          "type": "boolean",
          "description": "Indicates if Bunchosia is classified as a genus."
        },
        "is_plant": {
          "type": "boolean",
          "description": "Indicates if Bunchosia is a genus of plants."
        },
        "family": {
          "type": "string",
          "description": "The botanical family Bunchosia belongs to."
        }
      },
      "required": [
        "is_genus",
        "is_plant",
        "family"
      ],
      "additionalProperties": false
    },
    "both_are_plant_genera": {
      "type": "boolean",
      "description": "The final answer to whether both Onoclea and Bunchosia are genera of plants."
    }
  },
  "required": [
    "question_context",
    "onoclea_classification",
    "bunchosia_classification",
    "both_are_plant_genera"
  ],
  "additionalProperties": false
}
