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
Eyes of the Soul: Eyes of the Soul is a lost 1919 American silent romantic drama film produced by Famous Players-Lasky and distributed through Paramount Pictures and Artcraft.  The star of the picture is Elsie Ferguson and its director was Emile Chautard.

The Eaglet (1913 film): The Eaglet (French:L'aiglon) is a 1913 French silent historical film directed by Emile Chautard.  It is an adaptation of the play "L'Aiglon" by Edmond Rostand, which portrays the life of Napoleon II.

The Marriage Price: The Marriage Price is a 1919 American silent romantic drama film produced by Famous Players-Lasky and distributed through Paramount Pictures and Artcraft.  Emile Chautard directed and Elsie Ferguson stars.  This film is lost.

Forsaking All Others (1922 film): Forsaking All Others is a 1922 American dramatic film starring actress Colleen Moore and directed by Emile Chautard for Universal Studios.  It was made before Colleen became famous as a flapper but did visit some of the same subjects her later films would.

Josef von Sternberg: Josef von Sternberg, (29 May 1894 – 22 December 1969) was an Austrian-American film director.  His family emigrated permanently to the United States when he was fourteen, and he grew up in New York City.  He started working at World Film Company in Fort Lee, New Jersey, where he was mentored by French director Emile Chautard.

A Hungry Heart: A Hungry Heart is a 1917 silent film drama directed by Emile Chautard and starring Alice Brady.  It was produced and distributed by World Film Corporation.  It is sometimes called The Hungry Heart but shouldn't be confused with the Pauline Frederick film of the same year.

The Web of Desire: The Web of Desire is a lost 1917 silent film drama directed by Emile Chautard and starring Ethel Clayton.  It was produced by Peerless Studios and distributed through World Pictures.

The Mystery of the Yellow Room (1919 film): The Mystery of the Yellow Room is a 1919 American crime drama film made by the Mayflower Photoplay Company and distributed through Realart Pictures Corporation.  Emile Chautard was a French actor, director, and producer.  Chautard was 55 years old when "The Mystery of the Yellow Room" was released in 1919.  "The Mystery of the Yellow Room" (in French "Le mystère de la chambre jaune") was first a novel by Gaston Leroux.  The novel was one of the first locked room mystery crime fiction novels.  It was first published in France in the periodical "L'Illustration" from September 1907 to November 1907, then in its own right as a book in 1908.

Dishonored (film): Dishonored is a 1931 Pre-Code romantic spy film made by Paramount Pictures.  It was co-written (with Daniel N. Rubin), directed and edited by Josef von Sternberg.  The costume design was by Travis Banton.  The film stars Marlene Dietrich, Victor McLaglen, Gustav von Seyffertitz and Warner Oland.

His Parisian Wife: His Parisian Wife is a lost 1919 silent film romantic drama produced by Famous Players-Lasky and distributed by Paramount Pictures.  It was directed by Emile Chautard and starred Elsie Ferguson.  The source for this picture was a novel by Andrew Soutar.

Question: Dishonored was edited by which director, who was a mentee of Emile Chautard?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "director_name": {
      "type": "string",
      "description": "The name of the director who edited the film."
    },
    "film_edited": {
      "type": "string",
      "description": "The title of the film that was edited."
    },
    "mentor_details": {
      "type": "object",
      "properties": {
        "mentor_name": {
          "type": "string",
          "description": "The name of the director's mentor."
        },
        "mentorship_context": {
          "type": "string",
          "description": "The context or place where the mentorship occurred."
        }
      },
      "required": [
        "mentor_name",
        "mentorship_context"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "director_name",
    "film_edited",
    "mentor_details"
  ],
  "additionalProperties": false
}
