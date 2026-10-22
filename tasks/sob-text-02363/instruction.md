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
2016 Bahrain Grand Prix: The 2016 Bahrain Grand Prix (formally known as the 2016 Formula 1 Gulf Air Bahrain Grand Prix) was a Formula One motor race that was held on 3 April 2016 at the Bahrain International Circuit in Sakhir, Bahrain.  The race was the second round of the 2016 season and marked the twelfth time that the Bahrain Grand Prix had been run as a round of the Formula One World Championship.  Lewis Hamilton was the defending race winner, while his Mercedes team-mate, Nico Rosberg was the Drivers' Championship leader coming into the round.

2017 Bahrain Grand Prix: The 2017 Bahrain Grand Prix (formally known as the 2017 Formula 1 Gulf Air Bahrain Grand Prix) was a Formula One motor race that took place on 16 April 2017 at the Bahrain International Circuit in Sakhir, Bahrain.  The race was the third round of the 2017 season and marked the thirteenth time that the Bahrain Grand Prix has been run as a round of the Formula One World Championship.  The winner of the previous Bahrain Grand Prix, Nico Rosberg, did not compete as he had retired after the 2016 season.  Before the race, Sebastian Vettel and Lewis Hamilton shared the lead in the Drivers' Championship.  Mercedes led the Constructors' Championship by one point over Ferrari.

2012 Bahrain Grand Prix: The 2012 Bahrain Grand Prix (formally known as the 2012 Formula 1 Gulf Air Bahrain Grand Prix) was a Formula One motor race held on 22 April 2012 at the Bahrain International Circuit in Sakhir, Bahrain.  It was the first time Formula One returned to Bahrain after the 2011 race was cancelled due to ongoing anti-government protests.  The race, the eighth running of the Bahrain Grand Prix, was contested over 57 laps and was the fourth round of the 2012 Formula One season.

2014 Bahrain Grand Prix: The 2014 Bahrain Grand Prix (formally the 2014 Formula 1 Gulf Air Bahrain Grand Prix) was a Formula One motor race held on 6 April at the Bahrain International Circuit in Sakhir, Bahrain.  It was the third round of the 2014 Formula One season, the 900th Formula One World Championship event, and the eleventh running of the race.  The 57-lap race was won by Mercedes driver Lewis Hamilton who started from second position.  His teammate Nico Rosberg finished second and Force India driver Sergio Pérez came in third.  It was Hamilton's second victory of the season, his first in Bahrain, and the 24th of his Formula One career.

2006 Bahrain Grand Prix: The 2006 Bahrain Grand Prix (formally the III Gulf Air Bahrain Grand Prix) was a Formula One motor race held at the Bahrain International Circuit in Sakhir, Bahrain on 12 March 2006.  The 57-lap race was the opening round of the 2006 Formula One season and the third running of the Bahrain Grand Prix.  It was won by the World Champions, Fernando Alonso and the Renault team.  Ferrari driver and polesitter Michael Schumacher began his final season in Formula One (before his return with Mercedes in ) with second position.  Kimi Räikkönen completed the podium after he finished in third place with the McLaren team, despite starting in last position.

Nico Rosberg: Nico Erik Rosberg (born 27 June 1985) is a German–Finnish former Formula One racing driver and current Formula One World Champion who drove for Williams F1 and Mercedes AMG Petronas under the German flag.  Born in Germany to Finnish former world champion Keke Rosberg and his German wife Sina, he holds dual nationality, and briefly competed for Finland early in his racing career.  However, he does not speak Finnish, although he is reported to be fluent in five languages.

2010 Bahrain Grand Prix: The 2010 Bahrain Grand Prix was a Formula One motor race held on 14 March 2010 at the Bahrain International Circuit, Sakhir, Bahrain.  It was the seventh Bahrain Grand Prix and the opening round of the 2010 Formula One season.  It was the first time since 2006 that Bahrain had hosted the opening round and the race took place on a lengthened layout of the track.

2013 Bahrain Grand Prix: The 2013 Bahrain Grand Prix (formally known as the 2013 Formula 1 Gulf Air Bahrain Grand Prix) was a Formula One motor race held on 21 April 2013 at the Bahrain International Circuit in Sakhir, Bahrain.  Mercedes' Nico Rosberg started the race from pole.  Sebastian Vettel won the race, with Lotus F1 drivers Kimi Räikkönen and Romain Grosjean completing the podium.

2015 Bahrain Grand Prix: The 2015 Bahrain Grand Prix (formally known as the 2015 Formula 1 Gulf Air Bahrain Grand Prix) was a Formula One motor race that was held on 19 April 2015 at the Bahrain International Circuit in Sakhir, Bahrain.  The race was the fourth round of the 2015 season and marked the eleventh time that the Bahrain Grand Prix has been run as a round of the Formula One World Championship.

2008 Bahrain Grand Prix: The 2008 Bahrain Grand Prix (formally the V Gulf Air Bahrain Grand Prix) was a Formula One motor race held on 6 April 2008 at the Bahrain International Circuit, in Sakhir, Bahrain.  It was the third race of the 2008 Formula One season.  The 57-lap race was won by Felipe Massa for the Ferrari team.  Kimi Räikkönen was second in the other Ferrari, and BMW Sauber driver Robert Kubica was third.

Question: The 2016 Bahrain Grand Prix, was a Formula One motor race that was held on which date, at the Bahrain International Circuit in Sakhir, Bahrain, Lewis Hamilton was the defending race winner, while his Mercedes team-mate, Nico Erik Rosberg, a German–Finnish former Formula One racing driver, was the Drivers' Championship leader coming into the round?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "grand_prix_year": {
      "type": "integer",
      "description": "The year the Grand Prix was held."
    },
    "race_date": {
      "type": "string",
      "description": "The specific date the race was held."
    },
    "circuit_details": {
      "type": "object",
      "properties": {
        "circuit_name": {
          "type": "string",
          "description": "The name of the racing circuit."
        },
        "city": {
          "type": "string",
          "description": "The city where the circuit is located."
        },
        "country": {
          "type": "string",
          "description": "The country where the circuit is located."
        }
      },
      "required": [
        "circuit_name",
        "city",
        "country"
      ],
      "additionalProperties": false
    },
    "driver_information": {
      "type": "array",
      "description": "Details about key drivers mentioned in the context of this race.",
      "items": {
        "type": "object",
        "properties": {
          "driver_name": {
            "type": "string",
            "description": "The name of the driver."
          },
          "role_in_race": {
            "type": "string",
            "description": "The driver's specific role or status related to this race (e.g., defending winner, championship leader)."
          },
          "team_mate_of": {
            "type": "string",
            "description": "The name of the driver's team-mate, if applicable."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the driver, if specified."
          }
        },
        "required": [
          "driver_name",
          "role_in_race"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "grand_prix_year",
    "race_date",
    "circuit_details",
    "driver_information"
  ],
  "additionalProperties": false
}
