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
Typhonium mirabile: Typhonium mirabile is a species of flowering plant in the Araceae family.  It is found growing in Australia in eucalypts woodlands at the base of "Cycas" plants.  It was first described in 1992 by Alistair Hay, as "Lazarum mirabile" and was the only species in the genus "Lazarum".  In 1997, Hay published a paper transferring it to the genus "Typhonium".

Heuchera: Heuchera is a genus of evergreen, herbaceous perennial plants in the family Saxifragaceae, all native to North America.  Common names include alumroot and coral bells.

Cycas: Cycas is the type genus and the only genus recognised in the family Cycadaceae.  About 113 species are accepted.  "Cycas circinalis", a species endemic to India was the first cycad species to be described and was the type of the generic name, "Cycas".  The best-known "Cycas" species is "Cycas revoluta".  "Cycas" is a very ancient genus of trees.  The group achieved its maximum diversity in the Jurassic and Cretaceous periods, when it was distributed almost worldwide.  At the end of the Cretaceous, when the non-avian dinosaurs became extinct, so did most of the cycas in the Northern Hemisphere.

Micranthes: Micranthes is a genus of flowering plants in the saxifrage family.  It was formerly included within the genus "Saxifraga" until recent DNA evidence showed the members of what is now "Micranthes" are more closely related to "Boykinia" and "Heuchera" than to other members of the genus "Saxifraga".

Question: Are Cycas and Heuchera both genus of plants ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_asked": {
      "type": "string",
      "description": "The original question posed by the user."
    },
    "is_both_genus": {
      "type": "boolean",
      "description": "True if both specified entities are confirmed to be genera of plants based on the context, false otherwise."
    },
    "plant_entities_analysis": {
      "type": "array",
      "description": "Detailed analysis for each plant entity mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "entity_name": {
            "type": "string",
            "description": "The name of the plant entity."
          },
          "is_confirmed_genus": {
            "type": "boolean",
            "description": "True if the context explicitly states this entity is a genus."
          },
          "taxonomic_family": {
            "type": "string",
            "description": "The taxonomic family to which the entity belongs, if specified in the context."
          },
          "context_evidence": {
            "type": "string",
            "description": "A snippet from the context that confirms the entity's genus status."
          }
        },
        "required": [
          "entity_name",
          "is_confirmed_genus",
          "taxonomic_family",
          "context_evidence"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "question_asked",
    "is_both_genus",
    "plant_entities_analysis"
  ],
  "additionalProperties": false
}
