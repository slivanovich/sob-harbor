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
Point of Entry: Point of Entry is the seventh album from the British heavy metal band Judas Priest.  It was released on 26 February 1981.

Hell Bent Forever: A Tribute to Judas Priest: Hell Bent Forever: A Tribute to Judas Priest is a tribute album, released in 2008.  It includes several rock and metal bands such as Motörhead, Icarus Witch, L.A. Guns and Sepultura, covering songs by British heavy metal band Judas Priest.  The album's font is a mistake because the red lettering is in the style of Iron Maiden's logo instead of Judas Priest's logo

Hero, Hero: Hero, Hero is a compilation album of early Judas Priest recordings, released in between "British Steel" (1980) and "Point of Entry" (1981) by Gull Records.

Judas Rising: "Judas Rising" is a song by heavy metal band Judas Priest.  It is the opening track on the band's 2005 album Angel of Retribution.  The song is about the Judas Priest "Messiah" on the cover of the albums "Sad Wings of Destiny", "Painkiller" and "Angel of Retribution".  .  It was also included on the album's The Essential Judas Priest and

Rocka Rolla: Rocka Rolla is the debut studio album by British heavy metal band Judas Priest, released on 6 September 1974 by Gull Records.  It was produced by Rodger Bain, who had made a name for himself as the producer of Black Sabbath's first three albums.  It is the only album to feature drummer John Hinch.

The Best of Judas Priest: The Best of Judas Priest is a collection of a few select songs from Judas Priest's first two albums, and was released under Gull, the band's former record label.  It was the first of many reissues of the band's earlier material produced in an effort to "capitalize on Judas Priest's popularity" and was released without any consent from the band.

Stained Class: Stained Class is the fourth album by British heavy metal group Judas Priest, released in February 1978.  It is the first of three albums to feature drummer Les Binks.  It gained notoriety for its dark lyrics and themes, as well as 1990 civil action trial where the band were accused of backmasking that led to the suicide attempts of two teenagers.  Stained Class was ranked as the greatest Judas Priest album on Stereogum.com, and was described by Steve Huey on Allmusic.com as “Judas Priest’s greatest achievement.”

Genocide (album): Genocide is a 2000 Judas Priest compilation consisting of their first two albums, "Rocka Rolla" and "Sad Wings of Destiny", plus a bonus track from the "Sad Wings of Destiny" sessions as well.  Like several others in the past, Genocide was released under the label Gull, in an effort to "capitalize on Judas Priest's popularity."  Judas Priest's management firmly states that people should not buy these compilations, because even though it would seem like a new album on the surface, it's just a re-issue of material already recorded.

A Tribute to Judas Priest: Legends of Metal: A Tribute to Judas Priest: Legends of Metal Vol.  I and A Tribute to Judas Priest: Legends of Metal Vol.  II are tribute albums, both released in 1997 by Century Media Records.  It includes several rock and metal bands such as Helloween, Overkill, Saxon, Heavens Gate, Blind Guardian, Mercyful Fate, and Iced Earth, covering songs by British heavy metal band Judas Priest.  Some of the songs included in this album have been previously released by the artists.

Victim of Changes (album): Victim of Changes is ex-Judas Priest singer Al Atkins's fourth release, named after a Judas Priest song of the same name originally featured on the "Sad Wings of Destiny" album.  The album's sleeve contains three pages of historic photos and a biography outlining his days in Judas Priest.  Former Judas Priest drummer Dave Holland plays on this release.

Question: What was Judas Priest's seventh album and produced by Gull Records?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "album_name": {
      "type": "string",
      "description": "The name of the album."
    },
    "album_release_order": {
      "type": "integer",
      "description": "The sequential release number of the album for the band."
    },
    "release_date": {
      "type": "string",
      "description": "The release date of the album."
    }
  },
  "required": [
    "album_name",
    "album_release_order",
    "release_date"
  ],
  "additionalProperties": false
}
