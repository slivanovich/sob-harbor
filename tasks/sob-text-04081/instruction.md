{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLee Bo-young: Lee Bo-young (; born January 12, 1979) is a South Korean actress.  She is best known for starring in the television dramas \"My Daughter Seo-young\" (2012), \"I Can Hear Your Voice\" (2013) and \"Whisper\" (2017).\n\nMan from the Equator: Man from the Equator (; also known as The Equator Man) is a 2012 South Korean television series, starring Uhm Tae-woong, Lee Joon-hyuk, Lee Bo-young and Im Jung-eun.  A tense, emotionally charged tale of brotherhood and betrayal, it follows two best friends with a tragic, twisted history that follows them from youth to adulthood.  It aired on KBS2 from March 21 to May 24, 2012 on Wednesdays and Thursdays at 21:55 for 20 episodes.\n\nBallad of Seodong: Ballad of Seodong () is a South Korean television series starring Jo Hyun-jae, Lee Bo-young and Ryu Jin.  It aired on SBS from September 5, 2005 to March 21, 2006 on Mondays and Tuesdays at 21:55 for 55 episodes.\n\nSave the Last Dance for Me (TV series): Save the Last Dance for Me () is a 20-episode South Korean television series that aired on SBS from October 23, 2004 to January 2, 2005 on Saturdays and Sundays at 21:45.  Starring Eugene, Ji Sung, Ryu Soo-young and Lee Bo-young.  The drama revolves around two lovers who don't let amnesia get in the way of their romance.\n\nWhisper (TV series): Whisper () is a 2017 South Korean television series starring Lee Bo-young, Lee Sang-yoon, Kwon Yul and Park Se-young.  It aired on SBS from March 27 to May 23, 2017 on Mondays and Tuesdays at 22:00 (KST) for 17 episodes.\n\nI Can Hear Your Voice: I Can Hear Your Voice () is a 2013 South Korean television series starring Lee Bo-young, Lee Jong-suk, Yoon Sang-hyun and Lee Da-hee.  It aired on SBS from June 5 to August 1, 2013, on Wednesdays and Thursdays at 21:55 for 18 episodes.\n\nBecoming a Billionaire: Becoming a Billionaire (; lit.  \"Birth of the Rich\") is a 2010 South Korean television series starring Ji Hyun-woo, Lee Bo-young, Lee Si-young and Namkoong Min.  It aired on KBS2 from March 1 to May 4, 2010 on Mondays and Tuesdays at 21:55 for 20 episodes.\n\n2013 SBS Drama Awards: The 2013 SBS Drama Awards () is a ceremony honoring the best performances in television on the SBS network for the year 2013.  It was held at the SBS Prism Tower in Sangam-dong, Seoul on December 31, 2013, and hosted by Lee Hwi-jae, Lee Bo-young, and Kim Woo-bin.\n\nGod's Gift: 14 Days: God's Gift – 14 Days () is a 2014 South Korean television series written by Choi Ran (the writer of \"Iljimae\"), starring Lee Bo-young, Jo Seung-woo, Kim Tae-woo, Jung Gyu-woon and Kim Yoo-bin.  It aired on SBS from March 3 to April 22, 2014, on Mondays and Tuesdays at 21:55 for 16 episodes.\n\nSeoyoung, My Daughter: Seoyoung, My Daughter () is a 2012 South Korean television series, starring Lee Bo-young, Chun Ho-jin, Lee Sang-yoon and Park Hae-jin.  The family drama focuses on the broken relationship between Seo-young and her father, who later reunite with the help of her twin brother.  It aired on KBS2 from September 15, 2012 to March 3, 2013 on Saturdays and Sundays at 19:55 for 50 episodes.\n\nQuestion: What television drama did Lee Bo-young star in that aired on SBS?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actress_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actress.\"\n    },\n    \"network_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the television network.\"\n    },\n    \"dramas_aired_on_network\": {\n      \"type\": \"array\",\n      \"description\": \"A list of television dramas starring the actress that aired on the specified network.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"title\": {\n            \"type\": \"string\",\n            \"description\": \"The title of the television drama.\"\n          },\n          \"start_year\": {\n            \"type\": \"integer\",\n            \"description\": \"The year the drama started airing.\"\n          },\n          \"end_year\": {\n            \"type\": \"integer\",\n            \"description\": \"The year the drama finished airing.\"\n          },\n          \"air_days\": {\n            \"type\": \"array\",\n            \"items\": {\n              \"type\": \"string\"\n            },\n            \"description\": \"The days of the week the drama aired.\"\n          },\n          \"number_of_episodes\": {\n            \"type\": \"integer\",\n            \"description\": \"The total number of episodes for the drama.\"\n          }\n        },\n        \"required\": [\n          \"title\",\n          \"start_year\",\n          \"end_year\",\n          \"air_days\",\n          \"number_of_episodes\"\n        ],\n        \"additionalProperties\": false\n      }\n    }\n  },\n  \"required\": [\n    \"actress_name\",\n    \"network_name\",\n    \"dramas_aired_on_network\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actress_name": {
        "type": "string",
        "description": "The name of the actress."
      },
      "network_name": {
        "type": "string",
        "description": "The name of the television network."
      },
      "dramas_aired_on_network": {
        "type": "array",
        "description": "A list of television dramas starring the actress that aired on the specified network.",
        "items": {
          "type": "object",
          "properties": {
            "title": {
              "type": "string",
              "description": "The title of the television drama."
            },
            "start_year": {
              "type": "integer",
              "description": "The year the drama started airing."
            },
            "end_year": {
              "type": "integer",
              "description": "The year the drama finished airing."
            },
            "air_days": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "description": "The days of the week the drama aired."
            },
            "number_of_episodes": {
              "type": "integer",
              "description": "The total number of episodes for the drama."
            }
          },
          "required": [
            "title",
            "start_year",
            "end_year",
            "air_days",
            "number_of_episodes"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": [
      "actress_name",
      "network_name",
      "dramas_aired_on_network"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
