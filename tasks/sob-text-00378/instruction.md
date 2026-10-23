{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nXingshan District: The district of Xingshan (兴山区 ; pinyin : Xìngshān Qū) is an administrative subdivision of the province of Heilongjiang, China.  It is under the jurisdiction of the prefecture-level city of Hegang.\n\nJiaonan: Jiaonan () was a former county and county-level city under the administration of Qingdao, Shandong, China, located in the southwestern portion of Qingdao along the Yellow Sea coast.  In 1945, as Zhushan County (珠山縣 ) it was carved from Jiao County and Qingdao City, and in 1946, renamed as Jiaonan County, deriving its name from its southern location relative to Jiaozhou Bay.  In 1990, it was upgraded to a county-level city.  Jiaonan has 7 subdistricts and 11 towns.  In December 2012, it was merged into Huangdao District.\n\nQuestion: Is Jiaonan located in the same province as Xingshan District?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"entity_1_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the first administrative entity mentioned in the question.\"\n    },\n    \"entity_1_province\": {\n      \"type\": \"string\",\n      \"description\": \"The province where the first entity is located.\"\n    },\n    \"entity_2_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the second administrative entity mentioned in the question.\"\n    },\n    \"entity_2_province\": {\n      \"type\": \"string\",\n      \"description\": \"The province where the second entity is located.\"\n    },\n    \"provinces_are_same\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if both entities are located in the same province, false otherwise.\"\n    },\n    \"final_answer\": {\n      \"type\": \"string\",\n      \"description\": \"The direct answer to the question (yes/no).\"\n    }\n  },\n  \"required\": [\n    \"entity_1_name\",\n    \"entity_1_province\",\n    \"entity_2_name\",\n    \"entity_2_province\",\n    \"provinces_are_same\",\n    \"final_answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "entity_1_name": {
        "type": "string",
        "description": "The name of the first administrative entity mentioned in the question."
      },
      "entity_1_province": {
        "type": "string",
        "description": "The province where the first entity is located."
      },
      "entity_2_name": {
        "type": "string",
        "description": "The name of the second administrative entity mentioned in the question."
      },
      "entity_2_province": {
        "type": "string",
        "description": "The province where the second entity is located."
      },
      "provinces_are_same": {
        "type": "boolean",
        "description": "True if both entities are located in the same province, false otherwise."
      },
      "final_answer": {
        "type": "string",
        "description": "The direct answer to the question (yes/no)."
      }
    },
    "required": [
      "entity_1_name",
      "entity_1_province",
      "entity_2_name",
      "entity_2_province",
      "provinces_are_same",
      "final_answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
