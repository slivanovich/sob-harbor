{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDrop Tower: Scream Zone: Drop Tower: Scream Zone, formerly known as Drop Zone: Stunt Tower, is the name of five drop tower thrill rides of varying sizes featured at five different Cedar Fair amusement parks in the United States and Canada.\n\nGuardians of the Galaxy – Mission: Breakout!: \"Guardians of the Galaxy\" – Mission: BREAKOUT!  is an accelerated drop tower dark ride attraction at Disney California Adventure.  Based on Marvel's \"Guardians of the Galaxy\" film series, the attraction depicts Rocket Raccoon recruiting guests to attempt to free the remaining Guardians of the Galaxy from display within the Collector's fortress.\n\nTower of Terror II: The Tower of Terror II is a steel shuttle roller coaster located at the Dreamworld amusement park on the Gold Coast, Queensland, Australia.  When the Tower of Terror opened on 23 January 1997, it was the first roller coaster in the world to reach 160.9 km/h speeds making it the tallest and fastest roller coaster in the world of its time.  The ride is situated on the Dreamworld Tower which also houses The Giant Drop free fall ride.  The ride was originally known as the \"Tower of Terror\" until it was modified and relaunched in September 2010.\n\nFalcon's Fury: Falcon's Fury is a free-standing Sky Jump drop tower attraction at the Busch Gardens Tampa amusement park in Tampa, Florida, United States.  Manufactured by Intaride (a subsidiary of Intamin), the ride reaches a maximum height of 335 ft making it North America's tallest free-standing drop tower.  Riders experience about five seconds of free fall, reaching a speed of 60 mph .  The ride's name was chosen to invoke a falcon's ability to dive steeply at high speed to capture prey.\n\nTower of Terror (film): Tower of Terror is a 1997 made-for-TV supernatural thriller directed by D. J. MacHale.  It is based on the theme park attraction, The Twilight Zone Tower of Terror, at Disney's Hollywood Studios at the Walt Disney World Resort in Bay Lake, Florida and was originally a presentation of \"The Wonderful World of Disney\".  It is also Disney's first film based on an attraction at one of its theme parks, and the only adaptation to be made for television.\n\nZumanjaro: Drop of Doom: Zumanjaro: Drop of Doom is a drop tower operating at the Six Flags Great Adventure amusement park in Jackson Township, New Jersey.  At 415 ft tall, the ride is attached to the existing Kingda Ka roller coaster and stands as the world's tallest drop tower.\n\nThe Twilight Zone Tower of Terror: \"The Twilight Zone\" Tower of Terror, also known as Tower of Terror, is an accelerated drop tower dark ride located at Disney's Hollywood Studios, Tokyo DisneySea, Walt Disney Studios Park, and formerly located at Disney California Adventure Park.  Except for the Tokyo DisneySea version, the attractions are inspired by Rod Serling's anthology television series, \"The Twilight Zone\", and take place in the fictional Hollywood Tower Hotel in Hollywood, California.  The Tokyo version, which features an original story line not related to \"The Twilight Zone\", takes place in the fictional Hotel Hightower.  All three versions place riders in a seemingly ordinary hotel elevator, and present the riders with a fictional backstory in which people have mysteriously disappeared from the elevator under the influence of some supernatural element many years prior.\n\nNemesis: Sub-Terra: Nemesis Sub-Terra is a drop tower dark ride at Alton Towers theme park.  The ride opened to the public on 24 March 2012.  The ride has not been operating since June 2015 however it is still standing and listed on the Alton Towers website and it is currently unknown whether it will ever be in operation again.\n\nThe Giant Drop: The Giant Drop is an Intamin drop tower ride located at the Dreamworld theme park on the Gold Coast, Australia.  The ride was added in December 1998 to the existing Dreamworld Tower which housed the Tower of Terror.  For fourteen years, The Giant Drop held the record for the tallest drop tower in the world.\n\nPitt Fall: Pitt Fall was a drop tower ride located at Kennywood amusement park in the Pittsburgh suburb of West Mifflin, Pennsylvania.  The ride was the first one at Kennywood to be manufactured by Intamin.  It was themed after a Pitfall trap , but spelled with two \"t\"'s as in an abbreviation of Pittsburgh.  When it opened in 1997, it was the tallest drop tower in the world.\n\nQuestion: Tower of Terror is a 1997 made-for-TV supernatural thriller, it's based on which accelerated drop tower dark ride?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"film_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"film_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the film.\"\n    },\n    \"based_on_attraction\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"attraction_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the theme park attraction the film is based on.\"\n        },\n        \"attraction_type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of the attraction.\"\n        }\n      },\n      \"required\": [\n        \"attraction_name\",\n        \"attraction_type\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"film_year\",\n    \"film_genre\",\n    \"based_on_attraction\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "film_year": {
        "type": "integer",
        "description": "The release year of the film."
      },
      "film_genre": {
        "type": "string",
        "description": "The genre of the film."
      },
      "based_on_attraction": {
        "type": "object",
        "properties": {
          "attraction_name": {
            "type": "string",
            "description": "The name of the theme park attraction the film is based on."
          },
          "attraction_type": {
            "type": "string",
            "description": "The type of the attraction."
          }
        },
        "required": [
          "attraction_name",
          "attraction_type"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_title",
      "film_year",
      "film_genre",
      "based_on_attraction"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
