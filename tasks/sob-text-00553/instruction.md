{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPj Perez: Pj Perez (born August 4, 1976) is an American editor, writer and musician, best known for his reports and commentary on Las Vegas culture in such publications as \"Rolling Stone\".  Perez was the founding managing editor of Las Vegas-based \"Racket Magazine\".\n\nNevada Power Company: Nevada Power Company was a Las Vegas-based company that produced, distributed, and sold electricity in the southern part of the state of Nevada.  In 2005, it had over 700,000 electric customers in parts of three Nevada counties — a service area of more than 4000 sqmi .  In 1998, Nevada Power merged with Nevada's other major utility, Sierra Pacific Resources.  It continued as a subsidiary of Sierra Pacific until 2005, when the company changed its name to NV Energy.\n\nDiamond Jo Casino: The Diamond Jo Casino is a gambling casino and entertainment complex located in the Port of Dubuque, in Dubuque, Iowa.  The casino is owned and operated by Las Vegas-based Boyd Gaming, which also owns the Diamond Jo Casino - Worth in Northwood, Iowa.  It is a member of the Iowa Gaming Association, and its license is held by the Dubuque Racing Association, which operates Q Casino.  Beginning operations on May 18, 1994, the Diamond Jo was a 3-level, 305 ft , 1,500-passenger vessel in Dubuque's Ice Harbor.  The boat was a dockside that did not cruise, the casino became land-based when its new facility opened December 11, 2008.\n\nJack Zwerner: Jack 'Action' Zwerner (born June 12, 1938) is an American professional poker player and business entrepreneur.  He is most known for founding land based casinos, gaming in international waters, and shaping the casino world as it is today.  He is also known for winning the 2006 World Series of Poker (WSOP) Event 8: Omaha Hi-Lo (8 or better).  T. J. Cloutier regards hims as the best heads-up Omaha player ever.\n\nHeavens Cafe: Heavens Cafe is a rock opera written and composed by John Miner.  It was first staged in Las Vegas, Nevada, in 1996.  The opportunity to perform the musical theater project came after Miner's demo was heard by investor Mike Lewis of Las Vegas-based Tributary Music Label after his departure from California-based progressive rock group Mantra Sunrise.  Miner established a new band, named \"Art Rock Circus\" with drummer Jon Weisberg and bassist Jon Cornell to stage the live performances at the Flamingo Theater in Las Vegas.  Former Follies Bergere performer Kristine Keppel directed the original casting.  In 2003, Los Angeles based theater director John Beane approached Miner about staging the opera in the Los Angeles area later that year.  Beane's new vision for the project came to fruition in May 2004 with a six-week California run at the Insurgo Theater which included Ken Jaquess on bass and Nolan Stolz on drums.\n\nBrian Rouff: Brian Rouff (born 1955) is an American author, freelance journalist and advertising executive, best known for his Las Vegas-based novels: Dice Angel (2002), Money Shot (2004) and The House Always Wins (to be released in October 2017) as well as his chapter in the Las Vegas collaborative serial mystery Restless City (2009).  He is the son of Morris Rouff, inventor of Formula 409.\n\nRawVegas.tv: RawVegas.tv is a defunct video website.  RawVegas was first launched on January 19, 2007 and is the first venture for Raw Networks LLC, a Las Vegas-based Internet television studio that creates and produces short form video content exclusively for the Internet.  Programming on RawVegas.tv includes a daily mix of content that focuses on Las Vegas, including a daily news show, review shows designed to inform both locals and visitors, regular red carpet interviews, a celebrity gossip beat, a number of comedy programs, wagering shows, a slate of reality series starring Las Vegas personalities and poker players and other programs that display life in Las Vegas.\n\nJake Records: Jake Records is a Las Vegas-based independent record label.\n\nWorld Series of Poker: The World Series of Poker (WSOP) is a series of poker tournaments held annually in Las Vegas and, since 2005, sponsored by Caesars Entertainment Corporation (known as Harrah's Entertainment until 2010).  It dates its origins to 1970, when Benny Binion invited seven of the best-known poker players to the Horseshoe Casino for a single tournament, with a set start and stop time, and a winner determined by a secret ballot of the seven players.\n\nZoltan Bathory: Zoltán Báthory, (born May 15, 1978) is a Hungarian-born musician and martial artist.  He is the founder, rhythm guitarist, and one of the main songwriters, for the Las Vegas-based multi-million record selling heavy metal band Five Finger Death Punch.  In 2010, he was named Golden God's \"Best Shredder\" by Metal Hammer Magazine.  Zoltan is also a founding board member of the veterans non profit Home Deployment Project in Las Vegas.  Home Deployment Project works to save and reintegrate homeless veterans.\n\nQuestion: Jack Zwerner won an event at which Las Vegas-based set of tournaments?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"winner_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person who won the event.\"\n    },\n    \"tournament_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the tournament series.\"\n    },\n    \"event_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the event was won.\"\n        },\n        \"event_number\": {\n          \"type\": \"string\",\n          \"description\": \"The specific event number or identifier.\"\n        },\n        \"game_type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of game played in the event.\"\n        }\n      },\n      \"required\": [\n        \"year\",\n        \"event_number\",\n        \"game_type\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"tournament_location\": {\n      \"type\": \"string\",\n      \"description\": \"The primary city where the tournament is held.\"\n    },\n    \"is_las_vegas_based\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the tournament is based in Las Vegas.\"\n    }\n  },\n  \"required\": [\n    \"winner_name\",\n    \"tournament_name\",\n    \"event_details\",\n    \"tournament_location\",\n    \"is_las_vegas_based\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "winner_name": {
        "type": "string",
        "description": "The name of the person who won the event."
      },
      "tournament_name": {
        "type": "string",
        "description": "The name of the tournament series."
      },
      "event_details": {
        "type": "object",
        "properties": {
          "year": {
            "type": "integer",
            "description": "The year the event was won."
          },
          "event_number": {
            "type": "string",
            "description": "The specific event number or identifier."
          },
          "game_type": {
            "type": "string",
            "description": "The type of game played in the event."
          }
        },
        "required": [
          "year",
          "event_number",
          "game_type"
        ],
        "additionalProperties": false
      },
      "tournament_location": {
        "type": "string",
        "description": "The primary city where the tournament is held."
      },
      "is_las_vegas_based": {
        "type": "boolean",
        "description": "Indicates if the tournament is based in Las Vegas."
      }
    },
    "required": [
      "winner_name",
      "tournament_name",
      "event_details",
      "tournament_location",
      "is_las_vegas_based"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
