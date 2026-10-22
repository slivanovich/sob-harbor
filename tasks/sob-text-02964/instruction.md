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
Arkham Horror: Arkham Horror is an adventure board game designed by Richard Launius, originally published in 1987 by Chaosium.  The game is based on Chaosium's roleplaying game "Call of Cthulhu", which is set in the Cthulhu Mythos of H.P. Lovecraft and other horror writers.  It was revised and reprinted by Fantasy Flight Games in 2005.  In this game, players take on the role of investigators in Lovecraft's Massachusetts town of Arkham.  Gates to other planes open throughout the town.  If too many gates open, a powerful alien being will enter, likely destroying the town and possibly threatening the world.  The investigators must avoid or fight alien creatures that enter Arkham through the gates, enter the gates themselves, survive the alien places beyond, return to Arkham, and close the gates.

The Shuttered Room and Other Pieces: The Shuttered Room and Other Pieces is an anthology fantasy, horror short stories, essays and memoirs by American author H. P. Lovecraft and others.  It was released in 1959 by Arkham House in an edition of 2,527 copies and was the fifth collection of Lovecraft's work to be released by Arkham House.  August Derleth, the owner of Arkham House, and an admirer and literary executor to Lovecraft, edited the collection and wrote the title story, "The Shuttered Room", as well as another story, "The Fisherman of Falcon Point" from lines of story ideas left by Lovecraft after his death.  Derleth billed himself as a "posthumous collaborator".

To Arkham and the Stars: "To Arkham and the Stars" is a short story written by Fritz Leiber in the Cthulhu Mythos genre of horror fiction.  It was written for the 1966 Arkham House anthology "The Dark Brotherhood and Other Pieces".  Set in H. P. Lovecraft's Arkham and Miskatonic University, it includes characters from and allusions to several Lovecraft stories.

Music of Batman: Arkham City: The "Batman: Arkham City – Original Video Game Score" was released on October 18, 2011, by WaterTower Music.  The album features 19 tracks composed for the game.  Ron Fish and Nick Arundel, composers for "Batman: Arkham Asylum", returned to write music for "Arkham City".

The Arkham Collector: The Arkham Collector was an American fantasy, horror fiction and poetry magazine first published in Summer 1967.  The magazine, edited by August Derleth, was the second of two magazines published by Arkham House, the other being the "Arkham Sampler".  Each issue of "The Arkham Collector" had an approximate print run of 2,500 copies.  Its headquarters was in Sauk City, Wisconsin.

Polarity (game): Polarity is a board game that requires strategic thinking and dexterity to control hovering magnetic discs.  "Polarity" was invented in 1985 by Canadian artist and designer Douglas Seaton.  It was first published in 1986.  The game has had a tumultuous past, with its rights changing hands several times over the past two decades.  The game has been published by Telemotion Technologies, Irwin Toy, briefly with Mattel and most recently by Temple Games.  The game ships in a canvas sleeve and include the magnets, the board, and a paper rulebook.  An unrelated game of the same name is published by a company called Mindwalk (Company).

Arkham Horror: The Card Game: Arkham Horror: The Card Game is produced by Fantasy Flight Games.  It is a cooperative game set in the universe of Chaosium's "Call of Cthulhu" roleplaying game which is based on the Cthulhu Mythos of H.P. Lovecraft and other horror writers.  The setting of the game is based in the titular (fictional) town of Arkham, MA.  The game was originally leaked in May 2016, before being officially announced in August of that same year.  It made its first limited public release at Arkham Nights 2016 to a sold out crowd.

Tide of Iron: Tide of Iron is a World War II based wargame designed and published in 2007 by Fantasy Flight Games, also notable for publishing other large games containing a large number of counters and/or other components such as "" and "Arkham Horror".

Flotilla (video game): Flotilla is a 2010 turn-based strategy space combat video game developed by Brendon Chung's studio, Blendo Games.  The game was released in March 2010 on Steam for Microsoft Windows and on Xbox Live Indie Games for the Xbox 360.  "Flotilla" was designed with Microsoft's XNA tools, and its development was influenced by animals as well as board games such as "Axis and Allies" and "Arkham Horror".  The game takes the player in an adventure through a randomly generated galaxy.

Elder Sign (card game): Elder Sign is a cooperative card and dice game, based on the Cthulhu Mythos of horror writer H.P. Lovecraft and Chaosium's Call of Cthulhu roleplaying game.  It is published by Fantasy Flight Games, which also produces the Cthulhu Mythos games "Arkham Horror", "", "Mansions of Madness", and "Eldritch Horror".

Question: Which game has had more publishers, Arkham Horror or Polarity?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "game_comparisons": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "game_name": {
            "type": "string",
            "description": "The name of the game."
          },
          "publisher_details": {
            "type": "object",
            "properties": {
              "publisher_count": {
                "type": "integer",
                "description": "The total number of publishers for the game."
              },
              "publisher_names": {
                "type": "array",
                "items": {
                  "type": "string"
                },
                "description": "A list of names of the publishers for the game."
              }
            },
            "required": [
              "publisher_count",
              "publisher_names"
            ],
            "additionalProperties": false
          }
        },
        "required": [
          "game_name",
          "publisher_details"
        ],
        "additionalProperties": false
      },
      "minItems": 2,
      "maxItems": 2,
      "description": "An array containing details for each game being compared."
    },
    "game_with_most_publishers": {
      "type": "string",
      "description": "The name of the game that has the most publishers."
    },
    "comparison_summary": {
      "type": "string",
      "description": "A summary statement comparing the number of publishers for the games."
    }
  },
  "required": [
    "game_comparisons",
    "game_with_most_publishers",
    "comparison_summary"
  ],
  "additionalProperties": false
}
