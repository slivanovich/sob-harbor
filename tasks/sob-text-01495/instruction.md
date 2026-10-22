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
Kelly Watch the Stars: "Kelly Watch the Stars" (also written "Kelly, Watch the Stars!")  is a song by Air, from their debut studio album "Moon Safari".

Sexy Boy (Air song): "Sexy Boy" is a single by French band Air and was featured in the film "10 Things I Hate About You" as well as the British television series "Queer as Folk".

All I Need (Air song): "All I Need" is a song by French music group Air from their debut album "Moon Safari" (1998).  The song was written by group members Nicolas Godin and Jean-Benoît Dunckel, along with American singer Beth Hirsch, who provides vocals on the song.  Production of the song was handled by the former two.  The song was released as the third single from "Moon Safari" on 9 November 1998.

Air (French band) discography: The discography of French electronic music duo AIR consists of seven studio albums (including one collaborative album), one remix album, one soundtrack album, one mix album, two video albums, one extended play, twenty-two singles and sixteen music videos.  The band's first release was the 1995 single "Modular Mix", which peaked at number 177 in the United Kingdom.  Their debut extended play, "Premiers Symptômes", was released in July 1997; it peaked at number 12 in the UK and was certified silver by the British Phonographic Industry (BPI). " Moon Safari", AIR's debut studio album, was released in January 1998.  It peaked at number 21 in France and was certified gold by the Syndicat National de l'Édition Phonographique (SNEP).  "Moon Safari" reached the top ten in countries such as Ireland and the UK and produced three singles: "Sexy Boy", "Kelly Watch the Stars" and "All I Need".  All three singles reached the top 40 in the UK; "Sexy Boy" and "All I Need" reached the top 25 in Finland and the Netherlands respectively.

Beth Hirsch: Beth Hirsch (born October 18, 1967) is a singer-songwriter from Tampa, Florida.  Hirsch is best known for her collaboration with Air on their album "Moon Safari".  Her first solo album, "Early Days", was released in 2000, followed by "Titles & Idols" in 2001.  After a series of collaborations with artists including Pale 3, Jakatta, and D*Note, Hirsch released her third solo album "Wholehearted", in 2007.

Moon Safari: Moon Safari is the debut studio album by French electronic music duo Air, released on 16 January 1998.  On 14 April 2008, Virgin Records re-released "Moon Safari" to mark the album's tenth anniversary.  The limited edition album came with a bound book, a DVD documentary about the duo, and an extra CD with live performances and remixes.

Jessica Riddle: Jessica Riddle (born April 15, 1980, in Los Angeles, California) is an American singer-songwriter.  Riddle attained minor fame with the hit "Even Angels Fall" on her debut album "Key of a Minor", which was featured in the 1999 movie "10 Things I Hate about You" and on its soundtrack.

10 Things I Hate About You (TV series): 10 Things I Hate About You is an American television sitcom broadcast on ABC Family beginning in 2009.  Developed by Carter Covington, the show is a half-hour, single camera series based on "Ten Things I Hate About You".  It premiered on Tuesday, July 7, 2009 at 8 pm and brought in 1.60 million viewers, a record for a 30-minute comedy debut on the ABC Family network.

Blomljud: <nowiki>Blomljud</nowiki> is the second album release from the Swedish progressive rock band Moon Safari.  It is the band's first double album, containing 11 songs of various lengths.  It was released in 2008, three years after their debut album, "A Doorway to Summer".  It was released on the independent label Blomljud Records.

Brian Reitzell: Brian Reitzell (born December 24, 1965) is a musician, composer, record producer and music supervisor best known for his work on many film and TV soundtracks.  He is notable for working extensively with the American film director Sofia Coppola (The Virgin Suicides, Lost in Translation, Marie Antoinette, "The Bling Ring").  He was formerly the drummer for the LA punk band Redd Kross.  He has collaborated extensively with the French electronica duo Air, having performed drums on their albums "The Virgin Suicides" and "10 000 Hz Legend".  Reitzell also toured with the band on their "Moon Safari" tour in 1998 and again in 2000 and 2001.  In 2003 he was nominated for a BAFTA, along with Kevin Shields of My Bloody Valentine, for the score to Sofia Coppola's film "Lost in Translation".

Question: What song by AIR was on their debut album "Moon Safari" and was featured in the film "10 Things I Hate About You"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_title": {
      "type": "string",
      "description": "The title of the song."
    },
    "artist_name": {
      "type": "string",
      "description": "The name of the artist or band."
    },
    "album_details": {
      "type": "object",
      "properties": {
        "album_name": {
          "type": "string",
          "description": "The name of the album the song is from."
        },
        "is_debut_album": {
          "type": "boolean",
          "description": "True if the album is the artist's debut studio album."
        }
      },
      "required": [
        "album_name",
        "is_debut_album"
      ],
      "additionalProperties": false
    },
    "featured_in_media": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "media_type": {
            "type": "string",
            "enum": [
              "film",
              "television_series"
            ],
            "description": "The type of media the song was featured in."
          },
          "media_title": {
            "type": "string",
            "description": "The title of the film or television series."
          }
        },
        "required": [
          "media_type",
          "media_title"
        ],
        "additionalProperties": false
      },
      "description": "A list of films or television series the song was featured in."
    }
  },
  "required": [
    "song_title",
    "artist_name",
    "album_details",
    "featured_in_media"
  ],
  "additionalProperties": false
}
