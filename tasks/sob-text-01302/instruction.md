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
Li (surname 李): Li () is the second most common surname in China, behind only Wang.  It is one of the most common surnames in the world, shared by 92.76 million people in China, and more than 100 million worldwide.  It is the fourth name listed in the Song dynasty classic text "Hundred Family Surnames".

Ji (surname 计): Jì is the Mandarin pinyin romanization of the Chinese surname written 计 in simplified Chinese and 計 in traditional Chinese.  It is romanized as Chi in Wade–Giles, and Kai or Gai in Cantonese.  Ji is listed 113th in the Song Dynasty classic text "Hundred Family Surnames".  Relatively uncommon, it is not among the top 300 surnames in China.

Li (surname): Li is the pinyin and Wade–Giles romanization (spelled Lí, Lǐ, or Lì when pinyin tone diacritics are used) of several distinct Chinese surnames that are written with different characters in Chinese.  Li 李 is by far the most common among them, shared by 93 million people in China, and more than 100 million worldwide.  It is the second most common Chinese surname behind Wang and the most common surname in Canada .

Bing (Chinese surname): Bing is the Mandarin pinyin romanization of the Chinese surname written 邴 in Chinese character.  It is romanized Ping in Wade–Giles.  Bing is listed 214th in the Song dynasty classic text "Hundred Family Surnames".  It is not among the 300 most common surnames in China.

Ji (surname 籍): Jí is the Mandarin pinyin romanization of the Chinese surname written 籍 in Chinese character.  It is romanized as Chi in Wade–Giles, and Zik in Cantonese.  Ji is listed 275th in the Song dynasty classic text "Hundred Family Surnames".  It is not among the 300 most common surnames in China.

Ban (surname): Ban is the Mandarin pinyin romanization of the Chinese surname written 班 in Chinese character.  It is romanized Pan in Wade–Giles.  Ban is listed 235th in the Song dynasty classic text "Hundred Family Surnames".  It is not among the 300 most common surnames in China.

Ji (surname 汲): Jí is the Mandarin pinyin romanization of the Chinese surname written 汲 in Chinese character.  It is romanized as Chi in Wade–Giles, and Kap in Cantonese.  Ji is listed 213th in the Song dynasty classic text "Hundred Family Surnames".  It is not among the 300 most common surnames in China.

Ji (surname 暨): Jì is the Mandarin pinyin romanization of the Chinese surname written 暨 in Chinese character.  It is romanized as Chi in Wade–Giles and Kei in Cantonese.  Ji is listed 345th in the Song dynasty classic text "Hundred Family Surnames".  It is not among the 300 most common surnames in China.

Rui (surname): Rui is the Mandarin pinyin romanization of the Chinese surname written 芮 in Chinese characters.  It is romanized Jui in Wade–Giles.  Rui is listed 209th in the Song dynasty classic text "Hundred Family Surnames".  It is not among the 300 most common surnames in China.

Ji (surname 蓟): Jì is the Mandarin pinyin romanization of the Chinese surname written 蓟 in simplified Chinese and 薊 in traditional Chinese.  It is romanized as Chi in Wade–Giles and Gai or Kai in Cantonese.  Ji is listed 263rd in the Song Dynasty classic text "Hundred Family Surnames".  It is not among the 300 most common surnames in China.

Question: What type of romanization is the fourth name listed in the Song dynasty classic text "Hundred Family Surnames"?

Respond with JSON matching this schema:
{
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
}
