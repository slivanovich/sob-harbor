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
Verbascum: Verbascum ( ), common name mullein (sg. )  (also known as velvet plant), is a genus of about 250 species of flowering plants in the figwort family Scrophulariaceae.  They are native to Europe and Asia, with the highest species diversity in the Mediterranean.

Selago: Selago is a genus of plant in family Scrophulariaceae, closely related to "Scrophularia" and "Verbascum".  It contains around 190 species, mostly in southern Africa; two are listed on the IUCN Red List:

Jasmine: Jasmine (taxonomic name Jasminum ) is a genus of shrubs and vines in the olive family (Oleaceae).  It contains around 200 species native to tropical and warm temperate regions of Eurasia, Australasia and Oceania.  Jasmines are widely cultivated for the characteristic fragrance of their flowers.  A number of unrelated plants contain the word "Jasmine" in their common names (see Other plants called "Jasmine").

Question: Which genus Verbascum or Jasmine contains more species ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "comparison_result": {
      "type": "string",
      "description": "The genus that contains more species."
    },
    "genera_compared": {
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
            "description": "The approximate number of species in the genus."
          }
        },
        "required": [
          "genus_name",
          "species_count"
        ],
        "additionalProperties": false
      }
    },
    "comparison_details": {
      "type": "object",
      "description": "Summary of the comparison.",
      "properties": {
        "comparison_type": {
          "type": "string",
          "description": "The attribute being compared (e.g., 'species_count')."
        },
        "higher_count_genus": {
          "type": "string",
          "description": "The genus identified as having the higher count."
        },
        "higher_count_value": {
          "type": "integer",
          "description": "The count value for the genus with the higher count."
        }
      },
      "required": [
        "comparison_type",
        "higher_count_genus",
        "higher_count_value"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "comparison_result",
    "genera_compared",
    "comparison_details"
  ],
  "additionalProperties": false
}
