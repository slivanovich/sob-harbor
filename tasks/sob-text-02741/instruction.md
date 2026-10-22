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
Pitts and Todd: Pitts and Todd were a comedy duo from the 1930s, put together by Hal Roach as the female counterpart to Laurel and Hardy.  The duo consisted of actresses Zasu Pitts and Thelma Todd.  The team changed members over the years, becoming Todd and Kelly, then Kelly and Kelton, followed by Kelly and Roberti, then finally coming full circle with Pitts and Kelly.

John O'Hurley: John George O'Hurley (born October 9, 1954) is an American actor, voice actor, author and television personality.  He is known for the role of J. Peterman on the NBC sitcom "Seinfeld", and was host of the game show "Family Feud" from 2006 to 2010.

Cockeyed Cavaliers: Cockeyed Cavaliers is a 1934 American Pre-Code comedy film starring the comedy duo of Wheeler & Woolsey.  Directed by Mark Sandrich from a screenplay by Edward Kaufman, Grant Garrett, Ralph Spence and Ben Holmes.  Also featured in the cast were Dorothy Lee and Thelma Todd.

Patsy Kelly: Patsy Kelly (January 12, 1910 – September 24, 1981) was an American stage, radio, film and television actress.  She is known for her role as the brash, wisecracking sidekick to Thelma Todd in a series of short comedy films produced by Hal Roach in the 1930s.  Known as the "Queen of Wisecracks", Kelly's career continued after Todd's death in 1935 in similar roles.

White Hot Peach: White Hot Peach is the Primitive Radio Gods' follow-up to Rocket, and was released on October 24, 2000.  Quite different in sound from the debut album, White Hot Peach features much less of the sampling that made the band famous.  Most of the material from this album is from "Mellotron On", the album the band planned on releasing through Sire Records in 1999, but could not due to that label's bankruptcy.

White Hot Odyssey (album): White Hot Odyssey is the debut album by American hard rock band White Hot Odyssey, released on Mojo/Jive Records in 2004.  The album was produced by lead singer-songwriter Steve Perry.

Corsair (film): Corsair is a 1931 American pre-Code crime drama written, produced and directed by Roland West.  The film is based on the 1931 novel "Corsair, a Pirate in White Flannels" by Walton Green and takes place in and was shot during the era of Prohibition in the United States.  The film stars Chester Morris and Thelma Todd (credited as Alison Loyd).

White Hot: The Mysterious Murder of Thelma Todd: White Hot: The Mysterious Murder of Thelma Todd is a 1991 television film in the biographical film genre, based on the life of the 1930s comedian actress Thelma Todd.  The film stars Loni Anderson as Todd, Maryedith Burrell, Robert Davi, Paul Dooley, Linda Kelsey, and John O'Hurley.

Fading Out: Fading Out is the Primitive Radio Gods' first and only officially released EP.  It doubles as an extended single for the song of the same name from the "White Hot Peach" album.  Aside from the title track, the EP contains two songs from "Mellotron On! " that did not make the cut for "White Hot Peach", a remix of "Fading Out", and a new track called "Rope".

The Maltese Falcon (1931 film): The Maltese Falcon is a 1931 American pre-Code crime film, based on the novel of the same name by Dashiell Hammett and directed by Roy Del Ruth.  The film stars Ricardo Cortez as private detective Sam Spade and Bebe Daniels as Ruth Wonderly.  Maude Fulton, Brown Holmes, and Lucien Hubbard (who went uncredited) wrote the screenplay.  The supporting cast features Dudley Digges, Thelma Todd, Walter Long, Una Merkel, and Dwight Frye.  The film is based on the 1929 novel "The Maltese Falcon" by Dashiell Hammett published by Alfred A. Knopf, Inc.

Question: White Hot: The Mysterious Murder of Thelma Todd stars which cast member from "Seinfeld"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film being discussed."
    },
    "year_of_film_release": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "actor_details": {
      "type": "object",
      "properties": {
        "actor_name": {
          "type": "string",
          "description": "The name of the actor who starred in both the film and Seinfeld."
        },
        "seinfeld_role": {
          "type": "string",
          "description": "The role the actor played in the sitcom Seinfeld."
        },
        "seinfeld_connection_present": {
          "type": "boolean",
          "description": "Indicates if a cast member from the film also had a role in Seinfeld."
        }
      },
      "required": [
        "actor_name",
        "seinfeld_role",
        "seinfeld_connection_present"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_title",
    "year_of_film_release",
    "actor_details"
  ],
  "additionalProperties": false
}
