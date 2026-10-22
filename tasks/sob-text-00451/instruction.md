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
Landslide (board game): Landslide is the name of two board games about the U.S. presidential elections, where players compete to become the president of the United States.

Alan R. Moon: Alan R. Moon (born 18 November 1951) is an author of board games, born in Southampton, England, and currently living in the United States.  He is generally considered to be one of the foremost designers of German-style board games.  Many of his games can be seen as board game variations on the travelling salesman problem.

Glossary of board games: This page explains commonly used terms in board games in alphabetical order.  For a list of board games, see List of board games.  For terms specific to chess, see Glossary of chess.  For terms related to chess problems, see Glossary of chess problems.

List of word board games: Word board games are those games played on a board as players of the game attempt to construct words that use a scoring system.  The player with the highest score wins the game.  Many if not most board games are also available as software programs and online.  Online word board games can be organized so that the player is playing against other people or the game can be played against an automated program acting as an artificial intelligence.  Players of some word board games organize themselves into associations, clubs, and tournaments.

Abalone (board game): Abalone is an award-winning two-player abstract strategy board game designed by Michel Lalet and Laurent Lévi in 1987.  Players are represented by opposing black and white marbles on a hexagonal board with the objective of pushing six of the opponent's marbles off the edge of the board.

David Parlett: David Parlett (born 1939) is a games scholar, historian, and translator from South London, who has studied both card games and board games. His published works include many popular books on games and the more academic volumes "The Oxford Guide to Card Games" and "The Oxford History of Board Games", both now out of print.  Parlett also invented a number of board games, the most successful of which is Hare and Tortoise (1974).  The German edition was awarded Spiel des Jahres (Game of the Year) in 1979.

Piecepack: Piecepack is a public-domain game system that can be used to play a wide variety of board games, much as a standard deck of cards can be used to play thousands of card games ("A game system is a set of components that function together in multiple games").  Piecepack has been used by dozens of different game designers to create over 150 different board games and is available from many different manufacturers.  It was created by James Kyle in 2001.

Mū tōrere: Mū tōrere is a board game played mainly by the Māori people from the east coast of New Zealand’s North Island.  It is one of two board games that the Māori people are known to have played before their country became part of the British Empire.

Elfenland: Elfenland is a German-style board game designed by Alan R. Moon and published by Amigo Spiele in German and Rio Grande Games in English in 1998.

Mark Rein-Hagen: Mark Rein-Hagen is a role-playing, card, video and board game designer best known as the creator of "" and its associated "World of Darkness" games.  Along with Jonathan Tweet, he is also one of the original two designers of "Ars Magica".  His work on "World of Darkness" has influenced the movie series "Underworld", "True Blood", and otherkin sub-cultures such as Real Life Vampires and Real Life Werewolves.

Question: Which of these two board games had two designers, Abalone or Elfenland?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "games_evaluated": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "game_name": {
            "type": "string"
          },
          "designer_count": {
            "type": "integer"
          },
          "designer_names": {
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "game_name",
          "designer_count",
          "designer_names"
        ],
        "additionalProperties": false
      }
    },
    "game_matching_criteria": {
      "type": "string",
      "description": "The name of the game that matches the criteria of having two designers."
    },
    "criteria_met": {
      "type": "object",
      "properties": {
        "number_of_designers": {
          "type": "integer",
          "description": "The specific number of designers the question was looking for."
        }
      },
      "required": [
        "number_of_designers"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "games_evaluated",
    "game_matching_criteria",
    "criteria_met"
  ],
  "additionalProperties": false
}
