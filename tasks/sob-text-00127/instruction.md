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
Blue Rose (role-playing game): Blue Rose is a fantasy role-playing game published by Green Ronin Publishing in 2005.  The game is in the romantic fantasy genre—it is inspired by fantasy fiction such as that of Mercedes Lackey and Diane Duane as opposed to Robert E. Howard–style of swords and sorcery.  In romantic fantasy the emphasis is on role-playing and character interaction more than on combat.  The game uses a derivative of the D20 system, called True20.  Blue Rose won the Gen Con ENWorld Roleplaying Silver Medal for Best Rules in 2005.  Green Ronin subsequently released True20 as a separate system without a setting and genre neutral.

Anders Blixt: Anders Blixt (born 1959) is a Swedish game designer and science journalist.  He is one of the most well-published designers of role playing games in Sweden and has had a leading role in the production of most of them, including classical titles such as Drakar och Demoner and Mutant.

Forgotten Realms: Forgotten Realms is a campaign setting for the "Dungeons & Dragons" ("D&D") fantasy role-playing game.  Commonly referred to by players and game designers alike as "The Realms", it was created by game designer Ed Greenwood around 1967 as a setting for his childhood stories.  Several years later, Greenwood brought the setting to the "D&D" game as a series of magazine articles, and the first Realms game products were released in 1987.  Role-playing game products have been produced for the setting ever since, as have various licensed products including sword and sorcery novels, role-playing video game adaptations (including the first massively multiplayer online role-playing game to use graphics), and comic books.  The Forgotten Realms is one of the most popular "D&D" settings, largely due to the success of novels by authors such as R. A. Salvatore and numerous role-playing video games, including "Pool of Radiance" (1988), "Eye of the Beholder" (1991), "Baldur's Gate" (1998), "Icewind Dale" (2000) and "Neverwinter Nights" (2002).

Tunnels &amp; Trolls: Tunnels & Trolls (abbreviated "T&T") is a fantasy role-playing game designed by Ken St. Andre and first published in 1975 by Flying Buffalo.  The second modern role-playing game published, it was written by Ken St. Andre to be a more accessible alternative to "Dungeons & Dragons" and is suitable for solitaire, group, and play-by-mail gameplay.

Alshard: Alshard (アルシャード ) is a Japanese role-playing game designed by Jun'ichi Inoue and FarEast Amusement Research.  It was released in July 2002.  The current, version 1.5, known as Alshard fortissimo or Alshard ff (アルシャードフォルティッシモ,アルシャードff ) was published in July 2005.  It is a fantasy role-playing game with mechanical items like as Final Fantasy.  Alshard's game system is named Standard RPG System (SRS for short) and is used in other games such as Tenra War and Kaze no Stigma RPG and so on.  SRS including Alshard series is one of the largest role-playing game systems published in Japan.

Drakar och Demoner: Drakar och Demoner (Swedish for "Dragons and Demons", in Sweden commonly referred to by the abbreviation "DoD") is a Swedish fantasy role-playing game first published in 1982 by the game publishing company Äventyrsspel ("Adventure Games", later renamed Target Games).

Frank Mentzer: Jacob Franklin "Frank" Mentzer III (born in 1950), is an American fantasy author and game designer best known for his work on early materials for the "Dungeons & Dragons" (D&D) fantasy role-playing game.  He was a performing folk musician from 1968 to 1975, and played one concert at the White House during the administration of Richard Nixon.  He was an employee of TSR, Inc. from 1980–1986, spending part of that time as Creative Advisor to the Chairman of the Board, Gary Gygax.  He also founded the Role-Playing Games Association (RPGA) during his time with TSR.  He has been closely involved with the world's largest game auction at the Gen Con game convention since 1983, and is an expert on, and a major collector of, family boardgames and role-playing games.  After Gygax was ousted from TSR at the end of 1985, Mentzer left TSR as well and helped him to start New Infinities Productions Inc. (NIPI).  When this venture failed, Mentzer left the gaming industry, eventually becoming the manager of a bakery.  In 2008, he closed down this business and, two years later, announced he was returning to the gaming industry as a founding partner of a new publishing company, Eldritch Enterprises.

Pagan Publishing: Pagan Publishing is a role-playing game publishing company founded by John Scott Tynes in 1990.  It began by publishing a "Call of Cthulhu" role-playing game fanzine, "The Unspeakable Oath".  In 1994, the company moved from Columbia, Missouri to Seattle, Washington where it incorporated.  The staff at this time included John Tynes as editor-in-chief, John H. Crowe III as business manager, Dennis Detwiller as art director, and Brian Appleton and Chris Klepac as editors.  Tynes, Detwiller and Adam Scott Glancy released the "Delta Green" modern "Call of Cthulhu" campaign setting in 1996.  Pagan has released many other "Call of Cthulhu" products, including a foray into card games with "Creatures & Cultists" and miniature games with "The Hills Rise Wild! ".

Ravenloft (module): Ravenloft is an adventure module for the "Dungeons & Dragons" ("D&D") fantasy role-playing game.  The American game publishing company TSR, Inc. released it as a standalone adventure booklet in 1983 for use with the first edition "Advanced Dungeons & Dragons" game.  It was written by Tracy and Laura Hickman, and includes art by Clyde Caldwell with maps by David Sutherland III.  The plot of "Ravenloft" focuses on the villain Strahd von Zarovich, a vampire who pines for his lost love.  Various story elements, including Strahd's motivation and the locations of magical weapons, are randomly determined by drawing cards.  The player characters attempt to defeat Strahd and, if successful, the adventure ends.

Palladium Fantasy Role-Playing Game: The Palladium Fantasy Role-Playing Game (often shortened to Palladium Fantasy or PFRPG) is a game produced by Palladium Books.  It is set in the Palladium world (use of the unofficial name "Palladia" is discouraged by the publisher) some 10,000 years after a great war between the elves and dwarves.  First published in July 1983 as "The Palladium Role-Playing Game", the "Palladium Fantasy Role-Playing Game" saw a second edition in April 1996.  The two are largely compatible, though the second edition uses a later iteration of Palladium's ruleset to be more compatible with the rest of their Megaverse.

Question: Anders Blixt had a leading role in the production of a Swedish fantasy role-playing game that was first published in 1982 by what publishing company?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "game_name": {
      "type": "string",
      "description": "The name of the role-playing game."
    },
    "publisher_name": {
      "type": "string",
      "description": "The name of the publishing company."
    },
    "publication_year": {
      "type": "integer",
      "description": "The year the game was first published."
    },
    "designer_involvement": {
      "type": "string",
      "description": "Description of the designer's role in the game's production."
    }
  },
  "required": [
    "game_name",
    "publisher_name",
    "publication_year",
    "designer_involvement"
  ],
  "additionalProperties": false
}
