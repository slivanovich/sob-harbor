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
Catasetum: Catasetum, abbreviated as Ctsm in horticultural trade, is a genus of showy epiphytic Orchids, family Orchidaceae, subfamily Epidendroideae, tribe Cymbidieae, subtribe Catasetinae, with 166 species, many of which are highly prized in horticulture.

Anisodontea: Anisodontea is a genus in the tribe Malveae in the family Malvaceae.  It comprises twenty-one species native to South Africa.  Members of the genus typically bear toothed leaves with three or five palmate, uneven lobes.  Members of the genus also typically bear flowers with a pubescent calyx, a five-petaled corolla streaked from the center and pink to magenta in color, and stamens with anthers of a dark color.

Question: Are Anisodontea and Catasetum both genus of plants ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_context": {
      "type": "string",
      "description": "The original question asked."
    },
    "genera_information": {
      "type": "array",
      "description": "Details about each genus mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "genus_name": {
            "type": "string",
            "description": "The name of the genus."
          },
          "is_identified_as_genus": {
            "type": "boolean",
            "description": "Whether the entity is explicitly identified as a genus in the context."
          },
          "is_part_of_plant_kingdom": {
            "type": "boolean",
            "description": "Whether the genus belongs to the plant kingdom, based on its family."
          },
          "family_name": {
            "type": "string",
            "description": "The family to which the genus belongs."
          }
        },
        "required": [
          "genus_name",
          "is_identified_as_genus",
          "is_part_of_plant_kingdom",
          "family_name"
        ],
        "additionalProperties": false
      }
    },
    "overall_conclusion": {
      "type": "object",
      "properties": {
        "all_mentioned_are_plant_genera": {
          "type": "boolean",
          "description": "The final answer to whether all mentioned entities are genera of plants."
        }
      },
      "required": [
        "all_mentioned_are_plant_genera"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "question_context",
    "genera_information",
    "overall_conclusion"
  ],
  "additionalProperties": false
}
