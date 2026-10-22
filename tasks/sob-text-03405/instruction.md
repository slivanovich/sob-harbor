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
Reckless: My Life as a Pretender: Reckless: My Life as a Pretender is a memoir by the American musician Chrissie Hynde, a member of rock band The Pretenders.  The book was published on September 8, 2015 by Doubleday, New York and London.  In it, Hynde documents her childhood and youth in the Midwest, the founding of The Pretenders, life on the road and interactions with other musicians.

Back on the Chain Gang: "Back on the Chain Gang" is a song written by Chrissie Hynde and originally recorded by her band, the Pretenders, and released as single by Sire Records in September 1982.  The song was also released on "The King of Comedy" soundtrack album in March 1983 and was later included on the Pretenders' next album "Learning to Crawl" in January 1984.

Loose Screw: Loose Screw is the eighth studio album by rock group The Pretenders, and was released in 2002.  It was the first time that the Pretenders had the same credited band line-up (Chrissie Hynde, Martin Chambers, Andy Hobson and Adam Seymour) on three consecutive studio albums.

Last of the Independents: Last of the Independents is the sixth album by rock group The Pretenders, released in 1994.  For this album, the band is officially credited as being Chrissie Hynde (vocals, guitar), Adam Seymour (guitar), Andy Hobson (bass) and Martin Chambers (drums).  However, this line-up only plays together on one track ("All My Dreams"); the rest of the album is performed by Hynde and Seymour in conjunction with a rotating series of musicians on bass and drums.  These musicians include Hobson and Chambers, as well as bassists Andy Rourke, Tom Kelly and David Paton, and drummers Jimmy Copley and J.F.T. Hood.  A few other session musicians also appear, including Ian Stanley, and one-time Pretenders guitarist Robbie McIntosh, who plays alongside Hynde and Seymour on "I'm a Mother".

The Pretenders: The Pretenders are an English-American rock band formed in Hereford, England, in March 1978.  The original band consisted of initiator and main songwriter Chrissie Hynde (lead vocals, rhythm guitar), James Honeyman-Scott (lead guitar, backing vocals, keyboards), Pete Farndon (bass guitar, backing vocals), and Martin Chambers (drums, backing vocals, percussion).  Following the drug-related deaths of Honeyman-Scott and Farndon, the band has experienced numerous subsequent personnel changes, with Hynde as the only consistent member, and Chambers returning after an absence of several years.

Packed!: Packed!  is the fifth album by rock group The Pretenders, released in 1990.  For this album, the only real member of the group is Chrissie Hynde; no other person is pictured anywhere within the album package, and a rotating cast of session musicians (rather than a set band) is used to back Hynde throughout, essentially making this a de facto solo album by Hynde, only using the Pretenders name to satisfy contractual obligations.  However, drummer Blair Cunningham plays on all tracks, though he is not credited as part of the band.

Mike Shinoda: Michael Kenji Shinoda ( , born February 11, 1977) is an American musician, songwriter, record producer and graphic designer.  He co-founded Linkin Park in 1996 and is the band's rhythm guitarist, primary songwriter, keyboardist, producer, and lead vocalist.  Shinoda later created a hip-hop-driven side project, Fort Minor, in 2004.  He served as a producer for tracks and albums by Lupe Fiasco, Styles of Beyond, and The X-Ecutioners.

Martin Chambers: Martin Dale Chambers (born 4 September 1951 in Hereford) is an English musician, who is best known as a founding member and drummer of the rock band the Pretenders.  In addition to playing the drums with the group, Chambers sings backing vocals (lead vocals on the song "Fast or Slow (The Law's the Law)", the B-side of the singles "2000 Miles" and "Show Me", which he also wrote) and plays percussion.  He was part of the original band line-up which also included Chrissie Hynde (vocals/guitar), James Honeyman-Scott (guitar/vocals/keyboards) and Pete Farndon (bass guitar/vocals).  Hynde and Chambers are the only two surviving original members, and he has served two separate tenures with the group.

Chrissie Hynde: Christine Ellen "Chrissie" Hynde (born September 7, 1951) is an American musician who is best known as a founding member of the rock band The Pretenders.

Hymn to Her: "Hymn to Her" is a song that was first released on the Pretenders' 1986 album "Get Close".  It was written by Meg Keene, a high school friend of Pretenders' lead singer Chrissie Hynde.  "Hymn to Her" was released as a single in the UK and reached #8 on the charts.  According to AllMusic critic Matthew Greenwald, the song has remained popular on adult contemporary radio stations.

Question: Were both Mike Shinoda and Chrissie Hynde members of the rock band The Pretenders?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_asked": {
      "type": "string",
      "description": "The original question posed."
    },
    "person_1": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "Name of the first person mentioned in the question."
        },
        "is_pretenders_member": {
          "type": "boolean",
          "description": "True if the person was a member of The Pretenders, false otherwise."
        },
        "known_bands": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "List of bands the person is known to be a member of."
        }
      },
      "required": [
        "name",
        "is_pretenders_member",
        "known_bands"
      ],
      "additionalProperties": false
    },
    "person_2": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "Name of the second person mentioned in the question."
        },
        "is_pretenders_member": {
          "type": "boolean",
          "description": "True if the person was a member of The Pretenders, false otherwise."
        },
        "known_bands": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "List of bands the person is known to be a member of."
        }
      },
      "required": [
        "name",
        "is_pretenders_member",
        "known_bands"
      ],
      "additionalProperties": false
    },
    "both_were_members": {
      "type": "boolean",
      "description": "True if both individuals were members of The Pretenders, false otherwise."
    },
    "final_answer": {
      "type": "boolean",
      "description": "The boolean answer to the question."
    }
  },
  "required": [
    "question_asked",
    "person_1",
    "person_2",
    "both_were_members",
    "final_answer"
  ],
  "additionalProperties": false
}
