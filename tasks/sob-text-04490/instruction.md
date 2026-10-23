{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSo Close to Paradise: So Close to Paradise () is a 1998 Chinese film directed by Wang Xiaoshuai, a member of Chinese cinema's so-called Sixth Generation.  It is alternatively known by the English title Ruan's Song or by its original Chinese title, The Girl From Vietnam ().  The film was a coproduction of the Beijing Film Studio, and Beijing Jin Die Yingshi Yishu, as such, it is Wang's first major film production within the Chinese studio system.  The film's literal title, The Pole-Carrier and the Girl, refers to two of the main characters played by Shi Yu and Wang Tong.\n\nFrozen (1997 film): Frozen () is a 1997 Chinese film directed by Wang Xiaoshuai.  The film was originally shot in 1994, but was banned by Chinese authorities and had to be smuggled out of the country.  Moreover, Wang was operating under a blacklisting from the Chinese Film Bureau that was imposed after his previous film, \"The Days\", was screened internationally without government approval.  As such, Wang was forced to use the pseudonym \"Wu Ming\" (literally \"Anonymous\") while making this film.\n\n11 Flowers: 11 Flowers () is a 2011 film directed by Wang Xiaoshuai centered on a boy named Wang Han who loses his white shirt which shows that he is his school's best gymnast.  The loss of the shirt is to take on greater metaphorical meaning as the film progresses which is inspired by the director's own experience as a youth during the cultural revolution and the more general confusion of childhood.\n\nJia Zhangke: Jia Zhangke (born 24 May 1970) is a Chinese film director and screenwriter.  He is generally regarded as a leading figure of the \"Sixth Generation\" movement of Chinese cinema, a group that also includes such figures as Wang Xiaoshuai, Lou Ye, Wang Quan'an and Zhang Yuan.\n\nKarmic Mahjong: Karmic Mahjong () is a 2006 Chinese comedy film directed by Wang Guangli.  It stars Francis Ng as a mechanic from Chengdu plagued by bad luck and Cherrie Ying as a young woman who appears to share the same affliction.  The film also features cameos by the prominent Chinese directors Wang Xiaoshuai and Jia Zhangke.\n\nRed Amnesia: Red Amnesia () is a 2014 Chinese thriller film directed by Wang Xiaoshuai.  The film deals with the psychological impact of an elderly retired widow (played by Lü Zhong)'s past.  Wang considers \"Red Amnesia\" to be the last film of his Cultural Revolution trilogy, which includes 2005's \"Shanghai Dreams\" and 2011's \"11 Flowers\".  It was released on April 30, 2015.\n\nLarry Cohen: Lawrence G. \"Larry\" Cohen (born July 15, 1941) is an American film producer, director, and screenwriter.  He is best known as a B-Movie auteur of horror and science fiction films – often containing a police procedural element – during the 1970s and 1980s.  He has since concentrated mainly on screenwriting including the Joel Schumacher thriller \"Phone Booth\" (2002), \"Cellular\" (2004) and \"Captivity\" (2007).  In 2006 Cohen returned to the directing chair for Mick Garris' \"Masters of Horror\" TV series (2006); he directed the episode \"Pick Me Up\".\n\nWang Xiaoshuai: Wang Xiaoshuai (; born May 22, 1966) is a Chinese film director, screenwriter and occasional actor.  He is commonly grouped under the loose association of filmmakers known as the \"Sixth Generation\" of the Cinema of China.\n\nThe House (1999 film): The House is a 1999 Chinese film directed by Wang Xiaoshuai.  It is rarely, if ever, screened abroad, and remains one of Wang Xiaoshuai's least well-known works outside of China.  It is alternatively referred to as Suburban Dreams, Fantasy Garden or Dream House.  The film was produced by the Beijing Film Studio and the China Film Group.  Wang Xiaoshuai himself considers it one of his most inconsequential efforts to date, to the extent that it has \"sunk into oblivion.\"\n\nShanghai Dreams: Shanghai Dreams () is a 2005 Chinese film directed by Wang Xiaoshuai and starring Gao Yuanyuan, Li Bin, Tang Yang, Wang Xiaoyang, and Yao Anlian.  The film was produced by Stellar Megamedia, Debo Films Ltd. and Kingwood Ltd.\n\nQuestion: What do Larry Cohen and Wang Xiaoshuai have in common?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_a\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"professions\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"All listed professions for this person in the context.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"professions\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"person_b\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"professions\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"All listed professions for this person in the context.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"professions\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"common_professions\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Professions shared by both individuals.\"\n    }\n  },\n  \"required\": [\n    \"person_a\",\n    \"person_b\",\n    \"common_professions\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_a": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "professions": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "All listed professions for this person in the context."
          }
        },
        "required": [
          "name",
          "professions"
        ],
        "additionalProperties": false
      },
      "person_b": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "professions": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "All listed professions for this person in the context."
          }
        },
        "required": [
          "name",
          "professions"
        ],
        "additionalProperties": false
      },
      "common_professions": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Professions shared by both individuals."
      }
    },
    "required": [
      "person_a",
      "person_b",
      "common_professions"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
