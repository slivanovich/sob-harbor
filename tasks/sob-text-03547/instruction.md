{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nTyphoon (Korean singer): Kim Gyun-woo (born April 8, 1983) better known as Typhoon or Jay Kim, is an American singer and actor of Korean descent.  He is a member of South Korean rock band TRAX and he was a member of South Korean ballad group S.M.  The Ballad.\n\nDumbfoundead: Jonathan Park (; born February 18, 1986), known professionally as Dumbfoundead, is an American rapper of Korean descent.  He originates from the Koreatown neighborhood of Los Angeles, California.\n\nJohn Park (musician): John Andrew Park (born September 13, 1988) is an American singer of Korean descent.  He was a semifinalist on the ninth season of \"American Idol\"; placing twentieth.  He is the runner-up of \"Superstar K2\", a Korean singing contest held by M.net.  He is currently signed to Music Farm Entertainment.\n\nEx-plicit linez: Brandon Jermaine Yun, better known by his stage name EXP (pronounced \"e-ex-pee\"), formerly EX-PLICIT LINEZ, is an American rapper and Former Radio personality for New York Korean Radio \"NYKR 1660 AM\", a mutual protégé of Drunken Tiger and Lee Hyun Do a.k.a. D.O. EXP first appeared on the underground rap scene in The Bronx in the mid 1990s on a DJ Platinum's mixtape series, \"Hate in Da Blood\".  He is one of the first generation of Asian American rappers to be involved in the Hip-Hop scene along with Jamez, John \"shogunna\" Chee and Mountain Brothers.  He's also known as one of the first Korean rappers to mix Korean and English words to rhyme in the song.  He is of Korean descent.\n\nBad Rap (documentary): Bad Rap is a 2016 documentary directed by Salima Koroma, and produced by Jaeki Cho.  The documentary follows the lives of Asian-American hip-hop artists Dumbfounddead, Awkwafina, Rekstizzy, and Lyricks, and their struggle to garner credibility in the American hip-hop industry.  \"Bad Rap\" premiered at the Tribeca Film Festival on April 13, 2016, and has since been screened at twelve other film festivals around the world.  As of September 7, 2017, the film has been made available on the iTunes Store, Amazon, VUDU, Google Play, and Netflix.\n\nWMTC-FM: WMTC (99.9 FM) is a Christian radio station, licensed to Vancleve, Kentucky, United States.  The station is currently owned by the Kentucky Mountain Bible College and features programming from Salem Media Group and Moody Radio.  WMTC's format consists of Southern Gospel music, as well as Christian talk and teaching programs such as \"Revive our Hearts with Nancy Leigh DeMoss\", \"Joni & Friends\", \"Focus on the Family\", and \"Unshackled! \", as well as children's programming such as \"Adventures in Odyssey\" and \"Jonathan Park\".\n\nK-Town (web series): K-Town is an American reality television series about the lives of a group of young Asian Americans living in Los Angeles' Koreatown.  The cast is mostly of Korean descent, with the exception of Scarlet Chan (who is of Chinese descent).  The show ran for two seasons.\n\nKwon Ri-se: Kwon Ri-se (August 16, 1991 – September 7, 2014), better known by her stage name RiSe, was a Japanese singer of Korean descent.  She was a member of the South Korean girl group Ladies' Code under Polaris Entertainment.  Prior to her joining Ladies' Code, she participated in Miss Korea 2009 and was crowned as \"Miss Korea Japan Jin\".  She was one of the Top 12 contestants of MBC's \"Star Audition The Great Birth\".  Born in Fukushima, Japan, she was fluent in Japanese as well as Korean.\n\nLucy H. Koh: Lucy Haeran Koh (born 1968) is a United States District Judge of the United States District Court for the Northern District of California and is a former nominee to be a United States Circuit Judge of the United States Court of Appeals for the Ninth Circuit.  She is the first Asian American United States district court judge in the Northern District of California, the first district court judge of Korean descent in the United States, the first female Korean American Article III judge, and the second Korean American federal judge, after Herbert Choy of the Ninth Circuit.\n\nMike B: Michael Byun (born January 11, 1989), better known by his stage name Mike B, is an London singer, songwriter, rapper, and producer of Korean descent.  He originates from the Koreatown neighborhood of Los Angeles, California.\n\nQuestion: Who directed the documentary that features an American rapper of Korean descent by the name of Jonathan Park?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"documentary_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the documentary.\"\n    },\n    \"documentary_director\": {\n      \"type\": \"string\",\n      \"description\": \"The director of the documentary.\"\n    },\n    \"featured_rapper_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"full_name\": {\n          \"type\": \"string\",\n          \"description\": \"The full name of the featured rapper.\"\n        },\n        \"stage_name\": {\n          \"type\": \"string\",\n          \"description\": \"The stage name of the featured rapper.\"\n        },\n        \"descent\": {\n          \"type\": \"string\",\n          \"description\": \"The ethnic descent of the rapper.\"\n        },\n        \"nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the rapper.\"\n        }\n      },\n      \"required\": [\n        \"full_name\",\n        \"stage_name\",\n        \"descent\",\n        \"nationality\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"documentary_title\",\n    \"documentary_director\",\n    \"featured_rapper_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "documentary_title": {
        "type": "string",
        "description": "The title of the documentary."
      },
      "documentary_director": {
        "type": "string",
        "description": "The director of the documentary."
      },
      "featured_rapper_details": {
        "type": "object",
        "properties": {
          "full_name": {
            "type": "string",
            "description": "The full name of the featured rapper."
          },
          "stage_name": {
            "type": "string",
            "description": "The stage name of the featured rapper."
          },
          "descent": {
            "type": "string",
            "description": "The ethnic descent of the rapper."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the rapper."
          }
        },
        "required": [
          "full_name",
          "stage_name",
          "descent",
          "nationality"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "documentary_title",
      "documentary_director",
      "featured_rapper_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
