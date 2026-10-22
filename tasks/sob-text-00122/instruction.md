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
What Are You So Scared Of?: What Are You So Scared Of?  is the debut studio album by Australian rock band Tonight Alive, released on 14 October 2011 through Sony Music Australia.  Tonight Alive traveled to Los Angeles to record the album with producer Mark Trombino (blink-182, Jimmy Eat World, Midtown).  As the follow-up to 2010's "Consider This" EP, "What Are You So Scared Of?"  debuted on the Australian albums chart at No. 15.  The record's first official single, "Starlight", was released 1 July 2011.  Its second, "Let It Land", was released 19 September 2011.

Bleed American (song): "Bleed American" is a song by American rock band Jimmy Eat World.  It was released in September 2001 as the lead single from their fourth album "Bleed American" (retitled "Jimmy Eat World").  The song was originally titled "Bleed American", but similar to the name change of the album after the September 11 attacks, the song was retitled "Salt Sweat Sugar" after the first line in the song's chorus.

Pain (Jimmy Eat World song): "Pain" is a song by American rock band Jimmy Eat World.  It was released in September 2004 as the first single from their 2004 album "Futures" and became their second number-one hit on the "Billboard" Modern Rock Tracks chart.  Although its album is not their most successful and "Pain" is not the highest charting single, the single has received Gold status by the RIAA, making "Pain" Jimmy Eat World's best-selling single.  It was featured on the video game "Karaoke Revolution Party".

Bleed American: Bleed American is the fourth studio album by American rock band Jimmy Eat World.  It was released on July 24, 2001 by DreamWorks Records.  It was the first recording launched after signing the band a few months prior.  The album was re-released as Jimmy Eat World after the September 11 attacks on New York and Washington, D.C. that took place a month after its initial release.

Mark Trombino: Mark Trombino is an American multi-platinum music producer, drummer, and recording artist.  He produced, engineered, and mixed tracks for many artists including Jimmy Eat World, Blink-182, The Starting Line, Finch, Motion City Soundtrack, and All Time Low

Invented (album): Invented is the seventh studio album by American rock band Jimmy Eat World, released on September 28, 2010 through Interscope Records.  Recorded primarily at the band's home-based studio, the album was co-produced by Mark Trombino, who had previously worked on the band's earlier material; "Static Prevails" (1996), "Clarity" (1999) and "Bleed American" (2001).  The album was preceded by the single "My Best Theory", released on digital download on August 10, 2010.

Jimmy Eat World (1994 album): Jimmy Eat World is the debut studio album by American rock band Jimmy Eat World, released in 1994 on Wooden Blue Records.  The album displays their early sound with guitarist and eventual backing vocalist Tom Linton singing lead on most of the songs on this album.  The one song on this album that is sung by current primary vocalist Jim Adkins is the track, "Usery".  The album also marks the only appearance of former bass guitarist Mitch Porter.

Static Prevails: Static Prevails is the second studio album by American rock band Jimmy Eat World, released on July 23, 1996 on Capitol Records.  Produced by Wes Kidd, Mark Trombino and the band itself, the album is the first to feature bass guitarist Rick Burch and the first to have been produced by Trombino.  The album marks the band's major label debut.

Self-titled Album (The Audition album): Self-titled Album is the third studio album released by The Audition.  It was produced by Mark Trombino, who has previously worked with Jimmy Eat World, Senses Fail, Blink-182 and Finch, amongst others.  This is the first release since the departure of original bassist and founding member Joe Lussa (Joe did record all bass parts on all 10 songs).

The Middle (song): "The Middle" is a song by American rock band Jimmy Eat World.  It was released in November 2001 as the second single of their fourth album "Bleed American".  It was a top five "Billboard" Hot 100 hit in 2002.  The song was a breakthrough hit for Jimmy Eat World (who had self-financed the recording of the "Bleed American" album after having been dropped by Capitol Records in 1999).

Question: Which Jimmy Eat World studio album was co-produced by Mark Trombino and re-released after September 11, 2001?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "album_title": {
      "type": "string",
      "description": "The original title of the studio album."
    },
    "band_name": {
      "type": "string",
      "description": "The name of the band that released the album."
    },
    "producer_name": {
      "type": "string",
      "description": "The name of the producer who co-produced the album."
    },
    "initial_release_date": {
      "type": "string",
      "description": "The date of the album's initial release."
    },
    "re_release_details": {
      "type": "object",
      "properties": {
        "re_release_title": {
          "type": "string",
          "description": "The title the album was re-released under."
        },
        "re_release_reason": {
          "type": "string",
          "description": "The event or reason for the album's re-release."
        }
      },
      "required": [
        "re_release_title",
        "re_release_reason"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "album_title",
    "band_name",
    "producer_name",
    "initial_release_date",
    "re_release_details"
  ],
  "additionalProperties": false
}
