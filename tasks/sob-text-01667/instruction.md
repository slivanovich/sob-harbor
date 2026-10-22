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
Brownea coccinea: Brownea coccinea is a species in the subfamily Caesalpinioideae of the family Fabaceae.  Common names include Scarlet Flame Bean, Mountain Rose, Rose of Venezuela and Cooper Hoop.

Brownea santanderensis: Brownea santanderensis is a species of legume in the Fabaceae family.

Brownea grandiceps: Brownea grandiceps is a species of tree in the family Fabaceae.  Its common names include the rose of Venezuela and the scarlet flame bean.  It originated in South America but is now widely grown as a decorative tree in tropical gardens.

Ecballium: Ecballium is a genus of flowering plants in the family Cucurbitaceae containing a single species, Ecballium elaterium, also called the squirting cucumber or exploding cucumber (but not to be confused with "Cyclanthera explodens").  It gets its unusual name from the fact that, when ripe, it squirts a stream of mucilaginous liquid containing its seeds, which can be seen with the naked eye.  It is thus considered to have rapid plant movement.

Brownea: Brownea is a genus of about 30 species in the family Fabaceae, subfamily Detarioideae.  The genus is native to tropical regions of the Americas.  The species are shrubs and trees growing to 20 m tall.

Question: Which has more species, Ecballium or Brownea?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "genus_comparison_summary": {
      "type": "string",
      "description": "A summary statement indicating which genus has more species."
    },
    "genera_details": {
      "type": "array",
      "description": "Details for each genus involved in the comparison.",
      "items": {
        "type": "object",
        "properties": {
          "genus_name": {
            "type": "string",
            "description": "The name of the genus."
          },
          "species_count": {
            "type": "integer",
            "description": "The number of species in the genus."
          }
        },
        "required": [
          "genus_name",
          "species_count"
        ],
        "additionalProperties": false
      }
    },
    "genus_with_more_species": {
      "type": "string",
      "description": "The name of the genus that has more species."
    },
    "species_count_difference": {
      "type": "integer",
      "description": "The numerical difference in species count between the two genera."
    }
  },
  "required": [
    "genus_comparison_summary",
    "genera_details",
    "genus_with_more_species",
    "species_count_difference"
  ],
  "additionalProperties": false
}
