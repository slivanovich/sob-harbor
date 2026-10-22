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
Titmouse, Inc.: Titmouse, Inc. is an American animation studio that develops and produces animated television programming, feature films, music videos, title sequences, commercials and short films.  The studio opened in 2000, and has offices in Los Angeles, New York City and Vancouver.  Some of their productions include "Motorcity" for Disney XD, "Metalocalypse", "China, IL", "Superjail! " and "Black Dynamite" for Adult Swim.

Metalocalypse: Metalocalypse is an American adult animated television series, created by Brendon Small and Tommy Blacha, which premiered on August 6, 2006, and concluded on October 27, 2013 on Adult Swim.  The television program centers on the larger than life melodic death metal band Dethklok, and often portrays dark and macabre content, including such subjects as violence, death, and the drawbacks of fame, with hyperbolic black comedy.  The show is widely heralded as both a parody and a pastiche of heavy metal culture.

Heavy metal guitar: Heavy metal guitar (or simply metal guitar) is the use of highly-amplified electric guitar in heavy metal.  Heavy metal guitar playing is rooted in the guitar playing styles developed in 1960s-era blues rock and psychedelic rock, and it uses a massive sound, characterized by highly amplified distortion, extended guitar solos and overall loudness.  The electric guitar and the sonic power that it projects through amplification has historically been the key element in heavy metal.  The heavy metal guitar sound comes from a combined use of high volumes and heavy distortion.

Massacration: Massacration is a Brazilian satirical heavy metal band, self-proclaimed "greatest and most classic heavy metal band, the inspiration behind most heavy bands since 1985, whose members' hairdos and posing influenced the whole heavy metal culture".  The classical line-up consists of Detonator (vocal, Bruno Sutter), Blondie Hammet (lead guitar, Fausto Fanti), Metal Avenger (bass guitar, Marco Antônio Alves), Jimmy "The Hammer" (drums, Felipe Torres) and Headmaster (rhythm guitar, Adriano Pereira).

South African heavy metal: South African heavy metal has its roots in South African hard rock and heavy metal bands in the 1980s.  Through the late 1980s and the early 1990s South Africa grew a well supported metal scene.  Particular scenes developed in Cape Town, Johannesburg and Pretoria.  South African heavy metal has been particularly influenced by foreign bands, particularly the New Wave of American heavy metal and American thrash metal.

Heavy metal music: Heavy metal (or simply metal) is a genre of rock music that developed in the late 1960s and early 1970s, largely in the United Kingdom.  With roots in blues rock and psychedelic/acid rock, the bands that created heavy metal developed a thick, massive sound, characterized by highly amplified distortion, extended guitar solos, emphatic beats, and overall loudness.  Heavy metal lyrics and performance styles are sometimes associated with aggression and machismo.

Mac Sabbath: Mac Sabbath is an American parody heavy metal tribute band formed in Los Angeles, California in 2014.  The self-appointed founders of "Drive Thru Metal", the band is primarily a parody of English heavy metal group Black Sabbath, utilizing lyricism and imagery centered on fast food.

Deena Weinstein: Deena Weinstein (born March 15, 1943) is a professor of sociology at DePaul University whose research focuses on popular culture.  She is particularly well known for her research on heavy metal music, as she has published two books on the genre: "Heavy Metal: A Cultural Sociology" (1991) and "Heavy Metal: The Music and Its Culture" (2009).  Because of her research on heavy metal, Weinstein was featured in the 2005 documentary "" and the later "Metal Evolution".

The Devil of Christmas: "The Devil of Christmas" is a Christmas special of the British dark comedy anthology television programme "Inside No. 9", and the first episode of the third series.  It was first aired on 27 December 2016 on BBC Two.  The episode was directed by Graeme Harper and written by Reece Shearsmith and Steve Pemberton.  Stylistically, it took heavy inspiration from classic 1970s anthology programmes, such as "Beasts", "Thriller", "Tales of the Unexpected" and "Armchair Theatre", and was filmed using authentic equipment.  Pemberton intended the episode to be a recreation of this kind of classic programming, with critics characterising it as a homage, pastiche or loving parody.

The V.I.P.s (band): The V.I.P.s were a British R&B musical ensemble formed in Carlisle, Cumberland, (North West England) in late 1963, out of an earlier outfit known as The Ramrods, who had formed in Carlisle in 1960.  After a change of personnel in April 1967, the band changed their name to "Art", and released the album "Supernatural Fairy Tales".  They also participated to a psychedelic bizarre album called "Featuring The Human Host And The Heavy Metal Kids" by a collective known as Hapshash and the Coloured Coat, formed by Guy Stevens and an influential British graphic design and avant-garde musical partnership between Michael English and Nigel Waymouth.  The musicians involved in that project were Mike Harrison on keys and vocals, Luther Grosvenor on guitars, Greg Ridley on bass and Mike Kellie on drums, as well as performances by Stevens, English and Waymouth.  It was the first time that the term "heavy metal" was ever used in music, even though that album had nothing to do with heavy metal music, being closer to psychedelic music.  That album was published in 1967 on Liberty Records and contained only five songs from two minutes to more than 15 minutes of psychedelic and almost meditative state kind of music.

Question: What kind of show is widely heralded as both a parody and a pastiche of heavy metal culture, and  was developed by Titmouse ,Inc?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "show_name": {
      "type": "string",
      "description": "The name of the television series."
    },
    "show_type": {
      "type": "string",
      "description": "The general classification or kind of the television series."
    },
    "production_studio": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the animation studio that produced the show."
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "cultural_commentary": {
      "type": "object",
      "properties": {
        "description": {
          "type": "string",
          "description": "A description of how the show relates to cultural commentary (e.g., parody, pastiche)."
        },
        "target_culture": {
          "type": "string",
          "description": "The specific culture that the show parodies or pastiches."
        },
        "commentary_types": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Specific types of cultural commentary, such as 'parody' or 'pastiche'."
        }
      },
      "required": [
        "description",
        "target_culture",
        "commentary_types"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "show_name",
    "show_type",
    "production_studio",
    "cultural_commentary"
  ],
  "additionalProperties": false
}
