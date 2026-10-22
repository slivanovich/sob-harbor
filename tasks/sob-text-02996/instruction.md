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
I Shot Jesse James: I Shot Jesse James is a 1949 American western film directed by Samuel Fuller about the murder of Jesse James by Robert Ford and Robert Ford's life afterwards.  The story is built around a fictional rivalry between Ford and his eventual killer Edward Kelley (called John in the film) over a woman.  "I Shot Jesse James" is Samuel Fuller's first movie, and stars Reed Hadley as Jesse James and John Ireland as Bob Ford.

Jesse James' Women: Jesse James' Women is a 1954 American film starring as well as directed, co-produced and co-written by Don "Red" Barry, who portrays Jesse James.  The supporting cast features Peggie Castle and Jack Buetel.  Filming took place in Silver Creek, Mississippi.

Thunder Over the Plains: Thunder Over The Plains is a 1953 western film directed by Andre DeToth and starring Randolph Scott.  The tag line on the original movie poster was “A tornado of adventure from Warner Bros.” The supporting cast features Lex Barker, Phyllis Kirk, Henry Hull, Elisha Cook, Jr. and Fess Parker.  This was Barker's first film after starring in five "Tarzan" pictures.

The Buckskin Lady: The Buckskin Lady is a 1957 American film directed by Carl K. Hittleman and starring Patricia Medina in the titular role and Richard Denning as her leading man.  The supporting cast features Gerald Mohr, Henry Hull, and Hank Worden.  The movie's tagline was, "She hid her scarlet past behind a pair of silver .45s!"

Werewolf of London: Werewolf of London is a 1935 horror film directed by Stuart Walker, starring Henry Hull as the titular werewolf, and produced by Universal Pictures.  Jack Pierce's werewolf make-up was simpler than his version six years later for Lon Chaney, Jr. in "The Wolf Man".  The film was the first Hollywood mainstream movie to feature a werewolf.  The film's supporting cast features Warner Oland and Valerie Hobson.

The True Story of Jesse James: The True Story of Jesse James is a 1957 American Western drama film adapted from Henry King's 1939 film "Jesse James", which was only loosely based on James' life.  It was directed by Nicholas Ray, with Robert Wagner portraying Jesse James and Jeffrey Hunter starring as Frank James.  Filming took place during 1955.  Originally titled The James Brothers in the United Kingdom, the film focused on the relationship between the two James brothers during the last 18 years of Jesse James' life.

The Return of Jesse James: The Return of Jesse James is a 1950 American western film directed by Arthur Hilton and starring John Ireland, Ann Dvorak and Henry Hull.

Jesse James (1939 film): Jesse James (1939) is a western film directed by Henry King and starring Tyrone Power, Henry Fonda, Nancy Kelly and Randolph Scott.  Written by Nunnally Johnson, the film is loosely based on the life of Jesse James, the notorious outlaw from whom the film derives its name.  It is "notorious for its historical inaccuracy."  The supporting cast features Henry Hull, John Carradine, Brian Donlevy, Jane Darwell and Lon Chaney, Jr..

Henry Hull: Henry Watterson Hull (October 3, 1890 – March 8, 1977) was an American character actor with a unique voice who is best remembered for playing the lead role in Universal Pictures's "Werewolf of London" (1935).

The Return of Frank James: The Return of Frank James is a 1940 western film directed by Fritz Lang and starring Henry Fonda and Gene Tierney.  It is a sequel to Henry King's 1939 film "Jesse James".  Written by Sam Hellman, the film loosely follows the life of Frank James following the death of his outlaw brother, Jesse James at the hands of the Ford brothers.  The film is universally considered historically inaccurate, but was a commercial success and is notable as being the first motion picture for the actress Gene Tierney, who plays a reporter for the newspaper "The Denver Star".

Question: Jesse James, is a western film directed by Henry King, the supporting cast features Henry Hull, he was an American character actor with a unique voice who is best remembered for playing the lead role in Universal Pictures's "Werewolf of London", released in which year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "release_year": {
      "type": "integer",
      "description": "The year the film was released."
    },
    "director": {
      "type": "string",
      "description": "The director of the film."
    },
    "production_company": {
      "type": "string",
      "description": "The production company of the film."
    },
    "starring_actor": {
      "type": "string",
      "description": "The main actor in the film."
    }
  },
  "required": [
    "film_title",
    "release_year",
    "director",
    "production_company",
    "starring_actor"
  ],
  "additionalProperties": false
}
