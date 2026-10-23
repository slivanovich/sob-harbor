{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nOne More Night (Phil Collins song): \"One More Night\" is the first single in the United States and second in the United Kingdom from Phil Collins' third album, the Diamond-certified \"No Jacket Required\".  \"One More Night\" was Phil Collins' second U.S. No. 1 single, following \"Against All Odds\", and was his fourth single to reach the top ten in the UK, peaking at No. 4 on the singles chart.  In the U.S., the single entered the Billboard Hot 100 at number 50 on the chart dated February 9, 1985.  It hit number one seven weeks later and remained on top for two weeks.  In the UK,the single was certified silver by the British Phonographic Industry.  It was also his first No. 1 on the U.S. Adult contemporary chart.\n\nHits (Phil Collins album): Hits (stylized as ...Hits), released in 1998 and again in 2008, following the success of \"In the Air Tonight\" on the Cadbury ad campaign, is the first greatest hits album by English singer-songwriter Phil Collins.  The collection included fourteen Top 40 hits, including seven American number 1 songs, spanning from the albums \"Face Value\" (1981) through \"Dance into the Light\" (1996).  One new Collins recording, a cover of Cyndi Lauper's \"True Colors\", also appeared on the collection and was a popular song on adult contemporary stations.  \"Hits\" was also the first Phil Collins album to include four songs originally recorded for motion pictures (all of them U.S. number 1 hits) as well as his popular duet with Philip Bailey, \"Easy Lover\" (a UK number 1 hit).\n\nSomething Happened on the Way to Heaven: \"Something Happened on the Way to Heaven\" is a song performed by Phil Collins and released in 1990, from the album \"...But Seriously\".  The song reached the #4 spot on the \"Billboard\" Hot 100 charts that same year.  A live performance of the song also appears on the \"Serious Hits... Live! \" album.  The song was written by Phil Collins and Daryl Stuermer and was produced by Phil Collins and Hugh Padgham.  It was also included on \"...Hits\" on which it is the track number eight.  The cover art shown here is a still from the 1946 film \"A Matter of Life and Death\" by Powell and Pressburger.  The single's UK release featured a different cover, depicting comedian Tony Hancock.  The song was originally written for the movie \"War of the Roses\".\n\nFading Lights: Fading Lights is the twelfth and final song on the album \"We Can't Dance\" by Genesis.  It is also one of the last songs that would include Phil Collins as a member of the progressive rock group.  The song was written by Tony Banks, Phil Collins, and Mike Rutherford.  It is also the longest song on the album.  The lyrics were written by Tony Banks.\n\nA Hot Night in Paris: A Hot Night in Paris is the only album by The Phil Collins Big Band, released in 1999 by Atlantic Records.  Fronted by Genesis lead singer Phil Collins, the album did not contain any singing.  Instead, the album consisted of big band renditions of primarily Collins and Genesis songs, with Collins remaining at the drums.\n\nNo One Is to Blame: \"No One Is to Blame\" is a song by British musician Howard Jones.  The song, in its original version, can be found on his second studio album, \"Dream into Action\", which was released in 1985.  Following the success of the previous singles taken from the album, the original track for \"No One Is to Blame\" was re-recorded to give the song a more radio-friendly sound.  Phil Collins and Hugh Padgham produced the re-recording, with Collins adding his own backing vocals and drum work.  This new version of the song was included on the 1986 US EP \"Action Replay\" as well as the CD version of Jones's 1986 studio album, \"One to One\".\n\nPhil Collins: Philip David Charles Collins {'1': \", '2': \", '3': \", '4': \"} (born 30 January 1951) is an English drummer, songwriter, record producer, actor and singer.  He is the drummer and lead singer of the rock band Genesis and is also a solo artist.  Between 1983 and 1990, Collins scored three UK and seven US number-one singles in his solo career.  When his work with Genesis, his work with other artists, as well as his solo career is totalled, Collins has more US Top 40 singles than any other artist during the 1980s.  His most successful singles from the period include \"In the Air Tonight\", \"Against All Odds (Take a Look at Me Now)\", \"One More Night\", \"Sussudio\" and \"Another Day in Paradise\".\n\nThe Phil Collins Big Band: The Phil Collins Big Band was a side project of English rock drummer, singer and musician Phil Collins, which performed in 1996 and 1998.\n\nLoco in Acapulco: \"Loco in Acapulco\" was a 1988 hit song by the Four Tops.  It was written and produced by Phil Collins (who also played drums) and Lamont Dozier (one third of the group's legendary Motown long-time songwriting team, Holland–Dozier–Holland), for the soundtrack to the film \"Buster\", that also starred Phil Collins in the title role.\n\nHugh Padgham: Hugh Charles Padgham (born 15 February 1955) is an English record producer and audio engineer.  He has won four Grammy Awards, for Producer of the Year and Album of the Year for 1985, Record of the Year for 1990, and Engineer of the Year for 1993.  A 1992 poll in \"Mix\" magazine voted him one of the world's Top Ten Most Influential Producers.  Padgham co-productions include hits by Phil Collins, Genesis, The Human League, Sting, and The Police.  He pioneered (with musician Peter Gabriel and producer Steve Lillywhite) the gated reverb drum sound used most famously on the Phil Collins hit \"In the Air Tonight\".\n\nQuestion: Among Phil Collins' production credits in the mid-1980s is No One Is to Blame by which singer?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"song_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the song.\"\n    },\n    \"primary_artist\": {\n      \"type\": \"string\",\n      \"description\": \"The main singer or artist of the song.\"\n    },\n    \"producers\": {\n      \"type\": \"array\",\n      \"description\": \"A list of individuals credited as producers for the song.\",\n      \"items\": {\n        \"type\": \"string\"\n      }\n    },\n    \"production_period\": {\n      \"type\": \"string\",\n      \"description\": \"The period when the song was produced or re-recorded.\"\n    }\n  },\n  \"required\": [\n    \"song_title\",\n    \"primary_artist\",\n    \"producers\",\n    \"production_period\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "song_title": {
        "type": "string",
        "description": "The title of the song."
      },
      "primary_artist": {
        "type": "string",
        "description": "The main singer or artist of the song."
      },
      "producers": {
        "type": "array",
        "description": "A list of individuals credited as producers for the song.",
        "items": {
          "type": "string"
        }
      },
      "production_period": {
        "type": "string",
        "description": "The period when the song was produced or re-recorded."
      }
    },
    "required": [
      "song_title",
      "primary_artist",
      "producers",
      "production_period"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
