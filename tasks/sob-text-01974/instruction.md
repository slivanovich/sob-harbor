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
Christy Cabanne: William Christy Cabanne (April 16, 1888 – October 15, 1950) was an American film director, screenwriter and silent film actor.

Scattergood Pulls the Strings: Scattergood Pulls the Strings is a 1941 American comedy film directed by Christy Cabanne and written by Christy Cabanne and Bernard Schubert.  It is the sequel to the 1941 film "Scattergood Baines".  The film stars Guy Kibbee, Bobs Watson, Susan Peters, James Corner, Emma Dunn, Dink Trout and Monte Blue.  The film was released on May 23, 1941, by RKO Pictures.

The Great Secret (serial): The Great Secret is a 1917 silent film adventure serial directed by Christy Cabanne and starring Francis X. Bushman and Beverly Bayne.  It was produced independently by Louis B. Mayer and released through Metro Pictures.  Mayer's first production credit.

Monte Carlo (1926 film): Monte Carlo is a 1926 romantic comedy silent film directed by Christy Cabanne and starring Lew Cody.  It was produced by and distributed through MGM.

David Howard (director): David Howard (October 6, 1896 – December 21, 1941) was an American film director.  He directed 46 films between 1930 and 1941.  He was born as David Paget Davis III in Philadelphia, Pennsylvania and died in Los Angeles, California.

The Sixth Commandment: The Sixth Commandment is a lost 1924 silent film drama directed by Christy Cabanne and starring William Faversham.

The Slacker: The Slacker is a 1917 silent film drama directed by Christy Cabanne and starring Emily Stevens.  It was produced and distributed by Metro Pictures.

The Lamb (1915 film): The Lamb is a 1915 American silent adventure comedy/Western film featuring Douglas Fairbanks in his first starring role.  Directed by W. Christy Cabanne, the film is based on the popular 1913 Broadway play "The New Henrietta", in which Fairbanks co-starred with William H. Crane, Amelia Bingham and a very young Patricia Collinge.  D. W. Griffith, writing under the pseudonym Granville Barker, along with director Christy Cabanne, essentially expanded the play beyond the plush nouveau riche apartment setting of the play, and provided a western element to the story.  This would give Fairbanks a chance to show his physical prowess cinematically and loosen the play from what would be stage bound constraints.  Griffith also altered characters; Fairbanks' character's name is changed to Gerald, with his parent being his mother (Kate Toncray), whereas in the play his character was named Nick with his parent being his father played by Crane.

Annapolis (1928 film): Annapolis is a 1928 silent film drama directed by Christy Cabanne.  It was released with Photophone sound and effects.  It stars Johnny Mack Brown, Jeanette Loff and Hugh Allan.

National Red Cross Pageant: National Red Cross Pageant (1917) is an all-star revue silent film, now considered a lost film, directed by Christy Cabanne.

Question: Who was a silent film actor in addition to being a director, Christy Cabanne or David Howard?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the individual who was a silent film actor and director."
    },
    "roles": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of professional roles held by the individual."
    },
    "is_silent_film_actor": {
      "type": "boolean",
      "description": "Indicates if the individual was a silent film actor."
    },
    "is_director": {
      "type": "boolean",
      "description": "Indicates if the individual was a director."
    }
  },
  "required": [
    "person_name",
    "roles",
    "is_silent_film_actor",
    "is_director"
  ],
  "additionalProperties": false
}
