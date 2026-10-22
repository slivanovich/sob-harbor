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
Kuytun: Kuytun or Kuitun () is a county-level city with about 285,000 residents (2000 census) in Ili Kazakh Autonomous Prefecture, Xinjiang, China.  Kuitun is located between Wusu and Shihezi on the railway from Ürümqi to Kazakhstan, close to a desert.

Zaoyang: Zaoyang () is a city in northern Hubei province, People's Republic of China, near the border with Henan province.  Administratively, it is a county-level city under the administration of Xiangyang.

Question: Zaoyang and Kuytun, are in which country?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "cities_mentioned": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "city_name": {
            "type": "string"
          },
          "administrative_division": {
            "type": "string"
          },
          "country": {
            "type": "string"
          }
        },
        "required": [
          "city_name",
          "country"
        ],
        "additionalProperties": false
      }
    },
    "number_of_cities": {
      "type": "integer"
    },
    "common_country": {
      "type": "string"
    }
  },
  "required": [
    "cities_mentioned",
    "number_of_cities",
    "common_country"
  ],
  "additionalProperties": false
}
