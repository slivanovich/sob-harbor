Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Phil Jones (footballer, born 1992): Philip Anthony Jones (born 21 February 1992) is an English professional footballer who plays for Premier League club Manchester United and the England national team.  Before joining Manchester United, Jones played for Blackburn Rovers at both youth and senior levels.  Although primarily a centre-back, he has also been used as a right-back or defensive midfielder.

Luke Shaw: Luke Paul Hoare Shaw (born 12 July 1995) is an English professional footballer who plays as a left-back for Premier League club Manchester United and the England national team.

Chris Smalling: Christopher Lloyd Smalling (born 22 November 1989) is an English professional footballer who plays as a centre-back for Premier League club Manchester United and the England national team.

Jesse Lingard: Jesse Ellis Lingard (born 15 December 1992) is an English professional footballer who plays as a winger for Premier League club Manchester United and the England national team.

Wayne Rooney: Wayne Mark Rooney ( ; born 24 October 1985) is an English professional footballer who plays for Premier League club Everton.  He has played much of his career as a forward, and he has also been used in various midfield roles.  He is the record goalscorer for the England national team and for Manchester United.  At club level, he has won every honour available in English, Continental and European football, with the exception of the European Super Cup.  Along with Michael Carrick, he is the only English player to win the Premier League, FA Cup, UEFA Champions League, League Cup, UEFA Europa League and FIFA Club World Cup.

2016 FA Community Shield: The 2016 FA Community Shield (also known as the 2016 FA Community Shield supported by McDonald's for sponsorship reasons) was the 94th FA Community Shield, an annual English football match played between the winners of the previous season's Premier League and FA Cup.  The match was contested by 2015–16 FA Cup winners Manchester United, and Leicester City, champions of the 2015–16 Premier League.  It was held at Wembley Stadium a week before the Premier League season kicked off.  Manchester United won the match 2–1 with goals from Jesse Lingard and Zlatan Ibrahimović, either side of a goal from Leicester striker Jamie Vardy.

Ashley Young: Ashley Simon Young (born 9 July 1985) is an English professional footballer who plays as a winger for Premier League club Manchester United and the England national team.

Danny Drinkwater: Daniel Noel Drinkwater (born 5 March 1990) is an English professional footballer who plays as a midfielder for Premier League club Chelsea and the England national team.  He has previously spent time on loan at Huddersfield Town, Cardiff City, Watford and Barnsley, and also played for Manchester United and Leicester City.  Drinkwater has also played internationally for England at under-18 and under-19 levels.  He is a Premier League winner, having won the competition with Leicester in the 2015–16 season.

Marcus Rashford: Marcus Rashford (born 31 October 1997) is an English professional footballer who plays as a forward for Premier League club Manchester United and the England national team.

Joe Hart: Charles Joseph John "Joe" Hart (born 19 April 1987) is an English professional footballer who plays as a goalkeeper for West Ham United, on loan from fellow Premier League club Manchester City, and the England national team.  With over 100 Premier League clean sheets, Hart holds the joint record for the most Premier League Golden Glove awards (four) and has amassed 73 international caps since his debut in 2008.

Question: Manchester United won the match 2–1 with goals from which English professional footballer who plays as a winger for Premier League club Manchester United and the England national team?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The full name of the footballer."
    },
    "player_nationality": {
      "type": "string",
      "description": "The nationality of the footballer."
    },
    "player_club": {
      "type": "string",
      "description": "The Premier League club the footballer plays for."
    },
    "player_national_team": {
      "type": "string",
      "description": "The national team the footballer plays for."
    },
    "player_position": {
      "type": "string",
      "description": "The primary playing position of the footballer."
    },
    "match_contribution": {
      "type": "object",
      "properties": {
        "match_name": {
          "type": "string",
          "description": "The name of the match where the contribution occurred."
        },
        "team_contributed_for": {
          "type": "string",
          "description": "The team the player contributed for in the match."
        },
        "contribution_type": {
          "type": "string",
          "description": "The type of contribution made by the player in the match (e.g., 'scored a goal')."
        }
      },
      "required": [
        "match_name",
        "team_contributed_for",
        "contribution_type"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "player_name",
    "player_nationality",
    "player_club",
    "player_national_team",
    "player_position",
    "match_contribution"
  ],
  "additionalProperties": false
}
