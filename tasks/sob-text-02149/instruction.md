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
Infinite Armies: Infinite Armies is a customizable card game for two players.  It was created by Greg Porter, and published in 2005 by Blacksburg Tactical Research Center.  It follows on the success of the collectible card game genre, but establishes its own niche by focusing more on card and deck customization.  It breaks from the traditional collectible card games by allowing players to fully design and customize their own cards.  Players do not even buy cards, but print their own.  Whether this is a viable business concept is still being tested, as most card games rely heavily on sales of cards and the continued publication of new cards.

Xiaolin Showdown Trading Card Game: Released in October 2005 by Wizards of the Coast, the Xiaolin Showdown Trading Card Game is a collectible card game based on the "Xiaolin Showdown" animated series.  It is a two player game where the object is to be the first to win four contests for Shen Gong Wu.  The Shen Gong Wu are hidden mystical objects, and searching for them and using them is a central focus of the series, with conflicts over their possession resolved by a Xiaolin Showdown.  The first expansion set, "Wudai Warriors", was released in March 2006.

ReCharge Collectible Card Game: ReCharge Collectible Card Game is a collectible card game (CCG) based on Marvel Superheroes and produced by Marvel Entertainment in 2001.  The game is modeled after Wizards of the Coast's "X-Men Trading Card Game".  It was subsumed by UpperDeck's Vs. System, which is still the torch-bearer as the main Marvel CCG.

The Spoils (card game): The Spoils is a collectible card game owned by Arcane Tinmen.  The design team was headed up by Josh Lytle, who also designed the collectible card game Magi-Nation Duel.  Jon Finkel, a prominent player in 's , aided the development team as an advisor since 2002.  Under the direction of Ken Pilcher, The Spoils Card Game won the Fan Favorite Origins Award for Best Collectible Card Game at the 2015 Origins Game Fair, beating other contenders including Legend of the Five Rings and Magic: The Gathering.  It was announced on December 29th 2016 that Organized Play and production of The Spoils Card Game will officially cease on January 1st 2017.

Chipper Jones: Larry Wayne "Chipper" Jones Jr. (born April 24, 1972) is an American former Major League Baseball (MLB) third baseman who spent his entire 19-year MLB career playing for the Atlanta Braves, and all 23 years as a professional baseball player in the Atlanta organization.  Initially a shortstop, he was the Braves' primary starting third baseman for nearly all of the period from 1995–2012.  In 2002 and 2003, Jones played left field before returning to third base in 2004.  Standing 6' 4" (76 in ) tall and weighing 210 lb during his playing career, Jones threw right-handed and was a switch hitter.

BattleTech Collectible Card Game: The BattleTech Collectible Card Game is a collectible card game set in the BattleTech universe developed by Wizards of the Coast (WotC) for FASA using a similar style of gameplay and card distribution as WotC's "".  It was designed by Richard Garfield.  Its production ran from 1996 through 2001.  The "BattleTech CCG" featured BattleMechs, characters, and technology from the original board game, with new artwork done by various artists.  Currently, the "BattleTech CCG" is no longer in print.

Call of Cthulhu: The Card Game: Call of Cthulhu: The Card Game (formerly the Call of Cthulhu Collectible Card Game) is a card game produced and marketed by Fantasy Flight Games.  It is based on Chaosium's "Call of Cthulhu" role-playing game, the writings of H. P. Lovecraft, and other Cthulhu Mythos fiction.  In 2008, Fantasy Flight moved the game over to its Living Card Game (LCG) format, which retains the deck-building aspect of collectible card games, but without the random distribution.

NBA Showdown: NBA Showdown is a trading card game produced by Wizards of the Coast based on the game of basketball.  The game is played with customizable decks of cards featuring National Basketball Association players and 20-sided dice.  It is one of several sport-themed card games produced by Wizards, including MLB Showdown and NFL Showdown.

Myths and Legends: Myths and Legends is a collectible card game based on universal mythologies, developed in 2000 in Santiago, Chile.  The game now has 39 editions and more than 3,000 collectible cards .  It is the only collectible card game integrally produced and developed in Latin-America (Chile), and it is translated into the English and German languages.  The game has been launched in Europe, United States, Oceania and Latin America.  In January 2010, the game went into "indefinite recess" due to the bankruptcy of the publisher, Salo.

MLB Showdown: MLB Showdown (colloq.  "Showdown") was a collectible card game made by Wizards of the Coast that ran from 2000 to 2005.  The game was introduced to the public in 2000, featuring Atlanta Braves third baseman Chipper Jones on the product cover.  Since the 2000 base set, cover athletes have included Shawn Green, Gary Sheffield, Manny Ramírez, Luis Gonzalez, Torii Hunter, Albert Pujols, and Craig Biggio.

Question: What 19-year MLB veteran who was initially a shortstop was also featured as a cover athlete on the collectible card game MLB Showdown?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "mlb_veteran_name": {
      "type": "string",
      "description": "The name of the MLB veteran."
    },
    "mlb_career_years": {
      "type": "integer",
      "description": "The total number of years the veteran played in MLB."
    },
    "initial_position": {
      "type": "string",
      "description": "The initial playing position of the veteran."
    },
    "card_game_details": {
      "type": "object",
      "properties": {
        "game_name": {
          "type": "string",
          "description": "The name of the collectible card game."
        },
        "feature_role": {
          "type": "string",
          "description": "The role of the veteran on the card game (e.g., cover athlete)."
        }
      },
      "required": [
        "game_name",
        "feature_role"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "mlb_veteran_name",
    "mlb_career_years",
    "initial_position",
    "card_game_details"
  ],
  "additionalProperties": false
}
