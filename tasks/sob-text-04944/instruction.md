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
Qingzhen: Qingzhen (Chinese: 清镇; Pinyin: Qīngzhèn) is a county-level city under the administration of Guiyang in Guizhou province, China.

Gongzhuling: Gongzhuling (, literally "Princess Ridge") is a city in western Jilin province of Northeast China located halfway between Siping City and Changchun, along the main railway line in the Northeast.  Major employers in the city include Jilin Academy of Agricultural Sciences, located on the north side of the railway and several factories which manufacture auto parts.  There is major military presence in the area, including a PLA base and a military airport.

Gongzhuling South Railway Station: Gongzhuling South Railway Station is a railway station of the Harbin–Dalian section of the Beijing–Harbin High-Speed Railway.  It is located in Gongzhuling, in the Jilin province of China.

Question: Are both Gongzhuling and Qingzhen located in the same province ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "are_cities_in_same_province": {
      "type": "boolean",
      "description": "True if both cities are located in the same province, false otherwise."
    },
    "city_locations": {
      "type": "array",
      "description": "Details about the location of each city mentioned.",
      "items": {
        "type": "object",
        "properties": {
          "city_name": {
            "type": "string",
            "description": "The name of the city."
          },
          "province_name": {
            "type": "string",
            "description": "The name of the province where the city is located."
          }
        },
        "required": [
          "city_name",
          "province_name"
        ],
        "additionalProperties": false
      }
    },
    "comparison_summary": {
      "type": "string",
      "description": "A summary of the comparison result regarding their provinces."
    }
  },
  "required": [
    "are_cities_in_same_province",
    "city_locations",
    "comparison_summary"
  ],
  "additionalProperties": false
}
