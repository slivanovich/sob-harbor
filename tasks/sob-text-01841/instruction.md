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
Houston Rockets all-time roster: The Houston Rockets are an American professional basketball team based in Houston, Texas.  The team plays in the Southwest Division of the Western Conference in National Basketball Association (NBA).  The team was established in 1967, and played in San Diego, California for four years before being moved to Houston.  In the Rockets debut season, they won only 15 games.  However, after drafting Elvin Hayes first overall in the 1969 NBA Draft, they made their first appearance in the playoffs in 1969.  After Hayes was traded, Moses Malone was acquired to replace him.  Malone won two MVPs during his time in Houston, and he led the Rockets to the conference finals in his first year with the team.  He also took the Rockets to the NBA Finals in 1981, but they were defeated in six games by the Boston Celtics.  In 1984, the Rockets drafted Hakeem Olajuwon, who led them to the 1986 Finals in his second year, where they lost again to Boston.  In the next seven seasons, they lost in the first round of the playoffs five times.  They won their first NBA championship in 1994, led by Olajuwon, who won Finals MVP.  They repeated as champions the next year, and Olajuwon won Finals MVP once again.  To date, the Rockets have not advanced to the finals again.  The Rockets missed the playoffs from 1999–2003, and did not make the playoffs again until after they drafted Yao Ming in 2002.  Since then, the Rockets have had a winning season in all but two of the next 14 seasons and, led by James Harden, advanced to the conference finals in 2015.

1998 NBA Playoffs: The 1998 NBA Playoffs was the postseason tournament of the National Basketball Association's 1997-98 season.  The tournament concluded with the Eastern Conference champion Chicago Bulls defeating the Western Conference champion Utah Jazz 4 games to 2 in the NBA Finals.  The Bulls also achieved a second three peat, a goal unrivaled since the Boston Celtics in 1966.  The 1998 playoffs was the last involving the Jordan-led Bulls (Chicago didn't make the playoffs again until 2005).  Michael Jordan was named NBA Finals MVP for the sixth and final time.

1987 NBA Playoffs: The 1987 NBA Playoffs was the postseason tournament of the National Basketball Association's 1986–87 season.  The tournament concluded with the Western Conference champion Los Angeles Lakers defeating the Eastern Conference champion Boston Celtics 4 games to 2 in the NBA Finals.  The Lakers earned their 10th NBA championship, and Magic Johnson was named NBA Finals MVP for a then-record third time.

Larry Bird: Larry Joe Bird (born December 7, 1956) is an American professional basketball executive, former coach and former player, most recently serving as president of the Indiana Pacers in the National Basketball Association (NBA).  Since retiring as a player for the Boston Celtics, he was a mainstay in the Indiana Pacers organization, but stepped down from the position of president following the first-round of the 2017 Eastern Conference playoffs.

1993 NBA Playoffs: The 1993 NBA Playoffs was the postseason tournament of the National Basketball Association's 1992–93 season.  The tournament concluded with the Eastern Conference champion Chicago Bulls defeating the Western Conference champion Phoenix Suns 4 games to 2 in the NBA Finals.  Michael Jordan was named NBA Finals MVP for the third straight year.  This was the Suns' second Western Conference title; they made their first NBA Finals appearance since 1976, losing to the Boston Celtics.

2003 NBA Playoffs: The 2003 NBA Playoffs was the postseason tournament of the National Basketball Association's 2002–03 season.  The tournament concluded with the Western Conference champion San Antonio Spurs defeating the Eastern Conference champion New Jersey Nets 4 games to 2 in the NBA Finals.  Tim Duncan was named NBA Finals MVP for the second time.

1982 NBA Playoffs: The 1982 NBA Playoffs were the postseason tournament of the National Basketball Association's 1981–82 season.  The tournament concluded with the Western Conference champion Los Angeles Lakers defeating the Eastern Conference champion Philadelphia 76ers 4 games to 2 in the NBA Finals.  Magic Johnson was named NBA Finals MVP for the second time.

1985 NBA Playoffs: The 1985 NBA Playoffs was the postseason tournament of the National Basketball Association's 1984–85 season.  The tournament concluded with the Western Conference champion Los Angeles Lakers defeating the Eastern Conference champion Boston Celtics 4 games to 2 in the NBA Finals.  Kareem Abdul-Jabbar was named NBA Finals MVP for the second time (he had won the award under his birth name, Lew Alcindor, as a Buck in 1971).

1973 NBA Playoffs: The 1973 NBA Playoffs was the postseason tournament of the National Basketball Association's 1972–73 season.  The tournament concluded with the Eastern Conference champion New York Knicks defeating the Western Conference champion Los Angeles Lakers 4 games to 1 in the NBA Finals.  The Knicks won their second (and most recent) NBA title.  Willis Reed became the first player to be named NBA Finals MVP twice.

1986 NBA Playoffs: The 1986 NBA Playoffs was the postseason tournament of the National Basketball Association's 1985–86 season.  The tournament concluded with the Eastern Conference champion Boston Celtics defeating the Western Conference champion Houston Rockets 4 games to 2 in the NBA Finals.  Larry Bird was named NBA Finals MVP for the second time.

Question: The person named NBA Finals MVP for the second time in the 1986 NBA Playoffs retired as a player for what team?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The name of the player who won the NBA Finals MVP award."
    },
    "award_details": {
      "type": "object",
      "properties": {
        "award_year": {
          "type": "integer",
          "description": "The year of the NBA Playoffs when the award was won."
        },
        "award_name": {
          "type": "string",
          "description": "The name of the award received."
        },
        "award_occurrence": {
          "type": "string",
          "description": "Indicates if it was the first, second, etc., time the player won the award."
        }
      },
      "required": [
        "award_year",
        "award_name",
        "award_occurrence"
      ],
      "additionalProperties": false
    },
    "retirement_team": {
      "type": "string",
      "description": "The team for which the player retired as a player."
    }
  },
  "required": [
    "player_name",
    "award_details",
    "retirement_team"
  ],
  "additionalProperties": false
}
