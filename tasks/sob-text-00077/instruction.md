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
Money Game (film): Money Game () is a 2015 Chinese comedy film directed by Huang Wei.  It was released on January 23, 2015.

Déjà Vu (2015 film): Déjà Vu () is a 2015 Chinese comedy film directed by Huang Wei.  It was released on January 23, 2015.

20 Once Again: 20 Once Again (Chinese: 重返20岁 "Chóng fǎn èrshí suì") is a 2015 Chinese comedy film directed by Leste Chen and starring Yang Zishan, Gua Ah-leh, Bolin Chen and Lu Han.  The film is a remake of the South Korean movie "Miss Granny".  It was released on January 8, 2015.

Hot Blood Band: Hot Blood Band () is a 2015 Chinese comedy film directed by Zha Muchun.  It was released on January 29, 2015.

Miss Granny: Miss Granny (; lit.  "Suspicious Girl") is a 2014 South Korean comedy-drama film directed by Hwang Dong-hyuk.  Na Moon-hee stars as a woman in her 70s who magically finds herself in the body of her 20-year-old self (Shim Eun-kyung) after having her picture taken at a mysterious photo studio.  After opening in theaters on January 22, 2014, it became a huge box office hit, with 8.65 million tickets sold.

Unforgettable Blast: Unforgettable Blast () is a 2015 Chinese comedy film directed by Yan Tinglu.  It was released in China on May 22, 2015.

Onion From the Boot of a Benz: Onion From the Boot of a Benz () is a 2015 Chinese comedy film directed by Guo Minger.  It was released on January 27, 2015.

Devil and Angel: Devil and Angel () is a 2015 Chinese comedy film directed by Yu Baimei and Deng Chao and starring Deng Chao and Sun Li.  It was released in China on December 24, 2015.

Goodbye Mr. Loser: Goodbye Mr. Loser () is a 2015 Chinese comedy film directed by Yan Fei and Peng Damo, and starring Shen Teng, Ma Li, Yin Zheng, Ai Lun, Wang Zhi, Tian Yu, Song Yang, Chang Yuan and Li Ping.  The film is based on a play of the same name.  It was released on September 30, 2015.  Some critics have accused the film of containing similar plot elements as the 1986 American film "Peggy Sue Got Married".  The directors later denied these allegations.

Heart for Heaven: Heart for Heaven is a 2015 Chinese comedy film directed by Zhang Cheng.  It was released in China on December 31, 2015.

Question: Who directed the original South Korean version of the 2015 Chinese comedy film, 20 Once Again?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "remake_film": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string"
        },
        "release_year": {
          "type": "integer"
        },
        "country_of_origin": {
          "type": "string"
        }
      },
      "required": [
        "title",
        "release_year",
        "country_of_origin"
      ],
      "additionalProperties": false
    },
    "original_film": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string"
        },
        "country_of_origin": {
          "type": "string"
        },
        "director": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            }
          },
          "required": [
            "name"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "title",
        "country_of_origin",
        "director"
      ],
      "additionalProperties": false
    },
    "relationship_type": {
      "type": "string"
    }
  },
  "required": [
    "remake_film",
    "original_film",
    "relationship_type"
  ],
  "additionalProperties": false
}
