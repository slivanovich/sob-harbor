{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCJ Carella's WitchCraft: CJ Carella's WitchCraft, or more informally WitchCraft (ISBN  ), is a modern horror role-playing game published by Eden Studios, Inc. It is based on the \"Unisystem\" game system and had been previously published by Myrmidon Press.  In both cases it was designed and written by C. J. Carella.  \"WitchCraft\" was the first RPG to use the \"Unisystem\" game system.\n\nStar Trek Roleplaying Game: The Star Trek Roleplaying Game is a role-playing game (RPG) set in the \"Star Trek\" universe using the \"CODA System\" rules and first published by Decipher, Inc. in 2002.  When Decipher acquired the rights to create the RPG, they also acquired most of the gaming studio from Last Unicorn Games.  However, the Decipher game system is dissimilar to .  Instead, the system is similar to Wizards of the Coast's \"d20 System\" but uses 2D6 to resolve actions.\n\nBuffyverse role-playing games: The Buffyverse role-playing games - the \"Buffy the Vampire Slayer\" and \"Angel\" role-playing games - are complementary, officially licensed role-playing games (RPGs) published by Eden Studios, Inc. The \"Buffy the Vampire Slayer Core Rulebook\" was published in 2002, while the \"Angel Corebook\" followed in 2003.  Both games use a streamlined (or \"Cinematic\") version of Eden Studios' popular \"Unisystem\" game engine, also featured in \"CJ Carella's WitchCraft\" and \"All Flesh Must Be Eaten\", two of Eden's better-known original product lines.  In both games, players are able to take on the roles of characters from the respective television series or create wholly original characters as they and their group see fit, effectively building their own Buffyverse series in the process.\n\nUnisystem: Unisystem is a generic role-playing game system produced by Eden Studios, Inc. It is used in \"All Flesh Must Be Eaten\", the Buffyverse role-playing games, \"CJ Carella's WitchCraft\", \"Conspiracy X (2nd Ed.) \", and several other games.  Games designed using \"Unisystem\" have been nominated for, and won, Origins Awards.\n\nStandard RPG System: The Standard RPG System (SRS for short) is a Japanese role-playing game system developed by FarEast Amusement Research and used in \"Alshard\", \"Tenra War\", \"Kaze no Stigma RPG\", \"Shinkyoku Sōkai Polyphonica RPG\" and so on.  The newest, the 14th game that use SRS are the \"Full Metal Panic!  RPG\" based upon the anime and light novels of the same title.  SRS games are published by several companies such as Game Field, Softbank Creative, JIVE and Kadokawa(Former Enterbrain and Fujimi Shobo).\n\nEden Games: Eden Games (known as Eden Studios until 2003) is a game development studio.  In May 2002, the company was sold to the Infogrames Group.  It is most well known for the \"V-Rally\" series of games, as well as the 2006 release \"Test Drive Unlimited\".  They have most recently developed \"Test Drive Unlimited 2\", which was released in February 2011 for the PlayStation 3, Xbox 360 and PC.  The company was a wholly owned subsidiary of Atari, SA.  In 2013 Atari decided to close it.  However, the company re-opened in 2014 under the impulsion of former employees and with the financing of ID Invest and Monster Capital.  As of 2013, Eden Games have started up as a small independent games company, independent of Atari and releases its new game, GT Spirit, on Apple TV in December, 2015.\n\nStar Wreck Roleplaying Game: Star Wreck Roleplaying Game is a Finnish role-playing game (RPG) set in the universe of the \"Star Wreck\" fan films. First published at Ropecon 2006, it is, as the designer has jokingly pointed out, the first Finnish RPG based on a movie franchise.\n\nConspiracy X: Conspiracy X is a role-playing game (RPG) published by Eden Studios, Inc. The current version is based on the \"Unisystem\", but previous versions have used \"GURPS\" and its own system.  All feature the same central story.\n\nEden Studios, Inc.: Eden Studios, Inc. is an American role-playing game publisher founded in 1996 by George Vasilakos, M. Alexander Jurkat, and Ed Healy.  Currently run by Mr. Vasilakos, Eden Studios is best known for \"Conspiracy X\", the \"Buffyverse role-playing games\", \"All Flesh Must Be Eaten\", \"CJ Carella's WitchCraft\" and most recently for the \"City of Heroes Roleplaying Game\", an unreleased adaptation of Cryptic Studios' MMORPG \"City of Heroes\".\n\nPokémon: Generations: Pokémon: Generations was an unlicensed 3D Action RPG based on the Pokémon franchise, first released on February 2, 2013.  The game's final update came on January 12, 2014, two months prior to lead developer Xatoku's announcement of the project's cancellation on March 2.\n\nQuestion: Eden Studios, Inc. is best known for the RPG based on what game system?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"publisher_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the role-playing game publisher.\"\n    },\n    \"known_for_rpgs\": {\n      \"type\": \"array\",\n      \"description\": \"A list of RPGs the publisher is best known for.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"rpg_title\": {\n            \"type\": \"string\",\n            \"description\": \"The title of the RPG.\"\n          },\n          \"game_system\": {\n            \"type\": \"string\",\n            \"description\": \"The game system used by the RPG.\"\n          }\n        },\n        \"required\": [\n          \"rpg_title\",\n          \"game_system\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"best_known_game_system\": {\n      \"type\": \"string\",\n      \"description\": \"The game system that the publisher's best-known RPGs are based on.\"\n    }\n  },\n  \"required\": [\n    \"publisher_name\",\n    \"known_for_rpgs\",\n    \"best_known_game_system\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "publisher_name": {
        "type": "string",
        "description": "The name of the role-playing game publisher."
      },
      "known_for_rpgs": {
        "type": "array",
        "description": "A list of RPGs the publisher is best known for.",
        "items": {
          "type": "object",
          "properties": {
            "rpg_title": {
              "type": "string",
              "description": "The title of the RPG."
            },
            "game_system": {
              "type": "string",
              "description": "The game system used by the RPG."
            }
          },
          "required": [
            "rpg_title",
            "game_system"
          ],
          "additionalProperties": false
        }
      },
      "best_known_game_system": {
        "type": "string",
        "description": "The game system that the publisher's best-known RPGs are based on."
      }
    },
    "required": [
      "publisher_name",
      "known_for_rpgs",
      "best_known_game_system"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
