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
Wings (1996 video game): Wings is a freeware computer game (originally shareware) created by Miika Virpioja.  A 2D, DOS-based computer game with space ships that behave like lunar landers.  You can select one of 33 weapons, and the surroundings can be destroyed.  The game features multiplayer capabilities, either through linked PCs or two or more players using one keyboard plus gamepads/joysticks.  In the original shareware version certain weapons were locked until the game was registered.  The game includes a level editor.

Monty Python's Flying Circus: The Computer Game: Monty Python's Flying Circus: The Computer Game (referred to simply as Monty Python's Flying Circus in the game itself) is a 1990 scrolling shoot 'em up computer game developed by Core Design.  It was released by Virgin Games for various computer formats including the Commodore Amiga, Commodore 64, Amstrad CPC and the Sinclair ZX Spectrum.  It is loosely based on material and characters from the 1970s British comedy series "Monty Python's Flying Circus", in particular the Gumby character.

Zen of Sudoku: Zen of Sudoku is a Sudoku based computer game developed by Charlie Cleveland of Unknown Worlds Entertainment and released on June 20, 2006.  Although the casual games market is not the intended direction of Unknown Worlds, or of Cleveland, "Zen of Sudoku" was produced in order to generate revenue towards funding "Natural Selection 2", a sequel to the original "Natural Selection" modification for Half-Life.  Cleveland cites casual games development as a "last option" for funding this sequel, having been unwilling to sacrifice control of the company to external investors.

The Specialists: The Specialists is a multiplayer modification for the first-person shooter computer game "Half-Life".

Half-Life 2: Deathmatch: Half-Life 2: Deathmatch is a multiplayer first-person shooter video game developed by Valve Corporation.  Released on Steam on November 30, 2004, it uses many of the assets from "Half-Life 2" and its Source engine.  It features new levels, optimized for multiplayer arena play, and a few new weapons.  Also included are portions of the game's source code, which were the basis for many early Source-based multiplayer modifications.  The game is the successor to the popular multiplayer component of the original "Half-Life", but is offered as a separate product from "Half-Life 2".  "Deathmatch", like "Half-Life"' s multiplayer, does not develop any part of the plot or story of the "Half-Life" series.

DarkSpace: DarkSpace is a massively multiplayer real-time strategy computer game developed by PaleStar.  Released in December 2001, DarkSpace involves multiplayer spaceship combat between three player-controlled factions.

Beyond Protocol: Beyond Protocol was a subscription based Sci-Fi Massively multiplayer online real-time strategy game (MMORTS) Computer Game developed by the independent game developer Dark Sky Entertainmentand and released in November 2008.  The 3D game modelled a persistent and player-driven fictional galaxy.  Beyond Protocol was an entirely Player versus player (PvP) game, no Non-player characters (NPCs) exist within the game, all activities (trade, combat, and diplomacy) happened between the players.

Half-Life (video game): Half-Life (stylized as HλLF-LIFE) is a science fiction first-person shooter video game developed by Valve, released in 1998 by Sierra Studios for Microsoft Windows.  It was Valve's debut product and the first in the "Half-Life" series.  Players assume the role of Dr. Gordon Freeman, who must fight his way out of a secret research facility after a teleportation experiment goes disastrously wrong, fighting enemies and solving puzzles.

I.G.I.-2: Covert Strike: I.G.I.-2 : Covert Strike is an action shooting computer game developed by Innerloop Studios and released by Codemasters in 2003.  The game is a stealth-based first person shooter.  It is the sequel to Innerloop's "".  The original, published by Eidos Interactive, offered only single-player play, and no game saves.  Covert Strike added multiplayer play and limited save game capability, but the game's many bugs led to poor sales, which contributed to Innerloop's demise.  Chris Ryan, a former Special Air Service operative best known for being the lone successful escapee of Bravo Two Zero, served as a consultant to the game.

John R. Taylor III: John R. Taylor (born January 13, 1957) is an American computer game designer, serial entrepreneur and massively multiplayer online game pioneer.  He is a co-founder (with his University of Virginia classmate Kelton Flinn) of the game company Kesmai, which they founded in 1981.  In 2011, Taylor was awarded the Online Game Legend Award by the Computer Game Developers Association.  and from Call of Duty Black Ops 3>

Question: The Specialists is a multiplayer modification for a computer game developed by what company?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "modification_name": {
      "type": "string",
      "description": "The name of the game modification."
    },
    "base_game_name": {
      "type": "string",
      "description": "The name of the computer game that was modified."
    },
    "base_game_developer": {
      "type": "string",
      "description": "The company that developed the base game."
    },
    "is_multiplayer": {
      "type": "boolean",
      "description": "Indicates if the modification is multiplayer."
    },
    "game_type": {
      "type": "string",
      "description": "The type of the base game, e.g., 'first-person shooter'."
    }
  },
  "required": [
    "modification_name",
    "base_game_name",
    "base_game_developer",
    "is_multiplayer",
    "game_type"
  ],
  "additionalProperties": false
}
