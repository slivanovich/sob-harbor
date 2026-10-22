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
Stephen R. Marsh: Stephen R. Marsh is an American game designer and lawyer best known for his contributions to early editions of TSR's "Dungeons & Dragons" fantasy tabletop role-playing game (RPG).  Some of the creatures he created for the original edition of "D&D" in 1975 have been included in every subsequent edition of the game.

Forgotten Realms: Forgotten Realms is a campaign setting for the "Dungeons & Dragons" ("D&D") fantasy role-playing game.  Commonly referred to by players and game designers alike as "The Realms", it was created by game designer Ed Greenwood around 1967 as a setting for his childhood stories.  Several years later, Greenwood brought the setting to the "D&D" game as a series of magazine articles, and the first Realms game products were released in 1987.  Role-playing game products have been produced for the setting ever since, as have various licensed products including sword and sorcery novels, role-playing video game adaptations (including the first massively multiplayer online role-playing game to use graphics), and comic books.  The Forgotten Realms is one of the most popular "D&D" settings, largely due to the success of novels by authors such as R. A. Salvatore and numerous role-playing video games, including "Pool of Radiance" (1988), "Eye of the Beholder" (1991), "Baldur's Gate" (1998), "Icewind Dale" (2000) and "Neverwinter Nights" (2002).

John Wick (game designer): John Wick is an American role-playing game designer best known for his creative contributions to the Alderac Entertainment Group (AEG) properties "Legend of the Five Rings" and "7th Sea".  He self-published Orkworld under the Wicked Press banner, and later co-founded the Wicked Dead Brewing Company with Jared Sorensen.  His games under that company include Cat, Schauermärchen, Enemy Gods, and Thirty.  He has won the Origins Award for Best Role-Playing Game and Best Collectible Card Game twice (for both the "Legend of the Five Rings" and "7th Sea" role-playing games and collectible card games).

Merle M. Rasmussen: Merle Martin Rasmussen is an American game designer and writer best known for creating the espionage role-playing game "Top Secret".

Top Secret (role-playing game): Top Secret is an espionage-themed role-playing game written by Merle M. Rasmussen and first published in 1980 by TSR, Inc.

Mark Nelson (video game designer): Mark Nelson is an American video game designer and humor writer best known for his work with Bethesda Game Studios and the game series The Elder Scrolls.  In March 2007, he joined computer games company Big Huge Games to create a new role-playing game, joining industry veteran Brian Reynolds and long-time collaborator Ken Rolston.

Matt James (game designer): Matt James (born 1981) is an American game designer and a decorated veteran of the United States Army.  As a game designer, James is best known for his online and print works for the "Dungeons & Dragons" fantasy role-playing game published by Wizards of the Coast, "Pathfinder" role-playing game by Paizo, and Privateer Press.  He has also designed game content for Wolfgang Baur's Kobold Press (formerly Open Design LLC).  In 2012 James won an ENnie Award for "" and has been nominated for several Origins Awards.  In 2014, James won an ENnie Award for "".

Brian Mitsoda: Brian Mitsoda (also credited as B. Mitsoda and b mitsoda) is an American video game designer and writer best known for his work on the 2004 game "".  He is the founder of DoubleBear Productions and is married to fellow writer/game designer Annie VanderMeer Mitsoda.

Dave Arneson: David Lance "Dave" Arneson (October 1, 1947 – April 7, 2009) was an American game designer best known for co-developing the first published role-playing game (RPG), "Dungeons & Dragons", with Gary Gygax, in the early 1970s.  Arneson's early work was fundamental to the development of the genre, developing the concept of the RPG using devices now considered to be archetypical, such as adventuring in "dungeons" and using a neutral judge who doubles as the voice and consciousness of all other characters to develop the storyline.

Killer: The Game of Assassination: Killer: The Game of Assassination is a live action role-playing game derived from the traditional "assassin" game.  Created by American game designer Steve Jackson and first published in 1981 or 1982 by his own game company, Steve Jackson Games, "Killer" is one of the oldest set of rules having been officially published to play the assassin game.

Question: Merle Martin Rasmussen is an American game designer and writer best known for creating which espionage-themed role-playing game, first published in 1980?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "game_name": {
      "type": "string",
      "description": "The name of the role-playing game."
    },
    "game_theme": {
      "type": "string",
      "description": "The theme of the role-playing game."
    },
    "publication_details": {
      "type": "object",
      "properties": {
        "first_published_year": {
          "type": "integer",
          "description": "The year the game was first published."
        }
      },
      "required": [
        "first_published_year"
      ],
      "additionalProperties": false
    },
    "creator_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the game's creator."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the game's creator."
        }
      },
      "required": [
        "name",
        "nationality"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "game_name",
    "game_theme",
    "publication_details",
    "creator_details"
  ],
  "additionalProperties": false
}
