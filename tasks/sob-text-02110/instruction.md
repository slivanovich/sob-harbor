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
John Carroll Lynch: John Carroll Lynch (born August 1, 1963) is an American actor.  He first gained notice for his role as Norm Gunderson in "Fargo".  He is also known for his television work on the ABC sitcom "The Drew Carey Show" as the title character's cross-dressing brother, Steve Carey, as well as on "" and "" as Twisty the Clown.  His films include "Face/Off", "Gran Torino", "Shutter Island", "Ted 2", "The Invitation", and "Zodiac".  Most recently, he portrayed McDonald's co-founder Maurice "Mac" McDonald in "The Founder".  He made his directorial debut with the 2017 film "Lucky".

Lucky (2017 American film): Lucky is a 2017 American drama film directed by John Carroll Lynch from a screenplay by Logan Sparks and Drago Sumonja.  It stars Harry Dean Stanton in one of his final on-screen roles before his death on September 15, 2017.

Miracles from Heaven (film): Miracles from Heaven is a 2016 American Christian drama film directed by Patricia Riggen and written by Randy Brown.  It is based on "Miracles from Heaven" by Christy Beam, which recounts the true story of her young daughter who had a near-death experience and was later cured of an incurable disease.  The film stars Jennifer Garner, Kylie Rogers, Martin Henderson, John Carroll Lynch, Eugenio Derbez, and Queen Latifah.  Principal photography began in Atlanta, Georgia, in July 2015.  The film was released on March 16, 2016.  The movie was financially successful, and although critical reception was mixed, Garner's performance earned general praise.

The Founder: The Founder is a 2016 American biographical drama film directed by John Lee Hancock and written by Robert Siegel.  The film stars Michael Keaton as businessman Ray Kroc, and portrays the story of his creation of the McDonald's fast food chain.  Nick Offerman and John Carroll Lynch co-star as McDonald's founders Richard and Maurice McDonald.

John Carroll University: John Carroll University (Latin: Universitas Joannis Carroll) is a private, co-educational Jesuit Catholic university in University Heights, Ohio, United States, a suburb of Cleveland.  It is primarily an undergraduate, liberal arts institution, accompanied by the AACSB-accredited John M. and Mary Jo Boler School of Business.  John Carroll has an enrollment of 3,673 undergraduate and 536 graduate students.  The university offers undergraduate programs in the liberal arts, sciences, and business, and in selected areas at the master's level.  John Carroll offers 70 academic programs of study for undergraduate students.  The university has been ranked in the top 10 of Midwest regional universities by U.S. News & World Report's annual guide, "America's Best Colleges," for 29 consecutive years.

Body of Proof (season 1): The first season of "Body of Proof", an American television series created by Christopher Murphey, commenced airing in the United States on March 29, 2011, concluded May 17, 2011, and consisted of 9 episodes.  It follows the life and career of Dr. Megan Hunt, a medical examiner, once a neurosurgeon, who now works in Philadelphia's Medical Examiner's office after a car accident ended her neurosurgery career.  Along with Hunt solving homicide cases are her colleagues, Nicholas Bishop as Peter Dunlop, Jeri Ryan as Dr. Kate Murphy, John Carroll Lynch and Sonja Sohn as Detective's Bud Morris and Samantha Baker and fellow medical examiners, Geoffrey Arend as Dr. Ethan Gross and Windell Middlebrooks as Dr. Curtis Brumfield.  Mary Mouser plays Megan's daughter Lacey, Jeffrey Nordling plays her ex-husband Todd and Joanna Cassidy plays her mother Joan.  All of whom she has a strained relationship with, one of the continuing stories throughout the season.

Zodiac (film): Zodiac is a 2007 American mystery-thriller film directed by David Fincher.  The screenplay by James Vanderbilt is based on the 1986 non-fiction book of the same name by Robert Graysmith.  The film stars Jake Gyllenhaal, Mark Ruffalo, and Robert Downey, Jr., with Anthony Edwards, Brian Cox, Elias Koteas, Donal Logue, John Carroll Lynch, Dermot Mulroney, and Chloë Sevigny in supporting roles.

The Pretty One: The Pretty One is a 2013 comedy drama film directed and written by Jenée LaMarque.  The film stars Zoe Kazan, Jake Johnson, Ron Livingston, Sterling Beaumon and John Carroll Lynch.

Drew Live: "Drew Live" is the eighth episode of the fifth season of the American sitcom "The Drew Carey Show", and the 109th overall.  The episode's plot focuses on Drew (Drew Carey) trying to stop his friend, Kate (Christa Miller), from pursuing a relationship with a mystery guy, as Drew is in love with her.  However, Drew is unaware that he is stopping Kate from pursuing him.  Meanwhile, Drew's brother Steve (John Carroll Lynch) and his fiancée Mimi Bobeck (Kathy Kinney) hold a joint bachelor and bachelorette party.

Camp X-Ray (film): Camp X-Ray is a 2014 American independent drama film based on the detention facility Camp X-Ray at the Guantanamo Bay detention camp.  The film is the directorial debut of Peter Sattler who also wrote the screenplay.  It stars Kristen Stewart and Peyman Moaadi with John Carroll Lynch, Lane Garrison, and Joseph Julian Soria in supporting roles.  The film premiered on January 17, 2014, at 2014 Sundance Film Festival in the U.S. dramatic competition category and released on October 17, 2014, by IFC Films.

Question: Who costarred as John Carroll Lynch's brother in his most recent film?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor who costarred as John Carroll Lynch's brother."
    },
    "film_title": {
      "type": "string",
      "description": "The title of the film where the costarring role occurred."
    },
    "character_played_by_actor": {
      "type": "string",
      "description": "The name of the character played by the identified actor."
    },
    "character_played_by_john_carroll_lynch": {
      "type": "string",
      "description": "The name of the character played by John Carroll Lynch in the film."
    },
    "relationship_type": {
      "type": "string",
      "description": "The type of relationship between the two characters."
    }
  },
  "required": [
    "actor_name",
    "film_title",
    "character_played_by_actor",
    "character_played_by_john_carroll_lynch",
    "relationship_type"
  ],
  "additionalProperties": false
}
