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
The Escorts (American band): The Escorts (later The Do's & Don'ts) are a 1950s and 1960s Rock and roll band from Iowa, United States.  The Iowa Rock 'N Roll Music Association's Hall of Fame inducted this band in the year that the Hall of Fame was started, 1997.  They were one of the first bands in Iowa to play Rock and Roll music, starting in 1959.  They released more 45 rpm records than any other Iowa band in the 1960s.  They performed in ballrooms all over Iowa and traveled out-of-state as well.  They are one of the few bands to perform for over 45 years.  See related article The Escorts / The Do's & The Don'ts (album).

Tehosekoitin: Tehosekoitin was a Finnish rock band formed in 1991.  The band made music with traditional rock 'n roll attitude.  Besides pure rock 'n roll, they also made some songs which were more like jazz, blues or tender ballads than actual rock.  Tehosekoitin was really popular in Finland.  The band toured after a successful decade in Suomi later under the new name Screamin' Stukas in Britain and Europe.  They translated all their lyrics into English.  The tour wasn't very successful.

Iowa Rock 'n' Roll Hall of Fame: The Iowa Rock ‘n’ Roll Hall of Fame is a museum located in Arnolds Park, Iowa and maintained by the non-profit Iowa Rock ‘n’ Roll Music Association (IRRMA).  The mission of IRRMA is to “retain and honor the legacy of rock ’n’ roll music and preserve the history of music in the state of Iowa.”

Jerry Haymes: Jerry Haymes, born August 30, 1940 in Vernon, Texas, raised in Clovis, New Mexico, has contributed to the body of rock 'n roll for over 50 years.  Even before graduating from Clovis High, Jerry was recording at the famed Norman Petty Studios, a foreshadow of his career to come.  Graduation from Clovis High School led Jerry to attend Abilene Christian University, Southern Methodist University, Midwest University and Kilgore College.  He also spent time studying at the London Conservatory of Music.  He was boyhood friends with Roy Orbison, who he worked with on a professional level.  This led Haymes to Sun Records where he was an original Sun Legends Musician and Singer (with Roy Orbison).  Over the years he has performed on many chart hits, and although some of his own records charted, the top spot eluded him.  Haymes is also a member of the Rock 'n Roll Hall of Fame and Texas Music Hall of Fame.

Back in the U.S.S.R.: "Back in the U.S.S.R." is a song by the Beatles.  It is credited to the songwriting partnership Lennon–McCartney, but written by Paul McCartney.  The song opens the 1968 double-disc album "The Beatles" (also known as the "White Album"), and then segues into "Dear Prudence".

It's Only Rock 'n Roll: It's Only Rock 'n Roll is the 12th British and 14th American studio album by The Rolling Stones, released in 1974.  It was the last Rolling Stones album for guitarist Mick Taylor and the songwriting and recording of the album's title track had a connection to Taylor's eventual replacement, Ronnie Wood.  The album also marked the 10th anniversary since the release of the band's debut album, "The Rolling Stones".  "It's Only Rock 'n Roll" has a firmer rock sound than the band's previous album, the more funk - and soul - inspired "Goats Head Soup".  "It's Only Rock 'n Roll" reached #1 in the US and #2 in the UK.

Rock 'n' Roll Music (album): Rock 'n' Roll Music is a compilation album by The Beatles that consists of previously released Beatles tracks.  The double album was issued on 7 June 1976 in the United States, on Capitol Records (catalogue number SKBO 11537), and on Parlophone (PCSP 719) in the United Kingdom, four days later.  The album is a combination of some notable Lennon–McCartney originals, such as "Drive My Car", "Revolution", "Back in the U.S.S.R." and "Get Back", George Harrison's "Taxman", and a dozen cover versions of songs written by significant rock and roll composers of the 1950s, including Chuck Berry, Little Richard, Carl Perkins and Larry Williams.  "Rock 'n' Roll Music" was the first Beatles album to include "I'm Down", which had previously only been available as the B-side of the "Help! " single.

I Hate Rock 'n' Roll: "I Hate Rock 'n' Roll" is a song by the Scottish alternative rock group The Jesus and Mary Chain.  It was the first single from the band's compilation album, "Hate Rock 'n' Roll".  It was released together with 3 other tracks by Blanco y Negro Records in June 1995 and reached #61 in the UK single charts.  This release was the last release for the band on this label.  The 10" format was numbered and limited to 5000 copies.  The reworked version of the track, which was dubbed as "I Love Rock 'n' Roll" was also included on the group's last album "Munki", released in 1998.

Just... Fabulous Rock 'n' Roll: Just... Fabulous Rock 'n' Roll is a studio album by Cliff Richard, released 11 November 2016.  The album continues the rock 'n' roll theme of his previous studio album "The Fabulous Rock 'n' Roll Songbook".  It comprises covers of 14 classic rock 'n' roll songs and one new song "It's Better to Dream".  It features Elvis Presley in duet with Richard in "Blue Suede Shoes" and Peter Frampton on guitar in "Dimples".  The album reached number 4 on the UK Albums Chart and has been certified Gold for sales over 100,000 in the UK.

Jive Time: Jive Time is a pinball machine released on April 23, 1970 and made by the Williams Manufacturing Company.  This table is nearly exactly the same as a pinball machine called "Rock 'n Roll" which was released on the same day as "Jive Time".  The only differences are that "Jive Time" has a replay feature and "Rock 'n Roll" has an Add a Ball feature.  The designer of the two tables is Norm Clark and the art of the two tables was made by Christian Marche.

Question: Back in the U.S.S.R is a song on a compilation album called Rock 'N Roll Music by what musical artist?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_title": {
      "type": "string",
      "description": "The title of the song."
    },
    "album_title": {
      "type": "string",
      "description": "The title of the album the song is featured on."
    },
    "album_type": {
      "type": "string",
      "description": "The type of album (e.g., compilation, studio)."
    },
    "musical_artist": {
      "type": "string",
      "description": "The musical artist who performed the song and released the album."
    },
    "song_writers": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The credited songwriters for the song."
    }
  },
  "required": [
    "song_title",
    "album_title",
    "album_type",
    "musical_artist",
    "song_writers"
  ],
  "additionalProperties": false
}
