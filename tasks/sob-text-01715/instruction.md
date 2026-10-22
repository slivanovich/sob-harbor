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
Victor Herbert Melodies, Vol. 1: Victor Herbert Melodies, Vol.  1 is a studio album featuring five 78 rpm phonograph records celebrating the music of Victor Herbert.  The recordings were made in December 1938 by Decca Records, who were probably aware that a film called "The Great Victor Herbert" was being made by Paramount Pictures.  Victor Young and His Orchestra provided the musical accompaniment to all of the tracks.

Sweethearts (1938 film): Sweethearts is a 1938 Technicolor musical romance directed by W.S. Van Dyke, starring Jeanette MacDonald and Nelson Eddy.  The screenplay, by Dorothy Parker and Alan Campbell, uses the “play within a play” device: a contemporary Broadway production of the 1913 Victor Herbert operetta is the setting for another pair of sweethearts, the stars of the show.  This was the first color film for Nelson or Jeanette (as well as MGM's first three strip Technicolor feature).

The Dream Girl (operetta): The Dream Girl is an operetta in three acts with music by Victor Herbert and book by Rida Johnson Young (who also wrote the lyrics) and Harold R. Atteridge.  Based on the 1906 play "The Road to Yesterday", by Beulah Marie Dix and Evelyn Greenleaf Sutherland, its satiric story concerns reincarnation.  Additional music was written by Sigmund Romberg.  The piece was Victor Herbert's last musical composition, and the work was produced posthumously on Broadway in 1924.

Victor Herbert Melodies, Vol. 2: Victor Herbert Melodies, Vol.  2 is a compilation album of phonograph records celebrating the music of Victor Herbert.  Most of the recordings were made in December 1938 by Decca Records, who were probably aware that a film called The Great Victor Herbert was being made by Paramount Pictures.  An album titled Victor Herbert Melodies, Vol.  1 had been issued earlier in 1939.  Victor Young and His Concert Orchestra provided the musical accompaniment to all of the tracks.

Babes in Toyland (operetta): Babes in Toyland is an operetta composed by Victor Herbert with a libretto by Glen MacDonough (1870–1924), which wove together various characters from Mother Goose nursery rhymes into a Christmas-themed musical extravaganza.  Following the extraordinary success of their stage musical "The Wizard of Oz", which was produced in New York beginning in January 1903, producer Fred R. Hamlin and director Julian P. Mitchell hoped to create more family musicals.  MacDonough had helped Mitchell with revisions to the "Oz" libretto by L. Frank Baum.  Mitchell and MacDonough persuaded Victor Herbert to join the production.  "Babes in Toyland" features some of Herbert's most famous songs – among them "Toyland", "March of the Toys", "Go To Sleep, Slumber Deep", and "I Can't Do the Sum".  The theme song "Toyland", and the most famous instrumental piece from the operetta, "March of the Toys", occasionally show up on Christmas compilations.

Victor Herbert (sculpture): Victor Herbert is an outdoor bronze portrait bust of Victor Herbert by Edmund Thomas Quinn, located in Central Park in Manhattan, New York.  The memorial sculpture, commissioned by the American Society of Composers, Authors, and Publishers (ASCAP), was unveiled by Herbert's daughter in 1927 at a dedication attended by Irving Berlin and Arthur Hammerstein.

Victor Herbert: Victor August Herbert (February 1, 1859 – May 26, 1924) was an Irish-born, German-raised American composer, cellist and conductor.  Although Herbert enjoyed important careers as a cello soloist and conductor, he is best known for composing many successful operettas that premiered on Broadway from the 1890s to World War I.  He was also prominent among the tin pan alley composers and was later a founder of the American Society of Composers, Authors, and Publishers (ASCAP).  A prolific composer, Herbert produced two operas, a cantata, 43 operettas, incidental music to 10 plays, 31 compositions for orchestra, nine band compositions, nine cello compositions, five violin compositions with piano or orchestra, 22 piano compositions and numerous songs, choral compositions and orchestrations of works by other composers, among other music.

Henry Blossom: Henry Martyn Blossom (May 10, 1866 – March 23, 1919) was a playwright and lyricist.  He was the lyricist for several Victor Herbert musicals, including his first Broadway musical project -"The Yankee Consul" (1904), "Mlle. Modiste" (1905), "The Red Mill" (1906), "Eileen" (1917), and "Kiss Me Again" (film version of "Mlle. Modeste", 1931).  He also wrote "When Uncle Sam is Ruler of the Sea" with Victor Herbert in 1916, "It's Not the Uniform That Makes the Man" with A. Baldwin Sloane in 1917 and "I Want to Go Back to the War" with Percival Knight (music was by Raymond Hubbell) in 1919.

Bing Crosby – Victor Herbert: Bing Crosby – Victor Herbert is a compilation album of phonograph records by Bing Crosby and Frances Langford of songs written by Victor Herbert.

The Great Victor Herbert: The Great Victor Herbert is a 1939 American musical film directed by Andrew L. Stone.  During production the movie was slated to be called The Gay Days of Victor Herbert.

Question: In the screenplay Sweethearts, Victor Herbert's play was was used. What type of performance was this?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film where the screenplay was used."
    },
    "screenplay_device_type": {
      "type": "string",
      "description": "The type of performance device used in the screenplay."
    },
    "screenplay_authors": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The authors of the screenplay."
    },
    "operetta_setting_year": {
      "type": "integer",
      "description": "The year of the Victor Herbert operetta that serves as the setting for the play within a play."
    }
  },
  "required": [
    "film_title",
    "screenplay_device_type",
    "screenplay_authors",
    "operetta_setting_year"
  ],
  "additionalProperties": false
}
