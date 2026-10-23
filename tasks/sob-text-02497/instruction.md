{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nForti: Forti Corse, commonly known as Forti, was an Italian motor racing team chiefly known for its brief and unsuccessful involvement in Formula One in the mid-1990s.  It was established in the late 1970s and competed in lower formulae for two decades.  The team's successes during this period included four Drivers' Championships in Italian Formula Three during the 1980s, and race wins in the International Formula 3000 championship, in which it competed from 1987 to 1994.  From 1992, team co-founder Guido Forti developed a relationship with the wealthy Brazilian businessman Abílio dos Santos Diniz that gave Diniz's racing driver son, Pedro, a permanent seat in the team and the outfit a sufficiently high budget to consider entering Formula One.\n\n2014 FIA Formula One World Championship: The 2014 FIA Formula One World Championship was the 68th season of FIA Formula One motor racing.  It featured the 2014 Formula One World Championship, a motor racing championship for Formula One cars, recognised by the sport's governing body, the Fédération Internationale de l'Automobile (FIA), as the highest class of competition for open-wheel racing cars.  The season started in Australia on 16 March and concluded in Abu Dhabi on 23 November.  In the nineteen Grands Prix of the season, a total of eleven teams and twenty-four drivers competed for the World Drivers' and World Constructors' championships.  It was the first Formula One season since to see an accident with ultimately fatal consequences as Jules Bianchi succumbed to the injuries he sustained during the 2014 Japanese Grand Prix.  He died on 17 July 2015 after spending nine months in a coma following the accident.\n\nMaserati in motorsport: Throughout its history, the Italian auto manufacturer Maserati has participated in various forms of motorsports including Formula One, sportscar racing and touring car racing, both as a works team and through private entrants.\n\nCache inclusion policy: Multi-level caches can be designed in various ways depending on whether the content of one cache is present in other level of caches.  If all blocks in the higher level cache are also present in the lower level cache, then the lower level cache is said to be inclusive of the higher level cache.  If the lower level cache contains blocks that are not present in the higher level cache, then the lower level cache is said to be exclusive of the higher level cache.  If the contents of the lower level cache are neither strictly inclusive nor exclusive of the higher level cache, then it is called non-inclusive non-exclusive (NINE) cache.\n\nItalian F4 Championship: Italian Formula 4 Championship is the first formula racing series regulated according to FIA Formula 4 regulations.  The inaugural season was the 2014 Formula 4 Italian Championship, effectively replacing the Formula Abarth.\n\nFédération Internationale de l'Automobile: The Fédération Internationale de l'Automobile (FIA, English: International Automobile Federation) is an association established as the Association Internationale des Automobile Clubs Reconnus (AIACR, English: 'International Association of Recognized Automobile Clubs') on 20 June 1904 to represent the interests of motoring organisations and motor car users.  To the general public, the FIA is mostly known as the governing body for many auto racing events.  The FIA also promotes road safety around the world.\n\nEuropean Formula Two Championship: The European Formula Two Championship was a Formula Two motor racing series that was held between 1967–84.  The races were held across Europe, and were contested both by drivers aiming to compete in Formula One in the future as well as current Formula One drivers wishing to practice.  The series was sanctioned by the FIA, motorsports world governing body.\n\n2017–18 Formula 4 UAE Championship: The 2017-18 Formula 4 UAE Championship will be the second season of the Formula 4 UAE Championship, a motor racing series for the United Arab Emirates regulated according to FIA Formula 4 regulations, and organised and promoted by the Automobile & Touring Club of the UAE (ATCUAE) and AUH Motorsports.\n\n2016–17 Formula 4 UAE Championship: The 2016-17 Formula 4 UAE Championship will be the inaugural season of the Formula 4 UAE Championship, a motor racing series for the United Arab Emirates regulated according to FIA Formula 4 regulations, and organised and promoted by the Automobile & Touring Club of the UAE (ATCUAE) and AUH Motorsports.\n\nFIA Global Pathway: The FIA Global Pathway from Karting to Formula One is a program developed by the Fédération Internationale de l'Automobile (FIA), the international sanctioning body for motorsports that is designed to assist racing drivers progress from karting to Formula One.  The program was first developed in 2014 with the creation of the Formula 4 category, and follows a tiered structure, with drivers racing in increasingly-powerful cars.  The Global Pathway represents the consolidation of feeder series to create a more linear approach to progressing into Formula One.\n\nQuestion: What is the full title of the governing body for Formula One and lower level of national motorsports including Italian Formula 4?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"governing_body_full_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full official name of the governing body.\"\n    },\n    \"abbreviation\": {\n      \"type\": \"string\",\n      \"description\": \"The common abbreviation for the governing body.\"\n    },\n    \"english_name\": {\n      \"type\": \"string\",\n      \"description\": \"The English translation of the governing body's name.\"\n    },\n    \"governed_series_examples\": {\n      \"type\": \"array\",\n      \"description\": \"Examples of motor racing series governed or regulated by this body.\",\n      \"items\": {\n        \"type\": \"string\"\n      }\n    }\n  },\n  \"required\": [\n    \"governing_body_full_name\",\n    \"abbreviation\",\n    \"english_name\",\n    \"governed_series_examples\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "governing_body_full_name": {
        "type": "string",
        "description": "The full official name of the governing body."
      },
      "abbreviation": {
        "type": "string",
        "description": "The common abbreviation for the governing body."
      },
      "english_name": {
        "type": "string",
        "description": "The English translation of the governing body's name."
      },
      "governed_series_examples": {
        "type": "array",
        "description": "Examples of motor racing series governed or regulated by this body.",
        "items": {
          "type": "string"
        }
      }
    },
    "required": [
      "governing_body_full_name",
      "abbreviation",
      "english_name",
      "governed_series_examples"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
