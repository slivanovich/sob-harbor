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
Andalucia (album): Andalucia is the fourth studio album by Los Angeles rock band Tito & Tarantula, released in 2002.  The album marked several line-up changes in the band, which had previously consisted of lead singer/rhythm guitarist Tito Larriva, lead guitarist Peter Atanasoff, and drummer Johnny "Vatos" Hernandez.  This album featured the debut of lead guitarist Steven Hufsteter – who had previously played with Larriva in the Cruzados, bassist Io Perry, and keyboardist Marcus Praed.

Pinnacle of Bedlam: Pinnacle of Bedlam is the seventh studio album by American death metal band Suffocation.  It is the band's first full-length record since "Pierced from Within" to not feature Mike Smith (although he makes a guest appearance on the final track), instead the album features returning drummer Dave Culross, making this his only full-length record with Suffocation and his first release overall with the band since 1998's "Despise the Sun".  Track 10, 'Beginning of Sorrow', is a re-recording of the track of the same name from the album "Breeding the Spawn".  It is also the band's last album with longtime guitarist Guy Marchais.

Neal Tiemann: Neal Tiemann (born December 22, 1982 in Dallas, Texas) is an American musician, currently the lead guitarist and songwriter of the rock band the Midwest Kings (MWK), and guitarist for groove metal band DevilDriver.  From 2008 to 2011 he serve as the lead guitarist for David Cook's band The Anthemic.  He spent most of 2009 on the Declaration Tour with Cook and served as the tour's music director.  Tiemann played guitar on Cook's major label debut album "David Cook" (2008) as well as his independently released "Analog Heart" (2006).  He has also played on Burn Halo's 2009 "self-titled album" and Bryan Jewett's album "A Brief Look at the New You".  Tiemann and the rest of The Anthemic worked on Cook's second album, "This Loud Morning" (2011).

This House Is Not for Sale: This House Is Not for Sale is the thirteenth studio album by American rock band Bon Jovi.  It was released on November 4, 2016, by Island Records.  It is their first studio album without former lead guitarist Richie Sambora and the first album to feature the band's new lead guitarist Phil X and it is also the first album where bass guitarist Hugh McDonald is credited as an official member, even though he has played bass for the band since 1994.

Cage the Elephant: Cage the Elephant is an American rock band from Bowling Green, Kentucky, that formed in 2006 and relocated to London, England in 2008 before their first album was released.  The band currently consists of lead vocalist Matt Shultz, rhythm guitarist Brad Shultz, lead guitarist Nick Bockrath, guitarist and keyboardist Matthan Minster, bassist Daniel Tichenor, and drummer Jared Champion.  Lincoln Parish served as the band's lead guitarist from their formation in 2006 until December 2013, when he left on good terms to pursue a career in producing.  The band's first album, "Cage the Elephant", was released in 2008 to much success, spawning several successful radio singles and gained the band a large following in both the United States and the United Kingdom.

Abyssal Throne: Abyssal Throne is an EP by the Canadian technical death metal band Sympathy, released in 2005 on the Norwegian label Momentum Scandinavia.  The EP was released in a strictly limited edition of only 850 with an 8-page, 5-colour booklet with gold print.  The EP features several guest appearances: vocals by Matt Knowles of Royal Anguish on "Insipid", and additional lead guitar work by Dustin Olson, Tim Roth (Into Eternity) and Rob Doherty (Into Eternity).  The EP features an intro and 5 songs, of which 2 are new, "Insipid" and "Ascendency", and 2 are re-recorded versions from "Invocation", "Immolation of the Dragon" and "Occupy".  The last song, "Torn into Enthrallment" is a Suffocation cover from the 1995 album "Pierced from Within".  The cover artwork was designed by Samuel Durling, a reputive Swedish graphic designer.  The EP received good reviews, and the critics considered the Ep an improvement over the style of Arcane Path, being more extreme technical death/black metal.

Suffocation (band): Suffocation is an American death metal band that was formed in 1990 in Centereach, Long Island, New York, United States.  The band comprises vocalist Frank Mullen, lead guitarist Terrance Hobbs, bassist Derek Boyer, rhythm guitarist Charlie Errigo, and drummer Eric Morotti.  Suffocation rose to prominence of death metal and created a blueprint for the genre for the 1990s with their 1991 debut album "Effigy of the Forgotten", and have released seven studio albums since formation.  The band's raw death metal style uses growled vocals with a downtuned guitar sound, fast and complex guitar riffs and drumming, open chord notes, breakdowns, and a sophisticated sense of songwriting.

Hands (metal band): Hands was an American Christian metal band from Fargo, North Dakota.  The band started making music in 2007, with lead vocalist and guitarist Shane Ochsner, lead guitarist Ian Johnson, bass guitarist Chris Schwartz, and drummer Josh Silbernagel.  Jerik Hendrickson became the band's lead guitarist in 2010, but he has since left the band, with Shane Ochsner taking over lead guitar duties.  The band released one extended play, "The Everlasting", independently in 2007.  Their first studio album, "The Sounds of Earth", was released by Oort Records in 2009.  The band signed with Facedown Records, where they released "Creator", a studio album, in 2009.  The third studio album, "Give Me Rest", was released in 2011, also on Facedown Records.  The band reunited in 2017 for Facedown Fest 2017.

Pierced from Within: Pierced from Within is an album released in 1995 by the technical death metal band Suffocation.  "Synthetically Revived" is a re-recording of the song of the same name from the "Human Waste" EP and "Breeding the Spawn" is a re-recording of the title track from the band's previous album.

Tremonti (band): Tremonti is an American heavy metal band founded and fronted by lead vocalist and guitarist Mark Tremonti, best known as the guitarist of the American rock band Creed, and the lead guitarist of American rock band Alter Bridge.  The band also consists of rhythm guitarist Eric Friedman and drummer Garrett Whitlock.  Bassist Wolfgang Van Halen was in the band between 2012 to 2017.  What originally started as a Mark Tremonti solo project evolved into a fully fledged band after the release of the group's first album, "All I Was", in July 2012.  That album featured Tremonti himself playing guitar in addition to lead vocals, and the band was joined by Tremonti's Creed and Alter Bridge bandmate Brian Marshall playing bass on tour until his departure later that year.  He was replaced by Van Halen bassist Wolfgang Van Halen, who contributed to the band's second album, "Cauterize", which was released on June 9, 2015.  The band also has another album, entitled "Dust", in April 2016, serving as a continuation to "Cauterize".

Question: Who is the lead guitarist for band the released the album "Pierced from Within"? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "album_name": {
      "type": "string",
      "description": "The name of the album in question."
    },
    "band": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the band that released the album."
        },
        "genre": {
          "type": "string",
          "description": "The musical genre of the band."
        },
        "lead_guitarist": {
          "type": "string",
          "description": "The name of the lead guitarist for the band."
        }
      },
      "required": [
        "name",
        "genre",
        "lead_guitarist"
      ],
      "additionalProperties": false
    },
    "album_release_year": {
      "type": "integer",
      "description": "The year the album was released."
    }
  },
  "required": [
    "album_name",
    "band",
    "album_release_year"
  ],
  "additionalProperties": false
}
