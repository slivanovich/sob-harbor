{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\n4-Track Demos: 4-Track Demos is an album of demos by British singer-songwriter PJ Harvey.  It was released in October 1993 by Island Records.  It consists of 8 demos of songs from her previous album, \"Rid of Me\", along with 6 demos of some unreleased tracks which never made it to release with the three-piece PJ Harvey line-up.  According to interviews with Harvey, all fourteen of these songs were written and demoed at her home between mid-1991 and autumn 1992.  \"4-Track Demos\" was Harvey's first self-produced album, a job she would not take on again until 2004's \"Uh Huh Her\".\n\nCake Like: Cake Like was an all-female indie rock band based in New York City.  Its members were bassist and lead singer Kerri Kenney, drummer Jody Seifert, and vocalist and guitarist Nina Hellman.  The band came together in 1993 when Kenney and Hellman met at New York University's Experimental Theater Wing, decided to form a band, and were joined by Hellman's roommate Seifert.  The members had never played music before and so developed their own unique style.  Their songs often play out like poetry set to erratic guitar-rock.  They soon attracted the attention of John Zorn, who signed the band to his Avant Records label, which released their first LP.  Ric Ocasek, formerly of The Cars, produced their follow-up EP.  Subsequently, Neil Young signed the band to his Vapor Records label, which released their second and third LPs.\n\nHandball (school): School students in Australia, New Zealand and Fiji often play a style of handball (Also known as four square or - square, with the number in the latter determined by the number of players) that is different from nearly all other types of handball.  The game is played at recess, lunch or before and after school.  It can also be played at home or anywhere that has a hard surface and at least one line.  It has quick set-up time and simple rules, contributing to its popularity.\n\nFootball pitch: A football pitch (also known as a football field or soccer field) is the playing surface for the game of association football.  its dimensions and markings are defined by Law 1 of the Laws of the Game, \"The Field of Play\".  The surface can be either natural or artificial, but FIFA's Laws of the Game specify that all artificial surfaces must be painted green.  The pitch is typically made of turf (grass) or artificial turf, although amateur and recreational teams often play on dirt fields.\n\nRoblox: Roblox is a user-generated massively multiplayer online social gaming platform developed and published by the Roblox Corporation and released in 2006; the first demos of the game were tested in 2004 under the name \"DynaBlocks\".\n\nVG Cats: VG Cats (short for \"Video Game Cats\") is a webcomic written and drawn by Canadian cartoonist Scott Ramsoomair.  Published on its own website, it features the adventures of a pair of anthropomorphic cats, who often play the roles of characters in popular video games that are parodied in the strip.  Strips are usually presented in a large format and in full color.  The author generally set Mondays as days for updating the comic; however, the update schedule has a reputation of being incredibly sporadic; he frequently mocks his tardiness in updating in various strips due to personal reasons and frequent convention appearances.  As of October 2016, the site had approximately 369 comics listed in its main archives.  Based on this archive alone, \"VG Cats\" averaged 25 comics a year while it was at its peak.\n\nHolychild: Holychild (stylized as HOLYCHILD) is an American indie pop duo from Los Angeles, California, United States.  The band consists of songwriter and vocalist Liz Nistico and producer and multi-instrumentalist Louie Diller, though they often play with more musicians for their live show.  The band signed to Glassnote Records in 2013, and define their genre as \"brat pop\".  Holychild released an EP entitled \"Mindspeak\" in 2014 and their full-length debut album \"The Shape of Brat Pop to Come\" was released in June 2015.  \"America Oil Lamb\", a followup EP of collaboration songs was released in June 2016.\n\nODers: ODers or online daters are people who take part in dating in online video games.  This occurs and is addressed frequently in games such as Roblox, and Habbo Hotel.  Many use the term within memes.\n\nNative Nod: Native Nod was a groundbreaking emotive hardcore band formed in the early '90s based in the New York / New Jersey area where the group would often play shows.  The band is often credited with giving rise to the emo scene, and at very young ages (high school).  In their short lifetime as a band they only released 9 songs, divided amongst the 3 seven inch EPs \"Bread\", \"Answers\", and \"Lower GI Bleed\".  These 9 songs can be found on the Gern Blandsten Records discography \"Today Puberty, Tomorrow The World\".\n\nPeter (actor): Shinnosuke Ikehata (池畑 慎之介 , Ikehata Shinnosuke ) (born August 8, 1952 in Sakai, Osaka, Japan) is a Japanese singer, dancer and actor who has appeared in Akira Kurosawa's \"Ran\" and Toshio Matsumoto's \"Bara no Sōretsu\".  Ikehata also uses his stage name of Peter (ピーター , Pītā ) when he appears on TV variety shows and musical revues.  Always seen dancing with tight shirts and pants at dancing clubs, he adopted the stage name when he was 16 after his style of dress and dance which was said to resemble Peter Pan.  One of Japan's most famous gay entertainers, Peter's androgynous appearance has enabled him to often play transvestite characters and he often appears on stage in women's clothing.\n\nQuestion: What is the name of the game that ODers often play, released in 2006 and first demoed in 2004?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"game_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the game.\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the game was released.\"\n        },\n        \"first_demo_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the game was first demoed.\"\n        },\n        \"original_demo_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name under which the game was originally demoed.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"release_year\",\n        \"first_demo_year\",\n        \"original_demo_name\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"player_group_association\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"group_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the player group.\"\n        },\n        \"plays_game\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the player group often plays this game.\"\n        }\n      },\n      \"required\": [\n        \"group_name\",\n        \"plays_game\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"final_answer\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the game that matches all criteria.\"\n    }\n  },\n  \"required\": [\n    \"game_details\",\n    \"player_group_association\",\n    \"final_answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "game_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the game."
          },
          "release_year": {
            "type": "integer",
            "description": "The year the game was released."
          },
          "first_demo_year": {
            "type": "integer",
            "description": "The year the game was first demoed."
          },
          "original_demo_name": {
            "type": "string",
            "description": "The name under which the game was originally demoed."
          }
        },
        "required": [
          "name",
          "release_year",
          "first_demo_year",
          "original_demo_name"
        ],
        "additionalProperties": false
      },
      "player_group_association": {
        "type": "object",
        "properties": {
          "group_name": {
            "type": "string",
            "description": "The name of the player group."
          },
          "plays_game": {
            "type": "boolean",
            "description": "Indicates if the player group often plays this game."
          }
        },
        "required": [
          "group_name",
          "plays_game"
        ],
        "additionalProperties": false
      },
      "final_answer": {
        "type": "string",
        "description": "The name of the game that matches all criteria."
      }
    },
    "required": [
      "game_details",
      "player_group_association",
      "final_answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
