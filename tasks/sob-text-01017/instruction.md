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
Dave Carter: Dave Carter (August 13, 1952 – July 19, 2002) was an American folk singer-songwriter who described his style as "post-modern mythic American folk music."  He was one half of the duo Dave Carter and Tracy Grammer, who were heralded as the new "voice of modern folk music" in the months before Carter's unexpected death in July 2002.  They were ranked as number one on the year-end list for "Top Artists" on the "Folk Music Radio Airplay Chart" for 2001 and 2002, and their popularity has endured in the years following Carter's death.  Joan Baez who went on tour with the duo in 2002 spoke of Carter's songs in the same terms that she once used to promote a young Bob Dylan:

Rosalie Sorrels: Rosalie Sorrels (June 24, 1933 – June 11, 2017) was an American folk singer-songwriter.  She began her public career as a singer and collector of traditional folksongs in the late 1950s.  During the early 1960s she left her husband and began traveling and performing at music festivals and clubs throughout the United States.  She and her five children traveled across the country as she worked to support her family and establish herself as a performer.  Along the way she made many lifelong friends among the folk and beat scene.  Her career of social activism, storytelling, teaching, learning, songwriting, collecting folk songs, performing, and recording spanned six decades.

Gil Turner: Gil Turner (born Gilbert Strunk; May 6, 1933 – September 23, 1974) was an American folk singer-songwriter, magazine editor, Shakespearean actor, political activist, and for a time, a lay Baptist preacher.  Turner was a prominent figure in the Greenwich Village scene of the early 1960s, where he was master of ceremonies at New York's leading folk music venue, Gerde's Folk City, as well as co-editor of the protest song magazine "Broadside".  He also wrote for "Sing Out! ", the quarterly folk music journal.

Jules Halfant: Jules Halfant (June 23, 1909 in New York City, New York – May 5, 2001 in Berkeley Heights, New Jersey) is an American painter and printmaker.  He is notable as a Federal Art Project (FAP) artist during the Great Depression of the 1930s in both mural and easel categories of the New York Works Progress Administration (WPA).  While in the WPA, he worked alongside such well-known artists as Jackson Pollock, Mark Rothko, Milton Avery and Stuart Davis.  From 1953 to 1988 Jules Halfant was Art Director of Vanguard Records where he designed albums featuring Joan Baez, Tom Paxton, Country Joe and the Fish, Buffy Sainte-Marie and many other musicians.

Tom Paxton: Thomas Richard Paxton (born October 31, 1937) is an American folk singer-songwriter who has had a music career spanning more than fifty years.  In 2009, Paxton received a Grammy Lifetime Achievement Award.  He is noteworthy as a music educator as well as an advocate for folk singers to combine traditional songs with new compositions.

Martha Wainwright: Martha Wainwright (born May 8, 1976) is a Canadian-American folk-rock singer-songwriter.  She is the daughter of American folk singer and actor Loudon Wainwright III and Canadian folk singer-songwriter Kate McGarrigle.  She was raised in a musical family along with her older brother, Rufus Wainwright, in Montreal, Quebec, Canada.

Richard Meyer (folk music): Richard Meyer (September 6, 1952 – May 14th 2012) was an American folk singer-songwriter, writer, painter, and set designer.  Meyer was active in the Greenwich Village folk music scene of the 1980s and 1990s and did much to promote other artists.  As one of the leaders of a musicians cooperative in the Village he handled booking at the SpeakEasy and edited "Fast Folk Musical Magazine" (1986-1997).  Later, he wrote reviews for various media such as "Allmusic".  He also worked extensively as a lighting/scenery designer in theater.

South of Delia: South of Delia is the seventh solo album by American folk singer-songwriter Richard Shindell.  "South of Delia" is a cover album.  Although he himself is sometimes described as a "songwriter's songwriter," covers are not new to Shindell.  In addition to recording a few on his previous solo albums, he was also one third of the folk supergroup / cover band Cry Cry Cry (along with Dar Williams and Lucy Kaplansky).  On "South of Delia", Shindell covers songs from several songwriting legends, including Woody Guthrie and Bob Dylan, as well as some from younger up-and-coming writer/performers, such as Jeffrey Foucault and Josh Ritter.

Fred Neil: Frederick Neil (March 16, 1936 – July 7, 2001) was an American folk singer-songwriter in the 1960s and early 1970s.  He did not achieve commercial success as a performer and is mainly known through other people's recordings of his material – particularly "Everybody's Talkin'", which became a hit for Harry Nilsson after it was used in the film "Midnight Cowboy" in 1969.  Though highly regarded by contemporary folk singers, he was reluctant to tour and spent much of the last 30 years of his life assisting with the preservation of dolphins.

Cliff Eberhardt: Cliff Eberhardt (born January 7, 1954 in Berwyn, Pennsylvania) is an American folk singer-songwriter.  He is a founding member of the Fast Folk Music Cooperative in New York City.  Eberhardt joined Red House Records in 1997 and has recorded five albums for the label, the most recent in 2009, "500 Miles: The Blue Rock Sessions".  In 2011, he released an acoustic album of Doors songs, "All Wood and Doors", with fellow musician James Lee Stanley on Beechwood Recordings.  Also that year, he contributed a cover to "Nod to Bob II", a Red House compilation honoring Bob Dylan on his 70th birthday.

Question: Jules Halfant designed a record for which American folk singer-songwriter?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "designer_information": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person who designed the album."
        },
        "role": {
          "type": "string",
          "description": "The role of the designer at the record company."
        },
        "company": {
          "type": "string",
          "description": "The record company where the designer worked."
        }
      },
      "required": [
        "name",
        "role",
        "company"
      ],
      "additionalProperties": false
    },
    "artist_information": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the artist for whom the album was designed."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the artist."
        },
        "genre": {
          "type": "string",
          "description": "The primary music genre of the artist."
        }
      },
      "required": [
        "name",
        "nationality",
        "genre"
      ],
      "additionalProperties": false
    },
    "album_design_confirmation": {
      "type": "boolean",
      "description": "Indicates whether Jules Halfant designed an album for the identified artist."
    },
    "answer": {
      "type": "string",
      "description": "The name of the American folk singer-songwriter for whom Jules Halfant designed a record."
    }
  },
  "required": [
    "designer_information",
    "artist_information",
    "album_design_confirmation",
    "answer"
  ],
  "additionalProperties": false
}
