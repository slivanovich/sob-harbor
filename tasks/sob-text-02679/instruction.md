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
Stay (Black Stone Cherry song): "Stay" is a song by American rock band Black Stone Cherry, written by the band along with Joey Moi.  Black Stone Cherry recorded it on their 2011 album "Between the Devil and the Deep Blue Sea", produced by Howard Benson.

Like a Storm: Like a Storm is a hard rock band from Auckland, New Zealand, best known for combining heavy baritone guitar riffs and hard rock songs with didgeridoo.  Formed by Chris, Kent, and Matt Brooks, Like a Storm have shared American & European stages with Alter Bridge, Korn, Shinedown, Black Veil Brides, Creed, Puddle of Mudd, Staind, Sick Puppies, and many others, as well as touring North America extensively as a headline act.  Like a Storm are the highest charting New Zealand hard rock band in American radio history .  Both of Like a Storm's two studio albums, "The End of the Beginning" and "Awaken the Fire", debuted in the Billboard 200.  The band has toured with Alter Bridge, Black Stone Cherry, Three Days Grace, Steel Panther, Shinedown and Hellyeah.

Black to Blues: Black to Blues is the third EP by American band Black Stone Cherry.  It was released on September 29, 2017, through Mascot Records.

Dark Horse Tour: The "Dark Horse" Tour was a worldwide concert tour by Canadian rock band Nickelback.  It was their first world tour since the conclusion of their massive All the Right Reasons Tour, ending on September 2, 2007, in Kansas City, Missouri.  The tour was in support of their new album "Dark Horse" (2008).  Dates were announced on November 26, 2008.  Seether and Saving Abel were the opening acts on the tour.  On the second half of the North American tour, Hinder, Papa Roach, and Saving Abel were in support.  Black Stone Cherry were the support act for the European tour of the UK in May 2009.

Hell &amp; High Water: "Hell & High Water" is the second promo single from Black Stone Cherry's self-titled debut "Black Stone Cherry. " It follows the first successful single, Lonely Train.  This song reached <nowiki>#</nowiki>30 on the Mainstream Rock Tracks chart.  It was supported by a video directed by JB Carlin.

Black Stone Cherry (album): Black Stone Cherry is the debut album from southern rockers Black Stone Cherry.  The album was released on July 18, 2006 through Roadrunner Records.  The album has produced three singles: "Lonely Train", "Hell & High Water" and "Rain Wizard".

The Amorettes: The Amorettes are a Scottish hard rock band formed in 2009.  They released their first album, "Haulin' Ass", the following year.  Their second album, "Game On", which was produced by Chris Tsangarides, followed in 2015.  They have performed in support of W.A.S.P., Europe, Black Star Riders, Ash, Black Stone Cherry, Gun and Thunder among others, and have toured across the UK, as well as in several countries throughout Europe.

At the Drive-In: At the Drive-In is an American punk rock band from El Paso, Texas, formed in 1994.  The band currently consists of Cedric Bixler (vocals), Omar Rodríguez (guitar, vocals), Paul Hinojos (bass), Tony Hajjar (drums) and Keeley Davis (guitar, vocals).  After several early line-up changes, the band solidified into a five-piece, consisting of Bixler, Rodríguez, Jim Ward, Hinojos and Hajjar.  At the Drive-In released three studio albums and five EPs before breaking up in 2001.  Their third and final album before their split, 2000's "Relationship of Command", received a number of accolades and is cited as a landmark of the post-hardcore genre.  Following the breakup, Bixler-Zavala and Rodríguez-López formed The Mars Volta while Ward, Hinojos, and Hajjar formed Sparta.  At the Drive-In reunited in January 2012 and played the 2012 Coachella Valley Music and Arts Festival, as well as the 2012 Lollapalooza Festival.  In 2016, the band reunited for a second time, with guitarist and occasional lead vocalist Jim Ward no longer participating.  He was replaced by Sparta's Keeley Davis.  The band released their fourth studio album, "in•ter a•li•a", in 2017.

Rain Wizard: "Rain Wizard" is the third single from Black Stone Cherry's self-titled debut album, "Black Stone Cherry".  It follows the second successful single, "Hell & High Water."  This song reached <nowiki>#</nowiki>29 on the Mainstream Rock Tracks chart.  It is about a local legend that talks of a mysterious wiseman who could bring the rain in times of drought.

Black Stone Cherry: Black Stone Cherry is an American hard rock band, formed in 2001 in Edmonton, Kentucky.  They were signed to Roadrunner Records until 2015; the band is now signed to Mascot Label Group.  The band consists of Chris Robertson (lead vocals, lead guitar), Ben Wells (rhythm guitar, backing vocals), Jon Lawhon (bass guitar, backing vocals), and John Fred Young (drums, backing vocals).  Black Stone Cherry has released five studio albums: "Black Stone Cherry" (2006), "Folklore and Superstition" (2008), "Between the Devil and the Deep Blue Sea" (2011), "Magic Mountain" (2014), and "Kentucky" (2016), as well as three EPs, and have charted eight singles on the US Mainstream Rock Tracks charts.  The band's fifth album, "Kentucky" was released on April 1, 2016.

Question: Is At the Drive-In or Black Stone Cherry from further north?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_1_name": {
      "type": "string",
      "description": "The name of the first band being compared."
    },
    "band_1_origin": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city of origin for the first band."
        },
        "state": {
          "type": "string",
          "description": "The state of origin for the first band."
        }
      },
      "required": [
        "city",
        "state"
      ],
      "additionalProperties": false
    },
    "band_2_name": {
      "type": "string",
      "description": "The name of the second band being compared."
    },
    "band_2_origin": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city of origin for the second band."
        },
        "state": {
          "type": "string",
          "description": "The state of origin for the second band."
        }
      },
      "required": [
        "city",
        "state"
      ],
      "additionalProperties": false
    },
    "band_further_north": {
      "type": "string",
      "description": "The name of the band that originates from further north."
    },
    "comparison_reason": {
      "type": "string",
      "description": "A brief explanation of why one band's origin is considered further north."
    }
  },
  "required": [
    "band_1_name",
    "band_1_origin",
    "band_2_name",
    "band_2_origin",
    "band_further_north",
    "comparison_reason"
  ],
  "additionalProperties": false
}
