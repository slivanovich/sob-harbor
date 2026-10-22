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
War Babies (band): War Babies was an American rock band formed in Seattle, WA in 1988, fronted by former TKO vocalist Brad Sinsel.  Although associated with hard rock, the band's sound incorporated some elements of grunge music.  They only released one album, in 1991, the self-titled War Babies.

The Electric Spanking of War Babies (song): "The Electric Spanking of War Babies" is the title track from the last album recorded by the American funk band Funkadelic.  The song was released as a single in 1981 by Warner Bros.  Records.  Instrumentally the track was constructed by co-writer Walter Morrison.  It charted on the "Billboard" R&B chart, peaking at number 60.

Guy Lacey: Guy Lacey is an American rock guitarist, singer and songwriter.  He is best known for his work with Seattle grunge rock band War babies in the 1990s and with American punk rock outfit Sledgeback in the 2000s. He has recorded the one and only album of War babies, released on Columbia records in 1992 including the song "In the Wind" which features in the 1992 film "Buffy the Vampire Slayer", the forerunner to the later successful TV series.Lacey joined Sledgeback in 2006.  His signature guitar style became an important part of Seattle punk rock stalwarts Sledgeback.

Live in Oklahoma 1976: Live in Oklahoma 1976 is a live album by the American Funk band Bootsy's Rubber Band.  The album was released in 2001 and represents a collaborative effort between the Funk To The Max label, based in the Netherlands, and Bootzilla Records in the U.S..  The performance was recorded while Bootsy's Rubber Band was the support act (along with Sly and the Family Stone) for headliners Parliament-Funkadelic.

Blinddog Smokin': Blinddog Smokin' is an American funk band.  Their original funk music also incorporates roots, rock, blues, gospel and soul stylings.  Over two decades they have performed internationally, across America, recorded twelve albums, and produced sixty-one original songs.  They have also collaborated with Bobby Rush and Dr. John.

Funkadelic: Funkadelic is an American band that was most prominent during the 1970s.  The band and its sister act Parliament, both led by George Clinton, pioneered the funk music culture of that decade.

War Babies (War Babies album): War Babies is the debut and only album by the band War Babies, who disbanded in 1993.  The album was released by Columbia Records in 1991 and re-issued by German label UlfTone Music in 2003 and French company Bad Reputation in 2007, respectively.

Ain't but the One Way: Ain't But the One Way is the tenth and final album by Sly and the Family Stone, released by Warner Bros.  Records in 1982.  The album began its existence as a collaborative project between Sly Stone and George Clinton, a sequel to Stone's appearance on the 1981 Funkadelic album "The Electric Spanking of War Babies".  While working on "Ain't But the One Way", Clinton and Funkadelic quarreled with and eventually left Warner Bros.  Records, and Sly Stone went into self-seclusion and could not be found.  Producer Stewart Levine was assigned to take control of the project, and do what he could to complete an album.  Upon its 1982 release, "Ain't But The One Way" underperformed and marked the end of Sly Stone's career with Warner Bros.  Records.

The Electric Spanking of War Babies: The Electric Spanking of War Babies is the 13th studio album by the American funk band Funkadelic, released in April of 1981 on Warner Bros.  Records.  The title is an allusion to the Vietnam War and baby boomers.  It includes many relative newcomers to P-Funk, many of whom remained employed by George Clinton on future releases under his own name or under the name George Clinton & the P-Funk All-Stars.  Sly Stone is a collaborator on this album.  Clinton originally planned on this being a double album, but the idea was quashed by Warner Brothers.  Some of the deleted tracks appeared on later P-Funk releases, most notably the 1982 hit single "Atomic Dog" which appeared on the first George Clinton solo album, "Computer Games".

Plush Funk: Plush Funk is the second installment of the George Clinton Family Series collection.  The album was released in 1992 by P-Vine Records in Japan, and then was released the next year by AEM Records in the United States and Sequel Records in the United Kingdom.  The CD features the track "May Day (S.O.S)", which was an outtake from the Funkadelic album "The Electric Spanking of War Babies".

Question: What is the name of the sister act of this American funk band that recorded The Electric Spanking of War Babies that pioneered the funk music culture of the 1970s?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "main_band_name": {
      "type": "string",
      "description": "The name of the American funk band that recorded the album."
    },
    "album_name": {
      "type": "string",
      "description": "The name of the album mentioned in the question."
    },
    "sister_act_name": {
      "type": "string",
      "description": "The name of the sister act of the main band."
    },
    "band_leader": {
      "type": "string",
      "description": "The leader of both the main band and its sister act."
    },
    "pioneering_genre": {
      "type": "string",
      "description": "The music genre pioneered by the bands."
    },
    "pioneering_decade": {
      "type": "string",
      "description": "The decade in which the music culture was pioneered."
    }
  },
  "required": [
    "main_band_name",
    "album_name",
    "sister_act_name",
    "band_leader",
    "pioneering_genre",
    "pioneering_decade"
  ],
  "additionalProperties": false
}
