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
Photinia: Photinia ( ) is a genus of about 40–60 species of small trees and large shrubs, but the taxonomy has recently varied greatly, with the genera "Heteromeles", "Stranvaesia" and "Aronia" sometimes included in "Photinia".

Nandina: Nandina domestica ( ) commonly known as nandina, heavenly bamboo or sacred bamboo, is a species of flowering plant in the family Berberidaceae, native to eastern Asia from the Himalayas to Japan.  It is the only member of the monotypic genus Nandina.

Question: Which genus has more species, Nandina or Photinia 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "comparison_result": {
      "type": "object",
      "properties": {
        "genus_with_more_species": {
          "type": "string",
          "description": "The name of the genus identified as having more species."
        },
        "more_species_count_range": {
          "type": "string",
          "description": "The range of species count for the genus with more species, as stated in the context."
        },
        "less_species_genus": {
          "type": "string",
          "description": "The name of the genus identified as having fewer species."
        },
        "less_species_count": {
          "type": "integer",
          "description": "The exact species count for the genus with fewer species."
        }
      },
      "required": [
        "genus_with_more_species",
        "more_species_count_range",
        "less_species_genus",
        "less_species_count"
      ],
      "additionalProperties": false
    },
    "photinia_details": {
      "type": "object",
      "properties": {
        "genus_name": {
          "type": "string"
        },
        "species_count_range": {
          "type": "string",
          "description": "The stated range of species for Photinia."
        }
      },
      "required": [
        "genus_name",
        "species_count_range"
      ],
      "additionalProperties": false
    },
    "nandina_details": {
      "type": "object",
      "properties": {
        "genus_name": {
          "type": "string"
        },
        "species_count": {
          "type": "integer",
          "description": "The exact species count for Nandina."
        }
      },
      "required": [
        "genus_name",
        "species_count"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "comparison_result",
    "photinia_details",
    "nandina_details"
  ],
  "additionalProperties": false
}
