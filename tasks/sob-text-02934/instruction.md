{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nHorizon Zero Dawn: Horizon Zero Dawn is an action role-playing video game developed by Guerrilla Games and published by Sony Interactive Entertainment for PlayStation 4 and released in early 2017.  The plot revolves around Aloy, a hunter and archer living in a world overrun by robots.  Having been an outcast her whole life, she sets out to discover the dangers that kept her sheltered.  The character uses ranged weapons and a spear and stealth tactics to combat the mechanised creatures, whose remains can be looted for resources.  A skill tree provides the player with new abilities and passive bonuses.  The game features an open world environment for Aloy to explore, divided into tribes that hold side quests to undertake, while the main story guides her across the entire map.\n\nNioh: Nioh (Japanese: 仁王 , Hepburn: Niō , \"benevolent king\") is an action role-playing video game developed by Team Ninja for the PlayStation 4.  It was released worldwide in February 2017, and was published by Koei Tecmo in Japan and Sony Interactive Entertainment internationally.  Gameplay revolves around navigating levels and defeating monsters that have infested an area.  \"Nioh\" takes place in the early 1600s during a fictionalized version of the Sengoku period, when Japan was in the midst of civil war prior to the ascension of the Tokugawa shogunate.  A sailor named William, in pursuit of an enemy, arrives in Japan and is enlisted by Hattori Hanzo, servant to Tokugawa Ieyasu, in defeating yōkai that are flourishing in the chaos of war.\n\nPolyphony Digital: Polyphony Digital is an internal Japanese first-party video game development studio of Sony Interactive Entertainment, part of Sony Interactive Entertainment Worldwide Studios.  Originally a development group within Sony Computer Entertainment known as Polys Entertainment, after the success of \"Gran Turismo\" in Japan, they were granted greater autonomy and their name changed to Polyphony Digital.\n\nGod of War (2018 video game): God of War (commonly referred to as God of War 4) is an upcoming third-person action-adventure video game in development by Santa Monica Studio and to be published by Sony Interactive Entertainment (SIE).  It is scheduled to be released in early 2018 for the PlayStation 4 (PS4) console.  It will be the eighth installment in the \"God of War\" series, the eighth chronologically, and the sequel to 2010's \"God of War III\".  The game will be a soft reboot for the franchise and will take the series to the world of Norse mythology—all previous games were based on Greek mythology.  Series protagonist Kratos will return as the main character, and he now has a son named Atreus.  Kratos acts as a mentor and protector to his son, and has to master the rage that has driven him for many years.\n\nMiddle-earth: Shadow of War: Middle-earth: Shadow of War is an upcoming action role-playing video game developed by Monolith Productions and published by Warner Bros.  Interactive Entertainment.  It is the sequel to 2014's \"\", and it is scheduled to be released worldwide on October 10, 2017 for Microsoft Windows, PlayStation 4 and Xbox One.  A companion game was released for iOS and Android as a free-to-play top-down video game.\n\nGuerrilla Games: Guerrilla B.V., doing business as Guerrilla Games, is a Dutch first-party video game developer founded in 2000 as \"Lost Boys Games\".  Based in Amsterdam, Netherlands, it is a wholly owned subsidiary of Sony Interactive Entertainment.  The company currently employs approximately 270 individuals, and is headed by managing director Hermen Hulst.\n\nLance Reddick: Lance Reddick (born December 31, 1962) is an American actor and musician.  He is best known for portraying Cedric Daniels in \"The Wire\" and Phillip Broyles in \"Fringe\".  He is also known for playing Detective Johnny Basil on \"Oz\" and Matthew Abbadon in the fourth and fifth seasons of \"Lost\".  Additionally, Reddick provided both the voice and likeness for video game characters Martin Hatch in \"Quantum Break\" and Sylens in \"Horizon Zero Dawn\".  He voices the character Commander Zavala in the \"Destiny\" video game franchise.\n\nBastion (video game): Bastion is an action role-playing video game developed by independent developer Supergiant Games and published by Warner Bros.  Interactive Entertainment.  In the game, the player controls \"the Kid\" as he moves through floating, fantasy-themed environments and fights enemies of various types.  It features a dynamic voiceover from a narrator, and is presented as a two-dimensional game with an isometric camera and a hand-painted, colorful art style.  \"Bastion\"' s story follows the Kid as he collects special shards of rock to power a structure, the Bastion, in the wake of an apocalyptic Calamity.\n\nAlienation (video game): Alienation is a shooter and role-playing video game developed by Housemarque and published by Sony Interactive Entertainment.  It was released in April 2016 for PlayStation 4.  The game is an isometric twin-stick shooter in which one to four players defend themselves against an alien invasion on Earth through increasingly-difficult levels.  Players can choose one of three character classes, each with its own abilities.  Players can upgrade their weapons with collectables, known as upgrade cores.\n\nThe Surge (video game): The Surge is a science fiction, action role-playing video game developed by Deck13 Interactive and published by Focus Home Interactive for Microsoft Windows, PlayStation 4, and Xbox One.  It is considered a spiritual successor to Deck13 Interactive's earlier action role-playing game \"Lords of the Fallen\", with which it shares many gameplay features.  Deck13 Interactive described the game as inspired by \"Rise of the Robots\" and the \"Souls\" series.\n\nQuestion: Name the action role-playing video game developed by Guerrilla Games and published by Sony Interactive Entertainment for the PS4 which features the character Sylens whose voice and likeness was provided by American actor and musician Lance Reddick?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"game_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the video game.\"\n    },\n    \"developer\": {\n      \"type\": \"string\",\n      \"description\": \"The developer of the video game.\"\n    },\n    \"publisher\": {\n      \"type\": \"string\",\n      \"description\": \"The publisher of the video game.\"\n    },\n    \"platform\": {\n      \"type\": \"string\",\n      \"description\": \"The primary platform the game was released on.\"\n    },\n    \"genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the video game.\"\n    },\n    \"character_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"character_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the character whose details are being provided.\"\n        },\n        \"actor_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the actor who provided the voice and/or likeness for the character.\"\n        },\n        \"actor_role\": {\n          \"type\": \"string\",\n          \"description\": \"The specific role the actor played for the character (e.g., voice, likeness, voice and likeness).\"\n        }\n      },\n      \"required\": [\n        \"character_name\",\n        \"actor_name\",\n        \"actor_role\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"game_title\",\n    \"developer\",\n    \"publisher\",\n    \"platform\",\n    \"genre\",\n    \"character_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "game_title": {
        "type": "string",
        "description": "The title of the video game."
      },
      "developer": {
        "type": "string",
        "description": "The developer of the video game."
      },
      "publisher": {
        "type": "string",
        "description": "The publisher of the video game."
      },
      "platform": {
        "type": "string",
        "description": "The primary platform the game was released on."
      },
      "genre": {
        "type": "string",
        "description": "The genre of the video game."
      },
      "character_details": {
        "type": "object",
        "properties": {
          "character_name": {
            "type": "string",
            "description": "The name of the character whose details are being provided."
          },
          "actor_name": {
            "type": "string",
            "description": "The name of the actor who provided the voice and/or likeness for the character."
          },
          "actor_role": {
            "type": "string",
            "description": "The specific role the actor played for the character (e.g., voice, likeness, voice and likeness)."
          }
        },
        "required": [
          "character_name",
          "actor_name",
          "actor_role"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "game_title",
      "developer",
      "publisher",
      "platform",
      "genre",
      "character_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
