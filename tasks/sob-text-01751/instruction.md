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
Jennifer Kent: Jennifer Kent is an Australian actress, writer and director, best known for her horror film "The Babadook" (2014), which was her directorial debut.  She is currently filming her second film, "The Nightingale".

The Babadook: The Babadook is a 2014 Australian psychological horror film written and directed by Jennifer Kent in her directorial debut, and produced by Kristina Ceyton and Kristian Moliere.  The film stars Essie Davis, Noah Wiseman, Daniel Henshall, Hayley McElhinney, Barbara West, and Ben Winspear.  It is based on the 2005 short film "Monster", also written and directed by Kent.

Mindhorn: Mindhorn is a British 2016 independent comedy film directed by Sean Foley, written by Julian Barratt and Simon Farnaby, and produced by Steve Coogan and Ridley Scott.  It stars Barratt, Farnaby, Essie Davis, Russell Tovey and Andrea Riseborough, with cameo appearances by Kenneth Branagh and Simon Callow as themselves.  Barratt plays Richard Thorncroft, a faded television actor drawn into negotiations with a criminal who believes his character Detective Mindhorn is real.

Leprechaun (film): Leprechaun is a 1993 American horror comedy film written and directed by Mark Jones.  It stars Warwick Davis in the title role and Jennifer Aniston in her film debut.  Davis plays a vengeful leprechaun who believes a family has stolen his pot of gold.  As he hunts them, they attempt to locate his gold to vanquish him.  The film was originally meant to be more of a straight horror film, but Davis injected humor into his role.  Re-shoots also added increased gore to appeal to older audiences.

Lila &amp; Eve: Lila & Eve is a 2015 American crime drama film directed by Charles Stone III and written by Patrick Gilfillan.  The film stars Viola Davis and Jennifer Lopez.  It premiered on January 30, 2015, at the Sundance Film Festival.  The film was released in North America on July 17, 2015, in a limited release and through video on demand by Samuel Goldwyn Films.  This marks the second time Davis and Lopez acted in a film together, the first being the Steven Soderbergh film "Out of Sight" in 1998.

The Nightingale (2017 film): The Nightingale is an upcoming Australian period thriller film written and directed by Jennifer Kent.  Set in 1825 in the British penal colony of Van Diemen's Land (now the Australian state of Tasmania), the film follows a young convict woman seeking revenge on a soldier who murdered her family.  It began filming in March 2017.

Mr. Popper's Penguins (film): Mr. Popper's Penguins is a 2011 American family comedy film distributed by 20th Century Fox, directed by Mark Waters, produced by John Davis, co-produced by Davis Entertainment Company and Dune Entertainment, written by Sean Anders, John Morris and Jared Stern with music by Rolfe Kent and starring Jim Carrey, Carla Gugino, Madeline Carroll, Maxwell Perry Cotton, Angela Lansbury, Desmin Borges, Philip Baker Hall, Dominic Chianese, Clark Gregg, Ophelia Lovibond, Jeffrey Tambor, David Krumholtz, Henry Keleman, Dylan Clark Marshall with Frank Welker and James Tupper.  It was loosely based on the children's book of the same name.  The film was originally slated for a release on August 12, 2011, but was moved up to June 17, 2011.  The film received mixed reviews from critics and it earned $187.3 million on a $55 million budget.

Essie Davis: Esther "Essie" Davis (born January 7, 1970) is an Australian actress.  She is best known for her roles as Phryne Fisher in "Miss Fisher's Murder Mysteries" and Amelia Vanek in "The Babadook".  Other major work has included a recurring role in season six of the TV series "Game of Thrones", and a role as Elizabeth Woodville in the TV series "The White Princess", an adaptation of Philippa Gregory's historical novel.

River Street (film): River Street is a 1996 Australian film directed by Tony Mahood and starring Aden Young, Bill Hunter, Essie Davis, and Mitchell Dillon.  It started filming on 18 September 1995.

Uncle Kent: Uncle Kent is a 2011 American film written by Kent Osborne and co-written and directed and Joe Swanberg.  The film stars Kent Osborne in the titular role of Kent, and Jennifer Prediger, Josephine Decker, Kevin Bewersdof, and Swanberg.  The film premiered at the Sundance Film Festival and was released through video on demand, the same day on January 21, 2011.

Question: Which film did Essie Davis play in that was directed by Jennifer Kent?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "director_name": {
      "type": "string",
      "description": "The name of the film's director."
    },
    "actor_name": {
      "type": "string",
      "description": "The name of the actor who played in the film."
    },
    "release_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "film_genre": {
      "type": "string",
      "description": "The genre of the film."
    }
  },
  "required": [
    "film_title",
    "director_name",
    "actor_name",
    "release_year",
    "film_genre"
  ],
  "additionalProperties": false
}
