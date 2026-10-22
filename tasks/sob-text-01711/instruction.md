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
God of Our Fathers: "God of Our Fathers" is a 19th-century American Christian hymn, written in 1876 to commemorate the 100th anniversary of the United States Declaration of Independence.

How Great Thou Art: "How Great Thou Art" is a Christian hymn based on a Swedish traditional melody and a poem written by Carl Gustav Boberg (1859–1940) in Mönsterås, Sweden in 1885.  It was translated into German and then into Russian and became a hymn.  It was translated into English from the Russian by English missionary Stuart K. Hine, who also added two original verses of his own.  The composition was set to a Russian melody.  It was popularised by George Beverly Shea and Cliff Barrows during the Billy Graham crusades.  It was voted the United Kingdom's favourite hymn by BBC's "Songs of Praise."  "How Great Thou Art" was ranked second (after "Amazing Grace") on a list of the favourite hymns of all time in a survey by "Today's Christian" magazine in 2001.

Nearer, My God, to Thee: "Nearer, My God, to Thee" is a 19th-century Christian hymn by Sarah Flower Adams, which retells the story of Jacob's dream.  Genesis 28:11–12 can be translated as follows: "So he came to a certain place and stayed there all night, because the sun had set.  And he took one of the stones of that place and put it at his head, and he lay down in that place to sleep.  Then he dreamed, and behold, a ladder was set up on the earth, and its top reached to heaven; and there the angels of God were ascending and descending on it..."

Onward, Christian Soldiers: "Onward, Christian Soldiers" is a 19th-century English hymn.  The words were written by Sabine Baring-Gould in 1865, and the music was composed by Arthur Sullivan in 1871.  Sullivan named the tune "St. Gertrude," after the wife of his friend Ernest Clay Ker Seymer, at whose country home he composed the tune.  The Salvation Army adopted the hymn as its favoured processional.  The piece became Sullivan's most popular hymn.  The hymn's theme is taken from references in the New Testament to the Christian being a soldier for Christ, for example II Timothy 2:3 (KJV): "Thou therefore endure hardness, as a good soldier of Jesus Christ."

Onward, Christian Pilgrims: "Onward, Christian Pilgrims" is a 20th-century Christian hymn by David Wright.  It was composed in 1982, is based on "Onward, Christian Soldiers", and was intended as a non-militaristic version of the earlier hymn.

Naneun Ggomsuda: Naneun Ggomsuda (Korean: 나는 꼼수다 ), also known as Naggomsu (Korean: 나꼼수 ) or in English as I'm a weasel is a popular South Korean political podcast under the internet newspaper, .  Naneun Ggomsuda is famous for lampooning the South Korean president, Lee Myung-bak.  The hosts of Naneun Ggomsuda humorously call Lee Myung-bak as "His Excellency" or Gaka (각하) in Korean as a sarcastic title.  They have also made a satire song (based on a Christian hymn, Nearer, My God, to Thee) about Lee's disputes on his Naegok-dong property purchase.  Kim Ou joon (김어준) was the original creator of Naneun Ggomsuda and currently runs Papa is (파파이스) and News factory (뉴스공장)

Nearer My God to Thee (disambiguation): "Nearer, My God, to Thee" is a 19th-century Christian hymn by Sarah Flower Adams.

Abide with Me, 'Tis Eventide: "Abide with Me, 'Tis Eventide" is a 19th-century American Christian hymn written by Martin Lowrie Hofford (lyrics) and Harrison Millard in 1870 (music).  The lyrics and music to the hymn were heavily influenced by the American Civil War.

Nunc sancte nobis spiritus: Nunc, Sancte, nobis Spiritus is a Christian hymn which has traditionally been attributed to the fourth century St. Ambrose of Milan.  However the earliest manuscript tradition for the hymn seems to only go back to the ninth century.  The hymn has traditionally been a core part of the prayers at Terce in the Liturgy of the Hours.  The reason for this is that the Acts of the Apostles records an event at Pentecost where the apostles are filled with the Holy Spirit.  The experience clearly causes the apostles to behave in an unusual way and in chapter 2 verse 15 the Acts of the Apostles states explicitly that the apostles were not drunk because it was only the third hour of the day (ie 9am).  As the Acts of the Apostles was so explicit in linking the Pentecost experience of the Apostles to the third hour of the day, Christian hymns and prayers intended to be used at that time of the day, have traditionally made reference to the coming of the Holy Spirit.

Lift High the Cross: "Lift High the Cross" is a 19th-century English Christian hymn.  It was written in 1887 by George Kitchin and revised in 1916 by Michael R. Newbolt.

Question:  Naneun Ggomsuda made a satire song based on the 19th-century Christian hymn by whom?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "satire_song_creator": {
      "type": "string",
      "description": "The name of the entity that created the satire song."
    },
    "original_hymn_title": {
      "type": "string",
      "description": "The title of the original Christian hymn."
    },
    "original_hymn_author": {
      "type": "string",
      "description": "The author of the original Christian hymn."
    },
    "hymn_century": {
      "type": "string",
      "description": "The century in which the original hymn was written."
    }
  },
  "required": [
    "satire_song_creator",
    "original_hymn_title",
    "original_hymn_author",
    "hymn_century"
  ],
  "additionalProperties": false
}
