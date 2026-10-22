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
2008 UEFA Champions League Final: The 2008 UEFA Champions League Final was a football match that took place on Wednesday, 21 May 2008, at the Luzhniki Stadium in Moscow, Russia, to determine the winner of the 2007–08 UEFA Champions League.  It was contested by Manchester United and Chelsea, making it an all-English club final for the first time in the history of the competition.  This was only the third time that two clubs from the same country had contested the final; the others being the 2000 and 2003 finals.  It was the first European Cup final played in Russia, and hence the easternmost final in the tournament's history.  It also marked the 100th anniversary of Manchester United's first league triumph, the 50th anniversary of the Munich air disaster, and the 40th anniversary of United's first European Cup triumph in 1968.  It was Manchester United's third European Cup final after 1968 and 1999, while it was Chelsea's first.

2012 UEFA Champions League Final: The 2012 UEFA Champions League Final was a football match which took place on Saturday, 19 May 2012 between Bayern Munich of Germany and Chelsea of England at the Allianz Arena in Munich, Germany.  The match was to decide the winner of the 2011–12 season of the UEFA Champions League, Europe's premier club football tournament.  Bayern were making their ninth appearance in the competition's final, having won four and lost four, most recently losing in 2010.  Chelsea were appearing in their second final, having lost their first in 2008.

2000–01 UEFA Champions League: The 2000–01 UEFA Champions League was the 46th season of the UEFA Champions League, UEFA's premier European club football tournament, and the ninth since it was rebranded from the "European Champion Clubs' Cup" or "European Cup".  The competition was won by Bayern Munich (first title since 1976), who beat Valencia 5–4 on penalties after a 1–1 draw after extra time.  It was their first UEFA Champions League title, and their fourth European Cup title overall, it was Valencia's second consecutive final defeat, losing to Real Madrid in the previous season.  The knockout phase saw Bayern eliminate the preceding two Champions League winners, Manchester United and Real Madrid, winning all four games in the process.  Valencia, meanwhile, defeated English sides Arsenal and Leeds United in the knockout phase en route to the final.

2001 UEFA Champions League Final: The 2001 UEFA Champions League Final was a football match that took place at San Siro in Milan, Italy, on 23 May 2001, to decide the winner of the 2000–01 UEFA Champions League.  The match pitted Bayern Munich against Valencia.  The match finished in a 1–1 draw, but Bayern clinched their fourth title by winning 5–4 on penalties.  This was also their first European Cup title in a quarter-century, also representing Valencia's second consecutive final defeat (2000 and 2001).  Due to all the goals scored by penalties and the penalty shootout needed to decide the winner, this UEFA Champions League match became an "all-penalty" final and the only one ever to happen to this day.  The 2001 final saw the two previous seasons' losing finalists clash, Bayern Munich lost to Manchester United in the 1999 final and Valencia lost to Real Madrid in the 2000 final.

1957 European Cup Final: The 1957 European Cup Final was a football match which took place at the Santiago Bernabéu Stadium in Madrid, Spain, on 30 May 1957.  It was contested between Real Madrid of Spain and Fiorentina of Italy.  Real Madrid won 2–0 after goals from Alfredo Di Stéfano and Francisco Gento in the second half.  It was the first of four finals (also counting the Champions League era, followed by the 1965, 1984 and 2012 finals) where one of the teams played in its home stadium, and also the first final where the winning team played at their home stadium.

1961 European Cup Winners' Cup Final: The 1961 European Cup Winners' Cup Final was a football match contested between Fiorentina of Italy and Rangers of Scotland.  It was the final of the 1960–61 European Cup Winners' Cup the first UEFA Cup Winners' Cup final.  It was the only time that the final was played over two legs.  The first leg was played at Ibrox Stadium, Glasgow and the second leg at the Stadio Comunale in Florence.  It was Rangers first European final and in doing so became the first British team to reach the final of a European football competition.  It was Fiorentina's second European final having previously reached the 1957 European Cup final.

2003 UEFA Champions League Final: The 2003 UEFA Champions League Final was a football match that took place at Old Trafford in Manchester, England on 28 May 2003 to decide the winner of the 2002–03 UEFA Champions League.  The match was contested by two Italian teams: Juventus and Milan.  The match made history as it was the first time two clubs from Italy had faced each other in the final.  It was also the second intra-national final of the competition, following the all-Spanish 2000 UEFA Champions League Final three years earlier.  Milan won the match via a penalty shoot-out after the game had finished 0–0 after extra time.  It gave Milan their sixth success in the European Cup.

2017 UEFA Champions League Final: The 2017 UEFA Champions League Final was the final match of the 2016–17 UEFA Champions League, the 62nd season of Europe's premier club football tournament organised by UEFA, and the 25th season since it was renamed from the European Champion Clubs' Cup to the UEFA Champions League.  It was played at the Millennium Stadium in Cardiff, Wales on 3 June 2017, between Italian side Juventus and Spanish side and title holders Real Madrid, in a repeat of the 1998 final.  Real Madrid won the match 4–1 to secure their 12th title in this competition.  With this victory, as the defending champions, Real Madrid became the first ever team to successfully defend their title in the Champions League era, and the first to do so since Milan in 1990.  On the other hand, Juventus lost a fifth final in a row and a seventh in nine finals reached.

2003 UEFA Super Cup: The 2003 UEFA Super Cup was played on 29 August 2003 between Milan of Italy and Porto of Portugal.  Milan qualified by beating Juventus in the 2003 UEFA Champions League Final.  Porto had made it to the Super Cup after beating Celtic in the 2003 UEFA Cup Final.  Milan won the match 1–0.  After the match, defeated Porto manager José Mourinho said "We leave here convinced we can go into the UEFA Champions League with the hope and certainty we can compete with any team".  They finished the season as UEFA Champions League winner.

1987 European Cup Final: The 1987 European Cup Final was a football match held at the Prater Stadium, Vienna, on 27 May 1987, that saw Porto of Portugal defeat Bayern Munich of West Germany 2–1.  Both sides were missing key players: the Portuguese were without their injured striker Fernando Gomes, while the Germans were missing their sweeper, and captain, Klaus Augenthaler, who was suspended, along with striker Roland Wohlfarth and midfield player Hans Dorfner, who were both injured.  The Portuguese side fought back from 1–0 down to win their first European Cup, with the goals coming from a back heel by Rabah Madjer and a volley from Juary, after a Ludwig Kögl header had given Bayern the lead in the first half.  The final was the first European Cup final that Bayern, and their captain Lothar Matthäus would lose to successive late goals, repeated 12 years later in the 1999 UEFA Champions League Final against Manchester United.

Question: What was unusual about the venue of the 1957 European Cup Final and 2012 UEFA Champions League Final?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "unusual_venue_characteristic": {
      "type": "string",
      "description": "The unusual characteristic shared by the venues of the specified finals."
    },
    "finals_with_characteristic": {
      "type": "array",
      "description": "Details of the finals that exhibited this unusual venue characteristic.",
      "items": {
        "type": "object",
        "properties": {
          "year": {
            "type": "integer",
            "description": "The year the final took place."
          },
          "stadium": {
            "type": "string",
            "description": "The name of the stadium where the final was held."
          },
          "city": {
            "type": "string",
            "description": "The city where the stadium is located."
          },
          "home_team": {
            "type": "string",
            "description": "The team that played in its home stadium."
          }
        },
        "required": [
          "year",
          "stadium",
          "city",
          "home_team"
        ],
        "additionalProperties": false
      }
    },
    "number_of_finals_with_characteristic": {
      "type": "integer",
      "description": "The total count of finals mentioned in the context with this characteristic."
    }
  },
  "required": [
    "unusual_venue_characteristic",
    "finals_with_characteristic",
    "number_of_finals_with_characteristic"
  ],
  "additionalProperties": false
}
