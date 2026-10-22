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
I Stand Alone (Godsmack song): "I Stand Alone" is a song by the American rock band Godsmack.  It served as a single from the "Scorpion King" soundtrack on March 5, 2002.  It would reappear on Godsmack's third studio album, "Faceless", the following year.  It won a 2002 Metal Edge Readers' Choice Award for "Song of the Year From a Movie Soundtrack."

Hometown Life: Hometown Life is the second solo studio album by American rock musician Sully Erna, released on September 30, 2016.

Hollow (Godsmack song): "Hollow" is an acoustic song by the heavy metal band Godsmack from their fourth studio album, "IV".  Frontman Sully Erna and Lisa Guyer are on the song vocals.  "Hollow" is the only acoustic song that appeared in the album, and Erna has played it frequently on his solo tour.

Godsmack discography: Godsmack is an American alternative metal band founded in 1995 by singer Sully Erna and bassist Robbie Merrill.  The band has released six studio albums, one EP, one compilation, three video albums, and twenty-three singles.  Erna and Merrill recruited local friend and guitarist Lee Richards and drummer Tommy Stewart to complete the band's lineup.  In 1996, Tony Rombola replaced Richards, as the band's guitarist.  In 1998, Godsmack released their self-titled debut album, a remastered version of the "All Wound Up" demo.  The album was distributed by Universal/Republic Records and shipped four million copies in the United States.  In 2001, the band contributed the track "Why" to the Any Given Sunday soundtrack.  After two years of touring, the band released "Awake".  Although the album was a commercial success, it failed to match the sales of "Godsmack".  In 2002, Stewart left the band due to personal differences, and was replaced by Shannon Larkin.

Godsmack: Godsmack is an American rock band from Lawrence, Massachusetts, formed in 1995.  The band is composed of founder, frontman and songwriter Sully Erna, guitarist Tony Rombola, bassist Robbie Merrill, and drummer Shannon Larkin.  Since its formation, Godsmack has released six studio albums, one EP ("The Other Side"), four DVDs, one compilation album ("Good Times, Bad Times... Ten Years of Godsmack"), and one live album ("Live and Inspired").

Someone in London: "Someone in London" is a song by the rock band Godsmack from their self-titled debut album and this is an instrumental interlude.  It's the only music on the album that lead singer Sully Erna had no part in writing.  It was written by guitarist Tony Rombola.

Whatever (Godsmack song): "Whatever" is the first single by the American rock band Godsmack.  Featured on the band's self-titled album, "Whatever" is one of Godsmack's most famous songs.

Tony Rombola: Tony Rombola (born November 24, 1964) is an American musician who has been the lead guitarist and backing vocalist for the Boston-based Hard Rock band Godsmack since the mid-1990s.  Tony Rombola has been cited as 'an extraodinaire' in the guitar world, by Guitar World magazine, and is cited to be the only guitarist to keep an 'original soloing style' during the nu metal period, earning him the respect of the guitar industry.  Rombola is also a guitarist for the side-project band Another Animal, formed at the beginning of 2007, the band released their self-titled debut album in October 2007, and played shows, whilst frontman Sully Erna did a small solo tour.

Sully Erna: Salvatore Paul "Sully" Erna Jr. (born February 7, 1968) is the American vocalist and guitarist for the American hard rock band Godsmack.  He is also a harmonica player, percussionist and pianist, performing these on albums and at live shows.  He was ranked 47th in the Top 100 Heavy Metal Vocalists by "Hit Parader".

Sick of Life: "Sick of Life" is a song by the rock band Godsmack.  It was released on the band's second studio album "Awake".  The song is best known for its use in the United States Navy's "Accelerate Your Life" commercials, following a similar use of the album's title track.  "Sick of Life" was written during Godsmack's tour supporting their self-titled album.

Question: What American vocalist and guitarist for the band Godsmack had the solo album Hometown Life?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "musician_name": {
      "type": "string",
      "description": "The name of the American vocalist and guitarist."
    },
    "band_name": {
      "type": "string",
      "description": "The name of the band the musician is associated with."
    },
    "musician_roles": {
      "type": "array",
      "description": "The roles of the musician within the band.",
      "items": {
        "type": "string"
      }
    },
    "solo_album_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the solo album."
        },
        "release_date": {
          "type": "string",
          "description": "The release date of the solo album."
        }
      },
      "required": [
        "title",
        "release_date"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "musician_name",
    "band_name",
    "musician_roles",
    "solo_album_details"
  ],
  "additionalProperties": false
}
