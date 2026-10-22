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
Boy Howdy: Boy Howdy was an American country music band.  It was founded in 1990 in Los Angeles, California, United States by Jeffrey Steele (lead vocals, bass guitar), Hugh Wright (drums), and brothers Cary (guitar, mandolin, vocals) and Larry Park (guitar, fiddle, vocals).  Between 1992 and 1995, the band recorded two albums (1992's "Welcome to Howdywood" and 1995's "Born That Way") and an extended play (1994's "She'd Give Anything"), all on the Curb Records label.  In that same time span, Boy Howdy charted seven singles on the "Billboard" Hot Country Singles & Tracks (now Hot Country Songs) charts, including the Top Ten hits "She'd Give Anything" and "They Don't Make 'Em Like That Anymore."  After Boy Howdy disbanded in 1996, frontman Jeffrey Steele embarked on a solo career, recording several solo albums, in addition to writing more than sixty hit singles for other country acts.

Frank Iero: Frank Anthony Iero, Jr. (born October 31, 1981) is an American musician who was the rhythm guitarist and backup vocalist of the rock band My Chemical Romance and post-hardcore band Leathermouth.  He has a solo punk rock project titled Frank Iero and the Patience.  He released an album under the previous name of frnkiero andthe cellabration titled "Stomachaches" which was released on August 26, 2014.  The first single off the album, called "Weighted", premiered on BBC Radio One on July 8, 2014.

Craig Wiseman: Craig Michael Wiseman is an American country music songwriter.  He has been writing since the late 1980s, and his songs have been recorded by Tim McGraw, Kenny Chesney, Dolly Parton, Blake Shelton, and numerous other acts.  He has written twenty-six #1 songs on the "Billboard" Hot Country Songs music charts, and has won a number of industry awards.  In 2009 he was named "Songwriter of the Decade" by the Nashville Songwriters Association International, and in 2015, he was inducted into the Nashville Songwriters Hall of Fame.

Frank Iero and the Patience: Frank Iero and the Patience is an American rock band from Belleville, New Jersey.  Their debut album, "Stomachaches", was released on August 25, 2014.  Their second album "Parachutes" was released on October 27, 2016 with the promotional singles "I'm A Mess", "Remedy", and "Oceans".  Their current lineup consists of Frank Iero, Evan Nestor, Matt Olsson, and Alex Grippo.  Steve Evetts is credited with writing and recording the bass tracks on "Parachutes".

My Chemical Romance: My Chemical Romance (often abbreviated as MCR) was an American rock band from Newark, New Jersey, active from 2001 to 2013.  The band's best-known lineup consisted of lead vocalist Gerard Way, guitarists Ray Toro and Frank Iero, bassist Mikey Way and drummer Bob Bryar.  Founded by Gerard, Mikey, Toro, Matt Pelissier, and later joined by Iero, the band signed to Eyeball Records and released their debut album "I Brought You My Bullets, You Brought Me Your Love" in 2002.  They signed with Reprise Records the next year and released their major label debut "Three Cheers for Sweet Revenge" in 2004.  Shortly after the album's release, Pelissier was replaced by Bob Bryar.  A commercial success, the album was awarded platinum status over a year later.

Sonny Throckmorton: James Fron "Sonny" Throckmorton (born April 2, 1941 in Carlsbad, New Mexico) is an American country music singer and songwriter.  Known primarily for his songwriting, Throckmorton has had more than 1,000 of his songs recorded by various country singers.  He has also had minor success as a recording artist, having released two major-label albums: "The Last Cheater's Waltz" in 1978 on Mercury Records and "Southern Train" in 1986 on Warner Bros.  Records.  Throckmorton is a member of the Nashville Songwriters' Hall of Fame, and has been awarded Songwriter of the Year by both Broadcast Music Incorporated and the Nashville Songwriters Association International.

Jeffrey Steele: Jeffrey LeVasseur (born August 27, 1961) is an American country music singer and songwriter, more commonly known by the name Jeffrey Steele.  Along with recording his own material, Steele has become a prolific Nashville songwriter, having co-written more than sixty hit songs for such artists as Montgomery Gentry, Tim McGraw, Faith Hill, LeAnn Rimes, Rascal Flatts, Billy Ray Cyrus, and others.

Nashville Songwriters Foundation: The Nashville Songwriters Foundation is a non-profit organization foundation for the Nashville music community.  Songwriters are inducted into the Nashville Songwriters Hall of Fame each year and the foundation's purpose is to "educate, archive, and celebrate the contributions of the members of the Nashville Songwriters Hall of Fame to the world of music."

List of songs recorded by My Chemical Romance: The following is a list of recorded songs by the American alternative rock/punk band My Chemical Romance.  A song titled "Hell Hath No Fury" was recorded for The Man with the Iron Fists but was never released.  An instrumental of the track credited to Gerard Way, Mikey Way, Frank Iero, Ray Toro and James Dewees appears in the movie.

Nashville Songwriters Hall of Fame: The Nashville Songwriters Hall of Fame was established in 1970 by the Nashville Songwriters Foundation, Inc. in Nashville, Tennessee, United States.  A non-profit organization, its objective is to honor and preserve the songwriting legacy that is uniquely associated with the music community in the city of Nashville.  The Foundation's stated purpose is to educate, archive, and celebrate the contributions of the members of the Nashville Songwriters Hall of Fame to the world of music.

Question: Did Jeffrey Steele and Frank Iero both become Nashville songwriters?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_asked": {
      "type": "string",
      "description": "The original question that was asked."
    },
    "answer": {
      "type": "boolean",
      "description": "True if both individuals became Nashville songwriters, false otherwise."
    },
    "individuals_evaluated": {
      "type": "array",
      "description": "Details for each individual mentioned in the question regarding their status as a Nashville songwriter.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the individual."
          },
          "is_nashville_songwriter": {
            "type": "boolean",
            "description": "True if the individual is identified as a Nashville songwriter in the context, false otherwise."
          },
          "reasoning": {
            "type": "string",
            "description": "Explanation based on the context for whether the individual is a Nashville songwriter."
          }
        },
        "required": [
          "name",
          "is_nashville_songwriter",
          "reasoning"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "question_asked",
    "answer",
    "individuals_evaluated"
  ],
  "additionalProperties": false
}
