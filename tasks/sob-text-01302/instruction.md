{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLi (surname 李): Li () is the second most common surname in China, behind only Wang.  It is one of the most common surnames in the world, shared by 92.76 million people in China, and more than 100 million worldwide.  It is the fourth name listed in the Song dynasty classic text \"Hundred Family Surnames\".\n\nJi (surname 计): Jì is the Mandarin pinyin romanization of the Chinese surname written 计 in simplified Chinese and 計 in traditional Chinese.  It is romanized as Chi in Wade–Giles, and Kai or Gai in Cantonese.  Ji is listed 113th in the Song Dynasty classic text \"Hundred Family Surnames\".  Relatively uncommon, it is not among the top 300 surnames in China.\n\nLi (surname): Li is the pinyin and Wade–Giles romanization (spelled Lí, Lǐ, or Lì when pinyin tone diacritics are used) of several distinct Chinese surnames that are written with different characters in Chinese.  Li 李 is by far the most common among them, shared by 93 million people in China, and more than 100 million worldwide.  It is the second most common Chinese surname behind Wang and the most common surname in Canada .\n\nBing (Chinese surname): Bing is the Mandarin pinyin romanization of the Chinese surname written 邴 in Chinese character.  It is romanized Ping in Wade–Giles.  Bing is listed 214th in the Song dynasty classic text \"Hundred Family Surnames\".  It is not among the 300 most common surnames in China.\n\nJi (surname 籍): Jí is the Mandarin pinyin romanization of the Chinese surname written 籍 in Chinese character.  It is romanized as Chi in Wade–Giles, and Zik in Cantonese.  Ji is listed 275th in the Song dynasty classic text \"Hundred Family Surnames\".  It is not among the 300 most common surnames in China.\n\nBan (surname): Ban is the Mandarin pinyin romanization of the Chinese surname written 班 in Chinese character.  It is romanized Pan in Wade–Giles.  Ban is listed 235th in the Song dynasty classic text \"Hundred Family Surnames\".  It is not among the 300 most common surnames in China.\n\nJi (surname 汲): Jí is the Mandarin pinyin romanization of the Chinese surname written 汲 in Chinese character.  It is romanized as Chi in Wade–Giles, and Kap in Cantonese.  Ji is listed 213th in the Song dynasty classic text \"Hundred Family Surnames\".  It is not among the 300 most common surnames in China.\n\nJi (surname 暨): Jì is the Mandarin pinyin romanization of the Chinese surname written 暨 in Chinese character.  It is romanized as Chi in Wade–Giles and Kei in Cantonese.  Ji is listed 345th in the Song dynasty classic text \"Hundred Family Surnames\".  It is not among the 300 most common surnames in China.\n\nRui (surname): Rui is the Mandarin pinyin romanization of the Chinese surname written 芮 in Chinese characters.  It is romanized Jui in Wade–Giles.  Rui is listed 209th in the Song dynasty classic text \"Hundred Family Surnames\".  It is not among the 300 most common surnames in China.\n\nJi (surname 蓟): Jì is the Mandarin pinyin romanization of the Chinese surname written 蓟 in simplified Chinese and 薊 in traditional Chinese.  It is romanized as Chi in Wade–Giles and Gai or Kai in Cantonese.  Ji is listed 263rd in the Song Dynasty classic text \"Hundred Family Surnames\".  It is not among the 300 most common surnames in China.\n\nQuestion: What type of romanization is the fourth name listed in the Song dynasty classic text \"Hundred Family Surnames\"?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"surname_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the surname.\"\n    },\n    \"hundred_family_surnames_rank\": {\n      \"type\": \"integer\",\n      \"description\": \"The rank of the surname in the Song dynasty classic text 'Hundred Family Surnames'.\"\n    },\n    \"romanization_types\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of romanization systems used for the surname.\"\n    }\n  },\n  \"required\": [\n    \"surname_name\",\n    \"hundred_family_surnames_rank\",\n    \"romanization_types\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "surname_name": {
        "type": "string",
        "description": "The name of the surname."
      },
      "hundred_family_surnames_rank": {
        "type": "integer",
        "description": "The rank of the surname in the Song dynasty classic text 'Hundred Family Surnames'."
      },
      "romanization_types": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of romanization systems used for the surname."
      }
    },
    "required": [
      "surname_name",
      "hundred_family_surnames_rank",
      "romanization_types"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
