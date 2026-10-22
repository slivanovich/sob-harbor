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
2015–16 Minnesota Timberwolves season: The 2015–16 Minnesota Timberwolves season was the 27th season of the franchise in the National Basketball Association (NBA).  Before the season, the Timberwolves announced that head coach and team president Flip Saunders will not coach the team this season as he continued his battle with cancer.  Sam Mitchell was named interim head coach.  On October 25, 2015, Saunders died and the Wolves announced that Mitchell would be the interim coach for the entire season.  Around the start of the season, the Timberwolves would be the first team in NBA history to hold four players that were around 20 or younger between Andrew Wiggins, Zach LaVine, Karl-Anthony Towns, and Tyus Jones to start out a season.  It would also mark the final season under Kevin Garnett's time in the NBA and his return with the Timberwolves.

Brandon Roy: Brandon Dawayne Roy (born July 23, 1984) is an American basketball coach and a former professional basketball player who played for the Portland Trail Blazers and Minnesota Timberwolves in the National Basketball Association (NBA).  He was selected sixth in the 2006 NBA draft, having completed four years playing for the Washington Huskies.  His nickname was "B-Roy", but he was also referred to as "The Natural" by Trail Blazers announcer Brian Wheeler.  On December 10, 2011, Roy announced his retirement from basketball due to a degenerative knee condition, though he returned in 2012 to play five games for the Timberwolves.

Karl-Anthony Towns: Karl-Anthony Towns Jr. (born November 15, 1995) is a Dominican-American professional basketball player for the Minnesota Timberwolves of the National Basketball Association (NBA).  He played college basketball for the University of Kentucky.  Towns was named to the Dominican Republic national basketball team Olympic squad as a 16-year-old, although the Dominican Republic ultimately did not qualify for the 2012 Olympics.  He was selected with the first overall pick in the 2015 NBA draft by the Minnesota Timberwolves, and went on to be named NBA Rookie of the Year for the 2015–16 season.

Zacarías Ferreíra: Zacarías Ferreira is a Bachata artist from the Dominican Republic.  He was born in the 1970s in the Dominican Republic.  He is the uncle of professional basketball player Karl-Anthony Towns, who currently plays on the Minnesota Timberwolves, of the NBA.

Charlie Villanueva: Charlie Alexander Villanueva (born August 24, 1984) is a Dominican-American professional basketball player who last played for the Dallas Mavericks of the National Basketball Association (NBA).

Graham Betchart: Graham Betchart (born April 30, 1978) is a sports psychology mental skills coach and current director of mental training for Lucid Performance.  He is known for the concept "Play Present," which teaches that an athlete needs to stay focused on the task at hand and immediately move on to the next play despite results or outcomes.  He is also noted for the "MVP" program (Mediate, Visualize, Positive affirmation), a sports psychology mental training tool, as well as "WIN" (What is Important Now), which asserts that a player can only control attitude, effort, and focus.  Notable athletes Betchart has coached include Andrew Wiggins, Karl-Anthony Towns, and Ben Simmons, the first overall picks for the 2014, 2015, and 2016 NBA drafts, respectively.

Rick Brunson: Eric Daniel "Rick" Brunson (born June 14, 1972) is an American former professional basketball player and coach who is an assistant coach for the Minnesota Timberwolves of the National Basketball Association (NBA).  He played 9 seasons in the National Basketball Association (NBA) and has also worked as an assistant coach for several teams.  He played college basketball for Temple.

Tyus Jones: Tyus Robert Jones (born May 10, 1996) is an American professional basketball player for the Minnesota Timberwolves of the National Basketball Association (NBA).  He played college basketball for the Duke Blue Devils in his freshman season as part of the 2014–15 National Championship team.  He was ranked among the top 10 players in the national high school class of 2014 by Rivals.com, Scout.com and ESPN.  He was a Minnesota State High School League (MSHSL) Class 4A state champion, three-time Minnesota Associated Press Boys Basketball Player of the Year and three-time Minnesota Boys Basketball Gatorade Player of the Year for Apple Valley High School.  He played in the 2014 McDonald's All-American Boys Game, 2014 Jordan Brand Classic and the 2014 Nike Hoop Summit.  He won the skills competition at the 2014 McDonald's All-American Game and posted the only double-double in the 2014 Jordan Brand Classic.

Sam Mitchell (basketball): Samuel E. Mitchell Jr. (born September 2, 1963) is a former professional basketball player and coach who is currently head coach of the U.S. Virgin Islands national basketball team.  He was most recently the interim head coach for the Minnesota Timberwolves of the National Basketball Association (NBA).  He was also the head coach for the Toronto Raptors of the National Basketball Association (NBA) from 2004 to 2008.  Mitchell has also done analyst work for TSN and NBA TV as well as radio work for WHAL-AM in Columbus and WZGC-FM "92.9 The Game" in Atlanta.  He also currently works as a talk show co-host/analyst on SiriusXM NBA Radio.

Ricky Rubio: Ricard Rubio i Vives (born October 21, 1990) is a Spanish professional basketball player for the Utah Jazz of the National Basketball Association (NBA).  Rubio became the youngest player ever to play in the Spanish ACB League on October 15, 2005, at age 14.  He made his EuroLeague debut on October 24, 2006, at age 16, becoming the first player born in the 1990s to play in a EuroLeague game.  He is the fifth-youngest player to make their debut in the EuroLeague.  On June 25, 2009, he was drafted with the fifth pick in the first round of the 2009 NBA draft by the Timberwolves, making him the first player born in the 1990s to be drafted by the NBA.  The Timberwolves had an agreement in principle with his former Spanish team, DKV Joventut, to buy out his contract, but Rubio backed out of the deal.  On August 31, 2009, Joventut traded the rights to Rubio to FC Barcelona, and Rubio signed a six-year contract with FC Barcelona the following day.  In 2011, Rubio joined the Minnesota Timberwolves, and spent six seasons in Minnesota before being traded to the Jazz in June 2017.

Question: Who was the coach of Karl-Anthony Towns Jr., a Dominican-American professional basketball player for the Minnesota Timberwolves of the National Basketball Association ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The full name of the basketball player."
    },
    "player_nationality": {
      "type": "string",
      "description": "The nationality of the basketball player."
    },
    "player_team": {
      "type": "string",
      "description": "The NBA team the player plays for."
    },
    "coach_name": {
      "type": "string",
      "description": "The name of the coach."
    },
    "coach_role": {
      "type": "string",
      "description": "The specific role or type of coaching provided."
    }
  },
  "required": [
    "player_name",
    "player_nationality",
    "player_team",
    "coach_name",
    "coach_role"
  ],
  "additionalProperties": false
}
