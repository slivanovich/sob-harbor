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
A. R. Kennedy: Albert Rutherford "Bert" Kennedy (October 24, 1876 – September 5, 1969) was an American football player and coach.  He was born on the family farm in rural Wakarusa Township, just outside Lawrence, Kansas, to Leander Jack Kennedy (September 21, 1836 – June 29, 1903) and Amanda E. Kennedy (née Todd) (November 23, 1841 – March 4, 1926).  He played college football at both the University of Kansas, three seasons from 1895 to 1897 including one as team captain, and at the University of Pennsylvania, for one season in 1899.  Kennedy also played one year of professional football immediately after graduating from Penn.  During this time he played in the first professional football game ever played in Madison Square Garden which was also the first indoor professional football game ever played.  After his one and only year of playing professionally, he returned to his home state of Kansas and coached football at Washburn University (1903, 1916–1917), at the University of Kansas (1904–1910), and at the Haskell Institute, now known as Haskell Indian Nations University, (1911–1916), compiling a career record of 96–43–10.  His 52 wins with the Kansas Jayhawks football team are the most in the program's history.

Nate Jacks: Nathaniel "Nate" Jacks (born January 31, 1980) is a former American professional football player who was a cornerback in the National Indoor Football League (NIFL) for six seasons.  He played college football for Bacone College, Kansas and Dodge City Community College.  The Lincoln Capitols signed him in 2004 after he was cut from the New York Jets during the 2003 NFL Training Camp.  Nate also played professionally for the first professional football team in Anchorage, AK, Alaska Wild of the Intense Football League (IFL) and World League Hamburg Sea Devils.  Alaska Wild (notable for being the first ever professional football team in the state of Alaska).

Bub Weller: Raymond Fred "Bub" Weller (June 30, 1902 – August 18, 1993) was an American football player who played college football for the University of Nebraska and played five years and 60 games of professional football in the early years of the National Football League (NFL).  Weller was unanimously selected for All-American honors at the tackle position in 1922.  Weller was 6 ft and weighed during his years as a professional football player.

Bubba Smith: Charles Aaron "Bubba" Smith (February 28, 1945 – August 3, 2011) was an American professional football player who became an actor after his retirement from the sport.  He first came into prominence at Michigan State University, where he twice earned All-American honors as a defensive end on the Spartans football team.  He had a major role in a 10–10 tie with Notre Dame in 1966 that was billed as "The Game of the Century."  He was one of only three players to have his jersey number retired by the program.  He was inducted into the College Football Hall of Fame in 1988.

Fred Chicken: Fred S. Chicken was a professional football player who spent one season in the early National Football League, then called the American Professional Football Association, with the Rock Island Independents.  However, he also played for the Minneapolis Marines (1915-1918), prior to that team's entry into the NFL.  He was the star halfback of the 1907 undefeated and unscored upon Minneapolis North High School National Football Champions of the US.  They had defeated the Oak Park, Illinois football team, another undefeated and unscored upon team, to claim that title.

Boss Nigger: Boss Nigger (also known as Boss and The Black Bounty Killer) is a 1975 Western film directed by Jack Arnold.  It stars former football player Fred Williamson, who both wrote and co-produced the film.  "Boss Nigger" is the first film for which Williamson was credited as screenwriter or producer.

Ray Whipple: Ray Christopher Whipple (November 14, 1893 - December 1973) was an American football player.  He played at the end position in college football for the Notre Dame Fighting Irish in professional football from the Detroit Heralds from 1917 to 1920.  He played for the 1920 Detroit Heralds during the first regular season of the National Football League (then known as the American Professional Football Association).  He was selected as an All-Pro player in 1917.

Down 'n Dirty: Down 'n Dirty is an action movie starring Fred Williamson as Dakota Smith.  It also stars Bubba Smith, Gary Busey , Tony Lo Bianco, Beverly Johnson, Randy J. Goodwin, David Carradine and Charles Napier.

1920 APFA season: The 1920 APFA season was the inaugural season of the American Professional Football Association—renamed the National Football League in 1922.  The league was formed on August 20, 1920, by independent professional American football teams from Ohio, all of whom had previously played in the Ohio League or New York Pro Football League (NYPFL).  At the meeting, they first called their new league the American Professional Football Conference.  A second organizational meeting was held in Canton on September 17, adding more teams to the league.  At the meeting, the name of the league became the American Professional Football Association.  Four other teams also joined the Association during the year.  Meanwhile, Jim Thorpe of the Canton Bulldogs was named the APFA's first president but continued to play for the team.

Dick King (American football): Richard Stewart Cutter "Dick" King (February 9, 1895 - October 16, 1930) was an All-American and professional football player.  He played college football for Harvard University and was selected as an All-American at halfback) in 1915.  In 1916, he signed with the Pine Village professional football team, becoming one of the first eastern football stars to play professional football.  He also played professional football for the Hammond Pros, Milwaukee Badgers, Rochester Jeffersons and St. Louis All-Stars in 1923.

Question: What is the name of the character played by Fred Williamson in a movie which also starred the American professional football player?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "movie_title": {
      "type": "string",
      "description": "The title of the movie."
    },
    "fred_williamson_character_name": {
      "type": "string",
      "description": "The name of the character played by Fred Williamson in the movie."
    },
    "other_football_player_actor": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the other American professional football player who also starred in the movie."
        },
        "notable_football_achievement": {
          "type": "string",
          "description": "A notable achievement or characteristic of the other football player's career."
        }
      },
      "required": [
        "name",
        "notable_football_achievement"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "movie_title",
    "fred_williamson_character_name",
    "other_football_player_actor"
  ],
  "additionalProperties": false
}
