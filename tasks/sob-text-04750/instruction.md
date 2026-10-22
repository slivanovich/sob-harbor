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
Krom Hendricks: Armien 'Krom' Hendricks was a South African cricketer.  Hendricks, a Cape Malay, was considered the fastest bowler in South Africa in the 1890s.  He suffered from the racial segregation in South Africa throughout his career, particularly in a much publicised prevention of him touring England in 1894.  He instead made gradually reduced appearances in South African domestic cricket.

Holland (album): Holland is the 19th studio album by the American rock group the Beach Boys, released on January 8, 1973.  Self-produced by the band, the album peaked at No. 36 in the US and No. 20 in the UK.  The album is the second of two studio recordings to feature Blondie Chaplin and Ricky Fataar, who joined the band the previous year to record "Carl and the Passions - So Tough" (1972).

Why Fight It?: Why Fight It?  is the sixth and final studio album by Australian rock band Mondo Rock, released in December 1990.  The album includes former Beach Boys drummer Ricky Fataar and American guitarist Waddy Wachtel.  The album peaked at number 92 on the Kent Music Report.

The Flames: The Flames was a musical group from Durban in South Africa.  The band was originally formed in 1963 by guitarist Steve Fataar, bassist Brother Fataar (real name Edries Fataar), drummer George Faber and guitarist Eugene Champion.  However, this line-up would only be together to record a couple of songs.  Ricky Fataar replaced George Faber as the band's drummer around 1964 and Edries Fredericks replaced Eugene Champion as the guitarist.  Baby Duval briefly replaced Edries Fredericks in 1967, although it is unclear whether he was involved in any of the recordings that were released.  Blondie Chaplin then replaced Baby Duval in 1967.  This was to be the line-up from 1967 until their demise as a group in 1970.

Sosatie: Sosatie (pl sosaties) is a traditional South African dish of meat (usually lamb or mutton) cooked on skewers.  The term derives from "sate" ("skewered meat") and "saus" (spicy sauce).  It is of Cape Malay origin, used in Afrikaans, the primary language of the Cape Malays, and the word has gained greater circulation in South Africa.  Marinated, cubed meat (usually lamb) is skewered and braaied (barbecued) shish-kebab style.  Sosatie recipes vary, but commonly the ingredients can include cubes of lamb, beef, chicken, dried apricots, red onions and mixed peppers.

Johnny Lee Schell: Johnny Lee Schell is an American guitarist and songwriter.  In the 1970s, he premiered as a prominent member of a Texas-based southern rock band, Baby.  Since his professional debut, he has played with dozens of well-known recording artists.  His inclusion on albums such as Bonnie Raitt's "Green Light" (1982) and "Nick of Time" (1989) has lent him his bearing in American pop music culture.  Yet, Schell's works had already journeyed from North America to Australia, when he worked with Australian soul singer Renée Geyer on her album "So Lucky" (1981).  As a member of Bonnie Raitt's road band, Schell backed the Australian Geyer while recording "So Lucky" (renamed "Renee Geyer" for international market) at Shangri La studios in Malibu, California.  Other members included Ian McLagan (formerly of The Faces) and drummer/producer extraordinaire Ricky Fataar.

The Rutles: The Rutles ( ) are a rock band known for their visual and aural pastiches and parodies of the Beatles.  This originally fictional band, created by Eric Idle and Neil Innes for 1970s television programming, became an actual group – whilst remaining a parody of the Beatles – which toured and recorded, releasing many songs and albums that included two UK chart hits.

Ricky Fataar: Ricky Fataar (born 5 September 1952) is a South African multi-instrumentalist of Cape Malay descent, who has performed as both a drummer and a guitarist.  He gained fame as an actor in "The Rutles: All You Need Is Cash", a spoof on the actual history of The Beatles in which he also performed as a member of The Rutles.  He is also known for his stint as a member of The Beach Boys.  Fataar may also be recognized for his contributions as a record producer, and has worked on projects scoring music to film and television.

Carl and the Passions – &quot;So Tough&quot;: Carl and the Passions – "So Tough" is the 18th studio album by American rock band the Beach Boys, released on May 15, 1972.  The album is frequently considered a transitional album for the band, with the addition of Blondie Chaplin and Ricky Fataar on guitar and drums, respectively, and long-time member Bruce Johnston departing during its initial sessions.

Bo-Kaap: The Bo-Kaap is an area of Cape Town, South Africa formerly known as the Malay Quarter.  It is a former township, situated on the slopes of Signal Hill above the city centre and is an historical centre of Cape Malay culture in Cape Town.  The Nurul Islam Mosque, established in 1844, is located in the area.

Question: South African multi-instrumentalist of Cape Malay descent, Ricky Fataar, performed in a rock band known for their visual and aural pastiches and parody of what famous band?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "parodied_band_name": {
      "type": "string",
      "description": "The name of the famous band that was parodied."
    },
    "parody_band_name": {
      "type": "string",
      "description": "The name of the rock band known for the parody."
    },
    "ricky_fataar_involvement": {
      "type": "object",
      "properties": {
        "is_member": {
          "type": "boolean",
          "description": "Indicates if Ricky Fataar was a member of the parody band."
        },
        "is_actor": {
          "type": "boolean",
          "description": "Indicates if Ricky Fataar was an actor in the parody's associated production."
        },
        "context_of_involvement": {
          "type": "string",
          "description": "The specific production or context where Ricky Fataar was involved with the parody band."
        }
      },
      "required": [
        "is_member",
        "is_actor",
        "context_of_involvement"
      ],
      "additionalProperties": false
    },
    "parody_characteristics": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of characteristics describing how the parody was executed."
    }
  },
  "required": [
    "parodied_band_name",
    "parody_band_name",
    "ricky_fataar_involvement",
    "parody_characteristics"
  ],
  "additionalProperties": false
}
