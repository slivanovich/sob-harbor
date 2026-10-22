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
Fanorona: Fanorona (] ) is a strategy board game for two players.  The game is indigenous to Madagascar.

Limaye: Limaye is a family name, common among the Chitpavan Kokanastha Brahmin community in Western Maharashtra, India.  The names Karandikar, Dixit and Khasgiwale are supposedly derived from the same clan.  The origin of the Limaye/Karandikar/Dixit and Khasgiwale family is believed to be from the Western Coast of India, Maharashtra - Ratnagiri, a Southern District of Konkan - Maharashtra region.

Dixit (card game): Dixit is a card game created by Jean-Louis Roubira, and published by Libellud.  Using a deck of cards illustrated with dreamlike images, players select cards that match a title suggested by the "storyteller", and attempt to guess which card the "storyteller" selected.  The game was introduced in 2008.  "Dixit" won the 2010 Spiel des Jahres award.

Question: Dixit and Fanorona are the names of what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "entity_names": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Names of the entities being categorized."
    },
    "common_category": {
      "type": "string",
      "description": "The common category that both entities belong to."
    },
    "games": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the game."
          },
          "type": {
            "type": "string",
            "description": "The specific type of game (e.g., board game, card game)."
          },
          "origin_or_creator": {
            "type": "string",
            "description": "The origin country or the creator of the game."
          },
          "number_of_players": {
            "type": "integer",
            "description": "The number of players for the game."
          },
          "publisher": {
            "type": "string",
            "description": "The publisher of the game."
          },
          "introduction_year": {
            "type": "integer",
            "description": "The year the game was introduced."
          },
          "award_won": {
            "type": "string",
            "description": "The name of the award won by the game."
          },
          "award_year": {
            "type": "integer",
            "description": "The year the award was won."
          }
        },
        "required": [
          "name",
          "type",
          "origin_or_creator"
        ],
        "additionalProperties": false
      },
      "description": "Detailed information about each game."
    }
  },
  "required": [
    "entity_names",
    "common_category",
    "games"
  ],
  "additionalProperties": false
}
