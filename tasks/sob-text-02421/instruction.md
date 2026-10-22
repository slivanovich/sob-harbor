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
Something's Gotta Give (album): Something's Gotta Give is the fifth full-length studio album by New York hardcore band, Agnostic Front.  It was released in June 1998 on Epitaph Records and follows 1995's "Raw Unleashed" compilation album.  It is actually the first studio album since 1992's "One Voice".  The album was co-produced by Billy Milano, the frontman of crossover thrash bands S.O.D. and M.O.D..  It marks a return to a more hardcore punk style of sound than the thrash metal inspired music of "One Voice".  Backing vocals, amongst others, were provided by Tim Armstrong and Lars Frederiksen of Rancid, and Jimmy Gestapo of Murphy's Law.

Something's Gotta Give (LeAnn Rimes song): "Something's Gotta Give" is a song written by Craig Wiseman and Tony Mullins, and recorded by American country music artist LeAnn Rimes.  It was released in December 2005 as the third single from her seventh studio album "This Woman".  The song reached a peak of #2 on the Hot Country Songs chart in mid-2006, becoming Rimes' highest-peaking country single since the Number One "One Way Ticket (Because I Can)" in 1996-1997.  The #1 spot was held by "Summertime" by Kenny Chesney.  The song also won ASCAP awards for its writers.

Future Hearts: Future Hearts is the sixth studio album by American rock band All Time Low, released April 3, 2015 by Hopeless Records as the follow-up to "Don't Panic" (2012).  The first single, "Something's Gotta Give" premiered on BBC Radio 1 on January 12, 2015.  Every physical copy contains five of twenty collectible "polaroids".  Deluxe editions of "Future Hearts" feature bonus songs, expanded artwork and an alternate cover.  This is the last All Time Low album to be released on Hopeless Records.

Roxanne Beckford: Roxanne Beckford (born November 17, 1969), a.k.a. Roxanne Beckford-Hoge, is an American actress who was born and raised in Jamaica.  She has acted in numerous television series and played small roles in movies, including "Bewitched" (2005) "Something's Gotta Give" (2003), and "Father of the Bride Part II" (1995).  Beckford began her career in acting as a child starring in television commercials in Jamaica.  Her husband, Bob Hoge, is also an actor.  They have four children, including twins who were featured on episode 1 of TLC's "Bringing Home Baby" in 2005.

Something's Gotta Give (The John Butler Trio song): Something's Gotta Give (The John Butler Trio song)

James S. Levine: James Scott Levine (born 1974) is a composer and member of Remote Control Productions.  He has won seven BMI awards and seven ASCAP awards.  His credits include the films "Running with Scissors", "Delta Farce", and "The Weather Man", and the television shows "Nip/Tuck", "Glee", "The Closer", "Rizzoli & Isles", and "American Horror Story".  He has also provided additional music for films such as "Madagascar", "Pearl Harbor", and "Something's Gotta Give".

Fred Astaire: Fred Astaire (born Frederick Austerlitz; May 10, 1899 – June 22, 1987) was an American dancer, singer, actor, choreographer and television presenter.

Something's Gotta Give: Something's Gotta Give or Something's Got to Give may refer to:

Something's Gotta Give (film): Something's Gotta Give is a 2003 American romantic comedy film written, produced and directed by Nancy Meyers.  It stars Jack Nicholson and Diane Keaton as a successful 60-something and 50-something, who find love for each other in later life, despite being complete opposites.  Keanu Reeves and Amanda Peet co-star, with Frances McDormand, Paul Michael Glaser, Jon Favreau, and KaDee Strickland playing key supporting roles.

Something's Gotta Give (Johnny Mercer song): "Something's Gotta Give" is a popular song with words and music by Johnny Mercer in 1954.  It was published in 1955.  It was written for and first performed by Fred Astaire in the 1955 musical film "Daddy Long Legs", and was nominated for an Academy Award in 1955 as Best Original Song, losing to Love is a Many Splendored Thing.

Question: Something's Gotta Give was first performed by an actor of what heritage?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_title": {
      "type": "string",
      "description": "The title of the song."
    },
    "first_performer": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the artist who first performed the song."
        },
        "heritage": {
          "type": "string",
          "description": "The heritage of the first performer."
        },
        "roles": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "The professional roles of the performer."
        }
      },
      "required": [
        "name",
        "heritage"
      ],
      "additionalProperties": false
    },
    "performance_context": {
      "type": "object",
      "properties": {
        "media_type": {
          "type": "string",
          "description": "The type of media in which the song was first performed."
        },
        "year": {
          "type": "integer",
          "description": "The year the song was first performed."
        }
      },
      "required": [
        "media_type",
        "year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "song_title",
    "first_performer",
    "performance_context"
  ],
  "additionalProperties": false
}
