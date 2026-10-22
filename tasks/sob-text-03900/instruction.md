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
Albert Park and Lake: Albert Park and Albert Park Lake are situated in the City of Port Phillip, Victoria, Australia, 3 km south of the Melbourne CBD.

2013 Australian Grand Prix: The 2013 Australian Grand Prix (formally known as the 2013 Formula 1 Rolex Australian Grand Prix) was a Formula One motor race that was held on 17 March 2013 as the opening round of the 2013 championship.  The race was held at the Melbourne Grand Prix Circuit in the Melbourne suburb of Albert Park.  It was the 78th race in the combined history of the Australian Grand Prix—which dates back to the 100 Miles Road Race of 1928—and the 18th time the event has been held at the Melbourne Grand Prix Circuit.  The race was won by Kimi Räikkönen with Fernando Alonso coming second and Sebastian Vettel coming third.

2006 Australian Grand Prix: The 2006 Australian Grand Prix (formally the LXXI Foster's Australian Grand Prix) was a Formula One motor race held at the Melbourne Grand Prix Circuit in Albert Park, Melbourne on 2 April 2006.  The 57-lap race was the 22nd Australian Grand Prix as part of the World Championship, and the 71st Australian Grand Prix overall.  It was also the third round of the 2006 Formula One season; the Australian Grand Prix had been the season opener since 1996, but this race was held later due to the 2006 Commonwealth Games being held in Melbourne at the time of the opening round.  The season was instead opened in Bahrain, and Australia regained its first round of the season slot for 2007.

2014 Australian Grand Prix: The 2014 Australian Grand Prix (formally known as the 2014 Formula 1 Rolex Australian Grand Prix) was a Formula One motor race that was held on 16 March 2014 in Melbourne.  The race was contested over 58 laps of the Melbourne Grand Prix Circuit and was the first round of the 2014 FIA Formula One World Championship.  It marked the début of new Formula One regulations which introduced 1.6 litre turbocharged V6 engines to the sport; the first such instance, since the 1988 Australian Grand Prix, that turbocharged engines have been used in Formula One.  It was the seventy-ninth race in the combined history of the Australian Grand Prix—which dates back to the 100 Miles Road Race of 1928—and the nineteenth time the event was held at the Melbourne Grand Prix Circuit.  The race also marked the thirtieth year that the Australian Grand Prix was run as a round of the Formula One World Championship.

Australian Grand Prix: The Australian Grand Prix is a motor race held annually in Australia currently under contract to host Formula One until 2023.  The Grand Prix is the oldest surviving motor racing competition held in Australia having been held 79 times since it was first run at Phillip Island in 1928.  Since 1985, the race has been a round of the FIA Formula One World Championship and is currently held at the Melbourne Grand Prix Circuit at Albert Park in Melbourne.  Prior to its inclusion in the World Championship, it was held at a multitude of venues in every state of Australia.  It was a centrepiece of the Tasman Series in most years between 1964 and 1972 and was a round of the Australian Drivers' Championship on many occasions between 1957 and 1983.  It became part of the Formula One World Championship in 1985 and was held at the Adelaide Street Circuit in Adelaide, South Australia, from that year to 1995, before moving to Melbourne in 1996.  The winner of the race is presented with a circular plate, recently named the Jack Brabham trophy named for the three-time winner in a design based on the steering wheel of one of Brabham's racing cars and a perpetual trophy, the Lex Davison trophy, named for four-time winner and dates back to the 1960s.

2017 Australian Grand Prix: The 2017 Australian Grand Prix (formally known as the 2017 Formula 1 Rolex Australian Grand Prix) was a Formula One motor race that took place on 26 March 2017 in Melbourne.  The race was contested over fifty-seven laps of the Melbourne Grand Prix Circuit and was the first round of the 2017 FIA Formula One World Championship.  The race marked the eighty-first race in the combined history of the Australian Grand Prix – which dates back to the 100 Miles Road Race of 1928 – and the twenty-second time the event was held at the Melbourne Grand Prix Circuit.  The reigning World Champion Nico Rosberg was the winner of the 2016 race, but he did not defend his win as he retired from the sport after the 2016 season.

2016 Australian Grand Prix: The 2016 Australian Grand Prix (formally known as the 2016 Formula 1 Rolex Australian Grand Prix) was a Formula One motor race that was held on 20 March 2016 in Melbourne.  The race was contested over fifty-seven laps of the Melbourne Grand Prix Circuit and was the first round of the 2016 FIA Formula One World Championship.  The race marked the eightieth race in the combined history of the Australian Grand Prix—which dates back to the 100 Miles Road Race of 1928—and the twenty-first time the event was held at the Melbourne Grand Prix Circuit.  Mercedes driver Lewis Hamilton was the defending race winner.

2001 Australian Grand Prix: The 2001 Australian Grand Prix was a Formula One motor race held on 4 March 2001 at the Melbourne Grand Prix Circuit.  It was the 66th running of the Australian Grand Prix and the first race of the 2001 Formula One season.  The race was won by German driver Michael Schumacher driving a Ferrari F2001, but the race was marred by the death of track marshal Graham Beveridge during the race.  This was the last trackside death in Formula One until the 2013 Canadian Grand Prix.

2012 Australian Grand Prix: The 2012 Australian Grand Prix (formally, the 2012 Formula 1 Qantas Australian Grand Prix) was a Formula One motor race held on 18 March 2012 as the opening round of the 2012 Formula One season.  It was the 77th race in the combined history of the Australian Grand Prix that dates back to the 100 Miles Road Race of 1928, and the 17th time the event has been held at the Melbourne Grand Prix Circuit at Albert Park.

2015 Australian Grand Prix: The 2015 Australian Grand Prix, formally titled the 2015 Formula 1 Rolex Australian Grand Prix, was a Formula One motor race that was held on 15 March 2015 in Melbourne.  The race was contested over fifty-eight laps of the Melbourne Grand Prix Circuit and was the first round of the FIA Formula One World Championship.  The race marked the 80th race in the combined history of the Australian Grand Prix—which dates back to the 100 Miles Road Race of 1928—and the twentieth time the event was held at the Melbourne Grand Prix Circuit.

Question: The 2006 Australian Grand Prix, was a Formula One motor race held at the Melbourne Grand Prix Circuit in which location situated in the City of Port Phillip, Victoria, Australia, 3 km south of the Melbourne CBD?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "grand_prix_year": {
      "type": "integer",
      "description": "The year the Grand Prix was held."
    },
    "circuit_name": {
      "type": "string",
      "description": "The name of the motor racing circuit."
    },
    "circuit_location_details": {
      "type": "object",
      "properties": {
        "location_name": {
          "type": "string",
          "description": "The specific suburb or park where the circuit is located."
        },
        "city": {
          "type": "string",
          "description": "The main city where the circuit is located."
        },
        "city_of_port_phillip": {
          "type": "boolean",
          "description": "Indicates if the location is within the City of Port Phillip."
        },
        "state": {
          "type": "string",
          "description": "The state or territory where the circuit is located."
        },
        "country": {
          "type": "string",
          "description": "The country where the circuit is located."
        },
        "distance_from_melbourne_cbd_km": {
          "type": "integer",
          "description": "The distance in kilometers from the Melbourne CBD."
        }
      },
      "required": [
        "location_name",
        "city",
        "city_of_port_phillip",
        "state",
        "country",
        "distance_from_melbourne_cbd_km"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "grand_prix_year",
    "circuit_name",
    "circuit_location_details"
  ],
  "additionalProperties": false
}
