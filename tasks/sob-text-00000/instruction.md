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
2007 Masters of Formula 3: The 2007 Zandvoort Masters of Formula 3 @ Zolder was the seventeenth Masters of Formula 3 race held at Zolder on 5 August 2007.  It was won by Nico Hülkenberg, for ASM Formule 3.

Richard Lietz: Richard Lietz (born 17 December 1983 in Waidhofen an der Ybbs) is an Austrian professional racing driver.  He has competed in such series as American Le Mans Series, Formula 3 Euro Series and the Rolex Sports Car Series.  He is also a multiple race-winner in Porsche Supercup.  Lietz was overall series champion in the 2007 International GT Open season with Swiss driver Joël Camathias.  He has won the GT2 class of the Le Mans Series twice, alongside German driver Marc Lieb in both in the 2009 and 2010 seasons.

James Rossiter: James Rossiter (born 25 August 1983) is a professional racing driver from England.  He is currently driving for TOM'S in Super GT and in Super Formula.  Previously he was an F1 test driver for the Honda, Super Aguri and Force India Formula One teams.  He has participated in karting, Formula Renault, British Formula 3 and Formula 3 Euro Series.  His father, Jeremy, was also a racing driver.

Felix Rosenqvist: Felix Rosenqvist (born 7 November 1991 in Värnamo) is a Swedish racing driver currently racing in Formula E for Mahindra Racing and Super Formula for SUNOCO Team LeMans.  He holds the record of being the only driver ever to win the Macau Grand Prix (twice), Masters of Formula 3 (twice), Grand Prix de Pau and the FIA Formula 3 European Championship.

Nico Hülkenberg: Nicolas Hülkenberg (] , born 19 August 1987) is a German professional racing driver currently racing for the Renault Sport F1 Team.  In 2015, he also contested in two rounds of the 2015 FIA World Endurance Championship season for Porsche, winning the 2015 24 Hours of Le Mans in his first attempt.  He was the 2009 champion of the GP2 Series, and is a previous champion of both the Formula 3 Euro Series and A1 Grand Prix, as part of A1 Team Germany.  He is one of three drivers since 2005 to win the GP2 series championship in his debut season, the others being Lewis Hamilton and Nico Rosberg.  s of September 2017 , Hülkenberg holds the record for the most Formula One career starts without a podium finish, a record he broke when he failed to finish in his 129th race (the 2017 Singapore Grand Prix) and in so doing passed Adrian Sutil's previous record of 128.

Derek Daly: Derek Daly (born 11 March 1953 in Ballinteer, Dublin) is a former racing driver from Ireland.  He won the 1977 British Formula 3 Championship, and competed as a professional racing driver for 17 years participating in 64 World Championship Formula One Grands Prix, debuting on 2 April 1978.  He scored a total of 15 championship points.  He also participated in several non-Championship Formula One races.  Daly later became a US citizen and now resides in Noblesville, Indiana with his third wife and three children from his second marriage.

Jeroen Bleekemolen: Jeroen Bleekemolen (born 23 October 1981 in Heemstede) is a Dutch professional racing driver.  In the Chrysler Viper GTS-R he drove in the FIA GT Championship, with great success.  He competed in the very competitive German Formula Three Championship and drove a number of times at the Masters of Formula 3 at Circuit Zandvoort, the unofficial F3 World Championship.  Together with Opel he raced in the DTM.  In 2005 Jeroen Bleekemolen competes in the ELF BRL V6.

John Martin (Australian racing driver): John Martin is an Australian professional racing driver.  Martin has had wide experience racing in European based open-wheel series since 2006.  In that time Martin has had a wide experience of open-wheel racing having driven in various national and international series driving Formula Ford, Formula 3, A1 Grand Prix and Formula Renault 3.5.  For the past two season Martin has raced for several teams in the football inspired series Superleague Formula.  Martin has long been associated with the British Alan Docking Racing team having raced with them in a variety of formulae for four of the five years he has been racing in Europe.  In 2012 Martin will again race with ADR, racing an Oreca 03 sports car in the LMP2 class of the FIA World Endurance Championship.

Jo Zeller: Jo Zeller (born 17 July 1955 in Männedorf) is a Swiss racing driver.  He has raced in such series as Austria Formula 3 Cup and is a twelve-time Swiss Formula Three champion.  In the early 1990s, he set up his own racing team, Jo Zeller Racing, which has raced in series such as Formula 3 Euro Series, Formula Lista Junior, Austria Formula 3 Cup and the German Formula Three Championship.

Tom Coronel: Tom Romeo Coronel (born 5 April 1972) is a Dutch professional racing driver.  Tom's twin brother Tim is also a racer, just like their father Tom Coronel Sr.  His most important results are winning the Marlboro Masters of Formula 3 race in 1997, the Formula Nippon championship in 1999, and the 2006 and 2009 World Touring Car Championship Independents' Trophy.  As of September 2016, Tom Coronel has driven over 1,000 races.

Question: Which  German professional racing driver won  2007 Masters of Formula 3 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "driver_name": {
      "type": "string",
      "description": "The name of the professional racing driver."
    },
    "driver_nationality": {
      "type": "string",
      "description": "The nationality of the racing driver."
    },
    "event_name": {
      "type": "string",
      "description": "The name of the racing event won."
    },
    "event_year": {
      "type": "integer",
      "description": "The year the event was won."
    },
    "winning_team": {
      "type": "string",
      "description": "The team the driver won for."
    }
  },
  "required": [
    "driver_name",
    "driver_nationality",
    "event_name",
    "event_year"
  ],
  "additionalProperties": false
}
