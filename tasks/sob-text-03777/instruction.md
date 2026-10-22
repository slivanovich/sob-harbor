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
DNA (film): DNA is a 1997 American science fiction action horror film starring Mark Dacascos and Jürgen Prochnow, and directed by William Mesa.  Filming took place in the Philippines.  The film was retitled "ADN - La menace" for its French DVD release, and "Scarabée" for its television showing.  It is also known as "Genetic Code" in some areas of Europe.

Battlefield Earth (film): Battlefield Earth (also referred to as Battlefield Earth: A Saga of the Year 3000) is a 2000 American science fiction action film based upon the first half of L. Ron Hubbard's 1982 novel of the same name.  Directed by Roger Christian and starring John Travolta, Barry Pepper and Forest Whitaker, the film depicts an Earth that has been under the rule of the alien Psychlos for 1,000 years and tells the story of the rebellion that develops when the Psychlos attempt to use the surviving humans as gold miners.

Men in Black (1997 film): Men in Black is a 1997 American science fiction action comedy film directed by Barry Sonnenfeld and produced by Walter F. Parkes and Laurie MacDonald.  Loosely adapted from "The Men in Black" comic book series created by Lowell Cunningham and Sandy Carruthers, the film stars Tommy Lee Jones and Will Smith as two agents of a secret organization called the Men in Black, who supervise extraterrestrial lifeforms who live on Earth and hide their existence from ordinary humans.  The film featured the creature effects and makeup of Rick Baker and visual effects by Industrial Light & Magic.

Paycheck (film): Paycheck is a 2003 American science fiction action film based on the short story of the same name by science fiction writer Philip K. Dick.  The film was directed by John Woo and stars Ben Affleck, Uma Thurman and Aaron Eckhart.  Paul Giamatti, Michael C. Hall, Joe Morton and Colm Feore also appear.

Jumper (2008 film): Jumper is a 2008 American science fiction action film loosely based on the 1992 science fiction novel of the same name written by Steven Gould.  The film is directed by Doug Liman and stars Hayden Christensen, Jamie Bell, Rachel Bilson, Max Thieriot, AnnaSophia Robb, Diane Lane, Michael Rooker, and Samuel L. Jackson.  The film follows a young man capable of teleporting as he is chased by a secret society intent on killing him.  The script went through a rewrite prior to filming and the roles for the main characters were changed during production.  "Jumper" was filmed in 20 cities in 14 countries between 2006-07.  The film was released on February 14, 2008, and the soundtrack was released five days later on February 19.  The film held the first position in its opening weekend with $27.3 million, but received generally unfavourable reviews from critics, mostly due to the many changes from Gould's novel, rushed plot and anti-climactic ending.

Nick Loren: Nick Loren (born December 14, 1970) is an American actor, singer-songwriter, producer, and professional stunt double.  He has been the professional stunt double for John Travolta and an accredited actor in over 17 films including "From Paris with Love", "Old Dogs", "Wild Hogs", "Hairspray", "A Love Song for Bobby Long", "Be Cool", "Swordfish", and "Face/Off".  Loren has been featured on "Entertainment Tonight", "The Insider", "The Hollywood Reporter", AdAge.com, , "Dateline NBC", "Eye on LA", as well as many morning shows and magazines.

Face/Off: Face/Off is a 1997 American science fiction action film directed by John Woo, written by Mike Werb and Michael Colleary, and starring John Travolta and Nicolas Cage.  Travolta plays an FBI agent and Cage plays a terrorist, sworn enemies who assume each other's physical appearance.

Action film: Action film is a genre in which the protagonist or protagonists end up in a series of challenges that typically include violence, extended fighting, physical feats, and frantic chases.  Action films tend to feature a resourceful hero struggling against incredible odds, which include life-threatening situations, a villain, or a pursuit which generally concludes in victory for the hero (though a small number of films in this genre "have" ended in victory for the villain instead).  Advancements in CGI have made it cheaper and easier to create action sequences and other visual effects that required the efforts of professional stunt crews in the past.  However, reactions to action films containing significant amounts of CGI have been mixed as films that use computer animations to create unrealistic, highly unbelievable events are often met with criticism.  While action has long been a recurring component in films, the "action film" genre began to develop in the 1970s along with the increase of stunts and special effects.

The 5th Wave (film): The 5th Wave is a 2016 American science fiction action film directed by J Blakeson, with a screenplay by Susannah Grant, Akiva Goldsman, and Jeff Pinkner, based on the novel of the same name by Rick Yancey.  The film stars Chloë Grace Moretz, Nick Robinson, Ron Livingston, Maggie Siff, Alex Roe, Maria Bello, Maika Monroe and Liev Schreiber.

James Cameron filmography: James Cameron is a Canadian director, screenwriter, and producer who has had an extensive career in film and television.  Cameron's debut was the 1978 science fiction short "Xenogenesis", which he directed, wrote and produced.  In the early part of his career, he did various technical jobs such as special visual effects producer, set dresser assistant, matte artist, and photographer.  His feature directorial debut was the 1981 release "".  The next film he directed was the science fiction action thriller "The Terminator" (1984).  It starred Arnold Schwarzenegger as the titular cyborg assassin, and was Cameron's breakthrough feature.  In 1986, he directed and wrote the science fiction action sequel "Aliens" starring Sigourney Weaver.  He followed this by directing another science fiction film "The Abyss" (1989).  In 1991, Cameron directed the sequel to "The Terminator", "" (with Schwarzenegger reprising his role), and also executive produced the action crime film "Point Break".  Three years later he directed a third Schwarzenegger-starring action film "True Lies" (1994).

Question: Nick Loren was the professional stunt double for John Travolta in a 1997 American science fiction action film directed by who?

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
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The genres of the film."
    },
    "director": {
      "type": "string",
      "description": "The director of the film."
    },
    "stunt_double_details": {
      "type": "object",
      "properties": {
        "stunt_double_name": {
          "type": "string",
          "description": "The name of the professional stunt double."
        },
        "actor_stunt_doubled_for": {
          "type": "string",
          "description": "The name of the actor for whom the stunt double worked."
        }
      },
      "required": [
        "stunt_double_name",
        "actor_stunt_doubled_for"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_title",
    "film_year",
    "film_genre",
    "director",
    "stunt_double_details"
  ],
  "additionalProperties": false
}
