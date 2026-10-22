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
Fetty Wap (album): Fetty Wap is the eponymous debut studio album by American rapper Fetty Wap.  It was released on September 25, 2015, by RGF Productions, distributed by Because Music and 300 Entertainment.  The album features guest appearances from Remy Boyz, Monty and M80.  Both Monty and M80, who were members of the Remy Boyz, contributed as featured guest artists on the album.

The One (Tamar Braxton song): "The One" is a song by American R&B recording artist Tamar Braxton.  Written by Braxton, Yung Berg, Shaunice Lasha Jones, LaShawn Daniels, and its producer K.E. on the Track, the song contains samples from Juicy Fruit by Mtume.  The song also contains re-sung lyrics from The Notorious B.I.G.'s "Juicy", which also sampled Juicy Fruit.  It was released as the second single on May 7, 2013 from her second studio album "Love and War" (2013).

My Way (Fetty Wap song): "My Way" is the third single by American rapper Fetty Wap, featuring Remy Boyz's RGF Productions' member Monty, from Wap's self-titled debut album.  It peaked at number seven on the "Billboard" Hot 100.

Jimmy Choo (song): "Jimmy Choo" is a song by American rapper Fetty Wap for his upcoming album "King Zoo".  It was released on February 5, 2016 and was produced by K.E. on the Track.

Fetty Wap: Willie Maxwell II (born June 7, 1991) is an American rapper better known by his stage name Fetty Wap.  He rose to prominence after his debut single "Trap Queen", reached number two on the U.S. "Billboard" Hot 100 chart in May 2015.  This helped Fetty Wap secure a record deal with 300 Entertainment, a record label distributed by Atlantic Records.  He subsequently released two Top 10 singles in the U.S., "679" and "My Way".  Fetty Wap's eponymously titled debut album was released in September 2015 and reached number one on the U.S. "Billboard" 200 chart.

Wake Up (Fetty Wap song): "Wake Up" is a song by American hip hop recording artist Fetty Wap for his upcoming of the album King Zoo.  The song was released on April 20, 2016 by RGF Productions and 300 Entertainment.  The track was produced by Frenzy.  It was certified Gold by the RIAA on November 14, 2016.

Westside (Fetty Wap song): "Westside" is a song by American rapper Fetty Wap featuring Snoop Dogg for his upcoming of the album King Zoo.  The song was released on June 3, 2016 by RGF Productions and 300 Entertainment.  The track was produced by London on da Track.

Asking 4 It: "Asking 4 It" is a song by American singer and songwriter Gwen Stefani from her third studio album, "This Is What the Truth Feels Like" (2016).  The song features guest vocals from American rapper Fetty Wap.  It was released on March 18, 2016, as the ninth track on "This Is What the Truth Feels Like" by Interscope Records.  The track was written by Stefani, Justin Tranter, Julia Michaels, Tor Hermansen, Mikkel Eriksen, and Fetty Wap.  The track's production was handled by Stargate, while additional production was made by Tim Blacksmith and Danny D.

Bang My Head: "Bang My Head" is a song by French DJ and music producer David Guetta, featuring vocals from Australian singer Sia and American rapper Fetty Wap.  It was released as the second single from the re-release of Guetta's sixth studio album, "Listen".  "Bang My Head" tallies as the album's seventh single overall.  It was released via digital download on 30 October 2015.  The original album version of the song only featured Sia's vocals, but the second verse was later replaced with vocals from Fetty Wap for the reworked single release.

K.E. on the Track: Kevin Erondu, better known as K.E. on the Track, is an American record producer.

Question: American producer K.E. on the Track worked with Fetty Wap on a song named after which shoemaker?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_title": {
      "type": "string",
      "description": "The title of the song."
    },
    "main_artist": {
      "type": "string",
      "description": "The primary artist of the song."
    },
    "producer": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the producer."
        },
        "alias": {
          "type": "string",
          "description": "The stage name or alias of the producer."
        }
      },
      "required": [
        "name",
        "alias"
      ],
      "additionalProperties": false
    },
    "named_after_shoemaker": {
      "type": "boolean",
      "description": "Indicates if the song is named after a shoemaker."
    }
  },
  "required": [
    "song_title",
    "main_artist",
    "producer",
    "named_after_shoemaker"
  ],
  "additionalProperties": false
}
