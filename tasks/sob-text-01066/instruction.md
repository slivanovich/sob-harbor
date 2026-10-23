{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLive at Clark University: Live at Clark University is a posthumous live album by The Jimi Hendrix Experience, released on July 6, 1999 by Dagger Records.  The album documents the band's performance at Clark University in Worcester, Massachusetts on March 15, 1968. \" Fire\", \"Red House\" and \"Foxey Lady\", as well as the two interviews with Jimi Hendrix, were featured on the companion CD to the 2007 book \"Jimi Hendrix: An Illustrated Experience\".  The album was re-released on vinyl in 2010 as part of Record Store Day.\n\nThe Kennedy Experience: The Kennedy Experience is a music group and eponymous instrumental album conceived and produced in 1999 by violinist Nigel Kennedy.  The album is largely derived from the music of rock guitarist Jimi Hendrix and the title references his group The Jimi Hendrix Experience.  According to a BBC interview with Kennedy, the violinist stated that the recording is \"an album of music inspired by Jimi Hendrix.  It is an extended instrumental work in six movements, each movement a classical interpretation of a Hendrix song\".  On the recording, Kennedy is accompanied by seven other musicians, and the lineup includes two cellos, an oboe, two guitars, a Dobro, flute, and double bass.  With cellist Lynn Harrell, he has recorded an album of duets.\n\nThe Jimi Hendrix Experience: The Jimi Hendrix Experience was an American-English rock band that formed in Westminster, London, in September 1966.  Singer, songwriter, and guitarist Jimi Hendrix, bassist and backing vocalist Noel Redding, and drummer Mitch Mitchell comprised the group, which was active until June 1969.  During this time, they released three studio albums and became one of the most popular acts in rock.  In April 1970, Hendrix, Mitchell, and bassist Billy Cox performed and recorded until Hendrix's death on September 18, 1970.  This later trio was sometimes billed as the \"Jimi Hendrix Experience\", but the title was never formalized.\n\nAre You Experienced? (song): \"Are You Experienced?\"  is the title song for the Jimi Hendrix Experience 1967 debut album.  It has been described as one of Jimi Hendrix's most original compositions on the album by writer Keith Shadwick.  The song is largely based on one chord and has a drone-like quality reminiscent of Indian classical music.  It features recorded guitar and drum parts that are played backwards and a repeating piano chord, but no bass.  Live recordings from 1968 are found on \"The Jimi Hendrix Concerts\" album and \"Winterland\" box set.\n\nI Don't Live Today: \"I Don't Live Today\" is a song by the Jimi Hendrix Experience, released on May 12, 1967, on the band's debut album \"Are You Experienced\".  In honor of his Cherokee heritage, Hendrix dedicated the song to the American Indians and other minority groups.\n\nJimi Plays Monterey: Jimi Plays Monterey is a posthumous live album by Jimi Hendrix released in February 1986.  The album documents The Jimi Hendrix Experience's performance at the Monterey Pop Festival on June 18, 1967.  As well as songs from the band's debut album \"Are You Experienced\", \"Monterey\" also includes covers of \"Killing Floor\" (Howlin' Wolf), \"Like a Rolling Stone\" (Bob Dylan), \"Rock Me Baby\" (B. B. King) and \"Wild Thing\" (Chip Taylor).  The version of \"Wild Thing\" on the album is one of the most notable live performances ever, as, in an iconic moment in rock history, he sets his guitar alight after the song and then smashes it.\n\nFire: The Jimi Hendrix Collection: Fire: The Jimi Hendrix Collection is a posthumous compilation album by American blues-rock musician Jimi Hendrix.  Released on June 7, 2010, the album features 20 songs from throughout the career of The Jimi Hendrix Experience and Hendrix as a solo musician, including \"Valleys of Neptune\", only officially released on the album of the same name in March 2010.  Released by CMG, the album is named after The Experience song \"Fire\", originally released on the band's debut album \"Are You Experienced\" in 1967.\n\nExperience Hendrix: The Best of Jimi Hendrix: Experience Hendrix: The Best of Jimi Hendrix is a compilation album of Jimi Hendrix songs released in 1997.  The single compact disc collects 20 songs spanning his career from his first recordings with the Jimi Hendrix Experience in 1966 to his last with Billy Cox and Mitch Mitchell in 1970.\n\nFreedom: Atlanta Pop Festival: Freedom: Atlanta Pop Festival is a posthumous live album by The Jimi Hendrix Experience, documenting their July 4, 1970 performance at the Atlanta International Pop Festival.  Billy Cox and Mitch Mitchell accompany Hendrix.  It features sixteen songs recorded during their evening performance, some of which appeared on the 1991 live compilation \"Stages\".  However, neither album contains all the songs played, as both omit Hey Baby (New Rising Sun) with which Jimi closed the show.  The album was released on August 28, 2015, in conjunction with the Jimi Hendrix video documentary, Jimi Hendrix: Electric Church.\n\nAre You Experienced: Are You Experienced is the debut studio album by English-American rock band the Jimi Hendrix Experience.  Released in 1967, the LP was an immediate critical and commercial success, and it is widely regarded as one of the greatest debuts in the history of rock music.  The album features Jimi Hendrix's innovative approach to songwriting and electric guitar playing which soon established a new direction in psychedelic and hard rock music.\n\nQuestion: The song on the band's debut album, Are You Experienced, by the Jimi Hendrix Experience, released on which date?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"song_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the song.\"\n    },\n    \"album_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the album the song is on.\"\n    },\n    \"band_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the band that performed the song.\"\n    },\n    \"release_date\": {\n      \"type\": \"string\",\n      \"format\": \"date\",\n      \"description\": \"The release date of the song.\"\n    }\n  },\n  \"required\": [\n    \"song_title\",\n    \"album_title\",\n    \"band_name\",\n    \"release_date\"\n  ],\n  \"additionalProperties\": false\n}"
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
        "description": "The title of the album the song is on."
      },
      "band_name": {
        "type": "string",
        "description": "The name of the band that performed the song."
      },
      "release_date": {
        "type": "string",
        "format": "date",
        "description": "The release date of the song."
      }
    },
    "required": [
      "song_title",
      "album_title",
      "band_name",
      "release_date"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
