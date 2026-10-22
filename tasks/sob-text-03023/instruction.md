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
All Systems Go (Vinnie Vincent Invasion album): All Systems Go is the second and final studio album by American glam metal band Vinnie Vincent Invasion, released on May 17, 1988.  "All Systems Go" featured new vocalist Mark Slaughter, who replaced Robert Fleischman.  The band toured in support for the album, headlining small clubs, but broke up after the completion of the tour at the end of August 1988.  The album features Yngwie Malmsteen's vocalist Jeff Scott Soto on backing vocals.

Angelfish (album): Angelfish is the 1994 self-titled debut and only studio album released by Scottish alternative rock group Angelfish, fronted by Shirley Manson.  The "Angelfish" album was born out of necessity when Goodbye Mr. Mackenzie's record distributor MCA expressed interest in recording an album with Manson on lead vocals rather than furthering its commitment to the Mackenzies.  The Mackenzies' record label boss Gary Kurfirst signed Manson as a solo artist, with the remaining Mackenzies performing as her backing band to circumvent the band's existing deal with MCA.

Not Your Kind of People: Not Your Kind of People is the fifth studio album by American-Scottish alternative rock band Garbage.  It was released on May 11, 2012 through the band's own record label, Stunvolume.  The album marks the return of the band after a seven-year hiatus that started with previous album "Bleed Like Me".  Guitarist Duke Erikson said at the launch of the record that "working with Garbage again was very instinctual.  Like getting on a bicycle...with three other people."  The band emphasized that they did not want to reinvent themselves, but embrace their sonic identity, reflecting their classic sound whilst updating it for 2012.  Although Shirley Manson's morose dispositions have a presence on the record, many of the songs share a more optimistic outlook on life, influenced by some of Manson's personal experiences during their hiatus.

Slaughter (band): Slaughter is an American rock band formed in Las Vegas, Nevada by lead vocalist/rhythm guitarist Mark Slaughter and bassist Dana Strum.  The band reached stardom in 1990 with their first album "Stick It to Ya", which spawned several hit singles including "Up All Night", "Spend My Life", "Mad About You" and "Fly to the Angels".  The album reached double platinum status in the United States.  The band remains a steady act in national tours, mainly in the Rock Never Stops Tour which features several bands of the same era.

Abel Axe: The Abel Axe is an electric guitar invented by Jeff Abel from Wyoming, United States and engineered by James Jones.  Made from aircraft grade T-6 Billet aluminum, its distinguishing features are the various sized holes dotting the body.  All Abel Axes are made in the United States.  Abel Axe has won the Emerging Manufacturer Award in the 1999 Annual Manufacturing Awards Ceremony.  Mark Slaughter, leader of the band Slaughter, owned an Abel Axe.

Shirley Manson: Shirley Ann Manson (born 26 August 1966) is a Scottish singer, songwriter and actress.  She is the lead vocalist of the alternative rock band Garbage.  For much of her international career Manson commuted between her home city of Edinburgh and the United States to record with Garbage; she now lives and works in Los Angeles.  Manson gained media attention for her forthright style, rebellious attitude and distinctive voice.

Queer (song): "Queer" is a song written and produced by alternative rock band Garbage for the band's self-titled debut album.  The song started as a demo during sessions between band members Butch Vig, Duke Erikson and Steve Marker, and had its composition finished after singer Shirley Manson joined the band.  Manson rewrote the sexualized lyrics to be more ambiguous, and rearranged the song into a subdued trip hop and rock crossover structure.

Up All Night (Slaughter song): "Up All Night" is a song by American hard rock band Slaughter.  Written by band members Mark Slaughter and Dana Strum, it was the third title on the band's debut album, "Stick It to Ya", and the band's first single.  It is their second most popular song, according to Last.fm.  It was released in 1990.

Dana Strum: Dana Strum (born Dana Strumwasser on December 13, 1958 in Washington, DC) is the bassist of glam metal band Slaughter.  Before that, he was in Vinnie Vincent Invasion together with future Slaughter bandmate, Mark Slaughter.  He was raised in Southern California's San Fernando Valley and began his performing career in the band Badaxe, playing regularly at the infamous Starwood along with Quiet Riot, Mötley Crüe, and others.

Mark Slaughter: Mark Allen Slaughter (born July 4, 1964) is an American singer and musician.  He is one of the founders of the hard rock band Slaughter, and he has also worked as a voice actor and composer.

Question: Shirley Manson and Mark Slaughter, have which mutual occupation?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_1": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "roles": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      },
      "required": [
        "name",
        "roles"
      ],
      "additionalProperties": false
    },
    "person_2": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "roles": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      },
      "required": [
        "name",
        "roles"
      ],
      "additionalProperties": false
    },
    "mutual_occupation": {
      "type": "string"
    }
  },
  "required": [
    "person_1",
    "person_2",
    "mutual_occupation"
  ],
  "additionalProperties": false
}
