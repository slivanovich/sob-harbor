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
Jaren Jackson: Jaren Jackson Sr. (born October 27, 1967) is an American professional basketball coach and former professional basketball player.  A 6'4" (1.93 m) shooting guard born in New Orleans, Louisiana, Jackson played at Georgetown University from 1985 to 1989 and graduated with a bachelor's degree in finance.  He was never drafted into the NBA but played 13 season for multiple teams.  He is best known for his tenure with the San Antonio Spurs, who he helped win their first NBA Championship in 1999.

2013–14 Miami Heat season: The 2013–14 Miami Heat season was the franchise's 26th season in the National Basketball Association (NBA).  They entered the season as two-time defending NBA champions (third overall), and three-time defending Eastern Conference champions, the fourth and final season playing with the "Big Three" of Dwyane Wade, LeBron James, and Chris Bosh, and the sixth season under head coach Erik Spoelstra.  In a rematch of the previous year's Eastern Conference Finals, the Heat defeated the Indiana Pacers in six games to become the first team to win four consecutive Eastern Conference championships since the 1986–87 Boston Celtics capped a Boston-dominant string going back to the 1983–84 season.  Miami's quest for a three-peat ended when the San Antonio Spurs, whom they would meet again in a rematch of last year's NBA Finals and defeated in seven games, won the NBA Finals by a 4–1 margin.  Following the season, LeBron left the Heat to rejoin the Cleveland Cavaliers.

2010 NBA Finals: The 2010 NBA Finals was the National Basketball Association (NBA)'s championship series for the 2009–10 season.  The best-of-seven playoff was contested between the Western Conference champion Los Angeles Lakers (who were also defending NBA champions), and the Eastern Conference champion Boston Celtics.  The Lakers defeated the Celtics, four games to three, to win the franchise's 16th NBA championship.  The 64th edition of the championship series was played between June 3 and June 17, was broadcast on ABC, and was watched by an average of 18.1 million people.

1998–99 NBA season: The 1999 NBA season was the 53rd season of the National Basketball Association (NBA).  Due to a lockout, the season did not start until February 5, 1999, after a new six-year Collective Bargaining Agreement was reached between the NBA and the National Basketball Players Association.  All 29 teams played a shortened 50-game regular season schedule and the 16 teams who qualified for the playoffs played a full post-season schedule.  That season's All-Star Game was also canceled.  The season ended with the San Antonio Spurs winning the franchise's first NBA championship, beating the New York Knicks 4 games to 1 in the 1999 NBA Finals.

2007–08 Detroit Pistons season: The 2007–08 Detroit Pistons season was the 67th season of the franchise, the 60th in the National Basketball Association (NBA), and the 51st in the Detroit area.  The Central Division Pistons finished the regular season with a 59–23 record, 14 games ahead of the second place Cavaliers.  Their 59 wins were the third most in franchise history.  In the NBA Playoffs, Detroit advanced to the Eastern Conference Finals for the sixth consecutive time since 2003, making them the first team since the 1986–87 Los Angeles Lakers to appear that many consecutive times in their respective Conference Finals.  The Pistons lost to the eventual NBA champions Boston Celtics in the Eastern Conference Finals four games to two.

2012–13 Miami Heat season: The 2012–13 Miami Heat season was the franchise's 25th season in the National Basketball Association (NBA).  They came into the season as the defending NBA champions, back-to-back Eastern Conference champions, the third season playing with the "Big Three" of Dwyane Wade, LeBron James, and Chris Bosh, and the fifth season under head coach Erik Spoelstra.  During the season, the Heat embarked on a 27-game winning streak, which still ranks as the 3rd longest winning streak in a single season in NBA history.  On June 3, 2013, the Heat defeated the Indiana Pacers in game seven of the Eastern Conference Finals to become the first team since the Chicago Bulls in 1998 to Three-peat as Eastern Conference champions.  The Heat then defeated the San Antonio Spurs in an NBA Finals that went the full seven games, handing the Spurs their very first loss in the NBA Finals, and with this victory in the NBA Finals, it echoed the 1997-98 Bulls as they had also been the last Eastern team to repeat as NBA champions.

2011–12 Oklahoma City Thunder season: The 2011–12 Oklahoma City Thunder season was the 4th season of the franchise's existence in Oklahoma City as a member of the National Basketball Association (NBA).  The Thunder continued to build on recent success in previous years by making the NBA Playoffs, defeating and sweeping the defending NBA champions, the Dallas Mavericks in the First Round, the Los Angeles Lakers in the Semifinals, and finally, the San Antonio Spurs in the Western Conference Finals to advance to the NBA Finals.  Despite winning Game 1 in the NBA Finals, the Thunder would then go on to lose the next four games and the NBA Finals against the Miami Heat.

2002 NBA Finals: The 2002 NBA Finals was the National Basketball Association (NBA)'s championship series for the 2001–02 season.  The best-of-seven playoff was contested between the Western Conference champion Los Angeles Lakers (who were also two-time defending NBA champions), and the Eastern Conference champion New Jersey Nets.  The Lakers swept the Nets four games to none to win the franchise's 14th NBA championship.  The 56th edition of the championship series was played between June 5 and June 12 and was broadcast on NBC — the last NBA games broadcast on the network to date.

San Antonio Spurs: The San Antonio Spurs are an American professional basketball team based in San Antonio, Texas.  The Spurs compete in the National Basketball Association (NBA) as a member of the league's Western Conference Southwest Division.  The team plays its home games at the AT&T Center in San Antonio.

1999 NBA Finals: The 1999 NBA Finals was the championship round of the shortened 1998–99 NBA season or the 1999 season.  The Western Conference champion San Antonio Spurs took on the Eastern Conference champion New York Knicks for the title, with the Spurs holding home court advantage.  The series was played under a best-of-seven format, with the first team to collect four game victories winning the series.  The Spurs defeated the Knicks 4 games to 1 to win the championship.  As of 2017, this is the last NBA Finals where neither team scored 100 or more points in any game during the series.

Question: The 1999 NBA Champions are from what conference?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "championship_year": {
      "type": "integer",
      "description": "The year the NBA championship was won."
    },
    "champion_team": {
      "type": "string",
      "description": "The name of the team that won the NBA championship."
    },
    "team_conference": {
      "type": "string",
      "description": "The conference of the champion team."
    },
    "team_division": {
      "type": "string",
      "description": "The division of the champion team within their conference."
    }
  },
  "required": [
    "championship_year",
    "champion_team",
    "team_conference",
    "team_division"
  ],
  "additionalProperties": false
}
