{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSouth Park: The Stick of Truth: South Park: The Stick of Truth is a 2014 role-playing video game developed by Obsidian Entertainment in collaboration with South Park Digital Studios and published by Ubisoft.  Based on the American adult animated television series \"South Park\", the game follows the New Kid, who has moved to the eponymous town and becomes involved in an epic role-play fantasy war involving humans, wizards, and elves, who are fighting for control of the all-powerful Stick of Truth.  Their game quickly escalates out of control and brings them into conflict with aliens, Nazi zombies, and gnomes, threatening the entire town with destruction.\n\nKingdom Under Fire II: Kingdom Under Fire II is a video game set in a high fantasy setting developed by Blueside which merge real-time strategy (RTS), role-playing game (RPG) and massively multiplayer online game (MMO) genres - the game is to have a single player, and online multiplayer mode.  The game follows on chronologically from \"\", and is the first RTS game set in the \"Kingdom Under Fire\" universe to be released since the 2005 \"\".\n\nAbaza (TV series): Abaza is an Egyptian television series that aired for one season on Sada Elbalad TV in 2014.  \"Abaza\" is set in a fictitious world where humans and monsters live next to each other in harmony.  The monsters in \"Abaza\" are not evil and are portrayed in a caricatured manner.\n\nEon (role-playing game): Eon is a fantasy role-playing game set in the fictitious world of Mundana.  It's developed and published by Swedish company Helmgast.  Eon is the Swedish word for Aeon.\n\nWarhammer Fantasy Roleplay: Warhammer Fantasy Roleplay or Warhammer Fantasy Role-Play (abbreviated to WFRP or WHFRP) is a role-playing game set in the \"Warhammer Fantasy\" setting.  Over the years, it has been through a number of phases and different publishers, most of which were related in some way to Games Workshop.\n\nThe Caine Mutiny (film): The Caine Mutiny is a 1954 American film.  A fictional Navy drama set in the Pacific during World War II, it was directed by Edward Dmytryk and produced by Stanley Kramer, and stars Humphrey Bogart, José Ferrer, Van Johnson, and Fred MacMurray.  The film is based on \"The Caine Mutiny,\" the 1951 Pulitzer Prize-winning novel written by Herman Wouk.  It depicts the events on board a fictitious World War II U.S. Navy destroyer minesweeper and a subsequent court-martial for mutiny.\n\nLorien Trust: Lorien Trust (sometimes abbreviated to LT) is the trading name of Merlinroute ltd., a Live Action Role-Play organisation that runs LARP events at Locko Park, Derby, UK.  It runs some of Britain's largest Live Roleplay events, attracting around 1,200 to 1,500 to its first three events each year and around 2,500 to 3,000 people to The Gathering.  It was formed in 1992, originally as a charitable organisation (hence \"Trust\" in the name).  In 1995 it became Merlinroute ltd trading as Lorien Trust.  The Lorien Trust has a well established game world, and uses its own set of LARP rules, known simply as the \"Lorien Trust rules system\".  In addition to the four events held per year, the Lorien Trust also sanctions many smaller events to use the same system and game world.\n\nMetagaming: Metagaming is any strategy, action or method used in a game which transcends a prescribed ruleset, uses external factors to affect the game, or goes beyond the supposed limits or environment set by the game.  Another definition refers to the game universe outside of the game itself.  In role-play situations, for example, it would mean to tell somebody some information about another player or something they are doing that the said player's character should not intrinsically know about.  In simple terms, it is the use of out-of-game information or resources to affect one's in-game decisions.\n\nPretty Pretty Princess: The board game Pretty Pretty Princess is a game for young children (ages five and up) with a fantasy/role-play theme.  This game does not sell in stores anymore.\n\nNeogames: Neogames is a Swedish role-playing game publisher situated in Gothenburg.  They were after the re-creation of Target Games the largest RPG publisher in the country.  Neogames are known for developing the three first editions of the fantasy RPG license \"Eon\", a role-playing game set in a fairly standard fantasy setting with elves, dwarves and magic.\n\nQuestion: What fantasy role-play game set in the fictitious world of Mundana was created by Neogames?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"game_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the fantasy role-play game.\"\n    },\n    \"game_type\": {\n      \"type\": \"string\",\n      \"description\": \"The genre or type of the game.\"\n    },\n    \"setting_world\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the fictitious world where the game is set.\"\n    },\n    \"developer_info\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the company that developed the game.\"\n        },\n        \"role\": {\n          \"type\": \"string\",\n          \"description\": \"The specific role of the developer in creating the game (e.g., 'developed first three editions').\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"role\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"game_name\",\n    \"game_type\",\n    \"setting_world\",\n    \"developer_info\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "game_name": {
        "type": "string",
        "description": "The name of the fantasy role-play game."
      },
      "game_type": {
        "type": "string",
        "description": "The genre or type of the game."
      },
      "setting_world": {
        "type": "string",
        "description": "The name of the fictitious world where the game is set."
      },
      "developer_info": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the company that developed the game."
          },
          "role": {
            "type": "string",
            "description": "The specific role of the developer in creating the game (e.g., 'developed first three editions')."
          }
        },
        "required": [
          "name",
          "role"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "game_name",
      "game_type",
      "setting_world",
      "developer_info"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
