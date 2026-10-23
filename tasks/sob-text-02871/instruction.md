{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nStephen Coniglio: Stephen J. Coniglio (born 15 December 1993) is a professional Australian rules footballer playing for the Greater Western Sydney Giants in the Australian Football League (AFL).  He previously played for Swan Districts in the West Australian Football League (WAFL), and represented Western Australia at the 2010 and 2011 National Under 18 Championships, winning the Larke Medal as the best player in the competition in 2011.  Drafted with the second pick in the 2011 AFL National Draft, Coniglio made his debut for Greater Western Sydney in the first round of the 2012 season, and was later nominated for the 2012 AFL Rising Star award.\n\nAdam Tomlinson: Adam Tomlinson (born 10 August 1993) is a professional Australian rules footballer playing for the Greater Western Sydney Giants in the Australian Football League (AFL).  He was recruited by Greater Western Sydney with their seventh selection and ninth overall in the 2011 national draft.  He made his debut in the sixty-three point loss against Sydney at ANZ Stadium in Greater Western Sydney's inaugural match in round one.\n\nCallan Ward: Callan Ward (born 10 April 1990) is a professional Australian rules footballer playing for the Greater Western Sydney Giants in the Australian Football League (AFL).  He previously played for the Western Bulldogs between 2008 and 2011.  Ward has served as Greater Western Sydney Giants co-captain since the club's inaugural season in 2012, and is also the current games record holder for the Giants with 131 games.\n\nJosh Kelly (footballer): Josh Kelly (born 12 February 1995) is a professional Australian rules footballer playing for the Greater Western Sydney Giants in the Australian Football League (AFL).  He was recruited by the Greater Western Sydney Giants with the second overall selection in the 2013 national draft.  Kelly had a breakout year in 2017, winning inclusion in the All-Australian team and finishing fifth in the Brownlow Medal.\n\nHeath Shaw: Heath Shaw (born 27 November 1985) is a professional Australian rules footballer playing for the Greater Western Sydney Giants in the Australian Football League (AFL).  He previously played for the Collingwood Football Club from 2004 to 2013.\n\nWill Hoskin-Elliott: Will Hoskin-Elliott is a professional Australian rules footballer playing for the Collingwood Football Club in the Australian Football League (AFL).  He previously played for the Greater Western Sydney Giants from 2012 to 2016.  He was taken with the fourth overall selection in the 2011 national draft, and played in the Greater Western Sydney's first season, in 2012.  Hoskin-Elliot made his debut in Round 1, against Sydney .\n\nTim Golds: Tim Golds (born 6 April 1993) is a former professional Australian rules footballer who played for the Greater Western Sydney Giants in the Australian Football League (AFL).  He was also listed with the Collingwood Football Club in 2016, but did not play a senior match.  He was recruited by the Greater Western Sydney Giants as an underage selection at the age of 17.  Golds made his debut for the Giants in round 20, 2012, against Gold Coast at Carrara Stadium.  He was delisted by the Giants in October 2015.\n\nRay Shaw (Australian footballer): Ray Shaw (born 27 April 1954) is a former Australian rules footballer who played for Collingwood in the Victorian Football League (VFL).  His younger brothers Tony and Neville as well as his two sons Heath and Rhyce also played for Collingwood.\n\nDaniel Lloyd (footballer): Daniel Lloyd (born 18 February 1992) is a professional Australian rules footballer playing for the Greater Western Sydney Giants in the Australian Football League (AFL).  He was drafted by Greater Western Sydney with their second selection and twenty-sixth overall in the 2016 rookie draft.  He made his debut in the three point win against Collingwood at Spotless Stadium in round eight of the 2017 season.\n\nToby Greene: Toby Greene (born 25 September 1993) is a professional Australian rules footballer playing for the Greater Western Sydney Giants in the Australian Football League (AFL).  He was recruited by the Greater Western Sydney Giants with the 11th overall selection in the 2011 national draft.\n\nQuestion: Ray Shaw (born 27 April 1954) is a former Australian rules footballer who played for Collingwood in the Victorian Football League (VFL), his two sons also played for Collingwood, one son is Heath Shaw,   a professional Australian rules footballer playing for the Greater Western Sydney Giants in which organization? \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"player_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the player.\"\n    },\n    \"current_team\": {\n      \"type\": \"string\",\n      \"description\": \"The team the player currently plays for.\"\n    },\n    \"league_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The full name of the league or organization.\"\n        },\n        \"abbreviation\": {\n          \"type\": \"string\",\n          \"description\": \"The abbreviation of the league or organization.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"abbreviation\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"player_name\",\n    \"current_team\",\n    \"league_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "player_name": {
        "type": "string",
        "description": "The name of the player."
      },
      "current_team": {
        "type": "string",
        "description": "The team the player currently plays for."
      },
      "league_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The full name of the league or organization."
          },
          "abbreviation": {
            "type": "string",
            "description": "The abbreviation of the league or organization."
          }
        },
        "required": [
          "name",
          "abbreviation"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "player_name",
      "current_team",
      "league_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
