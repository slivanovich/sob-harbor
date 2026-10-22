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
Syzygium guineense: Syzygium guineense (Bambara: "Kokisa" ) is a leafy forest tree of the Myrtaceae family, found in many parts of Africa both wild and domesticated.  Both its fruits and leaves are edible; the pulp and the fruit skin are sucked and the seed discarded.  It is sometimes called "waterberry", but this may also refer to other species of "Syzygium".

Syzygium: Syzygium is a genus of flowering plants that belongs to the myrtle family, Myrtaceae.  The genus comprises about 1200–1800 species, and has a native range that extends from Africa and Madagascar through southern Asia east through the Pacific.  Its highest levels of diversity occur from Malaysia to northeastern Australia, where many species are very poorly known and many more have not been described taxonomically.

Cyanotis: Cyanotis (syn.  "Tonningia") is a genus of mainly perennial plants in the family Commelinaceae, first described in 1825.  It is native to Africa, southern Asia, and northern Australia.

Question: Are the genuses Cyanotis and Syzygium both found in Africa?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_context": {
      "type": "string",
      "description": "Describes the overall topic of the question."
    },
    "genus_distribution_details": {
      "type": "array",
      "description": "Details about each genus mentioned in the question and its native distribution.",
      "items": {
        "type": "object",
        "properties": {
          "genus_name": {
            "type": "string",
            "description": "The name of the plant genus."
          },
          "native_range_description": {
            "type": "string",
            "description": "The description of the genus's native range as found in the context."
          },
          "is_native_to_africa": {
            "type": "boolean",
            "description": "Indicates whether the genus's native range includes Africa."
          }
        },
        "required": [
          "genus_name",
          "native_range_description",
          "is_native_to_africa"
        ],
        "additionalProperties": false
      }
    },
    "are_both_native_to_africa": {
      "type": "boolean",
      "description": "The final answer to whether both genuses are found in Africa."
    }
  },
  "required": [
    "question_context",
    "genus_distribution_details",
    "are_both_native_to_africa"
  ],
  "additionalProperties": false
}
