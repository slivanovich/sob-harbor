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
Disney Sports Basketball: Disney Sports Basketball is a 2002 sports video game released by Konami.

Anaheim Sports: Anaheim Sports, Inc., formerly Disney Sports Enterprises, Inc. (DSE), was a fully owned subsidiary of the Walt Disney Company based in Anaheim, California and created in 1992 as the ownership group for the Mighty Ducks of Anaheim professional hockey team.

RunDisney: runDisney (formerly Disney Endurance Series and The Endurance Series at Walt Disney World Resort), is the road race division of Disney Sports Enterprises, a unit of Walt Disney Parks and Resorts, a segment and subsidiary of The Walt Disney Company.  The division is designed to get runners to plan a "runcation", a vacation planned to coincide with the race they signed up for.

Disney Golf: Disney Golf, known in Japan as Disney Golf Classic (ディズニーゴルフクラシック "Dizunīgorufukurashikku"), is a Disney sports game and the spiritual successor to another golf game called "Swing Away Golf", themed with Disney characters.  First shown at the Electronic Entertainment Expo in 2002, it was the fifth golf game to be made for the system.  It was released by Disney Interactive in North America and Japan in 2002, and in Europe in 2005.

Disney Sports Soccer: Disney Sports Soccer, known as Disney Sports Football in Europe, is a 2002 sports video game released by Konami.

Disney Sports Football: Disney Sports Football is a Nintendo GameCube video game released in 2002 by Konami.

Pete (Disney): Pete (also called Peg-Leg Pete, Pistol Pete and Black Pete, among other names) is an anthropomorphic cartoon character created in 1925 by Walt Disney and Ub Iwerks.  He is a character of The Walt Disney Company and often appears as a nemesis and the main antagonist in Mickey Mouse universe stories.  He was originally an anthropomorphic bear but with the advent of Mickey Mouse in 1928, he was defined as a cat.  Pete is the oldest continuing Disney character, having debuted three years before Mickey Mouse in the cartoon "Alice Solves the Puzzle" (1925).

Walt Disney World Marathon: The Walt Disney World Marathon is an annual marathon and weekend race series held every January in Orlando, Florida held by runDisney, a race series and division of Disney Sports Enterprises.

Hameen Ali: Hameen Mitsurugi Ali III (born April 14, 1977) is an American former college football player for the College of William & Mary who is known for being the 2000 recipient of the Disney Sports Spirit Award.  The award is presented annually to "college football's most inspirational athlete, who displays a sense of courage and an undying love for the game, while overcoming adversity on or off the field."

Disney Sports Skateboarding: Disney Sports Skateboarding, also known as Disney All Star Sports: Skateboarding in Europe, is a 2002 sports video game released by Konami.  The playable characters include Mickey Mouse, Minnie Mouse, Donald Duck, Goofy, Max Goof and Pete.

Question: Disney Sports Skateboarding includes the character created in 1925 by whom?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "character_name": {
      "type": "string",
      "description": "The name of the character featured in the game."
    },
    "creation_year": {
      "type": "integer",
      "description": "The year the character was created."
    },
    "creators": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of individuals credited with creating the character."
    },
    "game_title": {
      "type": "string",
      "description": "The title of the video game in which the character appears."
    }
  },
  "required": [
    "character_name",
    "creation_year",
    "creators",
    "game_title"
  ],
  "additionalProperties": false
}
