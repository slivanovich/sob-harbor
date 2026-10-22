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
Ryu Hayabusa: Ryu Hayabusa (Japanese: リュウ・ハヤブサ/隼 龍 , Hepburn: Hayabusa Ryū ) is a fictional character who serves as the protagonist of Tecmo's "Ninja Gaiden" action-adventure video game series, in addition to featuring as a player character in the "Dead or Alive" fighting game franchise by Koei Tecmo and Team Ninja.  He is a dragon-human hybrid who wields an ancestral weapon called the Dragon Sword, and is the leader of the Hayabusa ninja clan.  One of Tecmo's most enduring characters, Ryu has appeared on official series merchandise as well as the feature film "", and has made many crossover appearances in other games.  He has received public and critical reception as one of the most iconic ninja in video games.

God of War video game collections: "God of War" is an action-adventure video game series loosely based on Greek mythology.  Debuting in 2005, the series has become a flagship title for the PlayStation brand and the character Kratos is one of its most popular characters.  The series consists of seven games across multiple platforms.  Five of these have been re-released through three separate compilations for the PlayStation 3 (PS3) platform: "God of War Collection" (2009), "God of War: Origins Collection" (2011), and "God of War Saga" (2012).  With the exception of "God of War III" in the "God of War Saga", each collection features remastered ports of the games that were not originally released on the PS3.  "God of War III" was later remastered as "God of War III Remastered" and released on PlayStation 4 (PS4) in July 2015. ""  and "" are the only installments that have not been remastered for a newer platform or included in a collection.

Castlevania: Lament of Innocence: Castlevania: Lament of Innocence is an action-adventure video game developed by Konami for the PlayStation 2 console.  Belonging to Konami's "Castlevania" video game series, it is the first installment of the series on the PlayStation 2 and the third to make use of a 3D style of gameplay.  It was released in Japan and North America in late 2003 and Europe and Australia in early 2004.

Lego Batman 3: Beyond Gotham: Lego Batman 3: Beyond Gotham is a Lego-themed action-adventure video game developed by Traveller's Tales and published by Warner Bros.  Interactive Entertainment in November 2014 for multiple platforms.  It is the third installment in the "Lego Batman" video game series and a sequel to "" and "".  A port was released to mobile phones, excluding the numeral in the titile.

Dishonored: Dishonored is a 2012 stealth action-adventure video game developed by Arkane Studios and published by Bethesda Softworks.  Set in the fictional, plague-ridden industrial city of Dunwall, "Dishonored" follows the story of Corvo Attano, bodyguard to the Empress of the Isles.  He is framed for her murder and forced to become an assassin, seeking revenge on those who conspired against him.  Corvo is aided in his quest by the Loyalistsa resistance group fighting to reclaim Dunwall, and the Outsidera powerful being who imbues Corvo with magical abilities.  Several noted actors including Susan Sarandon, Brad Dourif, Carrie Fisher, Michael Madsen, Lena Headey and Chloë Grace Moretz provided voice work for the game.

List of Star Fox video games: The "Star Fox" video game series is a franchise of rail shooters and other action-adventure games published and produced by Nintendo.  The games have been developed by a variety of developers, but all of the games have had input from Nintendo.  All "Star Fox" video games have been developed exclusively for Nintendo video game consoles and handhelds dating from the Super Nintendo Entertainment System to the current generation of video game consoles.  The series debuted in Japan on February 21, 1993 with "Sutā Fokkusu" (スターフォックス , Sutā Fokkusu , lit.  "Star Fox") , which was later released in North America as "Star Fox" and in Europe as "Starwing".  The series revolves around the Star Fox team, a group of mercenaries hired to protect the Lylat system.  The leader of the group, Fox McCloud, is the protagonist of the series, and the only playable character in most of the games.  Currently, the series contains five games.  One reason the "Star Fox" series has remained popular is because of the shoot 'em up aerial sequences found in many of the games, which are recognized as the series' high points.  Dylan Cuthbert, one of the original creators of the series, noted that it was the combination of the on-rails aerial action and the in-game universe that made the games successful.

Metroid: Zero Mission: Metroid: Zero Mission is a side-scrolling action-adventure video game published by Nintendo, and developed by its Research & Development 1 (R&D1) division for the Game Boy Advance.  It is a remake of the 1986 game "Metroid"—the first installment in the "Metroid" video game series, and is designed to retell that entry's story with "Super Metroid"-like gameplay.  It was initially released in North America in February 2004.

Tomb Raider: Tomb Raider, also known as Lara Croft: Tomb Raider between 2001 and 2007, is a media franchise that originated with an action-adventure video game series created by British gaming company Core Design.  Formerly owned by Eidos Interactive, then by Square Enix after their acquisition of Eidos in 2009, the franchise focuses on a fictional English archaeologist Lara Croft, who travels around the world searching for lost artifacts and infiltrating dangerous tombs and ruins.  The gameplay generally focuses around action-adventure exploration of environments, solving puzzles, navigating hostile environments filled with traps, and fighting numerous enemies.  Additional media has grown up around the theme in the form of film adaptations, comics and novels.

Emily Kaldwin: Emily Kaldwin is a fictional character of the "Dishonored" series.  She is a lead protagonist in the sequel, "Dishonored 2".  In the story of the first game, she is the daughter of the Empress and the player-character, Corvo.  When the Empress is assassinated and Emily kidnapped, the player recovers Emily whereupon she serves as a moral compass by expressing herself differently based on the player's proclivity for violence in their gameplay choices.  Emily reigns for 15 years leading up to the sequel's story, when she is usurped and escapes to plot her revenge.  The developers noted Emily and her relationship with the player as one of the most compelling elements they took to the sequel.  Her announcement as its protagonist was unveiled as a surprise and welcomed by games journalists as emblematic of progress for female representation in video games, leading an industry trend towards more prevalent lead female protagonists at the 2015 Electronic Entertainment Expo.

Tomb Raider III: Tomb Raider III: Adventures of Lara Croft, or simply Tomb Raider III, is an action-adventure video game developed by Core Design and published by Eidos Interactive.  It was originally released for the PlayStation and Microsoft Windows platforms in 1998.  "Tomb Raider III" is the third title in the "Tomb Raider" video game series and a sequel to "Tomb Raider II".  The story of the game follows archaeologist-adventurer Lara Croft as she embarks upon a quest to recover four pieces of a meteorite that are scattered across the world.  To progress through the game, the player must explore five locations (India, South Pacific, London, Nevada, and Antarctica) and complete a series of levels that involve solving puzzles, jumping over obstacles, and defeating enemies.

Question: What is the setting for the action-adventure video game series which includes Emily Kaldwin as a character? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "game_series_name": {
      "type": "string",
      "description": "The name of the video game series."
    },
    "character_involved": {
      "type": "string",
      "description": "The name of the character mentioned in the question."
    },
    "setting": {
      "type": "object",
      "properties": {
        "description": {
          "type": "string",
          "description": "A detailed description of the game's setting."
        },
        "location_type": {
          "type": "string",
          "description": "The type of location for the setting (e.g., city, world, planet)."
        },
        "attributes": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Key attributes describing the setting."
        }
      },
      "required": [
        "description",
        "location_type",
        "attributes"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "game_series_name",
    "character_involved",
    "setting"
  ],
  "additionalProperties": false
}
