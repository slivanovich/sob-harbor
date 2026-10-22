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
BMW 6 Series (F06/F12/F13): The BMW F06/F12/F13 is the third generation of the BMW 6 Series range of grand tourers, and was launched in late 2011 as the successor to the BMW E63/E64 6 Series.  The body styles of the range are:

BMW M3: The BMW M3 is a high-performance version of the BMW 3 Series, developed by BMW in-house motorsport division, BMW M GmbH.  M3 models have been derived from the E30, E36, E46, E90/E92/E93 and F80.

BMW M6: The BMW M6 is a high-performance version of the 6 Series coupe/convertible, designed by the motorsport division of BMW.  The BMW M6 was produced from 1983–1989, 2005–2010 and 2012–present.

Cadillac CTS-V: The Cadillac CTS-V is a high-performance version of the Cadillac CTS.  The CTS-V series includes three body styles, all of which feature a pushrod OHV V-8 engine and a sport-tuned suspension.  The four-door CTS-V sedan was introduced in 2004, and the CTS-V sport wagon and coupe were introduced in 2010 for the 2011 model year.  The sedan competes in the North American consumer market against other high-performance luxury sedans and "echoes" their quality but is a more affordable option than competitors as the Audi RS6, BMW M5, and Mercedes E63 AMG.

BMW M4: The BMW M4 is a high-performance version of the BMW 4 Series automobile developed by BMW's motorsport division, the BMW M GmbH.  Part of the renumbering that splits the 3 Series coupe and convertible models to the 4 Series (to further differentiate it from the 3 Series), the M4 replaced the M3 Coupe and Convertible models.  Upgrades over the standard BMW 4-Series include: a very powerful and responsive, twin turbocharged engine; improved handling, suspension, and braking systems; aerodynamic body enhancements; interior/exterior accents with the tri-colour "M" (Motorsport) badging; the significantly reduced weight compared to the standard 4 series and its predecessor with an all-new stiffer chassis and extensive use of carbon fiber, especially the roof of the car.

BMW Z9: The BMW Z9 (or Z9 Gran Turismo, Z9 GT) is a four-seat coupe concept car, carbon-fiber skin over an aluminum space frame.  It was introduced on September in 1999 at the Frankfurt Auto Show.  During the 2000 Paris Auto Show a convertible variant of the Z9 was debuted.  It was designed by Chris Bangle, who was promoted to Director of BMW Group Design.  Much of the styling found on E63 6 series is derived from the Z9.

BMW 8 Series: The BMW 8 Series is a Grand Tourer built by BMW from 1989 to 1999 powered by either a V8 or V12 engine.  While it did supplant the original E24 based 6 Series in 1991, a common misconception is that the 8 Series was developed as a successor.  It was actually in an entirely new model class aimed at a different market, with a substantially higher price and performance than the 6 Series.  In 1999, BMW discontinued the 8 Series because of low demand and sales.  However, in 2017, BMW announced a new generation to be available from 2018 and previewed it with the BMW Concept 8 Series.  BMW also confirmed that the second generation will get an M version.

BMW M Coupe: The BMW M Coupe is a shooting-brake styled high-performance automobile produced by BMW.  Only two generations of the M Coupe have been manufactured, the original E36/8 Z3 Coupe and the second generation E86 Z4 Coupe.

Moscow BMW billboard: The Moscow BMW billboard was unveiled in 2008 as one of the largest and most elaborate billboards in the world.  The billboard had an area of 1.5 acres and depicted an expressway, containing real, full-sized BMWs.  At night, the headlights of the cars are lit up.  The car models on the billboard were the BMW M Coupe, the BMW M3, the BMW M5, and BMW M6.

Nader Faghihzadeh: Nader Faghihzadeh (Persian: نادر فقیه‌زاده‎ ‎ , born 1976 in Tehran) is an Iranian-German Automobile Designer based in Munich.  He is a Car Designer at BMW Design and was responsible for the Interior Design of the BMW 7 Series (F01/F02), the Exterior Design of the BMW 6 Series Gran Coupé, Coupé and Convertible (F06/F12/F13) and the Exterior Design of the BMW 7 series (G11/G12).

Question: What is the name of this high-performance version of the 6 series coupe/ convertible, which appeared on the Moscow BMW billboard?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "car_name": {
      "type": "string",
      "description": "The name of the high-performance car model."
    },
    "is_high_performance_version": {
      "type": "boolean",
      "description": "Indicates if the car is a high-performance version of a base series."
    },
    "base_series": {
      "type": "string",
      "description": "The name of the base car series this model is derived from."
    },
    "body_styles": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The body styles available for this high-performance version."
    },
    "appeared_on_moscow_billboard": {
      "type": "boolean",
      "description": "Indicates if the car model appeared on the Moscow BMW billboard."
    },
    "production_periods": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "start_year": {
            "type": "integer",
            "description": "The start year of a production period."
          },
          "end_year": {
            "type": "integer",
            "description": "The end year of a production period. Omitted if production is ongoing."
          }
        },
        "required": [
          "start_year"
        ],
        "additionalProperties": false
      },
      "description": "A list of production periods for the car model."
    }
  },
  "required": [
    "car_name",
    "is_high_performance_version",
    "base_series",
    "body_styles",
    "appeared_on_moscow_billboard",
    "production_periods"
  ],
  "additionalProperties": false
}
