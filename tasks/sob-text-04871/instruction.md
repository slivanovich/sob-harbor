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
Bellini discography: The discography of Bellini, a German pop girl group, consists of two studio albums, one compilation album, 11 singles, including 1 as featured artist, 2 promotional singles and 11 music videos.  The first Bellini release was the debut studio album "Samba de Janeiro" in 1997, preceded by the massive chart hit of the same name "Samba de Janeiro", which heavily samples Airto Moreira's 1972 song "Tombo In 7/4" from his album "Fingers", also released in 1997.  This release was followed with the compilation album "Samba de Janeiro - Non-Stop Best of Bellini" and the sophomore studio album "Festival" in 2001 and 2014.

Young Divas discography: The discography of Young Divas, an Australian pop girl group, consists of two studio albums, one compilation album, four singles, two album appearances and four music videos.  The group was formed in 2006 by Sony BMG Australia which included previous "Australian Idol" contestants Ricki-Lee Coulter, Paulini, Kate DeAraugo and Emily Williams.  Young Divas released their self-titled debut album in November 2006, which debuted at number four on the ARIA Albums Chart and was certified double platinum by the Australian Recording Industry Association (ARIA), for shipments of 140,000 copies.  A cover of Donna Summer's "This Time I Know It's for Real" was released as the album's lead single and peaked at number two on the ARIA Singles Chart.  The song was certified platinum by the ARIA, for shipments of 70,000 copies.  The second single was a cover of Lonnie Gordon's "Happenin' All Over Again", which peaked at number nine and was certified gold for shipments of 35,000 copies.  A cover of Hazell Dean's "Searchin'" was released as the third and final single from the album, and peaked at number 40.

Muse discography: The discography of Muse, an English rock band, consists of seven studio albums, two live albums, one compilation album, five extended plays (EPs), 38 singles, two video albums, 52 music videos and four other appearances.  Formed in Teignmouth, Devon in 1994, the band signed with Mushroom Records in the United Kingdom and Maverick Records in the United States before releasing their debut album "Showbiz" in 1999.  The album was a success across Europe, and in the UK reached number 29 on the UK Albums Chart, as well as being certified platinum by the British Phonographic Industry (BPI).  Five singles were released from "Showbiz", with final release "Unintended" the band's first to reach the top 20 on the UK Singles Chart.  Muse released their second album "Origin of Symmetry" in 2001, which reached number 3 on the UK Albums Chart and was certified double platinum by the BPI.  The album's first three singles, "Plug In Baby", "New Born" and "Bliss", all reached the UK top 25.

Taio Cruz discography: The discography of Taio Cruz, a British singer, songwriter and record producer, consists of three studio albums, one compilation album, one live album, one extended play, twenty singles (including six as a featured artist) and twenty-three music videos.  After signing a publishing deal at the age of 19, Cruz released his debut studio album, "Departure", in 2006; it reached number 17 on the UK Albums Chart and was certified gold by the British Phonographic Industry (BPI).  The album contained five singles, all of which reached the top 30 of the UK Singles Chart: "Come on Girl", which peaked at number five, was the most successful of these singles.

Siobhán Donaghy discography: The discography of English singer consists of two studio albums, five singles (including one as a featured artist) and four music videos.

Nick Carter discography: The discography of Nick Carter, an American pop singer, consists of two studio album, one compilation album, five singles (including one as a featured artist) and four music videos.

Nick Carter (musician): Nickolas Gene "Nick" Carter (born January 28, 1980) is an American singer, songwriter, actor, and dancer.  He is best known as a member of the pop group the Backstreet Boys.  As of 2015, Carter has released three solo albums, "Now or Never", "I'm Taking Off" and "All American" during breaks between Backstreet Boys schedules, and a collaboration with Jordan Knight titled "Nick & Knight".  He has made occasional television appearances and starred in his own reality shows, "House of Carters" and "I (Heart) Nick Carter".  He gained fame in the mid 1990s and early 2000s as a teen idol.  He is also the older brother of singer Aaron Carter and the late Leslie Carter.

Kyuss discography: The following is a comprehensive discography of Kyuss, a Southern California-based stoner/desert rock band, active between 1988 and 1995, and again since their reunion in 2010 (as Kyuss Lives!) .  During their initial seven-year run, Kyuss had four full-length studio albums, one compilation album, one split album, seven singles, and four music videos.  They also released one EP under the name "Sons of Kyuss".  This list does not include material performed by members or former members of Kyuss that was recorded with Queens of the Stone Age, Slo Burn, Unida, Hermano, Yawning Man, Mondo Generator, Brant Bjork and the Bros, Eagles of Death Metal, and Fu Manchu.

Margaret Berger discography: The discography of Margaret Berger, a Norwegian electropop singer-songwriter, consists of two studio albums, one compilation album, five singles and five music videos.

Andy Mineo discography: The discography of American Christian hip hop artist Andy Mineo, formerly known as C-Lite, consists of two studio albums, two mixtapes, one compilation album, fourteen singles, including seven as a featured performer, fourteen music videos, including six as a featured artist, and fifteen guest appearances on various albums.  Originally from Syracuse, Mineo initially achieved success as a producer in Upstate New York, and was a member of the hip hop group Fat Camp, signed to Syracuse University's Marshall Street Records.  After moving to New York City where he re-dedicated his life to Christ, he closed down his production studio and restarted his career.  He released his first mixtape "Sin is Wack Vol.  1" in 2009.  After providing sung vocals for the song "Background" by Lecrae from the album "Rehab", he experienced a surge in popularity and became highly sought after for collaborations.  His 2011 single "In My City" featuring Efrain from Doubledge also garnered attention, as did his appearance on the song "Reverse" by Tedashii from "Blacklight".  He signed to Reach Records in 2011 and dropped his stage name "C-Lite" in favor of his legal name.  Under this name he released another mixtape, "Formerly Known", in 2011.  In May 2012 he debuted a four episode web series entitled "Saturday Morning Car-Tunez" in which he remixed classic hip hop songs.  The four songs were subsequently released for free as a compilation album.  His debut full-length studio album, "Heroes for Sale", was released April 2013.

Question: Who is the singer younger brother of the man with a discography that consists of two studio albums, one compilation album, five singles, and four music videos?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person who is the answer to the question."
    },
    "relationship_to_other_person": {
      "type": "string",
      "description": "The relationship of the person_name to the other person described in the question."
    },
    "other_person": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person whose discography was described."
        },
        "discography_summary": {
          "type": "object",
          "properties": {
            "studio_albums_count": {
              "type": "integer",
              "description": "Number of studio albums in the discography."
            },
            "compilation_albums_count": {
              "type": "integer",
              "description": "Number of compilation albums in the discography."
            },
            "singles_count": {
              "type": "integer",
              "description": "Number of singles in the discography."
            },
            "music_videos_count": {
              "type": "integer",
              "description": "Number of music videos in the discography."
            }
          },
          "required": [
            "studio_albums_count",
            "compilation_albums_count",
            "singles_count",
            "music_videos_count"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "name",
        "discography_summary"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_name",
    "relationship_to_other_person",
    "other_person"
  ],
  "additionalProperties": false
}
