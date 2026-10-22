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
Jiaozhoubei Railway Station: The Jiaozhoubei Railway Station () is a railway station found in the boundary between Jiaodong Subdistrict and Jiaolai Town of Jiaozhou City, Qingdao, China.  It currently lies on the Qingdao–Jinan High-Speed Railway.

Yinghai Subdistrict, Jiaozhou: Yinghai Subdistrict () is a subdistrict of Jiaozhou City, Shandong, People's Republic of China, located south of G22 Qingdao–Lanzhou Expressway southeast of downtown.  , it has 47 villages under its administration.

Yingkou: Yingkou () is a prefecture-level city of Liaoning province, People's Republic of China.  It is a port city of the Bohai Sea, and is the location of the mouth of the Liao River.

Jiaozhou City: Jiaozhou (), formerly Jiaoxian or Jiao County, is a county-level city of Qingdao sub-provincial city, Shandong Province, China.  It gained its current county-level city designation in 1987.  It has an area of 1,313 km and a population at the 2000 Census of 783,478.

Question: Jiaozhou City and Yingkou, are in which country?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "country_of_location": {
      "type": "string",
      "description": "The country where the mentioned cities are located."
    },
    "entities_located": {
      "type": "array",
      "description": "Details about each entity mentioned in the question and its location.",
      "items": {
        "type": "object",
        "properties": {
          "entity_name": {
            "type": "string",
            "description": "The name of the city or entity."
          },
          "entity_type": {
            "type": "string",
            "description": "The administrative type of the entity (e.g., county-level city, prefecture-level city)."
          },
          "province_or_region": {
            "type": "string",
            "description": "The province or region within the country where the entity is located."
          }
        },
        "required": [
          "entity_name",
          "entity_type",
          "province_or_region"
        ],
        "additionalProperties": false
      }
    },
    "total_entities_found": {
      "type": "integer",
      "description": "The total number of entities whose location was identified."
    }
  },
  "required": [
    "country_of_location",
    "entities_located",
    "total_entities_found"
  ],
  "additionalProperties": false
}
