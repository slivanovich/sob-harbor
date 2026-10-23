{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\n1998 Toledo Rockets football team: The 1998 Toledo Rockets football team was an American football team that represented the University of Toledo in the Mid-American Conference (MAC) during the 1998 NCAA Division I-A football season.  In their eighth season under head coach Gary Pinkel, the Rockets compiled a 7–5 record (6–2 against MAC opponents), finished in first place in the MAC's West Division, lost to Marshall in the MAC Football Championship Game (17–23), and outscored all opponents by a combined total of 229 to 216.\n\n1998 SMU Mustangs football team: The 1998 SMU Mustangs football team represented Southern Methodist University in the 1998 NCAA Division I-A football season as members of the Western Athletic Conference (WAC) in the Mountain Division.  They played their home games at the Cotton Bowl in Dallas, Texas.  Head coach Mike Cavan returned for his second season leading SMU, following a 6–5 season in 1997, SMU's first winning season since the 1987–88 SMU \"death penalty\" was handed down by the NCAA, the highest punishment possible in the association.  SMU finished the season 5–7 (4–4 WAC), but SMU vacated 10 games after Steve Malin was found to have been ineligible due to academic fraud.\n\n1998 Baylor Bears football team: The 1998 Baylor Bears football team (variously \"Baylor\", \"BU\", or the \"Bears\") represented Baylor University in the 1998 NCAA Division I-A football season.  They were represented in the Big 12 Conference in the South Division.  They played their home games at Floyd Casey Stadium in Waco, Texas.  They were coached by head coach Dave Roberts.\n\n1998 Marshall Thundering Herd football team: The 1998 Marshall Thundering Herd football team represented Marshall University in the 1998 NCAA Division I-A football season.  It was Marshall's second season competing at the NCAA Division I-A level.  The team won their second consecutive Mid-American Conference (MAC) championship and was invited to the Motor City Bowl.\n\n1998 San Diego State Aztecs football team: The 1998 San Diego State Aztecs football team represented San Diego State University during the 1998 NCAA Division I-A football season as a member of the Western Athletic Conference (WAC).  This was the last season for the Aztecs in the WAC, as they became a charter member of the Mountain West Conference in the 1999 season.\n\n1978 NCAA Division I-A football season: The 1978 NCAA Division I-A football season was the first season of Division I-A football; Division I-A was created in 1978 when Division I was subdivided into Division I-A and I-AA for football only.  The season came down to a rare #1 vs. #2 post-season meeting as #1 Penn State and #2 Alabama met in the New Year's Day Sugar Bowl.  The game is most remembered for Alabama's goal line stand with four minutes left in the game.  On fourth down and a foot, Alabama managed to keep Penn State out of the end zone and went on to win 14-7.  Keith Jackson, who did the play by play for ABC, called it the greatest game he'd ever seen.  76,824 people packed the Louisiana Superdome, which was tremendously loud.\n\n1978 Lamar Cardinals football team: The 1978 Lamar Cardinals football team represented Lamar University in the 1978 NCAA Division I-A football season as a member of the Southland Conference.  NCAA Division I split into Division I-A, the current Football Bowl Subdivision (FBS), and Division I-AA, the current Football Championship Subdivision (FCS), for football in 1978.  Lamar and the Southland Conference opted to compete at the Division I-A level.  The Cardinals played their home games at Cardinal Stadium now named Provost Umphrey Stadium in Beaumont, Texas.  Lamar finished the 1978 season with a 2–8–1 overall record and a 0–5 conference record.  The 1978 season marked Bob Frederick's final season as Lamar's head football coach.\n\n1998 NCAA Division I-A football rankings: Two human polls and one formulaic ranking make up the 1998 NCAA Division I-A football rankings.  Unlike most sports, college football's governing body, the National Collegiate Athletic Association (NCAA), does not bestow a National Championship title for Division I-A football.  That title is primarily bestowed by different polling agencies.  There are several polls that currently exist.  The main weekly polls are the AP Poll and Coaches Poll.  The Bowl Championship Series (BCS) Standings made their debut in 1998, and began being released about halfway through the season.\n\nGreg Jerman: Gregory Stephen Jerman (born January 24, 1979) is a former American football offensive lineman.  He played four seasons in the National Football League for the Miami Dolphins from 2002 to 2004 and for the Buffalo Bills in 2005.  He played college football at Baylor University from 1998 to 2001.  He was born in 1979 at Hyannis, Massachusetts, and attended Franklin High School in El Paso, Texas.  He was admitted to the Texas State Bar in 2014 and began practicing law with the Lubbock County Criminal District Attorney's office.\n\n1998 San Jose State Spartans football team: The 1998 San Jose State Spartans football team represented San Jose State University during the 1998 NCAA Division I-A football season as a member of the Western Athletic Conference.  The team was led by head coach Dave Baldwin, in his second year as head coach at San Jose State.  They played their home games at Spartan Stadium in San Jose, California.  The Spartans finished the 1998 season with a record of four wins and eight losses (4–8, 3–5 WAC).\n\nQuestion: Which university Gregory Stephen Jerman represented as member of BU in the 1998 NCAA Division I-A football season?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"player_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the football player.\"\n    },\n    \"season\": {\n      \"type\": \"integer\",\n      \"description\": \"The NCAA Division I-A football season.\"\n    },\n    \"university_represented\": {\n      \"type\": \"string\",\n      \"description\": \"The university the player represented during the specified season.\"\n    },\n    \"team_nickname\": {\n      \"type\": \"string\",\n      \"description\": \"The nickname or abbreviation used for the university's team.\"\n    }\n  },\n  \"required\": [\n    \"player_name\",\n    \"season\",\n    \"university_represented\",\n    \"team_nickname\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "player_name": {
        "type": "string",
        "description": "The full name of the football player."
      },
      "season": {
        "type": "integer",
        "description": "The NCAA Division I-A football season."
      },
      "university_represented": {
        "type": "string",
        "description": "The university the player represented during the specified season."
      },
      "team_nickname": {
        "type": "string",
        "description": "The nickname or abbreviation used for the university's team."
      }
    },
    "required": [
      "player_name",
      "season",
      "university_represented",
      "team_nickname"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
