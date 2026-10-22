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
Louis Mandylor: Louis Mandylor (born Elias Theodosopoulos; Greek: Ηλίας Θεοδοσόπουλος; 13 September 1966) is a Greek Australian film and television actor.  He is best recognized as Nick Portokalos in "My Big Fat Greek Wedding" (2002), a role he reprised in the sequel "My Big Fat Greek Wedding 2" (2016).

Alexandra Breckenridge: Alexandra Hetherington Breckenridge (born May 15, 1982) is an American actress and photographer.  She began her career with supporting roles in the teen comedy films "Big Fat Liar" (2002) and "She's the Man" (2006).  She later played reporter Willa McPherson in the series "Dirt", and had a supporting role on the short-lived series "The Ex List".  She is also the voice of various characters on the animated television series "Family Guy".  She starred in the first season of FX's "" as young Moira O'Hara, and portrayed Kaylee in the third season, "".  She portrayed Jessie Anderson in the AMC series "The Walking Dead".

My Big Fat Obnoxious Boss: My Big Fat Obnoxious Boss was a television show on the Fox Network that was filmed in July 2004 and aired from November–December 2004.  Similar to "My Big Fat Obnoxious Fiance," it was a parody of shows such as "The Apprentice."  The contestants performed several tasks that they were all told would help them win a job at the Chicago-based conglomerate IOCOR and a $250,000 prize.  However, none of the contestants knew that the company – and the position – were fake.

Michael Moore Is a Big Fat Stupid White Man: Michael Moore Is a Big Fat Stupid White Man is a book by David T. Hardy and Jason Clarke about author and filmmaker Michael Moore, criticizing him and his works.  The title can be seen as a parody of the titles "Stupid White Men" by Moore and "Rush Limbaugh is a Big Fat Idiot" by Al Franken.  It was listed as a best-seller for several weeks by "The New York Times".

Move It Like This: Move It Like This is the seventh studio album released by Bahamas-based group Baha Men.  It was released in 2002 under S-Curve record, making it their first album under the label.  The album includes a cover of Harry Nilsson's "Coconut".  None of the songs rose to success, including the album's title single "Move It Like This," but the album did chart at number 57 on the "Billboard" 200.  Two of the songs were used in feature films including "Move It Like This" ("Big Fat Liar") and "Best Years of Our Lives" ("Shrek").  One of the VEE's Shows used this song in "Barney Live in Concert".

Frankie Muniz: Francisco "Frankie" Muniz IV (born December 5, 1985) is an American actor, musician, writer, producer, race car driver, and band manager.  He is best known for playing the title character in the Fox television family sitcom "Malcolm in the Middle", which earned him an Emmy Award nomination and two Golden Globe Award nominations.

My Big Fat Greek Life: My Big Fat Greek Life is an American sitcom that ran on CBS in 2003.  The series is a continuation of the 2002 movie "My Big Fat Greek Wedding" and was produced by Sony Pictures Television and Tom Hanks's Playtone Productions for Sony Pictures Television.  The two lead characters' names are changed, from Toula to Nia, and Ian to Thomas.

Shawn Levy: Shawn Levy (born July 23, 1968) is a Canadian film director, producer, and actor.  He directed the films "Big Fat Liar" (2002), "Just Married" (2003), "Cheaper by the Dozen" (2003), "The Pink Panther" (2006), "Night at the Museum" (2006), "" (2009), "Date Night" (2010), "Real Steel" (2011), "The Internship" (2013), "This Is Where I Leave You" (2014) and "" (2014).

Big Fat Liar: Big Fat Liar is a 2002 American teen comedy film, directed by Shawn Levy, written by Dan Schneider and Brian Robbins, and starring Frankie Muniz, Paul Giamatti and Amanda Bynes, with Amanda Detmer, Donald Faison and Lee Majors.

Paul Giamatti: Paul Edward Valentine Giamatti ( ; born June 6, 1967) is an American actor and producer.  He was nominated for an Academy Award for Best Supporting Actor for the film "Cinderella Man" and is also known for his roles in the films " Thunderpants", " Private Parts", " Sideways", "American Splendor," "The Illusionist", "Cold Souls", "Barney's Version", "Big Fat Liar", "Love & Mercy", "Straight Outta Compton", "San Andreas", and "Win Win", as well as the series "Downton Abbey" and the miniseries "John Adams".  He has won two Golden Globe Awards, a Primetime Emmy Award, and four Screen Actors Guild Awards.

Question: Big Fat Liar starred the actor who played the title character on what Fox family sitcom?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "movie_title": {
      "type": "string",
      "description": "The title of the film mentioned in the question."
    },
    "actor_details": {
      "type": "object",
      "properties": {
        "actor_name": {
          "type": "string",
          "description": "The name of the actor who starred in both the movie and the sitcom."
        },
        "actor_known_for_sitcom": {
          "type": "boolean",
          "description": "Indicates if the actor is best known for the sitcom."
        }
      },
      "required": [
        "actor_name",
        "actor_known_for_sitcom"
      ],
      "additionalProperties": false
    },
    "sitcom_details": {
      "type": "object",
      "properties": {
        "sitcom_title": {
          "type": "string",
          "description": "The title of the Fox family sitcom."
        },
        "network": {
          "type": "string",
          "description": "The television network the sitcom aired on."
        },
        "genre": {
          "type": "string",
          "description": "The genre of the television series."
        },
        "actor_role_in_sitcom": {
          "type": "string",
          "description": "The role the actor played in the sitcom."
        }
      },
      "required": [
        "sitcom_title",
        "network",
        "genre",
        "actor_role_in_sitcom"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "movie_title",
    "actor_details",
    "sitcom_details"
  ],
  "additionalProperties": false
}
