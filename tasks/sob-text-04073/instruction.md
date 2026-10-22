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
Pop Life (Prince song): "Pop Life" is a 1985 song by Prince and The Revolution.  It was the second US (and final UK) single from their 1985 album, "Around the World in a Day", reaching number 7 in the US charts.  The song starts with a faded-in synth line and quickly starts the main tune.  The easy groove is achieved with a smooth bass guitar and piano embellishments.  A drum machine provides handclaps to make the song danceable.  "Pop Life" was recorded before "Purple Rain" was completed, indicating the new direction Prince wanted to take after the success of that album and film.  Drums on the song were played by Sheila E. in tandem with Prince's then-drummer Bobby Z., bass was played by Brownmark, keyboards were played by Matt Fink and Wendy & Lisa provide backing vocals in addition to guitar and keyboards respectively, Jonathan Melvoin played tambourine and the rest of the song was performed by Prince.

Jonathan Melvoin: Jonathan Melvoin (December 6, 1961 – July 12, 1996) was an American musician active in the 1980s and 1990s.

Susannah Melvoin: Susannah Melvoin (born January 26, 1964) is an American vocalist and songwriter, best known for her association with Prince in the mid-1980s.  Coming from a musical family, Melvoin is the twin sister of musician Wendy Melvoin, sister of Jonathan Melvoin (touring keyboardist with The Smashing Pumpkins), and daughter of jazz pianist (and former NARAS president) Michael Melvoin.

Flavour of the Old School: '"Flavour of the Old School"' is a song by British R&B recording artist Beverley Knight, released as her debut single from her debut "The B-Funk" (1995).  The track, which peaked at number fifty on the UK Singles Chart when it was released in March 1995, was accompanied by a low budget music video that saw Knight in the recording studio singing directly into the camera.  It was re-released however in October 1995, supported by a new video and strong support from urban radio.  The song went on to become Knight's first top 40 single, peaking at number thirty-three in the official UK Singles Chart.  The song later reappeared on the b-side of Knight's 1999 single "Made it Back".  The video is frequently shown in rotation on MTV Base.

Sign o' the Times (song): "Sign o' the Times" is the lead single from American musician Prince's 1987 album of the same name.  Despite being negative in nature, the song was originally intended for two separate Prince albums meant to be released in 1986, that were both shelved: "Dream Factory" and "Crystal Ball".  (Many of the tracks from both of these albums ended up on the album "Sign o' the Times".)  Prince sings and performs the entire track all by himself; however this was one of the songs where he removed the other band member's contributions.  In this case Susannah Melvoin's.  "Sign o' the Times" was reportedly written and composed on a Sunday, when Prince usually wrote his most introspective songs.

Dennis Flemion: Dennis Flemion (June 6, 1955 – July 7, 2012) was a founding member, with his younger brother Jimmy, of controversial independent rock band The Frogs.  He was the primary percussionist for the band.  Dennis was also a temporary member of The Smashing Pumpkins from 1996 to 1997, filling in on live keyboards following the death of Jonathan Melvoin.

Angel (Sarah McLachlan song): "Angel" is a song by Canadian singer-songwriter Sarah McLachlan about the heroin overdose death of Jonathan Melvoin (1961-1996), the Smashing Pumpkins touring keyboard player.  as McLachlan explained on "VH1 Storytellers".  The song first appeared on "Surfacing", the Canadian singer's 1997 album.  It is sometimes mistitled as "In the Arms of an Angel" or "Arms of the Angel".

Could I Have This Dance: "Could I Have This Dance" is a song recorded by Canadian country music artist Anne Murray.  "Could I Have This Dance" was featured in the 1980 film "Urban Cowboy" and appeared on both the soundtrack album for that film, as well as on Murray's "Greatest Hits" compilation, issued in late 1980.  It was released in August 1980 and became Anne Murray's fifth number one country hit as a solo artist.  The single went to number one for one week and spent a total of ten weeks on the country chart.  "Could I Have This Dance" was also Anne Murray's tenth Top 40 on the U.S. pop singles chart, hit peaking at number thirty-three.  The song was written by Wayland Holyfield and Bob House.

Hit by Love: "Hit by Love" is a 1994 song by the musician CeCe Peniston, released as the fourth single from her album record "Thought 'Ya Knew", and the fifth number one hit in the "Billboard" Hot Dance Music/Club Play for the artist.  The song, issued in Europe with "I'm Not Over You" on B-side, climbed in the UK Top 75 chart to number thirty-three and number ninety in the Hot 100 chart.

Thirty-Three (song): "Thirty-Three" is a song by American alternative rock band The Smashing Pumpkins.  It was the fifth and final single from their third album, "Mellon Collie and the Infinite Sadness".  It was also the first single released after the firing of Jimmy Chamberlin and death of Jonathan Melvoin.  The song peaked at 39 on the "Billboard" Hot 100 in late 1996.

Question: What nationality are Jonathan Melvoin and artist that sings the song "Thirty-Three"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "entities": {
      "type": "array",
      "description": "List of entities whose nationality is being queried.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "Name of the entity."
          },
          "type": {
            "type": "string",
            "description": "Type of entity (e.g., 'person', 'band')."
          }
        },
        "required": [
          "name",
          "type"
        ],
        "additionalProperties": false
      }
    },
    "shared_nationality": {
      "type": "string",
      "description": "The common nationality of all specified entities."
    },
    "nationality_source": {
      "type": "string",
      "description": "The source of the nationality information in the context."
    }
  },
  "required": [
    "entities",
    "shared_nationality",
    "nationality_source"
  ],
  "additionalProperties": false
}
