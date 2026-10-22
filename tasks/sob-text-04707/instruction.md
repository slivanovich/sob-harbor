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
The Package (Lost): "The Package" is the tenth television episode of the American Broadcasting Company's sixth season of the serial drama television series "Lost" and 113th episode overall.  The episode was aired on March 30, 2010, on ABC in the United States.  The episode was written by producer Paul Zbyszewski and story editor Graham Roland.  The episode is centered on Sun-Hwa Kwon and Jin-Soo Kwon.

The Fight (Star Trek: Voyager): "The Fight" is the 113th episode of the science fiction television series "", the 19th episode of the .

113th Ohio Infantry: The 113th Ohio Volunteer Infantry (or 113th OVI) was an infantry regiment in the Union Army during the American Civil War.

Spanky (film): Spanky is a 1932 "Our Gang" short comedy film directed by Robert F. McGowan.  It was the 113th (25th talking episode) "Our Gang" short that was released.  The film was based on "Our Gang" co-star George "Spanky" McFarland.

The Masterpiece Society: "The Masterpiece Society" is the 113th episode of the American science fiction television series "", the 13th episode of the .  In this episode, while the crew of the USS "Enterprise" saves an isolated genetically engineered society from immediate destruction, the cultural contamination resulting from their interaction may still ultimately doom the colony.

Robot Wrecks: Robot Wrecks is a 1941 "Our Gang" short comedy film directed by Edward Cahn.  It was the 200th "Our Gang" short (201st episode, 112th talking short, 113th talking episode, and 32nd MGM produced episode) that was released.

George McFarland: George "Spanky" McFarland (October 2, 1928 – June 30, 1993) was an American actor most famous for his appearances as a child in the "Our Gang" series of short-subject comedies of the 1930s and 1940s.  The "Our Gang" shorts were later syndicated to television as "The Little Rascals".

Secret Santa (The Office): "Secret Santa" is the 13th episode of the sixth season of the U.S. comedy series "The Office" and the show's 113th episode overall.  It was written by Mindy Kaling and directed by Randall Einhorn.  The night the episode premiered, it was immediately followed by an episode of "30 Rock" with the same title.

By Inferno's Light: "By Inferno's Light" is the 113th episode of the television series "", the 15th episode of the .

Helping Hands (film): Helping Hands is a 1941 "Our Gang" short comedy film directed by Edward Cahn.  It was the 201st "Our Gang" short (202nd episode, 113th talking short, 114th talking episode, and 33rd MGM produced episode) that was released.

Question: What American actor was the inspiration for the 113th episode of "Our Gang"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "inspired_actor": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the American actor who inspired the episode."
        },
        "nickname": {
          "type": "string",
          "description": "The common nickname of the actor, if available."
        }
      },
      "required": [
        "name"
      ]
    },
    "inspired_episode": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the 'Our Gang' episode."
        },
        "episode_number": {
          "type": "integer",
          "description": "The overall episode number of the 'Our Gang' short."
        },
        "series_name": {
          "type": "string",
          "description": "The name of the series the episode belongs to."
        }
      },
      "required": [
        "title",
        "episode_number",
        "series_name"
      ]
    },
    "inspiration_type": {
      "type": "string",
      "description": "Describes the nature of the inspiration (e.g., 'based on')."
    }
  },
  "required": [
    "inspired_actor",
    "inspired_episode",
    "inspiration_type"
  ],
  "additionalProperties": false
}
