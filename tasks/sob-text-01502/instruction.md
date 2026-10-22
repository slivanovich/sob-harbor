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
Colm Mac Con Iomaire: Colm Mac Con Iomaire is an Irish musician from Blackrock, County Dublin.  He plays violin and sings vocals with rock group The Frames.  Mac Con Iomaire has been involved with The Frames since 1990 and has been a touring member of The Swell Season since 2006 (albums "Once" and "Strict Joy").  He also played violin on David Gray's 1998 album "White Ladder" (on the track "Silver Lining").

Sunday Bloody Sunday (film): Sunday Bloody Sunday is a 1971 British drama film written by Penelope Gilliatt, directed by John Schlesinger and starring Murray Head, Glenda Jackson, Peter Finch and Peggy Ashcroft.  It tells the story of a free-spirited young bisexual artist (played by Head) and his simultaneous relationships with a female recruitment consultant (Jackson) and a male Jewish doctor (Finch).

Steve Wickham: Steve Wickham is an Irish musician.  Originally from Marino, Dublin, but calling Sligo home, Wickham played violin on the classic U2 song "Sunday Bloody Sunday", as well as recordings by Elvis Costello, the Hothouse Flowers, Sinéad O'Connor, and World Party.  He is a long-standing member of The Waterboys.  Wickham plays both rock and roll and traditional Irish music, and has developed a rock music technique for violin he calls the "fuzz fiddle".

Sunday Bloody Sunday: "Sunday Bloody Sunday" is a song by Irish rock band U2.  It is the opening track from their 1983 album "War" and was released as the album's third single on 11 March 1983 in Germany and the Netherlands.  "Sunday Bloody Sunday" is noted for its militaristic drumbeat, harsh guitar, and melodic harmonies.  One of U2's most overtly political songs, its lyrics describe the horror felt by an observer of the Troubles in Northern Ireland, mainly focusing on the Bloody Sunday incident in Derry where British troops shot and killed unarmed civil rights protesters and bystanders.  At the same time, the lyrics reject hate and revenge as a response, as noted in the line "There's many lost, but tell me who has won."  Along with "New Year's Day," the song helped U2 reach a wider listening audience.  It was generally well received by critics on the album's release.

Sunday Bloody Sunday (disambiguation): "Sunday Bloody Sunday" is a song by U2.

This Is the Sea: This Is the Sea, released in September 1985, is the third The Waterboys album, and the last of their "Big Music" albums.  Considered by critics to be the finest album of their early rock-oriented sound, described as "epic" and "a defining moment", it was the first Waterboys album to enter the United Kingdom charts, peaking at number 37.  Steve Wickham makes his Waterboys recording debut playing violin on 'The Pan Within' and subsequently joined the band, appearing on the video of "The Whole of the Moon".  "This Is the Sea" is the last album with contributions from Karl Wallinger, who left the group to form his own band, World Party.

War (U2 album): War is the third studio album by Irish rock band U2.  It was produced by Steve Lillywhite, and was released on 28 February 1983 on Island Records.  The album has come to be regarded as U2's first overtly political album, in part because of songs like "Sunday Bloody Sunday" and "New Year's Day", as well as the title, which stems from the band's perception of the world at the time; Bono stated that "war seemed to be the motif for 1982."

Larry Mullen Jr.: Laurence Joseph Mullen Jr. (born 31 October 1961) is an Irish musician and actor, best known as the drummer of the Irish rock band U2.  Mullen's distinctive drumming style developed from his playing martial beats in a childhood marching band, the Artane Boys Band.  Some of his most notable contributions to the U2 catalogue include "Sunday Bloody Sunday", "Pride (In the Name of Love)", "Where the Streets Have No Name", "Zoo Station," "Mysterious Ways", and "City of Blinding Lights".

U2 discography: The discography of Irish rock band U2 consists of thirteen studio albums, one live album, three compilation albums, sixty-seven singles, and eight extended plays (EPs).  The band formed at Mount Temple Comprehensive School in 1976 as teenagers.  In 1979, the group issued their first release, the EP "U2-3", which sold well in Ireland.  The following year, the group signed to Island Records and released their debut album, "Boy".  It reached number 52 in the UK and number 63 in the US.  They followed it up with the release of "October" (1981) and "War" (1983).  "War" was a commercial success, becoming the band's first number-one album in the UK while reaching number 12 in the US.  The album yielded the singles "Sunday Bloody Sunday" and "New Year's Day" and have since become among the band's most popular songs.  On the subsequent War Tour, the group recorded the live album "Under a Blood Red Sky" and concert film "", both of which sold well and helped establish them globally as a live act.

War Tour: The War Tour was a concert tour by the Irish rock band U2, which took place in 1982 and 1983 in support of the group's third album "War".  The tour took place in Western Europe, the United States, and Japan, with new material from "War" taking an increasing role as the tour progressed.  Venues were mostly halls, but some arenas were introduced later on.  U2's performances were very well received both critically and commercially, especially in the United States where U2 broke through to become a major act.  Scenes of lead singer Bono waving a white flag during the song "Sunday Bloody Sunday" became an emblematic image of this phase of U2's career.  It was their first tour as full-time headlining act and their first to be profitable.

Question: Steve Wickham is an Irish musician, who played violin on the song "Sunday Bloody Sunday", a song by what rock band?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "musician_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "instrument": {
          "type": "string"
        },
        "origin_country": {
          "type": "string"
        }
      },
      "required": [
        "name",
        "instrument",
        "origin_country"
      ],
      "additionalProperties": false
    },
    "song_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string"
        },
        "album": {
          "type": "string"
        },
        "album_release_year": {
          "type": "integer"
        }
      },
      "required": [
        "title",
        "album",
        "album_release_year"
      ],
      "additionalProperties": false
    },
    "performing_band": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "country_of_origin": {
          "type": "string"
        },
        "genre": {
          "type": "string"
        }
      },
      "required": [
        "name",
        "country_of_origin",
        "genre"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "musician_details",
    "song_details",
    "performing_band"
  ],
  "additionalProperties": false
}
