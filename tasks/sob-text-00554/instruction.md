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
The President's Mystery: The President's Mystery is a 1936 American film directed by Phil Rosen.

I Killed That Man: I Killed That Man is a 1941 American film directed by Phil Rosen that was a remake of his 1933 film "The Devil's Mate".  It starred Ricardo Cortez and was produced by the King Brothers.

Beggars in Ermine: Beggars in Ermine is a 1934 American film directed by Phil Rosen.

Paul Bogart: Paul Bogart (November 21, 1919 – April 15, 2012) was an American television and film director and producer.

Born to Gamble: Born to Gamble (1935) is an American film directed by Phil Rosen and released by Republic Pictures.

Phil Rosen: Phil Rosen (May 8, 1888 – October 22, 1951) was an American film director and cinematographer.  He directed 142 films between 1915 and 1949.

The Scarlet Clue: The Scarlet Clue is a 1945 American film directed by Phil Rosen.

Road to Happiness: Road to Happiness is a 1942 American film directed by Phil Rosen.

Roar of the Press: Roar of the Press is a 1941 American film directed by Phil Rosen.

Paper Bullets: Paper Bullets is a 1941 American film directed by Phil Rosen and starring Joan Woodbury.  It was the first film produced by the King Brothers, launching their career.

Question: Are Phil Rosen and Paul Bogart American film directors?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "overall_answer": {
      "type": "boolean",
      "description": "True if both individuals are American film directors, false otherwise."
    },
    "individuals_checked": {
      "type": "array",
      "description": "Details for each individual mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the individual."
          },
          "is_american": {
            "type": "boolean",
            "description": "True if the individual is American."
          },
          "is_film_director": {
            "type": "boolean",
            "description": "True if the individual is a film director."
          },
          "nationality": {
            "type": "string",
            "description": "The stated nationality of the individual."
          },
          "professions": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of professions attributed to the individual."
          }
        },
        "required": [
          "name",
          "is_american",
          "is_film_director",
          "nationality",
          "professions"
        ],
        "additionalProperties": false
      }
    },
    "number_of_individuals_found": {
      "type": "integer",
      "description": "The total number of individuals found in the context that were asked about."
    }
  },
  "required": [
    "overall_answer",
    "individuals_checked",
    "number_of_individuals_found"
  ],
  "additionalProperties": false
}
