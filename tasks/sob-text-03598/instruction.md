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
CLAVVS: CLAVVS (pronounced "claws") is an indie pop and trip hop duo from Atlanta, Georgia.  Composed of four-time Grammy Award-winning producer and multi-instrumentalist Graham Marsh (Gnarls Barkley, Kid Cudi, Lauryn Hill) and writer and vocalist Amber Renee, CLAVVS was formed in 2013 in East Atlanta Village.  They debuted with single "Sit You Down" in 2015, which was featured on the international PBS series "The Music Voyager" alongside Janelle Monáe.  Follow-up single "Spectre" was featured in MTV's "Teen Wolf" on season 6, episode 3.  CLAVVS self-released their first full-length album "halfblood" on April 4, 2016.  They have since performed with the likes of Rhye, Ibeyi, Baio, and Ages and Ages.  Their second LP "World Underwater" was released on March 24, 2017.

Gnarls Biggie: is a hip hop mashup album created in the same vein as Danger Mouse's "The Grey Album".  It was produced by a group of Brooklyn-based DJ's known as Sound Advice.  The album features 11 songs in which the tracks of Gnarls Barkley are cut-up into beats and then layered with raps of The Notorious B.I.G. It was released on July 17, 2006 on the website gnotorious.com and was featured on the websites of the music magazines "VIBE" and "Spin".  There was also a promotional video released on YouTube.  Its album cover parodies the cover of The Notorious B.I.G.'s "Ready to Die" by replacing the baby's head with Cee-Lo's head.  All of the tracks on the album use beats that sample Gnarls Barkley's album "St. Elsewhere".

Salsa (EP): Salsa is an EP by American alternative rock band "Residual Kid", which was released April 8, 2016.  It was produced by Grammy-nominated Chris "Frenchie" Smith.  To celebrate the release, the band held an EP release show at The Hi-Dive in Denver, Colorado.  The song "Scentless Princess" was released as the lead single from the EP, with a video directed by Joshua Logan and Michael Anthony Gibson.  A second music video was released later for the song "Chill."

Gnarls Barkley: Gnarls Barkley is an American soul duo, composed of singer-songwriter CeeLo Green and producer Danger Mouse.  They have released two studio albums, "St. Elsewhere" (2006) and "The Odd Couple" (2008).  "St. Elsewhere" was recorded on the Warner Music UK label, and contained their hit single "Crazy" which topped at number two on the US Hot 100, and topped the charts in the UK.  It was also nominated at the 2007 Grammy Awards for Record of the Year, and was platinum certified for shipping over 1,000,000 records.  "The Odd Couple" was recorded on Downtown Records label, and was scheduled for release in April 2008, but due to a leak of their album over the internet, they were forced to release it early.  The album in its entirety received good reviews, but did not have as much commercial success as their first album.

Four Leaf Clover (Second Person song): "Four Leaf Clover" is a song by English post-trip hop band Second Person, which will be on the band's forthcoming album: "Come to Dust" - the follow-up to their debut album "Chromatography".  Due for release in 2007 this song has a music video currently in production by Mina Song (best known for her work on the original Gnarls Barkley video for "Crazy").

Barnaby Clay: Barnaby Clay (born May 15, 1973) – also known as Barney Clay - is a British film director.  Clay graduated London International Film School in 1996, directing the school‘s entry to the Fuji Film Scholarship Awards – the short film ‘Justice in Mind’ took home the top award of Best Film.  Soon after leaving film school he moved into directing music videos and commercials.  He has directed music videos for bands like John Spencer Blues Explosion, TV on the Radio, Gnarls Barkley, the Yeah Yeah Yeahs, Dave Gahan to name a few.  In 2003 Clay traveled to Russia with the band gypsy punk band Menlo Park to make his first documentary for Britain’s Channel 4, entitled ‘Greetings From Beartown'.  In 2005 he wrote and directed a short film for Ritz Fine Jewellery titled ‘Carousel’, starring the actress Chloe Sevigny.

Faces (EP): Faces is an EP by American alternative rock band "Residual Kid", which was released in October 2012.  It was produced by Grammy-nominated Chris "Frenchie" Smith.

Gnarls Barkley discography: The discography of Gnarls Barkley, an American alternative hip hop duo composed of record producer Danger Mouse and soul singer Cee Lo Green, consists of two studio albums, two extended plays, seven singles and seven music videos.  The duo originally met in the late 1990s, and began to record music together in 2003 following the release of Danger Mouse's 2003 album "Ghetto Pop Life".  Their first single, "Crazy", was released in 2006; it achieved worldwide chart success, reaching number two on the US "Billboard" Hot 100 – where it was certified double platinum by the Recording Industry Association of America (RIAA) – and reaching the top ten of the Australian, New Zealand and Swiss singles charts, among others.  It also topped the UK Singles Chart, attracting considerable attention for becoming the first song ever to top the chart on digital download sales alone, following a change to the chart's eligibility rules allowing songs to chart purely on digital sales providing that it was given a physical release the following week.  The song appeared on Gnarls Barkley's debut studio album, "St. Elsewhere", which peaked at number four on the US "Billboard" 200 as well as topping the New Zealand and United Kingdom albums charts.  Three further singles – "Smiley Faces", which reached the top ten of the UK and Irish singles charts, "Who Cares? " and a cover of the Violent Femmes song "Gone Daddy Gone" – were released from "St. Elsewhere", although none of them appeared on the "Billboard" Hot 100.

Residual Kid: Residual Kid is an American rock band from Austin, Texas formed in 2009.  The group consists of Deven Ivy (vocals, guitar), Ben Redman (drums), and Max Redman (bass guitar).  They have released three EPs: "Box" in 2011, which was recorded with an earlier lineup, "Faces", featuring the current lineup, in 2012, and "Salsa" in 2016.

Run (I'm a Natural Disaster): "Run (I'm a Natural Disaster)", also known more commonly as "Run", is a song written and recorded by Gnarls Barkley.  It is the first single to be released from the band's second album "The Odd Couple".  Released in February 2008 as a digital download in the UK and the US via the iTunes Store, a physical release of the single followed in the UK on March 31.  The song features a sample from Keith Mansfield's "Junior Jet Set" from the KPM LP "Flamboyant Themes" and "Starting Out the Day" by Strawberry Alarm Clock.  The song is featured in the film "", as a playable song in the video game "Dance Central 2", and is heard in promos for Disney-Pixar's "Cars 2".  This song was number 34 on "Rolling Stone"' s list of the 100 Best Songs of 2008.

Question: Which is a band from Texas, Gnarls Barkley or Residual Kid?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_name": {
      "type": "string",
      "description": "The name of the band from Texas."
    },
    "origin_city": {
      "type": "string",
      "description": "The city where the band originated."
    },
    "origin_state": {
      "type": "string",
      "description": "The state where the band originated."
    },
    "genre": {
      "type": "string",
      "description": "The musical genre of the band."
    },
    "formation_year": {
      "type": "integer",
      "description": "The year the band was formed."
    }
  },
  "required": [
    "band_name",
    "origin_city",
    "origin_state",
    "genre",
    "formation_year"
  ],
  "additionalProperties": false
}
