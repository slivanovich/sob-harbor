{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nKhalid El-Amin: Khalid El-Amin (born April 25, 1979) is an American professional basketball player who last played for Marinos de Anzoátegui of the Liga Profesional de Baloncesto (LPB).  He was a member of the 1999 University of Connecticut men's basketball team that won the NCAA championship.  He is originally from Minnesota where he played for North High School in Minneapolis.  In 2000, he was selected in the 2nd round by the Chicago Bulls of the NBA Draft and played 50 games for them, averaging 6.3 points and 2.9 assists per game.\n\nPhiladelphia 76ers: The Philadelphia 76ers (also commonly known as the Sixers) are an American professional basketball team based in the Philadelphia metropolitan area.  The 76ers compete in the National Basketball Association (NBA) as a member of the league's Eastern Conference Atlantic Division and play at Wells Fargo Center.  Founded in 1946 and originally known as the Syracuse Nationals, they are one of the oldest franchises in the NBA, and one of only eight (out of 23) to survive the league's first decade.\n\nRuss Millard: Russ Millard (born March 1, 1973 in Bradenton, Florida) is an American basketball player who was selected by the Phoenix Suns in the 2nd round (39th overall) of the 1996 NBA Draft.  A 6'8\" forward from University of Iowa, Millard never appeared in an NBA game.\n\nJeff Wilkins (basketball): Jeffrey \"Jeff\" Wilkins (born March 9, 1955) is a retired American professional basketball player who played in the National Basketball Association (NBA) and other leagues.  A 6'11\" 230 lb center born in Chicago, Illinois, Wilkins played college basketball at Illinois State University and was selected with the 15th pick in the 2nd round of the 1977 NBA Draft by the San Antonio Spurs.\n\nGreg Stokes: Gregory Lewis \"Greg\" Stokes (born August 5, 1963) is a retired American professional basketball player who was selected by the Philadelphia 76ers in the 2nd round (33rd overall) of the 1985 NBA Draft.  A 6'10\" forward-center from the University of Iowa, Stokes played in 2 NBA seasons for the 76ers and Sacramento Kings.  In his NBA career, Stokes played in 42 games and scored a total of 130 points.  He played at Hamilton High School in Hamilton, Ohio in 1980-1981 and help lead team to a 25-1 record and regional finals appearance.  He also played professionally in Italy and Australia.  His daughter Kiah Stokes played college basketball at the University of Connecticut from 2011-2015.  Kiah now plays professional basketball for the WNBA team the New York Liberty.\n\nDorie Murrey: Dorie S. Murrey (born September 7, 1943) is a retired American professional basketball player.  He was a 6'8\" (2.03 m) 215 lb (97½ kg) forward and he played collegiately at the University of Detroit Mercy.  He has played in the NBA from 1966 to 1972.  He was originally selected with the second pick in the 2nd round of the 1966 NBA draft by the Detroit Pistons.  He was taken in two expansion drafts.  In 1967 he was made available by the Pistons to be selected by the Seattle SuperSonics, and in 1970 he was made available by the Sonics to be selected by the Portland Trail Blazers.  He was traded 3 games into the 1970–71 season, on October 10, 1970, by the Trail Blazers to the Baltimore Bullets in exchange for a 1971 2nd round draft choice (Rick Fisher).  During his six-year NBA career Murrey averaged 4.7 points and 4.4 rebounds per game in 357 career games.\n\nLavoy Allen: Lavoy Allen (born February 4, 1989) is an American professional basketball player who last played for the Indiana Pacers of the National Basketball Association (NBA).  He was selected in the 2nd Round, 50th overall pick in the 2011 NBA draft by the Philadelphia 76ers.  Allen is the son of a truck driver, and did not play much basketball until eighth grade.  He attended Pennsbury High School, where he was coached by Frank Sciolla.  Rivals.com ranked him the 14th best center in his class, and Scout.com named him the 110th overall prospect.  Allen committed to Temple University and coach Fran Dunphy.\n\nShelton Jones: Shelton Jones (born April 4, 1966) is a retired American professional basketball player who played collegiately at St. John's University.  He was selected by the San Antonio Spurs in the 2nd round (27th overall) of the 1988 NBA Draft.  Shelton played only one year in the NBA during the 1988-89 season, splitting time with the Spurs, Golden State Warriors and mainly, the Philadelphia 76ers, for whom he also appeared in the NBA Slam Dunk Contest, finishing on 4th place after advancing to the semi-finals.  After the season, he was selected by the Minnesota Timberwolves as the 16th pick in the NBA Expansion Draft.  After his selection, he said: \"I'm a little stunned right now.  I thought I'd be taken by Orlando because I'd heard some things.  Things like this happen.  That's the kind of year I had.  I'll make the best of the situation.  I look forward to getting out there and meeting with the coach.  I don't even know who it is.\" .  As it turned out, the Timberwolves waived him before the season began, and he never played in the NBA again.\n\nDarington Hobson: Darington O'Neal Hobson (born September 29, 1987) is an American professional basketball player for the Guangxi Weizhuang Rhinos of the Chinese National Basketball League (NBL).  He played college basketball for the University of New Mexico Lobos men's basketball team.  Born in Las Vegas, Nevada, Hobson attended five high schools and a junior college before finally becoming eligible to play Division I college basketball.  Hobson was drafted in the 2nd round (37th overall) of the 2010 NBA Draft by the Milwaukee Bucks.  Hobson was waived on December 2, 2010, due to injury.  A year later, Hobson was re-signed by the Bucks for the 2011–12 season.  He was waived again on February 3, 2012.\n\nJamie Feick: Jamie Feick (born July 3, 1974) is an American retired professional basketball player.  He was selected by the Philadelphia 76ers in the 2nd round (48th overall) of the 1996 NBA draft.  A 6 ft center from Michigan State University, Feick played in the NBA from 1996 to 2001.  He played for the Charlotte Hornets, San Antonio Spurs, Milwaukee Bucks and New Jersey Nets.\n\nQuestion: Which American professional basketball team was founded in 1946 and picked Jamie Feick in the 2nd round of the 1996 NBA draft?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"team_name\": {\n      \"type\": \"string\",\n      \"description\": \"The current name of the professional basketball team.\"\n    },\n    \"founded_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the team was founded.\"\n    },\n    \"original_team_name\": {\n      \"type\": \"string\",\n      \"description\": \"The original name of the team when it was founded.\"\n    },\n    \"draft_pick_details\": {\n      \"type\": \"object\",\n      \"description\": \"Details about the specific player drafted by the team.\",\n      \"properties\": {\n        \"player_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the player drafted.\"\n        },\n        \"draft_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the player was drafted.\"\n        },\n        \"draft_round\": {\n          \"type\": \"integer\",\n          \"description\": \"The round in which the player was drafted.\"\n        },\n        \"overall_pick\": {\n          \"type\": \"integer\",\n          \"description\": \"The overall pick number in the draft.\"\n        }\n      },\n      \"required\": [\n        \"player_name\",\n        \"draft_year\",\n        \"draft_round\",\n        \"overall_pick\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"team_name\",\n    \"founded_year\",\n    \"original_team_name\",\n    \"draft_pick_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "team_name": {
        "type": "string",
        "description": "The current name of the professional basketball team."
      },
      "founded_year": {
        "type": "integer",
        "description": "The year the team was founded."
      },
      "original_team_name": {
        "type": "string",
        "description": "The original name of the team when it was founded."
      },
      "draft_pick_details": {
        "type": "object",
        "description": "Details about the specific player drafted by the team.",
        "properties": {
          "player_name": {
            "type": "string",
            "description": "The name of the player drafted."
          },
          "draft_year": {
            "type": "integer",
            "description": "The year the player was drafted."
          },
          "draft_round": {
            "type": "integer",
            "description": "The round in which the player was drafted."
          },
          "overall_pick": {
            "type": "integer",
            "description": "The overall pick number in the draft."
          }
        },
        "required": [
          "player_name",
          "draft_year",
          "draft_round",
          "overall_pick"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "team_name",
      "founded_year",
      "original_team_name",
      "draft_pick_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
