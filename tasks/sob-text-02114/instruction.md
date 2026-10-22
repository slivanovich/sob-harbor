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
My Love (Mary J. Blige song): "My Love" is a song by American R&B singer Mary J. Blige from her 1992 debut album "What's the 411? " The song was co-written by singer-songwriter Kenny Greene and Dave Hall, who served as the song's original producer.

Kenny Greene: Kenny Greene (January 17, 1969 – October 1, 2001) was an American singer-songwriter who was also a member of the R&B group Intro.

Dave Evans (singer): Dave Evans (born 20 July 1953) is an Australian singer who briefly sang for the hard rock band AC/DC in 1973–1974.

Rockin' in the Parlour: Rockin' in the Parlour is the B-side of the first single issued by hard rock band AC/DC.  The song was released on 22 July 1974 under the Australian record label Albert Productions.  This single is the only commercial recording of the group's first singer Dave Evans.

Reminisce (song): "Reminisce" is a song by American recording artist Mary J. Blige from her debut album, "What's the 411? ".  The song was co-written by Kenny Greene and Dave "Jam" Hall, the song's producer.  The song contains a sample of "Stop, Look, Listen" by American rapper MC Lyte.  It peaked at number fifty-seven on the "Billboard" Hot 100 and number six on the Hot R&B/Hip-Hop Songs chart.  A more uptempo and hip hop-inspired remix of the song, featuring duo Pete Rock & CL Smooth, later appeared on Blige's 1993 remix album of the same name.

List of AC/DC band members: AC/DC are an Australian hard rock band formed by guitarist brothers Angus and Malcolm Young in 1973.  Originally featuring vocalist Dave Evans, bassist Larry Van Kriedt and drummer Colin Burgess, after a number of lineup changes the band settled with Bon Scott on vocals, Mark Evans on bass guitar and Phil Rudd on drums, and released five albums (two limited to Australia) between 1974 and 1977.  Due to continuing clashes with lead guitarist Angus Young, Evans was later fired from the band shortly after the release of "Let There Be Rock", although "musical differences" was the official reason given for his departure.  Cliff Williams was brought in as his replacement.

Can I Sit Next to You, Girl: "Can I Sit Next to You, Girl" is the debut single by Australian hard rock band AC/DC issued on 22 July 1974.  On August 26, 1974, the song peaked at number 50 on the Aria charts and then disappeared.  This version has lead vocals performed by Dave Evans prior to his being replaced by Bon Scott, as well as drums by ex-Masters Apprentices member Colin Burgess and bass guitar by ex-The Easybeats member George Young (older brother of band cofounders Malcolm Young & Angus Young; co-producer).  Originally, AC/DC's first bassist, Larry Van Kriedt, played the bass parts, but George recorded his own over them later.  In 1975, after Scott joined, the group re-wrote and re-recorded the song as the seventh track on their Australia-only album "T.N.T.", released in December 1975 (see 1975 in music), and as the sixth track on the international version of "High Voltage", released in May 1976.  The title of this version of the song removed the comma, becoming "Can I Sit Next To You Girl".

Love No Limit: "Love No Limit" is a song by American recording artist Mary J. Blige.  It was co-written by Kenny Greene and Dave Hall for her debut album, "What's the 411? " (1992), with the latter serving as the song's producer.  Released as the album's fourth and final single, the song became a top five hit, reaching number-five on the R&B singles chart, and peaked at number forty-four on the US "Billboard" Hot 100 chart.

Rabbit (band): Rabbit (originally, The Cherries) were an Australian glam rock band from Newcastle, which formed in 1973 by Jim Porteus on bass guitar, Phil Screen on drums and Mark Tinson on guitar and vocals.  In October 1974 they were joined by Dave Evans (ex-AC/DC) on lead vocals.  The group relocated to Sydney and released two albums, "Rabbit" (1975) and "Too Much Rock n Roll" (1976), before disbanding in late 1977.  Porteus, Screen and Tinson returned to Newcastle where they formed a hard rock band, Heroes, with Peter De Jong on guitar and vocals.  They issued a self-titled album in October 1980 and disbanded in 1982.

Intro (R&amp;B group): Intro is an American R&B trio from Brooklyn, New York City, New York.  The trio consisted of members Jeff Sanders, Clinton "Buddy" Wike and lead singer/songwriter Kenny Greene.  Intro released two albums (for Atlantic Records): 1993's "Intro" and their second album, 1995's "New Life".  The group had a string of US hits in the 1990s.  The hits included the singles "Let Me Be The One", the Stevie Wonder cover "Ribbon in the Sky", "Funny How Time Flies" and their highest charting hit, "Come Inside".  Greene died from complications of AIDS in 2001, which led to the group's disbanding.

Question: Who was an Australian singer, Kenny Greene or Dave Evans?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "australian_singer_name": {
      "type": "string",
      "description": "The name of the person identified as the Australian singer."
    },
    "identified_person_details": {
      "type": "object",
      "description": "Details about the person identified as the Australian singer.",
      "properties": {
        "name": {
          "type": "string"
        },
        "nationality": {
          "type": "string"
        },
        "professions": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "associated_bands": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      },
      "required": [
        "name",
        "nationality",
        "professions",
        "associated_bands"
      ],
      "additionalProperties": false
    },
    "other_person_details": {
      "type": "object",
      "description": "Details about the other person mentioned in the question for comparison.",
      "properties": {
        "name": {
          "type": "string"
        },
        "nationality": {
          "type": "string"
        },
        "professions": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "associated_bands": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      },
      "required": [
        "name",
        "nationality",
        "professions",
        "associated_bands"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "australian_singer_name",
    "identified_person_details",
    "other_person_details"
  ],
  "additionalProperties": false
}
