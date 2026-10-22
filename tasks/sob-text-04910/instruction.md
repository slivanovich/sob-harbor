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
Dzeko &amp; Torres: Dzeko & Torres is a Canadian production and DJ duo based in Toronto, Ontario, Canada.  Founded around 2008 by teenagers Julian Dzeko and Luis Torres, the duo has released a number of singles in conjunction with labels such as Mixmash Records, Monstercat, and Musical Freedom Records.  They released the EP "Hey" on Dim Mak Records in 2012, and have had airplay on radio stations including Tiesto’s "Club Life", Paul Oakenfold’s "Planet Perfecto", David Guetta's radio show "Radio DJ Mix", and Steve Aoki's BBC Radio 1 "Essential Mix 2012".

Phone Down: "Phone Down" is a song recorded by American DJs Lost Kings and singer Emily Warren.  It was released as a single on October 7, 2016, via Disruptor Records and RCA Records.

The Funk Hunters: The Funk Hunters are a Canadian electronic music act and DJ duo based in Vancouver, British Columbia.  Composed of members Nick Middleton and Duncan Smith, The Funk Hunters are recognized on the international dance scene for their future funk sound, which is a mix of old school soul, disco, funk and classic hip hop, deeply cross-pollinated with contemporary electronic dance music.

New York City (The Chainsmokers song): "New York City" is a song by American DJ duo The Chainsmokers.  It features uncredited vocals from American singer Victoria Zaro.  It is the fifth, and last, single from the duo's first EP "Bouquet EP".  The song peaked at number 25 on the "Billboard" Dance/Electronic Songs chart and number 80 on the 2016 Dance/Electronic Songs year-end chart.

Duck Sauce: Duck Sauce is an American–Canadian DJ duo, formed during 2009 in New York, New York.  The duo consists of American DJ Armand Van Helden and Canadian DJ A-Trak.

Lost Kings: Lost Kings is an American DJ duo consisting of Robert Abisi and Nick Shanholtz, based in Los Angeles.  The duo gained popularity beginning in 2014 through their official remixes for artists such as Imagine Dragons, Krewella, Halsey, Vance Joy, Echosmith, Rihanna, and Tori Kelly, and through their original EDM/progressive house music.  Managed by Disruptor Management, a joint venture at Sony Music Entertainment, they signed to Disruptor Records/RCA Records in October 2016.

Dzeko &amp; Torres discography: Dzeko & Torres is a Canadian DJ duo based in Toronto, Canada.  They released the EP "Hey" on Dim Mak Records in 2012, and have had airplay on radio stations including Tiesto's "Club Life", Paul Oakenfold's "Planet Perfecto", David Guetta's radio show "Radio DJ Mix", and Steve Aoki's BBC Radio 1 "Essential Mix 2012".

Setting Fires (song): "Setting Fires" is a song by American DJ duo The Chainsmokers, released as a promotional single from the duo's second extended play, "Collage" (2016).  It features the vocal collaboration of American electronic music duo XYLØ.  The song was written by Melanie Fontana, Jon Asher and Andrew Taggart.  "Setting Fires" was released on November 4, 2016, through Disruptor Records and Columbia Records.

Queens of Noize: Queens of Noize were a DJ duo based in London, consisting of Mairead Nash and Tabitha Denholm, during their time as a duo they presented for MTV2 and BBC 6 Music and performed at a number of international festivals.

Riley &amp; Durrant: Riley & Durrant are an electronic music production and DJ duo based in Leeds, UK.

Question: Phone Down was a song recorded by an American DJ duo based out of where?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_title": {
      "type": "string",
      "description": "The title of the song."
    },
    "dj_duo_name": {
      "type": "string",
      "description": "The name of the DJ duo that recorded the song."
    },
    "dj_duo_nationality": {
      "type": "string",
      "description": "The nationality of the DJ duo."
    },
    "dj_duo_base_city": {
      "type": "string",
      "description": "The city where the DJ duo is based."
    }
  },
  "required": [
    "song_title",
    "dj_duo_name",
    "dj_duo_nationality",
    "dj_duo_base_city"
  ],
  "additionalProperties": false
}
