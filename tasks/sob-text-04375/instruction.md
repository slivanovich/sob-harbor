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
Reggaestep: Reggaestep (portmanteau of reggae and dubstep) is a fusion genre of reggae music and dubstep that has gained popularity online, particularly SoundCloud.  Reggaestep typically has similar drum samples as those used in reggae; however, the timing of these drums corresponds with the typical syncopation of drums in dubstep.  Other influence taken from reggae include harmonic accentuation of the offbeats, however off-beat rhythms can sometimes be layered on top of more traditional dubstep or ragga melodies.  The tempo tends to be at 140 BPM which is typical to dubstep.  The "drops" in reggaestep are very similar to those of dubstep, but often follow similar melody patterns to reggae.

Metalcore: Metalcore is a fusion genre combining elements of heavy metal and hardcore punk.  The word is a portmanteau of the names of the two genres.  Among other styles blending metal and hardcore, such as crust punk and grindcore, metalcore is noted for its use of breakdowns, which are slow, intense passages conducive to moshing.  Pioneering metalcore bands—such as Integrity, Earth Crisis and Converge, all of which had formed by 1990—are described as leaning more toward hardcore, with their style sometimes being called metallic hardcore, whereas later bands—such as Killswitch Engage, All That Remains, Trivium, As I Lay Dying, Bullet for My Valentine, and Parkway Drive—are described as leaning more towards metal.  Pantera and Sepultura (who influenced Trivium, Atreyu, Bleeding Through and Unearth) have been particularly influential to the development of metalcore in the 2000s, which saw many bands in the genre achieve commercial success.

Fail Emotions: Fail Emotions (sometimes called simply FE) is a Russian Electronicore band from Yaroslavl.

Subatomic Sound System: Founded in 1999 by John Emch and Noah Shachtman, Subatomic Sound System brought together musicians, producers, DJs and visual artists from a variety of backgrounds and traditions primarily based in New York City and Brooklyn to form a record label and collective that built on a combination of new music technology and traditional instruments to produce music across a variety of genres, often combining genres, in an effort to adapt 1970s’ Jamaican sound system culture and dub studio techniques to current music genres and forms of live performance.  In fall 2008, Subatomic Sound System garnered international attention for a limited edition vinyl 12" featuring their collaboration with Vienna's Dubblestandart and dub inventor Lee "Scratch" Perry, releasing the first songs from Perry in the dubstep genre, one of the first recorded examples of a tangible connection between the popular UK based electronic genre that emerged in the begin of the first decade of the 21st century and the Jamaican dub from the 1970s where dubstep's origins were rooted and which had been primarily originated by Perry himself.  Beginning in 2008, Subatomic Sound System started hosting weekly radio shows on 91.5fm, Radio New York and webcast on Brooklyn Radio.

Vitamin D (album): Vitamin D is the first studio album by Canadian dubstep producer and artist Datsik, released on April 10, 2012 in US.  The album was co-produced by various electronic music producers such as fellow Canadian dubstep producer Downlink, Israeli psytrance and electronica production duo Infected Mushroom and American DJ Z-Trip.  The first official single from the album is "Fully Blown" (featuring Snak the Ripper), which was released on January 31.  The second single, "Evilution", which was co-produced by Infected Mushroom and features vocals from Jonathan Davis of the nu metal band Korn, was released on March 13.

Electronicore: Electronicore (also known as synthcore or trancecore) describes a stylistic fusion of metalcore with elements of various electronic music genres, such as trance, electronica, dubstep, or others.  The term electronicore is a portmanteau of "electronic" and "metalcore".  Notable artists of this genre have originated from the United Kingdom, the United States, Australia, Canada, France, Hong Kong and Japan.

The Remix Master: Jackson Tan (born February 14, 1975) better known by his stage name The Remix Master is a musician, DJ and producer.  He is also known as DJ JT, T, The Blizzard, 2B1, WMN and Apex.  His works are notable for integrating trance, electro, dubstep, techno, hip hop with electronic music sounds and world music genres.  JT composes his own beats, dance and trance tracks which frequently feature a prominent bass lineHe has appeared alongside artists including Michael Procter, Akon, Pitbull, Lil Jon, Loren Taylor, Lil Wayne, Wendy Lewis, The Bliz, Ne-Yo, Jason D, Britney Spears, Chris Brown, Whitney Houston, Foxes, Christina Milian, and Ellie Goulding.

Oscilloscoop: OscilloScoop is an interactive music app for iOS that runs on the iPad, iPhone, and iPod Touch, available through the iTunes App Store.  The app presents a real-time interface for creating electronic music in various electronic music genres from hip hop to techno and house.  The app is designed with a minimalist modern interface of three colored crowns, that spin like potters' wheels.  Touching each crown affects the parameters of the audio.  The top crown controls pitch, the middle a low pass resonant filter, and the bottom a fader.  Controls on the left allow one to change the bassline beat, while buttons on the right allow the user to save their creation, and a slider below controls tempo.

Digitally Imported: Digitally Imported (DI) is an Internet radio broadcaster playing various types of electronic music including house, trance, progressive, techno, eurodance, drum and bass, and dubstep, across 91 hand curated channels.  It was founded in December 1999 as a hobby project by Ari Shohat in his Binghamton University dorm room and was one of the first Internet radio stations.  It has often been listed as one of the top electronic dance music radio stations online and was awarded "Best Global Radio Station" at the International Dance Music Awards in March 2010.  It also offers streaming radio services of other, non-electronic dance music genres  — such as pop hits, jazz and rock — across nearly 300 channels through its sister networks, RadioTunes, JAZZRADIO, ROCKRADIO, and ClassicalRadio.

The Spindle Sect: The Spindle Sect is an alternative metal band originally from Cape Town, South Africa, now based in the United Kingdom.  They combine alternative metal, hip hop and various heavy subgenres, such as metalcore and hardcore punk, with elements of various electronic bass music genres, such as breakbeat, big beat, electronica, trance, industrial, drum and bass and dubstep.

Question: What describes a stylistic fusion of metalcore with elements of various electronic music genres, such as trance, electronica, dubstep, or others whos genre has a band from Yaroslavl , that is a portmanteau of what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "genre_name": {
      "type": "string",
      "description": "The name of the fusion genre."
    },
    "genre_description": {
      "type": "string",
      "description": "A description of the genre's stylistic fusion."
    },
    "portmanteau_components": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The words that form the portmanteau for the genre name."
    },
    "example_band": {
      "type": "object",
      "properties": {
        "band_name": {
          "type": "string",
          "description": "The name of a band associated with the genre."
        },
        "origin_city": {
          "type": "string",
          "description": "The city of origin for the band."
        },
        "origin_country": {
          "type": "string",
          "description": "The country of origin for the band."
        }
      },
      "required": [
        "band_name",
        "origin_city",
        "origin_country"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "genre_name",
    "genre_description",
    "portmanteau_components",
    "example_band"
  ],
  "additionalProperties": false
}
