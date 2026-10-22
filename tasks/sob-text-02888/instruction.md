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
Craig Northey: Craig Northey (born February 9, 1962) is a Canadian musician and film and TV composer.  He's one of the founding members of the band Odds, which released four albums between 1991 and 1996.  They were best known for the radio singles "It Falls Apart", "Eat my Brain", "Heterosexual Man" and "Someone Who’s Cool".

Omarion: Omari Ishmael Grandberry (born November 12, 1984, known by his stage name Omarion) is an American singer, songwriter, rapper, actor and dancer.  He is best known as being the lead singer of the American R&B boy band B2K; the group achieved success with singles like "Bump, Bump, Bump", "Uh Huh", and "Girlfriend", which all reached success on the "Billboard" Hot 100.  After the group's disbandment, Omarion released his debut solo album, "O" (2005), which debuted atop the "Billboard" 200 and received a Grammy Award nomination for Best Contemporary R&B Album at the 48th Grammy Awards.  His second solo album, "21" (2006), contained his second highest-charting single to date, "Ice Box", which reached the top 20 on the "Billboard" Hot 100.  His third solo album, "Ollusion" (2010), was released on January 12, 2010, with the lead single, "I Get It In".  His fourth solo album, "Sex Playlist" (2014), spawned the single, "Post to Be", which was certified 3x platinum and reached number 13 on the Hot 100 chart in May 2015, and became his highest charting single to date.

Rita Redshoes: Rita Pereira (born 10 July 1981), known by her stage name Rita Redshoes, is a solo musical artist from Portugal.  In 1996 she sang with her first band, Atomic Bees, releasing an album in 2000 entitled "love.noises.and.kisses".  In 2003, she was invited to sing with David Fonseca, and shared with him the song “Hold Still” from "Our Hearts Will Beat As One", his second solo album.  In 2008 she released her debut solo album "Golden Era".  In 2010 the band Snow Patrol invited her to perform the single "Set the fire to the third bar" in Rock in Rio Lisbon.

Jeff Rosenstock: Jeff Rosenstock is an American musician and songwriter from Long Island.  He was the lead singer of the ska-punk band The Arrogant Sons of Bitches, the musical collective Bomb the Music Industry!  and the indie rock band Kudrow.  More recently, he has begun a solo career, releasing his first solo album, "I Look Like Shit", in 2012, and a follow up album, "We Cool? " in 2015.  His third solo album, entitled "Worry", was released on October 14, 2016.

Stripper's Union: Stripper's Union is a Canadian rock band consisting of Rob Baker (vocals, guitar), Craig Northey (vocals, guitar), Doug Elliott (bass guitar), Simon Kendall (piano), and Pat Steward (drums).  The band released two albums between 2005 and 2011.

Guess Who (rapper): Laurenţiu Mocanu (born June 2, 1986), better known by his stage name Guess Who is a Romanian rapper.  He began his career as a member of the rap group Anonim along with group members Zekko and Griffo, and later launched a successful solo career in music.  He is one of the most successful artists from the new wave of Romanian hip hop and has gained considerable appreciation and mainstream attention in his native Romania following the release of his first solo album in 2009 called Probe Audio (Sound Check).  Guess Who gained popularity as a solo artist in 2007 when he leaked three tracks he had recorded for his solo album on the Internet.  The feedback was overwhelmingly positive and his cynical and ironic approach to writing quickly earned him a large fanbase.  Even though he repeatedly delayed for over two years releasing his first album, the Romanian audience received it well and he even gained attention from high level Romanian music executives when his video for the first single Tu (You) was aired on the Romanian music channel 1Music.

Odds: Odds are a numerical expression, usually expressed as a pair of numbers, used in both gambling and statistics.  In statistics, the odds for or odds of some event reflect the likelihood that the event will take place, while odds against reflect the likelihood that it will not.  In gambling, the odds are the ratio of payoff to stake, and do not necessarily reflect exactly the probabilities.  Odds are expressed in several ways (see below), and sometimes the term is used incorrectly to mean simply the probability of an event.  Conventionally, gambling odds are expressed in the form "X to Y", where X and Y are numbers, and it is implied that the odds are odds against the event on which the gambler is considering wagering.  In both gambling and statistics, the 'odds' are a numerical expression of the likelihood of some possible event.

Jesse Valenzuela: Jesse Valenzuela (born May 22, 1962) is an American rock singer and musician who is perhaps best known as a member of the Alternative rock band, the Gin Blossoms.  Valenzuela was originally the vocalist in the Gin Blossoms when the band first formed in 1987.  In 1988, he switched roles with the band's new guitarist, Robin Wilson.  He continued to be a member until the band's breakup in 1997, and reunited with the rest of the group in 2002.  In 2002, he released a solo album, "Tunes Young People Will Enjoy."  In 2004, Valenzuela collaborated with Canadian singer-songwriter Craig Northey on the album "Northey Valenzuela", and they co-wrote and performed "Not A Lot Goin' On", the theme song to the Canadian sitcom "Corner Gas.

Giddy Up (album): Giddy Up is the first solo CD released by Craig Northey, a former member of the Canadian 1990's alternative band Odds.  It was released in 2001 and has eight songs, totaling a running time of approximately 25 minutes.  Other composers who contributed to the album include David Gamson and Blair Packham.

A Different Sort of Solitude: A Different Sort of Solitude is a single by Steven Page.  It was released January 17, 2012.  It contains two non-album tracks.  "A Different Sort of Solitude" was written and recorded for the film "French Immersion".  The b-side, "Manchild", was co-written with Craig Northey of the Vancouver-based band Odds.  On the same day as the release of the single, Page was nominated for the 32nd Annual Genie Awards for the composition of "A Different Sort of Solitude".

Question: Which band did Craig Northey formerly play with before releasing his solo album Giddy Up?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "artist_name": {
      "type": "string",
      "description": "The name of the musician."
    },
    "solo_album": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the solo album."
        },
        "release_year": {
          "type": "integer",
          "description": "The year the solo album was released."
        }
      },
      "required": [
        "title",
        "release_year"
      ],
      "additionalProperties": false
    },
    "former_band": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the band the artist formerly played with."
        },
        "role_in_band": {
          "type": "string",
          "description": "The artist's role in the former band."
        },
        "band_active_years": {
          "type": "string",
          "description": "The period during which the band released albums."
        }
      },
      "required": [
        "name",
        "role_in_band",
        "band_active_years"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "artist_name",
    "solo_album",
    "former_band"
  ],
  "additionalProperties": false
}
