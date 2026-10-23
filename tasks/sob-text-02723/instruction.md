{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nTenra War: Tenra War (天羅WAR ) is a Japanese mixed-genre tabletop role-playing game designed by Jun'ichi Inoue and FarEast Amusement Research.  It was released in April 2007.  It is a triple crossover product, based on an oriental science fantasy RPG \"Tenra Bansho\", steampunk western RPG \"Terra the Gunslinger\", and post-apocalypse mecha RPG \"Angel Gear\".  All three of the original games were designed by Jun'ichi Inoue.\n\nMonte Cook: Monte Cook is an American professional table-top role-playing game designer and writer, best known for his work on \"Dungeons & Dragons\".\n\nRole-playing video game: A role-playing video game (commonly referred to as role-playing game or RPG, as well as computer role-playing game or CRPG) is a video game genre where the player controls the actions of a character (and/or several party members) immersed in some well-defined world.  Many role-playing video games have origins in tabletop role-playing games (Including \"Dungeons & Dragons\") and use much of the same , settings and game mechanics.  Other major similarities with pen-and-paper games include developed story-telling and narrative elements, player character development, complexity, as well as replayability and immersion.  The electronic medium removes the necessity for a gamemaster and increases combat resolution speed.  RPGs have evolved from simple text-based console-window games into visually rich 3D experiences.\n\nNumenera: Numenera is an award-winning science fantasy tabletop role-playing game (RPG) set in the far distant future, written by Monte Cook.\n\nStephen R. Marsh: Stephen R. Marsh is an American game designer and lawyer best known for his contributions to early editions of TSR's \"Dungeons & Dragons\" fantasy tabletop role-playing game (RPG).  Some of the creatures he created for the original edition of \"D&D\" in 1975 have been included in every subsequent edition of the game.\n\nDungeons &amp; Dragons: Dungeons & Dragons (abbreviated as D&D or DnD) is a fantasy tabletop role-playing game (RPG) originally designed by Gary Gygax and Dave Arneson, and first published in 1974 by Tactical Studies Rules, Inc. (TSR).  The game has been published by Wizards of the Coast (now a subsidiary of Hasbro) since 1997.  It was derived from miniature wargames with a variation of the \"Chainmail\" game serving as the initial rule system.  \"D&D\"'s publication is commonly recognized as the beginning of modern role-playing games and the role-playing game industry.\n\nShadowrun: Shadowrun is a science fantasy tabletop role-playing game set in a near-future fictional universe in which cybernetics, magic and fantasy creatures co-exist.  It combines genres of cyberpunk, urban fantasy and crime, with occasional elements of conspiracy, horror and detective fiction.  From its inception in 1989, \"Shadowrun\" has remained among the most popular role-playing games.  It has spawned a vast franchise that includes a series of novels, a collectible card game, two miniature-based tabletop wargames, and multiple video games.\n\nTabletop role-playing game: A tabletop role-playing game (or pen-and-paper role-playing game) is a form of role-playing game (RPG) in which the participants describe their characters' actions through speech.  Participants determine the actions of their characters based on their characterization, and the actions succeed or fail according to a set formal system of rules and guidelines.  Within the rules, players have the freedom to improvise; their choices shape the direction and outcome of the game.\n\nThe Strange: The Strange is a science fantasy tabletop role-playing game (RPG) set in multiple alternate dimensions, written by Bruce Cordell & Monte Cook.\n\n13th Age: 13th Age is a d20 fantasy tabletop role-playing game, designed by Rob Heinsoo (lead designer of \"Dungeons & Dragons\" 4th Edition) and Jonathan Tweet (lead designer of \"D&D\" 3rd Edition), and published by Pelgrane Press.  It was released on August 3, 2013, and the pre-release version was a nominee for the RPG Geek RPG of the Year 2013.  As of December 2013 the ENWorld hot games list showed that discussions of it were responsible for 2.6% of all \"D&D\" related web traffic they had been able to index.\n\nQuestion: Numenera is an award-winning science fantasy tabletop role-playing game (RPG) set in the far distant future, written by Monte Cook, an American professional table-top role-playing game designer and writer, best known for his work on what?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"designer_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the game designer.\"\n    },\n    \"game_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of game the designer works on.\"\n    },\n    \"known_for_work\": {\n      \"type\": \"string\",\n      \"description\": \"The specific work the designer is best known for.\"\n    }\n  },\n  \"required\": [\n    \"designer_name\",\n    \"game_type\",\n    \"known_for_work\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "designer_name": {
        "type": "string",
        "description": "The name of the game designer."
      },
      "game_type": {
        "type": "string",
        "description": "The type of game the designer works on."
      },
      "known_for_work": {
        "type": "string",
        "description": "The specific work the designer is best known for."
      }
    },
    "required": [
      "designer_name",
      "game_type",
      "known_for_work"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
