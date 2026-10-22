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
What Men Deserve to Lose: What Men Deserve To Lose is the fifth album by Scottish Celtic fusion group Peatbog Faeries, recorded at Skye Recording in Roag on the band's native Isle of Skye in 2007, and was commercially released on 16 July 2007 on the band's own label Peatbog Records, though the album had been sold at festivals, and from the band's website, since 22 June 2007.  It is the band's first album to feature Graeme Stafford, who brings what the band described as a "dancey" feel to the album.

Mellowosity: Mellowosity is the debut studio album by Scottish Celtic fusion group Peatbog Faeries, released in 1996 on Greentrax Recordings.  After forming as a vocal-based Celtic rock group in 1994, the duo had settled into becoming an instrumental Celtic fusion group by the release of "Mellowosity".  The album draws from a wide range of musical styles and influences including jazz, reggae, afrobeat, rock, Eastern music, dub and funk, that are mixed in with the band's traditional Scottish folk/Celtic sound featuring fiddles and bagpipes.

Celtic music: Celtic music is a broad grouping of music genres that evolved out of the folk music traditions of the Celtic people of Western Europe.  It refers to both orally-transmitted traditional music and recorded music and the styles vary considerably to include everything from "trad" (traditional) music to a wide range of hybrids.

Solar Shears: Solar Shears is the third studio album and fourth album overall by Scottish Celtic fusion band Shooglenifty.  After the critical acclaim given to their underground second album "A Whisky Kiss" (1996), the band left Greentrax Recordings and signed to Vertical Records in the UK and Compass Records in the US and hired long time producer Jim Sutherland to produce their new album.  The album sees the band expand their self-described "acid croft" sound, featuring a wide range of musical influences such as worldbeat, Eastern music, African music, psychedelic music, bluegrass, breakbeat and techno fused with a traditional Scottish Celtic music sound.  With this album, Sutherland introduced many unorthodox approaches to the band's music, including looped beats, scratching, electro-atmospherics and sampled 'discovered sounds' from industrial clanks and rumbles to snatches of telephone conversation and recorded pelican crossing announcements.

Croftwork: Croftwork (stylised on the album cover as CroftworK) is the fourth album by Scottish Celtic fusion group Peatbog Faeries, recorded in Roag on the Isle of Skye, and released in 2005 on the band's own Peatbog Records label.  It was released as the label's second album following on from the band's previous album "Welcome to Dun Vegas" (2003).  They recorded the album at Phat Controller Productions on the band's native Isle of Skye.

Welcome to Dun Vegas: Welcome To Dun Vegas is the third album by Scottish Celtic fusion group Peatbog Faeries, recorded in a cottage on the banks of Pool Roag, near Dunvegan, on the Isle of Skye, and released in July 2003 as the first release on the band's own Peatbog Records label.  Following the electronic-infused "Faerie Stories" (2001), "Dun Vegas" was co-produced between Calum MacLean and the band's drummer Iain Copeland.  The album is experimental, mixing traditional and modern Celtic music with other genres and styles such as African music and electronica and featuring experimental effects including backwards drumming and a track based around a kitchen cooker timer.

Faerie Stories: Faerie Stories is the second album by Scottish Celtic fusion group Peatbog Faeries, released in 2001 on Greentrax Recordings.  The album was reissued in 2008 as a digipack.  The album is large departure from the sound of their début album "Mellowosity" (1996), and sees the band explore a largely electronic sound mixed with their traditional Celtic fusion sound.  Influences of electronic genres such as electronica, house, dubtronica and trip hop, in addition to even dub music and African music can be heard on the album fused with traditional Scottish Celtic music.

Blackhouse (album): Blackhouse is the seventh studio album by Scottish celtic fusion band Peatbog Faeries, released in May 2015 by the band's label Peatbog Records.  After recording their acclaimed album "Dust" (2011), the band played live for the following few years, during which time fiddler Peter Tickell left the band, to be replaced by Ross Touper.  As the band had not recorded an album for some years, they returned to record "Blackhouse" mainly in a cottage in Kilchoan, Ardnamurchan during 2014, although recording continued into 2015.  Their first album with Touper, and their first without a brass section since "Welcome to Dun Vegas" (2003), "Blackhouse" was produced by Calum MacLean and displays a very eclectic array of genres, fusing the band's Scottish celtic roots with genres such as jazz, funk, reggae, dance and house.

Dust (Peatbog Faeries album): Dust is the sixth studio album by the Scottish Celtic fusion band Peatbog Faeries, released on 8 August 2011 on Peatbog Records, although pre-release copies were released on 20 July 2011 through the band's online shop.  Following the band's 2008 tour and subsequent live album, the band's fiddle player Adam Sutherland and drummer Iain Copeland left the band, replaced by Peter Tickell and Stu Haikney respectively whose experience helped stir the band in a new direction.  The band set to record "Dust" in 2011 with longtime producer Calum MacLean, beginning work in Orbost and concluding work at Cumbernauld College.  Haikney brought experimental fiddle techniques to the band, and similarly experimental production techniques, whilst the entire band experimented with various genres of music including African music, funk, reggae, ambient music and electronic music alongside the band's traditional Celtic fusion sound.  The brass sound of previous albums also returned.  The album was also an attempt to translate the band's live sound to studio work.

Live (Peatbog Faeries album): Live is the first (and only) live album by Scottish celtic fusion band Peatbog Faeries, released in 2009 by Peatbog Records.  It is a compilation album of live tracks from two of the band's concerts in their 2008 tour, and is the band's first album to have been released in a digipak.

Question: Faerie Stories is the second album by Scottish Celtic fusion group Peatbog Faeries, released in 2001 on Greentrax Recordings, influences of electronic genres such as electronica, house, dubtronica and trip hop, in addition to even dub music and African music can be heard on the album fused with traditional Scottish music of which type, that's a broad grouping of music genres that evolved out of the folk music traditions of the Celtic people of Western Europe?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "album_title": {
      "type": "string",
      "description": "The title of the album."
    },
    "band_name": {
      "type": "string",
      "description": "The name of the band that released the album."
    },
    "album_number": {
      "type": "integer",
      "description": "The sequential number of the album in the band's discography."
    },
    "release_year": {
      "type": "integer",
      "description": "The year the album was released."
    },
    "record_label": {
      "type": "string",
      "description": "The record label the album was released on."
    },
    "musical_influences": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of musical genres and styles that influenced the album's sound."
    },
    "fused_traditional_music_type": {
      "type": "string",
      "description": "The specific type of traditional music the album fuses with."
    },
    "traditional_music_description": {
      "type": "string",
      "description": "A description of the fused traditional music type."
    }
  },
  "required": [
    "album_title",
    "band_name",
    "album_number",
    "release_year",
    "record_label",
    "musical_influences",
    "fused_traditional_music_type",
    "traditional_music_description"
  ],
  "additionalProperties": false
}
