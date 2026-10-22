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
Supercharged (album): Supercharged is the eighth album by American soul/R&B group Tavares, produced by David Foster, Benjamin Wright and Bobby Colomby (former drummer of the rock group Blood, Sweat & Tears), and released in 1980 on the Capitol label.  "Supercharged" is similar in style to the group's previous album "Madam Butterfly", and although not as highly regarded at its predecessor, critical reaction is generally positive.  Lead single "Bad Times" reached the R&B top 10 and #47 on the pop chart, the group's first showing on that chart since "More Than a Woman" in 1977.  "Supercharged" made #20 on the R&B chart and #75 on the pop chart.

Jaco Pastorius (album): Jaco Pastorius is the solo debut album by Jaco Pastorius, released in 1976.  The album was produced by Bobby Colomby, drummer and founder of Blood, Sweat & Tears.

Mikee Plastik: Mikee Plastik is an American composer, actor, and artist.  Mikee Plastik was born Michael Scott Hollash in Tampa, FL, on November 9, 1976.  He is mostly known through his work in the music industry.  Early on, Plastik signed a licensing deal with Cleopatra Records, having a couple of his tracks released worldwide through compilation albums.  He was a founding member of the band Grim Faeries, which featured members of My Life With The Thrill Kill Kult, Pigface, and a former touring stage performer from U2.  They became known through their work on the legendary MMORPG PC gaming franchise Ultima Online, when they were contracted by Origin Systems to provide a reworked version of their single "Love Is Hell" for the official promotional trailer for the developing Ultima Online 2.  The trailer was first released on a promotional DVD sampler in the June 2000 issue of PC Gamer, giving the subscribing fanbase their first glimpse of what was to come.  The Grim Faeries full length album "The Disenchanted Forest" and various compilations that they were featured on, which Plastik wrote and tracked the guitar parts on, were either released or handled by Invisible Records and were distributed through Caroline Records.  Over the years, Mikee Plastik has collaborated and recorded with various cutting edge bands and artists on their releases, such as Hate Dept., Pete Jones (Public Image Limited / Department S), Pigface, Psychotica, Team Cybergeist, and many others.  Most recently, he and Pete Jones were brought in and collaborated together recording and producing two tracks on the Patrick Briggs album "Pervert".  Over the years, Plastik has written and composed for film and TV around recording within the record industry.  He has placed his primary focus on film underscoring more recently.

Terry Riley: Terrence Mitchell "Terry" Riley ( ; born June 24, 1935) is an American composer and performing musician associated with the minimalist school of Western classical music, of which he was a pioneer.  His work is deeply influenced by both jazz and Indian classical music.

Days in Avalon: Days In Avalon is the sixth studio album by singer/songwriter Richard Marx, released independently in 2000 on the now defunct label "Signal 21".  This was the only release on the label created by Marx and Blood, Sweat, and Tears drummer Bobby Colomby.

Bobby Colomby: Robert Wayne Colomby (born 20 December 1944, in New York) is a jazz-rock fusion drummer, and an original member of the group Blood, Sweat & Tears.  He is also the uncredited drummer on John Cale and Terry Riley's collaboration album "Church of Anthrax".

Harold Spina: Harold Spina (21 June 1906 – 18 July 1997) was an American composer of popular songs.  His best-known work happened in the early 1930s, when he collaborated with lyricists Johnny Burke and Joe Young on songs such as "Annie Doesn't Live Here Anymore", "You're Not the Only Oyster in the Stew", "My Very Good Friend the Milkman" (these two hits for Fats Waller), "Shadows on the Swanee", "The Beat of My Heart", "Now You've Got Me Doing It", and "I've Got a Warm Spot in My Heart for You".  He also collaborated with lyricist John Elliot for several songs, including "It's So Nice To Have A Man Around The House" (made famous by Dinah Shore).

Now Is the Time (Jeff Lorber Fusion album): Now Is the Time is a jazz album released by Jeff Lorber Fusion.  The album was released in 2010 on Heads Up Records and was produced by Jeff Lorber, Bobby Colomby, and Jimmy Haslip.  It was nominated for the 2011 Grammy Award for Best Contemporary Jazz Album.

Brand New Day (Blood, Sweat &amp; Tears album): Brand New Day is an album by the band Blood, Sweat & Tears, released in 1977.  This was the band's tenth studio album and their first and only release for ABC Records.  Brand New Day was produced by Roy Halee and former BS&T drummer Bobby Colomby.  Colomby and Halee had also co-produced the group's fourth album, "Blood, Sweat & Tears 4" in 1971.  This collection failed to chart on the Billboard Album Charts in the top 200 even though it did reach #205 under the chart.

Signal 21 Records: Signal 21 Records is a defunct independent record label created by singer-songwriter Richard Marx and Blood, Sweat, and Tears drummer Bobby Colomby in 2000.  This label ended up being the primary vehicle for the quiet release of Marx's October 24, 2000 album "Days In Avalon" and later the release of "Timeline", a compilation album that was released to radio stations to help promote "Days In Avalon".  The label folded shortly thereafter.  The discs were distributed by the Navarre label, an offshoot company of the Universal Music Group.

Question: Which American composer collaborated with Bobby Colomby on an album?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "collaborator_name": {
      "type": "string",
      "description": "The name of the American composer who collaborated with Bobby Colomby."
    },
    "collaborator_nationality": {
      "type": "string",
      "description": "The nationality of the composer."
    },
    "collaborator_primary_profession": {
      "type": "string",
      "description": "The primary profession of the composer."
    },
    "album_of_collaboration": {
      "type": "string",
      "description": "The name of the album on which the collaboration occurred."
    },
    "bobby_colomby_role_on_album": {
      "type": "string",
      "description": "Bobby Colomby's role in the collaboration on the specified album."
    }
  },
  "required": [
    "collaborator_name",
    "collaborator_nationality",
    "collaborator_primary_profession",
    "album_of_collaboration",
    "bobby_colomby_role_on_album"
  ],
  "additionalProperties": false
}
