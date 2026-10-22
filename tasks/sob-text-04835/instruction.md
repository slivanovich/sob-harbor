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
2014 KNVB Cup Final: The 2014 KNVB Cup Final was a football match between PEC Zwolle and Ajax on 20 April 2014 at De Kuip, Rotterdam.  It was the final match of the 2013–14 KNVB Cup competition.  PEC Zwolle beat Ajax 5–1 to secure their first KNVB Cup trophy.

2005 KNVB Cup Final: The 2005 KNVB Cup Final was a football match between Willem II and PSV on 29 May 2005 at De Kuip, Rotterdam.  It was the final match of the 2004–05 KNVB Cup competition.  PSV won 4–0 after goals from Wilfred Bouma, Phillip Cocu, Park Ji-sung and Jan Vennegoor of Hesselink.  With this victory, PSV clinched the double, as they had also become champions of the 2004–05 Eredivisie.  This was PSV's first double since the 1988–89 season.

2015 Johan Cruyff Shield: The 2015 Johan Cruyff Shield was the twentieth Johan Cruyff Shield (Dutch: "Johan Cruijff Schaal"), an annual Dutch football match played between the winners of the previous season's Eredivisie and KNVB Cup.  The match was contested by FC Groningen, the 2014–15 KNVB Cup winners, and PSV, champions of the 2014–15 Eredivisie.  It was held at the Amsterdam Arena on 2 August 2015.  PSV won the match 3–0.

2016 Johan Cruyff Shield: The 2016 Johan Cruyff Shield was the twenty-first Johan Cruyff Shield (Dutch: "Johan Cruijff Schaal"), an annual Dutch football match played between the winners of the previous season's Eredivisie and KNVB Cup.  The match was contested by Feyenoord, the 2015–16 KNVB Cup winners, and PSV, champions of the 2015–16 Eredivisie.  It was held at the Amsterdam Arena on 31 July 2016.  Watched by a crowd of 30,000 and a television audience of 1.7 million, PSV won the match 1–0.

FC Twente: Football Club Twente (] ) is a Dutch professional football club from the city of Enschede, playing in the Eredivisie.  The club was formed in 1965 by the merger of 1926 Dutch champions, Sportclub Enschede and Enschedese Boys.  They were the holders of the 2011 KNVB Cup and Johan Cruijff Schaal trophies, and were Eredivisie champions in the 2009–10 season; the team has also finished as Eredivisie runner-up thrice, was runner-up in the 1974–75 UEFA Cup, and has won the KNVB Cup three times.  Twente's home ground since 1998 is De Grolsch Veste.

2009 KNVB Cup Final: The 2009 KNVB Cup Final was a football match between Heerenveen and FC Twente on 17 May 2009 at De Kuip, Rotterdam.  It was the final match of the 2008–09 KNVB Cup competition.  Heerenveen beat FC Twente on penalties after the match finished 2–2 after extra time.  It was the side's first KNVB Cup trophy.

Phillip Cocu: Phillip John-William Cocu (] ; born 29 October 1970) is a Dutch professional football manager and former player, currently coaching PSV.

KNVB Reserve Cup: The KNVB Reserve Cup (Dutch: "KNVB Beker voor beloften" ) was a cup competition for the reserve teams of professional football clubs in the Netherlands.  The winner qualifies for next year's KNVB Cup; if the cup winner is also the champion in the national competition for reserve teams (Dutch: "Eredivisie voor beloften" ), the cup runner-up also qualifies for the KNVB Cup.

1997 KNVB Cup Final: The 1997 KNVB Cup Final was a football match between Roda JC and Heerenveen on 8 May 1997 at De Kuip, Rotterdam.  It was the final match of the 1996–97 KNVB Cup competition and the 79th KNVB Cup final.  Roda won 4–2 after goals from Gerald Sibon, Ger Senden, Eric van der Luer and Maarten Schops.  It was the side's first KNVB Cup trophy.

2006 KNVB Cup Final: The 2006 KNVB Cup Final was a football match between Ajax and PSV on 7 May 2006 at De Kuip, Rotterdam.  It was the final match of the 2005–06 KNVB Cup competition.  Ajax won 2–1, both of their goals being scored by Klaas-Jan Huntelaar.  Michael Lamey scored for PSV.

Question: What Dutch professional football manager and former player currently coaching PSV scored a goal in the 2005 KNVB Cup Final?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the Dutch professional football manager and former player."
    },
    "current_coaching_team": {
      "type": "string",
      "description": "The team the person is currently coaching."
    },
    "role_description": {
      "type": "string",
      "description": "A description of the person's professional role."
    },
    "scoring_event": {
      "type": "object",
      "properties": {
        "event_name": {
          "type": "string",
          "description": "The name of the football final where the person scored a goal."
        },
        "event_year": {
          "type": "integer",
          "description": "The year the final took place."
        }
      },
      "required": [
        "event_name",
        "event_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_name",
    "current_coaching_team",
    "role_description",
    "scoring_event"
  ],
  "additionalProperties": false
}
