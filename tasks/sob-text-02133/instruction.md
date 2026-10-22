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
1986–87 European Cup Winners' Cup: The 1986–87 season of the European Cup Winners' Cup was won by Ajax in the final against Lokomotive Leipzig.  The young Ajax side, which included the likes of Marco van Basten, Frank Rijkaard and Dennis Bergkamp, was guided to victory by its coach Johan Cruyff.  It was Ajax's only title in the competition, and was added to a hat-trick of European Cup wins from 1971 to 1973.  They also went on to win another European Cup and a UEFA Cup in the 1990s.

Rosenborg BK in European football: Rosenborg Ballklub is an association football club from Trondheim, Norway.  The team has participated in 32 seasons of Union of European Football Associations (UEFA) club competitions, including 21 seasons in the European Cup and Champions League, 16 seasons in the UEFA Cup and Europa League, one season in the Cup Winners' Cup and one season in the Intertoto Cup.  Rosenborg has played six times in the UEFA Cup after qualifying via the Champions League and once via the Intertoto Cup.  It has played 206 UEFA games, resulting in 81 wins, 39 draws and 86 defeats.  The club's first appearance was in the 1965–66 European Cup Winners' Cup, and it subsequently entered tournaments in six seasons until 1974–75.  The club's next appearance was in the 1986–87 European Cup, and then in the 1989–90 European Cup.  Since then, Rosenborg has been involved in a UEFA tournament every season except the 2006–07 season.  The club's best performance is reaching the quarter-finals of the 1996–97 Champions League, while their only European trophy came when they co-won the 2008 UEFA Intertoto Cup.

Dennis Bergkamp: Dennis Nicolaas Maria Bergkamp (] ; born 10 May 1969) is a former Dutch professional footballer, who is the assistant manager at Ajax.  Originally a wide midfielder, Bergkamp was moved to main striker and then to second striker, where he remained throughout his playing career.  Bergkamp has been described by Jan Mulder as having "the finest technique" of any Dutch international and a "dream for a striker" by teammate Thierry Henry.

Arnold Mühren: Arnold Johannes Hyacinthus Mühren (born 2 June 1951 in Volendam, North Holland) is a Dutch football manager and former midfielder.  His older brother Gerrie, also a midfield player, won three European Cup titles with Ajax in the early 1970s.  Mühren is among the few players to have won all three major UEFA-organised club competitions, the European Cup (1972–73), the Cup Winners' Cup (1986–87) and the UEFA Cup (1980–81).  The last of these was won with Ipswich Town, while the other titles were won while playing for Ajax.  He is also one of the two Dutch players, together with Danny Blind, to have won all UEFA club competitions and the Intercontinental Cup.

Beşiktaş J.K. in European football: Beşiktaş J.K.,is a professional football club based in Beşiktaş, Istanbul.  After winning the 1957–58 Federation Cup, a tournament that was held to designate the Turkey's representative in the European Cup, the club first participated in a European competition in 1958.  Since then, Beşiktaş J.K. regularly participated in European tournaments.  The club managed to reach the quarter-finals of 1986–87 European Cup, 2002–03 UEFA Cup and 2016–17 UEFA Europa League.

1987 European Cup Winners' Cup Final: The 1987 European Cup Winners' Cup Final was a football match contested between Ajax of Netherlands and Lokomotive Leipzig of East Germany.  It was the final match of the 1986–87 European Cup Winners' Cup and the 27th European Cup Winners' Cup Final.  The final was held at Olympic Stadium in Athens, Greece.  Ajax won the match 1–0 with a 20th-minute header from Marco van Basten.

1973 European Cup Final: The 1973 European Cup Final was a football match held at the Red Star Stadium, Belgrade, on 30 May 1973, in which Ajax of the Netherlands defeated Juventus of Italy 1–0.  A goal from Johnny Rep four minutes into the match was enough for Ajax to claim their third consecutive European Cup.  This victory meant that Ajax had earned the privilege of keeping the trophy permanently.  Juventus, however, got revenge 23 years later beating Ajax in the 1996 final in Rome.

1994–95 AFC Ajax season: During the 1994–95 Dutch football season, AFC Ajax competed in the Eredivisie.  Ajax won a league-cup double.  They won their 25th Dutch title in style, not losing a single match all season and scoring 106 goals.  Ajax also won their fourth European Cup, defeating A.C. Milan 1-0 in the final.  This Ajax squad is considered to be one of the best teams in football history.

1973 European Super Cup: The 1973 European Super Cup was played between 1972–73 European Cup winners Ajax and 1972–73 European Cup Winners' Cup winners Milan, with Ajax winning 6–1 on aggregate, making it the worst defeat for an Italian team in an UEFA competition final.  Unlike future Super Cup matches, the 1973 edition took place at the start of the following calendar year rather than the start of the following season.

AFC Ajax in European football: AFC Ajax is one of the most successful football clubs in Europe.  There are only three clubs in the history of the game to have won the European Cup/Champions League titles (won four times by Ajax) three times consecutively.  Only Real Madrid and Bayern Munich have achieved this feat aside from Ajax.  Furthermore, Ajax have won the UEFA Cup Winners' Cup once, the UEFA Cup once, the UEFA Super Cup three times, the Intercontinental Cup twice and the International Football Cup once.  The club has also appeared in three additional finals finishing as runners-up.  In the 1979–80 season, Ajax player Søren Lerby was top scorer of the European Cup with 10 goals.  Below is a list of all official European matches contested by Ajax.

Question: Which Ajax player that competed in the 1986-87 European Cup later became the assistant manager for Ajax? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The name of the Ajax player."
    },
    "role_in_1986_87_season": {
      "type": "string",
      "description": "The player's role during the 1986-87 European Cup Winners' Cup season."
    },
    "later_role_at_ajax": {
      "type": "string",
      "description": "The player's later role at Ajax."
    },
    "competition_season": {
      "type": "string",
      "description": "The season and competition the player participated in with Ajax."
    }
  },
  "required": [
    "player_name",
    "role_in_1986_87_season",
    "later_role_at_ajax",
    "competition_season"
  ],
  "additionalProperties": false
}
