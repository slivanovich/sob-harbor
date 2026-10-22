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
Cannon Fodder (film): Cannon Fodder, also known by the alternate titles of "Basar Totahim" and "Battle of the Undead", is a 2013 horror film that was directed by Eitan Gafny, based on a script written by Gafny and Amit Lior, and is Gafny's feature film directorial debut.  The film had its world premiere on 10 May 2013 at the Cape Fear Independent Film Festival and stars Liron Levo as a security operative sent to Lebanon on a final mission, only to discover that his opponents are of the dead.

Babes in Toyland (1934 film): Babes in Toyland is a Laurel and Hardy musical film released on November 30, 1934.  The film is also known by the alternate titles "Laurel and Hardy in Toyland", "Revenge Is Sweet" (the 1948 European reissue title), "March of the Wooden Soldiers", and "Wooden Soldiers" (in the United States).

Marianne Edwards: Marianne Edwards (December 9, 1930 - November 8, 2013) was a former child actress who appeared in the "Our Gang" film series from 1934 to 1936.  She also appeared in several feature films in the 1930s, including "Gold Diggers Of 1933", "Babes In Toyland", "Stand Up and Cheer! ", and "The Wizard Of Oz".

Psi-man Heal My Child!: "Psi-man Heal My Child!"  is a science fiction short story by American writer Philip K. Dick in 1955.  It also has the alternate titles "Psi-man" and "Outside Consultant" and appeared in Dick's short story collection "Second Variety".

Acting on Impulse: Acting on Impulse is a 1993 film starring Linda Fiorentino, Nancy Allen and C. Thomas Howell.  The film, which is also known under the alternate titles "Secret Lives" and "Eyes of a Stranger", premiered at the Seattle International Film Festival on June 3, 1993 before being broadcast by Showtime on July 10, 1993.  Adam Ant, Isaac Hayes, Zelda Rubinstein and Dick Sargent, in his last role, make cameo appearances.

C. S. Leigh: C. S. Leigh (born 1964) is a British-American film director based in London and Paris.  In 1998 he premiered his directing debut "Sentimental Education" under his own name Christian Leigh.  His 2001 film "Far from China" starred singer and actress Marianne Faithfull and featured original music by Suede.  His 2005 film "See You at Regis Debray" is about Andreas Baader.  His last release was "A Quiet American: Ralph Rucci & Paris", a documentary about fashion designer Ralph Rucci.  "Projection", starring Lars Eidinger and Yekaterina Golubeva, is currently in post-production.

Leon Jessel: Leon Jessel, or Léon Jessel (January 22, 1871 – January 4, 1942) was a German composer of operettas and light classical music pieces.  Today he is best known internationally as the composer of the popular jaunty march "The Parade of the Tin Soldiers", also known as "The Parade of the Wooden Soldiers".  Jessel was a prolific composer who wrote hundreds of light orchestral pieces, piano pieces, songs, waltzes, mazurkas, marches, choruses, and other salon music.  He achieved considerable acclaim with a number of his operettas — in particular "Schwarzwaldmädel" ("Black Forest Girl"), which remains popular to this day.

Chaitivel: "Chaitivel", also known as "Les Quatre Deuils" or "Le Malheureux" in modern French or "The Four Sorrows" in English, is a Breton lai by the medieval poet Marie de France.  "Chaitivel" is the tenth poem in the collection known as the "Lais of Marie de France" and is one of very few lais to contain alternate titles.  Like the other poems in this collection, "Chaitivel" is written in the Anglo-Norman dialect of Old French, in couplets of eight syllables in length.

Cain's Cutthroats: Cain's Cutthroats is a 1971 western-themed exploitation film.  It is a story of brutality, betrayal, and revenge set in the period immediately following the end of the American Civil War.  The film was released under the alternate titles "Cain's Way", "The Blood Seekers", and "Justice Cain".  It stars John Carradine, Scott Brady, Darwin Joston, Robert Dix, Tereza Thaw, and Adair Jameson.

The Parade of the Tin Soldiers: The Parade of the Tin Soldiers ("Die Parade der Zinnsoldaten"), also known as The Parade of the Wooden Soldiers, is an instrumental musical character piece, in the form of a popular jaunty march, written by German composer Leon Jessel, in 1897.

Question: Child actress Marianne Edwards starred in what film also known by alternate titles like Revenge is Sweet and Wooden Soldiers?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The primary title of the film."
    },
    "release_year": {
      "type": "integer",
      "description": "The year the film was released."
    },
    "alternate_titles": {
      "type": "array",
      "description": "A list of alternate titles for the film.",
      "items": {
        "type": "string"
      }
    },
    "starring_actress": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the actress."
        },
        "role_type": {
          "type": "string",
          "description": "The type of role the actress was known for (e.g., child actress)."
        }
      },
      "required": [
        "name",
        "role_type"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_title",
    "release_year",
    "alternate_titles",
    "starring_actress"
  ],
  "additionalProperties": false
}
