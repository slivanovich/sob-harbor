{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nReturn to Pepperland: Return to Pepperland is a cancelled Paul McCartney album recorded in 1984–1987.  The album was built up of mostly home demos and was a reflection of work from McCartney's career as a member of the English rock band the Beatles.  Although it was made around twenty years after the release of the Beatles' 1967 album \"Sgt. Pepper's Lonely Hearts Club Band\" (which inspired it), some tracks which made their way onto the bootleg were written whilst McCartney was in the Beatles, including the Lennon–McCartney-written \"Love Me Do\" and \"P.S. I Love You\".  Other songs turned up on CD-single B-sides including the McCartney/Stewart song \"Don't Break the Promise\".\n\nSgt. Pepper Knew My Father: Sgt. Pepper Knew My Father is a 1988 multi-artist compilation of 1980s artists recording new versions of the songs on The Beatles album \"Sgt. Pepper's Lonely Hearts Club Band\".  The album was produced by the \"New Musical Express\" to raise money for Childline, the charity founded by the now-defunct BBC1 consumer programme \"That's Life! \".  It was also intended to celebrate the 21st anniversary of the original release of \"Sgt. Pepper's Lonely Hearts Club Band\" on 1 June 1967.\n\nI'm the Greatest: \"I'm the Greatest\" is a song written by English musician John Lennon that was released as the opening track of the 1973 album \"Ringo\" by Ringo Starr.  With Starr, Lennon and George Harrison appearing on the track, it marks the only time that three former Beatles recorded together between the band's break-up in 1970 and Lennon's death in 1980.  Lennon wrote the song in December 1970 as a wry comment on his rise to fame, and later tailored the composition for Starr to sing.  Named after one of Muhammad Ali's catchphrases, the song partly evokes the stage-show concept of the Beatles' 1967 album \"Sgt. Pepper's Lonely Hearts Club Band\".\n\nWith a Little Help from My Friends: \"With a Little Help from My Friends\" is a song by the Beatles, written by John Lennon and Paul McCartney from the album \"Sgt. Pepper's Lonely Hearts Club Band\" issued worldwide in June 1967.  The song was written for and sung by the Beatles' drummer Ringo Starr as the character \"Billy Shears\".  The song, paired with \"Sgt. Pepper's Lonely Hearts Club Band\" and featuring \"A Day in the Life\" as its B-side, was reissued as a single in the U.S. in August 1978 (#71) and in the U.K. in September 1978 (#63).  \"With a Little Help from My Friends\" was ranked No. 311 on \"Rolling Stone\"' s list of the 500 Greatest Songs of All Time.\n\nSt. James' Gate: St. James' Gate Brewery (Irish: \"Grúdlann Gheata Naomh Séamuis\" ) is a brewery founded in 1759 in Dublin, Ireland, by Arthur Guinness.  The company is now a part of Diageo, a company formed from the merger of Guinness and Grand Metropolitan in 1997.  The main product of the brewery is Guinness Draught.\n\nGuinness Brewery: St. James' Gate Brewery (Irish: \"Grúdlann Gheata Naomh Séamuis\" ) is a brewery founded in 1759 in Dublin, Ireland, by Arthur Guinness.  The company is now a part of Diageo, a British company formed from the merger of Guinness and Grand Metropolitan in 1997.  The main product of the brewery is Guinness Draught.\n\nFixing a Hole: \"Fixing a Hole\" is a song by the English rock band the Beatles that was released on their 1967 album \"Sgt. Pepper's Lonely Hearts Club Band\".  It was written by Paul McCartney, although credited to Lennon–McCartney.  The Beatles recorded the track in February 1967, with the main session taking place at Regent Sound Studios in central London.  It marked the first time that the Beatles had used a British studio other than EMI's facility at Abbey Road for one of their EMI recordings.\n\nSgt. Pepper's Lonely Hearts Club Band (song): \"Sgt. Pepper's Lonely Hearts Club Band\" is a song written by Paul McCartney (credited to Lennon–McCartney), and first recorded and released in 1967, on the album of the same name by the Beatles.  The song appears twice on the album: as the opening track (segueing into \"With a Little Help from My Friends\"), and as \"Sgt. Pepper's Lonely Hearts Club Band (Reprise)\", the penultimate track (segueing into \"A Day in the Life\").  As the title song, the lyrics introduce the fictional band that performs on the album.\n\nGuinness: Guinness ( ) is an Irish dry stout that originated in the brewery of Arthur Guinness (1725–1803) at St. James's Gate brewery in the capital city of Dublin, Ireland.  Guinness, produced by the Diageo beverages company, is one of the most successful beer brands worldwide.  It is brewed in almost 50 countries and is available in over 120.  Annual sales total of Guinness in 2011 was 850 e6litre .\n\nA Day in the Life: \"A Day in the Life\" is a song by the English rock band the Beatles that was released as the final track of their 1967 album \"Sgt. Pepper's Lonely Hearts Club Band\".  Credited to Lennon–McCartney, the verses were written mainly by John Lennon, with Paul McCartney primarily contributing the song's middle section.  Lennon's lyrics were inspired by contemporary newspaper articles, including a report on the death of Guinness heir Tara Browne.  The recording includes two passages of orchestral glissandos that were partly improvised in the avant-garde style.  As with the sustained piano chord that closes the song, the orchestral passages were added after the Beatles had recorded the main rhythm track.\n\nQuestion: \"A Day in the Life\" is a song by the English rock band the Beatles that was released as the final track of their 1967 album \"Sgt. Pepper's Lonely Hearts Club Band\", Lennon's lyrics were inspired by contemporary newspaper articles, including a report on the death of which Guinness heir, Guinness, is an Irish dry stout that originated in the brewery of Arthur Guinness (1725–1803) at St. James's Gate brewery in the capital city of Dublin, Ireland?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"song_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the song.\"\n    },\n    \"album_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the album the song was released on.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the album was released.\"\n    },\n    \"lyric_inspiration\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"source\": {\n          \"type\": \"string\",\n          \"description\": \"The general source of inspiration for the lyrics.\"\n        },\n        \"inspired_person\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the person whose death inspired part of the lyrics.\"\n        },\n        \"person_connection\": {\n          \"type\": \"string\",\n          \"description\": \"The connection of the inspired person to Guinness.\"\n        }\n      },\n      \"required\": [\n        \"source\",\n        \"inspired_person\",\n        \"person_connection\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"song_title\",\n    \"album_title\",\n    \"release_year\",\n    \"lyric_inspiration\"\n  ],\n  \"additionalProperties\": false\n}"
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
        "description": "The title of the album the song was released on."
      },
      "release_year": {
        "type": "integer",
        "description": "The year the album was released."
      },
      "lyric_inspiration": {
        "type": "object",
        "properties": {
          "source": {
            "type": "string",
            "description": "The general source of inspiration for the lyrics."
          },
          "inspired_person": {
            "type": "string",
            "description": "The name of the person whose death inspired part of the lyrics."
          },
          "person_connection": {
            "type": "string",
            "description": "The connection of the inspired person to Guinness."
          }
        },
        "required": [
          "source",
          "inspired_person",
          "person_connection"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "song_title",
      "album_title",
      "release_year",
      "lyric_inspiration"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
