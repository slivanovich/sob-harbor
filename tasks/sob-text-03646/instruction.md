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
Tannin (monster): Tannin (Hebrew: תנין ‎ ‎ ) or Tunannu (Ugaritic: 𐎚𐎐𐎐 "Tnn", vocalized "tu-un-na-nu") was a <a href="sea%20monster">sea monster</a> in <a href="Ancient%20Canaanite%20religion">Canaanite</a>, <a href="Sanchuniathon">Phoenician</a>, and <a href="Jewish%20mythology">Hebrew mythology</a> used as a symbol of <a href="chaos%20%28cosmogony%29">chaos</a> and <a href="evil">evil</a>.

Dwyfan and Dwyfach: Dwyfan and Dwyfach, sometimes also called Dwyvan and Dwyvach, in Welsh mythology, were the equivalents of Noah or Deucalion who take their names from small rivers, as told in a flood legend from the Welsh Triads.  A great flood was caused by the monster Afanc, who dwelt in Llyn Llion (possibly Bala Lake).  All humans were drowned except Dwyfan and Dwyfach, who escaped in a mastless boat.  They built an imposing ship (or ark) called Nefyd Naf Neifion, on which they carried two of every living kind.  From Dwyfan and Dwyfach all of the island of Prydain (Britain) was repeopled.  Dwyfach appears to take her name from the small Dwyfach (Welsh: little "Dwy") River of Gwynedd (until 1974, Caernarvonshire) that flows into Cardigan Bay; Dwyfan would then derive from the river it enters, the Dwyfawr or Dwyfor (Welsh: great "Dwy"). A lake monster from Welsh mythology, the afanc can also be traced through references in British and Celtic folklore.

Ustad Mansur: Ustad Mansur (flourished 1590-1624) was a seventeenth-century Mughal painter and court artist.  He grew in acclaim during the reign of Jahangir (r. 1605 - 1627) during which period he excelled at depicting plants and animals.  He was the earliest artist to depict the dodo in colour, apart from being the first to illustrate the Siberian crane.  Towards the end of Akbar's reign, he gained the title of "ustad" (=master) and during the reign of Mughal Emperor Jahangir his masterpieces earned him the title of "Nãdir-al-’Asr" ("Unequalled of the age").  Although largely known for his natural history illustrations, he also portrayed people in various manuscript illustrations.

Keith Parkinson: Keith A. Parkinson (October 22, 1958 – October 26, 2005) was an American fantasy artist and illustrator known for book covers and artwork for games such as "EverQuest", "Guardians", "", and "".  After designing book and magazine covers for TSR, Parkinson moved into game design in the 1990s, and co-designed the collectible card game "Guardians".  Parkinson died of leukemia in 2005, just four days after his 47th birthday.

Monster High: Monster High is an American fashion doll franchise created by Mattel and launched in July 2010.  The characters are inspired by monster movies, sci-fi horror, thriller fiction, and various other creatures.  Monster High was created by Garrett Sander, with illustrations by Kellee Riley and illustrator Glen Hanson.

Monster Manual: The Monster Manual (MM) is the primary bestiary sourcebook for monsters in the "Dungeons & Dragons" ("D&D") fantasy role-playing game, first published in 1977 by TSR.  It includes monsters derived from mythology, and folklore, as well as creatures created for "D&D" specifically.  It describes each with game-specific statistics (such as the monster's level or number of hit dice), and a brief description of its habits and habitats.  Most of the entries also have an image of the creature.  Along with the "Player's Handbook" and "Dungeon Master's Guide", it is one of the three "core rulebooks" in most editions of the "D&D" game.  Several editions of the "Monster Manual" have been released for each edition of "D&D".  It was the first hardcover book of the "D&D" series.  Due to the level of detail and illustration included, it was cited as a pivotal example of a new style of wargame books.  Future editions would draw on various sources and act as a compendium of published monsters.

WarWizard: WarWizard was a fantasy role-playing video game that was released as shareware in 1993, first for Amiga, then ported to MS-DOS for IBM-compatible computers.  It was developed by MicroGenesis, a small company founded by Brad McQuaid and Steve Clover in 1989.  Today, the game is most notable as the commercial start for McQuaid, Clover, and artist Milo Cooper, who later worked together at Sony Online Entertainment on "EverQuest" and at Sigil Games Online on "".

Monster Mythology: Monster Mythology is a sourcebook for the second edition of the "Dungeons & Dragons" roleplaying game.  Released by TSR in 1992 and written by Carl Sargent, with interior illustrations by Terry Dykstra, John and Laura Lakey, and Keith Parkinson, "Monster Mythology" was released as a companion volume for "Legends & Lore".  This book contains detailed information on the societies, cultures, myths, and deities of several non-human pantheons, including those of the elves, dwarves, gnomes, halflings, orcs, goblins, dragons, giants, drow, and many other creatures.

Happy Birthday, Cookie Monster: Happy Birthday, Cookie Monster (ISBN  ) is a children's book by Felice Haus, with illustrations by Carol Nicklausm published 1986 by Random House.  The book features Cookie Monster, a character from the PBS children's television series, "Sesame Street".  The book was honoured as an International Reading Association Children's Choice.

Winifred Milius Lubell: Winifred Milius Lubell (June 14, 1914 – January 3, 2012) was an American illustrator artist and writer.  In her early adult years, Milius was active in the Communist Party of the United States and an advocate for social justice.  She began her artistic career creating pen and ink portraits of victims of the Great Depression, before proceeding to examine the struggles of the working poor in the towns of the Eastern United States through woodcuts, as well as producing drawings from the sit down strikes in Chicago.  An artist and an illustrator, Milius' most notable publications include the illustrations for Dorothy Sterling's Cape Cod natural history book "The Outer Lands".  In her eighties she wrote and illustrated the women's studies exploration of feminism, sexuality and mythology: "The Metamorphosis of Baubo, Myths of Woman's Sexual Energy".  She died on January 3, 2012 of congestive heart failure.  She was 97.

Question: Monster Mythology has illustrations by which Everquest artist?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "artist_name": {
      "type": "string",
      "description": "The full name of the artist."
    },
    "illustrated_work": {
      "type": "string",
      "description": "The title of the work illustrated by the artist."
    },
    "other_notable_work": {
      "type": "string",
      "description": "Another significant work the artist is known for, as specified in the question."
    },
    "artist_details": {
      "type": "object",
      "properties": {
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the artist."
        },
        "death_year": {
          "type": "integer",
          "description": "The death year of the artist."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the artist."
        },
        "known_for_genre": {
          "type": "string",
          "description": "The genre the artist is primarily known for."
        }
      },
      "required": [
        "birth_year",
        "death_year",
        "nationality",
        "known_for_genre"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "artist_name",
    "illustrated_work",
    "other_notable_work",
    "artist_details"
  ],
  "additionalProperties": false
}
