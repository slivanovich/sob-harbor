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
Failure (band): Failure is an American alternative rock band from Los Angeles that was active from 1990 to 1997 and from 2014 onwards.  They are often compared to other alternative rock bands from that time that were similarly labeled as "alternative", such as Nirvana and Soundgarden, but are distinguished by their meticulous attention to textural sonic detail, inventive use of guitar effects and signal processing, and the overall expansive sound design of their later albums.  Failure reunited in 2014.

Silver Sail: Silver Sail, released in 1993, is the seventh studio album by punk rock band Wipers and the first since their reunion.  After disbanding Wipers in 1989 and releasing a 1991 solo album, "Sacrifice (For Love)", Sage decided to release a new album under the Wipers name.  The album was written, produced and recorded by Sage at his own Zeno Studios in Phoenix, Arizona.  It was released by the Tim/Kerr label in the U.S. and by Gift of Life in Germany.

The Rats (American band): The Rats were an American garage punk band from Portland, Oregon, formed by Fred Cole previously of the garage rock band, The Lollipop Shoppe.  Cole played guitar and sang, his wife, "Toody" played bass and sang, and initially Rod Rat played drums.  Their sound was a raw mix of punk rock with occasional country touches.  Their self-titled debut album appeared on Cole's Whizeagle label in 1980.  Soon after, Rod Rat left the band, though he guested on the 1981 follow-up "Intermittent Signals" before his death by suicide.  (Prior to his suicide Rod Rat (aka Rod Hibbert) also played drums in 1980-81 for Portland power pop band Domino Theory).  Sam Henry, formerly of the Wipers, played drums on this LP but left to join another Portland band, Napalm Beach.  Louis Samora was on the drum throne for the 1983 album "In a Desperate Red", still on Whizeagle.  Samora left in 1984 to concentrate on his rockabilly band, The Jackals.  The band broke up, but Bill Barker of Profile Studios in Vancouver, British Columbia convinced the band to reunite for a single.  It appeared under the band name The Desperate Edge later in 1984.  Soon after, Cole assembled a country band, Western Front, and he and Toody later reunited in Dead Moon.  The Rats' records have long been out of print and sell for high prices on eBay.  In 2008, Portland's Mississippi Records reissued the first album on vinyl.

Wipers: The Wipers were a punk rock group formed in Portland, Oregon in 1977 by guitarist Greg Sage, along with drummer Sam Henry and bassist Dave Koupal.  The group's tight song structure and use of heavy distortion were hailed as extremely influential by numerous critics and musicians.  The band is considered the first Pacific Northwest punk band.

Kris Crummett: Kris Crummett is an American record producer and owner of the Interlace Audio, in Portland, Oregon.  Kris started recording in 2002.  He has worked with many notable indie music record labels, including Rise Records, Epitaph Records, Fearless Records, Sumerian Records, Equal Vision Records, and many more.  He is best known for his work with bands such as Sleeping With Sirens, Issues, Dance Gavin Dance, Drop Dead, Gorgeous and Alesana.  He is also currently a member of the Portland, Oregon band The Crash Engine.

O (gesture): The "O" is a gesture used predominantly at the University of Oregon (UO) in Eugene, Oregon, United States, and at events in which the school's athletic teams, the Oregon Ducks, are taking part.  The gesture, in which the forefinger and thumb of each hand are pressed together to form an "O" shape, is used to show support for the team.  First used by University of Oregon band directors as a cue to indicate the song to be played, it gained its current meaning after a photograph of quarterback Joey Harrington appeared on the front page of "The Oregonian" making the "O" sign with his hands.

Napalm Beach: Napalm Beach is an American punk rock band from Portland, Oregon.  One of the longest-running punk bands in the U.S., they are credited by some as being early innovators of the grunge sound.  Nicholas Pell, writing for the "Portland Mercury" said "a huge influence on the grunge and alternative rock of the 1990s, Napalm Beach never had the name recognition of other Portland bands like Poison Idea or the Wipers."  Napalm Beach shared the stage with bands such as X, Public Image Ltd., Joan Jett, Johnny Thunders, Gun Club, Bad Brains, Soundgarden, Screaming Trees, Mudhoney, Dead Moon, and Poison Idea.  They also toured Germany five times between 1989 and 1992.  During their long musical career they have released more than 30 studio and live recordings in various formats on a number of small independent labels in the U.S. and Germany.

Wipers Live: Wipers is a self-titled live album by punk rock band Wipers, recorded between February and March 1984 and released in 1985 by Enigma Records.  It had previously been issued by the band's own Trap Records as a cassette-only release titled "Wipers Tour 84".  It was later reissued as "Wipers" by Restless and band leader Greg Sage's Zeno Records.

The Range Rats: In 1986, following the breakup of the Portland, Oregon band Western Front, guitarist/vocalist Fred Cole and his wife Toody (bass/vocals) formed "The Range Rats", which continued Western Front's mix of punk rock and country music.  Drummer Andrew Loomis auditioned for The Range Rats but it didn't work out, so Fred and Toody enlisted a drum machine and began touring Oregon mining towns.  They recorded an unreleased album, but on the way back from a Reno vacation in 1987, Cole decided he wanted to return to the rock 'n' roll he had played in bands such as The Lollipop Shoppe and The Rats.  A second audition with Loomis worked out, and Dead Moon began.  Songs by The Range Rats wound up in the Dead Moon documentary "Unknown Passage", and the song "Go My Way" was rerecorded for Dead Moon's "Dead Ahead" album.

Maria Catherine Callahan: Maria Catherine Callahan (born June 22, 1965) is an American singer-songwriter from Portland, Oregon.  In the 1990s Callahan was lead vocalist, guitarist and co-songwriter for the critically acclaimed power pop Portland, Oregon band, Doris Daze.  Doris Daze released two albums, "Uncle" (1994) and "Perpetual Happiness Machine" (1997) before disbanding in 1999.

Question: Wipers and Failure have similarities to what Portland, Oregon band? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_name": {
      "type": "string",
      "description": "The name of the Portland, Oregon band that shares similarities with Wipers and Failure."
    },
    "location": {
      "type": "string",
      "description": "The city and state where the band is from."
    },
    "genres": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of genres associated with the band, including those that show similarity to Wipers or Failure."
    },
    "similarity_to_wipers_description": {
      "type": "string",
      "description": "A description of the similarities between this band and Wipers, based on the context."
    },
    "similarity_to_failure_description": {
      "type": "string",
      "description": "A description of the similarities between this band and Failure, based on the context."
    }
  },
  "required": [
    "band_name",
    "location",
    "genres",
    "similarity_to_wipers_description",
    "similarity_to_failure_description"
  ],
  "additionalProperties": false
}
