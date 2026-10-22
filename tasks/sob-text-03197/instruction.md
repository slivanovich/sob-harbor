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
2015–16 Borussia Dortmund season: The 2015–16 Borussia Dortmund season is the 105th season (and 106th overall year) in the football club's history and 40th consecutive and 49th overall season in the top flight of German football, the Bundesliga, having been promoted from the 2.  Bundesliga in 1976.  In addition to the domestic league, Borussia Dortmund will also participate in this season's editions of the domestic cup, the DFB-Pokal, and the second-tier continental cup, the UEFA Europa League.  This will be the 43rd season for the club in the Westfalenstadion, located in Dortmund, Germany.  The stadium has a capacity of 81,359 for Bundesliga matches, and a capacity of 65,851 for continental matches.  The season covers a period from 1 July 2015 to 30 June 2016.

2002 UEFA Cup Final: The 2002 UEFA Cup Final was a football match played on 8 May 2002, between Feyenoord of the Netherlands and Borussia Dortmund of Germany.  Feyenoord won the match 3–2.  It was the 31st UEFA Cup Final and was held in the Feijenoord Stadion in Rotterdam, which is the home ground of Feyenoord.  This was the first time since the introduction of single–match finals in the UEFA Cup in 1998, that the final had been played at a finalists home ground.  Previous to this match, Feyenoord had not won a European trophy since 1974, when they beat Tottenham Hotspur to win the UEFA Cup.  Borussia Dortmund, who had already won the Bundesliga title, were hoping to join Ajax, Bayern Munich and Juventus in being the only clubs to win all three European trophies.  Feyenoord's victory marked the first European triumph for a Dutch club in seven years, after Ajax won the Champions League in 1995.

2016–17 Borussia Dortmund season: The 2016–17 Borussia Dortmund season is the 106th season (and 107th overall year) in the football club's history and 41st consecutive and 50th overall season in the top flight of German football, the Bundesliga, having been promoted from the 2.  Bundesliga in 1976.  In addition to the domestic league, Borussia Dortmund will also participate in this season's editions of the domestic cup, the DFB-Pokal, and the first-tier continental cup, the UEFA Champions League.  This will be the 44th season for the club in the Westfalenstadion, located in Dortmund, Germany.  The stadium has a capacity of 81,360 for Bundesliga matches, and a capacity of 65,851 for continental matches.  The season covers a period from 1 July 2016 to 30 June 2017.

2017–18 Borussia Dortmund season: The 2017–18 Borussia Dortmund season is the 109th season in the football club's history and 42nd consecutive and 51st overall season in the top flight of German football, the Bundesliga, having been promoted from the 2.  Bundesliga Nord in 1976.  In addition to the domestic league, Borussia Dortmund also are participating in this season's editions of the domestic cup, the DFB-Pokal, and the first-tier continental cup, the UEFA Champions League.  Dortmund are the reigning DFB-Pokal champions, and therefore also are participating in the German super cup, the DFL-Supercup.  This is the 44th season for Dortmund in the Westfalenstadion, located in Dortmund, North Rhine-Westphalia, Germany.  The season covers a period from 1 July 2017 to 30 June 2018.

Borussia Dortmund in European football: Ballspielverein Borussia 09 e.V. Dortmund, commonly known as Borussia Dortmund ] , BVB, or simply Dortmund, is a German sports club based in Dortmund, North Rhine-Westphalia ("Borussia" is the Latin equivalent of Prussia).

1996–97 Juventus F.C. season: Juventus Football Club won the domestic title and a second consecutive Champions League final, where Karl-Heinz Riedle scored twice for Borussia Dortmund in a 3–1 defeat of Juventus.

Borussia Dortmund: Ballspielverein Borussia 09 e.V. Dortmund, commonly known as Borussia Dortmund ] , BVB, or simply Dortmund, is a German sports club based in Dortmund, North Rhine-Westphalia ("Borussia" is the Latin equivalent of Prussia).  The football team is part of a large membership-based sports club with more than 145,000 members, making BVB the second largest sports club by membership in Germany.  Dortmund plays in the Bundesliga, the top tier of the German football league system.  Dortmund is one of the most successful clubs in German football history.

1993 UEFA Cup Final: The 1993 UEFA Cup Final was played on 5 May 1993 and 19 May 1993 between Juventus of Italy and Borussia Dortmund of Germany.  Juventus won 3–1 and 3–0 to record a 6–1 aggregate victory, a record aggregate score for a UEFA Cup Final.  The fixture would be repeated in the 1997 Champions League Final, when the result would be reversed, with Dortmund running out victors.  By then, three of Juventus' team (Kohler, Möller and Júlio César) had joined Dortmund.

Sándor Puhl: Sándor Puhl (born 14 July 1955) is a retired Hungarian football referee.  He is mostly known for supervising four matches in the 1994 FIFA World Cup in the United States, including the final between Brazil and Italy.  He also refereed UEFA Champions League matches, including the 1997 UEFA Champions League Final between Borussia Dortmund and Juventus.  Dortmund ended up being 3-1 winners.

1997 UEFA Champions League Final: The 1997 UEFA Champions League Final was a football match played at the Olympiastadion in Munich on 28 May 1997 to determine the winner of the 1996–97 UEFA Champions League.  The match was contested by Borussia Dortmund of Germany and Juventus of Italy.  Borussia Dortmund won 3–1 with goals from Karl-Heinz Riedle and Lars Ricken; Juventus' goal was scored by Alessandro Del Piero.

Question:  Juventus Football Club won the domestic title and a second consecutive Champions League final, where Karl-Heinz Riedle scored twice for Borussia Dortmund, a German sports club based where?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "club_name": {
      "type": "string",
      "description": "The name of the football club."
    },
    "club_location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the club is based."
        },
        "state": {
          "type": "string",
          "description": "The state or region where the club is based."
        }
      },
      "required": [
        "city",
        "state"
      ],
      "additionalProperties": false
    },
    "country": {
      "type": "string",
      "description": "The country where the club is based."
    }
  },
  "required": [
    "club_name",
    "club_location",
    "country"
  ],
  "additionalProperties": false
}
