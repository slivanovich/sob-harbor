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
Robot Commando: Robot Commando is a single-player roleplaying gamebook written by Steve Jackson (the American game designer, rather than the series co-creator), illustrated by Gary Mayes and originally published in 1986 by Puffin Books.  It forms part of Steve Jackson and Ian Livingstone's Fighting Fantasy series.  It is the 22nd in the series in the original Puffin series (ISBN  ).  There are currently no announced plans to republish this book as part of the modern Wizard series.

Ogre Battle 64: Person of Lordly Caliber: Ogre Battle 64: Person of Lordly Caliber (オウガバトル64 Person of Lordly Caliber , Ōga Batoru Rokujūyon Pāson obu rōdorī Kyaribā ) , sequel to "", is a real-time strategy role-playing video game developed by Quest and published by Atlus for the Nintendo 64 in 2000.  Though conceptually similar to the original "Ogre Battle", significant game play tweaks were implemented to improve the game's overall flow.  "Ogre Battle 64" is the third game in the series, the first two being "", and "".  Gaidens have been released in Japan, on Game Boy Advance and Neo Geo Pocket Color.  Unlike earlier "Ogre Battle" games, which feature "Queen" song titles, "Person of Lordly Caliber" is an original title.  "Ogre Battle 64" was released in Japan, Europe/Australia and North America via the Virtual Console on Wii in early 2010 making it available in Europe and Australia for the first time.  In February 2017, it was released for the Wii U Virtual Console in Europe/Australia and North America.  It was released for the Wii U Virtual Console in Japan during July 2017.

Steve Jackson (American game designer): Steve Jackson (born c. 1953 ) is an American game designer.

Wizard (board game): "Wizard" was designed by Steve Jackson, later of Steve Jackson Games, and released by Metagaming in 1978 as Microgame #6 as a magic-based pocket board game of individual combat.  It was based on Metagaming's earlier Melee (game) release, with the difference being that it added magic to the game system.  "Melee", "Wizard" and gamemaster supplement "In the Labyrinth" eventually formed Metagaming's "The Fantasy Trip" fantasy role-playing system.  Both "Melee" and "Wizard" were expanded and re-released as "Advanced Wizard" and "Advanced Melee", with many role-playing elements added to the basic fantasy combat system.  When Steve Jackson released GURPS years later, the magic system in its fantasy supplements took some ideas from Wizard.

Demons of the Deep: Demons of the Deep is a single-player roleplaying gamebook written by Steve Jackson (the American game designer, rather than the series co-creator), illustrated by Duncan Smith and originally published in 1984 by Puffin Books.  It forms part of Steve Jackson and Ian Livingstone's Fighting Fantasy series.  It is the 19th in the series in the original Puffin series (ISBN  ).  There are currently no announced plans to republish this book as part of the modern Wizard series.

Walter Milliken: Walter Milliken is a writer and game designer who has worked on a number of "GURPS" products for Steve Jackson Games.

Creature of Havoc: Creature of Havoc is a single-player roleplaying gamebook written by British game designer Steve Jackson (not to be confused with the US game designer of the same name), illustrated by Alan Langford and originally published in 1986 by Puffin Books.  It was later republished by Wizard Books in 2002.  It forms part of Jackson and Ian Livingstone's fictional Fighting Fantasy series, and is the last Fighting Fantasy gamebook written by Jackson.  It is the 24th in the series in the original Puffin series (ISBN  ) and 4th in the modern Wizard series (ISBN  ).

Ogre (2017 video game): Ogre is an upcoming 2017 computer game developed by Bristol-based studio Auroch Digital, based on the "Ogre" tabletop wargame by Steve Jackson.  It was initially announced as a stretch goal for the Kickstarter of "Ogre: Designer's Edition".

Killer: The Game of Assassination: Killer: The Game of Assassination is a live action role-playing game derived from the traditional "assassin" game.  Created by American game designer Steve Jackson and first published in 1981 or 1982 by his own game company, Steve Jackson Games, "Killer" is one of the oldest set of rules having been officially published to play the assassin game.

Scorpion Swamp: Scorpion Swamp is a single-player adventuring gamebook written by Steve Jackson (the American game designer, as opposed to the series co-creator), illustrated by Duncan Smith and originally published in 1984 by Puffin Books.  It forms part of Steve Jackson and Ian Livingstone's Fighting Fantasy series.  It is the 8th in the series in the original Puffin series (ISBN  ).  This was the first Fighting Fantasy book to be written by an author other than the co-creators of the series.

Question: What nationality is Steve Jackson, the game designer behind products such as "Ogre"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "designer_name": {
      "type": "string",
      "description": "The full name of the game designer."
    },
    "nationality": {
      "type": "string",
      "description": "The nationality of the game designer."
    },
    "associated_products": {
      "type": "array",
      "description": "A list of game products associated with this designer.",
      "items": {
        "type": "string"
      }
    },
    "company_founded": {
      "type": "string",
      "description": "The name of the game company founded by this designer."
    }
  },
  "required": [
    "designer_name",
    "nationality",
    "associated_products",
    "company_founded"
  ],
  "additionalProperties": false
}
