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
2017–18 ACF Fiorentina season: The 2017–18 season is the 91st season in ACF Fiorentina's history and their 80th in the top-flight of Italian football.  Fiorentina are competing in Serie A and the Coppa Italia, missing out on European football for the first time since the 2012–13 season following an eighth-place finish in the 2016–17 season.

2015–16 ACF Fiorentina season: The 2015–16 season was the 89th season in ACF Fiorentina's history and their 78th in the top-flight of Italian football.  Fiorentina finished the season in 5th place in Serie A, having topped the table early in the season.  In the Coppa Italia, the club was eliminated in the round of 16, losing at home to newly promoted Carpi 1–0.  Competing in the UEFA Europa League for the third season in a row, Fiorentina limped into second place in their group with a 3–1–2 record, and were eliminated in the Round of 32 by Tottenham Hotspur, 4–1 on aggregate.  The 2015–16 season was also notable for being the first season since the 2011–12 season in which the club was not managed by Vincenzo Montella, who had achieved 4th-place finishes in each of his seasons with the club.  Montella was replaced by Basel coach Paulo Sousa.

1994–95 A.C. Fiorentina season: Associazione Calcio Fiorentina returned to Serie A, following the 1993 relegation, and immediately established itself as a mid-table side once again.  Portuguese playmaker Rui Costa and Brazilian World Champion defender Márcio Santos were the two main signings in the summer, and both of them were key players for the team.  Rui Costa also established the special partnership with star striker Gabriel Batistuta that was going to be the key ingredient for the coming five years in Fiorentina's ascent towards the top of Italian football.  Batistuta became league topscorer with 26 goals, many of them provided by Rui Costa's passes.

2004–05 ACF Fiorentina season: ACF Fiorentina returned to Serie A, following a two-year absence after the bankruptcy of the previous incarnation of the club.  Fiorentina returned only due to the expansion in terms of the number of top-league teams, and therefore had to significantly strengthen the squad in pre-season.  Dario Dainelli, Giorgio Chiellini, Hidetoshi Nakata, Fabrizio Miccoli, Martin Jørgensen, goalkeeper Cristiano Lupatelli, Enzo Maresca, Tomáš Ujfaluši and Javier Portillo were among the highly rated players to sign up for Fiorentina, either permanently or on loan.  With this squad, Fiorentina was expected to challenge for a place on the top half of the table, but slipped into the relegation battle that affected more than half of the Serie A clubs during the dramatic season.  In the end, a strong finish to the season under incoming coach Dino Zoff saved "La Viola" from relegation, with an emotional 3–0 victory against Brescia confirming their survival.

2005–06 ACF Fiorentina season: The 2005–06 season was ACF Fiorentina's 80th season in its history and its 68th season in Serie A.  The club had its best season on the pitch since the 1998–99 season, originally finishing 4th with 74 points and securing a spot in the qualifying round of the 2006–07 UEFA Champions League.  However, the club was punished with a 30-point penalty for its involvement in the 2006 Italian football scandal, resulting in Fiorentina being pushed down the table to 9th.  This was a much better outcome than its original punishment, as "La Viola" were originally relegated to Serie B.  Following a successful appeal, Fiorentina was admitted to play in Serie A the following season, albeit losing its Champions League slot and having to start the season with a 15-point penalty, removing any chance of mounting a genuine title challenge and building on the success of the 2005–06 season.

2011–12 ACF Fiorentina season: The 2011–12 season was the 85th season in ACF Fiorentina's history and the club's 74th season in the top-flight of Italian football.  Fiorentina competed in Serie A, finishing a disappointing 13th, and was eliminated in the round of 16 in the Coppa Italia.

Javier Portillo: Javier García Portillo (born 30 March 1982 in Aranjuez, Community of Madrid) is a Spanish retired footballer who played as a forward.

ACF Fiorentina: ACF Fiorentina S.p.A., commonly referred to as simply Fiorentina ] , is a professional Italian football club from Florence, Tuscany.  Founded by a merger in 1926, and refounded in 2002 following bankruptcy, Fiorentina have played at the top level of Italian football for the majority of their existence; only four clubs have played in more Serie A seasons.

Fiorentina Women's F.C.: S.s.d. a r.l. Fiorentina Women's F.C. is an Italian women's football club from Florence, which is the women's section of ACF Fiorentina.  It was founded in 2015 after ACF Fiorentina bought out A.C.F. Firenze, an independent club who had participated in Serie A until 2014–15.

Sandro Mencucci: Sandro Mencucci (Italian: [sandro meŋkuttʃi]; born 18 July 1961) is an Italian businessman and Executive Director Sports Area and Board Director of the Italian Serie A football club ACF Fiorentina based in Florence, Italy.  In 2007, Mencucci became the President of the Promesse Viola Srl, the official youth academy for the club.  In 2014, Mencucci, became the President of International Development Players LLC, a youth development academy under the guidance of the youth sector division of the club with its headquarters in the United States of America.  In 2015, Mencucci became President of the Fiorentina Women's Football Club, the first ever professionally-affiliated women's football club in the history of Italy.  In 2017, Fiorentina Women's Football Club won the 2016-2017 Italian Championship in only two years from its upstart.  This is the first Tricolore for ACF Fiorentina since May 6, 1969 and it is the first Serie A championship won by the ACF Fiorentina's current owner Andre Delle Valle.  The Fiorentina Women's FC qualified to participate in the UEFA Champion's League in the 2017-2018 season although they will have a UEFA ranking of 0.  On June 17, 2017, the club ACF Fiorentina won its first doublet since 1926 when the Fiorentina Women's FC won the Coppa Italia.

Question: ACF Fiorentina returned to Serie A, following of how long of an absence, after the bankruptcy of the previous incarnation of the club, Javier García Portillo, a Spanish retired footballer who played as a forward, were among the highly rated players to sign up for Fiorentina, either permanently or on loan?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "season_of_return_to_serie_a": {
      "type": "string",
      "description": "The season when ACF Fiorentina returned to Serie A."
    },
    "absence_duration_years": {
      "type": "integer",
      "description": "The duration of ACF Fiorentina's absence from Serie A in years."
    },
    "reason_for_absence": {
      "type": "string",
      "description": "The reason for ACF Fiorentina's absence from Serie A."
    },
    "javier_portillo_signed": {
      "type": "boolean",
      "description": "Indicates whether Javier Portillo was among the highly rated players to sign up for Fiorentina during that period."
    }
  },
  "required": [
    "season_of_return_to_serie_a",
    "absence_duration_years",
    "reason_for_absence",
    "javier_portillo_signed"
  ],
  "additionalProperties": false
}
