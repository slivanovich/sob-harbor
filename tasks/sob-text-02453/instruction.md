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
Space Opera (role-playing game): Space Opera is a science-fiction role-playing game created by Edward E. Simbalist, A. Mark Ratner, and Phil McGregor in 1980 for Fantasy Games Unlimited.  While the system is applicable to the whole genre of science fiction, "Space Opera" had a default setting intended to be used as generic science fiction role-playing game rules, the focus being on creating space opera themed adventures.

Shining (series): Shining (シャイニング , "Shainingu" ) is a series of fantasy video games developed by Sega.  The series is Sega's main venture into the role-playing genre, along with the science fiction role-playing series "Phantasy Star".  The first game, "Shining in the Darkness", was a first-person dungeon crawler with randomly encountered, turn-based battles (comparable to "Wizardry" and "Might and Magic").  The next game released in the series was "Shining Force", which were turn-based strategy style tactical role-playing games with battle scenes acted out with sprites (comparable to the Kure Software Koubou games and "Fire Emblem").  Other spin-offs include "Shining Soul", a dungeon crawl action role-playing game with roguelike elements.

James Bond 007 (role-playing game): James Bond 007: Role-Playing In Her Majesty's Secret Service is a spy fiction role-playing game based on the James Bond books and films.  The game was designed by Gerard Christopher Klug and published by Victory Games (a branch of Avalon Hill).  The game and its supplements were published from 1983 until 1987, when the license lapsed.  At that time, it was the most popular espionage role-playing game.  "James Bond 007: Role-Playing In Her Majesty's Secret Service" won an Origins Award in 1983 and a Strategists' Club Award as Outstanding Role-Playing Game in 1984.

Metamorphosis Alpha: Metamorphosis Alpha is a science fiction role-playing game.  It was created by James M. Ward and originally produced by TSR, the publisher of "Dungeons & Dragons".  It was the first science fiction role-playing game, published in July 1976.

Lee Hammock: Lee Hammock is a professional writer and game designer.  Hammock has worked on numerous products for numerous companies, including "" RPG by Louis Porter Jr.  Design, "The Halo Graphic Novel" and the "Dawning Star Campaign Setting" by Blue Devil Games.

Firefly Role-Playing Game: The Firefly Role-Playing Game is a science fiction role-playing game released in 2014 and set in the universe of the Joss Whedon television show "Firefly".  It was produced by Margaret Weis Productions, Ltd, and uses the "Cortex Action" variant of Margaret Weis Production's proprietary Cortex Plus game system.

Universe (role-playing game): Universe: The Role-Playing Game of the Future is a science fiction role-playing game published by Simulation Publications, Inc (SPI) from 1981 to 1983.  It was praised for its innovative and tightly organized rules for such sci-fi RPG concerns as generating planets, applying character skills to in-game situations, and resolving the initial moments of alien encounters; however, it was also criticized for its cumbersome encounter/combat system and its lack of compelling background material.  "Universe" was also noted for its "striking" Interstellar Display, a poster-sized, astronomically accurate map of all stars within 30 light-years of Earth.

Dawning Star: Dawning Star (abbreviated "DS") is a science fiction role-playing game by Blue Devil Games built on "d20 Modern" and powered by "d20 Future" by Wizards of the Coast.  It is the first full-scale campaign setting using the "d20 Future" ruleset.  It is published under the Open Game License.

2300 AD: 2300 AD is a hard science fiction tabletop role-playing game created by Game Designers Workshop, originally offered as an alternative to the space opera portrayed by the company's leading science fiction role-playing game, "Traveller".  In fact it was originally titled "Traveller: 2300", but this caused confusion as the game used neither the rules system nor the setting of the original "Traveller".  The game was therefore renamed in its 2nd edition.

Corporation (role playing game): Corporation is a science fiction role-playing game created by Brutal Games.  It has been inspired by many Science fiction films and books, including "The Fifth Element", "Gattaca", "Johnny Mnemonic", and "Total Recall".  It has a small, but growing, fan base worldwide.  The game makers have also set up a forum for players to ask questions relating to the fictional world the game is set in, the rules, and even to discuss scenarios.

Question: Who hired professional developer Lee Hammock to design a science fiction role-playing game?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "developer_name": {
      "type": "string",
      "description": "The name of the professional developer."
    },
    "game_title": {
      "type": "string",
      "description": "The title of the science fiction role-playing game."
    },
    "hiring_company": {
      "type": "string",
      "description": "The name of the company that hired the developer for the game."
    },
    "game_genre": {
      "type": "string",
      "description": "The genre of the game."
    }
  },
  "required": [
    "developer_name",
    "game_title",
    "hiring_company",
    "game_genre"
  ],
  "additionalProperties": false
}
