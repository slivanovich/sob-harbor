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
List of Austin City Limits performers: This list of "Austin City Limits" performers is a list of musicians who have appeared on the American PBS television music program "Austin City Limits".  Also listed are years in which they appeared.  This list does not include performers who otherwise may have appeared at the annual Austin City Limits Music Festival, but who did not appear on the PBS television program.

The Dreadful Lemon Sky: The Dreadful Lemon Sky (1975) is the sixteenth novel in the Travis McGee series by John D. MacDonald.  It is the 87th novel in The Top 100 Crime Novels of All Time as compiled by the Mystery Writers of America (it is not included in the U.K. version of the list).

Lemon Sky: Lemon Sky is a play by Lanford Wilson which ran Off-Broadway in 1970.

Soul Survivors (band): The Soul Survivors are an American, Philadelphia-based, Soul Music and R&B group, founded by New York natives Richie and Charlie Ingui along with Kenny Jeremiah.  The Soul Survivors are known for their 1967 hit single "Expressway to Your Heart", which was the first hit by Philadelphia soul record producers and songwriters Kenny Gamble and Leon Huff.  The Soul Survivors are still performing and recording new music and covers, most recently working with David Uosikkenen of the The Hooters and his project "In The Pocket" which is paying tribute to the vast catalog of music created in Philadelphia.

Casey Affleck: Caleb Casey McGuire Affleck-Boldt (born August 12, 1975) is an American actor and director.  He began his career as a child actor, appearing in the PBS television movie "Lemon Sky" (1988) and the ABC miniseries "The Kennedys of Massachusetts" (1990).  He later appeared in three Gus Van Sant films – "To Die For" (1995), "Good Will Hunting" (1997), and "Gerry" (2002) – and in Steven Soderbergh's comedy heist trilogy "Ocean's Eleven" (2001), "Ocean's Twelve" (2004) and "Ocean's Thirteen" (2007).  His first leading role was in Steve Buscemi's independent comedy-drama "Lonesome Jim" (2006).

Sky Movies (New Zealand): Sky Movies is a group of subscription television movie channels in New Zealand operated by Sky Network Television.  Sky Movies was started in 1990 as one of the original channels on the Sky UHF Service.  Sky Movies has progressed from the original channel (now known as Sky Movies Premiere) in 1990 to six separate movie channels screening special interest movies, today.  All Sky Movies channels are simulcasted in high definition.

Neal Du Brock: Neal Du Brock directed the world-premieres of many important plays including Edward Albee's Box (play) and Lanford Wilson's Lemon Sky (starring Christopher Walken and Charles Durning).

Jill Eikenberry: Jill Susan Eikenberry (born January 21, 1947) is an American film, stage, and television actress.  She is known for her role as lawyer Ann Kelsey on the NBC drama "L.A. Law" (1986–94), for which she is a five-time Emmy Award and four-time Golden Globe Award nominee, winning the Golden Globe for Best Actress in a Drama Series in 1989.  She received an Obie Award in 1986 for the Off-Broadway plays "Lemon Sky" and "Life Under Water", and was nominated for a 2011 Drama Desk Award for the Off-Broadway musical "The Kid".  Her film appearances include "Hide in Plain Sight" (1980), "Arthur" (1981) and "The Manhattan Project" (1986).

Soul Survivors: Soul Survivors is a 2001 psychological thriller film starring Melissa Sagemiller as college student Cassie, whose boyfriend Sean (Casey Affleck) dies in a car accident that results from her driving after a night of partying.  The accident leaves Cassie racked with guilt and emotionally vulnerable to the point that she begins hallucinating strange visions and waking-dreams, even though Cassie's friends Annabel (Eliza Dushku) and Matt (Wes Bentley), as well as a local priest called Father Jude (Luke Wilson), all attempt to assist her in coping with the loss.

Melissa Sagemiller: Melissa Sagemiller (born June 1, 1974) is an American television and film actress.  She is known for her performances in films "Get Over It" (2001), "Soul Survivors" (2001), "Sorority Boys" (2002), "The Clearing" (2004), "The Guardian" (2006) and "Mr. Woodcock" (2007).  Sagemiller also starred in television dramas "Sleeper Cell" (2005–06), and "Raising the Bar" (2008–09), and from 2010 to 2011 had the recurring role as A.D.A. Gillian Hardwicke in the "".

Question: Which actor from the movie "Soul Survivors" started his career in the PBS television movie "Lemon Sky"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor."
    },
    "film_appearances": {
      "type": "array",
      "description": "A list of films or television movies the actor appeared in.",
      "items": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the film or television movie."
          },
          "type": {
            "type": "string",
            "description": "The type of production (e.g., 'film', 'PBS television movie')."
          },
          "year": {
            "type": "integer",
            "description": "The year of the production's release or broadcast."
          }
        },
        "required": [
          "title",
          "type",
          "year"
        ],
        "additionalProperties": false
      }
    },
    "common_roles_identified": {
      "type": "boolean",
      "description": "Indicates if an actor common to both productions was identified."
    }
  },
  "required": [
    "actor_name",
    "film_appearances",
    "common_roles_identified"
  ],
  "additionalProperties": false
}
