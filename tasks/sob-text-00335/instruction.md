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
Fear, Love &amp; War: Fear, Love & War is the third album by the hip hop group Killarmy, which was released September 11, 2001, on Loud/Relativity Records.  The album came three years after its second album, "Dirty Weaponry".  Nearly half the album was produced by the group's primary beat maker and group member 4th Disciple, with additional production provided by group affiliates Falling Down and Rebel Dainja, as well as underground production duo the Infinite Arkatechz.  The album features guest appearances from Wu-Tang Clan member U-God and Wu-Tang Clan affiliates Prodigal Sunn, Frukwan, Lord Superb, and Polite.  The album features the singles "Feel It" b/w "Militant" and "Street Monopoly" b/w "Monster."

Wu-Syndicate: Wu-Syndicate is a group from Virginia consisting of Joe Mafia, Napoleon, and Myalansky (who named himself after the gangster Meyer Lansky).  They were originally called Crime Syndicate but changed their name to Wu-Syndicate when they signed to Wu-Tang Records and became Wu-Tang Clan affiliates.  After debuting on the compilation "" in 1998, their self-titled debut album "Wu-Syndicate" was released in 1999 on both Wu-Tang Records and their own label Slot Time Records.  The album was, like most releases from Wu-Tang Clan affiliates during this time enjoyed moderately successful sales with the single "Where Wuz Heaven" going gold.  Soon after the release there was a dispute of an unknown origin between the group and Wu-Tang Records and the group briefly changed their name to The Syndicate until 2009 with eventual reconciliation and the release of their second official album "Grimlenz", produced mostly by Antagonist Dragonspit of Virginia Beach,VA.  Both Myalansky and Napoleon continue to work with Joe Mafia but have refused to work with each other since the release of their first album.  In an interview Napoleon stated that though they have always clashed, "Mya is still my dude though regardless".  The group has maintained ties with various members of the Wu-Tang Family.  Napoleon is currently working on a project with fellow Wu-Tang alumni Solomon Childs, Shaka Amazulu, and Dexter Wiggle called "Illuminati Network".  Joe Mafia released his debut solo album "This One" in 2002 and founded his own label called 58 West Diamond Street Records.  Napoleon released his first solo album, "Kingpin Wit Da Inkpen" in 2007 and a mixtape titled "Mark of the Beast" in 2011.  Myalansky released his first solo album, "Drastic Measures" in 2008 and a mixtape a few years later in 2011 "AMW.Com".  Myalansky has also been working with California rapper Mitchy Slick and has released two more volumes of his "AMW.Com" mixtape series.  In 2013 Myalansky and Joe Mafia featured on the song "Golden Age Rapper" by CHG Unfadable.

Enter the Wu-Tang (36 Chambers): Enter the Wu-Tang (36 Chambers) is the debut studio album by the American hip hop group Wu-Tang Clan, released November 9, 1993, on Loud Records and distributed through RCA Records.  Recording sessions for the album took place during 1992 to 1993 at Firehouse Studio in New York City, and it was mastered at The Hit Factory.  The album's title originates from the martial arts film "The 36th Chamber of Shaolin" (1978).  The group's "de facto" leader RZA produced the album entirely, utilizing gritty, eerie beats and a sound largely based on martial-arts movie clips and soul music samples.

Wu-Tang Clan: The Wu-Tang Clan is an American hip hop group from Staten Island, New York City, originally composed of East Coast rappers RZA, GZA, Ol' Dirty Bastard, Method Man, Raekwon, Ghostface Killah, Inspectah Deck, U-God and Masta Killa.  Cappadonna later became an official member of the group.  The Wu-Tang Clan has released four gold and platinum studio albums. Its 1993 debut album, "Enter the Wu-Tang (36 Chambers)", is considered to be one of the greatest albums in hip-hop history.

C.R.E.A.M.: "C.R.E.A.M." (Cash Rules Everything Around Me) is a song by the New York hip hop group Wu-Tang Clan, from their 1993 studio album, "Enter the Wu-Tang (36 Chambers)".  The song was produced by Wu-Tang Clan leader RZA, and samples The Charmels' 1967 song, "As Long As I've Got You".  "C.R.E.A.M." was released as a single through Loud in early 1994.

Wu-Tang Meets the Indie Culture: Wu-Tang Meets the Indie Culture is an album released October 18, 2005.  This album was put together by Dreddy Krueger who has produced Wu-Tang and others.  It includes collaborated tracks by Wu-Tang Clan members, Wu-Tang Clan affiliates, and various other underground hip-hop artists such as Cannibal Ox, Aesop Rock, Sean Price, Casual, and MF Doom.  The album has sold 59,133 units.

Method Man discography: The discography of Method Man, an American hip hop recording artist, consists of five studio albums (including one collaborative album) and 34 singles (including 16 as a featured artist).  Method Man embarked on his music career in 1992, as a member of East Coast hip hop group Wu-Tang Clan.  After the Wu-Tang Clan released their highly acclaimed debut album "Enter the Wu-Tang (36 Chambers)" (1993), Method Man would be the first member to release his solo debut album.  In November 1994, he released "Tical", under Def Jam Recordings.  His debut album "Tical", features his biggest hit single to date, "I'll Be There for You/You're All I Need to Get By", which features American R&B singer Mary J. Blige and peaked at number three on the US "Billboard" Hot 100.  Method Man would then go on to collaborate with fellow East Coast rapper Redman, and subsequently form a duo together.

The W: The W is the third studio album by the American hip hop group Wu-Tang Clan.  It was released on November 21, 2000, by Loud Records.  After their 1997 album "Wu-Tang Forever", several of the group's members released solo projects before "The W", which has a more rugged, less polished sound than that of most Wu-Tang related albums from that era.  The album also features guest appearances from Isaac Hayes, Redman, Nas, Busta Rhymes, Snoop Dogg, and Junior Reid.

Wu-Tang Forever: Wu-Tang Forever is the second studio album of American hip-hop group Wu-Tang Clan, released June 3, 1997, on Loud/RCA Records in the United States.  Pressed as a double album, it was released after a long run of successful solo projects from various members of the group, and serves as the follow-up to their debut album "Enter the Wu-Tang (36 Chambers)".  "Forever" features several guest appearances from Wu-Tang affiliates Cappadonna, Streetlife, 4th Disciple, True Master, and Tekitha.  The original run of compact discs featured an "Enhanced CD" which allowed users to walk around the "Wu Mansion" and access additional content.

Heavy Mental: Heavy Mental is the debut album by rapper Killah Priest, an associate of hip-hop group Wu-Tang Clan and a member of the group Sunz of Man.  It was released on March 10, 1998, on Geffen Records.

Question: On which day was the studio album of the American hip-hop group Wu-Tang Clan released, that came before their album "The W"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "album_name": {
      "type": "string",
      "description": "The name of the studio album."
    },
    "group_name": {
      "type": "string",
      "description": "The name of the hip-hop group."
    },
    "release_date": {
      "type": "object",
      "properties": {
        "day": {
          "type": "integer",
          "description": "The day of the month the album was released."
        },
        "month": {
          "type": "string",
          "description": "The month the album was released."
        },
        "year": {
          "type": "integer",
          "description": "The year the album was released."
        }
      },
      "required": [
        "day",
        "month",
        "year"
      ],
      "additionalProperties": false
    },
    "album_order_description": {
      "type": "string",
      "description": "Description of the album's order in the group's discography (e.g., 'second studio album')."
    },
    "preceded_album_name": {
      "type": "string",
      "description": "The name of the album that this album preceded."
    }
  },
  "required": [
    "album_name",
    "group_name",
    "release_date",
    "album_order_description",
    "preceded_album_name"
  ],
  "additionalProperties": false
}
