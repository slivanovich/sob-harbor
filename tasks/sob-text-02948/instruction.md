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
John Glascock: John Glascock (2 May 1951 – 17 November 1979) was the bass guitarist, backing vocalist, and occasional lead vocalist for the progressive rock band Carmen.  He was also the bass guitarist and backing vocalist for the progressive rock band Jethro Tull from December 1975 until August 1979.  He died in 1979, at the age of 28, as a result of a congenital heart valve defect, which was worsened by an infection caused by an abscessed tooth.

Avenged Sevenfold: Avenged Sevenfold (sometimes abbreviated as A7X) is an American heavy metal band from Huntington Beach, California, formed in 1999.  The band's current lineup consists of lead vocalist M. Shadows, rhythm guitarist and backing vocalist Zacky Vengeance, lead guitarist and backing vocalist Synyster Gates, bassist and backing vocalist Johnny Christ, and drummer Brooks Wackerman.

The Twang: The Twang are an English indie rock band, formed in 2004 in Birmingham.  The band have released four studio albums - "Love It When I Feel Like This" (2007), "Jewellery Quarter" (2009), "" (2012) and "NEONTWANG" (2014) Comprising vocalist and guitarist Phil Etheridge, bassist Jon Watkin, vocalist Martin Saunders, guitarist Stu Hartland and drummer Matty Clinton, the band garnered national acclaim when the influential NME magazine produced an article on music acts in the West Midlands.  Former touring-member Barry Fratelli is also a member of the Scottish band The Fratellis.

Sum 41: Sum 41 is a Canadian rock band from Ajax, Ontario.  Originally called Kaspir, the band formed in 1996 and currently consists of lead vocalist/rhythm guitarist/keyboardist Deryck Whibley, lead guitarist/backing vocalist Dave Baksh, rhythm/lead guitarist/keyboardist/backing vocalist Tom Thacker, bassist/backing vocalist Jason McCaslin and drummer Frank Zummo.

The Fratellis: The Fratellis are a Scottish rock band from Glasgow, formed in 2005.  The band consists of lead vocalist and guitarist Jon Fratelli (born John Lawler), bass guitarist Barry Fratelli (born Barry Wallace), and drummer and backing vocalist Mince Fratelli (born Gordon McRory).  Their singles "Chelsea Dagger" and "Whistle for the Choir" were both top ten hits in the UK charts.

The All-American Rejects: The All-American Rejects is an American rock band formed in Stillwater, Oklahoma in 1999.  The band consists of lead guitarist and backing vocalist Nick Wheeler, lead vocalist and bassist Tyson Ritter, rhythm guitarist and backing vocalist Mike Kennerty, and drummer Chris Gaylor.  Nick Wheeler and Tyson Ritter are the band's songwriters; Wheeler is the primary composer and Ritter is the main lyricist.

A Heady Tale: "A Heady Tale" is the third single by Scottish rock band, The Fratellis from their second album, "Here We Stand".  It was released on 22 December 2008.  This song is 1 of the 4 tracks on "Here We Stand" to have a heavy use of piano (the other 3 being "Mistress Mabel", "Milk And Money" & "Moriaty's Last Stand").  The B-sides "Mon Yous, Mon us but no' Them" and "When All the Lights Go Out" were also piano intensive.  Jon Fratelli has said that the B-Side "Lonesome Anti Christmas Blues" is the "most depressing Christmas song written".

Marianas Trench (band): Marianas Trench is a Canadian pop punk band from Vancouver, British Columbia, formed in 2001.  The band consists of members Josh Ramsay (lead vocalist, rhythm guitarist, pianist, songwriter, and occasional drummer), Matt Webb (lead guitarist and backing vocalist), Mike Ayley (bass guitarist and backing vocalist), and Ian Casselman (drummer, percussionist, and backing vocalist).  The band has released four full-length studio albums, the most recent titled "Astoria", released on October 23, 2015, along with 2011's "Ever After", 2009's "Masterpiece Theatre" and 2006's "Fix Me".  Their third album "Ever After" was nominated for a Juno Award.

Gnarwolves: Gnarwolves are a British melodic hardcore band, formed in 2011 and based in Brighton, England.  The band consists of lead vocalist and guitarist Thom Weeks, bass guitarist and backing vocalist Charlie Piper, and drummer Max Weeks.

Chelsea Dagger: "Chelsea Dagger" is a song by Scottish rock band The Fratellis.  It was released as the second single from their debut studio album, "Costello Music" (2006), on 28 August 2006.  It is named after Jon Fratelli's wife Heather, a burlesque dancer whose stage name – a play on Britney Spears – he borrowed for the song.  Fratelli described the tune as "a rock 'n' roll gig in an old speakeasy or something like that."

Question: What band  consists of lead vocalist and guitarist Jon Fratelli , bass guitarist Barry Fratelli , and drummer and backing vocalist Mince Fratelli that released their third single from their second album "Here We Stand", released on 22 December 2008? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_name": {
      "type": "string",
      "description": "The name of the band."
    },
    "members": {
      "type": "array",
      "description": "A list of the band members and their roles.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the band member."
          },
          "roles": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "The roles of the band member within the band."
          }
        },
        "required": [
          "name",
          "roles"
        ],
        "additionalProperties": false
      }
    },
    "single_release_details": {
      "type": "object",
      "description": "Details about the specified single release.",
      "properties": {
        "single_title": {
          "type": "string",
          "description": "The title of the single."
        },
        "album_title": {
          "type": "string",
          "description": "The title of the album the single is from."
        },
        "release_date": {
          "type": "string",
          "description": "The release date of the single."
        },
        "single_number_on_album": {
          "type": "integer",
          "description": "The sequential number of the single from the album."
        }
      },
      "required": [
        "single_title",
        "album_title",
        "release_date",
        "single_number_on_album"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "band_name",
    "members",
    "single_release_details"
  ],
  "additionalProperties": false
}
