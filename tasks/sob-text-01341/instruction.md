{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\n2010 Independence Bowl: The 2010 AdvoCare V100 Independence Bowl was the thirty-fifth edition of the college football bowl game and was played at Independence Stadium in Shreveport, Louisiana.  The game started at 5:00 PM US EST on Monday, December 27, 2010.  The game was telecast on ESPN2 and featured the Georgia Tech Yellow Jackets from the Atlantic Coast Conference (ACC) versus Air Force from the Mountain West Conference (MWC), the nation's top two rushing teams.\n\n2009 Champs Sports Bowl: The 2009 Champs Sports Bowl was a college football bowl game between the Wisconsin Badgers of the Big Ten Conference and the Miami Hurricanes of the Atlantic Coast Conference.  Played at the Citrus Bowl in Orlando, Florida, the game started at 8:00 PM US EST on Tuesday, December 29, 2009 and was televised by ESPN.  Wisconsin won the game 20-14.\n\n2009 Independence Bowl: The 2009 AdvoCare V100 Independence Bowl was the thirty-fourth edition of the college football bowl game, and was played at Independence Stadium in Shreveport, Louisiana.  The game started at 5:00 PM US EST on Monday, December 28, 2009.  The game was telecast on ESPN2 and the Georgia Bulldogs defeated the Texas A&M Aggies by a score of 44-20.\n\n2008 Auto Club 500: The 2008 Auto Club 500 was the second race of the 2008 NASCAR Sprint Cup Series, and started on February 24, 2008, at Auto Club Speedway of Southern California in Fontana, California, a suburb of Los Angeles.  The race was telecast on Fox starting at 3:30 PM US EST/12:30 PM PST, with MRN and Sirius Satellite Radio's broadcast starting at 2:45 PM EST/11:45 AM PST.  Rain stopped the race on Lap 87 and the race would continue on Monday, February 25 at 1 PM US EST/10 AM PDT.\n\n2009 Auto Club 500: The 2009 Auto Club 500 was the second race of the 2009 NASCAR Sprint Cup season.  the 500 mi race occurred on February 22, 2009, at the 2 mi Auto Club Speedway in Fontana, California, 60 mi from Los Angeles and was one of the cleanest races in the history of the track with only one caution for an on track incident out of all 250 laps.  Fox broadcast the race beginning at 5 pm US EST with radio coverage on MRN (terrestrial) and Sirius XM Radio (satellite) starting at 5:15 pm US EST.  The race started at 3 pm local time, and run into prime time, counterprogramming against the Academy Awards.\n\n2009 Armed Forces Bowl: The 2009 Armed Forces Bowl was the seventh edition of the college football bowl game, and was played at Amon G. Carter Stadium in Fort Worth, Texas.  The game started at 12:00 PM US EST on Thursday, December 31, 2009.  The game was telecast on ESPN and matched the Houston Cougars of Conference USA and the Air Force Falcons of the Mountain West Conference.  The game earned a 1.6 rating.\n\n2009 Hawaii Bowl: The 2009 Hawaii Bowl was the eighth edition of the college football bowl game, played at Aloha Stadium in Honolulu, Hawaii.  The game started at 3:00 pm local time (8:00 pm US EST) on Thursday, December 24, 2009, with the SMU Mustangs of Conference USA beating the Nevada Wolf Pack of the Western Athletic Conference 45–10.\n\n2009 Holiday Bowl: The 2009 Holiday Bowl was the thirty-second edition of the college football bowl game and was played at Qualcomm Stadium in San Diego, California.  The game started at 5:00 PM US PST on Wednesday, December 30, 2009.  The game was telecast on ESPN.  The Nebraska Cornhuskers defeated the Arizona Wildcats 33–0 for the first shutout in the history of the bowl.  This was a rematch of the two teams, who faced each other in the 1998 Holiday Bowl, where Arizona defeated Nebraska 23–20.\n\n2009 Meineke Car Care Bowl: The 2009 Meineke Car Care Bowl was the eighth edition of the college football bowl game, and was played at Bank of America Stadium in Charlotte, North Carolina.  The game started at 4:30 PM US EST on Saturday, December 26, 2009 and was telecasted on ESPN and ESPN360.  The Pittsburgh Panthers defeated the North Carolina Tar Heels 19–17 with a 33-yard field goal and .52 seconds remaining in the game.\n\n2009 Texas A&amp;M Aggies football team: The 2009 Texas A&M Aggies football team (often referred to as \"A&M\" or the \"Aggies\") represented Texas A&M University in the 2009 NCAA Division I FBS football season.  The team was led by second-year head coach Mike Sherman and played their home games at Kyle Field in College Station, Texas.  The Aggies finished the season 6–7, 3–5 in Big 12 play and lost in the Independence Bowl 44–20 against Georgia.\n\nQuestion: Who coached the team that lost in a game that started at 5:00 PM US EST on Monday, December 28, 2009?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"game_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the game.\"\n    },\n    \"game_date\": {\n      \"type\": \"string\",\n      \"description\": \"The date the game was played.\"\n    },\n    \"game_start_time_est\": {\n      \"type\": \"string\",\n      \"description\": \"The start time of the game in US EST.\"\n    },\n    \"losing_team_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"team_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the team that lost the game.\"\n        },\n        \"score\": {\n          \"type\": \"integer\",\n          \"description\": \"The score of the losing team.\"\n        },\n        \"coach_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the coach of the losing team.\"\n        }\n      },\n      \"required\": [\n        \"team_name\",\n        \"score\",\n        \"coach_name\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"game_name\",\n    \"game_date\",\n    \"game_start_time_est\",\n    \"losing_team_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "game_name": {
        "type": "string",
        "description": "The name of the game."
      },
      "game_date": {
        "type": "string",
        "description": "The date the game was played."
      },
      "game_start_time_est": {
        "type": "string",
        "description": "The start time of the game in US EST."
      },
      "losing_team_details": {
        "type": "object",
        "properties": {
          "team_name": {
            "type": "string",
            "description": "The name of the team that lost the game."
          },
          "score": {
            "type": "integer",
            "description": "The score of the losing team."
          },
          "coach_name": {
            "type": "string",
            "description": "The name of the coach of the losing team."
          }
        },
        "required": [
          "team_name",
          "score",
          "coach_name"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "game_name",
      "game_date",
      "game_start_time_est",
      "losing_team_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
