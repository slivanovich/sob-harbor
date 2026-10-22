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
Clijsters–Henin rivalry: Justine Henin and Kim Clijsters are Belgian professional tennis players who engaged in a long-standing rivalry which spanned twenty-five meetings over a twelve-year period, with eight taking place in a Grand Slam tournament.  Their final competitive meeting came at the 2010 Wimbledon Championships in the fourth round, with Clijsters winning in 3 sets, this brought their head to head record to 13–12 in Clijsters' favour.  The Belgians have met eight times in Grand Slam tournaments, three of which were finals.  Henin leads 5–3 in Grand Slam play including winning all their final match-ups.

2003 WTA Tour Championships: The 2003 WTA Tour Championships, also known by its sponsored name Bank of America WTA Tour Championships Presented by Porsche, was a women's tennis tournament played on indoor hard courts at the Staples Center in Los Angeles, United States.  It was the 33rd edition of the year-end singles championships, the 28th edition of the year-end doubles championships, and was part of the 2003 WTA Tour.  The tournament was held between November 4 and November 10, 2003.  First-seeded Kim Clijsters won the singles event and earned $1,000,030 first-prize money as well as 485 ranking points.  With her victory Clijsters became the first female tennis player to earn $US4 million in a season.  For the first time since 1978 a round robin system was used, after the men's Tennis Masters Cup.  Two groups of four players were formed and each contender had to play three matches.  Also, for singles, instead of the top sixteen players qualifying, only top eight qualified for the WTA Tour Championships.  For doubles, the top four pairs (previously top eight) pairs qualified for the WTA Tour Championships, but still continued with the single elimination format.

1999 French Open – Girls' Doubles: Kim Clijsters and Jelena Dokić were the defending champions, but only Clijsters competed with year with Mia Buric

2016 French Open – Women's Legends Doubles: Kim Clijsters and Martina Navratilova were the defending champions, but decided not to compete together this year.  Clijsters played alongside Tracy Austin-Holt, but they were eliminated at the round-robin stage.

2010 Billie Jean King Cup: The 2010 Billie Jean King Cup was the 2nd edition of this tennis exhibition tournament.  Seven-time Grand Slam champion Venus Williams, 2009 French Open Champion Svetlana Kuznetsova, and 2009 US Open Champion Kim Clijsters participated.  2009 Australian Open and Wimbledon Champion Serena Williams had to withdraw from the event due to a leg injury.  She was replaced by 2008 French Open Champion Ana Ivanovic.  In the first semifinal, Clijsters defeated Ivanovic in a tiebreaker (7–2), despite Ivanovic having match point at 5–4 up.  Williams defeated Kuznetsova in the second semifinal, 6–4.  Williams defeated Clijsters in the championship match by a score of 6–4 3–6 7–5.

Eva Dyrberg: Eva Dyrberg (born 17 February 1980) is a Danish former tennis player.  As a junior player, she won 1998 Wimbledon Championships with Jelena Kostanić and 1998 US Open with Kim Clijsters.  In 1998, Dyrberg was also ranked World No. 1 in junior doubles and was named ITF Junior Girls Doubles World Champion.  During her professional career, she won four singles and five doubles events organized by the International Tennis Federation, defeating players such as Magdalena Maleeva, Tathiana Garbin, Maria Elena Camerin, Nicole Pratt, and reaching one doubles final at WTA Tour, at Sanex Trophy in 2000.  She retired from professional tennis after the 2003 Australian Open.

2004 Wimbledon Championships – Women's Doubles: Kim Clijsters and Ai Sugiyama were the defending champions.  however Clijsters did not compete in the tournament this year.  Sugiyama played alongside Liezel Huber and they reached the final where they were defeated by Cara Black and Rennae Stubbs, 6–3, 7–6.

Kim Clijsters: Kim Antonie Lode Clijsters (] ; born 8 June 1983) is a Belgian former professional tennis player.  Clijsters is a former world No. 1 in both singles and doubles.

Mary Pierce: Mary Pierce (born 15 January 1975) is a French retired tennis professional who played on the Women's Tennis Association (WTA) tour.  Born in Canada, she is a citizen of Canada, and the United States.  Pierce played for France in team competitions and in the Olympics.

2004 French Open – Women's Doubles: Kim Clijsters and Ai Sugiyama were the defending champions, but Clijsters was chose not to participate.  Sugiyama played alongside Liezel Huber, but they lost in the first round to Shinobu Asagoe and Rika Fujiwara in the first round.

Question: Between two tennis players Kim Clijsters and Mary Pierce, who is older?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "players_involved": {
      "type": "array",
      "description": "Details of the tennis players involved in the comparison.",
      "items": {
        "type": "object",
        "properties": {
          "player_name": {
            "type": "string",
            "description": "The full name of the tennis player."
          },
          "birth_year": {
            "type": "integer",
            "description": "The birth year of the player."
          }
        },
        "required": [
          "player_name",
          "birth_year"
        ],
        "additionalProperties": false
      }
    },
    "older_player_name": {
      "type": "string",
      "description": "The name of the player who is older."
    },
    "younger_player_name": {
      "type": "string",
      "description": "The name of the player who is younger."
    },
    "age_difference_years": {
      "type": "integer",
      "description": "The difference in birth years between the two players."
    }
  },
  "required": [
    "players_involved",
    "older_player_name",
    "younger_player_name",
    "age_difference_years"
  ],
  "additionalProperties": false
}
