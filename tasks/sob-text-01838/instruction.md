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
Super Mario Kart: Super Mario Kart is a 1992 go-kart racing video game developed and published by Nintendo for the Super Nintendo Entertainment System video game console.  The first game of the "Mario Kart" series, it was launched in Japan on August 27, 1992, in North America on September 1, 1992, and in Europe on January 21, 1993.  Selling nine million copies worldwide, the game went on to become the third best selling SNES game of all time.  "Super Mario Kart" was re-released on the Wii's Virtual Console in Japan on June 9, 2009, North America on November 23, 2009, and in Europe on April 2, 2010.  "Super Mario Kart" was re-released again on the Wii U's Virtual Console in Japan on June 19, 2013, Europe on March 27, 2014, and in North America on August 6, 2014.  "Super Mario Kart" was released once more on the New Nintendo 3DS's Virtual Console.  Nintendo re-released "Super Mario Kart" in the United States in September 2017 as part of the company's Super NES Classic Edition.

Super Mario Bros. 3: Super Mario Bros. 3 is a platform video game developed and published by Nintendo for the Nintendo Entertainment System (NES) video game console.  It was first released in Japan on October 23, 1988, and later in North America on February 12, 1990.  The game was developed by Nintendo Entertainment Analysis and Development, led by Shigeru Miyamoto and Takashi Tezuka.  Enhanced remakes were later released on the Super NES in 1993 and the Game Boy Advance in 2003.  The game has been re-released as a Virtual Console title for the Wii, Nintendo 3DS, and Wii U consoles.

Super Mario Advance 4: Super Mario Bros. 3: Super Mario Advance 4: Super Mario Bros 3 is a platform video game developed and published by Nintendo for the Game Boy Advance handheld game console.  It was first released in Japan, and then later released in Europe, North America, and Australia.  It is an enhanced remake of the Nintendo Entertainment System video game "Super Mario Bros. 3", and is based on the remake found in "Super Mario All-Stars" for the Super NES.  It is the fourth and final release in the "Super Mario Advance" series.

Super Mario Bros.: Super Mario Bros. is a platform video game developed and published by Nintendo for the Nintendo Entertainment System home console.  Released as a sequel to the 1983 game "Mario Bros.", "Super Mario Bros." was released in Japan and North America in 1985, and in Europe and Australia two years later.  In "Super Mario Bros.", the player controls Mario and in a two-player game, a second player controls Mario's brother Luigi as he travels through the Mushroom Kingdom in order to rescue Princess Toadstool from the antagonist Bowser.

Koopa Troopa: Koopa Troopas, or just simply Koopas, known in Japan as Nokonoko (ノコノコ ) , are a fictional race of turtle or tortoise-like creatures from the "Mario" series, as well as its sister "Yoshi" series.  Although the term 'Koopa' is a blanket term for the entire species of anthropomorphic turtles in the series, to which creatures such as Lakitu, Hammer Bros. and even Bowser belong, the term is often used to refer colloquially to this particular enemy.  First appearing in the 1985 Nintendo Entertainment System game "Super Mario Bros.", they are among the oldest recurring enemies in the series, and have appeared in some form in all of the main games, and most of the spin-off games.  When defeated, Koopas may flee from or retreat inside their shells, which can then usually be used as weapons.  Shellcreepers are a different species, according to their trophy in "Super Smash Bros. for Nintendo 3DS and Wii U".  Koopa shells are a recurring weapon in the series, particularly popularized in the "Mario Kart" series, in which they can be fired as projectiles against other racers.  Despite making up the bulk of Bowser's army, known as the "Koopa Troop", Koopas as a species are often shown to be peaceful, some even teaming up with Mario.  An undead Koopa Troopa becomes a Dry Bones.

Super Mario Maker: Super Mario Maker is a side-scrolling platform video game and game creation system developed and published by Nintendo for the Wii U game console, which released worldwide in September 2015.  Players are able to create and play their own custom courses, based on "Super Mario Bros.", "Super Mario Bros. 3", "Super Mario World" and "New Super Mario Bros.  U", and share them online.  Over time, new editing tools are unlocked, allowing players to download and play courses designed by other players.

Yoshi's Island: Super Mario World 2: Yoshi's Island is a 1995 platform video game developed and published by Nintendo for the Super Nintendo Entertainment System.  A prequel to the "Mario" franchise, the game casts players as Yoshi as he escorts Baby Mario through nearly 50 levels in order to reunite him with his brother Luigi, who had been kidnapped by Baby Bowser's minions.  Yoshi runs and jumps to reach the end of the level while solving puzzles and collecting items.  In a style new to the series, the game has a hand-drawn aesthetic and is the first to have Yoshi as its main character.  The game introduces his signature abilities to flutter jump, produce eggs from swallowed enemies, and transform into vehicles.

Yoshi: Yoshi (ヨッシー , Yosshī ) (English: or ), once romanized as Yossy, is a fictional anthropomorphic dinosaur who appears in video games published by Nintendo.  Yoshi debuted in "Super Mario World" (1990) on the Super Nintendo Entertainment System as Mario and Luigi's sidekick.  Yoshi later starred in platform and puzzle games, including "", "Yoshi's Story" and "Yoshi's Woolly World".  Yoshi also appears in many of the "Mario" spin-off games, including "Mario Party" and "Mario Kart", various "Mario" sports games, and Nintendo's crossover fighting game series "Super Smash Bros." Yoshi belongs to the species of the same name, which is characterized by their variety of colors.

Super Mario All-Stars: Super Mario All-Stars is a 1993 compilation of "Super Mario" platform video games developed and published by Nintendo for the Super Nintendo Entertainment System.  The game contains enhanced remakes of the four "Super Mario" games released for the Nintendo Entertainment System: "Super Mario Bros.", "Super Mario Bros. 2", "Super Mario Bros. 3", and "", the latter of which was the original Japanese version of "Super Mario Bros. 2" which was never released outside Japan prior to this compilation.  The games were restructured to take advantage of the Super NES hardware, featuring updated graphics and sounds and additional save mechanisms.

List of Yoshi video games: The Yoshi video game series is a franchise of platform games and puzzle games that is a spin-off of the "Mario" series published and produced by the Japanese gaming company Nintendo.  The games have been developed by a variety of developers including Nintendo, Game Freak, Intelligent Systems, Artoon, Arzest, and Good-Feel.  "Yoshi" games have been released for Nintendo video game consoles and handhelds dating from the Nintendo Entertainment System (NES) to the current generation of video game consoles.  Some of the original Nintendo Entertainment System and Super Nintendo Entertainment System games have been ported to Game Boy Advance or the Virtual Console (both, in the case of "Super Mario World").

Question: Koopa Troopas, or just simply Koopas, known in Japan as Nokonoko, are a fictional race of turtle or tortoise-like creatures from the "Mario" series, as well as its sister "Yoshi" series, they first appeared in Super Mario Bros., a Nintendo Entertainment System game, released in what year in the U.S., a platform video game developed and published by Nintendo, for the Nintendo Entertainment System home console?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "game_title": {
      "type": "string",
      "description": "The title of the video game."
    },
    "entity_first_appearance": {
      "type": "string",
      "description": "The entity that first appeared in the game."
    },
    "release_details": {
      "type": "object",
      "properties": {
        "region": {
          "type": "string",
          "description": "The region of release."
        },
        "year": {
          "type": "integer",
          "description": "The year of release in the specified region."
        }
      },
      "required": [
        "region",
        "year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "game_title",
    "entity_first_appearance",
    "release_details"
  ],
  "additionalProperties": false
}
