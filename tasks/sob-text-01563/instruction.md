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
Stan Laurel: Stan Laurel (born Arthur Stanley Jefferson; 16 June 1890 – 23 February 1965) was an English comic actor, writer and film director, who was part of the comedy duo Laurel and Hardy.  He appeared with his comedy partner Oliver Hardy in 107 short films, feature films, and cameo roles.

Simon MacCorkindale: Simon Charles Pendered MacCorkindale (12 February 195214 October 2010) was a British actor, film director, writer and producer.  MacCorkindale spent much of his childhood moving around due to his father's commission with the Royal Air Force.  Poor eyesight prevented him following a similar career in the RAF, so he instead planned to become a theatre director.  Training at the Theatre of Arts in London, MacCorkindale started work as an actor, making his West End debut in 1974.  He went on to appear in numerous roles in television, including the series "I, Claudius" and "Jesus of Nazareth", before starring as Simon Doyle in the film "Death on the Nile" (1978).  This proved to be a breakthrough role and allowed MacCorkindale to move to the United States, where he appeared in a variety of films and TV series including "Quatermass" (1979), "The Riddle of the Sands" (1979), "The Sword and the Sorcerer" (1982) and "Jaws 3-D" (1983).

Sands of the Kalahari: Sands of the Kalahari is a 1965 British adventure film starring Stuart Whitman, Stanley Baker, Susannah York, Harry Andrews and Theodore Bikel, based on the 1960 novel by William Mulvihill.  The screenplay was written by Cy Endfield and William Mulvihill and directed by Cy Endfield.  It was filmed in South-West Africa and Spain and released by Paramount Pictures.

Vibes (film): Vibes is a 1988 American romantic adventure comedy film starring Cyndi Lauper, Jeff Goldblum, Julian Sands and Peter Falk.  It was directed by Ken Kwapis.  The plot revolves around Sylvia, a ditzy psychic, and Nick, her equally odd psychic friend and their trip into the Ecuadorian Andes to find the "source of psychic energy".

The Garage (1920 film): The Garage is a 1920 American short comedy film starring Buster Keaton and Roscoe "Fatty" Arbuckle.  It was directed by Arbuckle himself.  The film was also known as Fire Chief.  This was the fourteenth film starring the duo.  The film also stars Luke the Dog who starred in many other short comedies starring Keaton and Arbuckle.

La piste: La Piste (The Trail) is a 2006 French film starring Julian Sands and Camille Summers.  The film was directed by French photographer and director Éric Valli.

Scorching Sun, Fierce Winds, Wild Fire: Scorching Sun, Fierce Winds, Wild Fire, also released as Any Which Way You Punch, is a 1978 Taiwanese kung fu film starring Angela Mao, Dorian Tan, Chang Yi, and Lo Lieh.

Scorching Sands: Scorching Sands is a 1923 American silent film starring Stan Laurel.

The Wreck of the Mary Deare: The Wreck of the Mary Deare is a 1956 novel written by British author Hammond Innes, which was later adapted as a film starring Gary Cooper released in 1959 by MGM.  It tells the story of a very old ship described as "A deathtrap of rattling rivets", which is found adrift at sea by salvageer John Sands.  Sands boards it hoping to claim it for salvage, but finds the first officer, Gideon Patch, still aboard and trying to run the ship on his own.  Patch convinces Sands to help him beach the ship, even though it will void his salvage claim.  When they return to London, Patch is brought before a board of inquiry to determine what happened.  It soon becomes apparent that the ship owners were planning to wreck the "Mary Deare" all along and have Patch as the fall guy.

Sands of Iwo Jima: Sands of Iwo Jima is a 1949 war film starring John Wayne that follows a group of United States Marines from training to the Battle of Iwo Jima during World War II.  The film also features John Agar, Adele Mara and Forrest Tucker, was written by Harry Brown and James Edward Grant, and directed by Allan Dwan.  The picture was a Republic Pictures production.

Question: Scorching Sands was a film starring the actor who was a part of what duo?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film mentioned in the question."
    },
    "starring_actor": {
      "type": "string",
      "description": "The name of the actor who starred in the film."
    },
    "actor_details": {
      "type": "object",
      "properties": {
        "comedy_duo_name": {
          "type": "string",
          "description": "The name of the comedy duo the actor was a part of."
        },
        "duo_partner": {
          "type": "string",
          "description": "The name of the actor's partner in the comedy duo."
        }
      },
      "required": [
        "comedy_duo_name",
        "duo_partner"
      ],
      "additionalProperties": false
    },
    "final_answer": {
      "type": "string",
      "description": "The name of the comedy duo."
    }
  },
  "required": [
    "film_title",
    "starring_actor",
    "actor_details",
    "final_answer"
  ],
  "additionalProperties": false
}
