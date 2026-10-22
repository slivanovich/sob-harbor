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
Planet Asia: Jason Green (born October 24, 1976), better known as Planet Asia, is a rapper from Fresno, California.  He is prominent for being one half of the now broken up hip-hop duo the Cali Agents and is currently a member of the groups Gold Chain Military and Durag Dynasty.  He is also well known for his vast discography of mixtapes.

2008 All-Pro Team: The 2008 All-Pro Team is composed of the National Football League (NFL) players that were named to the Associated Press (AP), Pro Football Writers Association (PFWA), and Sporting News All-Pro Teams in 2008.  These are the current teams that historically appear in "Total Football: The Official Encyclopedia of the NFL".  Although the NFL has no official awards, according to the NFL spokesman Greg Aiello, the "NFL Record and Fact Book" has historically listed All-Pro teams from major news sources such as the Associated Press, Sporting News, Pro Football Writers Association, as well as teams from organizations that no longer release All-Pro teams such as Newspaper Enterprise Association and United Press International.

George Esper: George Esper (1932 – February 2, 2012) was an American journalist.  Esper was a noted foreign correspondent for the Associated Press during the Vietnam war, working at the AP's Saigon Bureau under bureau chief Edwin Q. White.  Esper refused to leave the city, now known as Ho Chi Minh City, during the Fall of Saigon, choosing to cover the aftermath of the end of the war.  He spent forty-two years reporting for the Associated Press.  He worked as a journalism professor at West Virginia University following his retirement from the AP in 2000.

Four Stars (album): Four Stars (stylized as "★★★★" or ) is the fourth studio album by rock band The Greenhornes, it is available on iTunes, and the CD and LP released on November 9, 2010.  It is their first studio album in eight years, with "Dual Mono" in 2002 and their first original release since "East Grand Blues", an EP released in 2005.  After the recording and release of "East Grand Blues" and their compilation album "Sewed Soles" in 2005, the group was on temporary hiatus, and Patrick Keeler and Jack Lawrence formed The Raconteurs with Detroit friends Jack White and Brendan Benson.  After recording two albums and immense touring through North America, the UK and Australia, the group announced they would be taking a break and returning to their other bands.  During this time, Lawrence and Keeler also performed as "The Do-Whatters", Jack White's rhythm band for a collaboration with Loretta Lynn on her album "Van Lear Rose".  After these projects, Jack Lawrence and Patrick Keeler reunited with Craig Fox again in Ohio, where they recorded "Four Stars" in mid-2010.

Jack White: John Anthony "Jack" White (né Gillis; July 9, 1975) is an American musician, singer, songwriter, record producer and actor.  He is known as the lead singer and guitarist of duo The White Stripes.  He has also had success in other bands and as a solo artist.  On April 24, 2012, White released his debut solo album, "Blunderbuss".  His second studio album, "Lazaretto", was released on June 10, 2014.  Both received wide commercial and critical acclaim.

Ruby Amanfu: Ruby Amanfu is a Ghanaian-born singer and songwriter based out of Nashville, TN and Los Angeles, CA.  Amanfu released her most recent studio album, Standing Still, on August 28, 2015, following a double single release of "Bluff" and "Love Out Loud" in 2013.  Amanfu is known for her collaborations with Jack White in his all-female band, The Peacocks.  She is also well known for being one half of the duo Sam & Ruby, whose album was named Associated Press Album of the Year in 2009.

Associated Press NFL Most Valuable Player Award: The Associated Press NFL Most Valuable Player Award is presented annually by the Associated Press (AP) to the National Football League (NFL) player deemed to have been the "most valuable" in that year's regular season.  While there have been many selectors of NFL MVPs in the past, today the MVP award presented by the AP is considered the "de facto" official NFL MVP award and the most prestigious.  Since 2011, the NFL has held the annual NFL Honors ceremony to recognize the winner of each year's Associated Press MVP award, along with other AP awards, such as the AP NFL Offensive Player of the Year and AP NFL Defensive Player of the Year.  The incumbent AP NFL MVP is Matt Ryan, who led the Atlanta Falcons to an 11–5 record and whose 117.1 passer rating was the highest among quarterbacks in the 2016 season.

Sam Nixon: Sam Nixon (born 21 March 1986) is an English singer and television presenter.  He came third on the "Pop Idol" television series in 2003 and is now one half of the duo Sam & Mark, with the other being Mark Rhodes.

Rod Cason: Rod Cason (born February 9, 1950) is a former American football offensive tackle.  He played college football at Angelo State University in San Angelo, Texas from 1969-1971 where he was named twice named Associated Press "Second Team All-America" as well as being the first player named First Team NAIA All-America honors three consecutive times.  He was elected to the College Football Hall of Fame in 2002.  He was selected in the 11th round of the NFL draft by the New England Patriots in 1972.

Sam &amp; Ruby: Sam & Ruby are an American musical duo composed of Sam Brooker and Ruby Amanfu.  Sam & Ruby are based in Nashville and have recorded two EPs and one full-length record, and are currently signed to the Rykodisc record label.  Their song "Heaven's My Home" was featured on the movie and soundtrack "The Secret Life of Bees".  They are both members of the A Capella group The Collective featured on Season 3 of NBC's The Sing-Off.

Question: Ruby Amanfu is a Ghanaian-born singer and son Amanfu is known for her collaborations with Jack White, she is also well known for being one half of the duo Sam & Ruby, whose album was named Associated Press Album of the Year, in which year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "artist_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the artist."
        },
        "origin": {
          "type": "string",
          "description": "The birthplace or origin of the artist."
        }
      },
      "required": [
        "name",
        "origin"
      ],
      "additionalProperties": false
    },
    "duo_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the musical duo."
        },
        "member_count": {
          "type": "integer",
          "description": "The number of members in the duo."
        }
      },
      "required": [
        "name",
        "member_count"
      ],
      "additionalProperties": false
    },
    "album_award": {
      "type": "object",
      "properties": {
        "award_name": {
          "type": "string",
          "description": "The name of the award received by the album."
        },
        "award_year": {
          "type": "integer",
          "description": "The year the album received the award."
        }
      },
      "required": [
        "award_name",
        "award_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "artist_details",
    "duo_details",
    "album_award"
  ],
  "additionalProperties": false
}
