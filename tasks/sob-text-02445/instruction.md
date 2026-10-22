Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Grand Ages: Rome: Grand Ages: Rome (previously known as "Imperium Romanum 2") is a 2009 city-building and real-time strategy game developed by Haemimont Games and published by Kalypso Media.  It was released in Europe on March 6, 2009 and in North America on March 17, 2009.  It is the sequel to 2008's "Imperium Romanum".  A sequel, "Grand Ages: Medieval" was released on September 25, 2015.

Shattered Empire: Shattered Empire is the first expansion to the board game "Twilight Imperium", both of which were designed and published by gaming company Fantasy Flight Games.  It was released in December 2006.

Miku Flick/02: Miku Flick/02 (ミクフリック/02 ) is a 2012 rhythm game created by Sega and Crypton Future Media for the iOS operating system for iPhone, iPad and iPod Touch.  The game is a sequel to "Miku Flick" and a spin off of the "" series of Vocaloid rhythm games that was released earlier in 2012.  Like the original the game primarily makes use of Vocaloids, a series of singing synthesizer software, and the songs created using these vocaloids most notably the virtual-diva Vocaloid Hatsune Miku.  The game was released internationally on August 10, 2012, making it the second Project Diva game to be released in English.

Trouble (board game): Trouble (known as Frustration in the UK and Kimble in Finland) is a board game in which players compete to be the first to send four pieces all the way around a board.  Pieces are moved according to the roll of a die.  "Trouble" was developed by the Kohner Brothers and initially manufactured by Irwin Toy Ltd., later by Milton Bradley (now part of Hasbro).  The game was launched in the United States in 1965.  It is very similar to the much older game, "Mensch ärgere dich nicht", as well as another Hasbro game, "Sorry!"  (originally marketed by Parker Brothers).  The classic version is now marketed by Winning Moves.  All these games are versions of the classic Indian game Pachisi, which was first introduced to the western world in England under the name of "Ludo".

Shards of the Throne: Shards of the Throne is the second expansion to the board game Twilight Imperium, both of which were designed and published by gaming company Fantasy Flight Games.  It was released in May 2011.

Glory of the Roman Empire: Glory of the Roman Empire is a 2006 city-building game set during the age of the Roman Empire, developed by Haemimont Games.  The game was released on 26 June 2006 in the United States.  The game features a three-dimensional game engine and individual modeling of game character behaviors.  The game was released in Spain and Italy in December 2006 by FX Interactive under the name "Imperium Civitas".  The difference in naming is explained by the popularity of Haemimont's previous games, Imperium I, II and III, which sold more than 1 million copies in these countries.

Twilight Imperium: Twilight Imperium is a strategy board game produced by Fantasy Flight Games.  It was designed by Christian T. Petersen and was first released in 1998.  The game is in its third edition (2005), which has large changes over previous editions.  This edition also has two expansions – "Shattered Empire" released in 2006, and "Shards of the Throne" released in 2011.  It is known for the length of its gameplay (typically greater than 6 hours), and its in-depth strategy (including military, political, technological and trade).

Steel Gunner: Steel Gunner (スティールガンナー , Sutīru Gannā ) is a first-person shooter arcade game that was released by Namco in 1990; it runs on Namco System 2 hardware, and was the second game from the company to utilize lightguns (the first was "Golly!  Ghost! ", which was released earlier in 1990 and it was also their fourth game to allow scores not ending in "0").  A sequel, Steel Gunner 2, was released in 1991 and the US version of it was also the second game from the company to feature the Federal Bureau of Investigation's "Winners Don't Use Drugs" screen in the attract sequence (the first was "Tank Force", which was released earlier in 1991) - and it would later go on to feature in five more US-released Namco titles.

Mag Blast: Mag Blast is a spaceship-themed strategy card game, produced by gaming company Fantasy Flight Games.  The first edition was set in the universe of "Twilight Imperium", a board game made by the same company.  The game is playable for 2-8 players, and is described as "a game of screaming space battles"

Twilight Imperium: The Role-Playing Game: Twilight Imperium: The Role-Playing Game is a role-playing game published by Fantasy Flight Games in 1999.

Question: Between Trouble and Twilight Imperium, which game was released earlier?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "game_one": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "release_year": {
          "type": "integer"
        }
      },
      "required": [
        "name",
        "release_year"
      ],
      "additionalProperties": false
    },
    "game_two": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "release_year": {
          "type": "integer"
        }
      },
      "required": [
        "name",
        "release_year"
      ],
      "additionalProperties": false
    },
    "earlier_released_game_name": {
      "type": "string"
    },
    "release_year_difference": {
      "type": "integer",
      "description": "The absolute difference in release years between the two games."
    }
  },
  "required": [
    "game_one",
    "game_two",
    "earlier_released_game_name",
    "release_year_difference"
  ],
  "additionalProperties": false
}
