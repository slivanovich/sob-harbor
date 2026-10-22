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
Royal Blood (Doctor Who): Royal Blood is a BBC Books original novel written by Una McCormack and based on the long-running British science fiction television series "Doctor Who".  It features the Twelfth Doctor and Clara Oswald.  The book was released on 10 September 2015 as a part of "The Glamour Chronicles", alongside "Big Bang Generation" and "Deep Time".

Peter Capaldi: Peter Dougan Capaldi (born 14 April 1958) is a Scottish actor, writer and director, best known for playing the twelfth incarnation of the Doctor in "Doctor Who" and as spin doctor Malcolm Tucker in "The Thick of It", for which he has received four British Academy Television Award nominations, winning Best Male Comedy Performance in 2010.  For reprising the role in the spinoff film "In the Loop", Capaldi was honoured with several film critic award nominations for Best Supporting Actor.  He further took on the role of Paddington Bear's neighbour Mr. Curry in the family comedy film "Paddington"; he is set to reprise the role in "Paddington 2".

Doctor Puppet: Doctor Puppet (also known as The Doctor Puppet) is a US/UK stop-motion science fiction animation fan series that celebrates the top selling BBC TV series, "Doctor Who" and its rich history through hand-crafted puppets and original stories.  Created by Alisa Stern in 2012 in her New York apartment, Doctor Puppet consists of a Tumblr blog, an eight episode series of short films featuring the likenesses of the Eleventh Doctor (Matt Smith) and other Doctors and characters from the BBC TV series, other short films with the Twelfth Doctor (Peter Capaldi) and Clara Oswald (Jenna Coleman), three Christmas specials, music videos, behind the scenes documentaries and Google Hangouts with the creative team.  The series is composed and narrated by UK film score composer Scott Ampleford.

Last Christmas (Doctor Who): "Last Christmas" is an episode of the British science fiction television series "Doctor Who" that was first broadcast on 25 December 2014.  It is the tenth Christmas special since the show’s revival in 2005, and the first full Christmas special to feature the Twelfth Doctor.  It was written by Steven Moffat and directed by Paul Wilmshurst.

Deep Time (Doctor Who): Deep Time is a BBC Books original novel written by Trevor Baxendale and based on the long-running British science fiction television series "Doctor Who".  It features the Twelfth Doctor and Clara Oswald.  The book was released on 10 September 2015 as a part of "The Glamour Chronicles", alongside "Royal Blood" and "Big Bang Generation".

Big Bang Generation: Big Bang Generation is a BBC Books original novel written by Gary Russell and based on the long-running British science fiction television series "Doctor Who".  It features the Twelfth Doctor and Bernice Summerfield, making her first appearance in the New Series Adventures along with the Doctor from the revived series.  The book was released on 10 September 2015 as a part of "The Glamour Chronicles", alongside "Royal Blood" and "Deep Time".

The Blood Cell: The Blood Cell is a BBC Books original novel written by James Goss and based on the long-running British science fiction television series "Doctor Who".  It features the Twelfth Doctor and Clara Oswald.  The book was released on 11 September 2014 along with "Silhouette" and "The Crawling Terror".

Paddington 2: Paddington 2 is an upcoming British-French family-comedy film directed by Paul King, co written by King and Simon Farnaby, and produced by David Heyman.  It is the sequel to 2014's "Paddington".  The film stars Hugh Grant, Brendan Gleeson, Hugh Bonneville, Sally Hawkins, Julie Walters, Jim Broadbent, Peter Capaldi, Madeleine Harris, Samuel Joslin, and the voices of Ben Whishaw and Imelda Staunton.  Production began in October 2016, and ended in June 2017.  The film is set to release on 10 November 2017.

The Time of the Doctor: "The Time of the Doctor" is an episode of the British science fiction television programme "Doctor Who", written by Steven Moffat and directed by Jamie Payne, and was broadcast as the ninth "Doctor Who" Christmas special on 25 December 2013 on BBC One.  It features the final regular appearance of Matt Smith as the Eleventh Doctor and the first regular appearance of Peter Capaldi as the Twelfth Doctor following his brief cameo in "The Day of the Doctor".  The episode also features Jenna Coleman as the Doctor's companion Clara Oswald, plus several enemies of the Doctor, including the Cybermen, Silence, Daleks, and Weeping Angels.

The Crawling Terror: The Crawling Terror is a BBC Books original novel written by Mike Tucker and based on the long-running British science fiction television series "Doctor Who".  It features the Twelfth Doctor and Clara Oswald.  The book was released on 11 September 2014 along with "The Blood Cell" and "Silhouette".

Question: Which film, directed by Paul King, features the twelfth Doctor from Doctor Who?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "director": {
      "type": "string",
      "description": "The director of the film."
    },
    "doctor_actor_name": {
      "type": "string",
      "description": "The name of the actor who plays the Twelfth Doctor and is featured in the film."
    },
    "doctor_actor_role_in_film": {
      "type": "string",
      "description": "The specific role played by the actor in the film."
    },
    "is_doctor_character_in_film": {
      "type": "boolean",
      "description": "Indicates if the actual 'Twelfth Doctor' character appears in the film, or just the actor who plays him."
    }
  },
  "required": [
    "film_title",
    "director",
    "doctor_actor_name",
    "doctor_actor_role_in_film",
    "is_doctor_character_in_film"
  ],
  "additionalProperties": false
}
