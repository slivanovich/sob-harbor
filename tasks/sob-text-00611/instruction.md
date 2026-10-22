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
Christina Aguilera videography: American singer Christina Aguilera has released five video albums and been featured in thirty-three music videos, five films, thirteen television programs, and seven commercials.  Aguilera achieved early fame in 1993 and 1994 when she appeared in the Disney Channel television series "The New Mickey Mouse Club", which co-starred her contemporaries Britney Spears, Justin Timberlake, and Ryan Gosling.  In 1999, she rose to prominence with her eponymous debut album, whose singles "Genie in a Bottle", "What a Girl Wants", "I Turn to You" and "Come On Over Baby (All I Want Is You)" all received their music videos.  The videos for the Spanish versions of the four singles were subsequently released in conjunction with the promotion of Aguilera's 2000 Spanish album "Mi Reflejo".  In 2001, Aguilera appeared in the music video for "Lady Marmalade", a collaboration with Mýa, Lil' Kim, and Pink, which earned two MTV Video Music Awards for Video of the Year and Best Video from a Film at the 2001 ceremony.

Shelly Peiken: Shelly Meg Peiken is an American songwriter who is best known for co-writing the US #1 hits "What A Girl Wants" and "Come On Over Baby (All I Want Is You)" by Christina Aguilera the US #2 hit "Bitch" by Meredith Brooks, and the US #16 hit "Almost Doesn't Count" by Brandy.  She has also written for or with Britney Spears, Natasha Bedingfield, Keith Urban, Celine Dion, Cher, Reba McEntire, Laura Pausini, NSYNC, Miley Cyrus, Ed Sheeran, Aaliyah, Selena Gomez, Idina Menzel and Demi Lovato.

Christina Aguilera: Christina María Aguilera (born December 18, 1980) is an American singer, songwriter, actress and television personality.  Born in Staten Island, New York and raised in Rochester and Wexford, Pennsylvania, she appeared on the television series "Star Search" and "The Mickey Mouse Club" in her early years.  After recording "Reflection", the theme for Disney's 1998 film "Mulan", Aguilera signed with RCA Records.  She rose to prominence with her 1999 self-titled debut album that spawned the "Billboard" Hot 100 number-one singles "Genie in a Bottle", "What a Girl Wants", and "Come On Over Baby (All I Want Is You)".  The following year, Aguilera released two studio albums; the Spanish-language album "Mi Reflejo" and the holiday album "My Kind of Christmas".

Selena Gomez: Selena Marie Gomez ( ; ] ; born July 22, 1992) is an American singer and actress.  Gomez began her career starring in the children's television series "Barney & Friends".  She rose to fame playing the lead role of Alex Russo in the Disney Channel series "Wizards of Waverly Place" (2007–2012).  She also starred in films such as "Ramona and Beezus" (2010), "Monte Carlo" (2011), and "Spring Breakers" (2013).

Paul Davis (singer): Paul Lavon Davis (April 21, 1948 – April 22, 2008) was an American singer and songwriter, best known for his radio hits and solo career which started worldwide in 1970.  His career encompassed soul, country, and pop music.  Typically, the slower the tempo of a Davis record, the longer it took to reach its peak position.  His most successful songs are 1977's "I Go Crazy", a #7 pop hit which once held the record for the longest chart run on the "Billboard" Hot 100, and 1982's "'65 Love Affair", which at #6 is his highest-charting single.  In the mid-1980s, he also had two country #1 hits as a guest vocalist on songs by Marie Osmond and Tanya Tucker.

What a Girl Wants (Christina Aguilera song): "What a Girl Wants" is a song by American singer Christina Aguilera, taken from her self-titled debut album (1999).  A re-recorded version was released on November 28, 1999 by RCA Records as the second single from the album, following the commercial success of the lead single "Genie in a Bottle".  The song was written by Shelly Peiken and Guy Roche.  The song was completed and pitched to RCA executive Ron Fair as "What a Girl Needs" and was renamed "What a Girl Wants"; Fair later gave the track to Aguilera.  A Spanish version of the song, titled "Una Mujer," was included on Aguilera's second studio album "Mi Reflejo" (2000).

Guy Roche: Guy Roche is a record producer and songwriter who is best known for the hit singles he has co-written/co-produced for Christina Aguilera, which include but are not limited to "What a Girl Wants", "I Turn to You", and "Come On Over Baby (All I Want Is You).  He also co-wrote Brandy's "Never Say Never" single "Almost Doesn't Count" (along with Shelly Peiken).  He also produced Selena's song "Dreaming Of You", included on Selena's last album "Dreaming of You".  He has also written and produced songs for Aaliyah, Gladys Knight, Natasha Bedingfield, Brandy, Xscape, RBD, Cher (including her #3 Billboard hit "If I Could Turn Back Time"), Celine Dion, Chimène Badi and Dru Hill.

List of songs recorded by Christina Aguilera: American singer Christina Aguilera has recorded songs for her seven studio albums and collaborated with other artists for duets and featured songs on their respective albums.  In 1998, Aguilera signed a contract with RCA Records to record her self-titled debut album, which was released in August 1999.  The album spawned four singles, three of which charted atop the US "Billboard" Hot 100: "Genie in a Bottle", "What a Girl Wants", and "Come On Over Baby (All I Want Is You)".  In 2000, Aguilera released her two next studio albums: "Mi Reflejo", which consists of Spanish-language versions of songs from Aguilera's debut, and "My Kind of Christmas", which is a compilation of covers of Christmas standards and dance-pop-oriented songs.

Scott Harris (songwriter): Scott Harris Friedman is an American multi-platinum songwriter, producer, and musician best known for his work with Shawn Mendes and co-writing hit song "Don't Let Me Down" by The Chainsmokers featuring Daya, which reached #1 on the US Mainstream Top 40 chart in 2016.  Harris has 10 songs on Shawn Mendes' sophomore album "Illuminate" including the lead single "Treat You Better" which reached the top 3 at the US Mainstream Top 40 chart, "There's Nothing Holdin' Me Back which hit number 1 at the US Mainstream Top 40 chart and 10 songs on Shawn Mendes' debut album Handwritten which debuted at number 1 on the "Billboard" 200.  Harris has also written songs for a number of artists, including Jessie J, Melanie Martinez, X Ambassadors, and Tiesto; he co-wrote every song on The Shawn Mendes EP in 2014, which debuted at number five on the "Billboard" 200.

James Ingram: James Edward Ingram (born February 16, 1952) is an American singer, songwriter, record producer, and instrumentalist.  He is a two-time Grammy Award-winner and a two-time Academy Award nominee for Best Original Song.  Since beginning his career in 1973, Ingram has charted eight Top 40 hits on the US "Billboard" Hot 100 chart from the early 1980s until the early 1990s, as well as thirteen top 40 hits on the Hot R&B/Hip-Hop Songs chart.  In addition, he charted 20 hits on the Adult Contemporary chart (including two number-ones).  He had two number-one singles on the Hot 100: the first, a duet with fellow R&B artist Patti Austin, 1982's "Baby, Come to Me" topped the U.S. pop chart in 1983; "I Don't Have the Heart", which became his second number-one in 1990 was his only number-one as a solo artist.  In between these hits he also recorded the song "Somewhere Out There" with fellow recording artist Linda Ronstadt for the animated film "An American Tail".  The song and the music video both became gigantic hits.  Ingram co-wrote "The Day I Fall in Love", from the motion picture "Beethoven's 2nd" (1993), and singer Patty Smyth's "Look What Love Has Done", from the motion picture "Junior" (1994), which earned him nominations for Best Original Song from the Oscars, Golden Globe, and Grammy Awards in 1994 and 1995.

Question: What t.v. show did an American singer and actress begin her career , who also has written songs with the songwriter who is best known for co-writing the US #1 hits "What A Girl Wants" and "Come On Over Baby"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "tv_show_name": {
      "type": "string",
      "description": "The name of the television show where the artist began her career."
    },
    "artist_details": {
      "type": "object",
      "description": "Details about the American singer and actress.",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the artist."
        },
        "roles": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "The professional roles of the artist (e.g., singer, actress)."
        }
      },
      "required": [
        "name",
        "roles"
      ],
      "additionalProperties": false
    },
    "songwriter_details": {
      "type": "object",
      "description": "Details about the songwriter who collaborated with the artist.",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the songwriter."
        },
        "known_for_hits": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of hit songs the songwriter is best known for co-writing."
        }
      },
      "required": [
        "name",
        "known_for_hits"
      ],
      "additionalProperties": false
    },
    "collaboration_type": {
      "type": "string",
      "description": "Describes the nature of the collaboration between the artist and the songwriter."
    }
  },
  "required": [
    "tv_show_name",
    "artist_details",
    "songwriter_details",
    "collaboration_type"
  ],
  "additionalProperties": false
}
