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
Vartan Malakian: Vartan Malakian (Armenian: Վարդան Մալաքյան, born February 14, 1947) is an artist and painter.  He is the father of Daron Malakian, guitarist co-founder of System of a Down and Scars on Broadway.  He was born on February 14, 1947 in Mosul, Iraq.

Scars on Broadway (album): Scars on Broadway is the only studio album by Scars on Broadway, a band consisting of System of a Down members Daron Malakian and John Dolmayan.  The album contains fifteen tracks, all written by Malakian.

Scars on Broadway: Scars on Broadway was an American rock band, founded by System of a Down member Daron Malakian.  The band's eponymous debut album was released on July 29, 2008.

Daron Malakian: Daron Vartan Malakian (Armenian: Տարօն/Տարոն Վարդան Մալաքեան, born July 18, 1975) is an Armenian–American singer-songwriter, multi-instrumentalist, and record producer.  He is best known as the guitarist, songwriter and second vocalist of the rock band System of a Down and as the lead vocalist, lead guitarist and songwriter of the band Scars on Broadway.  Like the rest of the Hollywood-based band System of a Down, he is of Armenian ancestry, but he is the only member to have been born in the United States.  Daron Malakian is known for his distinctive playing and is ranked 40th in Loudwire's list of "Top 50 Hard Rock + Metal Guitarists Of All Time" and #11 in MusicRadar's poll, "The 20 Greatest Metal Guitarists Ever".  He is placed 30th in Guitar World's List of The 100 Greatest Heavy Metal Guitarists of All Time.

Rebellion (song): "Rebellion" is a song by American rock band Linkin Park.  The song was originally recorded by the band for their sixth studio album, "The Hunting Party", where it appears as the eighth track on the album.  The song features Armenian-American multi-instrumentalist Daron Malakian from rock band System of a Down, who plays additional guitar on the track.  The track was released as second promotional single from "The Hunting Party" on June 4, 2014 and was later released as the fourth official single from the album on October 13, 2014, and was included on American rock radio.

Lynch the Weirdo: Lynch The Weirdo is the title of the second full-length album by the metal band Bad Acid Trip, released on April 20, 2004.  It was produced by System of a Down member Daron Malakian.

Lonely Day: "Lonely Day" is the second single from the 2005 album "Hypnotize" by Armenian American metal band System of a Down.  It was written by guitarist Daron Malakian, who also provides lead vocals on the track.  The song received a nomination for Best Hard Rock Performance at the 49th Annual Grammy Awards.

Steal This Album!: Steal This Album!  is the third studio album by Armenian American rock band System of a Down, released on November 26, 2002, on American Recordings.  The album was produced by Rick Rubin and Daron Malakian, and reached #15 in the "Billboard" Top 200.

Matthew Tuck: Matthew "Matt" Tuck (born 20 January 1980) is a Welsh musician.  He is the lead vocalist and rhythm guitarist in the Welsh heavy metal band Bullet for My Valentine.  He and the other 3 members of his old band founded "Jeff Killed John" in 1998, but after bassist Nick Crandle left in 2003, the band was renamed to Bullet for My Valentine.  He is also a singer and guitarist in the supergroup AxeWound, which was formed in 2012.  He also plays piano, drums, keyboard, and harmonica.  He did a collaboration with Max Cavalera (Soulfly, Cavalera Conspiracy, ex-Sepultura) and with Apocalyptica in the song "Repressed".

System of a Down: System of a Down, sometimes shortened to System and abbreviated as SOAD, is an Armenian-American heavy metal band from Glendale, California, formed in 1994.  The band currently consists of Serj Tankian (lead vocals, keyboards), Daron Malakian (vocals, guitar), Shavo Odadjian (bass, backing vocals) and John Dolmayan (drums).

Question: Of Matthew Tuck and Daron Malakian, whom is older?

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
        "birth_date": {
          "type": "string",
          "format": "date"
        }
      },
      "required": [
        "name",
        "birth_date"
      ],
      "additionalProperties": false
    },
    "person_2": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "birth_date": {
          "type": "string",
          "format": "date"
        }
      },
      "required": [
        "name",
        "birth_date"
      ],
      "additionalProperties": false
    },
    "older_person_name": {
      "type": "string"
    },
    "age_difference_years": {
      "type": "integer"
    }
  },
  "required": [
    "person_1",
    "person_2",
    "older_person_name",
    "age_difference_years"
  ],
  "additionalProperties": false
}
