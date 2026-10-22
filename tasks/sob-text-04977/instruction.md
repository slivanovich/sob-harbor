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
Laura Marling: Laura Beatrice Marling (born 1 February 1990) is a British folk singer-songwriter and musician from Eversley, Hampshire.  Her debut album "Alas, I Cannot Swim", her second album "I Speak Because I Can", and her fourth album "Once I Was an Eagle" were each nominated for the Mercury Music Prize in 2008, 2010, and 2013, respectively.  She won the Brit Award for Best British Female Solo Artist at the 2011 Brit Awards, and was nominated for the same award at the 2012, 2014 and 2016 Brit Awards.

Buster (soundtrack): Buster: The Original Motion Picture Soundtrack is the soundtrack for the 1988 British film "Buster".  The album is essentially a collection of oldies, tucked in between two Phil Collins songs that were recorded for the film, in which he starred. " Two Hearts" was specially written for the film, having earned a Grammy Award for Best Song Written Specifically for a Motion Picture or Television in 1989, a Golden Globe Award for Best Original Song (tying with "Let the River Run" from "Working Girl" by Carly Simon) as well as an Academy Award nomination for Best Original Song, and "A Groovy Kind of Love" with a Grammy Award nomination for Best Pop Vocal Performance, Male was a remake of a song taken to #2 in the UK Singles Chart in 1965 by The Mindbenders.  Both were released as singles, and topped the "Billboard" Hot 100 chart, with "A Groovy Kind of Love" also reaching #1 in the UK.  Other new songs include Collins' "Big Noise" and The Four Tops' "Loco in Acapulco", co-written by Collins.  The soundtrack received at the Brit Awards in 1989 the award for British Soundtrack Album, while Collins received the award British Male Artist for his contribution to the soundtrack album.

Nick Morris: Nick Morris is a film maker who began writing and making amateur films at school, one of which was shown at the NFT.  His professional career began in the 1980s with music videos for "The Final Countdown" by Europe, "Kyrie" by Mr. Mister and "Everytime You Go Away" by Paul Young.  After making approximately 100 promos for artists such as Elton John, Celine Dion, Alison Moyet, Warrant, Terence Trent D'Arby, Stevie Wonder, Paul Carrack, Prefab Sprout, Kirsty MacColl, Go West, the Kane Gang, The Alarm, Status Quo, Toto, Natalie Cole, Nena, Scorpions and the number one charity single Ferry Aid, he moved into longer form projects including the Cirque du Soleil show "Alegría", which was nominated for a primetime Emmy, "Jesus Christ Superstar", which won an International Emmy, and AC/DC's "Stiff Upper Lip Live" in Munich.  He has also directed DVDs for comedians such as The Mighty Boosh, Mitchell and Webb and Bill Bailey.  Other work includes numerous trailers and music clips for West End shows such as "The Producers", "Spamalot", "Calendar Girls", "Guys and Dolls", "Edward Scissorhands" and "The Rocky Horror Show".  in 2009 he captured Spandau Ballet's triumphant homecoming concert at the O2 Arena in London and Jude Law's portrayal of Hamlet.

Paul Young: Paul Antony Young (born 17 January 1956) is an English singer, songwriter and musician.  Formerly the frontman of the short-lived bands Kat Kool & the Kool Cats, Streetband and Q-Tips, his subsequent solo success turned him into a 1980s teen idol.  He is famous for such hit singles as "Love of the Common People", "Wherever I Lay My Hat", "Come Back and Stay", "Everytime You Go Away" and "Everything Must Change", all reaching the top 10 of the UK Singles Chart.  Released in 1983, his debut album "No Parlez", the first of three UK number one albums, turned him into a household name.  His smooth yet soulful voice belonged to a genre known as "blue-eyed soul".  At the 1985 Brit Awards, Young received the award for Best British Male.

Brit Awards: The Brit Awards (sometimes stylised as the BRIT Awards; often simply called the Brits) are the British Phonographic Industry's annual pop music awards.  The name was originally a shortened form of "British", "Britain" or "Britannia" (in the early days the awards were sponsored by Britannia Music Club), but subsequently became a backronym for British Record Industry Trusts Show.  In addition, an equivalent awards ceremony for classical music, called the Classic Brit Awards, is held each May.  Robbie Williams holds the record for the most Brit Awards, 13 as a solo artist and another five as part of Take That.

Ed Sheeran: Edward Christopher Sheeran, {'1': ", '2': ", '3': ", '4': "} (born 17 February 1991) is an English singer-songwriter, guitarist, and record producer.  He was born in Halifax, West Yorkshire, and raised in Framlingham, Suffolk.  He attended the Academy of Contemporary Music in Guildford, Surrey, as an undergraduate from the age of 18 in 2009.  In early 2011, Sheeran independently released the extended play, "No. 5 Collaborations Project".  After signing with Asylum Records, his debut album, "+" (read as "plus"), was released on 9 September 2011 and has since been certified seven-times platinum in the UK.  The album contains the single "The A Team", which earned him the Ivor Novello Award for Best Song Musically and Lyrically.  In 2012, Sheeran won the Brit Awards for Best British Male Solo Artist and British Breakthrough Act.

Riptide (album): Riptide is the eighth solo studio album by the British singer Robert Palmer.  It was originally released in November 1985.  The album was recorded over a period of three months in 1985, at Compass Point Studios in Nassau, Bahamas.  The album charted at number 8 in the US and No. 5 in the UK.  It was certified double platinum in the US by the RIAA in March 1996 and certified gold in the UK by BPI in August 1986.  It featured the songs "Addicted to Love", "I Didn't Mean to Turn You On", "Discipline of Love", and "Riptide" which were all released as singles.  The single "Addicted to Love" was accompanied by a memorable and much-imitated music video, directed by Terence Donovan, in which Palmer is surrounded by a bevy of near-identically clad, heavily made-up (and appropriately pouty) female "musicians," either mimicking or mocking the painting style of Patrick Nagel.  In September 1986, Palmer performed "Addicted to Love" at the 1986 MTV Video Music Awards in Los Angeles.  In 1987, he won the Grammy Award for Best Male Rock Vocal Performance for "Addicted to Love".  At the 1987 Brit Awards, Palmer received his first nomination for Best British Male.

James Bay (singer): James Michael Bay (born 4 September 1990) is an English singer-songwriter and guitarist.  In 2014, he released his single "Hold Back the River", which has been certified platinum, before releasing his debut studio album "Chaos and the Calm" (2015).  The album went to number one in the UK and number 15 in the US.  In February 2015, Bay received the Brit Awards "Critics' Choice" award.  At the 2016 Brit Awards he received the award for Best British Male Solo Artist.  Bay also received three nominations at the 2016 Grammy Awards, for Best New Artist, Best Rock Album, and Best Rock Song.

David Gray (musician): David Gray (born 13 June 1968) is an English singer-songwriter.  Gray released his first studio album in 1993 and received worldwide attention after the release of "White Ladder" six years later.  It was the first of three UK chart-toppers in six years for Gray, of which the latter two also made the Top 17 in the US.  "White Ladder" became the fifth best-selling album of the 2000s in the UK.  Gray has been nominated for four Brit Awards – twice for Best British Male.

Brit Award for British Female Solo Artist: The Brit Award for British Female Solo Artist is an award given by the British Phonographic Industry (BPI), an organisation which represents record companies and artists in the United Kingdom.  The accolade is presented at the Brit Awards, an annual celebration of British and international music.  The winners and nominees are determined by the BRIT Awards voting academy with over one-thousand members, which comprise record labels, publishers, managers, agents, media, and previous winners and nominees.  The award was first presented in 1977 as Best British Female.

Question: Nick Morris made the music video for which song by the 1985 Brit Awards "Best British Male" recipient?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "artist_name": {
      "type": "string",
      "description": "The name of the artist who received the specified Brit Award."
    },
    "award_name": {
      "type": "string",
      "description": "The name of the Brit Award received by the artist."
    },
    "award_year": {
      "type": "integer",
      "description": "The year the artist received the Brit Award."
    },
    "music_video_director": {
      "type": "string",
      "description": "The director of the music video."
    },
    "song_title": {
      "type": "string",
      "description": "The title of the song for which the music video was made by the specified director."
    }
  },
  "required": [
    "artist_name",
    "award_name",
    "award_year",
    "music_video_director",
    "song_title"
  ],
  "additionalProperties": false
}
