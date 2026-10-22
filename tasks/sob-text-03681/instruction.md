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
Inner Mongolia: Inner Mongolia (Mongolian: "Öbür Monggol" in Mongolian script; ), officially the Inner Mongolia Autonomous Region or Nei Mongol Autonomous Region, is an autonomous region of the People's Republic of China, located in the north of the country, containing most of China's border with Mongolia (the rest of the China-Mongolia border is taken up by the Xinjiang autonomous region and Gansu province) and a small section of the border with Russia.  Its capital is Hohhot, and other major cities include Baotou, Chifeng, and Ordos.

Baotou: Baotou (Mongolian: ; ) also known as Bugthot is the largest industrial city in the Inner Mongolia Autonomous Region of northern China.  Governed as a prefecture-level city, its built-up ("or metro") area made up of 5 urban districts is home to 2,070,801 inhabitants with a total population of over 2.65 million accounting for counties under its jurisdiction.  The city's Mongolian name means "place with deer", and an alternate name is "Lucheng" (鹿城 ; "Lùchéng"), meaning "Deer City".

Shouguang: Shouguang () is a county-level city located in Weifang Prefecture-level city, Shandong Province, China.  It has 1,139,454 people residing within the municipality and its surrounding towns and villages, even though the built-up ("or metro") area is much smaller.

Question: Baotou and Shouguang, are located in which country?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "country_name": {
      "type": "string",
      "description": "The name of the country where the cities are located."
    },
    "cities_information": {
      "type": "array",
      "description": "Details about each city mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "city_name": {
            "type": "string",
            "description": "The name of the city."
          },
          "parent_administrative_region": {
            "type": "string",
            "description": "The immediate administrative region (e.g., autonomous region, province) the city is located within."
          }
        },
        "required": [
          "city_name",
          "parent_administrative_region"
        ],
        "additionalProperties": false
      }
    },
    "number_of_cities_mentioned": {
      "type": "integer",
      "description": "The total count of cities explicitly mentioned in the question."
    }
  },
  "required": [
    "country_name",
    "cities_information",
    "number_of_cities_mentioned"
  ],
  "additionalProperties": false
}
