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
Realm of Chaos (Warhammer): The first version of Realm of Chaos is a two-volume publication by Games Workshop concerning the forces of Chaos.  The hardback books contain background material and rules for "Warhammer Fantasy Roleplay" (1st edition), "Warhammer 40,000: Rogue Trader" and "Warhammer Fantasy Battle" (3rd edition).

Warhammer Fantasy Battle: Warhammer: The Game of Fantasy Battles (formerly Warhammer Fantasy Battle and often abbreviated to Warhammer, WFB, and WHFB) is a tabletop wargame created by Games Workshop, and is the origin of the "Warhammer Fantasy" setting.  The game is designed for regiments of miniatures of various fantasy races such as humans (The Empire, Bretonnia, Kislev), Elves (Dark Elves, High Elves, Wood Elves), Dwarfs, Undead, and Orcs and Goblins, as well as some more unusual types such as Lizardmen, Skaven and the daemonic forces of Chaos, with each race having its own unique strengths and weaknesses.

Fimir: Fimir are a fantasy race created by Graeme Davis and Jes Goodwin at the end of the 1980s for Warhammer Fantasy Roleplay (WFRP) and the 3rd edition of Warhammer Fantasy Battle (WFB).

Black Library: The Black Library is a division of Games Workshop (formerly a part of BL Publishing) which is devoted to publishing novels and audiobooks (and has previously produced art books, background books, and graphic novels) set in the "Warhammer Fantasy Battle" and "Warhammer 40,000" fictional universes.  The publishing company took their name from the fictional Black Library in "Warhammer 40,000", where the Eldar race keep their stored knowledge of Chaos and the Necrons.  Some of Black Library's best known titles include the Gaunt's Ghosts and Eisenhorn series of novels by Dan Abnett and the Gotrek and Felix series by William King and Nathan Long.

Warhammer Fantasy (setting): Warhammer Fantasy is a high fantasy fictional universe created by Games Workshop and used in many of its games, including the table top wargame "Warhammer Fantasy Battle", the "Warhammer Fantasy Roleplay" (WFRP) pen-and-paper role-playing game, and the MMORPG "".

John Blanche: John Blanche is a British fantasy and science fiction illustrator and modeler known for his work for Games Workshop's White Dwarf magazine, Warhammer Fantasy Battle, Warhammer Fantasy Roleplay and Warhammer 40,000 games and his role as art director for the company, including his work in the field of fantasy miniature painting, and for illustrations for various game book and Fighting Fantasy publications.

Undead (Warhammer): The Undead of the Warhammer Fantasy Tabletop Wargame (Games Workshop ltd.), were introduced to the game in its very earliest editions.  The term itself can refer either to the undivided and all-inclusive army—ranging from ghosts and vampires to skeletons and mummies—or to the separate components which make up the two: The Tomb Kings of Khemri, and the Vampire Counts.  Up to and including the fifth edition of Warhammer Fantasy Battle, the Undead represented the combined forces.  For the sixth edition, Games Workshop divided the Undead into two separate armies to represent the chaos which Nagash created when he cast his Spell of Awakening to begin his assault on the lands of the living.

Mighty Empires: Mighty Empires was a board game published by Games Workshop.  It was intended to add a strategic layer to Warhammer Fantasy Battle giving rise to campaigns where the results of one battle would affect later battles, although the game included simple point based rules if the players did not have Warhammer Fantasy Battle or were unwilling to play out each battle.

Von Carstein: The Von Carsteins are a vampiric bloodline in the fictive setting of "Warhammer Fantasy", including the Warhammer Fantasy Battle tabletop wargame.  Their stories are told through background material in publications such as "Warhammer Armies: Undead" and "Vampire Counts" and in a trilogy of novels by Steven Savile; all three of which are published, "Inheritance", "Dominion" and "Retribution".

Man O' War (game): Man O' War (sometimes also written as “Manowar”) is a now out-of-print table top war game by Games Workshop.  The game was set in the same realm of Warhammer Fantasy as used for the Warhammer Fantasy Battle and included most of the factions from that setting.  Other races of the Warhammer world were not included, either because they were lacking seafaring abilities (Wood Elves), missing from the main factions at that time (Ogres, Lizardmen), or both.

Question: Warhammer Fantasy Battle contains which race that includes ghosts and vampires?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "race_name": {
      "type": "string",
      "description": "The name of the fantasy race."
    },
    "game_name": {
      "type": "string",
      "description": "The name of the game where the race is featured."
    },
    "publisher": {
      "type": "string",
      "description": "The publisher of the game."
    },
    "included_creatures": {
      "type": "array",
      "description": "A list of creature types that are part of this race.",
      "items": {
        "type": "string"
      }
    },
    "sub_factions": {
      "type": "array",
      "description": "Separate components or sub-factions that make up the race.",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "race_name",
    "game_name",
    "publisher",
    "included_creatures"
  ],
  "additionalProperties": false
}
