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
Hesperaloe: Hesperaloe (false yucca) is a genus of flowering plants in the family Asparagaceae, subfamily Agavoideae.  It contains perennial yucca-like plants with long, narrow leaves produced in a basal rosette and flowers borne on long panicles or racemes.  The species are native to the arid parts of Texas in the United States and Mexico and are sometimes cultivated as xerophytic ornamental plants.

Theatre of ancient Greece: The ancient Greek drama was a theatrical culture that flourished in ancient Greece from c. 700 BC.  The city-state of Athens, which became a significant cultural, political, and military power during this period, was its center, where it was institutionalised as part of a festival called the Dionysia, which honoured the god Dionysus.  Tragedy (late 500 BC), comedy (490 BC), and the satyr play were the three dramatic genres to emerge there.  Athens exported the festival to its numerous colonies and allies in order to promote a common cultural identity.

Helen (play): Helen (Ancient Greek: Ἑλένη , "Helenē") is a drama by Euripides about Helen, first produced in 412 BC for the Dionysia in a trilogy that also contained Euripides' lost "Andromeda".  The play has much in common with "Iphigenia in Tauris", one of the playwright's later works.

Dionysia (plant): Dionysia is a genus containing 49 species of flowering plants in the family Primulaceae.  They are small, cushion-forming alpines native to mountains in central Asia.  They are usually evergreen perennials with felted leaves, covered with bright yellow or pink, five-petalled flowers in spring.  They are often difficult to cultivate if the correct conditions are not provided.

Question: What do Dionysia and Hesperaloe have in common?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "common_characteristics": {
      "type": "array",
      "description": "A list of high-level characteristics shared by both entities.",
      "items": {
        "type": "string"
      }
    },
    "shared_botanical_classification": {
      "type": "object",
      "description": "Specific botanical classifications that both entities share.",
      "properties": {
        "is_flowering_plant": {
          "type": "boolean",
          "description": "True if both are classified as flowering plants."
        },
        "is_perennial": {
          "type": "boolean",
          "description": "True if both are perennial plants."
        },
        "is_genus": {
          "type": "boolean",
          "description": "True if both are classified as a genus."
        }
      },
      "required": [
        "is_flowering_plant",
        "is_perennial",
        "is_genus"
      ],
      "additionalProperties": false
    },
    "compared_plant_genera": {
      "type": "array",
      "description": "Details for each plant genus being compared.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the plant genus."
          },
          "family": {
            "type": "string",
            "description": "The botanical family of the plant genus."
          }
        },
        "required": [
          "name",
          "family"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "common_characteristics",
    "shared_botanical_classification",
    "compared_plant_genera"
  ],
  "additionalProperties": false
}
