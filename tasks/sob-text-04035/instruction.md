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
Juha Harju: Juha Harju (born 1981 in Kuopio) is a Finnish heavy metal musician.  He was the vocalist of the Finnish dark metal/black metal band Shade Empire and dark-metal band Chaosweaver (Cypher Commander).  He also plays bass in black metal bands Ajattara (under the alias Tohtori Kuolio) and Deathchain (under the alias Kuolio).  He has named Ozzy Osbourne and Chuck Schuldiner as his favourite musicians.

Gary Cherone: Gary Francis Caine Cherone ( ; born July 26, 1961) is an American rock singer and songwriter.  He is best known for his work as the lead vocalist of the Boston rock group Extreme, as well as his short stint as the lead vocalist for Van Halen on their 11th album "Van Halen III" and subsequent tour.  In recent years he has released solo recordings.  In 2007, he reunited with Extreme.

Chuck Schuldiner: Charles Michael Schuldiner (May 13, 1967 – December 13, 2001) was an American singer, songwriter, and guitarist.  He founded the pioneering band Death in 1983.  Schuldiner is often referred to as "The Godfather of Death metal",

Shannon Hamm: Shannon Hamm is a death metal guitarist who played in Death from 1996 until their break-up in 2001.  He then joined Chuck Schuldiner's second band Control Denied, which ended with the death of Schuldiner in 2001.  Before Death, he was a locally well known guitarist in the Texas underground metal scene.  He was particularly good friends with "Dimebag" Darrell Abbott of Pantera and Damageplan.  According to Abbott, Hamm "out shredded" Darrell in Pantera's glam metal days while Hamm was in a band named Metalstorm.

Van Halen III: Van Halen III is the eleventh studio album by American rock band Van Halen, released on March 17, 1998 by Warner Bros.  Records.  Produced by Mike Post and Eddie Van Halen, it is the band's only studio album to feature lead vocalist Gary Cherone, and the last to feature bass guitarist Michael Anthony before he was replaced in the band by Eddie's son Wolfgang in 2006.  Work on a follow-up album with Cherone commenced in 1999, but never advanced past a few demos.

Tribe of Judah (band): Tribe of Judah is Gary Cherone's post-Van Halen band featuring a couple of former members of Extreme (bassist Pat Badger and drummer Mike Mangini).  An eponymous EP was released in 2001 and a full-length album was released in late 2002.  Tribe of Judah is different from Cherone's other work as it features a more industrial/electronic sound.  At least one song, "Left for Dead", was (supposedly) slated to be a track on a follow-up Van Halen album which would have featured Cherone.

Chris Reifert: Chris Reifert (born February 23, 1968) is an American death metal musician, and one of the pioneers of the death/doom genre.  Although his music is more death metal than doom metal, he is one of the first musicians that blended the two styles.  He played drums on the Death debut album, "Scream Bloody Gore".  Since he parted ways with Chuck Schuldiner in 1987 after Schuldiner moved back to Florida, Reifert decided to stay in the San Francisco Bay Area, and in 1987 he formed his own band, Autopsy.  In this band, he played not only drums but handled the vocals as well.  After several albums, Autopsy split up in 1995 and Reifert and bandmate Danny Coralles began playing in their side-project, Abscess, full-time.  After Abscess dissolved in 2010, Autopsy reformed and is currently planning to tour and record new material.

Control Denied: Control Denied was a band formed by death metal musician and Death founder Chuck Schuldiner to create progressive heavy metal.  The band started in 1996 as Schuldiner wanted to procure a more melodic style than was possible with Death.  The project was interrupted by Death's release "The Sound of Perseverance" in 1998, but finally the debut album "The Fragile Art of Existence" was released in 1999.  A second album, tentatively titled When Man and Machine Collide, was partly recorded, but the death of Schuldiner in 2001 put the recordings on hold.  Remaining band members have expressed a wish to complete and release the material.

Death discography: The discography of Death, a metal band, consists of seven studio albums and four live albums. Death was an American metal band founded in 1983.  The band's founder, Chuck Schuldiner, is considered "a pioneering force in death metal and grindcore".  The band ceased to exist after Schuldiner died of brain cancer in 2001, though it remains an enduring metal brand.

Death (metal band): Death was an American death metal band from Orlando, Florida, founded in 1983 by guitarist and vocalist Chuck Schuldiner.  Death is considered to be one of the most influential bands in heavy metal and a pioneering force in death metal.  Its debut album, "Scream Bloody Gore", has been widely regarded as the first death metal record, while the band's driving force, Chuck Schuldiner, is acknowledged as the originator of extreme metal.  Death had a revolving lineup, with Schuldiner being the sole consistent member.  The group's style also progressed, from the raw sound on its early albums to a more sophisticated one in its later stage.  The band ceased to exist after Schuldiner died of glioma and pneumonia in December 2001, but remains an enduring metal band.

Question: Did Chuck Schuldiner and Gary Cherone ever play in the same bands?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "musician_1_name": {
      "type": "string",
      "description": "The name of the first musician."
    },
    "musician_2_name": {
      "type": "string",
      "description": "The name of the second musician."
    },
    "played_in_same_bands": {
      "type": "boolean",
      "description": "Indicates whether the two musicians ever played in the same bands."
    },
    "musician_1_bands": {
      "type": "array",
      "description": "A list of bands the first musician played in, with their role.",
      "items": {
        "type": "object",
        "properties": {
          "band_name": {
            "type": "string"
          },
          "role": {
            "type": "string"
          }
        },
        "required": [
          "band_name",
          "role"
        ],
        "additionalProperties": false
      }
    },
    "musician_2_bands": {
      "type": "array",
      "description": "A list of bands the second musician played in, with their role.",
      "items": {
        "type": "object",
        "properties": {
          "band_name": {
            "type": "string"
          },
          "role": {
            "type": "string"
          }
        },
        "required": [
          "band_name",
          "role"
        ],
        "additionalProperties": false
      }
    },
    "common_bands": {
      "type": "array",
      "description": "A list of bands that both musicians played in.",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "musician_1_name",
    "musician_2_name",
    "played_in_same_bands",
    "musician_1_bands",
    "musician_2_bands",
    "common_bands"
  ],
  "additionalProperties": false
}
