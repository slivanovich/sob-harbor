{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nA World Without Love: \"A World Without Love\" is a song recorded by the English duo Peter and Gordon and released as their first single in February 1964.  It was included on the duo's debut album in the UK, and in the US on an album of the same name.  The song was written by Paul McCartney and attributed to Lennon–McCartney.  The B-side was \"If I Were You\", written by Peter and Gordon.\n\nGirlfriend (Paul McCartney song): \"Girlfriend\" is a song written by Paul McCartney.  McCartney thought of the song as one that Michael Jackson might like to record, and mentioned this to Jackson at a party in Hollywood.  Jackson had stated in interviews with the music press in the 1970s that he was a fan of The Beatles and the chance to record a McCartney original helped to inspire his next project.  However, McCartney ended up recording it himself with his band Wings, and it was issued in 1978 on the album \"London Town\".  Subsequently, it was suggested by Quincy Jones as a possible track for Jackson to record for his 1979 album \"Off the Wall\".  Jones was unaware that the song had been written for Jackson in the first place.  Jackson's recording omitted the middle eight heard in McCartney's version.  It was issued exclusively in the UK in 1980, as the fifth and final single from the \"Off the Wall\" album.  This proved to be another hit single for Jackson and one of his first recordings of a Paul McCartney song.\n\nOnce Upon a Long Ago: \"Once Upon a Long Ago\" is a Paul McCartney song, released as his fortieth single on 16 November 1987, as part of his compilation \"All the Best! \", released two weeks before the single.  The track was produced by Phil Ramone and mixed by George Martin, and features violin by Nigel Kennedy.\n\nShe's My Baby (Wings song): \"She's My Baby\" is a song credited to Paul and Linda McCartney that was first released by Wings on their 1976 album \"Wings at the Speed of Sound\".  It is a love song sung by Paul directed at Linda.  Critical opinion of the song has ranged from a description as Paul McCartney's \"sweetest, daftest love song\" to a suggestion that it deserves an \"honor for sheer awfulness.\"  In 1998, after Linda's death, Paul McCartney rearranged the song for string quartet to be played at memorial concerts for his late wife.  This version was included on the 1999 album \"Working Classical\".\n\nMellow Dubmarine: Mellow Dubmarine is a double album featuring reggae covers of various Beatles songs.  A handful of Wings, Paul McCartney, John Lennon and George Harrison solo tracks are also featured.  The tracks compiled were apparently recorded between the late 1960s and 2000.  Several songs are covered by more than one artist - for example, there are three versions of \"Let It Be\".  The album is hard to find in stores.\n\nDel Davis (singer): Del Davis is a reggae singer of the 1970s.  His cover of \"World Without Love\" was featured on \"Mellow Dubmarine\".\n\nJust a Ride: \"Just a Ride\" is the second single released by Jem from her debut album \"Finally Woken\".  The song was featured on \"\", along with \"Maybe I'm Amazed\" (a cover of the Paul McCartney song).\n\nShe's Leaving Home: \"She's Leaving Home\" is a Lennon–McCartney song, released in 1967 on the Beatles album \"Sgt. Pepper's Lonely Hearts Club Band\".  Paul McCartney wrote and sang the verse and John Lennon wrote the chorus, which they sang together.  Neither George Harrison nor Ringo Starr was involved in the recording.  The song's instrumental background was performed entirely by a small string orchestra arranged by Mike Leander, and was one of only a handful of Beatles songs in which the members did not play any instruments on the recording.\n\nAlan Whitehead (drummer): Alan Whitehead is a British musician and businessman.  He started his career in the music industry in 1966 as the drummer for Crispian St. Peters, but is best known as a member of Marmalade, whose most successful single in the UK was a cover version of the Paul McCartney song \"Ob-La-Di, Ob-La-Da\".  In 1969 Marmalade were signed to Decca Records and their next song \"Reflections of My Life\" became a number 10 hit in the USA.  Whitehead left the band in 1978 and set up his own management company, negotiating his first production contract with EMI Records.  Groups that he successfully managed were Lipps Inc., Mel and Kim, Modern Romance and Rikki Peebles.  He later went on to manage all girl groups Amazulu and Belle Stars.\n\nBrian Kay: Brian Christopher Kay (born 12 May 1944) is an English radio presenter, conductor and singer.  He is well known as the bass in the King's Singers during the group's formative years from 1968 until 1982, and as such is to be heard on many of their 1970s LP recordings.  He was also the voice of Papageno in the film \"Amadeus\" and the lowest frog in the Paul McCartney song \"We All Stand Together\" (The Frog's Chorus).\n\nQuestion: Which Paul McCartney song did Del Davis sing on \"Mellow Dubmarine.\"\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"song_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the song.\"\n    },\n    \"original_writer\": {\n      \"type\": \"string\",\n      \"description\": \"The original writer of the song.\"\n    },\n    \"performer_on_album\": {\n      \"type\": \"string\",\n      \"description\": \"The artist who performed the song on the specified album.\"\n    },\n    \"album_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the album where the song was featured.\"\n    },\n    \"album_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the album.\"\n    }\n  },\n  \"required\": [\n    \"song_title\",\n    \"original_writer\",\n    \"performer_on_album\",\n    \"album_title\",\n    \"album_genre\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "song_title": {
        "type": "string",
        "description": "The title of the song."
      },
      "original_writer": {
        "type": "string",
        "description": "The original writer of the song."
      },
      "performer_on_album": {
        "type": "string",
        "description": "The artist who performed the song on the specified album."
      },
      "album_title": {
        "type": "string",
        "description": "The title of the album where the song was featured."
      },
      "album_genre": {
        "type": "string",
        "description": "The genre of the album."
      }
    },
    "required": [
      "song_title",
      "original_writer",
      "performer_on_album",
      "album_title",
      "album_genre"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
