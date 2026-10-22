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
Galanthus elwesii: Galanthus elwesii (Elwes's snowdrop, greater snowdrop) is one of a number of species of the genus "Galanthus", herbaceous, perennial, bulbous plants belonging to the family Amaryllidaceae.  It is a native of the Caucasus.

Galanthus nivalis: Galanthus nivalis, the snowdrop or common snowdrop, is the best-known and most widespread of the 20 species in its genus, "Galanthus".  Snowdrops are among the first bulbs to bloom in spring and can form impressive carpets of white in areas where they are native or have been naturalised.  They should not be confused with the snowflakes, in the genera "Leucojum" and "Acis".

Galanthus: Galanthus (snowdrop; Greek "gála" "milk", "ánthos" "flower") is a small genus of about 20 species of bulbous perennial herbaceous plants in the family Amaryllidaceae.  The plants have two linear leaves and a single small white drooping bell shaped flower with six petal-like (petaloid) tepals in two circles (whorls).  The smaller inner petals have green markings.

Rhodanthemum: Rhodanthemum syn.  "Chrysanthemopsis", "Pyrethropsis" (Moroccan daisy), is a genus of flowering plants in the family Asteraceae, mostly native to exposed rocky places in Northern Africa (Morocco and Algeria).  Formerly included in either "Chrysanthemum" or "Leucanthemum", the 10 or 15 species of "Rhodanthemum" display many similarities to their former parents, with composite daisy-like flowers.  They are mat-forming, prostrate perennials or subshrubs, and some are cultivated as ornamental plants.

Question: Which genus has more species, Galanthus or Rhodanthemum?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "genus_comparison": {
      "type": "object",
      "properties": {
        "first_genus": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "species_count": {
              "type": "integer"
            }
          },
          "required": [
            "name",
            "species_count"
          ],
          "additionalProperties": false
        },
        "second_genus": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "species_count_description": {
              "type": "string"
            }
          },
          "required": [
            "name",
            "species_count_description"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "first_genus",
        "second_genus"
      ],
      "additionalProperties": false
    },
    "genus_with_more_species": {
      "type": "string"
    },
    "comparison_summary": {
      "type": "string"
    }
  },
  "required": [
    "genus_comparison",
    "genus_with_more_species",
    "comparison_summary"
  ],
  "additionalProperties": false
}
