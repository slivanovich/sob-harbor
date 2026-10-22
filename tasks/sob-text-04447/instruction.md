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
Serial (Bad) Weddings: Serial (Bad) Weddings (French: Qu'est-ce qu'on a fait au Bon Dieu ? )  is a French comedy film directed by Philippe de Chauveron released in 2014.

Noom Diawara: Noom Diawara (born 26 December 1978) is a French actor.  He is known for playing the role of Charles in "Serial (Bad) Weddings".

Annie Hall: Annie Hall is a 1977 American romantic comedy film directed by Woody Allen from a screenplay he co-wrote with Marshall Brickman.  Produced by Allen's manager, Charles H. Joffe, the film stars the director as Alvy "Max" Singer, who tries to figure out the reasons for the failure of his relationship with the film's eponymous female lead, played by Diane Keaton in a role written specifically for her.

Swingin' Along: Swingin' Along is a 1961 American comedy film directed by Charles Barton.  The film, which was released by 20th Century Fox, marked the final appearance of the comedy team of Tommy Noonan and Peter Marshall.  The film focuses on Noonan as a courier who dreams of becoming a songwriter and Marshall as a con artist who wants to enter Noonan’s original composition in a music competition.  The film co-stars Barbara Eden and features musical performances by Ray Charles, Bobby Vee and Roger Williams.

Madras to Pondicherry: Madras to Pondicherry (தமிழ்: மதராஸ் டு பாண்டிச்சேரி) is a 1966 Tamil language film directed by Thirumalai Mahalingam and produce by Vividha Baarathy.  Though the dialog and story was written by 'Usilai' Somanathan.  Music by T. K. Ramamoorthy assets to the movie.  Starring Kalpana, Ravichandran was playe lead role in protagonist.  Nagesh, Manorama, V. K. Ramasamy, C. T. Rajakantham, V. S. Raghavan and O. A. K. Thevar was play key role.  The film was a runaway hit at the box office.  The movie was eventually remade in Hindi as "Bombay to Goa".  The role played by Nagesh in Tamil version was reprised by Mehmood in the Hindi version.  This film was the last film in which the comedian C. T. Rajakantham (who became famous through the first Tamil box-office hit comedy film Sabapathy(1941)) acted.

His Girl Friday: His Girl Friday is a 1940 American screwball comedy film directed by Howard Hawks, from an adaptation by Charles Lederer, Ben Hecht and Charles MacArthur of the play "The Front Page" by Hecht and MacArthur.  This was the second time the play had been adapted for the screen, the first occasion being the 1931 film also called "The Front Page".  The major change in this version, introduced by Hawks, is that the role of Hildy Johnson is a woman.

The Dictator (1915 film): The Dictator is a 1915 American silent comedy film directed by Oscar Eagle and reputedly Edwin S. Porter.  It was based on a play "The Dictator" by Richard Harding Davis and produced by Adolph Zukor (Famous Players Film Company) and the Charles Frohman Company.  John Barrymore stars in a role played on the stage by William Collier, Sr. whose company Barrymore had performed in this play.  The film was rereleased on April 13, 1919 as part of the Paramount "Success Series" of their early screen successes.  The story was refilmed in 1922 as "The Dictator" starring Wallace Reid.  Today the film is lost.

Mixed Nuts: Mixed Nuts is a 1994 American Christmas comedy film directed by Nora Ephron, based on the 1982 French comedy film, "Le Père Noël est une ordure".  Co-written by Ephron and her sister Delia, the film features an ensemble cast which includes Steve Martin, Madeline Kahn, Rita Wilson, Anthony LaPaglia, Garry Shandling, Juliette Lewis, Adam Sandler and, in his first film role, Liev Schreiber.

The Lovable Cheat: The Lovable Cheat is a 1949 American comedy film directed by Richard Oswald and starring Charles Ruggles, Peggy Ann Garner and Richard Ney.  It is based on the 1848 play "Mercadet Le Falseur" by Honoré de Balzac.  It was the final film of the Austrian director Oswald, who had fled into exile following the Nazi rise to power.  Buster Keaton played a small supporting role in the film, as his career had seriously declined by this stage.

Masterji: Masterji is an Bollywood romantic comedy film directed by K. Raghavendra Rao, released on 30 August, 1985.  The film stars Rajesh Khanna in the title role as Masterji and Sridevi as his heroine as the main lead characters of the film.  This film was of different genre - Comedy than the other films of the pair.  This film was remake of 1984 Tamil film "Mundhanai Mudichu", directed by K. Bhagyaraj, where Bhagyaraj also played the lead male role.  After the Tamil version, K. Bhagyaraj decided to remake it in Hindi but handed over directorship to Kovelamudi Raghavendra Rao.  K. Bhagyaraj himself wrote the story and screenplay for "Masterji".

Question: Noom Diawara played the role of Charles in the comedy film directed by whom?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "actor_name": {
      "type": "string",
      "description": "The name of the actor."
    },
    "role_name": {
      "type": "string",
      "description": "The name of the role played by the actor."
    },
    "director_name": {
      "type": "string",
      "description": "The name of the director of the film."
    },
    "film_genre": {
      "type": "string",
      "description": "The genre of the film."
    },
    "release_year": {
      "type": "integer",
      "description": "The release year of the film."
    }
  },
  "required": [
    "film_title",
    "actor_name",
    "role_name",
    "director_name",
    "film_genre",
    "release_year"
  ],
  "additionalProperties": false
}
