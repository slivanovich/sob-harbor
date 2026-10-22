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
Trick Pony: Trick Pony is an American country music group, formed in 1996 by Heidi Newfield (lead vocals, acoustic guitar, harmonica), Keith Burns (lead guitar, vocals), and Ira Dean (bass guitar, upright bass, vocals).  They recorded three studio albums: "Trick Pony", "On a Mission", and "R.I.D.E.", released in 2001, 2002, and 2005.  These albums produced eight singles on the "Billboard" Hot Country Songs chart, including four Top 20 hits: "Pour Me", "On a Night like This", "Just What I Do", and "On a Mission".

Billion Dollar Gravy: Billion Dollar Gravy is a drum n bass album by London Elektricity released in 2003.  The album is known for its usage of live musicians, such as the Jungle Drummer (drums), Liane Carroll (jazz vocals), Andy Waterworth (upright bass), Robert Owens (vocals), and others, much like London Elektricity's debut, "Pull the Plug".

Per Mathisen: Per Mathisen (born 7 October 1969 in Sandefjord, Norway) is a Norwegian jazz musician (upright bass and guitar bass) and composer, known from collaborations with great jazz musicians like Terri Lyne Carrington, Geri Allen, Gary Thomas, Bill Bruford, Alex Acuña, Gary Husband, Ralph Peterson, Nguyen Le and Terje Rypdal.  He is married to pianist Olga Konkova, and the brother of jazz musicians Hans Mathisen (guitar), Nils Mathisen (keyboards, guitar and violin) and Ole Mathisen (saxophone and clarinet).

Willie Dixon: William James "Willie" Dixon (July 1, 1915January 29, 1992) was an American blues musician, vocalist, songwriter, arranger and record producer.  He was proficient in playing both the upright bass and the guitar and was a capable singer, but he is perhaps best known as one of the most prolific songwriters of his time.  Next to Muddy Waters, Dixon is recognized as the most influential person in shaping the post–World War II sound of the Chicago blues.

Oytun Ersan: Oytun Ersan (born June 22, 1978) is a Turkish Cypriot electric bass and upright bass player, composer and recording artist.  He has collaborated with a wide variety of artists including Dave Weckl, Eric Marienthal, Gary Husband, Gerry Etkins, Mike Miller, Brett Garsed, Dean Brown, Okan Ersan, Karen Briggs, Prof. Rex Richardson, Wycliffe Gordon, Çağrı Sertel, Thomas Wolff, Savvas Savva, Tony Jones, Ola Onabule, Lloyd Chisholm, Paul Roos and Andrey Alpatov.  He is an official artist endorser for some top profile companies like Fodera Guitars (USA), MarkBass (IT) and Gruv Gear (USA).  In May 2015, he released his first Jazz Fusion album entitled "East Meets West" as seen in "Bass Musician Magazine" and "All About Jazz".  His second Jazz Fusion album <nowiki>"Fusiolicious"</nowiki> will be released in early 2017 which gathers some of the most influential Jazz musicians in the world including Dave Weckl, Eric Marienthal, Gary Husband, Gerry Etkins, Dean Brown, Mike Miller, Brett Garsed, Karen Briggs and Okan Ersan.  In addition to his production support, Mixing and Mastering of the album is carried out by Ric Fierabracci.  Oytun Ersan has performed at various international festivals and venues till date.

Harold Ashby: Harold Ashby (March 21, 1925 in Kansas City, Missouri – June 13, 2003 in New York City) was an American jazz tenor saxophonist.  He worked with Duke Ellington's band, having replaced Jimmy Hamilton in 1968.  In 1959, he recorded backing Willie Dixon on the latter's debut album, "Willie's Blues".

Brian Bromberg: Brian Bromberg (born December 5, 1960) is an American jazz bassist and record producer who performs on both electric and acoustic instruments.  Though he tends to gravitate towards the genre of smooth jazz, Bromberg has released some straight-ahead jazz records in which he performs with a trio, and has even ventured into more rock-oriented jazz fusion territory as of late.  His innovative and technically demanding style of playing extends to both electric and upright bass.  On his acoustic bass albums, Bromberg performs jazzy interpretations of various pop and rock staples from the 1960s and '70s completely solo.  Regarding his work with electric bass, Bromberg, among other bassists, helped popularize the piccolo bass, or bass with each string tuned an octave up, by releasing several albums in which he plays both the bass line and melody.  For instance, upon first listen many will be surprised to learn that, although soaring guitar can be heard throughout the album, Bromberg's 2005 release "Metal" contains only Bromberg on two overdubbed basses, one of which is heavily effects-laden to make it sound like an electric guitar.

John Jorgenson: John R. Jorgenson (born July 6, 1956) is an American musician.  Although best known for his guitar work with bands such as the Desert Rose Band and The Hellecasters, he is also proficient on the mandolin, mandocello, Dobro, pedal steel guitar, piano, upright bass, clarinet, bassoon, and saxophone.  While a member of the Desert Rose Band, he won the Academy of Country Music's "Guitarist of the Year" award two consecutive years.

Arsen Roulette: Arsen Sheklian, better known by his stage name Arsen Roulette, (born July 23, 1976) is an American singer, lyricist, guitar player and upright bass player from Fresno, California.  Roulette is a prolific songwriter penning more than 100 songs in the Rockabilly Genre, a mixture of Rock and Roll, Blues and American Hillbilly music.  In 1996 Arsen discovered Rocabilly music and in 1997 Arsen formed the rockabilly trio "Arsen Roulette and the Ricochets", the bands rotating members were a veritable whose who of neo-rockabilly giants.  After several name changes and a successful U.S. tour, the trio grew into a quartet of semi-permanent musicians, mainly European Rock-A-Billy musicians who play full-time in other bands of this genre.  Arsen Roulette makes bi-annual pilgrimages to Europe, frequently headlining Europe's biggest Rockabilly events; Summer Jamboree, Hemsby, Screamin' Festival and the Brighton Rumble just to name a few.

Mathias Eick: Mathias Eick (born 26 June 1979) is a Norwegian jazz musician, and the brother of the jazz musicians Johannes Eick and Trude Eick.  He is mainly known from his releases on the jazz label ECM Records.  His main instrument is the trumpet, but he also plays upright bass, vibraphone, piano and guitar.  He has performed with several well-known music groups and musicians, e.g. Jaga Jazzist, Manu Katché, and "Trondheim Jazz Orchestra" together with Chick Corea and Pat Metheny.  Besides this he is also known for his collaboration with Norwegian singer-songwriter Thomas Dybdahl, and recordings with the Norwegian bands Turboneger, DumDum Boys, Motorpsycho, D'Sound and Bigbang.

Question: Harold Ashby  recorded backing what famous musicians debut album proficient in playing both the upright bass and the guitar?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "musician_name": {
      "type": "string",
      "description": "The name of the musician whose debut album was backed."
    },
    "debut_album_title": {
      "type": "string",
      "description": "The title of the debut album."
    },
    "backing_musician": {
      "type": "string",
      "description": "The name of the musician who provided backing on the debut album."
    },
    "instrument_proficiencies": {
      "type": "array",
      "description": "A list of instruments the musician is proficient in.",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "musician_name",
    "debut_album_title",
    "backing_musician",
    "instrument_proficiencies"
  ],
  "additionalProperties": false
}
