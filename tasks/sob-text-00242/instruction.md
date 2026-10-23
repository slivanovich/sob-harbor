{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Division Bell: The Division Bell is the fourteenth studio album by the English progressive rock band Pink Floyd, released on 28 March 1994 by EMI Records in the United Kingdom and on 4 April by Columbia Records in the United States.  The album's music was written mostly by guitarist and singer David Gilmour and keyboardist Rick Wright, and features Wright's first lead vocal on a Pink Floyd album since \"The Dark Side of the Moon\" (1973).  Gilmour's new wife, Polly Samson, co-wrote many of the lyrics, which deal with themes of communication.  Recording took place in locations including the band's Britannia Row Studios, and Gilmour's houseboat, \"Astoria\".  The production team included Pink Floyd stalwarts such as producer Bob Ezrin, engineer Andy Jackson and saxophonist Dick Parry.\n\nPink Floyd bootleg recordings: Pink Floyd bootleg recordings are the collections of audio and video recordings of musical performances by the British rock band Pink Floyd, which were never officially released by the band.  The recordings consist of both live performances and outtakes from studio sessions unavailable in official releases.  In some cases, certain bootleg recordings may be highly prized among collectors, as at least 40 songs composed by Pink Floyd have never been officially released.\n\nAtom Heart Mother (suite): \"Atom Heart Mother\" is a six-part suite by the progressive rock band Pink Floyd, composed by all members of the band and Ron Geesin.  It appeared on the \"Atom Heart Mother\" album in 1970, taking up the whole first side of the original vinyl record.  It is Pink Floyd's longest uncut piece (the later \"Shine On You Crazy Diamond\", though longer, was split between two sides of \"Wish You Were Here\").  Pink Floyd performed it live between 1970 and 1972, occasionally with a brass section and choir in 1970–71.\n\nPink Floyd: Pink Floyd were an English rock band formed in London.  They achieved international acclaim with their progressive and psychedelic music.  Distinguished by their use of philosophical lyrics, sonic experimentation, extended compositions, and elaborate live shows, they are one of the most commercially successful and influential groups of popular music history.\n\nBrain Damage (song): \"Brain Damage\" is the ninth track from English rock band Pink Floyd's 1973 album \"The Dark Side of the Moon\".  It was sung on record by Roger Waters (with harmonies by David Gilmour), who would continue to sing it on his solo tours.  Gilmour sang the lead vocal when Pink Floyd performed it live on their 1994 tour (as can be heard on \"Pulse\").  The band originally called this track \"Lunatic\" during live performances and recording sessions.\n\nPerfect Sense, Part I: Perfect Sense, Part I is the third track from the concept album \"Amused to Death\" by ex-Pink Floyd member Roger Waters.  The song is sung partially by Roger Waters but mainly by PP Arnold on both the original album and live shows.\n\nAny Colour You Like: \"Any Colour You Like\" is the eighth track from English progressive rock band Pink Floyd's 1973 album, \"The Dark Side of the Moon\".  It is an instrumental written by David Gilmour, Richard Wright and Nick Mason, making it one of three tracks on the album that Roger Waters did not receive writing credit for, the last Pink Floyd track that Waters had no part in writing while he was still a member, and the last Pink Floyd studio track credited to Mason until \"The Endless River\".\n\nThe Final Cut (album): The Final Cut is the twelfth studio album by the English progressive rock band Pink Floyd, released on 21 March 1983 by Harvest Records in the United Kingdom and on 2 April by Columbia Records in the United States.  It was Pink Floyd's last studio album to include founding member, bass guitarist and songwriter Roger Waters, and their only album on which he alone is credited for writing and composition.  It was also the only Pink Floyd album that does not feature keyboardist Richard Wright.  Waters originally planned \"The Final Cut\" as a soundtrack album for the 1982 film \"Pink Floyd – The Wall\".  With the onset of the Falklands War, he rewrote it as a concept album, exploring what he considered the betrayal of his father, who died serving in the Second World War.  Waters sings most of the lyrics; lead guitarist David Gilmour provides lead vocals on only one track.  The packaging, also designed by Waters, reflects the album's war theme.\n\nA Momentary Lapse of Reason: A Momentary Lapse of Reason is the thirteenth studio album by English progressive rock band Pink Floyd, released in the UK and US in 7 September 1987, on the labels EMI and Columbia.  It followed guitarist David Gilmour's decision to include material recorded for his third solo album on a new Pink Floyd album with drummer Nick Mason and keyboardist Richard Wright.  Although for legal reasons Wright could not be re-admitted to the band, Wright and Mason helped Gilmour craft what became the first Pink Floyd album since the December 1985 departure of bass guitarist, singer, and primary songwriter Roger Waters.\n\nList of songs recorded by Syd Barrett: English musician Syd Barrett recorded many songs during his short career as a musician.  One of the founding members of English rock band Pink Floyd, he was the dominant force of the band in their early years, writing most of the material found on their first album, \"The Piper at the Gates of Dawn\", contributing to their second one, \"A Saucerful of Secrets\", and recording several unreleased songs with the band.  Due to increasing mental illness, Barrett was excluded from Pink Floyd in April 1968 and was subsequently replaced by guitarist David Gilmour.  After Pink Floyd, Barrett would record two solo albums, both released in 1970, before Barrett left the music business entirely in 1972.\n\nQuestion: What member of the English rock band Pink Floyd sang Perfect Sense, Part I?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"song_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the song.\"\n    },\n    \"album_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the album the song appears on.\"\n    },\n    \"pink_floyd_member_singer\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the Pink Floyd member who sang the song.\"\n    },\n    \"singing_contribution_type\": {\n      \"type\": \"string\",\n      \"description\": \"Describes the nature of the Pink Floyd member's vocal contribution (e.g., 'partially', 'lead', 'harmonies').\"\n    },\n    \"other_singers\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of other individuals who sang on the song.\"\n    }\n  },\n  \"required\": [\n    \"song_title\",\n    \"album_title\",\n    \"pink_floyd_member_singer\",\n    \"singing_contribution_type\",\n    \"other_singers\"\n  ],\n  \"additionalProperties\": false\n}"
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
        "description": "The title of the album the song appears on."
      },
      "pink_floyd_member_singer": {
        "type": "string",
        "description": "The name of the Pink Floyd member who sang the song."
      },
      "singing_contribution_type": {
        "type": "string",
        "description": "Describes the nature of the Pink Floyd member's vocal contribution (e.g., 'partially', 'lead', 'harmonies')."
      },
      "other_singers": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of other individuals who sang on the song."
      }
    },
    "required": [
      "song_title",
      "album_title",
      "pink_floyd_member_singer",
      "singing_contribution_type",
      "other_singers"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
