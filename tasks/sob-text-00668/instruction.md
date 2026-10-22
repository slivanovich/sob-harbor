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
1972 Pau Grand Prix: The 1972 Pau Grand Prix was a Formula Two motor race held on 5 May 1972 at the Pau circuit, in Pau, Pyrénées-Atlantiques, France.  The Grand Prix was won by Peter Gethin, driving the Chevron B20.  Patrick Depailler finished second and David Purley third.

1971 Pau Grand Prix: The 1971 Pau Grand Prix was a Formula Two motor race held on 25 April 1971 at the Pau circuit, in Pau, Pyrénées-Atlantiques, France.  The Grand Prix was won by Reine Wisell, driving the Lotus 69C.  Jean-Pierre Jabouille finished second and Jean-Pierre Jaussaud third.

1979 Pau Grand Prix: The 1979 Pau Grand Prix was a Formula Two motor race held on 4 June 1979 at the Pau circuit, in Pau, Pyrénées-Atlantiques, France.  The Grand Prix was won by Eddie Cheever, driving the Osella FA2/79.  Siegfried Stohr finished second and Marc Surer third.

Klenk: The Klenk-Meteor was a racing car which competed in the 1954 German Grand Prix.  The car was based on the established German marque of Veritas which was active between 1948 and 1953.  Veritas is chiefly remembered as a manufacturer of sports cars and successful Formula Two racing cars.  The company closed when its founder, Ernst Loof, became ill.  He subsequently died in 1956.  The Klenk-Meteor entered for the 1954 German Grand Prix was essentially a Veritas Formula Two car.  The car was owned and prepared by the noted German racing driver Hans Klenk who intended to race it himself in the Grand Prix.  However, Klenk's career as a racing driver came to an end when he suffered injuries in an accident while working as a test driver for Mercedes-Benz.  The car was driven in the Grand Prix by another German, Theo Helfrich.  He retired on lap 9 with engine failure.

George Russell (racing driver): George Russell (born 15 February 1998) is a British racing driver.

1969 Pau Grand Prix: The 1969 Pau Grand Prix was a Formula Two motor race held on 20 April 1969 at the Pau circuit, in Pau, Pyrénées-Atlantiques, France.  The Grand Prix was won by Jochen Rindt, driving the Lotus 59B.  Jean-Pierre Beltoise finished second and Piers Courage third.

2016 Pau Grand Prix: The 2016 Pau Grand Prix was a Formula Three motor race held on 15 May, 2016 at the Pau circuit, in Pau, Pyrénées-Atlantiques, France.  The Grand Prix was run as the third round of the 2016 European Formula 3 Championship and was won by Alessio Lorandi, driving for Carlin.  Lance Stroll finished second and George Russell third.

1970 Pau Grand Prix: The 1970 Pau Grand Prix was a Formula Two motor race held on 5 April 1970 at the Pau circuit, in Pau, Pyrénées-Atlantiques, France.  The Grand Prix was won by Jochen Rindt, driving the Lotus 69.  Henri Pescarolo finished second and Tim Schenken third.

Pau Grand Prix: The Pau Grand Prix (French: "Grand Prix de Pau" ) is a motor race held in Pau, in the Pyrénées-Atlantiques department of southwestern France.  The French Grand Prix was held at Pau in 1930, leading to the annual Pau Grand Prix being inaugurated in 1933.  It was not run during World War II.

1933 Pau Grand Prix: The 1933 Pau Grand Prix was a motor race held on 19 February 1933 at the Pau circuit, in Pau, Pyrénées-Atlantiques, France.  It was the inaugural Pau Grand Prix (i.e. the first race that actually held "Grand Prix de Pau" title), although the numbering of the races may not have reflected this due to a confusion about the 1901 race at Pau.  The Grand Prix was won by Marcel Lehoux, driving the Bugatti T51.  Guy Moll finished second and Philippe Étancelin third.

Question: Which British racing driver came third in 2016 Pau Grand Prix

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "grand_prix": {
      "type": "object",
      "properties": {
        "year": {
          "type": "integer",
          "description": "The year the Grand Prix took place."
        },
        "race_type": {
          "type": "string",
          "description": "The type of motor race (e.g., Formula Three)."
        }
      },
      "required": [
        "year",
        "race_type"
      ],
      "additionalProperties": false
    },
    "driver": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the racing driver."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the racing driver."
        }
      },
      "required": [
        "name",
        "nationality"
      ],
      "additionalProperties": false
    },
    "result": {
      "type": "object",
      "properties": {
        "position": {
          "type": "integer",
          "description": "The finishing position of the driver in the race."
        }
      },
      "required": [
        "position"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "grand_prix",
    "driver",
    "result"
  ],
  "additionalProperties": false
}
