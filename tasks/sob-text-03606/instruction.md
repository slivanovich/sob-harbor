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
Too Tough to Die: Too Tough to Die is the eighth studio album by the American punk rock band the Ramones.  It was released on October 1, 1984, and is the first Ramones record to feature Richie Ramone on drums.  With ex-member Tommy Ramone producing, the recording process was similar to that of the band's 1976 debut album, "Ramones".  Likewise, the record's style—both lyrically and compositionally—saw the band returning to their roots.  The photograph on the album cover, which features silhouettes of the band members, resulted from a "lucky accident" after photographer George DuBose's camera malfunctioned.

Commando (book): Commando is the autobiography of guitarist and songwriter Johnny Ramone of the punk rock band The Ramones.  The book was released in 2012 by Linda Ramone, surviving spouse of Johnny Ramone, following the death of Johnny in 2004 from prostate cancer.

Road to Ruin (Ramones album): Road to Ruin is the fourth studio album by American punk rock band the Ramones, released on September 21, 1978, through Sire Records.  It was the first Ramones album to feature new drummer Marky Ramone, who replaced founding member Tommy Ramone.  Tommy left due to lack of album sales and stress while touring; however, he stayed with the band to produce the album with Ed Stasium.  The artwork's concept was designed by Ramones fan Gus MacDonald and later modified by John Holmstrom to include Marky instead of Tommy.

Johnny Ramone: John William Cummings (October 8, 1948 – September 15, 2004), known professionally as Johnny Ramone, was an American guitarist and songwriter, best known for being the guitarist for the punk rock band the Ramones.  He was a founding member of the band, and remained a member throughout the band's entire career.  He died from prostate cancer on September 15, 2004.

Animal Boy: Animal Boy is the ninth studio album released by the American punk band the Ramones through Sire Records on May 19, 1986.  Due to conflicts within the group, the album features less of lead singer Joey Ramone, both in performing and writing, and less of lead guitarist Johnny Ramone.  Bassist Dee Dee Ramone wrote and sang more on this album than previous albums, and Richie Ramone became the first drummer to write songs for the band.  The album spawned four singles, all of which charted on the UK Singles Chart.  In addition to singles, the band promoted their album by making a music video which parodied the benefit concerts Live Aid and Hands Across America.

Pleasant Dreams: Pleasant Dreams is the sixth studio album by American punk rock band the Ramones released on July 20, 1981, through Sire Records.  While the band members wanted Steve Lillywhite to produce, Sire chose Graham Gouldman in an attempt to gain popularity through a well-known recording manager.  The recording process brought about many conflicts between band members, most notably the strife between Joey Ramone and Johnny Ramone, where Johnny began dating one of Joey's ex-girlfriends.  There were also disputes about the overall genre of the album, with Johnny leaning towards hard rock and Joey towards pop music.  Ultimately, the album incorporated a high production value and a variation of tone throughout the album.  "Pleasant Dreams" featured songs such as "We Want the Airwaves", "She's a Sensation", and "Come On Now", strayed from traditional punk rock and took on different styles.

Halfway to Sanity: Halfway to Sanity is the tenth studio album by American punk band the Ramones.  It was released on September 15, 1987 by Sire Records and was produced by Daniel Rey.  Recording sessions began in April 1987 at Intergalactic Studios in New York City, and the band began recording instruments before vocals as a method to learn songs more quickly.  Band members tended to disagree on many things at this time, and Rey described them to be impatient.  The album's front cover was shot by previous Ramones' photographer George DuBose in Chinatown, New York City.  The short lasted session resulted in a dimly lit album cover which guitarist Johnny Ramone said was good because it helped make them look younger.  The band toured around the world following the album's release, but certain show dates were cancelled after drummer Richie Ramone left the band due to financial conflicts with the band.  Clem Burke of Blondie was hired as Elvis Ramone to fill the drummer's spot for two shows, then was replaced the band's ex-member Marky Ramone, and the tour would continue with him.

Subterranean Jungle: Subterranean Jungle is the seventh studio album by the American punk rock band the Ramones, released by Sire Records in February 1983.  The album appealed to a hardcore punk rock style rather than featuring several pop oriented pieces; this is because guitarist Johnny Ramone received more leeway with steering the overall genre with his hard rock influenced riffs.  The recording sessions saw disputes between band members, mainly because many of the band members were dealing with alcohol addiction, or in bassist Dee Dee Ramone's case, cocaine.

Joey Ramone: Jeffrey Ross Hyman (May 19, 1951 – April 15, 2001), known professionally as Joey Ramone, was an American musician and singer-songwriter, lead vocalist of the punk rock band the Ramones.  Joey Ramone's image, voice, and tenure as frontman of the Ramones made him a countercultural icon.

Ramones discography: The Ramones were an American punk rock band from New York City.  Their discography consists of fourteen studio albums, six live albums, twelve compilation albums, seventy-one singles, thirty-two music videos and eleven films.  The band formed in early 1974, and upon signing with Seymour Stein of Sire Records, the Ramones released their self-titled debut album on April 23, 1976.  Despite the recording process only taking a week and being on a budget of $6,400, the album has since become their most accoladed and iconic release. " Leave Home" was the band's follow up album released less than a year later in 1977, also released through Sire.  While it was the first album to chart in the United Kingdom, it did not chart as well in the United States as "Ramones" nor their third record "Rocket to Russia", which was released in late 1977. " Road to Ruin" was the band's fourth studio album, and their first to feature a change in band member line-up, with drummer Marky Ramone replacing Tommy Ramone.

Question: Pleasant Dreams is the sixth studio album by American punk rock band the Ramones released on July 20, 1981, through Sire Records, the recording process brought about many conflicts between band members, most notably the strife between Joey Ramone and John William Cummings (October 8, 1948 – September 15, 2004), known professionally as Johnny Ramone, was an American guitarist and songwriter, best known for being what, for the punk rock band the Ramones?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The professional name of the person."
    },
    "band_name": {
      "type": "string",
      "description": "The name of the band the person is associated with."
    },
    "primary_role": {
      "type": "string",
      "description": "The main role of the person in the band."
    },
    "other_roles": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Other roles or contributions of the person in the band."
    },
    "is_founding_member": {
      "type": "boolean",
      "description": "Indicates if the person was a founding member of the band."
    }
  },
  "required": [
    "person_name",
    "band_name",
    "primary_role",
    "other_roles",
    "is_founding_member"
  ],
  "additionalProperties": false
}
