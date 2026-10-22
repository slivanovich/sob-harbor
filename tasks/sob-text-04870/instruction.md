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
Janis Joplin: Janis Lyn Joplin ( ; January 19, 1943 – October 4, 1970) was an American rock singer and songwriter.  She was one of the biggest female rock stars of her era.  After releasing three albums, she died of a heroin overdose at age 27.  A fourth album, "Pearl", was released in January 1971, just over three months after her death.  It reached number one on the "Billboard" charts.

Janis Joplin's Greatest Hits: Janis Joplin's Greatest Hits is a 1973 collection of hit songs by American singer-songwriter Janis Joplin, who died in 1970.

Kacee Clanton: Kacee Clanton (born Kellie Kristine Clanton) is a Los Angeles–based singer, songwriter, stage actress and performance coach who has worked as a background vocalist for recording artists Beth Hart, Joe Cocker, and Luis Miguel and toured as lead vocalist with Big Brother and the Holding Company.  She has played Janis Joplin in the musical "Love, Janis" and was the alternate lead on Broadway in the Tony-nominated musical "A Night With Janis Joplin."  She is also a vocal and performance instructor at Los Angeles College of Music.  Both her music and vocals have been used in a variety of films, TV shows, and video games.

Elizabeth Jagger: Elizabeth Scarlett "Lizzy" Jagger (born March 2, 1984) is an American-English model and actress.  Born in New York City, she is the eldest daughter of Mick Jagger and Jerry Hall.  She is the sister of James Leroy Augustin Jagger (born 1985), Georgia May Ayeesha Jagger (born 1992) and Gabriel Luke Beauregard Jagger (born 1997), and paternal half-sister of Karis Hunt Jagger (born 1970), Jade Sheena Jezebel Jagger (born 1971), Lucas Maurice Morad-Jagger (born 1999), and Deveraux Octavian Basil Jagger (born 2016).

Mick Jagger: Sir Michael Philip Jagger, MBE (born 26 July 1943) is an English singer-songwriter, multi-instrumentalist, and composer, who gained fame as the lead singer and one of the founder members of the Rolling Stones (1962-present).  Jagger's career has spanned over five decades, and he has been described as "one of the most popular and influential frontmen in the history of rock & roll".  His distinctive voice and performance, along with Keith Richards' guitar style, have been the trademark of the Rolling Stones throughout the career of the band.  Jagger gained press notoriety for his admitted drug use and romantic involvements, and was often portrayed as a countercultural figure.

Janis (1975 album): Janis is a collection of performances by Janis Joplin, issued in 1975 as a compilation album containing film soundtrack and live recordings.  Disc one is subtitled "From the soundtrack of the motion picture "Janis" (with substituted performances of 'Piece of my Heart' and 'Cry Baby')".  In addition to concert recordings from Toronto and Frankfurt, there are several short TV-interviews.  Disc two contains recordings from Austin, Texas (1963 and 1964), plus four recordings from San Francisco (1965).  The album booklet contains a photo documentary, with 22 pictures from Janis Joplin's life and career.

Kozmic Blues: "Kozmic Blues" is a song from Janis Joplin's "I Got Dem Ol' Kozmic Blues Again Mama! " album, her first after departing Big Brother and the Holding Company.  It was a part of Joplin's set at Woodstock Festival in 1969.  Although the concert as a whole is not regarded as Joplin at her best, that specific performance became very popular and was released on "The Essential Janis Joplin".

Grant Lyons: Grant Lyons (born 1941) is an American writer.  He was born in Butler, Pennsylvania, but grew up in Port Arthur, Texas.  While attending Thomas Jefferson High School in Port Arthur, Lyons and a group of male friends befriended Janis Joplin, who was otherwise an outcast in school.  As documented in all biographies of Janis Joplin, he was the person who played Janis her first Lead Belly record, which is considered a formative influence on her style of singing.  He attended Tulane University on a football scholarship, and he has a master's degree in Library Science as well as in History.  Lyons is also the grandson of Captain Ulysses Grant Lyons, who ran and was briefly pronounced winner of a U.S. house of Representatives seat, before Earl Beshlin was eventually named the winner.

Memo from Turner: "Memo from Turner" is a solo record by Mick Jagger, featuring the slide guitar by Ry Cooder, from the soundtrack of "Performance", in which Jagger played the leading role of Turner, a reclusive rock star.  It was re-released in October 2007 on a seventeen-song retrospective compilation album "The Very Best of Mick Jagger", making a re-appearance as a Jagger solo effort.  After its original release in 1970, it had been included on Rolling Stones compilations, such as "" as a track credited to the Jagger/Richards songwriting partnership.  "Memo from Turner" was ranked #92 in the 100 Greatest Guitar Songs list of "Rolling Stone".

Mary Bridget Davies: Mary Bridget Davies (born August 30, 1978) is an American singer and actress.  She performs with her own band, "The Mary Bridget Davies Group", and is also an interpreter of Janis Joplin's music.  She received a Tony Award nomination for Best Lead Actress in a Musical for her performance as Janis in "A Night with Janis Joplin".  Her band "The Mary Bridget Davies Group" released an album with original songs in 2012 titled "Wanna Feel Somethin".

Question: Mick Jagger and Janis Joplin, share which mutual occupations?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_a_name": {
      "type": "string",
      "description": "The name of the first person."
    },
    "person_b_name": {
      "type": "string",
      "description": "The name of the second person."
    },
    "shared_occupations": {
      "type": "array",
      "description": "A list of occupations shared by both individuals.",
      "items": {
        "type": "string"
      }
    },
    "number_of_shared_occupations": {
      "type": "integer",
      "description": "The count of occupations shared by both individuals."
    }
  },
  "required": [
    "person_a_name",
    "person_b_name",
    "shared_occupations",
    "number_of_shared_occupations"
  ],
  "additionalProperties": false
}
