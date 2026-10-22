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
Mystery Virgin: "Mystery Virgin" (ミステリー　ヴァージン ) is the debut solo single of Japanese idol Ryosuke Yamada.  It was the singer’s first solo single following his success as a member of the popular Japanese all-male band, Hey!  Say!  JUMP.  The song was produced and written by Vandrythem, Erik Lidbom, and Daichi.  It was first solicited to mainstream radio on November 30, 2012 and was available for digital download on December 26, 2012.  The song was physically released on January 9, 2013.  “Mystery Virgin” was written as the theme song for the fifth season of popular Japanese drama television series, Kindaichi Case Files, which Yamada also played the main role, Hajime Kindaichi.

Cherry Pop: "Cherry Pop" is a song recorded by Romanian recording artist Alexandra Stan for her second studio album "Unlocked" (2014).  It was made available for digital download on 28 May 2015 through Roton as the record's second single.  The track was written by the singer, Lukas Hällgren and Erik Lidbom, while production was handled by the latter two.  "Cherry pop" was recorded in Bucharest, Romania at the Fonogram Studios, with additional engineering being done at Lidbom's Hitfire Production.

Go! Go! Let's Go!: "Go!  Go!  Let's Go!"  is a song recorded and performed by Japanese collective unit E-girls, taken as a single from their fourth studio record "E.G. Crazy" (2017).  The track was released on November 30, 2016 through Rhythm Zone and Avex Music Creative Inc. in three physical formats—two CD's and a DVD bundle—and for digital consumption.  The song was written by Kotake Masato, composed by Lisa Desmond, Erik Lidbom and Maria Marcus, and produced by Exile's Hiro.  It is the final single to feature Dream member Erie Abe, whom left the band on December 31 that same year.

BoA: Kwon Bo-ah (Korean: 권보아 , , Japanese: クォン・ボア, 権宝兒 , born November 5, 1986), commonly stylized and known by her stage name BoA, is a South Korean singer and actress active in South Korea and Japan.

Dance (Alexandra Stan song): "Dance" is a song recorded by Romanian recording artist Alexandra Stan for her sophomore studio album, "Unlocked" (2014).  The track was made available for digital download on 16 July 2014, as the album's third single.  "Dance" was written by Stan, Cosmin Basasteanu, Alexandru Cotoi, Lee Anna McCollum, Mika Moupondo and Erik Lidbom, while production was handled by both Cazan and Lidbom.  A music video for the song was directed by Khaled Mokhtar and debuted on Stan's YouTube channel on 18 July 2014, where it has since amassed over seven million views.  The clip was shot during three days in Bucharest, Romania and sees Stan and her backup dancers performing choreographed dances, which were choreographed by Romanian performer Emil Rengle.

Catch Me If You Can (Girls' Generation song): "Catch Me If You Can" is a song recorded in two languages (Japanese and Korean) by South Korean girl group Girls' Generation.  The Korean version was released by S.M. Entertainment and KT Music on April 10, 2015, while the Japanese version was released on April 22 by EMI and Universal Music Japan.  The song was composed by Erik Lidbom and Jin Choi, with the Korean lyrics written by Mafly and Choe A-Leum, and the Japanese lyrics written by Junji Ishiwatari and Jeff Miyahara.  Musically, it was described by critics as an EDM track.  The song marked the first release of Girls' Generation as an eight-member group following the dismissal of member Jessica Jung in September 2014.

Erik Lidbom: Erik Lidbom (born 1977) is a Swedish songwriter and music producer based in Uppsala, Sweden.  Lidbom has written songs for Asian artists and bands like Arashi, EXILE, Namie Amuro, Kumi Koda, BoA, GFRIEND and miss A.

Unlocked (Alexandra Stan album): Unlocked is the second studio album by Romanian singer and songwriter Alexandra Stan, released on 27 August 2014 by Victor Entertainment.  Stan collaborated with several producers on the record, including Andreas Schuller, Sebastian Jacome, Chrishan Prince, Erik Lidbom and Gabriel Huiban.  She also developed material for the album while attending the first Romanian international songwriting camp FonoCamp in 2013.  "Unlocked" was released following an alleged physical altercation between Stan and her former manager Marcel Prodan, which had led her to take a short hiatus in 2013.  She signed a record deal with the Fonogram Records label to distribute the record in various countries.  The album's music features dance, techno, pop and R&B genres, with influences varying from J-pop and Bhangra to house music.  Lyrically, "Unlocked" deals with themes of liberation and new beginnings.  Music critics gave the album mixed reviews, with them criticizing the originality of the songs.

Yesung: Kim Jong-hoon (born Kim Jong-woon on August 24, 1984), better known by his stage name Yesung, is a South Korean singer and actor.  He debuted in 2005 as a member of Super Junior and its subgroups Super Junior-K.R.Y. (2006), Super Junior-H (2008) and participated in S.M. Entertainment's projects S.M.  The Ballad (2014).  Aside from group activities, he has recorded songs for various television dramas and movies, participated in various television dramas, movies, musical and also being radio hosting.

Kim Tae-yeon: Kim Tae-yeon (born March 9, 1989), referred to as Taeyeon, is a South Korean singer.  She had been a trainee at S.M. Entertainment's Starlight Academy during her middle school years before debuting as a member of the agency's girl group, Girls' Generation, in 2007.  Since then, she has risen to prominence due to the group's success on the Asian music scene and further participated in the agency's projects Girls' Generation-TTS and SM the Ballad.  Aside from group activities, she has also recorded songs for various television dramas and movies.

Question: Which South Korean singer and actress has recorded songs written by Erik Lidbom?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "artist_identified": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The stage name of the artist."
        },
        "full_name": {
          "type": "string",
          "description": "The full name of the artist."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the artist."
        },
        "professions": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of the artist's professions."
        }
      },
      "required": [
        "name",
        "full_name",
        "nationality",
        "professions"
      ],
      "additionalProperties": false
    },
    "songwriter_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the songwriter."
        },
        "contribution_type": {
          "type": "string",
          "description": "How the songwriter contributed to the artist's songs."
        }
      },
      "required": [
        "name",
        "contribution_type"
      ],
      "additionalProperties": false
    },
    "final_answer": {
      "type": "string",
      "description": "The name of the South Korean singer and actress who recorded songs written by Erik Lidbom."
    }
  },
  "required": [
    "artist_identified",
    "songwriter_details",
    "final_answer"
  ],
  "additionalProperties": false
}
