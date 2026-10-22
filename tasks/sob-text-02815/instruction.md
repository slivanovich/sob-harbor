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
Timothy Pesci: Timothy L. Pesci (June 26, 1944 – September 28, 2016) was a former Democratic member of the Pennsylvania House of Representatives, where he represented the 60th legislative district from 1989 to 2000.

The Enfield Haunting: The Enfield Haunting is a British drama horror series which was commissioned by Sky Living and first aired on 3 May 2015.  Kristoffer Nyholm, who rose to fame after the hugely popular Danish series, "The Killing", directed the new three-parter.  The series is based on Guy Lyon Playfair’s book, "This House Is Haunted" and is about a series of bizarre events around the phenomena collectively known as ‘The Enfield Poltergeist’ that took place at a council house from August 1977 to 1979.  The drama draws upon recordings and witness statements to draw the audience in to the unfolding supernatural events.  The series finished on 17 May 2015 after the third and last episode aired.

Timothy Spall: Timothy Leonard Spall, OBE (born 27 February 1957) is an English character actor and occasional presenter.  He became a household name in the UK after appearing as Barry Spencer Taylor in the 1983 ITV comedy-drama series "Auf Wiedersehen, Pet".

Timothy Barr: Timothy L. Barr is an American politician.  He is a member of the Georgia House of Representatives from the 103rd District, serving since 2013.  Barr has sponsored 205 bills.  He is a member of the Republican party.

Final Exam (film): Final Exam is an 1981 American slasher film written and directed by Jimmy Huston and starring Cecile Bagdadi, Joel S. Rice & Timothy L. Raynor.  The plot follows a killer stalking the remaining group of students left on a college campus days before the university's summer vacation.

Maurice Grosse: Maurice Grosse (6 March 1919 – 14 October 2006) was a British paranormal investigator.  Famous for his involvement in the Enfield Poltergeist case from 1977 to 1979, he has subsequently been portrayed in "The Enfield Haunting" (2015) by Timothy Spall and most recently in "The Conjuring 2" (2016) by Simon McBurney.

Elliot Kerley: Elliot Jude Kerley (born 8 November 2004) is an English child actor.  His roles have included parts in "The Bletchley Circle" and "The Enfield Haunting".  He began to voice Bing the bunny in the show "Bing" on CBeebies in 2014 when he was nine years old.

Timothy L. Raynor: Timothy L. Raynor (born March 15, 1950) is an American actor, stuntman, and stunt choreographer who is best known for his work on Jimmy Huston's 1981 slasher film "Final Exam", where he portrayed "The Killer" as well as acting as a fight choreographer.  Raynor has also appeared on television shows such as "Life", "My Name Is Earl", "Do Not Disturb", and "".  Recently, he has appeared in many independent films and shorts.

Eleanor Worthington Cox: Eleanor Worthington Cox (born 21 June 2001) is a British child actress from Merseyside most known for portraying Matilda Wormwood in "Matilda the Musical" for which she won a Laurence Olivier Award for Best Actress, and Janet Hodgson in "The Enfield Haunting", for which she received a British Academy Television Award nomination.  Worthington Cox is the youngest recipient of an Olivier Award at the age of 10.

Matthew Macfadyen: David Matthew Macfadyen (born 17 October 1974) is a BAFTA award-winning British actor, known for his roles as MI5 Intelligence Officer Tom Quinn in the BBC television drama series "Spooks", Mr. Darcy in the 2005 film of "Pride & Prejudice" and Daniel in the Frank Oz comedy "Death at a Funeral".  He is also known for portraying John Birt in the political drama "Frost/Nixon", as well as Detective Inspector Edmund Reid in the BBC series "Ripper Street".  In 2015 he starred in the Sky Living series "The Enfield Haunting" as Guy Lyon Playfair.

Question: Who did Timothy L. Spall portray in the film "The Enfield Haunting"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The full name of the actor."
    },
    "character_portrayed": {
      "type": "string",
      "description": "The name of the character the actor portrayed."
    },
    "production_title": {
      "type": "string",
      "description": "The title of the film or series where the portrayal occurred."
    },
    "production_type": {
      "type": "string",
      "description": "The type of production (e.g., 'series', 'film')."
    },
    "year_of_portrayal": {
      "type": "integer",
      "description": "The year the portrayal took place or the production aired."
    }
  },
  "required": [
    "actor_name",
    "character_portrayed",
    "production_title",
    "production_type",
    "year_of_portrayal"
  ],
  "additionalProperties": false
}
