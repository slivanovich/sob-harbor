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
Open My Heart: "Open My Heart" is a song by Yolanda Adams released in 1999.  The song gained Adams great popularity in the secular audiences.  Being the most groundbreaking single of her career, she won several awards for this song.  "Open My Heart" helped her 1999 album "Mountain High...Valley Low" gain multi-platinum status and reach charts heights not often attained by artists of the gospel genre.

Heart (Heart album): Heart is the self-titled eighth studio album, released by the American rock band Heart.  Released in 1985, the album continued the band's transition into mainstream rock, a genre that yielded the band its greatest commercial success.  Marking the band's Capitol Records debut, it spent 92 weeks on the U.S. "Billboard" 200 and became the only Heart album so far to hit number one, reaching quintuple platinum status.  It also yielded the first number-one single for the band, "These Dreams", along with four other hit singles: "What About Love", "Never", "Nothin' at All" and "If Looks Could Kill".  The first three cuts also made the U.S. top ten.

I Give You My Heart (Hillsong song): "I Give You My Heart" (sometimes called "Lord, I Give You My Heart" or "This is My Desire") is a 1995 song by Reuben Morgan, who wrote both the music and the lyrics.  The lyrics are about giving God the entirety of oneself.  The song is widely used in congregational singing, particularly within evangelicalism.  "I Give You My Heart" is a devotional song and is part of the contemporary worship music genre.  The song is also a slow soft rock ballad.

Open Your Heart (Madonna song): "Open Your Heart" is a song by American singer Madonna from her third studio album "True Blue" (1986).  It was released as the album's fourth single in November 19, 1986 by Sire Records.  It has since appeared remixed on the compilation albums "The Immaculate Collection" (1990) and "Celebration" (2009).  Originally a rock and roll song titled "Follow Your Heart", it was written for singer Cyndi Lauper by songwriters Gardner Cole and Peter Rafelson.  Looking for new songs for "True Blue", Madonna accepted it.  She rewrote the song and, along with Patrick Leonard, changed the composition to suit the dance-pop genre.  "Open Your Heart" is an innuendo-laden love song where Madonna expresses her sexual desire.

Tintin and I: Tintin and I (French: Tintin et moi) is a 2003 documentary by Anders Høgsbro Østergaard, about Belgian writer-artist Georges Remi, better known as Hergé, and his creation Tintin.  The film is a co-production of Denmark, Belgium, France, and Switzerland.

Chernobyl Heart: Chernobyl Heart is a 2003 documentary film by Maryann DeLeo.  The film won the Best Documentary Short Subject award at The 76th Academy Awards.

Wang Kuan-hsiung: Wang Kuan Hsiung was a lean dapper Taiwanese actor who was a well-known and popular leading man in the Kung Fu film genre of the 1970s and 1980s.  He was cast as a romantic leading man in some of his films and he gained many female fans and is still considered a heart throb He is mostly known for his role in a 1974 film as Chan Ming Lung a.k.a. "The Iron Ox" in Iron Ox, The Tiger's Killer, which is a tale about a student taking on a group of men, The Five Tigers in duels to avenge the death of his teacher.  This film also featured a well-known actor of the genre, Wong Fei-Lung

Kill from the Heart: Kill from the Heart is an album by the American hardcore punk band The Dicks.  Widely considered a classic of the genre, it was the band's first full-length album and the last to feature the group's original Texas-based line up.  The album finds the band mixing its hardcore punk style with blues aesthetics.  Tim Kerr of the Big Boys appears on the song "Anti-Klan (Part Two)".  "Anti-Klan (Parts One and Two)", "Rich Daddy", "No Nazi's Friend", and "Kill From The Heart" appear on the "1980-1986" CD compilation on Alternative Tentacles.  The album was reissued on CD & LP by Alternative Tentacles in 2012.

White Horse (film): White Horse is a short documentary by filmmakers Maryann DeLeo and Christophe Bisson that features a man (Maxym Surkov) returning to his Ukraine home for the first time in twenty years.  Evacuated from the city of Pripyat, Ukraine in 1986 due to the Chernobyl disaster, he has not returned since then.  DeLeo is the same filmmaker of the 2004 Academy Award-winning short film "Chernobyl Heart".

Sigismunda mourning over the Heart of Guiscardo: Sigismunda mourning over the Heart of Guiscardo, fully titled Sigismunda mourning over the Heart of Guiscardo, her murder'd Husband, is an oil painting by British artist William Hogarth.  Finished in 1759, it was the principal piece of the eight works he displayed in an exhibition in 1761.  It was the final and most ambitious of his attempts to secure for himself a reputation as a genre painter.  It depicts a dramatic moment in one of the "novelle" in Boccaccio's "Decameron".  While Hogarth had expected this work to be acclaimed as a masterpiece of dramatic painting, the work was met with criticism and ridicule.  In the catalogue of the exhibition of Hogarth's works at the Tate Gallery in 2007, the criticism was described as "some of the most damning critical opprobrium the artist ever suffered".

Question: Tintin and I and Chernobyl Heart, are of which genre?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "titles_analyzed": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "title_name": {
            "type": "string"
          },
          "genre": {
            "type": "string"
          },
          "release_year": {
            "type": "integer"
          }
        },
        "required": [
          "title_name",
          "genre",
          "release_year"
        ],
        "additionalProperties": false
      }
    },
    "identified_common_genre": {
      "type": "string"
    },
    "number_of_titles_analyzed": {
      "type": "integer"
    }
  },
  "required": [
    "titles_analyzed",
    "identified_common_genre",
    "number_of_titles_analyzed"
  ],
  "additionalProperties": false
}
