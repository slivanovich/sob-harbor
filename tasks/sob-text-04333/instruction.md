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
Helenio Herrera: Helenio Herrera Gavilán (] ; 10 April 1910 – 9 November 1997) was an Argentine, naturalized French, football player and manager.  He is best remembered for his tremendous success with the Inter Milan team known as "Grande Inter" in the 1960s.

2009–10 FC Barcelona season: In 2009–10, Futbol Club Barcelona started the new season with the prospect of winning six major competitions in the 2009–2010 season.  They contested for the Supercopa de España, UEFA Super Cup, FIFA Club World Cup, Copa del Rey, La Liga, and the UEFA Champions League.  During the summer transfer window, the club swapped their top league goal scorer during the treble season, Samuel Eto'o to Italy's Inter Milan in exchange for Zlatan Ibrahimović, along with €48 million, bringing the total to €69 million.

List of Inter Milan players: Inter Milan is an Italian association football club based in Milan, Lombardy.  The club was formed on 9 March 1908 to allow the foreign playes to play in Italy.  Inter played its first competitive match on 10 January 1910 against their cross-town rivals Milan, in which they lost 3–2.  The club won its very first title in 1910 – the 1909–10 Italian Football Championship.  Since then, the club has won further 17 league titles, along with seven Coppa Italia and five Supercoppa Italiana.  They have also been crowned champions of Europe on three occasions by winning two European Cups back-to-back in 1964 and 1965 and then another in 2010.  The club experienced the most successful period in their history from 2006 to 2010, in which it won five successive league titles, equaling the all-time record at that time, by adding three Italian Cups, three Italian Supercups, one UEFA Champions League and one FIFA Club World Cup.  During the 2009–10, Inter become the first and only Italian team to win the Treble and the second team to win five trophies in a calendar year.

Ricardo Quaresma: Ricardo Andrade Quaresma Bernardo (] ; born 26 September 1983) is a Portuguese professional footballer who plays as a winger for Turkish club Beşiktaş and the Portugal national team.

2006–07 Inter Milan season: The relegation of Juventus to Serie B due to Calciopoli, and Milan and Fiorentina's penalisations, made Inter a clear favourite for the title: the side was empowered with the arrivals of Zlatan Ibrahimović, Patrick Vieira, Fabio Grosso and Maicon.  In early September, the club suffered a tragedy: Inter's president Giacinto Facchetti died at the age of 64, due to a cancer.

2008–09 Inter Milan season: After Roberto Mancini's departure, José Mourinho became the new coach of Inter.  The Portuguese manager won a trophy at his debut, Supercoppa Italiana, defeating Roma on penalties.  He planned a 4–3–3 formation, with the new arrivals Amantino Mancini and Quaresma as wingers beside Zlatan Ibrahimović.

Becoming Zlatan: Becoming Zlatan (Swedish: "Den unge Zlatan" ) is a 2016 Swedish independent coming-of age sports documentary about Swedish International association football player Zlatan Ibrahimović.  The film was directed by brothers Fredrik and Magnus Gertten and follows Ibrahimović through his formative years with football clubs Malmö FF and AFC Ajax all the way to his break through with Juventus F.C. in 2005.

Trofeo Pirelli: The Pirelli Cup is an annual friendly football tournament sponsored by the Pirelli Tyre company.  The competition was started in 1996 as a single 90-minute friendly match between Pirelli-sponsored Inter Milan and another invited team.  Since 1996, 14 editions of the one-match tournament have been held.  The latest edition of the competition was held in 2010 in Baltimore, featuring Inter Milan and Manchester City.  The match ended 3-0 as Inter won the trophy.

List of Inter Milan managers: Inter Milan is an Italian association football club based in Milan, Lombardy.  The club was formed on 9 March 1908 to allow the foreign playes to play in Italy.  Inter played its first competitive match on 10 January 1910 against their cross-town rivals Milan, in which they lost 3–2.  The club won its very first title in 1910 – the 1909–10 Italian Football Championship.  Since then, the club has won further 17 league titles, along with seven Coppa Italia and five Supercoppa Italiana.  They have also been crowned champions of Europe on three occasions by winning two European Cups back-to-back in 1964 and 1965 and then another in 2010.  The club experienced the most successful period in their history from 2006 to 2010, in which it won five successive league titles, equaling the all-time record at that time, by adding three Italian Cups, three Italian Supercups, one UEFA Champions League and one FIFA Club World Cup.  During the 2009–10, Inter become the first and only Italian team to win the Treble and the second team to win five trophies in a calendar year.

Luis Suárez (footballer, born 1935): Luis Suárez Miramontes (] ; born 2 May 1935), also known by the diminutive Luisito, is a Spanish former footballer and manager.  He played as a midfielder for Deportivo de La Coruña, CD España Industrial, FC Barcelona, Inter Milan, Sampdoria and Spain.  Suárez is regarded as one of Spain's greatest players; he was noted for his elegant, fluid, graceful style of play.  Nicknamed "El Arquitecto" (The Architect) he was noted for his perceptive passing and explosive shot and in 1960 he became the only Spanish-born player to be voted Ballon d'Or.  In 1964 he helped Spain win the European Championship.  Suarez originally achieved prominence as a creative inside forward or attacking midfielder for the great Barcelona team of the 1950s before he joined Inter Milan where he reached his prime as deep lying playmaker for the legendary "Grande Inter" team of the 1960s.  He played a pivotal role in the success Herrera's Inter Milan side, and was one of the primary creative forces in the squad, due to his ball skills, vision, and passing range.  He retired as a player in 1973, after three seasons at Sampdoria.

Question: Which Portuguese winger played beside  Zlatan Ibrahimović in the 2008-09 Inter Milan team ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The name of the Portuguese winger."
    },
    "player_nationality": {
      "type": "string",
      "description": "The nationality of the player."
    },
    "player_position": {
      "type": "string",
      "description": "The primary playing position of the player."
    },
    "team_name": {
      "type": "string",
      "description": "The name of the football club."
    },
    "season": {
      "type": "string",
      "description": "The football season in question."
    },
    "played_alongside_player": {
      "type": "string",
      "description": "The name of the player the winger played beside."
    }
  },
  "required": [
    "player_name",
    "player_nationality",
    "player_position",
    "team_name",
    "season",
    "played_alongside_player"
  ],
  "additionalProperties": false
}
