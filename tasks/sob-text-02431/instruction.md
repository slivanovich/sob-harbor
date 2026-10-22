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
Kevin Foley (drummer): Kevin Foley (born March 10, 1988 in France) is a French drummer of Irish-Italian descent.  He has played with bands including Decapitated, Sepultura, Sabaton (band), Abbath, Disavowed, Benighted and Mumakil.

Sabaton discography: Sabaton is a power metal band from Falun, Sweden.  As of May 2014, they have released seven studio albums, including "Carolus Rex", which was recorded in separate Swedish and English versions, certified gold in Poland and platinum in Sweden with 40,000 album sales, making it the "most successful Swedish heavy metal album ever" according to the band.

Sabaton (band): Sabaton [ˈsæbəˌtɑn] is a Swedish heavy metal band from Falun.  The band's main lyrical themes are based on war and historical battles—the name is a reference to a sabaton, knight's foot armor.  The armor and battle theme is heard in the albums "The Art of War", "Coat of Arms", "Carolus Rex", "Heroes", and "The Last Stand" in which all of the songs contain these motifs, except final tracks which are tribute songs to influential heavy metal bands.  Lyrical content drawn from World War I, World War II and other historical conflicts is prevalent and lyrics often recite stories of heroic deeds by men and armies.  In April 2012, guitarists Oskar Montelius and Rikard Sundén, drummer Daniel Mullback, and keyboardist Daniel Mÿhr left the band to form Civil War.  Lead vocalist Joakim Brodén and bassist Pär Sundström continued with new members, with Brodén on keyboards.

Andi Kravljaca: Andi Kravljaca is a Bosnian-born Swedish heavy metal singer.  His main band is the progressive metal band Aeon Zen, although he is perhaps best known as vocalist for Swedish progressive metal band, Seventh Wonder, appearing on the band's first album, Become, in 2005.  He was born in Sarajevo.

Syron Vanes: Syron Vanes is a Swedish heavy metal band formed in 1980 in Arlöv, Sweden.  Originally assembled by former Drummer Staffan Lindstedt and guitarist Anders Hahne they are a big part of the early Swedish heavy metal scene.  "We just wanted to be rock stars Anders Hahne recalls"

Sami Karppinen: Sami Kristian Karppinen is a Finnish drummer.  He is a former drummer of Swedish heavy metal band Therion (1998–2001) and Finnish industrial metal band Ruoska (2002-2008), sound engineer and producer in Modern Art Studio, and session drummer.  He has been working as drum tech for Therion, after he left the band.

Infestissumam: Infestissumam (Latin superlative adjective meaning "very or most hostile", used by the band as "the most hostile" or "the biggest threat" in reference to the Antichrist) is the second full-length album by the Swedish heavy metal band Ghost.  It was recorded in Nashville, Tennessee, produced by Nick Raskulinecz and released on April 10, 2013.  It was released in North America by Loma Vista Recordings on April 16 in partnership with Republic Records, a division of Universal Music Group, marking the band's major label debut.  The album was generally well-received, with several music publications placing it on their list of the best heavy metal albums of the year, and won the 2014 Grammis Award for Best Hard Rock/Metal Album.  In late 2013, the band released a special edition of the album, called "Infestissumam Redux".

Meliora (album): Meliora (Latin for "the pursuit of something better") is the third full-length album by Swedish heavy metal band Ghost.  The album was produced by Klas Åhlund and released on August 21, 2015.  The album was generally well received, placing on several music publications' lists of the best heavy metal albums of the year and winning Best Hard Rock/Metal Album at the 2015 Grammis Awards.  Lead single "Cirice" won the 2016 Grammy Award for Best Metal Performance.  In September 2016, the band released a special edition of the album, called "Meliora Redux".

Heavy Load (band): Heavy Load was a Swedish heavy metal band from Stockholm.  The band is often hailed as the first Swedish heavy metal band, and were known for their Viking themes.  The Wahlquist brothers, who founded the band in 1976 along with Michael Backler, were later producers and owners of Thunderload Records in Sweden, were at one point producing Veni Domine, and also were considering releasing a new album, though that never occurred.  Misfortune struck when Thunderload Studios got severely damaged due to a water leakage in the 2000s, which meant a halt to its official existence.  After the breakup, the members then went on and performed with other bands.

Schlager Metal: Schlager Metal is a 1998 album by Swedish heavy metal band Black Ingvars.  On the album, they cover Melodifestivalen songs in heavy metal version.  However, the first song, "Cherie", was their own and they performed it at the Swedish Melodifestivalen 1998, where it finished fifth.

Question: Who is a Swedish heavy metal band from Falun, that had a French drummer of Irish-Italian play with them?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_name": {
      "type": "string",
      "description": "The name of the heavy metal band."
    },
    "band_origin_city": {
      "type": "string",
      "description": "The city where the band is from."
    },
    "band_origin_country": {
      "type": "string",
      "description": "The country where the band is from."
    },
    "band_genre": {
      "type": "string",
      "description": "The genre of the band."
    },
    "drummer_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the drummer."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the drummer."
        },
        "descent": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "The ethnic descent of the drummer."
        }
      },
      "required": [
        "name",
        "nationality",
        "descent"
      ],
      "additionalProperties": false
    },
    "relationship": {
      "type": "string",
      "description": "Description of the relationship between the drummer and the band."
    }
  },
  "required": [
    "band_name",
    "band_origin_city",
    "band_origin_country",
    "band_genre",
    "drummer_details",
    "relationship"
  ],
  "additionalProperties": false
}
