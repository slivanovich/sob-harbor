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
Cleo (magazine): Cleo is a Malaysian, Singaporean, Thailand and Indonesia monthly women's magazine.  The magazine was founded in 1972 in Australia; the Australia and New Zealand editions were discontinued in 2016.

JGeek and the Geeks: JGeeks are a New Zealand performance Maori comedy music group best known for their songs "Maori Boy" and "The Best Day I Ever Had", as well as their 2012 appearance as finalists in "New Zealand's Got Talent".  The group is led by former Disney Channel and C4 television presenter and Cleo Bachelor of the Year finalist, Jermaine Leef.

L'Arpeggiata: L'Arpeggiata is a European early music group led by Christina Pluhar, and founded by her in 2000.  The group has presented both traditional early music and also several collaged and themed performances and recordings.

Retrospective (Monkey House album): Retrospective is the name of an anthology album by the music group Monkey House, which was released in 2013 on the Green Dolphin Music label.  Monkey House is a rock/pop/jazz group led by Don Breithaupt.  This release has a total of 44 tracks: 38 songs, plus six interviews.  It includes almost every tune from their first two albums, "Welcome to the Club" (1992), and "True Winter" (1998), and also has four newer songs that were on the 2005 release entitled "Big Money: Singles Remasters Rarities 1992-2005".  Additionally, six tunes not previously released are on this anthology album, five of them being instrumentals, as well as the tune "I'm Not That Guy" from the "Headquarters" (2012 album) sessions, but had not been included on that album.  Special guests include Little Feat drummer Richie Hayward and former Pat Metheny Group member David Blamires.

George Petros: George Petros (born George Lawrence Petros, January 11, 1955, Chicago, Illinois, United States) is an American art designer, author, editor, interviewer and illustrator.  From 1984 through 1992 he published and edited "EXIT", a punk-inspired art and science fiction magazine he founded with Adam Parfrey and Kim Seltzer.  From 1992 through 2000 he edited and art-directed "Seconds", an all-interview music and culture magazine founded by Steven Blush.  From 2000 through 2005 he was a contributing editor of "Juxtapoz", the low-brow art magazine founded by Robert Williams, and the senior editor of "Propaganda", a goth/industrial music and style magazine founded by Fred H. Berger.

Anthony and the Camp: Anthony and the Camp is a dance music group led by producer Anthony Malloy.  The group also consists of Crawford Peterson, Henley Goddard and Linden Aaron.  Malloy, who already had a number-one hit on the Hot Dance Music/Club Play chart with his former group Temper, hit the top spot again with the Camp in 1986 with the song "What I Like".

Will Dailey: Will Dailey is an independent American recording artist, performer and producer.  His sound has been described as having a rich vintage vibe while having a firm appreciation of AM rock, pop and big hooks.  He has released albums with Universal, CBS Records, Wheelkick Records and JS Music Group.  Dailey has released four full-length albums since 2004.  His last full-length album, "National Throat", came out on Wheelkick Records, on August 26, 2014.  It directly followed Dailey's choice to split with a major label and use Pledge Music to create his album.  Based out of Boston, he is notable as being a 7 time winner in the Boston Music Award: Best Male Singer-Songwriter in 2006, again on December 2, 2009 and December 2, 2012 and Album of the Year and Artist of the Year December 14, 2014 and Male Vocalist in 2015 and 2016.  The first single, "Sunken Ship", was a finalist in the 2013 International Songwriting Competition, received heavy radio play and received Song of The Year in the New England Music Awards.  The album was released exclusively on vinyl three month prior to official release date.  It premiered on Billboards Heat Seekers chart at #18 and won Album of the Year in the New England Music Awards April 19, 2015 as well.  In 2009 and 2010, Dailey released "Torrent", which involved the artist digitally releasing a burst of new music approximately every three months, and then compiling that material, along with bonus material, as a physical and digital audio package twice a year.  Dailey is also a part of the John Mellencamp and Stephen King musical project Ghost Brothers of Darkland County.

Ty Morse: Ty Morse is an American composer, documentary film producer, and entrepreneur whose technology startup, Songwhale has become a leader in mobile marketing both in the U.S. and internationally.  Since 2007, Morse has expanded Songwhale from its offices in Pittsburgh, PA to several overseas markets, including Tokyo, Japan, Bangkok, Thailand, the Philippines, and Malaysia.  As CEO, Morse has been twice nominated as an Ernst and Young Entrepreneur of the Year Finalist and has led Songwhale to two Pittsburgh Technology Council nominations for Tech 50 Startup of the Year and Tech 50 Nominee for New Media.

Trapezoid (band): Trapezoid is an American folk music group led by Paul Reisler.  Founded in 1975 by Sam Rizzetta and Reisler, they began as a quartet of hammer dulcimer players.  Two of the four played the traditional hammer dulcimer, while the other two played baritone and treble hammer dulcimers specially designed by Rizzetta.  The name of the band reflects the shape of the hammer dulcimer.  Since 1975, the group's membership and instrumentation has changed repeatedly, always with Paul Reisler as a member.  Their sound has been described as a "plinking and plunking, buzzing, sweeping, ringing, droning, and wailing acoustic construction" and as "a delightful musical melange" by the New York Times.

Naomi Shelton &amp; the Gospel Queens: Naomi Shelton & the Gospel Queens are an American gospel and soul music group led by front woman Naomi Shelton.  The group was formed in 1999.  Two founding members were from Brooklyn, New York.  They have released two albums with Daptone Records, "What Have You Done, My Brother?"  (2009) and "Cold World" (2014).  Both albums charted on the "Billboard" magazine charts, where they placed on the Gospel Albums chart.

Question:  JGeeks is a music group led by a Bachelor of the Year finalist from a magazine founded in what year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "group_name": {
      "type": "string",
      "description": "The name of the music group."
    },
    "group_leader": {
      "type": "string",
      "description": "The name of the group leader who was a Bachelor of the Year finalist."
    },
    "magazine_name": {
      "type": "string",
      "description": "The name of the magazine that hosted the Bachelor of the Year competition."
    },
    "magazine_founding_year": {
      "type": "integer",
      "description": "The year the magazine was founded."
    }
  },
  "required": [
    "group_name",
    "group_leader",
    "magazine_name",
    "magazine_founding_year"
  ],
  "additionalProperties": false
}
