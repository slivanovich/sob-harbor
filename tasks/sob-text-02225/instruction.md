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
Pellaea: Pellaea is a genus of ferns in the Cheilanthoideae subfamily of the Pteridaceae.  The genus name is derived from the Greek word πελλος ("pellos"), meaning "dark," and refers to the bluish-gray stems.  Members of the genus are commonly known as cliffbrakes.  They primarily grow in rocky habitats, including moist rocky canyons, slopes, and bluffs.

Sophronanthe: Sophronanthe is a small genus of flowering plants in the Veronica family.  The two included species are native to the Southeastern United States.  These species were recently included in the genus "Gratiola", but a study in 2008 showed that there are four distinct groups within "Gratiola" and resurrected the genus "Sophronanthe".

Veronica (plant): Veronica is the largest genus in the flowering plant family Plantaginaceae, with about 500 species; it was formerly classified in the family Scrophulariaceae.  Common names include speedwell, bird's eye, and gypsyweed.

Question: Veronica and Pellaea, both are flowering plants?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "are_both_flowering_plants": {
      "type": "boolean",
      "description": "Indicates whether both Pellaea and Veronica are flowering plants."
    },
    "pellaea_details": {
      "type": "object",
      "properties": {
        "is_flowering_plant": {
          "type": "boolean",
          "description": "True if Pellaea is a flowering plant, false otherwise."
        },
        "plant_type": {
          "type": "string",
          "description": "The general type of plant for Pellaea."
        }
      },
      "required": [
        "is_flowering_plant",
        "plant_type"
      ],
      "additionalProperties": false
    },
    "veronica_details": {
      "type": "object",
      "properties": {
        "is_flowering_plant": {
          "type": "boolean",
          "description": "True if Veronica is a flowering plant, false otherwise."
        },
        "plant_type": {
          "type": "string",
          "description": "The general type of plant for Veronica."
        },
        "family": {
          "type": "string",
          "description": "The plant family Veronica belongs to."
        }
      },
      "required": [
        "is_flowering_plant",
        "plant_type",
        "family"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "are_both_flowering_plants",
    "pellaea_details",
    "veronica_details"
  ],
  "additionalProperties": false
}
