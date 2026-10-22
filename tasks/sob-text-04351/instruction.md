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
Shout Out to My Ex: "Shout Out to My Ex" is a song by British girl group Little Mix.  It is the first single from their fourth studio album "Glory Days" (2016) and premiered on "The X Factor" live shows on 16 October 2016, becoming the band's fourth number-one single in the United Kingdom.  The track was written by Edvard Førre Erfjord, Henrik Michelsen, Camille Purcell, Iain James and Little Mix, with production credits from Erfjord and Michelsen under their production monikers, Electric.

Word of Mouth (The Wanted album): Word of Mouth is the third studio album by English-Irish boy band The Wanted.  The album was released worldwide via Island Records on 4 November 2013.  The album was preceded by the release of six singles: "Chasing the Sun", "I Found You", "Walks Like Rihanna", "We Own the Night", "Show Me Love (America)" and "Glow in the Dark", the latter of which was released two weeks prior to the album.

Black Magic (song): "Black Magic" is a song by British girl group Little Mix.  It was written by Camille Purcell, Ed Drewett, Edvard Forre Erfjord, and Henrik Michelsen.  The Norwegian production duo Electric, who previously worked on the group's second studio album "Salute" (2013), produced the single with Matt Rad, who is additional producer.  It was released as the lead single from their third studio album, "Get Weird" on 21 May 2015.  "Black Magic" received critical acclaim from critics, who praised its upbeat and catchy sound and compared it to songs from their debut album, "DNA" (2012).

Two Strong Hearts: "Two Strong Hearts" is a song written by Andy Hill, Bruce Woolley.  Australian singer John Farnham recorded the song and released it as the second single from his album "Age of Reason" released in 1988.

No More Sad Songs: "No More Sad Songs" is a song by British girl group Little Mix from the group's fourth studio album, "Glory Days" (2016).  The song was written by Emily Warren, Edvard Førre Erfjord, Henrik Michelsen and Tash Phillips; produced by Electric and Joe Kearns.  A remix version, featuring newly recorded vocals from American rapper Machine Gun Kelly, was released as the third single from the album on 3 March 2017, through Syco Music.

Wasted Light: "Wasted Light" is a song released from Irish singer/songwriter Ronan Keating's ninth solo album "Fires".  The song was written by Edvard Førre Erfjord, Henrik Barman Michelsen and Gary Go.  It was released as promotional single.

Walks Like Rihanna: "Walks Like Rihanna" is a song by the British-Irish boy band The Wanted.  It was released in Australia on 10 May 2013, and in the United Kingdom and Ireland on 23 June 2013, as the third single from their third studio album "Word of Mouth" (2013).  The song was written by Andy Hill, Henrik Michelsen, and Edvard Førre Erfjord, and it was produced by Dr. Luke and Cirkut, with additional production by Michelsen and Erfjord under their stage name Electric.

Let in the Sun: "Let in the Sun" is a song by British pop group Take That.  It was released through Polydor Records on 2 March 2015 as the second single from their seventh studio album, "III" (2014).  The song was written by Take That, Edvard Førre Erfjord, Gary Go, Cass Lowe, and Henrik Barman Michelsen, and produced by Stuart Price and features Gary Barlow on lead vocal.

Electric (music producers): Electric is a Norwegian songwriting and production duo, composed of Henrik Barman Michelsen and Edvard Førre Erfjord.  Perhaps best known for their work with Little Mix on their #1 UK hits Black Magic and Shout Out to My Ex, the latter of which won Single of the Year at the 2017 Brit Awards, they have worked with artists such as Olly Murs, Machine Gun Kelly, Hailee Steinfeld, The Wanted, Cheryl Cole, and Fifth Harmony.

In the End (Stefanie Heinzmann song): "In the End" is a song by Swiss recording artist Stefanie Heinzmann.  It was written by Heinzmann along with Edvard Førre Erfjord, Henrik Barman Michelsen, and Sam Romans for her fourth studio album "Chance of Rain" (2015), with production helmed by Erfjord and Michelsen under their production moniker Electric.  Selected as the album's first single, "In the End" peaked at number nine on the Swiss Albums Chart, becoming Heinzmann's third domestic top ten hit, and reached the top thirty in Germany.

Question: "The Wanted" song written by Andy Hill, Henrik Michelsen, and Edvard Førre Erfjord was released on an album by what company?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_name": {
      "type": "string",
      "description": "The name of the band that performed the song."
    },
    "song_title": {
      "type": "string",
      "description": "The title of the song."
    },
    "song_writers": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of the writers of the song."
    },
    "album_title": {
      "type": "string",
      "description": "The title of the album the song is from."
    },
    "record_company": {
      "type": "string",
      "description": "The record company that released the album."
    }
  },
  "required": [
    "band_name",
    "song_title",
    "song_writers",
    "album_title",
    "record_company"
  ],
  "additionalProperties": false
}
