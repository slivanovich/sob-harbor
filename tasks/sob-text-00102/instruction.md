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
Perth SuperSprint: The Perth SuperSprint is an annual motor racing event for Supercars, held at Barbagallo Raceway in Wanneroo, Western Australia.  The event has been a regular part of the Supercars Championship—and its previous incarnations, the Australian Touring Car Championship, Shell Championship Series and V8 Supercars Championship—since 1973.

Sydney 500: The Sydney 500 (formally known as the Coates Hire Sydney 500) was an annual motor racing event for Supercars, held at the Homebush Street Circuit in Sydney Olympic Park, New South Wales, Australia.  The event was a regular part of the Supercars Championship—and its previous iteration, the V8 Supercars Championship—between 2009, and 2016, being the final event on the calendar each year.

2016 Coates Hire Sydney 500: The 2016 Coates Hire Sydney 500 was a motor racing event for the Supercars Championship held on the weekend of 2 to 4 December 2016.  The event was held at the Homebush Street Circuit in Sydney Olympic Park, New South Wales, and consisted of two races of 250 kilometres in length.  It was the final round of the 2016 International V8 Supercars Championship, and the final time that the venue hosted a Supercar race, being replaced by the Newcastle Street Circuit from 2017 onwards.

Tasmania SuperSprint: The Tasmania SuperSprint (formally known as the Tyrepower Tasmania SuperSprint) is an annual motor racing event for Supercars, held at Symmons Plains Raceway in Launceston, Tasmania.  The event has been a regular part of the Supercars Championship—and its previous incarnations, the Australian Touring Car Championship, Shell Championship Series and V8 Supercars Championship—since 1969.

Darwin Triple Crown: The Darwin Triple Crown, formally known as the CrownBet Darwin Triple Crown, is an annual motor racing event for Supercars, held at Hidden Valley Raceway in Darwin, Northern Territory.  The event has been a regular part of the Supercars Championship—and its previous incarnations, the Australian Touring Car Championship, Shell Championship Series and V8 Supercars Championship—since 1998.

Winton SuperSprint: The Winton SuperSprint (formally known as the Woodstock Winton SuperSprint) is an annual motor racing event for Supercars, held at Winton Motor Raceway in Winton, Victoria.  The event has been a regular part of the Supercars Championship—and its previous incarnations, the Australian Touring Car Championship, Shell Championship Series and V8 Supercars Championship—since 1985.

2016 International V8 Supercars Championship: The 2016 International V8 Supercars Championship (often simplified to the 2016 V8 Supercars Championship and known from 1 July as the 2016 Virgin Australia Supercars Championship) is an FIA-sanctioned international motor racing series for Supercars.  It is the eighteenth running of the Supercars Championship and the twentieth series in which Supercars have contested the premier Australian touring car title.

Supercars Championship: The Supercars Championship (known as the Virgin Australia Supercars Championship for sponsorship purposes and often shortened to just Supercars or its long-standing name V8 Supercars) is a touring car racing category based in Australia and run as an International Series under Fédération Internationale de l'Automobile (FIA) regulations.

Newcastle 500: The Newcastle 500 (formally known as the Coates Hire Newcastle 500) will be a motor racing event for Supercars that will be held at the Newcastle Street Circuit in Newcastle, New South Wales starting in 2017.

2017 Supercars Championship: The 2017 Supercars Championship (formally known as the 2017 Virgin Australia Supercars Championship) is a FIA-sanctioned international motor racing series for Supercars, which prior to July 2016 had been known as V8 Supercars.  It is the nineteenth running of the Supercars Championship and the twenty-first series Supercars have contested the premier Australian touring car title.  Shane van Gisbergen started the season as the defending drivers' champion with his team, Triple Eight Race Engineering, defending teams' champions.  After seven rounds, Scott McLaughlin leads the Drivers' Championship ahead of Jamie Whincup and Fabian Coulthard.  In the Teams' Championship, DJR Team Penske lead Triple Eight Race Engineering with Prodrive Racing Australia in third.

Question: While the Newcastle 500 is a motor racing event for Supercars, the Supercars Championship is what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "entity_name": {
      "type": "string",
      "description": "The formal name of the entity being described."
    },
    "category_type": {
      "type": "string",
      "description": "The type of racing category."
    },
    "base_location": {
      "type": "string",
      "description": "The country where the racing category is based."
    },
    "governing_body": {
      "type": "string",
      "description": "The international body that regulates the series."
    },
    "is_international_series": {
      "type": "boolean",
      "description": "Indicates if the series is run as an International Series."
    }
  },
  "required": [
    "entity_name",
    "category_type",
    "base_location",
    "governing_body",
    "is_international_series"
  ],
  "additionalProperties": false
}
