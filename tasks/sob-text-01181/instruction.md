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
Pistol Pete (New Mexico State University): Pistol Pete is the mascot for the New Mexico State Aggies, the athletic teams of New Mexico State University in Las Cruces, New Mexico, USA.  Pistol Pete is portrayed by a NMSU student dressed in traditional cowboy attire, including a cowboy hat, a vest, and chaps, and armed with twirling pistols.  NMSU licenses Pistol Pete from Oklahoma State University for $10/year as part of a settlement of a copyright infringement lawsuit.

1977 Paris Open: The 1977 Paris Open, also known as the Jean Becker Open, was a men's tennis tournament played on indoor carpet courts that was part of the 1977 Grand Prix circuit.  It was the 9th edition of the Paris Open (later known as the Paris Masters).  It took place at the Palais omnisports de Paris-Bercy in Paris, France from 31 October 1977 through 6 November 1977.  Corrado Barazzutti won the singles title.

Pete Sampras: Pete Sampras (born August 12, 1971) is a retired American tennis player widely regarded as one of the greatest in the history of the sport.  He was a right-handed player with a single-handed backhand and a precise and powerful serve that earned him the nickname "Pistol Pete".  His professional career began in 1988 and ended at the 2002 US Open, which he won, defeating rival Andre Agassi in the final.

1998 Paris Open: The 1998 Paris Masters was a tennis tournament played on indoor carpet courts.  It was the 27th edition of the Paris Masters, and is part of the ATP Masters Series of the 1998 ATP Tour.  It took place at the Palais omnisports de Paris-Bercy in Paris, France, from 2 November through 9 November 1998.  Greg Rusedski won the singles title.

1975 Paris Open: The 1975 Paris Open, also known as the Jean Becker Open, was a Grand Prix men's tennis tournament played onindoor carpet courts.  It was the 7th edition of the Paris Open (later known as the Paris Masters).  It took place at the Palais omnisports de Paris-Bercy in Paris, France from 27 October through 2 November 1975.  Tom Okker won the singles title.

1998 Paris Open – Singles: Pete Sampras was the defending champion but lost to Greg Rusedski in the final, 6–4, 7–6, 6–3

Pistol Pete (Oklahoma State University): Pistol Pete is the athletics mascot of Oklahoma State University.  In the past, New Mexico State University and the University of Wyoming have both used mascots based on the original Oklahoma State "Pistol Pete" caricature artwork; however both schools have subsequently revised their Pistol Pete mascots so that they no longer resemble Oklahoma State's Pistol Pete.  The Pistol Pete mascot costume features traditional cowboy attire and a headpiece resembling Frank Eaton.  Pistol Pete has been the mascot for the Oklahoma State Cowboys since 1923.

1972 Paris Open: The 1972 Paris Open, also known as the Jean Becker Open Championships, was a men's tennis tournament played on indoor carpet courts.  The event was part of the Grand Prix circuit and classified as a B category tournament.  It was the 4th edition of the Paris Open (later known as the Paris Masters) and took place at the Palais omnisports de Paris-Bercy in Paris, France, from October 30 through November 5, 1972.  Stan Smith won the singles title.

1976 Paris Open: The 1976 Paris Open, also known as the Jean Becker Open, was a Grand Prix men's tennis tournament played on indoor carpet courts.  It was the 8th edition of the Paris Open (later known as the Paris Masters).  It took place at the Palais omnisports de Paris-Bercy in Paris, France from 25 October through 31 October 1976.  Eddie Dibbs won the singles title.

1980 Paris Open: The 1980 Paris Open, also known that year as the Crocodile Open, was a Grand Prix tennis tournament played on indoor carpet courts.  It was the 12th edition of the Paris Open (later known as the Paris Masters).  It took place at the Palais omnisports de Paris-Bercy in Paris, France from 27 October through 2 November 1980.  Brian Gottfried won the singles title.

Question: What player with the nickname "Pistol Pete" lost to Greg Rusedski in the 1998 Paris Open – Singles?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The full name of the tennis player."
    },
    "player_nickname": {
      "type": "string",
      "description": "The nickname of the tennis player."
    },
    "tournament_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the tennis tournament."
        },
        "year": {
          "type": "integer",
          "description": "The year the tournament took place."
        },
        "event": {
          "type": "string",
          "description": "The specific event within the tournament (e.g., Singles)."
        }
      },
      "required": [
        "name",
        "year",
        "event"
      ],
      "additionalProperties": false
    },
    "match_result": {
      "type": "object",
      "properties": {
        "opponent_name": {
          "type": "string",
          "description": "The name of the opponent the player lost to."
        },
        "outcome": {
          "type": "string",
          "description": "Description of the match outcome from the player's perspective."
        },
        "score": {
          "type": "string",
          "description": "The final score of the match."
        }
      },
      "required": [
        "opponent_name",
        "outcome",
        "score"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "player_name",
    "player_nickname",
    "tournament_details",
    "match_result"
  ],
  "additionalProperties": false
}
