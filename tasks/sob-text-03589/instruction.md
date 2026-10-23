{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nShaquille Harrison: Shaquille Harrison (born October 3, 1993) is an American professional basketball player for the Northern Arizona Suns of the NBA G League.  He played college basketball at Tulsa.\n\nJoe Jackson (basketball): Joseph Nathaniel Jackson (born February 8, 1992) is an American professional basketball player for the Northern Arizona Suns of the NBA G League.  He played college basketball for the University of Memphis where he was named the 2013 Conference USA Player of the Year.\n\nAskia Booker: Askia Booker (born August 31, 1993) is an American professional basketball player for the Northern Arizona Suns of the NBA G League.  He played college basketball for the Colorado Buffaloes as a point guard.  In his senior year in 2014–15, he earned second-team all-conference honors in the Pac-12.\n\nTyrone Ellis: Tyrone Ellis (born October 5, 1977) is a retired naturalized Georgian professional basketball player, originally from the United States.  He is 1.93 m (6 ft 4 in) tall and played as a shooting guard.  He is currently the first head coach ever named for the Northern Arizona Suns of the NBA G League.\n\nAlec Peters: Alec Peters (born April 13, 1995) is an American professional basketball player for the Phoenix Suns of the National Basketball Association (NBA), on a two-way contract with the Suns' NBA G League affiliate, the Northern Arizona Suns.  He played college basketball for Valparaiso University, where he was an All-American in 2017.\n\nJosh Gray (basketball): Joshua Gray (born September 9, 1993) is an American professional basketball player for the Northern Arizona Suns of the NBA G League.  He played college basketball for Texas Tech, Odessa College and LSU.\n\n2016–17 Phoenix Suns season: The 2016–17 NBA season was the Suns' 49th season in the NBA.  It is also their 24th season in the Talking Stick Resort Arena.  It is also the first season with a team-owned D-League affiliate, called the Northern Arizona Suns, which recently relocated to the nearby Prescott Valley.  The Suns failed to qualify for the playoffs for the seventh straight season.\n\nWashington NBA G League team: The Washington NBA G League team is an American professional basketball team in the NBA G League and an affiliate of the Washington Wizards of the National Basketball Association.  Based in Washington, D.C., the team will play their home games during the 2018–19 season at the St. Elizabeths East Entertainment and Sports Arena.  The team became the twenty-third G League team to be owned by an NBA team.\n\nMike James (basketball, born 1990): Michael Perry James (born August 18, 1990) is an American professional basketball player for the Phoenix Suns of the National Basketball Association (NBA), on a two-way contract with the Suns' NBA G League affiliate, the Northern Arizona Suns.  He was a high school basketball standout playing for Grant High School in Portland, and played college basketball for Eastern Arizona College and Lamar University.\n\nNorthern Arizona Suns: The Northern Arizona Suns are an NBA G League team based in Prescott Valley, Arizona and the minor league affiliate of the Phoenix Suns.  The franchise began as the Long Beach Jam in 2003 under the revived American Basketball Association and moved to Bakersfield in the D-League in 2006 as the Bakersfield Jam; after 10 years in Bakersfield, California, the franchise was moved to Prescott Valley in 2016 by the Phoenix Suns and were subsequently renamed the Northern Arizona Suns.\n\nQuestion: Joseph Nathaniel Jackson (born February 8, 1992) is an American professional basketball player for the Northern Arizona Suns of the NBA G League team based in Prescott Valley, Arizona and the minor league affiliate of which sports organization?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"player_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the basketball player.\"\n    },\n    \"g_league_team\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the NBA G League team the player plays for.\"\n    },\n    \"parent_nba_affiliate\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the NBA team that the G League team is affiliated with.\"\n    },\n    \"g_league_team_location\": {\n      \"type\": \"string\",\n      \"description\": \"The city where the G League team is based.\"\n    }\n  },\n  \"required\": [\n    \"player_name\",\n    \"g_league_team\",\n    \"parent_nba_affiliate\",\n    \"g_league_team_location\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "player_name": {
        "type": "string",
        "description": "The full name of the basketball player."
      },
      "g_league_team": {
        "type": "string",
        "description": "The name of the NBA G League team the player plays for."
      },
      "parent_nba_affiliate": {
        "type": "string",
        "description": "The name of the NBA team that the G League team is affiliated with."
      },
      "g_league_team_location": {
        "type": "string",
        "description": "The city where the G League team is based."
      }
    },
    "required": [
      "player_name",
      "g_league_team",
      "parent_nba_affiliate",
      "g_league_team_location"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
