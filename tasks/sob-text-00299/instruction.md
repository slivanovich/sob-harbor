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
Monanthes: Monanthes is a genus of small, succulent, subtropical plants of the Crassulaceae family.  The about ten species are mostly endemic to the Canary Islands and Savage Islands, with some found on Madeira.  Its center of diversity is Tenerife, with seven species occurring on this island.  On Fuerteventura and Lanzarote, only "M. laxiflora" occurs.

Aichryson: Aichryson is a genus of about 15 species of succulent, subtropical plants, mostly native to the Canary Islands, with a few in the Azores, Madeira and Morocco, and one in Portugal.

Glottiphyllum: Glottiphyllum is a genus of about 57 species of succulent subtropical plants of the family "Aizoaceae".

Chrysosplenium: Chrysosplenium (golden saxifrage or golden-saxifrage) is a genus of 57 species of flowering plants in the family Saxifragaceae.  Species can be found throughout the arctic and northern temperate parts of the Northern Hemisphere, with the highest species diversity in eastern Asia; two species are found disjunctly in South America.

Glottiphyllum longum: Glottiphyllum longum is a species of succulent plant in the Aizoaceae family, native to South Africa.

Ariocarpus: Ariocarpus is a genus of 8 species of succulent, subtropical plants of the Cactaceae family.

Glottiphyllum cruciatum: Glottiphyllum cruciatum is a species that are part of over 50 succulents that are subtropical plants of the family "Aizoaceae".  The plant has many synonyms including "Glottiphyllum angustum".

Aeonium: Aeonium (tree houseleek) is a genus of about 35 species of succulent, subtropical plants of the family Crassulaceae.  Many species are popular in horticulture.  The genus name comes from the ancient Greek "aionos" (ageless).  While most of them are native to the Canary Islands, some are found in Madeira, Morocco, and in East Africa (for example in the Semien Mountains of Ethiopia).

Glottiphyllum uncatum: Glottiphyllum uncatum is a species of succulent plant in the Aizoaceae family, native to South Africa.

Arthrocereus: Arthrocereus is a genus of cactus, originating from southern Minas Gerais, Brazil.

Question: What is a genus of about 57 species of succulent subtropical plants of the family "Aizoaceae", Arthrocereus or Glottiphyllum ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "identified_genus_name": {
      "type": "string",
      "description": "The name of the genus that matches the description."
    },
    "species_count": {
      "type": "integer",
      "description": "The approximate number of species in the genus."
    },
    "plant_characteristics": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of characteristics describing the plants in the genus."
    },
    "family": {
      "type": "string",
      "description": "The botanical family to which the genus belongs."
    },
    "is_correct_answer": {
      "type": "boolean",
      "description": "Indicates if this genus is the correct answer to the question posed."
    }
  },
  "required": [
    "identified_genus_name",
    "species_count",
    "plant_characteristics",
    "family",
    "is_correct_answer"
  ],
  "additionalProperties": false
}
