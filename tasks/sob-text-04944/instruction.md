{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nQingzhen: Qingzhen (Chinese: 清镇; Pinyin: Qīngzhèn) is a county-level city under the administration of Guiyang in Guizhou province, China.\n\nGongzhuling: Gongzhuling (, literally \"Princess Ridge\") is a city in western Jilin province of Northeast China located halfway between Siping City and Changchun, along the main railway line in the Northeast.  Major employers in the city include Jilin Academy of Agricultural Sciences, located on the north side of the railway and several factories which manufacture auto parts.  There is major military presence in the area, including a PLA base and a military airport.\n\nGongzhuling South Railway Station: Gongzhuling South Railway Station is a railway station of the Harbin–Dalian section of the Beijing–Harbin High-Speed Railway.  It is located in Gongzhuling, in the Jilin province of China.\n\nQuestion: Are both Gongzhuling and Qingzhen located in the same province ?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"are_cities_in_same_province\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if both cities are located in the same province, false otherwise.\"\n    },\n    \"city_locations\": {\n      \"type\": \"array\",\n      \"description\": \"Details about the location of each city mentioned.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"city_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the city.\"\n          },\n          \"province_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the province where the city is located.\"\n          }\n        },\n        \"required\": [\n          \"city_name\",\n          \"province_name\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"comparison_summary\": {\n      \"type\": \"string\",\n      \"description\": \"A summary of the comparison result regarding their provinces.\"\n    }\n  },\n  \"required\": [\n    \"are_cities_in_same_province\",\n    \"city_locations\",\n    \"comparison_summary\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
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
  },
  "answer_path": "/tmp/answer.json"
}
