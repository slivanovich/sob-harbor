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
Billardiera: Billardiera is a genus of small vines and shrubs which is endemic to Australia.  The genus was first formally described in 1793 by botanist James Edward Smith who named it in honour of Jacques Labillardière, a French botanist.

Calothamnus: Calothamnus is a genus of shrubs in the family Myrtaceae and is endemic to the south-west of Western Australia.  The common names one-sided bottlebrush or claw flower are given to some species due to their having the flowers clustered on one side of the stem or because of the claw-like appearance of their flowers.  "Calothamnus" species are generally medium to tall woody shrubs with crowded leaves.  In most species the leaves are crowded and linear in shape, and the flowers are usually arranged in dense clusters.  The petals are small and fall off the flower soon after it opens but the stamens are long, numerous and usually bright red.

Question: Are Billardiera and Calothamnus both types of genuses?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_topic": {
      "type": "string",
      "description": "The general topic of the question."
    },
    "entity_1": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the first entity mentioned."
        },
        "is_genus": {
          "type": "boolean",
          "description": "Indicates if the entity is described as a genus."
        },
        "type_description": {
          "type": "string",
          "description": "A brief description of what the entity is (e.g., 'small vines and shrubs')."
        }
      },
      "required": [
        "name",
        "is_genus",
        "type_description"
      ],
      "additionalProperties": false
    },
    "entity_2": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the second entity mentioned."
        },
        "is_genus": {
          "type": "boolean",
          "description": "Indicates if the entity is described as a genus."
        },
        "type_description": {
          "type": "string",
          "description": "A brief description of what the entity is (e.g., 'shrubs')."
        }
      },
      "required": [
        "name",
        "is_genus",
        "type_description"
      ],
      "additionalProperties": false
    },
    "both_are_genuses": {
      "type": "boolean",
      "description": "The final answer to whether both entities are genuses."
    }
  },
  "required": [
    "question_topic",
    "entity_1",
    "entity_2",
    "both_are_genuses"
  ],
  "additionalProperties": false
}
