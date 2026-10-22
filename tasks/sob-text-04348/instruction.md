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
WBQC-LD: WBQC-LD, virtual channel 25 (UHF digital channel 47; branded as WKRP-TV), is a low-power television station with multiple affiliations that is licensed to Cincinnati, Ohio, United States.  The station is owned by Block Broadcasting, which also owns WOTH-CD.  WBQC's transmitter is located along Symmes Street, just south of East McMillan Street in Cincinnati (shared with WCPO-TV, channel 9).

WCPO-TV: WCPO-TV, virtual channel 9 (UHF digital channel 22), is an ABC-affiliated television station licensed to Cincinnati, Ohio, United States.  WCPO-TV is one of two flagship television properties of the Cincinnati-based E. W. Scripps Company (the other being WEWS-TV in Cleveland), which has owned the station since its inception, and maintains studio and office facilities in the Mount Adams neighborhood of Cincinnati.  The station's transmitter is located in the Mount Auburn section of the city.

WOTH-CD: WOTH-CD is a digital, Class A low-power television station in Cincinnati, Ohio, United States, broadcasting locally on UHF channel 20 (virtual channel 20).  WOTH transmits from WCPO-TV's (channel 9) tower located along Symmes Street, just south of East McMillan Street in Cincinnati.  Elliott B. Block's Block Broadcasting has owned WOTH since its inception in 1990, along with sister station WBQC-LD.

Question: What city are WBQC-LD and WCPO-TV are located in?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "station_locations": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "station_call_sign": {
            "type": "string",
            "description": "The call sign of the television station."
          },
          "city": {
            "type": "string",
            "description": "The city where the station is licensed."
          },
          "state": {
            "type": "string",
            "description": "The state where the station is licensed."
          }
        },
        "required": [
          "station_call_sign",
          "city",
          "state"
        ],
        "additionalProperties": false
      },
      "description": "A list of television stations and their licensed locations."
    },
    "common_location_city": {
      "type": "string",
      "description": "The city common to all listed stations."
    },
    "common_location_state": {
      "type": "string",
      "description": "The state common to all listed stations."
    }
  },
  "required": [
    "station_locations",
    "common_location_city",
    "common_location_state"
  ],
  "additionalProperties": false
}
