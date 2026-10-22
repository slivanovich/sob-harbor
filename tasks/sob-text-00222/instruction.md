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
Jaycen Joshua: Jaycen Joshua is a mix engineer who works at Larrabee Sound Studios in North Hollywood, California.  Joshua started his mix career in 2006 when he became partners with his mentor Dave Pensado and formed The Penua Project.  Joshua has won multiple Grammys and mixed many Grammy Award winning records such as "Single Ladies (Put a Ring on It)" by Beyoncé and "Blame It" by Jamie Foxx, as well as over 60 #1 singles and albums.  Joshua has worked with Mariah Carey, Justin Timberlake, Sean Combs, Jay-Z, Chris Brown, Miley Cyrus, Christina Aguilera, Mary J. Blige, Rihanna, R. Kelly, Celine Dion, J-Lo, T.I., Usher, Michael Jackson, Nicki Minaj, Katy Perry, Snoop Dogg, Justin Bieber, Seal, Nas, Chris Brown and Whitney Houston.  Joshua is managed by Terry Ross for Innersound Management, LLC.

Prince (musician): Prince Rogers Nelson (June 7, 1958 – April 21, 2016) was an American singer-songwriter, multi-instrumentalist, and record producer.  He was a musical innovator who was known for his eclectic work, flamboyant stage presence, extravagant dress and makeup, and wide vocal range.  His music integrates a wide variety of styles, including funk, rock, R&B, new wave, soul, psychedelia, and pop.  He has sold over 100 million records worldwide, making him one of the best-selling music artists of all time.  He won seven Grammy Awards, an American Music Award, a Golden Globe Award, and an Academy Award for the film "Purple Rain".  He was inducted into the Rock and Roll Hall of Fame in 2004, his first year of eligibility.

Circo (band): Circo is a band from Puerto Rico which formed in 2001.  Its members are Jose Luis "Fofé" Abreu (vocals), Edgardo "Egui" Santiago (keyboards), José David Pérez (drums, vibes), Nicolás Cordero (bass)(Nico is no longer with the band), and Orlando Méndez (guitar).  The band was nominated for Rock New Artist at the 16th Lo Nuestro Awards, losing to Mexican singer Alessandra Rosaldo.  They also have been nominated for various Latin Grammy Awards in Latin Grammy Awards of 2002,Latin Grammy Awards of 2005 and Latin Grammy Awards of 2008.

Juan Luis Guerra: Juan Luis Guerra Seijas (born June 7, 1957), known professionally as Juan Luis Guerra, is a Dominican singer, songwriter, composer, and producer.  He has sold over 30 million records, and has won numerous awards including 18 Latin Grammy Awards, two Grammy Awards, and two Latin Billboard Music Awards.  Guerra won 3 Latin Grammy Awards in 2010, including Album of the Year.  In 2012, he won the Latin Grammy Award for Producer of the Year.

Grammy Award for Best Concept Music Video: The Grammy Award for Best Concept Music Video was an award that was presented to recording artists at the 30th Grammy Awards in 1988, and the 31st Grammy Awards in 1989, for quality, concept music videos.  The Grammy Awards (Grammys) is an annual ceremony that was established in 1958 and was originally called the Gramophone Awards; awards are presented by the National Academy of Recording Arts and Sciences of the United States to "honor artistic achievement, technical proficiency and overall excellence in the recording industry, without regard to album sales or chart position".

Anotherloverholenyohead: "Anotherloverholenyohead" is a 1986 song by Prince and The Revolution, from the album "Parade", the soundtrack to the film "Under the Cherry Moon".  The song is essentially a full band performance by Prince & the Revolution, with backing vocals from Susannah Melvoin, and the horn section of Eric Leeds and Atlanta Bliss.  The song also features a string arrangement by Clare Fischer.  The song is set in a minor key, and written around a piano chord sequence, although the arrangement emphasizes an upfront guitar synth and a drum machine.  The lyrics are about a man trying to reclaim a lover who is intent on leaving him for another.  The song's title is a combination of the main idea of the song, and the line "U need another lover like u need a hole in yo head" from the chorus.  The single received a 12" extended release with intricate piano work and some dance commands from Prince.

Gordon Goodwin's Big Phat Band: Gordon Goodwin's Big Phat Band, or simply The Big Phat Band, is an 18-piece jazz orchestra that combines the big band swing of the 1930s and 1940s with contemporary music such as funk and jazz fusion.  The band is led by Gordon Goodwin, who arranges, composes, plays piano and saxophone.  Since its origin, the Big Phat Band has received several Grammy Awards and many Grammy nominations.

Paul Epworth: Paul Richard Epworth (born 25 July 1974 in Bishop's Stortford, Hertfordshire) is an English music producer, musician, and songwriter.  His production and writing credits include Adele, Rihanna, and Maxïmo Park amongst many others.  On 12 February 2012 at the 54th Grammy Awards, Epworth won four Grammy Awards for Producer of the Year, Album of the Year (Adele's "21"), and Song of the Year and Record of the Year (for "Rolling in the Deep").  He won the Academy Award for Best Original Song alongside Adele, for "Skyfall".  His sister Mary Epworth is a singer and songwriter.  He is a member of the Music Producers Guild.  He also has a record label, Wolf Tone, whose artists include Glass Animals, Rosie Lowe and Plaitum.  He has won 'Producer of the Year' at the BRIT Awards three times, the most recent in 2015.  At the 59th Grammy Awards in 2017, Epworth won a Grammy for Album of the Year for his work on Adele's 25".

Charles Chalmers: Charles Chalmers is a saxophonist, session musician, backup singer, songwriter and producer.  He has written several hit songs for many recording artists, and has also arranged & performed on many grammy winning recordings.  Seven of those recordings are in the Grammy Hall of Fame : Al Green's "Let's Stay together"; Aretha Franklin's "Respect," "Chain of Fools" & "Natural Woman"; Dusty Springfield's "Son of a Preacher Man"; and Wilson Pickett's "Mustang Sally" and "Land of a Thousand Dances."  He also holds an Album of the Century award for his work on Aretha Franklin's, "I Ain't Never Loved a Man the Way that I Love You."

Robert Glasper: Robert Glasper (born April 6, 1978, in Houston, Texas) is an American pianist and record producer.  He has been nominated for 6 Grammys, has won 3 Grammy Awards and is currently nominated for an Emmy Award.  His 2012 album "Black Radio" won the Grammy Award for Best R&B Album at the 55th Grammy Awards.  His 2014 album "Black Radio 2" won the Grammy Award for Best Traditional R&B Performance at the 56th Grammy Awards.  The song "These Walls" from Kendrick Lamar's album "To Pimp A Butterfly" won Best Rap/Sung Collaboration at the 57th Grammy Awards, on which Glasper plays keys.  The soundtrack for the film "Miles Ahead" won Best Soundtrack Compilation at the 58th Grammy Awards, for which Glasper was a producer.  The song "Letter To The Free", written with Common, is nominated for an Emmy Award for Best Original Song in the Ava Duvernay documentary film "13th" (Netflix) at the 2017 Emmys.

Question: How many Grammy Awards have been won by the singer of "Anotherloverholenyohead"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "entity_type": {
      "type": "string",
      "description": "The type of entity being queried (e.g., musician, band)."
    },
    "entity_name": {
      "type": "string",
      "description": "The name of the entity who won the awards."
    },
    "song_associated": {
      "type": "string",
      "description": "The title of the song mentioned in the question that is associated with the entity."
    },
    "award_type": {
      "type": "string",
      "description": "The type of award being counted."
    },
    "award_count": {
      "type": "integer",
      "description": "The total number of awards won by the entity."
    }
  },
  "required": [
    "entity_type",
    "entity_name",
    "song_associated",
    "award_type",
    "award_count"
  ],
  "additionalProperties": false
}
