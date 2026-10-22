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
Greatest Hits (Bomb Factory album): Greatest Hits is the first compilation album by punk rock band Bomb Factory.  It was released in November 2007 on Monstar Records/CCRE, and contains 16 songs.  The album artwork was produced by New York-based illustrator Joe Simko.  A year later, Bomb Factory signed with American N2O Records and re-released the album under the title Moshing Through Tokyo on August 18, 2008, making it their first release in the United States and the second in Europe after "Discord".  It was also their first release on iTunes.  The same tracks and cover art were included from "Greatest Hits" with only minor changes to the design.

Gossip (Sleeping with Sirens album): Gossip is the fifth studio album by American rock band Sleeping with Sirens.  The album was released on September 22, 2017, through Warner Bros.  Records and follows the band's fourth studio album "Madness" (2015).  It is the first release since the band's departure from Epitaph Records and their first release on a major label.  The lead single, "Legends", was released on July 14, 2017.

We (Don't) Care: We (Don't) Care is the first release by the American rock band The Management (now known as MGMT).  Newer versions of the tracks "Love Always Remains" and "Kids" were later released on MGMT's Cantora Records release "Time to Pretend" EP (2005) and additional versions of "Kids" appear on both their major-label debut "Oracular Spectacular" (2007–2008) and their demo album "Climbing to New Lows" (2005) recorded shortly after this EP.  Additionally, "We Care", "We Don't Care" and "Grutu (Just Becuz)" were also included on "Climbing to New Lows".

Three Cheers for Sweet Revenge: Three Cheers for Sweet Revenge is the second studio album by American rock band My Chemical Romance, released on June 8, 2004.  It is My Chemical Romance's first release through Reprise.  Their first and previous album, "I Brought You My Bullets, You Brought Me Your Love", was released through Eyeball Records.  It is the band's final release to feature drummer Matt Pelissier, who would later be replaced by Bob Bryar.  The album was certified platinum in less than a year from its release.  The album has sold over one million copies in the United States.

The Maine (band): The Maine is an American rock band from Tempe, Arizona, formed in 2007.  Their first release, the EP "Stay Up, Get Down" was released in late 2007, followed by a five-song EP titled "The Way We Talk" on December 11, 2007.  The band's first full-length album, "Can't Stop Won't Stop" was released July 8, 2008. " ...And a Happy New Year" was released in December 2008.  Their second full-length album, "Black & White", (July 13, 2010) sold 22,634 copies in its first week.  On December 6, 2011, the group's third album, "Pioneer", was released and it peaked at No. 90 on the Billboard 200.  Their fourth full-length record "Forever Halloween"(June 4, 2013) reached No. 39 on the Billboard 200 by selling over 10,000 copies in its first week and was followed by its deluxe edition on June 17, 2014.  Their fifth studio album, "American Candy", was released on March 31, 2015. " Lovely Little Lonely", their sixth full-length record, was released on April 7, 2017.

Climbing to New Lows: Climbing to New Lows is a demo album by the American rock band The Management (now known as MGMT) that inadvertently became their first full release.  "Climbing to New Lows" was intended to be only a demo album that was leaked on the Internet in 2005.  It featured some tracks from their self-released "We (Don't) Care" EP in 2004 such as "We Care", "We Don't Care", "Grutu (Just Becuz)" and "Kids".  It was their last release as The Management.

MGMT: MGMT is an American psychedelic rock band formed in 2002 at Wesleyan University.  It currently consists of Andrew VanWyngarden (lead vocals, guitar, keyboards, bass guitar, drums, percussion) and Ben Goldwasser (vocals, keyboards, guitar, percussion).  In the live lineup it consists of VanWyngarden, Goldwasser, Will Berman (drums, percussion, harmonica, backing vocals), Matt Asti (bass guitar, backing vocals), James Richardson (lead guitar, keyboards, backing vocals) and Hank Sullivant (guitar, keyboards).

Prey (Planes Mistaken for Stars album): Prey is the fourth studio album by American rock band Planes Mistaken for Stars.  Following the band's 2008 breakup and their 2010 sporadic return to touring, "Prey" marks the band's first release since the compilation album "We Ride to Fight!"  (2007) and first release of new material since "Mercy" (2006).  The album was released on October 21, 2016 through Deathwish Inc. who also reissued and remastered "Mercy" the previous year.

R.E.M.: R.E.M. was an American rock band that formed in Athens, Georgia, in 1980 by lead singer Michael Stipe, guitarist Peter Buck, bassist/backing vocalist Mike Mills, and drummer Bill Berry.  One of the first alternative rock bands, R.E.M. was noted for Stipe's particular vocal quality and obscure lyrics, Buck's ringing, arpeggiated guitar style, and Mills' melodic basslines and backing vocals.  R.E.M. released its first single—"Radio Free Europe"—in 1981 on the independent record label Hib-Tone.  The single was followed by the "Chronic Town" EP in 1982, the band's first release on I.R.S. Records.  In 1983, the group released its critically acclaimed debut album, "Murmur", and built its reputation over the next few years through subsequent releases, constant touring, and the support of college radio.  Following years of underground success, R.E.M. achieved a mainstream hit in 1987 with the single "The One I Love".  The group signed to Warner Bros.  Records in 1988, and began to espouse political and environmental concerns while playing large arenas worldwide.

U2 discography: The discography of Irish rock band U2 consists of thirteen studio albums, one live album, three compilation albums, sixty-seven singles, and eight extended plays (EPs).  The band formed at Mount Temple Comprehensive School in 1976 as teenagers.  In 1979, the group issued their first release, the EP "U2-3", which sold well in Ireland.  The following year, the group signed to Island Records and released their debut album, "Boy".  It reached number 52 in the UK and number 63 in the US.  They followed it up with the release of "October" (1981) and "War" (1983).  "War" was a commercial success, becoming the band's first number-one album in the UK while reaching number 12 in the US.  The album yielded the singles "Sunday Bloody Sunday" and "New Year's Day" and have since become among the band's most popular songs.  On the subsequent War Tour, the group recorded the live album "Under a Blood Red Sky" and concert film "", both of which sold well and helped establish them globally as a live act.

Question: We (Don't) Care is the first release by an American rock band that was formed in what year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "release_name": {
      "type": "string",
      "description": "The name of the album or EP in question."
    },
    "band_name": {
      "type": "string",
      "description": "The name of the band that released the album."
    },
    "band_formation_year": {
      "type": "integer",
      "description": "The year the band was formed."
    }
  },
  "required": [
    "release_name",
    "band_name",
    "band_formation_year"
  ],
  "additionalProperties": false
}
