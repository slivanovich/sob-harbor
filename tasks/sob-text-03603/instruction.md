{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nHsiao Ho (actor): Hsiao Ho, (Hsiao Hou) (; Cantonese: Siu Hau, born 1 January 1958 (age 58) in Meixian District, Guangdong, China) is a Hong Kong martial arts film actor, stunt performer and action choreographer.  A Hakka, he has acted in many films directed by Lau Kar-leung, including \"Mad Monkey Kung Fu\" and Legendary Weapons of China.  In 1985 he portrayed legendary kung fu warrior Fong Sai-Yuk in the Lau directed action-comedy, \"Disciples of the 36th Chamber\" and also took a lead role in Fake Ghost Catchers, directed by Lau Kar Wing.  Fake Ghost Catchers is marketed by Celestial Pictures as being made two years before Ghostbusters (inferring that the idea for Ghostbusters may have come from the movie).  Hou is also known for portraying the \"disfigured swordsman\" and doubling complicated action scenes in 1993's \"Iron Monkey\".  He was also the action director for the movie Shaolin Avengers (1994).  In 1982 he was nominated for Best Action Choreography for the movie Legendary Weapons of China (for which he was action director) at the Hong Kong Film Awards alongside Lau Kar Leung and Ching Chu who also provided choreography for the film.\n\nDisciples of the 36th Chamber: Disciples Of The 36th Chamber (霹靂十傑, \"Pi li shi jie\", \"Disciples of the Master Killer\" or \"Master Killer III\") is a 1985 Shaw Brothers Studio Hong Kong martial arts film comedy written, directed and choreographed Lau Kar-leung.  It is the third in a loose trilogy of films that began with \"The 36th Chamber of Shaolin\" (1978) and was followed by \"Return to the 36th Chamber\" (1980).  In \"Disciples\", the action is focused on Hsiao Ho, who portrays legendary martial artist Fong Sai-Yuk.  Gordon Liu, a constant in the \"36th Chamber\" series, reprises his role from \"The 36th Chamber of Shaolin\" as the monk San Te.\n\nInvincible Shaolin: Invincible Shaolin (Nan Shao Lin yu bei Shao Lin) a.k.a. \"Unbeatable Dragon\" is a Hong Kong films of 1978 Shaw Brothers kung fu film directed by Chang Cheh.  It is one of Chang Cheh's tales of Shaolin's historic rivalries with the Qing Dynasty.  It is one of the few Venom films featuring Wei Pai (the Snake).\n\nGordon Liu: Gordon Liu (Lau Ka-fai , birth name Xian Jinxi; born August 22, 1951) is a Chinese martial arts film actor and martial artist.  He became famous for playing the lead role of San Te in \"The 36th Chamber of Shaolin\" (1978) and its sequels.  He later became known for his two roles in Quentin Tarantino's \"Kill Bill\" films: Johnny Mo, the leader of the Crazy 88 Yakuza gang in \"\" (2003); and kung fu master Pai Mei in \"\" (2004).\n\nShaolin Kung Fu: Shaolin Kung Fu (), also called Shaolin Wushu () or Shaolin quan (), is one of the oldest, largest, and most famous styles of Chinese martial arts.  It combines Zen Buddhism and martial arts and originated and was developed in the Shaolin temple in Henan province, China during its 1500-year history.  In Chinese folklore, there are famous sayings \"All martial arts under heaven originated from Shaolin\" and \"Shaolin kung fu is the best under heaven,\" which, though not provable, indicate and appraise the influence and place of Shaolin kung fu among martial arts.  The name Shaolin is also used as a brand for the so-called external styles of kung fu.  Many styles in southern and northern China use the name Shaolin.\n\nThe 36th Chamber of Shaolin: The 36th Chamber of Shaolin, also known as \"The Master Killer\" and \"Shaolin Master Killer\" and \"Shao Lin san shi liu fang\" is a 1978 Shaw Brothers kung fu film directed by Liu Chia-liang and starring Gordon Liu.\n\nCrippled Avengers: Crippled Avengers is a 1978 Shaw Brothers kung fu film directed by Chang Cheh and starring four members of the Venom Mob.  It has been released in North America as Mortal Combat and Return of the 5 Deadly Venoms.  The film follows a group of martial artists seeking revenge after being crippled by Tu Tin-To (Chen Kuan Tai), a martial arts master, and his son (Lu Feng).\n\nLau Kar-leung: Lau Kar-leung (28 July 1934 – 25 June 2013), also known as Liu Chia-liang, was a Hong Kong-based Chinese actor, filmmaker, choreographer and martial artist.  Lau is best known for the films he made in the 1970s and 1980s for the Shaw Brothers Studio.  One of his most famous works is \"The 36th Chamber of Shaolin\" which starred Gordon Liu, as well as \"Drunken Master II\" which starred Jackie Chan.\n\nReturn to the 36th Chamber: Return to the 36th Chamber (少林搭棚大師, \"Shao Lin ta peng hsiao tzu\", \"Return of the Master Killer\" or \"Master Killer II\") is a 1980 Shaw Brothers Studio Hong Kong martial arts comedy film starring Gordon Liu.  It was directed by Lau Kar-Leung and written by Ni Kuang.  The film is the second in a loosely connected trilogy, following \"The 36th Chamber Of Shaolin\" (1978) and preceding \"Disciples Of The 36th Chamber\" (1985).  In the first and third films in the series, Liu portrays the Shaolin monk San Te, but in \"Return\", he portrays an imposter monk.\n\nHoi Sang Lee: Hoi Sang Lee (born April 15, 1945) is a Chinese martial arts film actor known for his roles in The 36th Chamber of Shaolin (as Li Hai Sheng, Abbot of Justice Office) (1978), Shaolin Challenges Ninja (1978), The Incredible Kung Fu Master (1979), The Young Master (1980), The Prodigal Son (1981), Project A (1983), Shaolin and Wu Tang (1983) and Disciples of the 36th Chamber (1985) alongside actors such as Gordon Liu, Sammo Hung and Jackie Chan.\n\nQuestion: The 36th Chamber of Shaolin, is a 1978 Shaw Brothers kung fu film directed by Liu Chia-liang and starring which Chinese martial arts film actor and martial artist, that became famous for playing the lead role of San Te in the film, and its sequels?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\"\n        },\n        \"director\": {\n          \"type\": \"string\"\n        },\n        \"studio\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"release_year\",\n        \"director\",\n        \"studio\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"starring_actor\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"nationality\": {\n          \"type\": \"string\"\n        },\n        \"professions\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          }\n        },\n        \"role_in_film\": {\n          \"type\": \"string\"\n        },\n        \"famous_for_role_in_sequels\": {\n          \"type\": \"boolean\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"nationality\",\n        \"professions\",\n        \"role_in_film\",\n        \"famous_for_role_in_sequels\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"film_series_info\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"series_name\": {\n          \"type\": \"string\"\n        },\n        \"first_film_title\": {\n          \"type\": \"string\"\n        },\n        \"sequel_titles\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          }\n        }\n      },\n      \"required\": [\n        \"series_name\",\n        \"first_film_title\",\n        \"sequel_titles\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_details\",\n    \"starring_actor\",\n    \"film_series_info\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string"
          },
          "release_year": {
            "type": "integer"
          },
          "director": {
            "type": "string"
          },
          "studio": {
            "type": "string"
          }
        },
        "required": [
          "title",
          "release_year",
          "director",
          "studio"
        ],
        "additionalProperties": false
      },
      "starring_actor": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "nationality": {
            "type": "string"
          },
          "professions": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "role_in_film": {
            "type": "string"
          },
          "famous_for_role_in_sequels": {
            "type": "boolean"
          }
        },
        "required": [
          "name",
          "nationality",
          "professions",
          "role_in_film",
          "famous_for_role_in_sequels"
        ],
        "additionalProperties": false
      },
      "film_series_info": {
        "type": "object",
        "properties": {
          "series_name": {
            "type": "string"
          },
          "first_film_title": {
            "type": "string"
          },
          "sequel_titles": {
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "series_name",
          "first_film_title",
          "sequel_titles"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_details",
      "starring_actor",
      "film_series_info"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
