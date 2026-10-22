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
Face the Music (EP): Face the Music: The EP (also known as Face the Music) is the title of the second extended play released by Canadian pop-rock group Marianas Trench.  Featuring popular songs from the group's most recent album, "Ever After" (2011), the EP marks Marianas Trench's first official US music release.  It was first released May 10, 2013 in New Zealand before being released in North America later that month, and was distributed through 604 Records, Cherrytree Records, and Interscope Records.

Something Old / Something New: Something Old / Something New is the third extended play recorded by Canadian rock group Marianas Trench, released May 26, 2015 through 604 Records, Cherrytree Records, and Interscope Records.  It contains two songs originally recorded for the band's fourth studio album, "Astoria" (2015), and two tracks that pre-date the recording of their debut studio album, "Fix Me" (2006), from their Self-Titled EP "Marianas Trench" (2002).  The EP was released in promotion of "Astoria" and serves as a "thank you" to their fans.

Fallout (song): "Fallout" is a song recorded by Canadian pop punk band Marianas Trench for their third studio album, "Ever After" (2011).  It was released November 14, 2011 as the album's second single.  The song has peaked in the Top 40 on the "Billboard" Canadian Hot 100 and been certified Gold by Music Canada.  In October 2016, "Fallout" was certified Double Platinum.

Never Say Die Tour (Marianas Trench tour): The Never Say Die Tour (Marianas Trench) is a Canadian concert tour by Canadian pop-rock band Marianas Trench (band) in support of their album "Astoria (Marianas Trench album)".

Marianas Trench (band): Marianas Trench is a Canadian pop punk band from Vancouver, British Columbia, formed in 2001.  The band consists of members Josh Ramsay (lead vocalist, rhythm guitarist, pianist, songwriter, and occasional drummer), Matt Webb (lead guitarist and backing vocalist), Mike Ayley (bass guitarist and backing vocalist), and Ian Casselman (drummer, percussionist, and backing vocalist).  The band has released four full-length studio albums, the most recent titled "Astoria", released on October 23, 2015, along with 2011's "Ever After", 2009's "Masterpiece Theatre" and 2006's "Fix Me".  Their third album "Ever After" was nominated for a Juno Award.

Haven't Had Enough: "Haven't Had Enough" is a song recorded by Canadian pop punk band Marianas Trench for their third studio album, "Ever After" (2011).  It was released July 19, 2011 as the album's lead single.  The song debuted at #9 on the Canadian Hot 100 and was certified Platinum by Music Canada in December 2011; it was later certified 2× Platinum in October 2016.

Poe (singer): Poe (born Anne Decatur Danielewski) is an American singer, songwriter, and record producer.  Poe's musical style is a blend of rock, jazz, electronica, folk, and hip hop elements combined with intimate lyrical compositions.  Many of Poe's songs have been featured in films and on television.  Poe first hit the modern rock charts in 1995.

Marianas Trench discography: The discography of Marianas Trench, a Canadian pop rock band, consists of four studio albums, three extended plays, 18 singles and 18 music videos.  The band recorded and released their debut EP in 2002, entitled "Marianas Trench" containing 8 tracks.

Astoria (Marianas Trench album): Astoria is the fourth studio album recorded by Canadian rock band Marianas Trench.  It was released on October 23, 2015 through 604 Records (in Canada) and Cherrytree Records and Interscope Records (internationally).  The album represents the band's official return to the music scene after promotion of their previous album, "Ever After" (2011), ended in 2013, and was preceded by the retrospective EP, "Something Old / Something New" earlier in 2015.

Pop 101: "Pop 101" (stylized as "POP 101") is a song recorded by Canadian pop rock band Marianas Trench, featuring hip hop artist Anami Vice.  Written and produced by lead singer Josh Ramsay, it was released July 29, 2014 through 604 Records, Cherrytree Records, and Interscope Records.  Originally announced as the lead single off the band's forthcoming fourth studio album, "Astoria" (2015), the song was later scrapped from the album and serves only as a buzz single; it is also included on their 2015 extended play, "Something Old / Something New".  "Pop 101" entered the Canadian Hot 100 at No. 27, and was certified Gold by Music Canada in November 2014.

Question: Do the Canadian band Marianas Trench and the American singer Poe have different music styles?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_name": {
      "type": "string",
      "description": "The name of the Canadian band."
    },
    "band_origin_country": {
      "type": "string",
      "description": "The country of origin for the Canadian band."
    },
    "band_music_styles": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of music styles associated with the Canadian band."
    },
    "singer_name": {
      "type": "string",
      "description": "The name of the American singer."
    },
    "singer_origin_country": {
      "type": "string",
      "description": "The country of origin for the American singer."
    },
    "singer_music_styles": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of music styles associated with the American singer."
    },
    "are_styles_different": {
      "type": "boolean",
      "description": "True if the music styles of the band and the singer are different, false otherwise."
    }
  },
  "required": [
    "band_name",
    "band_origin_country",
    "band_music_styles",
    "singer_name",
    "singer_origin_country",
    "singer_music_styles",
    "are_styles_different"
  ],
  "additionalProperties": false
}
