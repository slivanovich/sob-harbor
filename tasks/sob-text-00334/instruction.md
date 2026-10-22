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
Bessera: Bessera is a genus of Mexican plants in the cluster lily subfamily within the asparagus family.  It is a small genus of 3 known species of mostly herbaceous flowering plants with corms.  They have flowers with petals and petaloid sepals (tepals) with compound pistils.

Sesleria: Sesleria is a Eurasian and North African genus of perennial plants in the grass family.

Sesleria caerulea: Sesleria caerulea, known as blue moor-grass, is a species of perennial grass in the Poaceae family, native to Europe.

Sesleria insularis: Sesleria insularis is a species of perennial grass in the Poaceae family, with culms 30–65 cm long.

Sesleria albicans: Sesleria albicans is a species of perennial grass in the Poaceae family which can be found throughout Europe.

Sesleria heufleriana: Sesleria heufleriana is a species of perennial grass in the Poaceae family, native to central, southeastern, and eastern Europe and the Caucasus.  Culms are erect, ranging from 30–70 cm long; leaf-blades are conduplicate or convolute, and 20–35 cm long by 2–3 mm wide.

Sesleria argentea: Sesleria argentea is a species of perennial grass in the Poaceae family.  It is 35 – long with a 0.5 – long ciliolate membrane.  Its leaves are either conduplicate or convolute, and are 10 – long and 3 – wide.  It also has a linear panicle spiciform which is 3.5 – long and 0.5 – wide.

Question: Both Bessera and Sesleria are?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "common_classification": {
      "type": "string",
      "description": "The common biological classification level for both entities."
    },
    "common_plant_type": {
      "type": "string",
      "description": "The general type of organism both entities represent."
    },
    "genera_information": {
      "type": "array",
      "description": "Detailed information about each genus mentioned.",
      "items": {
        "type": "object",
        "properties": {
          "genus_name": {
            "type": "string",
            "description": "The name of the genus."
          },
          "family": {
            "type": "string",
            "description": "The plant family the genus belongs to."
          },
          "origin_regions": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Regions where the genus is native."
          },
          "is_perennial": {
            "type": "boolean",
            "description": "Indicates if the genus consists of perennial plants."
          },
          "number_of_known_species": {
            "type": "integer",
            "description": "The number of known species within the genus."
          }
        },
        "required": [
          "genus_name",
          "family",
          "origin_regions"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "common_classification",
    "common_plant_type",
    "genera_information"
  ],
  "additionalProperties": false
}
