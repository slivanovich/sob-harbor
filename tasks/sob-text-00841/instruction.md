{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSgt. Pepper's Lonely Hearts Club Band (song): \"Sgt. Pepper's Lonely Hearts Club Band\" is a song written by Paul McCartney (credited to Lennon–McCartney), and first recorded and released in 1967, on the album of the same name by the Beatles.  The song appears twice on the album: as the opening track (segueing into \"With a Little Help from My Friends\"), and as \"Sgt. Pepper's Lonely Hearts Club Band (Reprise)\", the penultimate track (segueing into \"A Day in the Life\").  As the title song, the lyrics introduce the fictional band that performs on the album.\n\nSgt. Pepper Live: Sgt. Pepper Live is a performance by the American rock band Cheap Trick with a full orchestra, released on August 25, 2009, in commemoration of the 42nd anniversary of the release of the historic album \"Sgt. Pepper's Lonely Hearts Club Band\" by the Beatles.  Both a live album and a companion DVD of the performance were released.  The album was engineered by Geoff Emerick.  Cheap Trick performed the \"Sgt. Pepper Live\" show at the Las Vegas Hilton for two weeks in September 2009.\n\nSgt. Pepper Knew My Father: Sgt. Pepper Knew My Father is a 1988 multi-artist compilation of 1980s artists recording new versions of the songs on The Beatles album \"Sgt. Pepper's Lonely Hearts Club Band\".  The album was produced by the \"New Musical Express\" to raise money for Childline, the charity founded by the now-defunct BBC1 consumer programme \"That's Life! \".  It was also intended to celebrate the 21st anniversary of the original release of \"Sgt. Pepper's Lonely Hearts Club Band\" on 1 June 1967.\n\nWithin You Without You: \"Within You Without You\" is a song written by George Harrison and released on the Beatles' 1967 album \"Sgt. Pepper's Lonely Hearts Club Band\".  It was Harrison's second composition in the Indian classical style, after \"Love You To\", and was inspired by his six-week stay in India with his mentor and sitar teacher, Ravi Shankar, over September–October 1966.  Recorded in London without the other Beatles, the song features Indian instrumentation such as sitar, dilruba and tabla, and was performed by Harrison and members of the Asian Music Circle.  The recording marked a significant departure from the Beatles' previous work; musically, it evokes the Indian devotional tradition, while the overtly spiritual quality of the lyrics reflects Harrison's absorption in Hindu philosophy and the teachings of the Vedas.  Although the song was his only composition on \"Sgt. Pepper\", Harrison's endorsement of Indian culture was further reflected in the inclusion of yogis such as Paramahansa Yogananda among the crowd depicted on the album cover.\n\nSgt. Pepper's (Big Daddy album): Sgt. Pepper's is a tribute album consisting of covers of the entirety of Sgt. Pepper's Lonely Hearts Club Band by The Beatles.  The album was recorded by Big Daddy in 1992 and features covers which combine the lyrics and some musical elements from the original Beatles versions with stylistic elements of certain genres and musicians, mostly ones popularized in the 1920s-1950s.  The album's release coincided with the 25th anniversary of the original Beatles album.  It was the band's last album until 2013's \"Smashing Songs of Stage and Screen\".\n\nSgt. Pepper's Lonely Hearts Club Band: Sgt. Pepper's Lonely Hearts Club Band is the eighth studio album by English rock band the Beatles.  Released on 26 May 1967 in the United Kingdom and 2 June 1967 in the United States, it was an immediate commercial and critical success, spending 27 weeks at the top of the UK albums chart and 15 weeks at number one in the US.  On release, the album was lauded by the vast majority of critics for its innovations in music production, songwriting and graphic design, for bridging a cultural divide between popular music and legitimate art, and for providing a musical representation of its generation and the contemporary counterculture.  It won four Grammy Awards in 1968, including Album of the Year, the first rock LP to receive this honour.\n\nSgt. Petsound's Lonely Hearts Club Band: Sgt. Petsound's Lonely Hearts Club Band is a track-for-track mash-up of The Beach Boys’ \"Pet Sounds\" with The Beatles’ \"Sgt. Pepper's Lonely Hearts Club Band\" by Clayton Counts, posted on his blog.  It was released under the pseudonym \"The Beachles\" and received favorable mentions in \"Entertainment Weekly\" and \"USA Today\", as well as blogs around the world.  Sometime around September 8, 2006, Counts received a cease and desist order from EMI's attorneys.  Notably, the letter included a demand for Counts to hand over the IP addresses of everyone who downloaded or streamed the songs.  Counts removed the songs, but refused to give up the IPs and fired back with a lengthy missive on his blog.  The incident drew the attention of the Associated Press and \"Rolling Stone\", and resulted in a letter-writing campaign and a boycott of EMI and Capitol Records on behalf of Mr. Counts.\n\nWith a Little Help from My Fwends: With a Little Help from My Fwends is the second main album of the \"Fwends\" series by American rock band the Flaming Lips.  It is a track-for-track tribute to the Beatles album \"Sgt. Pepper's Lonely Hearts Club Band\".  It was released on October 27, 2014, through Warner Bros.  Records.  All proceeds from record sales will go to the Bella Foundation, an organization in Oklahoma City that helps provide veterinary care to needy pet owners.\n\nWith a Little Help from My Friends: \"With a Little Help from My Friends\" is a song by the Beatles, written by John Lennon and Paul McCartney from the album \"Sgt. Pepper's Lonely Hearts Club Band\" issued worldwide in June 1967.  The song was written for and sung by the Beatles' drummer Ringo Starr as the character \"Billy Shears\".  The song, paired with \"Sgt. Pepper's Lonely Hearts Club Band\" and featuring \"A Day in the Life\" as its B-side, was reissued as a single in the U.S. in August 1978 (#71) and in the U.K. in September 1978 (#63).  \"With a Little Help from My Friends\" was ranked No. 311 on \"Rolling Stone\"' s list of the 500 Greatest Songs of All Time.\n\nPaul McCartney: Sir James Paul McCartney, {'1': \", '2': \", '3': \", '4': \"} (born 18 June 1942) is an English singer-songwriter, multi-instrumentalist, and composer.  He gained worldwide fame as the bass guitarist and singer for the rock band the Beatles, widely considered the most popular and influential group in the history of pop music.  His songwriting partnership with John Lennon is the most celebrated of the post-war era.  After the group disbanded in 1970, he pursued a solo career and formed the band Wings with his first wife, Linda, and Denny Laine.\n\nQuestion:  \"With a Little Help from My Friends\" is a song by the Beatles, written by which English singer-songwriter, multi-instrumentalist, and composer, from the album \"Sgt. Pepper's Lonely Hearts Club Band\" issued worldwide in June 1967?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"song_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the song.\"\n    },\n    \"album_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the album the song is from.\"\n    },\n    \"album_release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the album was released.\"\n    },\n    \"song_writers\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of all credited writers for the song.\"\n    },\n    \"identified_composer_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"full_name\": {\n          \"type\": \"string\",\n          \"description\": \"The full name of the composer identified by the specific description in the question.\"\n        },\n        \"description\": {\n          \"type\": \"string\",\n          \"description\": \"The specific professional description of the identified composer as stated in the context/question.\"\n        }\n      },\n      \"required\": [\n        \"full_name\",\n        \"description\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"song_title\",\n    \"album_title\",\n    \"album_release_year\",\n    \"song_writers\",\n    \"identified_composer_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "song_title": {
        "type": "string",
        "description": "The title of the song."
      },
      "album_title": {
        "type": "string",
        "description": "The title of the album the song is from."
      },
      "album_release_year": {
        "type": "integer",
        "description": "The year the album was released."
      },
      "song_writers": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of all credited writers for the song."
      },
      "identified_composer_details": {
        "type": "object",
        "properties": {
          "full_name": {
            "type": "string",
            "description": "The full name of the composer identified by the specific description in the question."
          },
          "description": {
            "type": "string",
            "description": "The specific professional description of the identified composer as stated in the context/question."
          }
        },
        "required": [
          "full_name",
          "description"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "song_title",
      "album_title",
      "album_release_year",
      "song_writers",
      "identified_composer_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
