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
2016–17 Brooklyn Nets season: The 2016–17 Brooklyn Nets season was the 41st season of the franchise in the National Basketball Association (NBA), 50th season overall, and its 5th season playing in the New York City borough of Brooklyn.  In the month of February, the Nets would go 0-10 marking the first time that they lost every game in a single month since going 0-14 in November 2009.  This would be Brook Lopez's final year in Brooklyn and the first season with new management.  The Nets hired Kenny Atkinson after Lionel Hollins was fired back in January 2016 when Tony Brown took over as the interim.  Billy King was also fired as the infamous trade back in 2013 where they traded their first round picks in 2014, 2016, and 2018 in exchange for Kevin Garnett and Paul Pierce hurt the Nets badly.  Sean Marks took over as the Nets began rebuilding.  They would finish 20–62, their worst record since 2009–10.

Paul Westhead: Paul William Westhead (born February 21, 1939) is an American basketball coach who most recently was the head coach of the University of Oregon women's team.  In his first year as an NBA head coach, he led a rookie Magic Johnson and the Los Angeles Lakers to the 1980 NBA Title.  He has previously been a head coach for three National Basketball Association (NBA) teams and an assistant for four others, and has also coached in the National Collegiate Athletic Association (NCAA), Women's National Basketball Association (WNBA), American Basketball Association (ABA) and Japan Basketball League (JBL).  He won titles in both the NBA and WNBA, and is also remembered as the coach of the Loyola Marymount University (LMU) men's basketball team during that school's era of greatest basketball glory.  Westhead is known for an unorthodox, run-and-gun style called "The System."  He attended Saint Joseph's University.

1979–80 Philadelphia 76ers season: The 1979–1980 Philadelphia 76ers season was the 76ers 31st season in the National Basketball Association (NBA) and 17th season in Philadelphia.  They finished with a record of 59–23, their best since the 1967–68 season.  The team had acquired guard Lionel Hollins from the Portland Trail Blazers after their effort to obtain Pete Maravich failed as he signed with the Boston Celtics.  In the playoffs, they won the 1980 Eastern Conference Championship over the Boston Celtics 4–1.  In the 1980 NBA Finals they would lose to the Los Angeles Lakers 4–2.  The series was memorable for Julius Erving's baseline move in Game 4, and Magic Johnson's 42-point effort in Game 6 starting the game at center in place of an injured Kareem Abdul-Jabbar.

Hue Hollins: Hue Spencer Hollins, Sr. (November 28, 1940 - July 4, 2013)  was an American professional basketball referee for the National Basketball Association (NBA).  During his 27-year career in the NBA, Hollins officiated 19 NBA Finals games and five NBA All-Star Games.  He is notable for working the Finals every year during the 1990s and for a notorious call during a 1994 NBA Playoffs game between the Chicago Bulls and New York Knicks.  Hollins was probed by the Federal Bureau of Investigation (FBI) over the 2007 NBA betting scandal involving former referee Tim Donaghy.

Lionel Hollins: Lionel Eugene Hollins (born October 19, 1953) is an American basketball coach and former professional basketball player.  He most recently served as the head coach of the Brooklyn Nets of the National Basketball Association (NBA).

Baltimore Bullets (1944–54): The Baltimore Bullets were an American Basketball League (1944–47) team, and later, a Basketball Association of America (1947–49), and (beginning in 1949, following the BAA's absorption of the National Basketball League) a National Basketball Association team based in Baltimore.  The team folded November 27, 1954 with a 3–11 record, making the Bullets the last NBA franchise to do so, as of 2016.  Out of all defunct NBA teams, the Bullets were members of the association for the longest time and the only defunct team to win a championship.

2001–02 Memphis Grizzlies season: The 2001–02 NBA season was the Grizzlies 7th season in the National Basketball Association, and their first season in Memphis.  After six years of struggling in Vancouver, the Grizzlies relocated to Memphis.  Although it was the first NBA team for the city, Memphis played home to an American Basketball Association team from 1970–1975.  During the offseason, the Grizzlies acquired rookie Pau Gasol, Brevin Knight and former University of Memphis star Lorenzen Wright from the Atlanta Hawks, while acquiring Jason Williams and Nick Anderson from the Sacramento Kings.  However, Bryant Reeves missed the entire season due to a preseason back injury, and retired after playing just six seasons in the NBA, while Michael Dickerson played just four games due to a groin injury.

2004–05 Memphis Grizzlies season: The 2004–05 NBA season was the Grizzlies' tenth season in the National Basketball Association, and their fourth season in Memphis.  Coming off their first playoff appearance in franchise history, the Grizzlies had a new look and moved into their new arena, the FedExForum.  However, the team struggled with a 5–7 start as 71-year old Hubie Brown retired from coaching due to "unexpected health problems".  The Grizzlies would lose their next four games under Lionel Hollins before replacing him with TNT analyst Mike Fratello.  Under Fratello, the Grizzlies would win 12 of their 15 games in January climbing back into playoff connection.  Despite losing five of their last six games, the Grizzlies finished fourth in the Southwest Division with a 45–37 record, making their second consecutive trip to the playoffs.

Philip Brownstein: Philip Brownstein (May 17, 1906 – February 11, 1999) was an American basketball coach, scout, and general manager at the prep school and professional levels.  He was the interim head coach for the Chicago Stags, an early National Basketball Association team, for 11 games during the 1948–49 season, and went 10–1 while head coach Harold Olsen was out.  Brownstein then took over as the Stags' head coach for the 1949–50 season and led them to a 40–28 record.

Emanual Davis: Emanual Davis (born August 27, 1968) is a retired American professional basketball player.  As a 6'4" (1.96 m) point guard, Davis played college basketball at Delaware State University in Dover, Delaware.  Davis was never drafted by a National Basketball Association team, and played in the Continental Basketball Association, Italian Basketball League, United States Basketball League and the Atlantic Basketball Association in a span of 5 years before making it into the NBA.  Davis played in 6 NBA seasons from 1996–1998 and 1999–2003.  He played for the Houston Rockets, Seattle SuperSonics and Atlanta Hawks.

Question: After being replaced as coach for the Memphis Grizzles, Lionel Hollins went on to coach what National Basketball Association team?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "coach_name": {
      "type": "string",
      "description": "The name of the basketball coach."
    },
    "previous_team": {
      "type": "string",
      "description": "The team the coach was replaced from."
    },
    "subsequent_team": {
      "type": "string",
      "description": "The team the coach went on to coach after the previous team."
    },
    "subsequent_team_details": {
      "type": "object",
      "properties": {
        "league": {
          "type": "string",
          "description": "The league of the subsequent team."
        },
        "coaching_role": {
          "type": "string",
          "description": "The coaching role held at the subsequent team."
        },
        "firing_date_from_subsequent_team": {
          "type": "string",
          "description": "The date the coach was fired from the subsequent team, if mentioned."
        }
      },
      "required": [
        "league",
        "coaching_role"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "coach_name",
    "previous_team",
    "subsequent_team",
    "subsequent_team_details"
  ],
  "additionalProperties": false
}
