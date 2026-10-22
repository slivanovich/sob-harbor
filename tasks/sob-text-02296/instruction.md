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
1996 German Grand Prix: The 1996 German Grand Prix was a Formula One motor race held on 28 July 1996 at Hockenheimring.  Damon Hill started the race on pole position, and won it after Gerhard Berger's engine failed with 3 laps to go.

1990 German Grand Prix: The 1990 German Grand Prix was a Formula One motor race held at Hockenheimring on 29 July 1990.  It was the ninth round of the 1990 Formula One season.  The race was the 52nd German Grand Prix and the 14th to be held at the Hockenheimring.  It was the 39th and last Formula One Grand Prix to be held in West Germany prior to its re-unification with East Germany.  The race was held over 45 laps of the seven kilometre circuit for a race distance of 306 kilometres.

2013 German Grand Prix: The 2013 German Grand Prix (formally known as the Formula 1 Großer Preis Santander von Deutschland 2013) was a Formula One motor race that was held on 7 July 2013 at the Nürburgring in Nürburg, Germany.  The race was the ninth round of the 2013 season, and marked the 74th running of the German Grand Prix overall, and the 60th running of the German Grand Prix since 1950, when the racing series now known as the Formula One World Championship was created.  This is the earliest a German Grand Prix has been held in a calendar year, followed by the 1926 and the 2009 editions of the race.

Jordi Torres: Jordi Torres Fernández (born August 27, 1987) is a Spanish motorcycle racer.  He is a two-time winner of the Spanish Moto2 championship, and has previously competed in his native Supersport and Stock Extreme championships.  He is best known for winning the 2013 German Grand Prix, in the Moto2 class; having qualified in a career-best second place, Torres overtook long-time race leader Pol Espargaró with ten laps remaining, and held on to win the race, his first Grand Prix podium.  In 2015 and 2016 he competed in the Superbike World Championship.

Börje Jansson: Börje Jansson (born November 10, 1942 ) was a former Grand Prix motorcycle road racer from Sweden.  His best years were in 1971 and 1972, when he finished third in the 125cc world championship riding for the Maico factory racing team.  He won the 1972 125cc East German Grand Prix, marking the first Grand Prix road racing victory for the German motorcycle manufacturer.  Jansson won four Grand Prix races in his career.  Jansson is the only rider in history to win a Grand Prix riding the Derbi 250 twin (1972 Austrian Grand Prix at the Salzburgring), out of only two races with the Spanish machine.

Gerhard Berger: Gerhard Berger (born 27 August 1959) is an Austrian former Formula One racing driver.  He competed in Formula One for 14 seasons, twice finishing 3rd overall in the championship (1988 and 1994), both times driving for Ferrari.  He won ten Grands Prix, achieved 48 podiums, 12 poles and 21 fastest laps.  With 210 starts he is amongst the most experienced Formula One drivers of all time.  He led 33 of the 210 races he competed in and retired from 95 of them.  His first and last victories were also the first and last victories for the Benetton team, with eleven years separating them.  He was also a race winner with Ferrari and with McLaren.  When at McLaren, Berger drove alongside Ayrton Senna, contributing to the team's 1990 and 1991 constructors titles.

Peter Westbury: Peter Westbury (26 May 1938 – 7 December 2015) was a British racing driver from England.  He participated in two World Championship Formula One Grands Prix, scoring no championship points.  In 1969 he raced a Formula 2 Brabham-Cosworth, driving in his first Grand Prix in the 1969 German Grand Prix.  He finished ninth on the road, fifth in the F2 class.  The following year he failed to qualify for the 1970 United States Grand Prix driving a works BRM, after an engine failure.

Klenk: The Klenk-Meteor was a racing car which competed in the 1954 German Grand Prix.  The car was based on the established German marque of Veritas which was active between 1948 and 1953.  Veritas is chiefly remembered as a manufacturer of sports cars and successful Formula Two racing cars.  The company closed when its founder, Ernst Loof, became ill.  He subsequently died in 1956.  The Klenk-Meteor entered for the 1954 German Grand Prix was essentially a Veritas Formula Two car.  The car was owned and prepared by the noted German racing driver Hans Klenk who intended to race it himself in the Grand Prix.  However, Klenk's career as a racing driver came to an end when he suffered injuries in an accident while working as a test driver for Mercedes-Benz.  The car was driven in the Grand Prix by another German, Theo Helfrich.  He retired on lap 9 with engine failure.

1961 German Grand Prix: The 1961 German Grand Prix was the 23rd time the German Grand Prix (or Grosser Preis von Deutschland) motor race was held.  The race also held the honorary designation of the 21st European Grand Prix.  It was run to Formula One regulations as race 6 of 8 in both the 1961 World Championship of Drivers and the 1961 International Cup for Formula One Manufacturers It was held on 6 August 1961 over 15 laps of the giant 14.2 mile Nürburgring Nordschleife circuit for a race distance of almost 213 miles.  The race also celebrated the 100th race since the establishment of the World Championship in 1950.

1974 German Grand Prix: The 1974 German Grand Prix was a Formula One motor race held at the Nürburgring on 4 August 1974.  It was race 11 of 15 in both the 1974 World Championship of Drivers and the 1974 International Cup for Formula One Manufacturers.  It was the 36th German Grand Prix and the 33rd to be held at the Nürburgring complex of circuits.  The race was won by Swiss driver Clay Regazzoni driving a Ferrari 312B3.  Regazzoni led every lap on the way to his second Grand Prix victory, some four years after his debut victory at the 1970 Italian Grand Prix.  South African driver Jody Scheckter was second driving a Tyrrell 007 ahead of Argentine driver Carlos Reutemann (Brabham BT44).

Question: The 1996 German Grand Prix was won by the driver who took over the lead when which Austrian's engine failed with 3 laps remaining?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "grand_prix_year": {
      "type": "integer",
      "description": "The year of the German Grand Prix."
    },
    "winning_driver": {
      "type": "string",
      "description": "The driver who won the Grand Prix."
    },
    "driver_who_retired": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the driver whose engine failed."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the driver whose engine failed."
        },
        "retirement_reason": {
          "type": "string",
          "description": "The reason for the driver's retirement from the race."
        },
        "laps_remaining_at_retirement": {
          "type": "integer",
          "description": "The number of laps remaining when the driver retired."
        }
      },
      "required": [
        "name",
        "nationality",
        "retirement_reason",
        "laps_remaining_at_retirement"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "grand_prix_year",
    "winning_driver",
    "driver_who_retired"
  ],
  "additionalProperties": false
}
