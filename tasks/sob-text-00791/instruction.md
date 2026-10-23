{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBuddha's Dispensation: Buddha's Dispensation (Buddha-sasana) is the time period which Dharma (Pali Canon) exist and follow.  It is totally 5000 years after the Buddha's Parinirvana (pass away or \"Skandha Parinirvana\").  There are three types of Parinirvana those are \"Klesha Parinirwana\", \"Skandha Parinirvana\" and \"Dhatu Parinirvana\".\n\nRoll on the Red Tour: The Roll on the Red Tour was a concert tour by American rock band Red Hot Chili Peppers.  The tour followed the band's hugely successful \"By the Way tour\".  During this tour the band recorded their first live album, Live in Hyde Park.  Near the tour's end, the dates mainly consisted of benefit and tribute shows including the Bridge School Benefit and a tribute show to longtime friend, Johnny Ramone.  The band's performance was released two years later on DVD as \"Too Tough to Die: A Tribute to Johnny Ramone\".  Ramone, who was too sick to attend the tribute (although show host, Rob Zombie called him during the event), would pass away a three days after the tribute show.  John Frusciante was among many famous friends and family to attend his funeral and memorial celebration.  On March 17, 2015, the band released \"\" a free MP3 download of the entire show through their website.\n\nSam Cooke: Samuel Dale \"Sam\" Cook (January 22, 1931 – December 11, 1964), was an American singer, songwriter, and entrepreneur.\n\nTwistin' the Night Away: \"Twistin' the Night Away\" is a song written and recorded by Sam Cooke.  It was released as a single in 1962 and became very popular, charting in the top ten of both the \"Billboard\" Hot 100 (#9) and Billboard's R&B chart (#1).  \"Twistin' the Night Away\" was successful overseas as well, peaking at #6 on the UK Singles Chart.\n\nDance the Night Away (Van Halen song): \"Dance the Night Away\" was Van Halen's first top 20 U.S. hit, peaking at #15, and the second song from their 1979 album \"Van Halen II\".  While the rest of the songs from this album had existed in various forms since their days doing demos and playing clubs, this song was possibly the only song written during the recording sessions for the album.  The band members conceived the song during the recording sessions while they were standing in a circle humming to each other.  It was inspired by Fleetwood Mac's \"Go Your Own Way\".  Eddie Van Halen purposely left a guitar solo out of the final version of the song, replacing it instead with a riff of tap harmonics.  David Lee Roth originally wanted to call the song \"Dance Lolita Dance\", but Eddie Van Halen convinced him that \"Dance the Night Away\" was more suitable and the chorus was changed to reflect that.\n\nWord taboo: Word taboo is the restricted use of words due to social constraints.  The taboo against naming the dead in parts of the world is an example.  Taboo words are commonly avoided with euphemisms, such as the English euphemism \"pass away\", meaning \"die\".  It is a common source of neologisms and lexical replacement.\n\nSing the Night Away: Sing the Night Away is a 5 track EP (plus the Bonus Track) by New Zealand punk band Steriogram.  It was released at concerts during the 2002 NZ Schools Tour.  A music video was made for the song \"Sing The Night Away\" although none of these tracks made their debut album Schmack! .  \"Sing the Night Away\", \"Free\", and \"Big Lady Loving\" featured on singles from the album Schmack! , and \"White Trash (DLT remix)\" features on the Schmack!  2005 Special Tour Edition.  West Side!  is the only song not to feature on another album or single.\n\nTrampoline (The Mavericks album): Trampoline is the fifth studio album by the American country music band The Mavericks.  The album was released on March 10, 1998, by MCA Nashville.  It includes the singles \"To Be with You\", \"Dance the Night Away\" and \"I've Got This Feeling\".  Although none of these singles were Top 40 hits on the U.S. country charts, \"Dance the Night Away\" reached #4 on the UK Singles Chart and \"I've Got This Feeling\" reached #27.\n\nNever a Dull Moment (Rod Stewart album): Never a Dull Moment is the fourth solo album by rock musician Rod Stewart.  It was released in the summer of 1972; that year it became a UK number-one album (for two weeks) and reached number two on the US Album chart.  The track \"You Wear It Well\", co-written by Stewart and classical guitarist Martin Quittenton, was a smash hit (another UK No. 1; in US No. 13), as well as \"Twisting the Night Away\", a song originally recorded (and written) by Sam Cooke.\n\nTwistin' the Night Away (album): Twistin' the Night Away is the tenth studio album by American singer-songwriter Sam Cooke.  Produced by Hugo & Luigi, the album was released in April 1962 in the United States by RCA Victor.  \"Twistin' the Night Away\" primarily capitalizes on the twist phenomenon and as a result became one of Cooke's most successful LPs, becoming his second to chart and creating a string of chart successes.\n\nQuestion: When did the singer who originally recorded \"Twisting the Night Away\" pass away?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"song_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the song in question.\"\n    },\n    \"original_artist_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the artist who originally recorded the song.\"\n    },\n    \"artist_birth_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth year of the original artist.\"\n    },\n    \"artist_death_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The death year of the original artist.\"\n    },\n    \"song_single_release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the song was released as a single.\"\n    }\n  },\n  \"required\": [\n    \"song_title\",\n    \"original_artist_name\",\n    \"artist_birth_year\",\n    \"artist_death_year\",\n    \"song_single_release_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "song_title": {
        "type": "string",
        "description": "The title of the song in question."
      },
      "original_artist_name": {
        "type": "string",
        "description": "The name of the artist who originally recorded the song."
      },
      "artist_birth_year": {
        "type": "integer",
        "description": "The birth year of the original artist."
      },
      "artist_death_year": {
        "type": "integer",
        "description": "The death year of the original artist."
      },
      "song_single_release_year": {
        "type": "integer",
        "description": "The year the song was released as a single."
      }
    },
    "required": [
      "song_title",
      "original_artist_name",
      "artist_birth_year",
      "artist_death_year",
      "song_single_release_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
