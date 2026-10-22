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
SC Bastia Reserves and Academy: The SC Bastia Reserves and Academy are the reserve team and academy of French football club Bastia.  The Plaine de l’Igesa serves as the home facility for the club's Reserves and Academy sides, which play their home matches at the Stade Erbajolo and Stade Armand Cesari.  It is located in the commune of Haute-Corse, located in the western suburbs of Bastia.  Notable graduates of the academy include Alex Song, Michael Essien, Nicolas Penneteau, Yannick Cahuzac, Wahbi Khazri, Claude Papi and Charles Orlanducci.  Ghislain Printant was the first director of the training centre.  Benoît Tavenot and former Bastia and French international player Frédéric Née is the current director.

2016–17 SC Bastia season: Sporting Club de Bastia (commonly referred to as SC Bastia or simply Bastia, Corsican: Sporting Club di Bastia) is a French association football club based in Bastia on the island of Corsica.During the 2016-17 campaign they will be competing in the following competitions: Ligue 1, Coupe De France, Coupe de la Ligue.

2013–14 SC Bastia season: The 2013–14 season is French football club SC Bastia's 108th professional season, their 48th consecutive season in French top-flight, and their 31st consecutive season in Ligue 1.  Bastia is president by Pierre-Marie Geronimi, managed by Frédéric Hantz, and captained by Yannick Cahuzac for the season.

Forza Bastia: "Forza Bastia" is a 26-minute film documenting a UEFA Cup match between PSV Eindhoven and French club SC Bastia at the Furiani Stadium in 1978.  Jacques Tati directed the piece at the request of friend Gilberto Trigano – the President of the Bastia club at that time.  It was subsequently shelved and kept in storage until Tati's daughter Sophie Tatischeff eventually assembled the footage, which was released in 2002.

Geoffrey Acheampong: Geoffrey Edwin Acheampong (born January 28, 1997) is a Ghanaian footballer who last played for SC Bastia in the French Ligue 1.

2012–13 SC Bastia season: The 2012–13 season is French football club SC Bastia's 107th professional season, their 47th consecutive season in French top-flight, and their 30th consecutive season in Ligue 1.  Bastia is president by Pierre-Marie Geronimi, managed by Frédéric Hantz, and captained by Yannick Cahuzac for the season.  Last season; finished as second league champion, and won the first league the right to rise.  Bastia, is finished 12 in league, participated in the Coupe de la Ligue for the first time since 2001, reaching the quarter-final before being eliminated by Lille.  In the Coupe de France; the "end of 64" tour, eliminated to CA Bastia.

SC Bastia: Sporting Club Bastiais (Corsican: "Sporting Club di Bastia" , commonly referred to as SC Bastia or simply Bastia) is a French association football club based in Bastia on the island of Corsica.  The club plays in Championnat National 3, the fifth tier of French football, after being demoted four levels from Ligue 1 in 2017 due to financial difficulties after playing in the first tier for five seasons.  The club plays its home matches at the Stade Armand Cesari located within the city.  Bastia is managed by Réginald Ray and captained by midfielder Yannick Cahuzac.

Patrick Valéry: Patrick Valéry (born 3 July 1969) is a French footballer born in Brignoles who spent the majority of his playing career playing for AS Monaco.  He also had spells with Toulouse FC and SC Bastia before joining Blackburn Rovers on a free transfer in June 1997.  After an unsuccessful spell at Rovers he returned to France, re-joining Bastia in July 1998 for a fee of £80,000.

Michael Essien: Michael Kojo Essien (born 3 December 1982) is a Ghanaian footballer who currently plays for Indonesian club Persib Bandung.  He has also played for the Ghana national team more than 50 times.  He is a physically strong midfielder who has often been touted as a box-to-box midfielder for his ability to exert energy in supporting offensive and defensive play and for his powerful and tough tackling playing style which has earned him the nickname "The Bison".  Essien can also play as a defender, both on the right of defence and in the centre.

2010–11 SC Bastia season: Corsican football club SC Bastia finished the 2010–11 season as champions of the French Championnat National and was promoted to Ligue 2.  The club's top scorer of the season was David Suarez with 23 goals in 20 league matches.  SC Bastia reached the 7th round of the Coupe de France and the last 16 of the Coupe de la Ligue.  In May 2010, prior to the season, manager Faruk Hadžibegić was replaced by Frédéric Hantz.

Question: In what year was the Ghanaian footballer who graduated from the SC Bastia Reserves and Academy born?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "footballer_name": {
      "type": "string",
      "description": "The name of the Ghanaian footballer who graduated from the academy."
    },
    "academy_name": {
      "type": "string",
      "description": "The name of the academy the footballer graduated from."
    },
    "birth_year": {
      "type": "integer",
      "description": "The birth year of the footballer."
    }
  },
  "required": [
    "footballer_name",
    "academy_name",
    "birth_year"
  ],
  "additionalProperties": false
}
