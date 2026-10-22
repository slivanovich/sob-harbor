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
Luoding: Luoding, formerly romanized as Loting, is a county-level city in western Guangdong, China.  It is administered as part of Yunfu.

Qingfengdian: Qingfengdian () is a town under the administration of Dingzhou City in western Hebei province, China, located about 12 km northeast of downtown Dingzhou and just off of China National Highway 107.  It has an area of 53 km2 and a reported population of 49,000 people.

Haotouzhuang Hui Ethnic Township: Haotouzhuang Hui Ethnic Township (; Xiao'erjing: هَوْتِوْتُوْا خُوِذُو سِیْا) is an ethnic township under the administration of Dingzhou City in Hebei province, China, located about 12 km southeast of downtown Dingzhou in the southern part of Baoding City.  , it has 17 villages under its administration.

Dingzhou East Railway Station: The Dingzhou East Railway Station is a railway station of Jingshi Passenger Railway that located in Hebei, People's Republic of China.

Dingzhou: Dingzhou (), formerly Dingxian ( postal: Tingsien) is a county-level city with sub-prefecture-level city status, located under the administration of the prefecture-level city of Baoding in the southwest of Hebei Province in northern China, about halfway between Baoding and Shijiazhuang.  As of 2009, Dingzhou had a population of 1.2 million.  Dingzhou has 3 subdistricts, 13 towns, 8 townships, and 1 ethnic township.  Dingzhou is 196 km southwest of Beijing, 68 km northeast of Shijiazhuang.

Question: Where are Luoding and Dingzhou located?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "places_info": {
      "type": "array",
      "description": "Information about each place mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "place_name": {
            "type": "string",
            "description": "The name of the place."
          },
          "country": {
            "type": "string",
            "description": "The country where the place is located."
          },
          "province": {
            "type": "string",
            "description": "The province where the place is located."
          },
          "administered_by_city": {
            "type": "string",
            "description": "The prefecture-level city or higher entity that administers the place."
          }
        },
        "required": [
          "place_name",
          "country",
          "province",
          "administered_by_city"
        ],
        "additionalProperties": false
      }
    },
    "shared_country": {
      "type": "string",
      "description": "The common country where all mentioned places are located."
    },
    "number_of_places": {
      "type": "integer",
      "description": "The total number of places whose location was requested."
    }
  },
  "required": [
    "places_info",
    "shared_country",
    "number_of_places"
  ],
  "additionalProperties": false
}
