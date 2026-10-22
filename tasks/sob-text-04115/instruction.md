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
Harald Pietschmann: Harald Pietschmann is an automotive designer, 4x4 consultant and journalist.  He designed the Mercedes-Benz GLK-Class for Jim Rogers for a trip around the world.  He is the author of Das große Buch des Jeep Grand Cherokee ISBN  , which is about the Jeep Grand Cherokee and Das grosse Buch der Mercedes M-Klasse ISBN  .

Balkania (trade name): Balkania was the trade name of 'K. Zacharopoulos A.B.E.E.' a Greek industrial and trading company based in Athens that produced 4x4 jeep-type vehicles and 4x4 trucks.  Since 1945, K. Zacharopoulos had been involved in vehicle repair and rebuilding.  The "Balkania" company was founded in 1954 and since 1972 it imported Romanian and Indian vehicles.  In 1975 it designed and introduced its own "Autotractor" model, a 4x4 multi-purpose truck with a Mercedes-Benz 3200 cc Diesel engine, metal cabin and a payload of 1500 kg .  In 1979 the model was redesigned, with a modern synthetic (glass-fiber reinforced composite) cabin.  It was produced, as some similar Greek vehicles, until a change of a favorable categorization for agricultural vehicles in 1984 limited its prospects (see also AutoDiana, Petropoulos).  The vehicle was modestly successful, as it exhibited certain quality problems.

Jeep Liberty: The Jeep Liberty, or Jeep Cherokee (KJ/KK) outside North America, is a compact SUV that was produced by Jeep for the model years 2002–2012.  Introduced as a replacement for the Cherokee (XJ), the Liberty was priced between the Wrangler and Grand Cherokee.  It was the smallest of the 4-door Jeep SUVs until the car based 4-door Compass and Patriot arrived for 2007.  The Liberty featured unibody-construction.  It was assembled at the Toledo North Assembly Plant in the United States, as well as in other countries including Egypt and Venezuela.  The Liberty ceased production on August 16, 2012.  The next generation restored the previous nameplate of Jeep Cherokee that was always used outside of North America.

Jeep Cherokee: The Jeep Cherokee is a line of vehicles sold by Jeep under various vehicle classes.  Originally sold as a variant of the popular Jeep Wagoneer, the Cherokee has evolved from a full-size SUV to one of the first compact SUVs and eventually into its current incarnation as a crossover SUV.  The nameplate has been in continuous use in some form since 1974 and also spawned Jeep's most successful vehicle, the Jeep Grand Cherokee, which was originally slated to be part of the Cherokee's lineup.  The vehicle is named after the Cherokee tribe of Native Americans.

Jeep Wagoneer (SJ): The Jeep Wagoneer is the first luxury 4x4, sold and produced for Jeep through numerous marques from 1963 to 1991.  A "sport utility vehicle" (SUV) for decades before the term was coined, the 4WD Wagoneer saw only minor mechanical changes during its 28-year plus production run, the third longest in U.S. automotive history.

Land Rover Group: Land Rover Group (LRG) was a division of British Leyland (BL) and later the Rover Group that was in existence between 1981 and 1987.  LRG brought British Leyland's light commercial vehicle production under one management, consisting of the Land Rover utility 4x4 range, the Range Rover luxury 4x4 and the former Leyland Sherpa van range (re-branded Freight Rover to match the other group members in 1984).  LRG operated two factories in the Birmingham area- the Solihull plant and the Freight Rover plant at Washwood Heath.

Jeep Cherokee (KL): The Jeep Cherokee (KL) is a mid-size crossover SUV produced by Jeep.  It was introduced for the 2014 model year at the 2013 New York International Auto Show and the sales started in November 2013.  The Cherokee is the first Jeep vehicle to be built on the Fiat Compact/Compact U.S. Wide platform, co-developed by Chrysler and Fiat.  The Jeep Cherokee is built at Belvidere Assembly Plant in Belvidere, Illinois.

Dodge Warlock: The Dodge Warlock, originally a concept vehicle and part of Dodge's late 1970s "adult toys" line, is a wheelbase truck that was produced in limited production in 1976 and regular production from 1977 to 1979.  They were available in 4x2 and 4x4 models.  The 4X4 models were named Power Wagons.  The 1978 models were offered only in black.  There were utiline trucks available in any color.  The warlock only came in black.  Its main draw was that it was a factory customizable truck, also known as a "trick truck", and was designed to appeal to young 4x4 buyers.  The Warlock featured custom wheels, wide tires, bucket seats, a Utiline bed, and oak racks for the bed.  Optional equipment included five-spoke wheels, bucket seats, tinted glass, bright rear bumper, and power steering.  All had black interiors accented by gold tape on the dash and the doors, and a "tuff" steering wheel.  Like the standard pickups, it had front disc brakes, and a standard slant six or a V-8.  The exterior was accented by gold pinstriping around the wheel wells and the body lines.  the pinstriping continued inside onto the doors, dashboard, and instrument panel.  Warlock was printed in gold on the tailgate.  The 1979 model however is different in that it has "Warlock II" printed on the tailgate.  It appears that all normal engine options were available.  It could have come with the standard Slant six, the 318 with either the 2 barrel or 4 barrel carburetor, the 360, the 400, or the 440.  The 318 appears to be the most common engine selected.

Jeep Cherokee (SJ): The SJ series Jeep Cherokee is a full-size SUV that was produced from 1974 through 1983 by Jeep.  It was based on the Wagoneer that was originally designed by Brooks Stevens in 1963.

Jeep Liberty (KJ): The Jeep Liberty (KJ), or Jeep Cherokee (KJ) outside North America, is a compact SUV that was produced by Jeep and designed by Bob Boniface through early 1998.  Introduced in May 2001 for the 2002 model year as a replacement for the Cherokee (XJ), the Liberty was priced between the Wrangler and Grand Cherokee.  It was the smallest of the 4-door Jeep SUVs up until the car platform based 4-door Compass and Patriot arrived for 2007.  The Liberty featured unibody-construction.  It was assembled at the Toledo North Assembly Plant in the United States, as well as in other countries including Egypt and Venezuela.

Question: The Jeep Cherokee’s design was based on what luxury 4x4?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "vehicle_name": {
      "type": "string",
      "description": "The name of the vehicle whose design basis is being queried."
    },
    "design_basis_vehicle": {
      "type": "string",
      "description": "The name of the vehicle that the queried vehicle's design was based on."
    },
    "design_basis_vehicle_type": {
      "type": "string",
      "description": "The type or classification of the design basis vehicle."
    },
    "design_basis_production_start_year": {
      "type": "integer",
      "description": "The start year of production for the design basis vehicle."
    },
    "design_basis_production_end_year": {
      "type": "integer",
      "description": "The end year of production for the design basis vehicle."
    }
  },
  "required": [
    "vehicle_name",
    "design_basis_vehicle",
    "design_basis_vehicle_type",
    "design_basis_production_start_year",
    "design_basis_production_end_year"
  ],
  "additionalProperties": false
}
