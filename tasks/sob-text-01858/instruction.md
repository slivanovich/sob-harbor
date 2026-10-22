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
Sauber C35: The Sauber C35 is a Formula One racing car designed by Sauber to compete in the 2016 Formula One season.  The car was driven by Marcus Ericsson and Felipe Nasr, and used the Ferrari 061 power unit.

Marcus Ericsson: Marcus Ericsson (born 2 September 1990) is a Swedish race car driver currently racing for Sauber in Formula One, where he is contracted to the end of the 2017 season.

Sauber C32: The Sauber C32 was a Formula One racing car designed and built by the Sauber team for use in the 2013 Formula One season.  It was driven by Esteban Gutiérrez in his Formula One debut alongside Nico Hülkenberg, who joined the team after racing for Force India in 2012.  The car was launched on 2 February 2013.

Force India VJM10: The Force India VJM10 is a Formula One racing car designed and constructed by Force India to compete during the 2017 Formula One season.  The car is driven by Sergio Pérez and Esteban Ocon, who joined the team after Nico Hülkenberg left the team at the end of the season.  It made its competitive début at the 2017 Australian Grand Prix.

Sauber C34: The Sauber C34 is a Formula One racing car which Sauber used to compete in the 2015 Formula One season.  The C34 was driven by Marcus Ericsson and Felipe Nasr.

Sauber C33: The Sauber C33 is a Formula One racing car designed by Sauber to compete in the 2014 Formula One season.  It was driven by Esteban Gutiérrez and Adrian Sutil, who joined the team after Nico Hülkenberg returned to Force India.  The C33 was designed to use Ferrari's new 1.6-litre V6 turbocharged engine, the 059/3.

Sauber C36: The Sauber C36 is a Formula One racing car designed and constructed by Sauber to compete during the 2017 Formula One season.  The car is driven by Marcus Ericsson and Pascal Wehrlein, who joined the team after Felipe Nasr left the team at the end of the season.  Antonio Giovinazzi drove the car in Wehrlein's place after a pre-season injury saw Wehrlein withdraw from the opening two rounds of the season as a precaution.  The C36 made its competitive début at the 2017 Australian Grand Prix, and uses a 2016-specification Ferrari engine.

Toro Rosso STR12: The Toro Rosso STR12 is a Formula One racing car designed and constructed by Scuderia Toro Rosso to compete during the 2017 Formula One season.  The car made its competitive début at the 2017 Australian Grand Prix and is driven by Daniil Kvyat and Carlos Sainz, Jr. Pierre Gasly replaced Kvyat ahead of the 2017 Malaysian Grand Prix.  The STR12 is powered by engines supplied by Renault after the team used 2015-specification Ferrari power units throughout the season; however, the engines were rebadged and the engine and chassis package run under the name 'Toro Rosso'.

Red Bull RB13: The Red Bull RB13 is a Formula One racing car designed and constructed by Red Bull Racing to compete during the 2017 Formula One season.  The car is driven by Daniel Ricciardo and Max Verstappen.  It made its competitive debut at the 2017 Australian Grand Prix.

Renault R.S.17: The Renault R.S.17 is a Formula One racing car designed and constructed by the Renault Sport Formula One Team to compete during the 2017 Formula One season.  The car is driven by Nico Hülkenberg and Jolyon Palmer.  Hülkenberg joined the team after Kevin Magnussen left the team at the end of the season.  It made its competitive début at the 2017 Australian Grand Prix.  Renault R.S.17 was the first car to be fueled by BP and lubricated by Castrol since Marussia MR02 car despite Cosworth had a technical relationship with BP-Castrol.

Question: The Sauber C36 is a Formula One racing car designed and constructed by Sauber to compete during the 2017 Formula One season, the The Sauber C36 is a Formula One racing car designed and constructed by Sauber to compete during the 2017 Formula One season, the car is driven by Marcus Ericsson and who?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "car_name": {
      "type": "string",
      "description": "The name of the Formula One racing car."
    },
    "competition_season": {
      "type": "integer",
      "description": "The Formula One season the car competed in."
    },
    "team_name": {
      "type": "string",
      "description": "The team that designed and constructed the car."
    },
    "drivers": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of drivers for the car during the season."
    },
    "primary_driver_from_question": {
      "type": "string",
      "description": "The driver explicitly mentioned in the question."
    },
    "co_driver_answer": {
      "type": "string",
      "description": "The co-driver of the car, which is the answer to the question."
    }
  },
  "required": [
    "car_name",
    "competition_season",
    "team_name",
    "drivers",
    "primary_driver_from_question",
    "co_driver_answer"
  ],
  "additionalProperties": false
}
