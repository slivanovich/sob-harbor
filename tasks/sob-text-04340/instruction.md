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
2010 Bahrain Grand Prix: The 2010 Bahrain Grand Prix was a Formula One motor race held on 14 March 2010 at the Bahrain International Circuit, Sakhir, Bahrain.  It was the seventh Bahrain Grand Prix and the opening round of the 2010 Formula One season.  It was the first time since 2006 that Bahrain had hosted the opening round and the race took place on a lengthened layout of the track.

2012 Bahrain Grand Prix: The 2012 Bahrain Grand Prix (formally known as the 2012 Formula 1 Gulf Air Bahrain Grand Prix) was a Formula One motor race held on 22 April 2012 at the Bahrain International Circuit in Sakhir, Bahrain.  It was the first time Formula One returned to Bahrain after the 2011 race was cancelled due to ongoing anti-government protests.  The race, the eighth running of the Bahrain Grand Prix, was contested over 57 laps and was the fourth round of the 2012 Formula One season.

2014 Bahrain Grand Prix: The 2014 Bahrain Grand Prix (formally the 2014 Formula 1 Gulf Air Bahrain Grand Prix) was a Formula One motor race held on 6 April at the Bahrain International Circuit in Sakhir, Bahrain.  It was the third round of the 2014 Formula One season, the 900th Formula One World Championship event, and the eleventh running of the race.  The 57-lap race was won by Mercedes driver Lewis Hamilton who started from second position.  His teammate Nico Rosberg finished second and Force India driver Sergio Pérez came in third.  It was Hamilton's second victory of the season, his first in Bahrain, and the 24th of his Formula One career.

2011 Bahrain Grand Prix: The 2011 Bahrain Grand Prix (formally the 2011 Formula 1 Gulf Air Bahrain Grand Prix) was scheduled to be the opening round of the 2011 Formula One season.  Planned to be held on 13 March 2011 at the Bahrain International Circuit in Sakhir, Bahrain, it was postponed on 21 February 2011 due to the Bahraini uprising.  On 3 June, it was announced that the race would be held on 30 October, thus making it round 17 of the 20 to be held during 2011.  Following controversy over the reinstatement of the race, organisers of the Grand Prix abandoned their bid to host a race in 2011.

2008 Bahrain Grand Prix: The 2008 Bahrain Grand Prix (formally the V Gulf Air Bahrain Grand Prix) was a Formula One motor race held on 6 April 2008 at the Bahrain International Circuit, in Sakhir, Bahrain.  It was the third race of the 2008 Formula One season.  The 57-lap race was won by Felipe Massa for the Ferrari team.  Kimi Räikkönen was second in the other Ferrari, and BMW Sauber driver Robert Kubica was third.

Kimi Räikkönen: Kimi-Matias Räikkönen (] ; born 17 October 1979), nicknamed "The Ice Man", is a Finnish racing driver currently driving for Ferrari in Formula One.  He won the F1 Driver's championship with Ferrari in 2007 and to date remains the last Ferrari Champion.

2006 Bahrain Grand Prix: The 2006 Bahrain Grand Prix (formally the III Gulf Air Bahrain Grand Prix) was a Formula One motor race held at the Bahrain International Circuit in Sakhir, Bahrain on 12 March 2006.  The 57-lap race was the opening round of the 2006 Formula One season and the third running of the Bahrain Grand Prix.  It was won by the World Champions, Fernando Alonso and the Renault team.  Ferrari driver and polesitter Michael Schumacher began his final season in Formula One (before his return with Mercedes in ) with second position.  Kimi Räikkönen completed the podium after he finished in third place with the McLaren team, despite starting in last position.

2016 Bahrain Grand Prix: The 2016 Bahrain Grand Prix (formally known as the 2016 Formula 1 Gulf Air Bahrain Grand Prix) was a Formula One motor race that was held on 3 April 2016 at the Bahrain International Circuit in Sakhir, Bahrain.  The race was the second round of the 2016 season and marked the twelfth time that the Bahrain Grand Prix had been run as a round of the Formula One World Championship.  Lewis Hamilton was the defending race winner, while his Mercedes team-mate, Nico Rosberg was the Drivers' Championship leader coming into the round.

2015 Bahrain Grand Prix: The 2015 Bahrain Grand Prix (formally known as the 2015 Formula 1 Gulf Air Bahrain Grand Prix) was a Formula One motor race that was held on 19 April 2015 at the Bahrain International Circuit in Sakhir, Bahrain.  The race was the fourth round of the 2015 season and marked the eleventh time that the Bahrain Grand Prix has been run as a round of the Formula One World Championship.

2017 Bahrain Grand Prix: The 2017 Bahrain Grand Prix (formally known as the 2017 Formula 1 Gulf Air Bahrain Grand Prix) was a Formula One motor race that took place on 16 April 2017 at the Bahrain International Circuit in Sakhir, Bahrain.  The race was the third round of the 2017 season and marked the thirteenth time that the Bahrain Grand Prix has been run as a round of the Formula One World Championship.  The winner of the previous Bahrain Grand Prix, Nico Rosberg, did not compete as he had retired after the 2016 season.  Before the race, Sebastian Vettel and Lewis Hamilton shared the lead in the Drivers' Championship.  Mercedes led the Constructors' Championship by one point over Ferrari.

Question: What is the nickname of the racer that came second in the 2008 Bahrain Grand Prix?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "grand_prix_year": {
      "type": "integer",
      "description": "The year the Grand Prix took place."
    },
    "grand_prix_name": {
      "type": "string",
      "description": "The formal name of the Grand Prix event."
    },
    "second_place_driver": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the driver who finished in second place."
        },
        "nickname": {
          "type": "string",
          "description": "The nickname of the driver."
        }
      },
      "required": [
        "name",
        "nickname"
      ],
      "additionalProperties": false
    },
    "answer": {
      "type": "string",
      "description": "The nickname of the racer who came second."
    }
  },
  "required": [
    "grand_prix_year",
    "grand_prix_name",
    "second_place_driver",
    "answer"
  ],
  "additionalProperties": false
}
