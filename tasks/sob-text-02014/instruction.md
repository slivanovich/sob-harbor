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
Spectrum (arena): The Spectrum (later known as CoreStates Spectrum, First Union Spectrum and Wachovia Spectrum) was an indoor arena in Philadelphia, Pennsylvania.  Opened in the fall of 1967 as part of what is now known as the South Philadelphia Sports Complex, after several expansions of its seating capacity it accommodated 18,168 for basketball and 17,380 for ice hockey, arena football, indoor soccer, and indoor lacrosse.

Dedication (Gary U.S. Bonds album): Dedication is an album released by Gary U.S. Bonds in 1981, the first of two on which he collaborated with Bruce Springsteen & the E Street Band, the second being "On the Line", released the following year, 1982.  The musicians accompanying Bonds on the album include many members of the E Street Band and the Asbury Jukes.  The album includes three songs written by Bruce Springsteen, one written by Steve Van Zandt, and several covers of songs from the Beatles, Bob Dylan, Jackson Browne, and others.  It also features a duet between Bonds and Springsteen on the track "Jole Blon".  Bonds' early 1960s sound had been a major influence on both Springsteen and Van Zandt.  The songs written by Springsteen, including the cover of "Jole Blon", were originally intended for his 1980 album, "The River", but he felt they fitted better with Bonds and his versions of them have never been released although he has performed most of them live, often featuring Bonds as a special guest.

Wachovia Spectrum, Philadelphia, PA 10/20/09: Wachovia Spectrum, Philadelphia, PA 10/20/09 is a live album by Bruce Springsteen and the E Street Band, released on July 13, 2017.  It is the fourteenth such release by the Bruce Springsteen Archives.  The performance was Springsteen's final show at the soon to be demolished Wachovia Spectrum in Philadelphia, PA and featured a full album performance of "Born in the U.S.A.", the show opener, "The Price You Pay", which was performed for the first time since 1981 and guest appearances by former band member Vini Lopez and even Springsteen's mother Adele.

Bruce Springsteen: Bruce Frederick Joseph Springsteen (born September 23, 1949) is an American singer-songwriter, known for his work with the E Street Band.  Nicknamed "The Boss", he is widely known for his brand of poetic lyrics, Americana, working class, sometimes political sentiments centered on his native New Jersey, his distinctive voice, and his lengthy and energetic stage performances—with concerts from the 1970s to the present decade running at up to four hours in length.  His artistic endeavors reflect both his personal growth and the zeitgeist of the times.

Chapter and Verse (Bruce Springsteen album): Chapter and Verse is an album by Bruce Springsteen that was released on September 23, 2016.  The album is a companion piece to Springsteen's 500 plus page autobiography, "Born to Run", which was released four days later.  The career-spanning album features eighteen songs handpicked by Springsteen, five of which have never been released.  The album contains Springsteen's earliest recording from 1966 and late '60s/early '70s songs from his tenure in The Castiles, Steel Mill and The Bruce Springsteen Band along with his first 1972 demos for Columbia Records and songs from his studio albums from 1973 until 2012.

Ed Manion: Ed Manion (born February 28, 1952), also known as Eddie "Kingfish" Manion, is an American saxophonist, who plays both tenor and baritone sax.As a solo artist, he released his own instrumental album titled Nightlife in 2015.  Manion is currently a recording and touring member of Little Steven and the Disciples of Soul.  He was a touring member of the horn section for Bruce Springsteen and the E Street Band and also a member of Bruce Springsteen with The Seeger Sessions Band Tour, later called Bruce Springsteen with The Sessions Band.  He is an original member of Southside Johnny and the Asbury Jukes, The Miami Horns, and Little Steven and the Disciples of Soul.  As a session musician, he has recorded, toured, and/or performed with, among others, Bruce Springsteen and The E Street Band, Diana Ross, Gary U.S. Bonds, Bon Jovi, Willy DeVille, Dave Edmunds, Bob Dylan, Keith Richards, Darlene Love, Ronnie Spector, Dion, The Allman Brothers Band, Kim Wilson, and Graham Parker.  As a solo artist, he released his own CD titled "Follow Through" in 2004.

Rosalita (Come Out Tonight): "Rosalita (Come Out Tonight)" is a 1973 song by Bruce Springsteen, from his "The Wild, the Innocent & the E Street Shuffle" album, and is especially famed as a concert number for Springsteen and The E Street Band.  The song, which clocks in at just over seven minutes, is a story of forbidden love between the singer and the titular Rosalita, whose parents disapprove of his life in a rock and roll band.  It is included on the compilation albums "The Essential Bruce Springsteen" and "Bruce Springsteen & The E Street Band Greatest Hits".

Frank Stefanko: Frank Stefanko is a fine art photographer with connections to New Jersey performers Patti Smith and Bruce Springsteen.  Stefanko's early photographs, taken in the 1960s through the 1980s, reveal the emerging careers of the two young artists.  Frank retains an on-going working relationship with both Springsteen and Smith.  Stefanko will be releasing a book in November of 2017, entitled "Bruce Springsteen: Further Up the Road" that chronicles the 40-year working relationship between himself and Bruce Springsteen.

Bruce Springsteen Archives: Bruce Springsteen Archives is an ongoing collection of officially released live albums by Bruce Springsteen & The E Street Band.  Beginning in November 2014 with the first release, Springsteen sought out to release fully recorded shows from his past archives officially to fans for purchase through http://live.brucespringsteen.net.  The idea originally came after Springsteen released every concert from his High Hopes Tour for fans to purchase.  Some of the shows have been previously released unofficially through lower quality bootlegs circulating amongst fans for many years but now have been digitally restored and remastered for the first time and officially endorsed for release by Springsteen.  Fans have the option of purchasing the album through digital download or CD.

The Fever (Bruce Springsteen song): "The Fever" is an early Bruce Springsteen song, recorded and released on an extremely rare 7" demo to promote the band, coupled with 'Rendezvous', a live track recorded in New York, although the venue and date remain a mystery - Rendezvous opens with Bruce calling out "New York!  Go ahead, Max!" .  The single was released under The Jersey Devil and was pressed on Bruce Records, which was Springsteen's own independent label for his band.  The Fever itself was performed by Springsteen in concert beginning in March 1973.  It was recorded in 914 Sound Studios in May 1973, during sessions for Springsteen's second album "The Wild, the Innocent & the E Street Shuffle", but was only used as a demo by manager Mike Appel's Laurel Canyon publishing arm and renamed "Fever For the Girl".  In early 1974 Appel sent it to several progressive rock radio stations, where it became a "turntable hit" in the ramp-up of Springsteen expectations prior to "Born to Run".  The original Springsteen recording finally achieved an official release surfacing in 1999 on his "18 Tracks" outtakes collection- the live b-side has never been officially released since in any other format, although a different live version is on 18 Tracks and Tracks (Bruce Springsteen album) and a studio cut of Rendezvous was released on 'The Promise' CD in 2010.

Question: What is special about Wachovia Spectrum by Bruce Springsteen?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "album_title": {
      "type": "string",
      "description": "The full title of the album."
    },
    "album_type": {
      "type": "string",
      "description": "The type of album, e.g., 'live album'."
    },
    "release_date": {
      "type": "string",
      "format": "date",
      "description": "The release date of the album."
    },
    "archive_release_number": {
      "type": "integer",
      "description": "The sequential number of the release within the Bruce Springsteen Archives."
    },
    "performance_details": {
      "type": "object",
      "properties": {
        "venue_name": {
          "type": "string",
          "description": "The name of the venue where the performance took place."
        },
        "venue_location": {
          "type": "string",
          "description": "The location of the venue."
        },
        "performance_significance": {
          "type": "string",
          "description": "A description of why this particular performance was notable."
        }
      },
      "required": [
        "venue_name",
        "venue_location",
        "performance_significance"
      ],
      "additionalProperties": false
    },
    "notable_performances": {
      "type": "object",
      "properties": {
        "full_album_performed": {
          "type": "string",
          "description": "The title of the album that was performed in its entirety during the show."
        },
        "rare_song_performances": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "song_title": {
                "type": "string",
                "description": "The title of a song performed that was notable for its rarity."
              },
              "first_performance_since_year": {
                "type": "integer",
                "description": "The year since which the song had not been performed."
              }
            },
            "required": [
              "song_title",
              "first_performance_since_year"
            ],
            "additionalProperties": false
          }
        }
      },
      "required": [
        "full_album_performed",
        "rare_song_performances"
      ],
      "additionalProperties": false
    },
    "guest_appearances": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the guest performer."
          },
          "role": {
            "type": "string",
            "description": "The role or relationship of the guest performer."
          }
        },
        "required": [
          "name",
          "role"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "album_title",
    "album_type",
    "release_date",
    "archive_release_number",
    "performance_details",
    "notable_performances",
    "guest_appearances"
  ],
  "additionalProperties": false
}
