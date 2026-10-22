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
Binzhou: Binzhou, formerly Putai, is a prefecture-level city in northern Shandong Province in the People's Republic of China.  The city proper sits on the northern bank of the Yellow River, while its administrative area straddles both sides of its lower course before its present delta.

Xinzhou: Xinzhou () is a prefecture-level city occupying the north-central section of Shanxi province, People's Republic of China.

Question: What do Xinzhou and Binzhou have in common?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "cities_compared": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Names of the cities being compared."
    },
    "common_features": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "feature_type": {
            "type": "string",
            "description": "The category of the common feature (e.g., 'country', 'administrative_level')."
          },
          "feature_value": {
            "type": "string",
            "description": "The specific value that is common between the cities."
          }
        },
        "required": [
          "feature_type",
          "feature_value"
        ],
        "additionalProperties": false
      },
      "description": "A list of common attributes shared by the cities."
    },
    "number_of_common_features": {
      "type": "integer",
      "description": "The total count of common features identified."
    }
  },
  "required": [
    "cities_compared",
    "common_features",
    "number_of_common_features"
  ],
  "additionalProperties": false
}
