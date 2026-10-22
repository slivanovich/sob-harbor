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
Voice of America (album): Voice of America is the second solo album by Little Steven & the Disciples of Soul released on May 7, 1984, four weeks before Bruce Springsteen released "Born in the U.S.A."

Freedom – No Compromise: Freedom – No Compromise is the third solo album by Little Steven released in 1987.

Adam Clayton: Adam Charles Clayton (born 13 March 1960) is an Irish musician, best known as the bass guitarist of the rock band U2.  He has resided in County Dublin since the time his family moved to Malahide when he was five years old in 1965.

Men Without Women (album): Men Without Women, credited to Little Steven & The Disciples of Soul, is the debut solo album by Steven Van Zandt, a member of Bruce Springsteen's E Street Band and a songwriter / producer with the Jersey Shore band Southside Johnny & The Asbury Jukes.  The title track was inspired by the Ernest Hemingway collection of short stories of the same name.

The Contrast (band): The Contrast are a guitar power pop band based in Peterborough, Cambridgeshire in the United Kingdom.  They were formed in 1999 by David Reid and have since released five albums on the New York based label Rainbow Quartz and two for Wicked Cool Records.  Since the release of their second album "Wireless Days", their music has been regularly played by Little Steven on his Underground Garage radio show.  Little Steven once described them on air as "One of the best bands on the planet – and England too" and consequently invited them to play the Underground Garage Festival on Randall's Island in 2004.  In May 2007, they released a new album called "Underground Ghosts" (also on Rainbow Quartz) that has since been regularly featured on Little Steven's Underground Garage show.  A compilation of tracks from all of the Rainbow Quartz albums was released in 2007.  This contains new and unreleased tracks and is the band's first release on Little Steven's "Wicked Cool" label.  The band's song "Mystery #1" was featured on a Wicked Cool compilation album, "The Coolest Songs In The World- Vol 2".

Born Again Savage: Born Again Savage is the fifth solo album by Little Steven released in 1999.  The album was a return to the raw, garage rock sound of his second album, "Voice of America".  The main topic of the album is religion.  U2 bassist Adam Clayton and Led Zeppelin drummer Jason Bonham are featured on all 10 tracks.  Jean Beauvoir, who was one of the original Disciples of Soul, sang background vocals on the album.  After its release, Little Steven returned to play for Bruce Springsteen & The E Street Band for good.

Will Smith discography: American actor/rapper Will Smith has released four studio albums, one compilation album, 17 singles (12 as lead artist and five as featured artist), one video album and 20 music videos (14 as lead artist, three as featured artist and three guest appearances).  After working in the late 1980s and early 1990s with Jeff Townes as DJ Jazzy Jeff & The Fresh Prince, Smith began his solo career in 1997 with the release of "Men in Black", the theme song for the film of the same name, which topped singles charts in several regions across the world, including the UK.  "Men in Black" (and second single "Just Cruisin'") was later included on Smith's debut solo album "Big Willie Style", which reached the top ten of the US "Billboard" 200 and was certified nine times platinum by the Recording Industry Association of America (RIAA).  The third single from the album, "Gettin' Jiggy wit It", became Smith's first "Billboard" Hot 100 number one when it was released in 1998.

Revolution (Little Steven album): Revolution is the fourth solo album by Little Steven released in 1989.  The Disciples of Soul were gone in all but name (although former Disciple/Young Rascals drummer Dino Danelli did the album art), and the music was largely electronic.

Steven Van Zandt: Steven Van Zandt (born November 22, 1950) is an American musician and actor, who frequently goes by the stage names Little Steven or Miami Steve.  He is a member of Bruce Springsteen's E Street Band, in which he plays guitar and mandolin.  He is also known for his roles on television dramas such as Silvio Dante on "The Sopranos" (1999–2007) and Frank Tagliano / Giovanni "Johnny" Henriksen on "Lilyhammer" (2012–2014).  Van Zandt also had his own solo band called Little Steven and The Disciples of Soul in the 1980s.  In 2014, Van Zandt was inducted into the Rock and Roll Hall of Fame as a member of the E Street Band.

Ed Manion: Ed Manion (born February 28, 1952), also known as Eddie "Kingfish" Manion, is an American saxophonist, who plays both tenor and baritone sax.As a solo artist, he released his own instrumental album titled Nightlife in 2015.  Manion is currently a recording and touring member of Little Steven and the Disciples of Soul.  He was a touring member of the horn section for Bruce Springsteen and the E Street Band and also a member of Bruce Springsteen with The Seeger Sessions Band Tour, later called Bruce Springsteen with The Sessions Band.  He is an original member of Southside Johnny and the Asbury Jukes, The Miami Horns, and Little Steven and the Disciples of Soul.  As a session musician, he has recorded, toured, and/or performed with, among others, Bruce Springsteen and The E Street Band, Diana Ross, Gary U.S. Bonds, Bon Jovi, Willy DeVille, Dave Edmunds, Bob Dylan, Keith Richards, Darlene Love, Ronnie Spector, Dion, The Allman Brothers Band, Kim Wilson, and Graham Parker.  As a solo artist, he released his own CD titled "Follow Through" in 2004.

Question: Which featured artist on the Little Steven solo album "Born Again Savage" has lived in County Dublin?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "album_name": {
      "type": "string",
      "description": "The name of the Little Steven solo album."
    },
    "album_artist": {
      "type": "string",
      "description": "The primary artist of the album."
    },
    "featured_artist_name": {
      "type": "string",
      "description": "The name of the featured artist on the album."
    },
    "featured_artist_instrument": {
      "type": "string",
      "description": "The instrument played by the featured artist on the album."
    },
    "residence_location": {
      "type": "string",
      "description": "The county where the featured artist has lived."
    },
    "residence_start_year": {
      "type": "integer",
      "description": "The year the featured artist began residing in the specified location."
    }
  },
  "required": [
    "album_name",
    "album_artist",
    "featured_artist_name",
    "featured_artist_instrument",
    "residence_location",
    "residence_start_year"
  ],
  "additionalProperties": false
}
