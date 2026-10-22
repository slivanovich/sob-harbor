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
Why Do Fools Fall in Love (soundtrack): Why Do Fools Fall in Love is the soundtrack to the 1998 film of the same name.  It was executive produced by Missy Elliott and released on September 8, 1998 through Elektra Records, East West Records and Missy Elliott's label The Goldmind Inc. The soundtrack featured main production by Elliott and Timbaland.  It peaked at 55 on the "Billboard" 200 and 15 on the Top R&B/Hip-Hop Albums and spawned the singles "I Want You Back" by Melanie Brown featuring Missy Elliott, "No Fool No More" by En Vogue, which peaked at 57 on the "Billboard" Hot 100 as well as Destiny's Child's "Get on the Bus".  Singer Lil' Mo also made her debut with the single and music video for "Five Minutes."

Reality Show (album): Reality Show is the third studio album by American R&B singer Jazmine Sullivan.  She recorded the album, her first in five years, during a hiatus from the music industry, writing and working with producers such as Anthony Bell, Salaam Remi, and Key Wane.  After the album was released on January 13, 2015, by RCA Records, it received widespread acclaim from critics and sold 30,000 copies in its first week.

Gotta Getcha: "Gotta Getcha" is a song by American record producer Jermaine Dupri, released as the first single from his compilation album "Young, Fly & Flashy, Vol.  1" (2005).  The album version features vocals by Johntá Austin, and uncredited vocals from Janet Jackson and Missy Elliott, who helped write the song alongside Dupri.  The original version featured Elliott rapping and singing the chorus.  The official remix features Usher, Johntá Austin and Rico Love.  Another remix featuring Usher, Johntá Austin and Missy Elliott was released via mixtapes.

Respect M.E.: Respect M.E. (short for Respect Missy Elliott) is the first greatest hits album by American rapper-songwriter Missy Elliott, released by Atlantic Records on September 4, 2006 in Europe, Asia and Australia.  It includes a collection of the singles from across all six of her studio albums, released between 1997 and 2005.  Speculation about two new tracks on the album began soon after its announcement.  Two tracks called "123" and "Magnifica" were supposed to be included; "123" was even able to be pre-ordered as a CD single from UK music store HMV.  However, these songs did not make the album.

Burnitup!: "Burnitup!"  (stylized as "BURNITUP!")  is a song by American singer Janet Jackson featuring rapper Missy Elliott recorded for Jackson's eleventh studio album, "Unbreakable" (2015).  It was written and produced by Jackson, Dem Jointz, Jimmy Jam and Terry Lewis and Elliott.  The song marked the fourth time Jackson and Elliott collaborated together.  "Burnitup!"  was released as a promotional single from the album on September 25, 2015, while a digital promo single containing the album's version and a radio edit was released on October 5, 2015 by Rhythm Nation Records and BMG Rights Management.

Make It Hot: Make It Hot is the debut studio album by R&B singer Nicole Wray.  The album was released in August 1998 through Missy Elliott's Elektra-distributed vanity label, The Goldmind.  The album was produced by Missy Elliott and Timbaland.  Some editions of the release credit Nicole as "Nicole Ray", an artist name she only used here and on her single "I Can't See".

1, 2 Step: "1, 2 Step" is a song recorded by American singer Ciara featuring female rapper Missy Elliott for Ciara's debut album, "Goodies".  Written by Ciara and Missy Elliott and produced by Jazze Pha, it was released as the album's second single on October 23, 2004 in the United States and the second quarter of 2005 internationally.  It peaked within the top ten of the charts in several countries worldwide, including Germany, New Zealand and the United Kingdom.  The song is heavily inspired by 1980s electro music production.  Throughout the song, Ciara gives a description of how the song's beat feels as she demands party-goers to dance to the music.  "1, 2 Step" was ranked 59th on "Billboard"<nowiki>'</nowiki>s Top 100 Songs of the 2000s.  In the United States, the song peaked at number two on the "Billboard" Hot 100 and stayed there for ten weeks.

Fighting Temptation: "Fighting Temptation" is a song recorded by American R&B singer Beyoncé and American female rappers Missy Elliott, MC Lyte, and Free in 2003.  The song was used to promote the film "The Fighting Temptations" (2003), in which Beyoncé stars.  It was composed by the Beyoncé, Missy Elliott, Lana Moorer, Marie Wright, Jonathan Burks, LaShaun Owens, Karriem Mack, and Walter Murphy.  "Fighting Temptations" was released as the lead single from the soundtrack album of the movie on July 5, 2003 through Columbia Records and Sony Music Entertainment.

The Road to Stardom with Missy Elliott: The Road to Stardom With Missy Elliott was a competitive reality television show that aired on the UPN Network in 2005.  The main judge and host was hip-hop artist Missy Elliott.  Other judges were singer-producer Teena Marie, producer Dallas Austin, and manager Mona Scott.

Jazmine Sullivan: Jazmine Marie Sullivan (born April 9, 1987) is an American singer-songwriter from Philadelphia, Pennsylvania.  Her debut single "Need U Bad", produced by Missy Elliott, reached #1 on "Billboard"' s Hot R&B/Hip-Hop Songs, while her second single, "Bust Your Windows", produced by Salaam Remi, peaked at #4.  Elements of R&B, reggae, dub, pop, jazz, neo soul and doo-wop can be heard in her work.  Sullivan cites singers Brandy, Changing Faces, Kim Burrell, Lauryn Hill, and Dorinda Clark-Cole as her main influences and inspirations.

Question: Which Philadephia singer, who has collaborated with Missy Elliott, released her third album Reality Show in 2015?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "singer_name": {
      "type": "string",
      "description": "The name of the singer."
    },
    "origin_city": {
      "type": "string",
      "description": "The city the singer is from."
    },
    "collaborated_with_missy_elliott": {
      "type": "boolean",
      "description": "Indicates if the singer has collaborated with Missy Elliott."
    },
    "album_details": {
      "type": "object",
      "properties": {
        "album_title": {
          "type": "string",
          "description": "The title of the album."
        },
        "release_year": {
          "type": "integer",
          "description": "The year the album was released."
        },
        "album_type": {
          "type": "string",
          "description": "The type of album (e.g., studio album)."
        },
        "album_number": {
          "type": "integer",
          "description": "The sequential number of the album for the artist."
        }
      },
      "required": [
        "album_title",
        "release_year",
        "album_type",
        "album_number"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "singer_name",
    "origin_city",
    "collaborated_with_missy_elliott",
    "album_details"
  ],
  "additionalProperties": false
}
