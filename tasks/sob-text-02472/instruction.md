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
Sorcerer (role-playing game): Sorcerer is an award winning occult-themed indie role-playing game written by Ron Edwards and published through Adept Press.  The game focuses on sorcerers who summon, bind, and interact with demons, powerful non-human entities who work with and against the sorcerer.

Indie role-playing game: An indie role-playing game is a role-playing game published outside of traditional, "mainstream" means.  Varying definitions require that commercial, design, or conceptual elements of the game stay under the control of the creator, or that the game should just be produced outside of a corporate environment.

Diana: Warrior Princess: Diana: Warrior Princess is an indie role-playing game written by Marcus Rowland and initially published by Heliograph Incorporated, based on an article describing the setting which originally appeared in "Valkyrie" magazine.  It is distributed as a PDF via Steve Jackson Games.  It describes a fictionalised version of the twentieth century as it might be seen a few thousand years from now.

Uresia: Grave of Heaven: Uresia: Grave of Heaven is an anime-inspired fantasy world for role-playing games written by S. John Ross.  Originally published for the "Big Eyes, Small Mouth" role-playing game, the most recent edition published in 2012 is systemless.  Like the previous edition, it includes maps drawn by the author.  "Uresia" was originally published by Guardians of Order.

Lexicon (game): Lexicon is a computer-assisted role-playing game invented by Neel Krishnaswami and popularised by the indie role-playing game community.  As originally proposed, it is played online using wiki software.  Players assume the role of scholars who write the history and background of a particular fictitious time, setting, or incident.  As the game goes on, the players collaboratively create an elaborately interwoven account.

Polaris (2005 role-playing game): Polaris: Chivalric Tragedy at Utmost North (2005) is an indie role-playing game written by Ben Lehman and published by These Are Our Games.  "Polaris" is a collaborative roleplaying game, and as such differs from many role-playing games in that there is no single "game master".  A player's "opposition" is controlled by the other players in the game.

The Shadow of Yesterday: The Shadow of Yesterday (or TSoY) is a narrativist sword and sorcery (with optional elements of heroic fantasy) indie role-playing game, designed by Clinton R. Nixon and published by CRN Games.

Halcyon (role-playing game): Halcyon is an indie role-playing game, independently published by Neuwerld Studios among two editions.  The "Player Codex" was released in 2008 in softcover format, replaced in 2010 by the illustrated "Core Rulebook" in hardcover format.

Risus: Risus: The Anything RPG is a rules-light generic role-playing game (RPG) written, designed and illustrated by S. John Ross of Cumberland Games and Diversions.  "Risus" is available free on the web.  It was first published online in 1993.  Earlier versions of the game were titled GUCS: The Generic Universal Comedy System (a parody of "GURPS") and were distributed privately beginning in 1989.

S. John Ross (game designer): Samuel John Ross, Jr., known as S. John Ross, is a game designer and owner of Cumberland Games & Diversions.  He wrote the early Indie role-playing game Risus.

Question: When was the early Indie role-playing game written by S.John Ross was first published?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "game_name": {
      "type": "string",
      "description": "The name of the role-playing game."
    },
    "author_name": {
      "type": "string",
      "description": "The name of the game's author."
    },
    "first_publication_year": {
      "type": "integer",
      "description": "The year the game was first published."
    }
  },
  "required": [
    "game_name",
    "author_name",
    "first_publication_year"
  ],
  "additionalProperties": false
}
