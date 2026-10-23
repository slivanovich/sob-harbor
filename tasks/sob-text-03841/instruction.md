{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGeof Motley: Geof Motley OAM is a former Australian rules footballer and coach who played for South Australian National Football League (SANFL) side Port Adelaide.  Motley was born near Alberton Oval, the home ground of the Port Adelaide Football Club, and grew up supporting Port Adelaide.\n\nNorwood–Port Adelaide rivalry: The Norwood–Port Adelaide rivalry is Australian rules football's oldest and one of its most intense rivalries.  It is contested between the Norwood Football Club and the Port Adelaide Football Club.  Together Port Adelaide (36) and Norwood (30) have won 66 South Australian National Football League (SANFL) premierships since the founding of the competition in 1878.  As the SANFL competition has been suspended due to war, only 132 seasons have been played, therefore together Norwood and Port Adelaide have won exactly half of all SANFL premierships awarded.  The two clubs have met in finals 50 times with 17 of those grand finals including 2 war-time grand finals.\n\nJacob Surjan: Jacob Adam Surjan (born 15 August 1985 in Perth, Australia) is an Australian rules footballer of Croatian descent and former player of the Port Adelaide Football Club.  He currently serves as the development coach of the Port Adelaide Football Club at AFL level, and as the midfield coach of Port Adelaide at SANFL level.\n\nPort Adelaide Football Club: The Port Adelaide Football Club is a professional Australian rules football club based in Alberton, Port Adelaide, South Australia.  The club's senior team plays in the Australian Football League (AFL) under the nickname Power, whilst its reserves and development teams compete in the South Australian National Football League (SANFL) under the nickname Magpies.  Port Adelaide is the oldest professional sporting club in South Australia and the fifth-oldest club in the AFL.  Since the club's first game on 24 May 1870, the club has won 36 South Australian league premierships, including six in a row.  The club also won the Champions of Australia competition on a record four occasions.  In 1997, the club joined the Australian Football League as the only pre-existing non-Victorian club—and subsequently added the 2004 AFL premiership to its achievements.\n\nJesse Palmer (Australian footballer): Jesse Palmer (born 17 October 1996) is an Australian rules footballer playing for the Port Adelaide Football Club in the Australian Football League (AFL).  He was drafted by the Port Adelaide Football Club with their third selection and seventy-eighth overall in the 2014 national draft.  He made his debut in the forty point loss against Melbourne in round 21, 2016 at the Adelaide Oval.\n\nDan Houston: Daniel \"Dan\" Houston (born 12 May 1997) is an Australian rules footballer playing for the Port Adelaide Football Club in the Australian Football League (AFL).  He was drafted by the Port Adelaide Football Club with their third selection and forty-fifth overall in the 2016 rookie draft.  Prior to the start of the 2017 season, he was promoted to the senior list and subsequently made his debut in the twenty-eight point win against Sydney in the opening round of the season at the Sydney Cricket Ground.\n\nChad Cornes: Chad Studley Cornes (born 12 November 1979) is a former professional Australian rules footballer who played for the Port Adelaide Football Club and Greater Western Sydney Giants in the Australian Football League (AFL).  He was a member of the Port Adelaide side which won the premiership in 2004.  On 3 July 2013, he retired from AFL football due to a troublesome knee.  Cornes is currently serving as the SANFL coach of Port Adelaide.\n\nGavin Wanganeen: Gavin Adrian Wanganeen (born 18 June 1973) is a former Australian rules footballer who played for Essendon in the Australian Football League (AFL) and Port Adelaide in both the AFL and the South Australian National Football League (SANFL).  Wanganeen won the 1993 Brownlow Medal.  Wanganeen is a descendant of the Kokatha Mula people.  He is the first cousin of brothers Aaron and Alwyn Davey.\n\nJohn Butcher (Australian footballer): John Butcher (born 3 July 1991) is a former professional Australian rules footballer who played for the Port Adelaide Football Club in the Australian Football League (AFL).  He was the earliest of the three Port Adelaide players drafted in the first round in the 2009 AFL Draft (he went at pick #8).  Butcher's younger brother Danny was drafted to Port Adelaide as part of the Rookie Draft in 2011 at pick 21.\n\nAshley Fernee: Ashley Fernee (born 24 June 1977) is a former Australian rules footballer who played in the Australian Football League (AFL).  He was selected for the Adelaide Football Club in the 1995 draft, having previously played with the Calder Cannons.  Fernee only played two games for the Adelaide Football Club in 1996, debuting against Fitzroy Football Club in round 17.  In spite of those two games, he was not selected to play in 1997, and in 1998 things were not looking promising, with Michelangelo Rucci stating that the \"wait will go on unless a long injury list strikes again\".  Fernee did not play in 1998, and he was delisted by the Adelaide Football Club in October of that year.  He played for the SANFL team, South Adelaide Football Club, in 1999, and nominated for the AFL draft at the end of the season.  Unsuccessful, Fernee left Adelaide to return to Victoria, where he played for the East Keilor Football Club.\n\nQuestion: Gavin Adrian Wanganeen played for The Port Adelaide Football Club that is located where?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"club_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the football club.\"\n    },\n    \"player_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the player associated with the club.\"\n    },\n    \"club_location\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"suburb\": {\n          \"type\": \"string\",\n          \"description\": \"The suburb where the club is based.\"\n        },\n        \"city\": {\n          \"type\": \"string\",\n          \"description\": \"The city where the club is located.\"\n        },\n        \"state\": {\n          \"type\": \"string\",\n          \"description\": \"The state where the club is located.\"\n        }\n      },\n      \"required\": [\n        \"suburb\",\n        \"city\",\n        \"state\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"club_name\",\n    \"player_name\",\n    \"club_location\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "club_name": {
        "type": "string",
        "description": "The name of the football club."
      },
      "player_name": {
        "type": "string",
        "description": "The name of the player associated with the club."
      },
      "club_location": {
        "type": "object",
        "properties": {
          "suburb": {
            "type": "string",
            "description": "The suburb where the club is based."
          },
          "city": {
            "type": "string",
            "description": "The city where the club is located."
          },
          "state": {
            "type": "string",
            "description": "The state where the club is located."
          }
        },
        "required": [
          "suburb",
          "city",
          "state"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "club_name",
      "player_name",
      "club_location"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
