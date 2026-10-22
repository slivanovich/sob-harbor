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
Back to School: Back to School is a 1986 American comedy film starring Rodney Dangerfield, Keith Gordon, Sally Kellerman, Burt Young, Terry Farrell, William Zabka, Ned Beatty, Sam Kinison, Paxton Whitehead and Robert Downey, Jr. It was directed by Alan Metter.

Back by Midnight: Back By Midnight is a 2005 American comedy film starring Rodney Dangerfield, Phil LaMarr, Harland Williams, Randy Quaid, Gilbert Gottfried, and Kirstie Alley.  The film was actually produced and completed in 2002.  It also features cameo appearances by Dangerfield's real-life friends, Ron Jeremy and Michael Bolton, as well as Louie Anderson.

My 5 Wives: My 5 Wives is a 2000 American comedy film directed by Sidney J. Furie and starring Rodney Dangerfield.

Ladybugs (film): Ladybugs is a 1992 American sports-comedy film starring Rodney Dangerfield and directed by Sidney J. Furie.  Dangerfield plays a Denver businessman who takes over a girls soccer team that the company he works for sponsors.  The film also stars Jackée Harry as his assistant coach, Ilene Graff as his girlfriend, Jonathan Brandis as his girlfriend's son, and Vinessa Shaw as his boss's daughter.

The 4th Tenor: The 4th Tenor is a 2002 American comedy film written by and starring Rodney Dangerfield.

Easy Money (1983 film): Easy Money is a 1983 American comedy film starring Rodney Dangerfield, Joe Pesci, Geraldine Fitzgerald, Candice Azzara, and Jennifer Jason Leigh.  It was directed by James Signorelli and written by Dangerfield, Michael Endler, P. J. O'Rourke and Dennis Blair.  The original music score was composed by Laurence Rosenthal.  The theme song "Easy Money" is performed by Billy Joel and was featured on his album "An Innocent Man".

Rodney Dangerfield: Rodney Dangerfield (born Jacob Cohen, November 22, 1921 – October 5, 2004) was an American stand-up comedian, actor, producer and screenwriter known for the catchphrase "I don't get no respect!"  and his monologues on that theme.  He is also remembered for his 1980s film roles, especially in "Easy Money", "Caddyshack", and "Back to School".

Dennis Blair (comedian): Dennis Blair (born Feb 21, 1955) is an American stand-up comedian.  He is known for writing, and appearing in, the 1983 movie "Easy Money", alongside his mentor, Rodney Dangerfield.  He provided the voice of Lem and Clem in the animated film "'Rover Dangerfield".  He wrote for Dangerfield for four years including sketches for his network specials and jokes for his act.

The Godson (film): The Godson is a 1998 comedy directed by Bob Hoge, starring Rodney Dangerfield, Kevin McDonald and Dom DeLuise.  The film is a parody of The Godfather franchise and "Scarface", as well as other gangster films that were popular in the 1970s, 1980s, and 1990s.

Harry Basil: Harry Basil is a stand-up comedian and comedy club operator, known for his impressions of Arnold Schwarzenegger and Superman.  As an actor, Basil appeared in the film "Peggy Sue Got Married".  His film credits include "Meet Wally Sparks", which he co-wrote with Rodney Dangerfield.

Question: My 5 Wives is a 2000 American comedy film directed by Sidney J. Furie and starring Rodney Dangerfield, an American stand-up comedian, actor, producer and screenwriter known for what catchphrase?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film mentioned in the question."
    },
    "film_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "director": {
      "type": "string",
      "description": "The director of the film."
    },
    "main_actor": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the main actor."
        },
        "occupation": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "The occupations of the main actor."
        },
        "catchphrase": {
          "type": "string",
          "description": "The well-known catchphrase of the main actor."
        }
      },
      "required": [
        "name",
        "occupation",
        "catchphrase"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_title",
    "film_year",
    "director",
    "main_actor"
  ],
  "additionalProperties": false
}
