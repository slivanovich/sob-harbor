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
Steve Feak: Steve Feak (born August 1, 1984), better known by the in-game name Guinsoo, is an American game designer.  He was one of the previous designers of the popular "" custom game mode, "DotA: Allstars".  Feak attracted the attention of the game industry and Riot Games, when his mod was played by 10 million gamers.  He began this project while studying computer science at the University of Wisconsin.  Since then, Feak was employed by Riot Games as a game designer for "League of Legends", a multiplayer online battle arena (MOBA) game directly inspired by his previous work.

PlayerUnknown's Battlegrounds: PlayerUnknown's Battlegrounds (PUBG) is a multiplayer online battle royale video game developed and published by PUBG Corp., a subsidary of Korean publisher Bluehole.  The game is based on previous mods that were developed by Brendan "PlayerUnknown" Greene for other games using the 2000 film "Battle Royale" for inspiration, and expanded into a standalone game under Greene's creative direction.  In the game, up to one hundred players parachute onto an island and scavenge for weapons and equipment to kill others while avoiding getting killed themselves.  The available safe area of the game's map decreases in size over time, directing surviving players into tighter areas to force encounters.  The last player or team standing wins the round.

Heroes of the Storm: Heroes of the Storm (HotS) is a multiplayer online battle arena video game developed and published by Blizzard Entertainment for Microsoft Windows and macOS that was released on June 2, 2015.  The game features heroes from Blizzard's franchises including "Warcraft", "Diablo", "StarCraft", "The Lost Vikings", and "Overwatch".  The game uses both free-to-play and freemium models and is supported by micropayments, which can be used to purchase heroes, visual alterations for the heroes in the game, and mounts.  Blizzard does not call the game a "multiplayer online battle arena" or an "action real-time strategy" because they feel it is something different with a broader playstyle; they refer to it as an online "hero brawler".

Infinite Crisis (video game): Infinite Crisis was a 2015 multiplayer online battle arena (MOBA) video game based on the fictional universe of DC Comics, developed by Turbine and published by Warner Bros.  Interactive Entertainment, loosely based on the comic book series of the same name.  The game featured two squads of DC heroes and villains as they competed in combats across multiple destructive battlefields featuring in-game changing catastrophic events.  It was a free-to-play game that was supported by micro-transactions.

Shroud (streamer): Michael Grzesiek (born June 2, 1994), better known by his in-game name Shroud, is a Canadian professional "" and "PlayerUnknown's Battlegrounds" player.  He joined Cloud9 on September 1, 2014.  He is one of the most well known "Counter-Strike: Global Offensive" and "PlayerUnknown's Battlegrounds" players in the World.

Multiplayer online game: A multiplayer online game is a multiplayer video game which can be played via a game server over the internet, with other players around the world.  Some prominent examples of this include fighting games (e.g. "Street Fighter IV" and "Tekken 6"), sports games (e.g. "NHL 14" and "Grid Autosport"), first-person shooters ("Battlefield", "Call of Duty", and "Counter-Strike"), a subgenre of shooter games called hero shooters ("Overwatch" and "Paladins"), strategy video games (e.g. "Total War", "Civilization", and "StarCraft II"), and a subgenre of strategy games called multiplayer online battle arena (e.g. "League of Legends", "Dota 2", "Smite, and "Heroes of the Storm").

End of Nations: End of Nations is an unreleased multiplayer online battle arena video game for Microsoft Windows.  It was being developed in-house by Trion Worlds.  It combined the aesthetics and tone of the sci-fi genre and put it in a multiplayer online battle arena (MOBA) game.  It is presumed cancelled.  Trion has since removed all mention of End of Nations from their website.

Dota 2: Dota 2 is a free-to-play multiplayer online battle arena (MOBA) video game developed and published by Valve Corporation.  The game is the stand-alone sequel to "Defense of the Ancients" ("DotA"), which was a community-created mod for Blizzard Entertainment's "" and its expansion pack, "".  "Dota 2" is played in matches between two teams of five players, with each team occupying and defending their own separate base on the map.  Each of the ten players independently controls a powerful character, known as a "hero", who all have unique abilities and differing styles of play.  During a match, the player collects experience points and items for their heroes in order to successfully fight the opposing team's heroes, who are doing the same.  A team wins by being the first to destroy a large structure located in the opposing team's base, called the "Ancient", which is guarded by defensive towers.

Clash Royale: Clash Royale is a freemium mobile tower rush video game developed and published by Supercell.  The game combines elements from collectible card games, tower defense, and multiplayer online battle arena.  The game was released globally on March 2, 2016.

ESports: eSports (also known as electronic sports, esports, e-sports, competitive (video) gaming, professional (video) gaming, or pro gaming) are a form of competition that is facilitated by electronic systems, particularly video games; the input of players and teams as well as the output of the eSports system are mediated by human-computer interfaces.  Most commonly, eSports take the form of organized, multiplayer video game competitions, particularly between professional players.  The most common video game genres associated with eSports are real-time strategy, fighting, first-person shooter (FPS), and multiplayer online battle arena (MOBA).  Tournaments such as The International, the "League of Legends" World Championship, the Evolution Championship Series and the Intel Extreme Masters provide live broadcasts of the competition, and prize money to competitors.

Question: Michael Grzesiek (born June 2, 1994), better known by his in-game name Shroud, is a Canadian professional "" and "PlayerUnknown's Battlegrounds" player, PlayerUnknown's Battlegrounds (PUBG) is a multiplayer online battle royale video game developed and published by PUBG Corp., a subsidary of which Korean publisher ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "game_name": {
      "type": "string",
      "description": "The name of the video game."
    },
    "developer": {
      "type": "string",
      "description": "The developer of the game."
    },
    "publisher": {
      "type": "string",
      "description": "The primary publisher of the game."
    },
    "parent_publisher": {
      "type": "string",
      "description": "The parent company or main publisher, if the primary publisher is a subsidiary."
    },
    "parent_publisher_country": {
      "type": "string",
      "description": "The country of origin of the parent publisher."
    }
  },
  "required": [
    "game_name",
    "developer",
    "publisher",
    "parent_publisher",
    "parent_publisher_country"
  ],
  "additionalProperties": false
}
