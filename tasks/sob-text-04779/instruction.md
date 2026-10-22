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
Peter Gabriel (1977 album): Peter Gabriel is the debut solo studio album by English progressive Rock singer-songwriter Peter Gabriel and the first of four with the same eponymous title.  Released on 25 February 1977, it was produced by Bob Ezrin.  Gabriel and Ezrin assembled a team of musicians, including King Crimson main-man Robert Fripp, to record the album.  Upon the album's release, Gabriel began touring with a seven-piece band under his own name.

Head Down (Rival Sons album): Head Down is the third studio album by the blues rock band Rival Sons.  The album was released on September 17, 2012 in the UK and was released in the rest of Europe on September 14, 2012.  It is the last Rival Sons album recorded by the original line-up, prior to bass player Robin Everhart's departure in August 2013.

Passion (Peter Gabriel album): Passion (re-released as Passion: Music for The Last Temptation of Christ) is an album released in 1989 by the English rock musician Peter Gabriel.  It was the first Peter Gabriel album to be released on Real World Records.  It is his second soundtrack and eighth album overall.  It was originally composed as the soundtrack album for the film "The Last Temptation of Christ", but Gabriel spent several months after the film's release further developing the music, finally releasing it as a full-fledged album instead of a movie soundtrack.  It is seen as a landmark in the popularisation of world music, and won a Grammy Award for Best New Age Album in 1990.  It was remastered with most of Gabriel's catalogue in 2002.

Storm Thorgerson: Storm Elvin Thorgerson (28 February 1944 – 18 April 2013) was an English graphic designer and music video director, best known for his work for rock artists such as Pink Floyd, Led Zeppelin, Phish, Nik Kershaw, Black Sabbath, Scorpions, Peter Gabriel, Genesis, Yes, Al Stewart, Europe, Catherine Wheel, Bruce Dickinson, Dream Theater, Anthrax, The Cranberries, The Mars Volta, Muse, The Alan Parsons Project, Helloween, Biffy Clyro, Angels and Airwaves and Rival Sons.

Pressure &amp; Time: Pressure & Time is the second studio album by Long Beach-based blues rock outfit Rival Sons.  It was released on June 20, 2011 in the UK and was released in the US on June 28, 2011 through UK independent label Earache Records.  The cover artwork was designed by Storm Thorgerson, who had worked for Led Zeppelin and Pink Floyd before.  A music video has been released for title track "Pressure & Time", which features the band performing in different backgrounds.  The title track was also used as the theme song of the 2013 action-adventure video game "".  The track "Get Mine" was featured in a Jeremiah Weed premium malt beverage television advertising campaign showing an arm wrestling competition.

Funk fingers: Funk Fingers are a kind of drumsticks that are attached to the fingers of a bass player for producing percussive, funky sounds on a bass guitar.  They were created by Tony Levin (Peter Gabriel, King Crimson, Liquid Tension Experiment) and his guitar tech, Andy Moore.  The aim was to recreate the effect of drumming on the strings of one’s bass as done by drummer Jerry Marotta for Peter Gabriel’s song “Big Time” when recording the album "So".  They later appeared on the songs “Steam” and “Secret World”, also by Peter Gabriel, and Levin can be seen playing them on the video and DVD release "Secret World Live".

Peter Gabriel (1980 album): Peter Gabriel is the third album by English rock musician Peter Gabriel, released in May 1980.  The album has been acclaimed as Gabriel's artistic breakthrough as a solo artist and for establishing him as one of rock's most ambitious, innovative musicians.  Gabriel also explored more overtly political material with two of his most famous singles, the anti-war song "Games Without Frontiers" (which became a number four hit and remains his joint highest charting single in the UK) and the anti-apartheid protest song "Biko", which remembered the murdered activist Steve Biko.  The album was remastered, along with most of Gabriel's catalogue, in 2002.

Peter Gabriel (1982 album): Peter Gabriel is the fourth album released by English rock musician Peter Gabriel.  As with his previous three albums, it had no title other than Gabriel's name.  In the United States and Canada, his new label Geffen Records issued the album, with Gabriel's reluctance, with a Security sticker on top of the shrink-wrap to differentiate it from his previous releases, and this title was also printed on the labels.  Whilst Gabriel provided the title himself, the album was officially known as "Peter Gabriel" in other territories.  As a result, it is known by fans as "Security" or "Peter Gabriel 4".  A German-language version of the album, entitled the "Deutsches Album", was released later in 1982.

Peter Gabriel (1978 album): Peter Gabriel is the second solo album by the English rock musician Peter Gabriel, released in 1978.  The album is the second of four with the same eponymous title.  Guitarist Robert Fripp served as producer, whose influence on the album is evident in the use of 'Frippertronics' on the track "Exposure".  The album did not sell as well as the first "Peter Gabriel", but reached No. 10 on the UK charts.  "Mother of Violence" was written by Peter and his first wife Jill Gabriel.

Rival Sons: Rival Sons is an American rock band from Long Beach, California.  Rival Sons was formed in 2009 from the ashes of guitarist Scott Holiday’s previous band Black Summer Crush (which featured Michael Miley on drums and Robin Everhart on bass).  The band took shape when singer Jay Buchanan was persuaded to come in as vocalist on the re-recording of "Before the Fire".  The band currently features bassist Dave Beste after Robin Everhart left in August 2013.  They are currently signed to Earache Records.

Question: Who worked on the cover art for a Rival Sons album and also worked for rock artist Peter Gabriel?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person who worked on the cover art."
    },
    "person_roles": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Roles held by the person."
    },
    "worked_for_artists_relevant_to_question": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of artists the person worked for, specifically those mentioned in the question's criteria."
    },
    "rival_sons_album_artwork_details": {
      "type": "object",
      "properties": {
        "album_title": {
          "type": "string",
          "description": "The title of the Rival Sons album for which the person designed artwork."
        },
        "artist_name": {
          "type": "string",
          "description": "The name of the artist for the album."
        }
      },
      "required": [
        "album_title",
        "artist_name"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_name",
    "person_roles",
    "worked_for_artists_relevant_to_question",
    "rival_sons_album_artwork_details"
  ],
  "additionalProperties": false
}
