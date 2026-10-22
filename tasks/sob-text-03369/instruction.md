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
Jason Terry: Jason Eugene Terry (born September 15, 1977) is an American professional basketball player for the Milwaukee Bucks of the National Basketball Association (NBA).  He plays at both guard positions and is nicknamed "The Jet".  Terry won the NBA Sixth Man of the Year award in 2009 and an NBA championship with the Dallas Mavericks in 2011.  Terry has made the third-most three-point field goals in NBA history.

Anthony Mason (basketball): Anthony George Douglas Mason (December 14, 1966 – February 28, 2015) was an American professional basketball player.  In his 13-year career he played with the New Jersey Nets, Denver Nuggets, New York Knicks, Charlotte Hornets, Milwaukee Bucks and Miami Heat of the National Basketball Association.  He averaged 10.8 points and 8.3 rebounds in his 13-year NBA career.  During the prime of his career in the mid-1990s, he earned the NBA Sixth Man of the Year Award in 1995 and then led the NBA in minutes played in the subsequent two seasons.  In 1997, he earned All-NBA (3rd team) and NBA All-Defensive Team (2nd team).  He was selected to the 2001 NBA All-Star Game.

Roy Tarpley: Roy James Tarpley (November 28, 1964 – January 9, 2015) was an American professional basketball player.  He played the power forward and center positions in the National Basketball Association (NBA), earning an NBA Sixth Man of the Year Award in 1988.  Tarpley was banned from the NBA because of his drug and alcohol abuse.  He had great success playing in Europe, most notably for Olympiacos and Aris.

Jamal Crawford: Aaron Jamal Crawford (born March 20, 1980) is an American professional basketball player for the Minnesota Timberwolves of the National Basketball Association (NBA).  Crawford played his high school basketball for Rainier Beach High School, a basketball powerhouse in Seattle, before committing to play for the University of Michigan.  Crawford was selected by the Cleveland Cavaliers but was traded on draft day to the Chicago Bulls.  In his career, he has also played for the New York Knicks, Golden State Warriors, Atlanta Hawks, Portland Trail Blazers and Los Angeles Clippers.  He won the NBA Sixth Man of the Year Award in 2010, 2014 and 2016, becoming the first three-time winner of the award in NBA history.  He currently holds the record for most career four-point plays made with 50 (55 when counting the playoffs).

1999 NBA draft: The 1999 NBA Draft was held on June 30, 1999, at the MCI Center (now Verizon Center) in Washington, D.C.  It was the first draft in which four players from the same college were picked in the first round, with Elton Brand (1st selection), Trajan Langdon (11th), Corey Maggette (13th) and William Avery (14th) being selected out of Duke University.  It is widely viewed as one of the best draft classes, with a total of nine future NBA All-Stars being chosen, as well as three winners of the NBA Sixth Man of the Year Award—Manu Ginóbili, Jason Terry, and Lamar Odom.  Undrafted Pablo Prigioni made his NBA debut at 2012/2013 season as the oldest rookie in league history, at age 35.

Shooting guard: The shooting guard (SG), also known as the two or off guard, is one of the five positions in a regulation basketball game.  A shooting guard's main objective is to score points for his team.  Some teams ask their shooting guards to bring up the ball as well; these players are known colloquially as combo guards.  Kobe Bryant, for example, as a shooting guard was as good a playmaker as he was a scorer; other examples of combo guards are Dwyane Wade, Allen Iverson, James Harden, Manu Ginóbili, Jamal Crawford, Randy Foye and Jason Terry.  A player who can switch between playing shooting guard and small forward is known as a swingman.  Notable swing men (also known as wing players) include Jimmy Butler, Tracy McGrady, Vince Carter, Joe Johnson, Andre Iguodala, Andrew Wiggins, Evan Turner and Tyreke Evans.  In the NBA, shooting guards usually range from 6' 4" (1.93 m) to 6' 7" (2.01 m) and 5' 9" (1.75 m) to 6' 0" (1.83 m) in the WNBA.

Leandro Barbosa: Leandro Mateus Barbosa (] ; born November 28, 1982) is a Brazilian professional basketball player who last played for the Phoenix Suns of the National Basketball Association (NBA).  He previously won the NBA Sixth Man of the Year Award with the Suns in 2007 and an NBA championship with the Golden State Warriors in 2015.  In Brazil, he is nicknamed "Leandrinho" (Little Leandro), and in the USA he is nicknamed "The Brazilian Blur", referring to his speed.

Lamar Odom: Lamar Joseph Odom (born November 6, 1979) is an American retired professional basketball player.  As a member of the Los Angeles Lakers in the National Basketball Association (NBA), he won NBA championships in 2009 and 2010 and was named the NBA Sixth Man of the Year in 2011.

Detlef Schrempf: Detlef Schrempf (born January 21, 1963) is a German-American retired professional basketball player.  He played college basketball for the Washington Huskies from 1981 to 1985, and was drafted into the National Basketball Association (NBA) by the Dallas Mavericks in the first round of the 1985 NBA draft, with the eighth overall pick.  He was an All-NBA Third Team member in 1995, a three-time NBA All-Star and the NBA Sixth Man of the Year twice.

Toni Kukoč: Toni Kukoč (] ; born September 18, 1968) is a Croatian retired professional basketball player who is currently Special Advisor to Jerry Reinsdorf, the owner of the Chicago Bulls.  After a highly successful period in European basketball, he was one of the first established European stars to play in the National Basketball Association (NBA).  He won the NBA Sixth Man of the Year Award in 1996.

Question: When did the American retired professional basketball player born who won NBA Sixth Man of the Year Award with Manu Ginóbili and Jason Terry?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The full name of the professional basketball player."
    },
    "player_nationality": {
      "type": "string",
      "description": "The nationality of the player."
    },
    "player_status": {
      "type": "string",
      "description": "The professional status of the player (e.g., 'retired professional basketball player')."
    },
    "birth_date": {
      "type": "string",
      "description": "The birth date of the player in 'Month Day, Year' format."
    },
    "award_details": {
      "type": "object",
      "properties": {
        "award_name": {
          "type": "string",
          "description": "The name of the award won by the player."
        },
        "award_year": {
          "type": "integer",
          "description": "The year the player won the specific award."
        },
        "other_winners_mentioned_for_award": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of other players mentioned in the context as also having won the same award."
        }
      },
      "required": [
        "award_name",
        "award_year",
        "other_winners_mentioned_for_award"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "player_name",
    "player_nationality",
    "player_status",
    "birth_date",
    "award_details"
  ],
  "additionalProperties": false
}
