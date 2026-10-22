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
Catfish and the Bottlemen: Catfish and the Bottlemen are a British rock band, formed in Llandudno, Wales in 2007.  Their debut album, "The Balcony", reached number 10 in the UK Albums Chart and achieved Platinum status on 30 December 2016.  The band have toured in South America, Japan, UK, Europe, North America, and Australia and have featured in a number of festivals including Lollapalooza, Glastonbury, Latitude, Community festival, Reading and Leeds, T in the Park, Governors Ball and Bonnaroo.  They won a Brit Award for British Breakthrough act on 24 February 2016.  On 27 May 2016, they released their second album, "The Ride".

Catfish (Four Tops song): "Catfish" is a 1976 soul song by the Four Tops.  Released as a single on ABC Records, it was the title track of the album of the same name.  The track features a disco sound reminiscent of contemporary musical groups.  In the United States, "Catfish" reached 71 on the "Billboard" Hot 100 pop singles chart and number 7 on the R&B singles chart.  By the release of "Catfish" in 1976, the Four Tops popularity had begun to decline.

Billy Bibby &amp; The Wry Smiles: Billy Bibby & The Wry Smiles are a British indie rock band formed in the autumn of 2015 in the area around Llandudno, North Wales and Chester, UK.  The band is fronted by Billy Bibby, former lead guitarist and founding member of Catfish and the Bottlemen.  Bibby parted ways with Catfish and the Bottlemen in the summer of 2014, shortly after co-writing and recording their Platinum selling debut album, "The Balcony".  Soon thereafter, Billy Bibby began writing songs and playing acoustic shows in various UK cities in order to test public response to his new music.  In the spring of 2015, Billy Bibby began seeking musicians to form a new band.  Auditions were conducted with the help of Simon Jones, formerly of The Verve.  Band members Rob Jones (lead guitar), Matt Bassy (bass), and Michael Pearce (drums) were selected to form the four-piece ensemble.

Collective Soul (2009 album): Collective Soul, also known as Rabbit to differentiate it from the band's 1995 album of the same name, is the eighth studio album by American rock band Collective Soul.  It was released on August 25, 2009.

Joey Huffman: Joey Huffman (born August 4, 1962) is an American musician.  Primarily known as a keyboard and organ player, Huffman has performed with many artists, both in the studio and live.  He was a member of Witness, Drivin' N Cryin', and the Georgia Satellites.  Joey has recorded on over 125 records as a musician and producer/engineer during his career including Bowling for Soup's "A Hangover You Don't Deserve", Skinny Molly's "Here For A Good Time", Miranda Lambert' "Kerosene", Soul Asylum's "Let Your Dim Light Shine", "After the Flood: Live from Grand Forks Prom", "Black Gold: The Best of Soul Asylum" and "Silver Lining", Meat Puppets' "No Joke", Matchbox Twenty's "Live From Down Under" DVD, Butch Walker's "Letters", Cee-lo Green's "Cee-Lo Green and His Perfect Imperfections", Collective Soul's "Youth", Izzy Stradlin's "Miami", Blackberry Smoke's "New Honky Tonk Bootlegs" to name a few.  He has also toured with Isaac Hayes (1989) Michelle Malone and Drag the River (1990-1991), The Georgia Satellites (1992-2004), Drivin N Cryin (1994-2006), Izzy Stradlin, (1993), Matchbox Twenty (1998), Soul Asylum (1993–1997).  in 2008, he performed live with Lynyrd Skynyrd, filling-in for Billy Powell.  He is currently a member of Hank Williams, Jr.'s touring band.

Catfish Haven: Catfish Haven is an indie soul rock band from Chicago.  Their music was described by "Onion AV" writer Kyle Ryan in 2006 as "Creedence Clearwater Revival meets Nirvana".  Ryan goes on in the same article to explain that "Because [Catfish Haven] grew up playing punk, they mostly avoid acoustic-rock conventions by channeling punk’s aggression and intensity.  Few similar bands match the racket Catfish Haven makes, but few bands mix elements of folk, country, rock, and punk so well."

Collective Soul: Collective Soul is an American rock band originally from Stockbridge, Georgia.  Now based in Atlanta, the group consists of lead vocalist Ed Roland, rhythm guitarist Dean Roland, bassist Will Turpin, drummer Johnny Rabb and lead guitarist Jesse Triplett.

Collective Soul 2013 Tour: The Collective Soul 2013 Tour was a concert tour by American rock band Collective Soul.

Collective Soul (1995 album): Collective Soul (sometimes referred to as the Blue Album to differentiate from the second self-titled album) is the second and eponymous studio album by Collective Soul.  It became the band's highest selling album to date, going Triple-Platinum, and spent 76 weeks on the "Billboard" 200 charts.  The singles "December," "The World I Know" and "Where the River Flows" all reached #1 on the Mainstream Rock Tracks chart, while the first two singles also became major pop hits.

Smashing Young Man: "Smashing Young Man" is a song by the American band Collective Soul.  It is the third single from their second studio album "Collective Soul".  The song was written as an insult to Smashing Pumpkins lead singer, Billy Corgan, who accused Collective Soul of plagiarizing music.

Question: Collective Soul and Catfish and the Bottlemen are both what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_names": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Names of the bands being compared."
    },
    "common_genre": {
      "type": "string",
      "description": "The musical genre that both bands belong to."
    },
    "is_musical_group": {
      "type": "boolean",
      "description": "Indicates if both entities are musical groups."
    }
  },
  "required": [
    "band_names",
    "common_genre",
    "is_musical_group"
  ],
  "additionalProperties": false
}
