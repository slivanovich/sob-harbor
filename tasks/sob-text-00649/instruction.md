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
My World Tour: The My World Tour was the debut concert tour by Canadian recording artist Justin Bieber.  It is Bieber's first concert tour which supports his two-part debut album "My World" and "My World 2.0".  The tour was officially announced on March 16, 2010, a week before "My World 2.0" was released.  The tour has multiple legs with the supporting acts of Mindless Behavior, Sean Kingston and Jessica Jarrell on North American dates and pop girl group The Stunners also joined the tour for the first twenty dates.  Jasmine Villegas joined the tour as opening act for the second leg.  The first leg of the tour is estimated to have grossed $35.6 million post inflation.  The tour made a total of $53,341,886 worldwide.

No Doubt: No Doubt is an American rock band from Anaheim, California, that formed in 1986.  Since 1994, the group has consisted of vocalist Gwen Stefani, bassist and keyboardist Tony Kanal, guitarist and keyboardist Tom Dumont, and drummer Adrian Young.  Since the mid-1990s in live performances and the studio, they have been supported by keyboardist and trombonist Gabrial McNair and keyboardist and trumpeter Stephen Bradley.

Harajuku Lovers Live: Harajuku Lovers Live is the first live long-form video by American recording artist Gwen Stefani.  It was released on DVD on December 4, 2006, by Interscope Records.  The DVD was directed by Sophie Muller and produced by Oil Factory Productions.  It is a recording of one of Stefani's concerts during her Harajuku Lovers Tour 2005 in late 2005 to promote her first album, "Love.  Angel.  Music.  Baby. ", released in November 2004.  The performance was recorded in November 2005, in Anaheim, California.  The concert features performances of all twelve songs from "Love.  Angel.  Music.  Baby."  and two new songs from her second studio album, "The Sweet Escape", as well as interviews with the musicians and dancers and a documentary of tour preparation.

Crazy Crazy/Harajuku Iyahoi: "Crazy Crazy / Harajuku Iyahoi" (Crazy Crazy / 原宿いやほい ) is the first physical single (second overall) by Japanese producer and Capsule member Yasutaka Nakata, and as well as the 13th single by Japanese model-singer Kyary Pamyu Pamyu, released on January 18, 2017.  The single was released in both CD and digital editions, also marking as their first split single.  It is also marked as the first collaboration single with UK artist and songwriter Charli XCX.

Wind It Up (Gwen Stefani song): "Wind It Up" is a song by American singer and songwriter Gwen Stefani.  Originally written for inclusion on Stefani's Harajuku Lovers Tour, the song was later recorded for her second solo studio album, "The Sweet Escape" (2006).  The track contains an interpolation of "The Sound of Music" song "The Lonely Goatherd".

Harajuku Lovers Tour: The Harajuku Lovers Tour was the first solo concert tour of American recording artist Gwen Stefani.  The tour began through October to November 2005, to support of her debut studio album "Love.  Angel.  Music.  Baby. " (2004).  Although Stefani embarked on multiple tours with her band No Doubt, she initially opted not to participate in a tour to promote her album, an attitude that the singer eventually abandoned due to the commercial success of "Love.  Angel.  Music.  Baby."

The 20/20 Experience World Tour: The 20/20 Experience World Tour was the fifth concert tour by American singer-songwriter Justin Timberlake.  It was launched in support of his third and fourth studio albums, "The 20/20 Experience" (2013) and "The 20/20 Experience – 2 of 2" (2013).  The tour began on November 6, 2013 in New York City, and concluded on January 2, 2015 in Las Vegas.  The 20/20 Experience World Tour grossed $231.6 million from 134 shows becoming the second highest-grossing tour of 2014 and one of the highest-grossing tours of the decade.  This made Timberlake the highest-grossing solo touring artist of the year.  It is also Timberlake's most successful tour to date.

Wonder World Tour (Miley Cyrus): The Wonder World Tour is the second concert tour by American recording artist Miley Cyrus.  The tour was held to promote her second studio album "Breakout" (2008) and first extended play (EP) "The Time of Our Lives" (2009).  It began in September 2009 and concluded in December 29, visiting cities in the United States and United Kingdom; thus, the Wonder World Tour became Cyrus' first world tour.  It also became Cyrus' first tour not to incorporate performances as Hannah Montana, although "Let's Get Crazy", an official Hannah-song, was performed.  Alternative band Metro Station served as opening act for all tour venues.  It was sponsored by Wal-Mart and promoted by AEG Live.  All tickets from the Wonder World Tour were sold using paperless ticketing, in order to prevent ticket scalping similar to what had occurred during Cyrus' previous tour.  One dollar from each ticket sold was donated to the City of Hope National Medical Center, an organization devoted to the fight against cancer.

A Big Night in with Darren Hayes Tour: A Big Night in with Darren Hayes Tour was the third tour undertaken by Australian singer-songwriter Darren Hayes as a solo artist.  The tour was undertaken to celebrate the release of Savage Garden's 10th anniversary greatest hits album.  The staging for the tour was simple, with a 'living room' feel, featuring a bar, dining area and wardrobe.  The show featured a great deal of audience participation, drawing on game shows, reality TV and internet dating.  Between songs, a male member of the audience was invited on to the stage where he was given a haircut and makeover by the tour's wardrobe staff.  Later, three women were invited on stage as potential 'dates', two being voted off by the audience via live text voting.  The winner was then introduced to the made-over male and the pair were served a candle lit dinner on stage, whilst Darren sang love ballads.  At the end of the show, the woman was given the choice of either "taking the bloke" or winning Geri Halliwell's mobile phone number, or alternatively Jason Donovan's home phone number for Australian performances, as a consolation prize.  The musical side of the show featured the greatest number of Savage Garden songs that Darren had performed since the demise of the group.  This served as a kind of farewell to these songs, as he has rarely revisited them since this tour.  During this tour he met keyboard player and producer Justin Shave, who has since gone on to become an ongoing musical collaborator with Hayes.  The DVD release of the tour, named "A Big Night in with Darren Hayes", was recorded in the Concert Hall of the Sydney Opera House in Sydney, Australia in July 2006.  The DVD was released in stores on 6 December 2006.  It contains the entire live show, as well as various bonus materials.

Romances Tour: Romances Tour was a concert tour performed by Luis Miguel during the years 1997 and 1998 to promote his new album Romances.  On this tour, Luis Miguel perform his last back-catalogue and also his last pop songs.  This was the longest tour of the artist until Mexico En La Piel Tour, with 17 consecutive sold-out concerts in the National Auditorium, and 5 times in the Radio City Music Hall from New York, with sold-out concerts, to put a new record.  Also he toured for first time Spain.  Pollstar mentioned this tour as one of the Top 20 All-Time Grossing, and one of the 20 artists that most tickets have sold in one same scenario in the history of the music.  The tour consisted of 84 concerts and was attended by approximately 1 million fans.

Question: Harajuku Lovers Tour is a tour by an artist who is also a member of a group from which city ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "tour_name": {
      "type": "string",
      "description": "The name of the concert tour."
    },
    "artist": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the artist who performed the tour."
        },
        "is_also_band_member": {
          "type": "boolean",
          "description": "Indicates if the artist is also a member of a band."
        }
      },
      "required": [
        "name",
        "is_also_band_member"
      ],
      "additionalProperties": false
    },
    "band": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the band the artist is a member of."
        },
        "origin_city": {
          "type": "string",
          "description": "The city where the band is from."
        },
        "origin_state": {
          "type": "string",
          "description": "The state where the band is from."
        }
      },
      "required": [
        "name",
        "origin_city",
        "origin_state"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "tour_name",
    "artist",
    "band"
  ],
  "additionalProperties": false
}
