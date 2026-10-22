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
VAQ-131: Electronic Attack Squadron 131 (VAQ-131), also known as the "Lancers," is a United States Navy tactical jet aircraft squadron specializing in kinetic and non-kinetic Suppression of Enemy Air Defenses (SEAD).  They are based at Naval Air Station Whidbey Island, flying the EA-18G Growler and are part of Carrier Air Wing 8, deploying aboard the USS "George H.W. Bush" .  Their radio callsign is "Skybolt."

Naval Air Station Whidbey Island: Naval Air Station Whidbey Island (NASWI) (IATA: NUW, ICAO: KNUW, FAA LID: NUW) is a naval air station of the United States Navy located on two pieces of land near Oak Harbor, on Whidbey Island, in Island County, Washington.

Question: In what state is VAQ-131 based in?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "squadron_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The official designation of the squadron."
        },
        "nickname": {
          "type": "string",
          "description": "The common nickname for the squadron."
        },
        "callsign": {
          "type": "string",
          "description": "The radio callsign of the squadron."
        }
      },
      "required": [
        "name",
        "nickname",
        "callsign"
      ],
      "additionalProperties": false
    },
    "base_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the naval air station where the squadron is based."
        },
        "location": {
          "type": "object",
          "properties": {
            "county": {
              "type": "string",
              "description": "The county where the base is located."
            },
            "state": {
              "type": "string",
              "description": "The state where the base is located."
            }
          },
          "required": [
            "county",
            "state"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "name",
        "location"
      ],
      "additionalProperties": false
    },
    "final_answer_state": {
      "type": "string",
      "description": "The state where VAQ-131 is based, as the direct answer to the question."
    }
  },
  "required": [
    "squadron_details",
    "base_details",
    "final_answer_state"
  ],
  "additionalProperties": false
}
