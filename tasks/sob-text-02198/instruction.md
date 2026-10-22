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
Leslie Nielsen: Leslie William Nielsen, OC (11 February 192628 November 2010) was a Canadian actor, comedian, and producer.  He appeared in more than 100 films and 150 television programs, portraying more than 220 characters.

Knights of the City: Knights of the City (originally Cry of the City) is a 1986 action adventure film starring Leon Isaac Kennedy, Nicholas Campbell, John Mengatti and Janine Turner.  It was directed by Dominic Orlando and written by Leon Isaac Kennedy and filmed in Miami, Ft. Lauderdale and Hollywood, Florida.

The Patriot (1986 film): The Patriot is a 1986 action film directed by Frank Harris and starring Gregg Henry, Simone Griffeth and Stack Pierce with Leslie Nielsen.

Armed Response (1986 film): Armed Response is a 1986 action crime film, starring David Carradine and Lee Van Cleef and directed by Fred Olen Ray.  This is the first action film made by CineTel Films which would become famous in that genre.

Iyo ang Tondo Kanya ang Cavite: Iyo ang Tondo, Kanya ang Cavite (  Tondo is Yours, Cavite is Theirs ) is a 1986 action film directed by Pablo Santiago and written by Antonio Pascua.

Let's Get Harry: Let's Get Harry is a 1986 action film directed by Stuart Rosenberg.  It stars Thomas F. Wilson, Michael Schoeffling, Glenn Frey, Rick Rossovich, Mark Harmon, Robert Duvall and Gary Busey.  Rosenberg chose to credit the film to Alan Smithee, a pseudonym used by directors who repudiate their involvement in a film.

Peter Hyams: Peter Hyams (born July 26, 1943) is an American film director, screenwriter and cinematographer, known for directing "Capricorn One", the 1981 science fiction thriller "Outland", "2010" (the sequel to Stanley Kubrick's ""), the 1986 action/comedy "Running Scared", the comic book adaptation "Timecop", the action film "Sudden Death" (both starring Jean-Claude Van Damme), and the horror films "The Relic" and "End of Days".

Cool Change (film): Cool Change is a 1986 action film directed by George T. Miller.  It stars Jon Blake and Lisa Armytage.

Quiet Cool: Quiet Cool is a 1986 action film directed by Clay Borris.

Tough Guys: Tough Guys is a 1986 action comedy film starring Burt Lancaster, Kirk Douglas, Eli Wallach, Charles Durning, Dana Carvey and Darlanne Fluegel.  It was directed by Jeff Kanew.  This was the first film to be released under the banner of Touchstone Pictures rather than Touchstone Films.

Question: The Patriot is a 1986 action film starring a Canadian actor who portrayed more than 220 what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "film_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "film_genre": {
      "type": "string",
      "description": "The genre of the film."
    },
    "actor_details": {
      "type": "object",
      "properties": {
        "actor_name": {
          "type": "string",
          "description": "The name of the actor."
        },
        "actor_nationality": {
          "type": "string",
          "description": "The nationality of the actor."
        },
        "portrayed_count_minimum": {
          "type": "integer",
          "description": "The minimum number of items portrayed by the actor."
        },
        "portrayed_item_type": {
          "type": "string",
          "description": "The type of items portrayed by the actor (e.g., characters, films)."
        }
      },
      "required": [
        "actor_name",
        "actor_nationality",
        "portrayed_count_minimum",
        "portrayed_item_type"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_title",
    "film_year",
    "film_genre",
    "actor_details"
  ],
  "additionalProperties": false
}
