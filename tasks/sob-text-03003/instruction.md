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
Hichem Yacoubi: Hichem Yacoubi is a Tunisian-born French actor whose most recent film was "A Prophet" (in French "Un prophète") (2009) directed by Jacques Audiard.  He studied theater (including a course at the Actor's Studio) and dance.  He has appeared in several films including a short film which he co-directed and co-wrote the screenplay with Daniel Kupferstein.

Chuck Carrington: Chuck Carrington (born 1968 in Lynchburg, Virginia) is an American actor best known for playing Petty Officer Jason Tiner on "JAG", and also starred as Renny Jacobsen in the independent feature thriller "The List", alongside Malcolm McDowell and Hilarie Burton.

A Prophet: A Prophet (French: Un prophète ) is a 2009 French prison drama-crime film directed by Jacques Audiard from a screenplay he co-wrote with Thomas Bidegain, Abdel Raouf Dafri and Nicolas Peufaillit.  The film stars Tahar Rahim in the title role as an imprisoned petty criminal of Algerian origins who rises in the inmate hierarchy, becoming an assassin and drug trafficker as he initiates himself into the Corsican and then Muslim subcultures.

Irene in Time: Irene in Time is a 2009 American independent film directed by Henry Jaglom.  It marked the second collaboration between director Jaglom and actress Tanna Frederick, who also starred in "Hollywood Dreams", Jaglom's 2006 film.  "Irene" also starred Victoria Tennant, Lanre Idewu, and Andrea Marcovicci.

Richard Reid: Richard Colvin Reid (born 12 August 1973), also known as the Shoe Bomber, is a British man arrested as the prime suspect who attempted to detonate explosives packed into the shoes he was wearing, while on American Airlines Flight 63 from Paris to Miami on December 22, 2001.  Born to a father who was a career criminal, Reid converted to Islam as a young man in prison after years as a petty criminal.  Later he became radicalised and went to Pakistan and Afghanistan, where he trained and became a member of al-Qaeda.

Jude Kuring: Judith Kuring (born November 1948) known as Jude Kuring is an Australian actress who appeared in film and television during the late 1970s and early 80s.  She remains best known for her role as petty criminal Noeline Bourke in the soap opera "Prisoner".

Murder in the First (film): Murder in the First is a 1995 American drama thriller film, directed by Marc Rocco, about a petty criminal named Henri Young (portrayed by Kevin Bacon) who is put on trial for murder in the first degree.  The film also stars Christian Slater and Gary Oldman.

Kartar Singh (1959 film): Kartar Singh (Urdu: ) is a Pakistani Punjabi film about the Partition of India and the violence after it.  It describes the conflicts between Hindus, Muslims and Sikhs.  This film is said to be based on real-life events in 1947.  The title role is about an antagonist Kartar Singh who is a petty criminal and trouble maker.  The title character is played by Allauddin who became very well-known after this film.  He is often remembered for this film.  It is said that Sikhs failed to recognize him as a Muslim,on seeing this film in Indian Punjab theater screens, as he is not a Sikh in real life.  It is considered to be one of the super hit blockbuster Punjabi films in Pakistan and ranks highly in the history of Punjabi cinema.  This film was also shown for three years in East Punjab, India.

Thieves (1996 film): Thieves (French: Les Voleurs ) is a 1996 French drama film directed by André Téchiné, starring Daniel Auteuil, Catherine Deneuve and Laurence Côte.  The plot follows a cynical police officer, who comes from a family of thieves, and a lonely philosophy professor, both romantically involved with a self-destructive petty criminal.  With a puzzling structure, the story is told through a series of flashbacks presented from four different perspectives.

David Huynh: David Huynh (born February 5, 1983) is a Canadian actor.  Huynh won a Special Jury Prize Award at the 2007 Los Angeles Asian Pacific Film Festival for Outstanding Newcomer and Best Emerging Actor for his performance in Juwan Chung's "Baby", which also won a Special Jury Award for Best Feature Length Film at that year's Festival.  Huynh has also Starred in Byron Q's film, "Bang Bang" (2011), which won a Special Jury Award for Best First Feature, Narrative, at the 2011 Los Angeles Asian Pacific Film Festival.  He also played Jonathan Chen in Byron Q's film, "Las Vegas Story" and Ty Do in Mark Tran's film "All About Dad".  He recently stars in a Web Series entitled "Hollywood Aliens" from Beyond Cinema Productions, directed by "Bang Bang" Director Byron Q and Kevin Boston.  He also appears as the protagonist "Fong" in a pilot entitled "Chinatown Squad" about 1890s San Francisco Chinatown, directed and produced by Stephane Gauger and written by and starring "Baby" co-star Feodor Chin, who plays the antagonist, "Pistol Pete."  He has also starred as Benson Fong in Timothy Tau's short film bio-pic Keye Luke, which premiered at the 2012 Los Angeles Asian Pacific Film Festival and which was Closing Night Film of the inaugural 2013 Seattle Asian American Film Festival.

Question: Who played a petty criminal in a film that also starred Hichem Yacoubi in 2009?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor who played the petty criminal."
    },
    "film_title": {
      "type": "string",
      "description": "The title of the film in which the petty criminal character appeared."
    },
    "film_release_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "other_starring_actor": {
      "type": "string",
      "description": "The name of the other actor who also starred in the film."
    },
    "character_role_description": {
      "type": "string",
      "description": "A description of the character played by the identified actor."
    }
  },
  "required": [
    "actor_name",
    "film_title",
    "film_release_year",
    "other_starring_actor",
    "character_role_description"
  ],
  "additionalProperties": false
}
