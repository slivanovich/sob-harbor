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
2016–17 Southampton F.C. season: The 2016–17 Southampton F.C. season was the club's 18th season in the Premier League and their 40th in the top division of English football.  In addition to the 2016–17 Premier League, the club also competed in the FA Cup, EFL Cup and UEFA Europa League.  The season was the club's only campaign with manager Claude Puel, who took over from Ronald Koeman on 30 June 2016.  The club finished eighth in the Premier League table, having won twelve, drawn ten and lost sixteen of their 38 matches played.  They were knocked out of the UEFA Europa League at the group stage, having won two, drawn two and lost two of their matches, and the FA Cup in the fourth round, while they finished as runners-up in the EFL Cup Final losing 3–2 to Manchester United.

Southampton Saints Girls &amp; Ladies F.C.: Southampton Saints Girls and Ladies Football Club is an English women's football club formerly affiliated with Southampton F.C..  They play in the FA Women's Premier League South West Division One .

Ronald Koeman: Ronald Koeman (] ; born 21 March 1963) is a former Dutch footballer and the current manager of English club Everton.  He is the younger brother of former Feyenoord coach Erwin Koeman and the son of former Dutch international Martin Koeman.  A composed player on the ball, Koeman was capable of being deployed both as a defender and as a midfielder, and he frequently played as a sweeper, due to his vision and his ability on the ball.  Regarded as one of the best and most prolific attacking central defenders of all time, Koeman was renowned for his long-range passing, as well as his shooting accuracy and power from distance, especially on free kicks, and is the top scoring defender in world football; he was also an accurate penalty kick taker.

Mauricio Pochettino: Mauricio Roberto Pochettino (] , ] ; born 2 March 1972) is an Argentine former footballer who played as a central defender, and is the current manager of Premier League club Tottenham Hotspur.

Richard Bakary: Richard Bakary (born 17 October 1997 in Porto-Novo, Benin) is a footballer who currently plays as a defender for Southampton F.C..

Freemantle F.C.: Freemantle Football Club were a football club based in the Freemantle area of Southampton, England who were active at the end of the nineteenth century.  During their brief heyday, they were rivals to Southampton F.C..  The club spent two seasons in the lower divisions of the Southern League.

Northam, Southampton: Northam is a suburb of Southampton in Hampshire.  On the West bank of the River Itchen, it shares borders with St Mary's, Bitterne and Bevois Valley.  Beside the border with St Mary's is the Chapel area, which has been home to some recent apartment building developments in Northam.  The A3024 road runs through the suburb and crosses the Northam Bridge, which links Northam with Bitterne via Bitterne Manor.  Although St Mary's Stadium takes its name from the neighbouring St Mary's, the stadium itself is in Northam, and home to Southampton F.C..

2011–12 Feyenoord season: The 2011–12 season was Feyenoord's 104th season of play, it was their 56th season in the Eredivisie and its 90th consecutive season in the highest Dutch football division.  They ended their league campaign in second place, after winning ten of the last eleven games of the season.  They reached the third round of the KNVB Cup.  It was the first season with Ronald Koeman, who signed as manager of Feyenoord after former manager Mario Been resigned on 13 July 2011 due to a lack of trust from the squad.

2010 Football League Trophy Final: The 2010 Football League Trophy Final was the 27th final of the domestic football cup competition for teams from Football Leagues One and Two, the Football League Trophy.  The final was played at Wembley Stadium in London on 28 March 2010.  The match was contested between Carlisle United and Southampton.  Southampton won the match 4–1 to give them their first silverware since winning the 1976 FA Cup.  The attendance may not be as high as it could have been because Carlisle did not require the maximum amount of seats, whereas Southampton F.C would have been able to sell more than their amount given, and this had angered the fans as Wembley Stadium would have some parts empty, and they could have been used by Southampton fans.

2014–15 Southampton F.C. season: The 2014–15 Southampton F.C. season was the club's 16th season in the Premier League and their 38th in the top division of English football.  It was also the club's first season with Dutch manager Ronald Koeman, who replaced Mauricio Pochettino on 16 June 2014.  Southampton finished seventh in the Premier League, having won 18, drawn six and lost 14 matches.  The club also made it to the fourth round of the FA Cup and the fifth round of the League Cup.

Question: In 2014, Ronald Koeman replaced what former footballer from Argentina as manager of Southampton F.C.?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "replaced_manager_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "nationality": {
          "type": "string"
        },
        "former_profession": {
          "type": "string"
        }
      },
      "required": [
        "name",
        "nationality",
        "former_profession"
      ],
      "additionalProperties": false
    },
    "replacing_manager_name": {
      "type": "string"
    },
    "year_of_replacement": {
      "type": "integer"
    },
    "club_involved": {
      "type": "string"
    }
  },
  "required": [
    "replaced_manager_details",
    "replacing_manager_name",
    "year_of_replacement",
    "club_involved"
  ],
  "additionalProperties": false
}
