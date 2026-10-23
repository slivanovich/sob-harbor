{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPark Bo-young: Park Bo-young (born February 12, 1990) is a South Korean actress.  She is best known for her roles in the hit films \"Scandal Makers\" (2008) and \"A Werewolf Boy\" (2012), and the television series \"Oh My Ghostess\" (2015) and \"Strong Woman Do Bong-soon\" (2017).\n\nThe Silenced: The Silenced (; lit.  \"Gyeongseong School: The Lost Girls\") is a 2015 South Korean mystery-thriller film written and directed by Lee Hae-young, starring Park Bo-young and Uhm Ji-won.\n\nOh Yeon-seo: Oh Yeon-seo (born Oh Haet-nim, on June 22, 1987), is a South Korean actress and former member of South Korean girl group, LUV.  She is best known for her roles in television dramas \"My Husband Got a Family\" (2012), \"Jang Bo-ri is Here! \" (2014), \"Shine or Go Crazy\" (2015) and \"Please Come Back, Mister\" (2016).\n\nCha Tae-hyun: Cha Tae-hyun (born March 25, 1976) is a South Korean actor, singer, television personality radio DJ and director.  He is best known for his lead roles in the box-office hit comedies \"My Sassy Girl\" (2001), \"Scandal Makers\" (2008) and \"Hello Ghost\" (2010) as well as the television series \"Jeon Woo-chi\" (2012) and \"The Producers\" (2015).  He made his directorial debut with the variety-drama \"Hit the Top\" (2017), in which he also stars.\n\nKang Hyeong-cheol: Kang Hyeong-cheol is a South Korean film director and screenwriter.  His first two films \"Scandal Makers\" (2008) and \"Sunny\" (2011) have been the highest grossing Korean films of their respective years, and are both among the highest grossing Korean films of all time.  Kang won Best Director at the 48th Grand Bell Awards in 2011.\n\nKim Seul-gi: Kim Seul-Gi (born October 10, 1991) is a South Korean actress who starred in many critically acclaimed dramas including \"Oh My Ghostess\" (2015), \"Splash Splash Love\" (2015) and \"The Guardians\" (2017).  She is also a former cast member of tvN's entertainment show \"SNL Korea\".\n\nOh My Ghostess: Oh My Ghostess () is a 2015 South Korean television series starring Jo Jung-suk, Park Bo-young, Kim Seul-gie and Lim Ju-hwan.  It aired on tvN from July 3 to August 22, 2015, on Fridays and Saturdays at 20:30 for 16 episodes.\n\nScandal Maker: Scandal Maker is a 2016 Chinese comedy-drama film directed by Ahn Byeong-ki, starring Tong Dawei and Michelle Chen and a remake of the 2008 South Korean film \"Scandal Makers\".  It was released in China on November 11, 2016.\n\nStrong Woman Do Bong-soon: Strong Woman Do Bong-soon () is a 2017 South Korean television series starring Park Bo-young in the title role as a woman with superhuman strength, with Park Hyung-sik and Ji Soo.  It aired every Friday and Saturday on JTBC starting from February 24, 2017 to April 15, 2017.\n\nScandal Makers: Scandal Makers (; lit.  Speedy Scandal) is a 2008 South Korean film written and directed by Kang Hyeong-cheol and starring Cha Tae-hyun in the lead role.  This was director Kang's first film and the highest grossing Korean film of the year.  A Chinese remake was released in 2016.\n\nQuestion: Oh My Ghostess, is a 2015 South Korean television series, stars include Park Bo-young, a South Korean actress, that is best known for her roles in the hit films \"Scandal Makers\", released in which year?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"series_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the television series mentioned in the question.\"\n    },\n    \"series_release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the television series.\"\n    },\n    \"actress_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the actress.\"\n        },\n        \"known_for_film\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"title\": {\n              \"type\": \"string\",\n              \"description\": \"The title of the film the actress is known for.\"\n            },\n            \"release_year\": {\n              \"type\": \"integer\",\n              \"description\": \"The release year of the film.\"\n            }\n          },\n          \"required\": [\n            \"title\",\n            \"release_year\"\n          ],\n          \"additionalProperties\": false\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"known_for_film\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"series_title\",\n    \"series_release_year\",\n    \"actress_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "series_title": {
        "type": "string",
        "description": "The title of the television series mentioned in the question."
      },
      "series_release_year": {
        "type": "integer",
        "description": "The release year of the television series."
      },
      "actress_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the actress."
          },
          "known_for_film": {
            "type": "object",
            "properties": {
              "title": {
                "type": "string",
                "description": "The title of the film the actress is known for."
              },
              "release_year": {
                "type": "integer",
                "description": "The release year of the film."
              }
            },
            "required": [
              "title",
              "release_year"
            ],
            "additionalProperties": false
          }
        },
        "required": [
          "name",
          "known_for_film"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "series_title",
      "series_release_year",
      "actress_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
