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
Live World Tour: Live World Tour was the fourth headlining World tour by American boy band, Big Time Rush.  The tour was in support of Big Time Rush's third studio album "24/Seven" released in 2013.  The tour began on February 7, 2014 in Grand Prairie Texas.  Ticketing presales for the shows started on December 10, 2013.

Song 2: "Song 2" (sometimes mistakenly titled as "Woo Hoo") is a song by English rock band Blur, the second track from their 1997 eponymous fifth studio album.  The hook features Damon Albarn yelling "woo-hoo!"  as the distorted bass comes in.  Released in April 1997, "Song 2" reached number two in the UK Singles Chart, number four on the Australian ARIA Charts, and number six on US "Billboard" Alternative Songs (previously called "Billboard" Modern Rock Tracks).

Big Time Movie: Big Time Movie is a television film adaptation based on the Nickelodeon television series, "Big Time Rush" and the songs of The Beatles, which aired March 10, 2012 in the United States.  It features the members of Big Time Rush (a.k.a. the TV show and the band members) visiting London for their world tour, where they also have to save the world.

Big Time Rush in Concert: Big Time Rush in Concert was the debut tour by American boy band, Big Time Rush.  Predominately visiting North America, the tour supports the band's first studio album, "BTR".  The majority of the tour performed at several radio festivals, state fairs and amusement parks.  The band also played shows in England and Germany.  The trek began in April 2011, ending December 2011.

Windows Down: "Windows Down" is a song by American boy band Big Time Rush from the re-release of their second studio album "Elevate".  The song was released on June 25, 2012.  The song's hook is sampled from "Song 2" by English rock band Blur.

Big Time Movie Soundtrack: Big Time Movie Soundtrack is the second EP by pop group Big Time Rush.  The EP is the soundtrack of the television film "Big Time Movie", which is based on the Nickelodeon series "Big Time Rush".  It was released on March 6, 2012.

Think Tank (Blur album): Think Tank is the seventh studio album by the English rock band Blur, released in May 2003.  Jettisoning the Britpop sound of Blur's early career as well as the lo-fi indie rock of "Blur" (1997), "Think Tank" continued the jam-based studio constructions of the group's previous album, "13" (1999).  The album expanded on the use of sampled rhythm loops and brooding, heavy electronic sounds.  There are also heavy influences from dance music, hip hop, dub, jazz, and African music, an indication of songwriter Damon Albarn's expanding musical interests.

Logan Henderson: Logan Phillip Henderson (born September 14, 1989) is an American actor and singer.  He is best known for his role as Logan Mitchell on the Nickelodeon series, "Big Time Rush", as well as being a former member of the Big Time Rush band itself.  He, along with the band, have won and been nominated for multiple awards over the past few years.

Big Time Rush (band): Big Time Rush (also known as BTR) was an American boy band pop group formed in 2009.  The group consisted of Kendall Schmidt, James Maslow, Logan Henderson, and Carlos Pena, Jr. The group starred in Nickelodeon's television series "Big Time Rush" and signed to a record deal with Nick Records simultaneously with the television series, and then the group was eventually signed to Columbia Records.  The show ran from November 28, 2009 to July 25, 2013.  The pilot episode featured the group's first promotional single, "Big Time Rush".  They have released three studio albums which all achieved success.  The band stopped performing in 2014.

Summer Break Tour: The Summer Break Tour was a headlining concert tour by American pop boy band, Big Time Rush that featured American pop artist, Victoria Justice.  This was Big Time Rush's third consecutive headlining tour, and Justice's second overall tour.  The tour supported Big Time Rush's third studio album "24/Seven" and Justice's music from the television show "Victorious".  The tour played 40 shows in North America.

Question: Big Time Rush released a song called Windows Down, where the song's hook is sampled from a song by the English rock band Blur, which was released when?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "sampling_song": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the song that samples another song."
        },
        "artist": {
          "type": "string",
          "description": "The artist of the song that samples another song."
        },
        "release_date": {
          "type": "string",
          "description": "The release date of the sampling song."
        }
      },
      "required": [
        "title",
        "artist",
        "release_date"
      ],
      "additionalProperties": false
    },
    "sampled_song": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the song that was sampled."
        },
        "artist": {
          "type": "string",
          "description": "The artist of the song that was sampled."
        },
        "artist_origin": {
          "type": "string",
          "description": "The country of origin of the artist of the sampled song."
        },
        "release_date": {
          "type": "string",
          "description": "The release date of the sampled song."
        }
      },
      "required": [
        "title",
        "artist",
        "artist_origin",
        "release_date"
      ],
      "additionalProperties": false
    },
    "sampling_detail": {
      "type": "string",
      "description": "Specific part of the song that was sampled."
    }
  },
  "required": [
    "sampling_song",
    "sampled_song",
    "sampling_detail"
  ],
  "additionalProperties": false
}
