{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nF-Zero X: F-Zero X is a futuristic racing video game for the Nintendo 64 (N64) console.  Developed by Nintendo's EAD division, it was released in Japan, North America, and Europe in 1998.  In 2000, an expansion pack was exclusively released in Japan providing numerous extra features not in the original game.  \"F-Zero X\" was ported in 2004 to the iQue Player in China.  The game was re-released on the Wii Virtual Console in Japan, Europe and in North America, in 2007.  To honor the 100th Virtual Console release in Europe, it became available on June 15.\n\nSonic the Hedgehog Pocket Adventure: Sonic the Hedgehog Pocket Adventure (ソニック・ザ・ヘッジホッグポケットアドベンチャー , Sonikku za Hejjihoggu Poketto Adobenchā ) , or Sonic Pocket Adventure for short, is a 1999 platform video game in the \"Sonic the Hedgehog\" series developed by SNK.  It was released in December 1999 in North America, and May 2000 in Japan, exclusively for the Neo Geo Pocket Color handheld game console.  It is also only the second game of the Sonic series ever to be released on a non-Sega video game console, the first being \"Sonic Jam\" on the Game.com.  The game was praised by critics, receiving perfect scores from multiple reviews.\n\nMonster Max: Monster Max is an isometric adventure video game developed by Rare and published by Titus Software.  It was exclusively released for the Game Boy handheld game console in 1994.  \"Monster Max\" was designed by Jon Ritman and Bernie Drummond and is very similar in both graphics and gameplay to Ritman and Drummond's 1987 title \"Head over Heels\".  The game sold poorly but received very positive reviews from critics.  It was not released in North America.\n\nVideo game accessory: A video game accessory is a distinct piece of hardware that is required to use a video game console, or one that enriches the video game's play experience.  Essentially, video game accessories are everything except the console itself, such as controllers, memory, power adapters (AC), and audio/visual cables.  Most video game consoles come with the accessories required to play games out of the box (minus software): one A/V cable, one AC cable, and a controller.  Memory is usually the most required accessory outside of these, as game data cannot be saved to compact discs.  The companies that manufacture video game consoles also make these accessories for replacement purposes (AC cords and A/V cables) as well as improving the overall experience (extra controllers for more players, or unique devices like light guns and dance pads).  There is an entire industry of companies that create accessories for consoles as well, called third-party companies.  The prices are often lower than those made by the maker of the console (first-party).  This is usually achieved by avoiding licensing or using cheaper materials.  For the mobile systems like the PlayStation Portable and Game Boy iterations, there are many accessories to make them more usable in mobile environments, such as mobile chargers, lighting to improve visibility, and cases to both protect and help organize the collection of system peripherals to.  Newer accessories include many home-made things like mod chips to bypass manufacturing protection or homemade software.\n\nPerfect Dark Zero: Perfect Dark Zero is a first-person shooter video game developed by Rare and published by Microsoft Game Studios.  It was exclusively released as a launch title for the Xbox 360 video game console on November 22, 2005 in North America and December 2, 2005 in Europe.  The game is part of the \"Perfect Dark\" series and a prequel to the original \"Perfect Dark\".  The story of the game follows bounty hunter Joanna Dark as she joins the Carrington Institute agency to prevent rival corporation dataDyne from getting possession of an ancient artefact which endows individuals with superhuman powers.\n\nPerfect Dark (Game Boy Color): Perfect Dark is an action video game developed and published by Rare.  It was exclusively released for the Game Boy Color handheld game console in August 2000, shortly after the release of its Nintendo 64 counterpart.  The game takes place in the year 2022, one year prior to the events of the Nintendo 64 game, and follows the exploits of Joanna Dark as she attempts to prove herself as an agent for the Carrington Institute agency.  The gameplay revolves around shooting opponents and completing objectives such as rescuing hostages or recovering items.  It also features a multiplayer mode where two players may compete in several deathmatch modes.\n\nJust Dance 3: Just Dance 3 is a music video game released on the Wii, Xbox 360, and PlayStation 3 with Kinect and Move support respectively for the latter two.  It is part of the \"Just Dance\" video game series published by Ubisoft originally on the Wii.  \"Just Dance 3\" was announced shortly after the release of \"Just Dance 2\" and was released on October 7, 2011 in North America and October 11, 2011 in Australia and Europe.  Emiliana Torrini's song \"Jungle Drum\" was going to appear in the game, but it was later taken out for reasons.  Ubisoft released \"Just Dance 4\" in October 2012.\n\nTurok 3: Shadow of Oblivion: Turok 3: Shadow of Oblivion is a first-person shooter video game developed by Acclaim Studios Austin and published by Acclaim Entertainment.  It was exclusively released for the Nintendo 64 video game console in 2000.  \"Shadow of Oblivion\" is the third main installment of the \"Turok\" series and a sequel to \"\".  The game received generally favorable reviews from critics.  A separate game, also titled \"\", which is set in the same fictional universe but follows a different storyline, was released for the Game Boy Color in 2000.\n\nJust Dance 2: Just Dance 2 is a dance video game developed by Ubisoft Paris and Ubisoft Milan and published by Ubisoft.  The game was released exclusively for Wii on 12 October 2010 in North America and in Australia and Europe on October 14, 2010, as a sequel to \"Just Dance\".  \"Just Dance 2\" focuses on improvements and enhancements to the original game, including the addition of new co-operative \"Duet\" routines, a team-based battle mode, a new exergaming-oriented mode known as \"Just Sweat\", and support for new songs to be bought for the game as downloadable content.\n\nList of Mortal Kombat media: \"Mortal Kombat\" is a video game franchise originally developed and produced by Midway Games.  The video games are a series of fighting games and several action-adventure games which debuted in North American arcades on October 8, 1992 with the release of \"Mortal Kombat\", created by Ed Boon and John Tobias.  Mortal Kombat titles have been released on numerous different video game consoles, handheld game consoles, and personal computer platforms and is considered one of the best-selling video game franchises of all time with over 26 million games sold.  The games have appeared on every major video game console produced since its debut including every console created by Sony and Microsoft, every console produced by Sega since the Sega Genesis (as well as the Master System in Europe and South America), and every console produced by Nintendo since the Super NES.\n\nQuestion: What video game console was the prequel of the music video game, which was supposed to include the song \"Jungle Drum\", was exclusively released for?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"game_series\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the video game series.\"\n    },\n    \"prequel_game_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the prequel game.\"\n    },\n    \"exclusive_console\": {\n      \"type\": \"string\",\n      \"description\": \"The video game console the prequel was exclusively released for.\"\n    },\n    \"release_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the prequel game was released.\"\n        },\n        \"regions\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"Regions where the prequel game was released.\"\n        }\n      },\n      \"required\": [\n        \"release_year\",\n        \"regions\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"game_series\",\n    \"prequel_game_title\",\n    \"exclusive_console\",\n    \"release_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "game_series": {
        "type": "string",
        "description": "The name of the video game series."
      },
      "prequel_game_title": {
        "type": "string",
        "description": "The title of the prequel game."
      },
      "exclusive_console": {
        "type": "string",
        "description": "The video game console the prequel was exclusively released for."
      },
      "release_details": {
        "type": "object",
        "properties": {
          "release_year": {
            "type": "integer",
            "description": "The year the prequel game was released."
          },
          "regions": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Regions where the prequel game was released."
          }
        },
        "required": [
          "release_year",
          "regions"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "game_series",
      "prequel_game_title",
      "exclusive_console",
      "release_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
