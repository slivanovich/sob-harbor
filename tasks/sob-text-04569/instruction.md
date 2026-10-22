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
Obvio! 828: Obvio!  828 is a car made by Obvio! .  The car was originally made by Dacon as Dacon 828.  Dacon was originally the Brazilian representative of Porsche, but when imports were prohibited in 1976 they developed a car of their own.  The name was chosen to remind one of Porsche 928 and the Dacon 828 used rear lights and other Porsche parts for their car.  The Dacon version was only sold between 1983 and July 1994, only 47 cars were sold.  It was then powered by a 1.6 litre VW boxer engine connected to a 4 speed gearbox.

Turbocharged petrol engines: Turbochargers are commonly used in passenger cars to obtain greater power output from a given engine size.  The compact nature of a turbocharger means it is often a more space-efficient solution for increasing power output than increasing engine displacement.  As an example, the turbo Porsche 944's acceleration performance was very similar to that of the larger-engine naturally aspirated Porsche 928.  Although turbocharging is less responsive than supercharging, turbocharging is generally considered more efficient than supercharging.  New techniques such as twin-turbo/biturbo (whether parallel or sequential) setups and twin-scroll turbocharger, in combination with technologies such as variable valve timing and direct fuel injection, have cut down on turbo lag.

Luxury vehicle: Luxury vehicle is a marketing term for a vehicle that provides luxury — pleasant or desirable features beyond strict necessity — at increased expense.

Porsche 968: The Porsche 968 is a sports car made by Porsche AG from 1992 to 1995.  It was the final evolution of a line of water-cooled front-engined rear wheel drive models begun almost 20 years earlier with the 924, taking over the entry-level position in the company lineup from the 944 with which it shared about 20% of its parts.  The 968 was Porsche's last new front-engined vehicle before the introduction of the Cayenne SUV in 2003.

Porsche Cayenne: The Porsche Cayenne (Type 9PA [Designated 955 in online forums, not recognized by Porsche Cars AG]) is a mid-size luxury crossover sport utility vehicle produced by the German manufacturer Porsche since 2002, with North American sales beginning in 2003.  It is the first V8-engined vehicle built by Porsche since 1995, when the Porsche 928 was discontinued.  It is also Porsche's first off road Varient sports car since its Super and Junior tractors of 1950s, and the first Porsche with four doors.  Since 2008, all engines have featured direct injection technology.

Porsche 911 (classic): The original Porsche 911 (pronounced "nine eleven", German: "Neunelfer" ) was a luxury sports car made by Porsche AG of Stuttgart, Germany.  The famous, distinctive, and durable design was introduced in autumn 1963 and built through 1989.  It was succeeded by a modified version, internally referred to as Porsche 964 but still sold as "Porsche 911", as are current models.

Personal luxury car: A personal luxury car is an American car classification describing a highly styled, mass produced, luxury vehicle with an emphasis on image over practicality.  Effectively high priced Veblen goods, personal luxury cars favor style and perceived cachet while accenting the comfort and satisfaction of their owner and driver above all else.  A high level of features and trim is offered, typically at the expense of passenger capacity, cargo room, and fuel economy.  Characteristically built on a two-door platform with distinctive exteriors, they often share mechanical components in common with their manufacturers' popular mass market vehicles.  As a result these vehicles were a profitable segment of the post-World War II automotive marketplace.

Jaguar XJS: The Jaguar XJ-S (later XJS), a luxury grand tourer, was produced by the British manufacturer Jaguar from 1975 to 1996.  The XJ-S superseded the E-Type (also known as XK-E) in September 1975, and was based on the XJ saloon.  It had been developed as the XK-F, though it was very different in character from its predecessor.  Although it never had quite the same sporting image, the XJ-S was a competent grand tourer, and more aerodynamic than the E-Type.  The last XJS was produced on 4 April 1996; by then 115,413 had been produced during a 21-year production life.

Porsche: Dr. Ing.  h.c. F. Porsche AG, usually shortened to Porsche AG (] ), is a German automobile manufacturer specializing in high-performance sports cars, SUVs and sedans.  Porsche AG is headquartered in Stuttgart, and is owned by Volkswagen AG, which is itself majority-owned by Porsche Automobil Holding SE.  Porsche's current lineup includes the 718 Boxster/Cayman, 911, Panamera, Macan and Cayenne.

Porsche 928: The Porsche 928 is a luxurious grand tourer produced by Porsche AG of Germany from 1978 to 1995.  Originally intended to replace the company's well-known and famed 911, the 928 combined the power, poise, and handling of a sports car with the refinement, comfort, and equipment of a luxurious saloon to create what some Porsche executives thought would be a vehicle with wider appeal than the compact, quirky and sometimes difficult 911.

Question: The Porsche 928 is a luxurious grand tourer produced by Porsche AG of which country, from 1978 to 1995, the 928 combined the power, poise, and handling of a sports car with the refinement, comfort, and equipment of a luxurious saloon, luxury vehicle is a marketing term for a vehicle that provides luxury — pleasant or desirable features beyond strict necessity — at increased expense?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "car_model": {
      "type": "string",
      "description": "The specific model of the car."
    },
    "manufacturer": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the manufacturing company."
        },
        "country_of_origin": {
          "type": "string",
          "description": "The country where the manufacturer is based."
        }
      },
      "required": [
        "name",
        "country_of_origin"
      ],
      "additionalProperties": false
    },
    "vehicle_type": {
      "type": "string",
      "description": "The classification of the vehicle."
    },
    "production_period": {
      "type": "object",
      "properties": {
        "start_year": {
          "type": "integer",
          "description": "The year production started."
        },
        "end_year": {
          "type": "integer",
          "description": "The year production ended."
        }
      },
      "required": [
        "start_year",
        "end_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "car_model",
    "manufacturer",
    "vehicle_type",
    "production_period"
  ],
  "additionalProperties": false
}
