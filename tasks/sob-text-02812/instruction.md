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
Fantasia 2000: Fantasia 2000 is a 1999 American animated film by Walt Disney Feature Animation and Walt Disney Pictures, and released by Buena Vista Pictures.  Produced by Roy E. Disney and Donald W. Ernst, it is the 38th Disney animated feature film and the sequel to "Fantasia" (1940).  Like its predecessor, "Fantasia 2000" consists of animated segments set to pieces of classical music.  Celebrities including Steve Martin, Itzhak Perlman, Quincy Jones, Bette Midler, James Earl Jones, Penn & Teller, and Angela Lansbury introduce each segment in live action scenes directed by Don Hahn.

Pixote Hunt: Pixote Hunt (or Maurice Hunt) is a director, artist, and animator.  He has been involved in films such as "The Black Cauldron" and "Fantasia 2000", and was most prolific in the 1980s and 1990s.

Aliki Theofilopoulos Grafft: Aliki Theofilopoulos Grafft (born June 14, 1972) is an Greek -American television writer, storyboard artist, and voice actress.  She is well known for her work on television series "Phineas and Ferb".  She began her career on Disney movies such as "Hercules", "Mulan", "Fantasia 2000" and many more.

Interstitial program: In television programming, an interstitial program (or wraparound program or wraparound segment) refers to a short program which is often shown between movies or other events, e.g. cast interviews after movies on premium channels.  The term can also refer to a narrative bridge between segments within a program, such as the live action introductions to the animated segments in the Disney films "Fantasia" and "Fantasia 2000", or the Simpson family's interludes during their annual "Treehouse of Horror" episodes.

The Incredibles: The Incredibles is a 2004 American computer-animated superhero film written and directed by Brad Bird, produced by Pixar Animation Studios, and released by Walt Disney Pictures.  The film follows a family of superheroes who are forced to hide their powers and live a quiet suburban life.  Mr. Incredible's desire to help people draws the entire family into a battle with Syndrome, a former fan who now plots to wipe out all superheroes with his killer robot.

Fantasia: Music Evolved: Fantasia: Music Evolved is a 2014 motion-controlled music rhythm game developed by Harmonix for the Xbox 360 and Xbox One with Kinect.  It is the interactive successor to Walt Disney's 1940 animated film "Fantasia" and its 1999 sequel "Fantasia 2000", both of which it is based upon.

Anthony DeRosa: Anthony "Tony" DeRosa is an american character animator, best known for his work at Walt Disney Animation Studios.  DeRosa has worked as a lead animator on several Disney animated features, including "The Lion King", "Pocahontas", "Hercules", "Fantasia 2000", "" and "The Princess and the Frog".  Outside of Disney, DeRosa has worked as an animator on films such as "", "Fat Albert", "Curious George" and "The Simpsons Movie", for which he received an Annie Award nomination.

Francis Glebas: Francis Glebas (born 1952) is a keynote speaker, writer, film director, storyboard artist, and teacher.  He worked in films such as "Aladdin", "The Lion King", "Pocahontas", "Hunchback", "Treasure Planet," "Fantasia 2000", "Piglet's Big Movie", "Space Chimps", "Rio" and "".

Irene Mecchi: Irene Mecchi is an American writer for television, movies, newspapers, and Broadway.  Originally from San Francisco, she started her work with Disney in March 1992, when she wrote "Recycle Rex", an animated short film which won the 1994 Environmental Media Award.  Irene has worked on Herb Caen's books, and is the co-screenwriter of Disney animated movies such as "The Lion King", "The Hunchback of Notre Dame", "Hercules", and "Fantasia 2000".  With co-author Roger Allers, she received a 1998 Tony nomination for writing the book for "The Lion King".  Irene wrote the teleplay for "Annie", which aired on ABC in 1999.

List of Disney's Fantasia characters: The following are fictional characters from Disney's 1940 film "Fantasia", its 1999 sequel "Fantasia 2000" and the video game "".  Characters in this list are sorted by the film and segment in which they appear.  The names of some characters including the original ones are never mentioned in the programs.

Question: What do Fantasia 2000 and The Incredibles have in common?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "common_entity_name": {
      "type": "string",
      "description": "The name of the entity that both films have in common."
    },
    "entity_role": {
      "type": "string",
      "description": "The role of the common entity in relation to the films (e.g., 'distributor', 'producer')."
    },
    "films_involved": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of the film titles being compared."
    }
  },
  "required": [
    "common_entity_name",
    "entity_role",
    "films_involved"
  ],
  "additionalProperties": false
}
