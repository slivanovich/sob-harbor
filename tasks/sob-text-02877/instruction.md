{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nList of Oregon Ducks head football coaches: The Oregon Ducks football program is a college football team representing the University of Oregon that is a member of the Pac-12 Conference.  The team has had 32 head coaches since its founding in 1894.  The Ducks have played in more than 1,100 games in 113 seasons.  In those seasons, eight different coaches have led Oregon to bowl games: Hugo Bezdek, Shy Huntington, Jim Aiken, Len Casanova, Rich Brooks, Mike Bellotti, Chip Kelly and Mark Helfrich.  Conference championships have been won by Huntington, Prink Callison, Jim Aiken, Casanova, Brooks, Bellotti, Kelly, and Mark Helfrich.  Brooks is the all-time leader in games coached; Mike Bellotti holds the record for most victories, while Chip Kelly is the leader in win percentage for coaches with more than one season of service.\n\nOregon Ducks football statistical leaders: The Oregon Ducks football statistical leaders are individual statistical leaders of the Oregon Ducks football program in various categories, including passing rushing receiving total offense, defensive stats, and kicking.  Within those areas, the lists identify single-game, single-season, and career leaders.  The Ducks represent the University of Oregon in the NCAA's Pac-12 Conference.\n\n1995 Oregon Ducks football team: The 1995 Oregon Ducks football team represented the University of Oregon during the 1995 NCAA Division I-A football season.  They were led by head coach Mike Bellotti, who was in his 1st season as head coach of the Ducks after replacing Rich Brooks, who resigned in February 1995 to become the head coach of the St. Louis Rams.  They played their home games at Autzen Stadium in Eugene, Oregon and participated as members of the Pacific-10 Conference.\n\n1990 Oregon Ducks football team: The 1990 Oregon Ducks football team represented the University of Oregon in the 1990 NCAA Division I-A football season.  The Ducks scored 341 points while the defense allowed 221 points.  Led by head coach Rich Brooks, the Ducks competed in the Freedom Bowl.\n\nKellen Clemens: Kellen Vincent Clemens (born June 6, 1983) is an American football quarterback for the Los Angeles Chargers of the National Football League (NFL).  He was selected by the New York Jets in the second round of the 2006 NFL Draft.  He played college football at Oregon.\n\n2009 Oregon Ducks football team: The 2009 Oregon Ducks football team represented the University of Oregon in the 2009 NCAA Division I FBS football season.  The team was led by head coach Chip Kelly in his first season as a head coach at the Division I FBS level.  Kelly was only the third Ducks head coach since 1977 and led the Ducks to a Pac-10 Championship and was named Pac-10 Coach of the Year.  He took over for Mike Bellotti.\n\nOregon Ducks football: The Oregon Ducks football program is a college football team for the University of Oregon, located in the U.S. state of Oregon.  The team competes at the NCAA Division I level in the FBS and is a member of the Pac-12 Conference (Pac-12).  Known as the Ducks, the team was commonly called the Webfoots until the mid-1960s.  The first football team was fielded in 1894.  Oregon plays its home games at the 54,000 seat Autzen Stadium in Eugene; its main rivals are the Oregon State Beavers and the Washington Huskies.  The Ducks and Beavers historically end each regular season with the Civil War rivalry game in late November.\n\n2008 Oregon Ducks football team: The 2008 Oregon Ducks football team represented the University of Oregon in the 2008 NCAA Division I FBS football season.  This was the final season for Mike Bellotti as the Ducks' head coach; he was promoted to become the school's athletic director after the season.  The Ducks played their home games at Autzen Stadium.  They finished the season 10–3, 7–2 in Pac-10 play, and were invited to the Holiday Bowl where they defeated Oklahoma State 42–31.\n\nNate Costa: Nathaniel William \"Nate\" Costa (born May 15, 1988) is a former American football player and current American football coach at the University of Oregon.  He played quarterback at the University of Oregon from 2006 to 2010 and was a team captain of the 2010 Oregon Ducks football team.  He is currently an Offensive Graduate Assistant coach on the Duck football coaching staff.\n\n2005 Oregon Ducks football team: In 2005, Oregon had success behind senior quarterback Kellen Clemens and a new spread offense.  During a game at Arizona, Clemens suffered a broken ankle.  At that point Oregon was 8-1 (their only loss was to #1 ranked USC 45-13, the loss was vacated in 2010), and still in the hunt for a BCS game.  Oregon won their final three games and their success led them into contention for a bid to the Fiesta Bowl.  The Ducks finished the regular season with a 10-1 record, their best finish since their Joey Harrington-led, Fiesta Bowl-winning 2001–2002 team.  They finished 5th overall in the BCS ranking system, which would in many years have been high enough to earn them a bid to a BCS Bowl.  In 2005, however, there were no at-large bids available to Oregon.  Ohio State finished just ahead of the Ducks, in 4th place, guaranteeing them one of the at-large berths (although they had an inferior 10-2 record).  Notre Dame finished 6th in the BCS, also securing a BCS bid due to a pre-existing clause in the BCS contract.  Many college football fans were outraged that two teams with worse records were selected over the Ducks.  Moreover, for the second consecutive year, the Pac-10 conference had a team that finished with a one-loss season snubbed by the BCS (the Cal Bears finished 10-1 in 2004).  It was later demonstrated that Oregon drew the highest bowl ratings in college football, calling the argument that TV ratings hurt the Ducks' BCS chances into question.  The situation (and others like it in recent years) has led to more calls for a playoff system to replace the BCS, which has received widespread criticism from college football fans.  Instead of a BCS game, they were assigned to the 2005 Holiday Bowl versus the Oklahoma Sooners.  Playing without their starting quarterback, Kellen Clemens, and combined with a strong showing from the Sooners, the Ducks fell in a close game, 17-14, finishing the season tied for the second-best in school history with a 10-1 overall record (the Southern Cal game was deemed vacated by violations in 2010).\n\nQuestion: Who does the 2005 Oregon Ducks football team quarterback currently play for?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"player_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the quarterback for the 2005 Oregon Ducks football team.\"\n    },\n    \"player_position\": {\n      \"type\": \"string\",\n      \"description\": \"The primary position of the player.\"\n    },\n    \"college_team_year\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"team_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the college team.\"\n        },\n        \"season_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the player played for the college team.\"\n        }\n      },\n      \"required\": [\n        \"team_name\",\n        \"season_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"current_nfl_team\": {\n      \"type\": \"string\",\n      \"description\": \"The NFL team the player currently plays for.\"\n    }\n  },\n  \"required\": [\n    \"player_name\",\n    \"player_position\",\n    \"college_team_year\",\n    \"current_nfl_team\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "player_name": {
        "type": "string",
        "description": "The name of the quarterback for the 2005 Oregon Ducks football team."
      },
      "player_position": {
        "type": "string",
        "description": "The primary position of the player."
      },
      "college_team_year": {
        "type": "object",
        "properties": {
          "team_name": {
            "type": "string",
            "description": "The name of the college team."
          },
          "season_year": {
            "type": "integer",
            "description": "The year the player played for the college team."
          }
        },
        "required": [
          "team_name",
          "season_year"
        ],
        "additionalProperties": false
      },
      "current_nfl_team": {
        "type": "string",
        "description": "The NFL team the player currently plays for."
      }
    },
    "required": [
      "player_name",
      "player_position",
      "college_team_year",
      "current_nfl_team"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
