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
Whitney: Can I Be Me: Whitney: Can I Be Me is a 2017 British-American documentary film, written, co-produced and co-directed by Nick Broomfield.  The film is about Whitney Houston's life and career.  Her rapid rise to fame and then her several problems with drug addiction.

The Sense of an Ending (film): The Sense of an Ending is a 2017 British-American mystery drama film directed by Ritesh Batra and written by Nick Payne, based on the novel of the same name by Julian Barnes.  The film stars Jim Broadbent, Charlotte Rampling, Harriet Walter, Emily Mortimer and Michelle Dockery.

The Great Muppet Caper: The Great Muppet Caper is a 1981 British-American mystery musical comedy film directed by Jim Henson, marking his feature directorial debut.  The film is about the Muppets who must travel to London to stop a jewel heist.  It is the second of a series of live-action musical feature films, starring Jim Henson's Muppets.  The film was a British-American venture produced by Henson Associates and ITC Entertainment, and originally released by Universal Pictures on 26 June 1981.  It is also the only Muppet feature film directed by Henson.  Shot in Great Britain in 1980, the film was released shortly after the final season of "The Muppet Show".

The Curse of King Tut's Tomb (1980 film): The Curse of King Tut's Tomb is a 1980 British-American mystery thriller film directed by Philip Leacock and starring Eva Marie Saint, Harry Andrews and Paul Scofield, with Tom Baker.

Final Portrait: Final Portrait is a 2017 British-American drama film written and directed by Stanley Tucci.  The film stars Geoffrey Rush, Armie Hammer, Clémence Poésy, Tony Shalhoub, James Faulkner and Sylvie Testud.

The Lunchbox: The Lunchbox is a 2013 Indian epistolary romantic film written and directed by Ritesh Batra, and produced by Guneet Monga, Anurag Kashyap, and Arun Rangachari.  The film was jointly produced by various studios including DAR motion pictures, UTV Motion Pictures, Dharma Productions, Sikhya Entertainment, NFDC (India), ROH Films (Germany), ASAP Films (France), and the Cine Mosaic (United States).  It stars Irrfan Khan, Nimrat Kaur and Nawazuddin Siddiqui in lead roles.  The film was screened at International Critics' Week at the 2013 Cannes Film Festival, and later won the Critics Week Viewers Choice Award also known as Grand Rail d'Or.  It was shown at the 2013 Toronto International Film Festival.  The film was released in India on 20 September 2013.  The film was a box-office success.

Our Souls at Night (film): Our Souls at Night is a 2017 American drama film directed by Ritesh Batra and written by Scott Neustadter and Michael H. Weber.  It is based on the novel of same name by Kent Haruf.  The film stars Robert Redford, Jane Fonda, Matthias Schoenaerts, and Judy Greer.  It had its world premiere at the Venice Film Festival on September 1, 2017.  It was released on September 29, 2017 by Netflix.

Billy Howle: Billy Howle (born November 9, 1989) is an actor, known for his work as James Warwick on the E4 television series, "Glue".  He has since co-starred in the film, "The Sense of an Ending" (as the younger version of Jim Broadbent's lead character) and the miniseries "The Witness for the Prosecution" in the pivotal role of defendant, Leonard Vole.  He also appeared in "Dunkirk".  Howle will next be seen opposite Saoirse Ronan in the drama, "On Chesil Beach", in the adaptation of Anton Chekhov's iconic play, "The Seagull", and in Netflix film "Outlaw King".

The Prestige (film): The Prestige is a 2006 British-American mystery thriller film directed by Christopher Nolan, from a screenplay adapted by Nolan and his brother Jonathan from Christopher Priest's 1995 novel of the same name.  Its story follows Robert Angier and Alfred Borden, rival stage magicians in London at the end of the 19th century.  Obsessed with creating the best stage illusion, they engage in competitive one-upmanship with tragic results.  The film stars Hugh Jackman as Robert Angier, Christian Bale as Alfred Borden, and David Bowie as Nikola Tesla.  It also stars Scarlett Johansson, Michael Caine, Piper Perabo, Andy Serkis, and Rebecca Hall.  The film reunites Nolan with actors Bale and Caine from "Batman Begins" and returning cinematographer Wally Pfister, production designer Nathan Crowley, film score composer David Julyan, and editor Lee Smith.

Lean on Pete: Lean on Pete is a 2017 British-American drama film written for the screen and directed by Andrew Haigh, based upon the novel of the same name by Willy Vlautin.  It stars Charlie Plummer, Travis Fimmel, Chloë Sevigny, Steve Buscemi, Steve Zahn, Thomas Mann, and Amy Seimetz.

Question: Who starred in both "Dunkirk" and a 2017 British-American mystery drama film directed by Ritesh Batra and written by Nick Payne?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor who starred in both films."
    },
    "films_starred_in": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of the two films the actor starred in."
    },
    "mystery_drama_film_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the mystery drama film."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the mystery drama film."
        },
        "director": {
          "type": "string",
          "description": "The director of the mystery drama film."
        },
        "writer": {
          "type": "string",
          "description": "The writer of the mystery drama film."
        },
        "actor_role_description": {
          "type": "string",
          "description": "A description of the actor's role in the mystery drama film."
        }
      },
      "required": [
        "title",
        "release_year",
        "director",
        "writer",
        "actor_role_description"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actor_name",
    "films_starred_in",
    "mystery_drama_film_details"
  ],
  "additionalProperties": false
}
