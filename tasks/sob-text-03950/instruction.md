{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMega Man Zero 4: Mega Man Zero 4, known in Japan as Rockman Zero 4 (ロックマンゼロ4, , Rokkuman Zero Fō ) , is a video game developed by Inti Creates and Natsume and published in 2005 by Capcom for the Game Boy Advance (GBA) handheld.  It is the fourth and final title in the \"Mega Man Zero\" subseries of the \"Mega Man\" franchise and is set several months after the events of \"Mega Man Zero 3\".  The game deals with Dr. Weil's reign over Neo Arcadia in which humans, who have been reduced to second-rate citizens, begin to escape in large numbers to the last-known livable location on the planet, Area Zero, beginning a conflict between the two groups.  The effects of this war eventually drive Zero and the Resistance to protect Area Zero and its inhabitants from Dr. Weil.\n\nCho Aniki Zero: Cho Aniki Zero (零・超兄貴 , \"Zero Chō Aniki\" , lit.  \"Zero Super Big Brother\") is a horizontally scrolling shoot 'em up, the latest game in the \"Cho Aniki\" series.  It was published in Japan by GungHo Works on 19 March 2009 for the PlayStation Portable.  The game was published in North America by Aksys Games on 25 March 2010 as a digital download exclusive for the PSP, with the full title of \"Cho Aniki Zero: Muscle Brothers\".  This makes it the second \"Cho Aniki\" title to be released in North America, following the Virtual Console port of the original game.  It is the first \"Cho Aniki\" title developed by extreme Co., Ltd., who had obtained the rights of original developers NCS Corp. and Masaya products.  The graphics followed the 3D appearance of the PS2 game.\n\nZork Nemesis: Zork Nemesis: The Forbidden Lands is a 1996 graphic adventure game, developed by Zombie LLC and published by Activision.  It is the eleventh game in the \"Zork\" series, and the first such title not to appear under the Infocom label.  It features a darker, less comical story within the Zork setting.  The story focuses on players investigating the sudden disappearance of four prominent figures and their children to the hands of a mysterious being known as the \"Nemesis\", and uncovering a sinister plot during their investigations that they must thwart.  The game was released for Windows 95, and ported to MS-DOS and Macintosh by Quicksilver Software.\n\nEnchanter (video game): Enchanter is a 1983 interactive fiction computer game written by Marc Blank and Dave Lebling and published by Infocom.  It belongs to the fantasy genre and was the first fantasy game published by Infocom after the \"Zork\" trilogy (it was originally intended to be \"Zork IV\").  The game had a parser that understood over 700 words, making it the most advanced interactive fiction game of its time.  It was Infocom's ninth game.\n\nPlanetfall: Planetfall is a science fiction interactive fiction computer game written by Steve Meretzky, and the eighth title published by Infocom in 1983.  Like most Infocom games, thanks to the portable Z-machine, it was released for several platforms simultaneously.  The original release included versions for the PC (both as a booter and for DOS) and Apple II.  The Atari ST and Commodore 64 versions were released in 1985.  A version for CP/M was also released.  Although \"Planetfall\" was Meretzky's first title, it proved one of his most popular works and a best-seller for Infocom; it was one of five top-selling titles to be re-released in Solid Gold versions including in-game hints.  Planetfall utilizes the Z-machine originally developed for the Zork franchise and was added as a bonus to the \"Zork Anthology\".\n\nZork III: Zork III: The Dungeon Master is an interactive fiction video game written by Marc Blank, Dave Lebling, Bruce Daniels and Tim Anderson and published by Infocom in 1982.  It was the third game in the popular Zork trilogy and was released for a wide range of computer systems.  It is Infocom's fourth game.\n\nZork I: Zork: The Great Underground Empire - Part I, later known as Zork I, is an interactive fiction video game written by Marc Blank, Dave Lebling, Bruce Daniels and Tim Anderson and published by Infocom in 1980.  It was the first game in the popular Zork trilogy and was released for a wide range of computer systems, followed by \"Zork II\" and \"Zork III\".  It was Infocom's first game, and sold 378,987 copies by 1986.\n\nReturn to Zork: Return to Zork is a 1993 graphic adventure game in the \"Zork\" series.  It was developed by Activision and was the final \"Zork\" game to be published under the Infocom label.\n\nZork II: Zork II: The Wizard of Frobozz is an interactive fiction video game published by Infocom in 1981.  It was written by Marc Blank, Dave Lebling, Bruce Daniels and Tim Anderson.  It was the second game in the popular Zork trilogy and was released for a wide range of computer systems.  It begins where \"Zork I\" left off and leads into \"Zork III\".  It is Infocom's second game.\n\nZork Zero: Zork Zero: The Revenge of Megaboz is an interactive fiction video game, written by Steve Meretzky over nearly 18 months and published by Infocom in 1988.  Although it is the ninth and last \"Zork\" game released by Infocom before the company's closure, \"Zork Zero\" takes place before the previous eight games (\"Zork I\", \"Zork II\", \"Zork III\", \"Enchanter\", \"Sorcerer\", \"Wishbringer\", \"Spellbreaker\" and \"Beyond Zork\").  Unlike its predecessors, \"Zork Zero\" is a vast game, featuring a graphical interface with scene-based colours and borders, an interactive map, menus, an in-game hints system, an interactive Encyclopedia Frobozzica, and playable graphical mini-games.  The graphics were created by computer artist James Shook.  It is Infocom's thirty-second game.\n\nQuestion: When was the game after Zork Zero published?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"reference_game\": {\n      \"type\": \"object\",\n      \"description\": \"Details about the game 'Zork Zero' which serves as the reference point for the question.\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The full title of the reference game.\"\n        },\n        \"publication_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the reference game was published.\"\n        },\n        \"narrative_placement_description\": {\n          \"type\": \"string\",\n          \"description\": \"Description of Zork Zero's position in the narrative timeline relative to other Zork games.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"publication_year\",\n        \"narrative_placement_description\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"identified_game\": {\n      \"type\": \"object\",\n      \"description\": \"Details about the game identified as 'after Zork Zero' based on narrative timeline and earliest publication date.\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The full title of the identified game.\"\n        },\n        \"publication_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the identified game was published.\"\n        },\n        \"reason_for_selection\": {\n          \"type\": \"string\",\n          \"description\": \"Explanation for why this specific game is considered 'after Zork Zero' in the context of the question.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"publication_year\",\n        \"reason_for_selection\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"answer_publication_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The publication year of the game identified as 'after Zork Zero' based on the narrative order.\"\n    }\n  },\n  \"required\": [\n    \"reference_game\",\n    \"identified_game\",\n    \"answer_publication_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "reference_game": {
        "type": "object",
        "description": "Details about the game 'Zork Zero' which serves as the reference point for the question.",
        "properties": {
          "title": {
            "type": "string",
            "description": "The full title of the reference game."
          },
          "publication_year": {
            "type": "integer",
            "description": "The year the reference game was published."
          },
          "narrative_placement_description": {
            "type": "string",
            "description": "Description of Zork Zero's position in the narrative timeline relative to other Zork games."
          }
        },
        "required": [
          "title",
          "publication_year",
          "narrative_placement_description"
        ],
        "additionalProperties": false
      },
      "identified_game": {
        "type": "object",
        "description": "Details about the game identified as 'after Zork Zero' based on narrative timeline and earliest publication date.",
        "properties": {
          "title": {
            "type": "string",
            "description": "The full title of the identified game."
          },
          "publication_year": {
            "type": "integer",
            "description": "The year the identified game was published."
          },
          "reason_for_selection": {
            "type": "string",
            "description": "Explanation for why this specific game is considered 'after Zork Zero' in the context of the question."
          }
        },
        "required": [
          "title",
          "publication_year",
          "reason_for_selection"
        ],
        "additionalProperties": false
      },
      "answer_publication_year": {
        "type": "integer",
        "description": "The publication year of the game identified as 'after Zork Zero' based on the narrative order."
      }
    },
    "required": [
      "reference_game",
      "identified_game",
      "answer_publication_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
