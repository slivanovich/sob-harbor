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
Uneven Structure: Uneven Structure is a progressive metal band based in Metz, France (though most members live in either Lyon and Montpellier).  They play a style of post-metal which is heavily influenced by the Swedish extreme metal band Meshuggah.  The band blends polyrhythmic passages and extremely low tunings with a heavily layered production style and ambient soundscapes.  They are often categorized in the djent movement due to the Meshuggah-like guitar tone they often employ.  The band was formed after the split of Longchat, a band which featured Igor Omodei and Benoit Friedrich.

Galactic Cowboys: Galactic Cowboys are an American heavy metal band based in Houston, Texas.  They combined progressive metal with a vocal style influenced by The Beatles and the heavy playing style of thrash bands such as Anthrax.  They have been described as "possibly the most melodic metal band ever to exist in Christian or general markets."  Although the band members are Christians, they did not consider Galactic Cowboys to be a Christian band.

Arcuri Overthrow: Arcuri Overthrow is an Venezuelan experimental metal band based in Valencia, Venezuela.  The band was formed in 2002 in Valencia by the brothers Arcuri: bassist Felipe and drummer Vicente, with the original name Black Rainbow.  It´s the first Venezuelan metal band, only with bass and drums.

Jorge Iacobellis: Jorge Iacobellis (born August 12, 1956) is an Argentine drummer, tour promoter and producer primarily known as the drummer of the thrash metal band Hirax and former drummer of Todos Tus Muertos.  He promoted and produced international bands on tour such as Kreator, Sick of It All, Viper, Ratos de Porão and Testament and assisted in the tour productions with Kiss, Iron Maiden, Machine Head, Jerry Lee Lewis, Motörhead, Exodus, Sepultura, Ramones, Poison, REO Speedwagon, Slayer and L.A. Guns.

Immortal Legacy: Immortal Legacy is the fifth studio album released by thrash metal band Hirax on February 24, 2014.  It is the first since the 1980's to feature a 4-piece band.  It is also the last with Jorge Iacobellis on drums.

Testament (band): Testament is an American thrash metal band from Berkeley, California.  Formed in 1983 under the name Legacy, the band's current lineup comprises guitarists Eric Peterson and Alex Skolnick, lead vocalist Chuck Billy, drummer Gene Hoglan, and bassist Steve Di Giorgio.  In the 34 years since its inception, Testament has had numerous lineup changes, and Peterson has been the only constant member.  Billy replaced former singer Steve Souza (who left the band to join Exodus as the replacement of Paul Baloff) in 1986, prior to the recording of their first studio album, "The Legacy", and has been a member of the band since.  Peterson and Billy are the only band members to appear on every album.

Allegiance (American band): Allegiance was a San Francisco-based straight edge hardcore punk band with a metal influence that existed from April 2002 to February 2008.  The majority of their catalog was released and is still available by popular Bay Area hardcore punk record label Rivalry Records.  Although they were not the first band to use the name “Allegiance,” as there was a black metal band from Sweden, a street punk band from Japan, a metalcore band from England and an Australian thrash metal band with the same name, they were the first notable American band to do so.  Throughout its existence the band played gigs at the local legendary DIY-Punk venue 924 Gilman in Berkeley, California; the band played its first and last shows here.  Allegiance also did countless tours up and down the West Coast, along with a handful of full USA tours and an extensive 5 week tour of Europe.

Per Wiberg: Per Jonas Wiberg (born 8 June 1968 in Borlänge) is the former keyboardist of Swedish progressive death metal band Opeth, and a member of Michael Amott's stoner metal band Spiritual Beggars.  Wiberg toured with Opeth from the 2003 "Deliverance"/"Damnation" tour onward, and joined Opeth officially in 2005.  Wiberg provided backing vocals for Opeth in addition to his keyboard duties.  Before joining Spiritual Beggars he was a member of Death Organ, a band based in Borlänge.  He has also fronted the band Boom Club, of the same area.

Bahimiron: Bahimiron was an American black metal band based in Houston, Texas and Phoenix, Arizona.  It was formed by vocalist and guitarist David "Grimlord" Herrera in 2001, after leaving the death metal band Imprecation in 1993.  Other members of the band included bassist Jenoside and drummer Blaash, who would play in the band from its formation until its dissolution, and second guitarist Luna, who joined Bahimiron in 2013.  The band was best knowm for their second album, "Southern Nihilizm", released in 2008.  After thirteen years of activity, Bahimiron split-up in 2014.

Morbid Angel: Morbid Angel is an American death metal band based in Tampa, Florida formed in 1983 by guitarist and sole remaining original member Trey Azagthoth, original vocalist and bassist Dallas Ward, and original drummer Mike Browning.  Widely considered as one of the most influential bands in the genre and important in the transition of death metal from its thrash metal roots, they were one of the first bands to incorporate guttural vocals, up-tempo blast beats, atonality in guitar playing, multiple tempo changes and dark atmosphere.  They have been described as one of "the most influential and emulated bands in death metal", alongside Cannibal Corpse, and have been cited as an influence by many later bands.  They were also the first death metal band to experience mainstream success in connection with being signed to Giant Records in 1992, heavy rotation of their music videos on MTV, and having the music video for the song "God of Emptiness" shown on an episode of "Beavis and Butt-head".  Their first four albums are considered classics in the genre.

Question: Which metal band based in Berkeley, California was promoted by producer Jorge Iacobellis?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_name": {
      "type": "string",
      "description": "The name of the metal band."
    },
    "band_location": {
      "type": "string",
      "description": "The city and state where the band is based."
    },
    "genre": {
      "type": "string",
      "description": "The primary genre of the band."
    },
    "promoter_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the promoter."
        },
        "role": {
          "type": "string",
          "description": "The role of the individual in relation to the band (e.g., promoter, producer)."
        }
      },
      "required": [
        "name",
        "role"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "band_name",
    "band_location",
    "genre",
    "promoter_details"
  ],
  "additionalProperties": false
}
