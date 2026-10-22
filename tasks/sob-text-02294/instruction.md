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
In My Life: "In My Life" is a song by the Beatles released on the 1965 album "Rubber Soul", and credited to Lennon–McCartney.  The song originated with John Lennon, but Paul McCartney and Lennon later disagreed over the extent of their respective contribution to that song, specifically the melody.  George Martin contributed the piano solo bridge.  It is ranked 23rd on "Rolling Stone"' s "The 500 Greatest Songs of All Time" as well as fifth on their list of the Beatles' 100 Greatest Songs.  The song placed second on CBC's 50 Tracks. " Mojo" magazine named it the best song of all time in 2000.

Started with a Song (song): "Started with a Song" is a song recorded by Canadian country music artist Brett Kissel.  It was released in June 2013 as the first single from his major label debut album, "Started with a Song".  It became the most added song at Canadian country radio in its first week, surpassing a record set by Taylor Swift's "We Are Never Ever Getting Back Together".

We Are Never Ever Getting Back Together: "We Are Never Ever Getting Back Together" is a song recorded by American singer-songwriter Taylor Swift for her fourth studio album, "Red" (2012).  Swift co-wrote the song with its producers, Max Martin and Shellback.  The song was released as the lead single from "Red" on August 13, 2012, by Big Machine Records.  Its lyrics depict Swift's frustrations at an ex-lover who wants to re-kindle their relationship. " Rolling Stone" magazine named the song the second best song of 2012 while it took the fourth spot in "Time"' s end-of-year poll.  It has received a Grammy Award nomination for Record of the Year.  It also received a People's Choice Awards nomination for Favorite Song of the Year.

Convoy (song): "Convoy" is a 1975 novelty song performed by C. W. McCall (a character co-created and voiced by Bill Fries, along with Chip Davis) that became a number-one song on both the country and pop charts in the US and is listed 98th among Rolling Stone magazine's 100 Greatest Country Songs of All Time.  Written by McCall and Chip Davis, the song spent six weeks at number one on the country charts and one week at number one on the pop charts.  The song went to number one in Canada as well, hitting the top of the "RPM" Top Singles Chart on January 24, 1976.  "Convoy" further peaked at number two in the UK.  The song capitalized on the fad for citizens band (CB) radio.  The song was the inspiration for the 1978 Sam Peckinpah film "Convoy".  The song is also in the video game's soundtrack on the in-game radio station, Rebel Radio from the 2013 video game "Grand Theft Auto V", and Disney Channel (including Disney Channel Southeast Asia), a basic cable and satellite television network that is owned by Disney Channels Worldwide, a unit of the Disney–ABC Television Group.

Rock This Country!: "Rock This Country!"  is a song co-written and recorded by Canadian country music singer Shania Twain.  It was the tenth single released to country radio in January 2000 from her album "Come on Over".  Written by Mutt Lange and Twain, "Rock This Country!"  was released to North American country radio stations in late 1999.  With no promotional performances or CD single, the song was the lowest charting single at country radio from the album.

Decade of Drive: Decade of Drive is the first greatest hits album by Canadian country music group Emerson Drive.  The album was released in Canada on February 8, 2011 via Open Road Recordings.  The album features 13 of the band's hits and three new songs.  The album's first single, "When I See You Again", was written in memory of the group's former bassist, the late Patrick Bourque, who committed suicide in September 2007.  It was released to Canadian radio in late 2010.  The album's second single "Let Your Love Speak" released to U.S. country radio in 2011.  The album's third single "Sleep It Off" released to Canadian country radio in August 1, 2011.

She's with Me: "She's with Me" is a song recorded by Canadian country music duo High Valley for their fourth studio album, "County Line" (2014).  The song was written by Seth Mosley, Brad Rempel, and Ben Stennis, and was produced by Mosley.  It was released to Canadian country radio on May 13, 2015 as the album's fourth single.  "She's with Me" was later included on the American track listing for the duo's fifth studio album and major-label debut, "Dear Life" (2016).  It is scheduled to impact American country radio April 17, 2017 as that album's fourth overall single and second in the United States.

Golden Age (song): "Golden Age" is a 2008 song by the band TV on the Radio, the first single from their album "Dear Science".  It was number 12 on "Rolling Stone"<nowiki>'</nowiki>s list of the 100 Best Songs of 2008.  Spin magazine chose the song as the 8th best song of the year.  MTV ranked it as the 20th best song of the year, and Pitchfork chose it as the 51st best song of the year.

Gypsy Road (album): Gypsy Road is the fifth studio album by Canadian country music artist Dean Brody.  It was released on April 21, 2015 via Open Road Recordings.  The first single, "Upside Down", was released on February 9.  The album's second single, "Bring Down the House", was released to Canadian country radio on May 25, 2015.  The album's third single, "Love Would Be Enough", was released to Canadian country radio on October 23, 2015.  The album's fourth single, "Monterey", was released to Canadian country radio on March 18, 2016.

Life, Death, Love and Freedom: Life, Death, Love and Freedom is the 20th folk rock album by singer-songwriter John Mellencamp and produced by T-Bone Burnett.  It was released on July 15, 2008.  At the end of 2008, Rolling Stone magazine named "Life, Death, Love and Freedom" No. 5 on its list of the 50 best albums of the year.  The song "Troubled Land" was number 48 on "Rolling Stone"' s list of the 100 Best Singles of 2008.  Antimusic.com named it number 18 on their top albums of the decade list.  The album was named No. 38 in "Q"' s 50 Best Albums of the Year 2008.

Question: What song , that Rolling Stone magazine named the second best song of 2012, did "Started with a Song" surpass as the most added song at Canadian country radio?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_title": {
      "type": "string",
      "description": "The title of the song that is the answer to the question."
    },
    "ranking_information": {
      "type": "object",
      "properties": {
        "magazine_name": {
          "type": "string",
          "description": "The name of the magazine that provided the ranking."
        },
        "rank_description": {
          "type": "string",
          "description": "The description of the song's rank (e.g., 'second best song')."
        },
        "ranking_year": {
          "type": "integer",
          "description": "The year the song received the ranking."
        }
      },
      "required": [
        "magazine_name",
        "rank_description",
        "ranking_year"
      ],
      "additionalProperties": false
    },
    "record_surpassed_by": {
      "type": "object",
      "properties": {
        "surpassing_song_title": {
          "type": "string",
          "description": "The title of the song that surpassed the record."
        },
        "record_type": {
          "type": "string",
          "description": "The type of record that was surpassed."
        }
      },
      "required": [
        "surpassing_song_title",
        "record_type"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "song_title",
    "ranking_information",
    "record_surpassed_by"
  ],
  "additionalProperties": false
}
