{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGeorge Jones: George Glenn Jones (September 12, 1931 – April 26, 2013) was an American musician, singer and songwriter.  He achieved international fame for his long list of hit records, including his best known song \"He Stopped Loving Her Today\", as well as his distinctive voice and phrasing.  For the last twenty years of his life, Jones was frequently referred to as the greatest living country singer.  Country music scholar Bill C. Malone writes, \"For the two or three minutes consumed by a song, Jones immerses himself so completely in its lyrics, and in the mood it conveys, that the listener can scarcely avoid becoming similarly involved.\"  Waylon Jennings expressed a similar opinion in his song \"It's Alright\": \"If we all could sound like we wanted to, we'd all sound like George Jones.\"  The shape of his nose and facial features earned Jones the nickname \"The Possum.\"\n\nAntennas to Hell: Antennas to Hell is the first greatest hits compilation album by American metal band Slipknot.  The album was released on July 23, 2012, in the United Kingdom and July 24, 2012, in the United States by Roadrunner Records.  The title is a reference to the critically acclaimed post-rock album \"Lift Your Skinny Fists Like Antennas to Heaven\", released by the band Godspeed You!  Black Emperor in 2000 .  The album features hit singles, fan favorites, and live tracks.  The two-disc version of \"Antennas to Hell\" features a bonus live CD capturing Slipknot's performance at the 2009 Download Festival in Donington Park, England.  The three-disc version includes a bonus DVD featuring every Slipknot music video and ten brand new video features, titled \"Broadcasts from Hell\", created by Shawn Crahan.  It is the first album released by the band since late bassist Paul Gray's death in 2010.  Despite being a greatest hits collection, Clown of Slipknot has stated that it's more of a tribute to what Slipknot were and used to be at the time of the songs, and also said that the collection comes with lots of artwork and DVD content.\n\nCul de Sac (band): Cul de Sac are a rock group formed in 1990 in Boston, Massachusetts and led by guitarist Glenn Jones.  Their music is primarily instrumental.  Jones and keyboardist Robin Amos have been the only constant members.\n\nPost-rock: Post-rock is a form of experimental rock characterized by the influence and use of instruments commonly associated with rock music, but using rhythms and \"guitars as facilitators of timbre and textures\" not traditionally found in rock.  Post-rock bands are often instrumental.  Although firmly rooted in the indie or underground scene of the 1980s and early 1990s, post-rock's style often bears little resemblance musically to that of contemporary indie rock.\n\nThe Epiphany of Glenn Jones: The Epiphany of Glenn Jones is an album by American fingerstyle guitarist and composer John Fahey and the alternative rock/Post-rock band Cul de Sac, released in 1997.\n\nThe Wanting: The Wanting is the fourth solo album by Glenn Jones, guitarist and founding member of the American instrumental band Cul de Sac. \" Mojo\" placed the album at number 33 on its list of \"Top 50 albums of 2011.\"\n\nJones Intercable: Jones Intercable was a cable television company founded by Glenn Jones in 1970.  Jones, already a cable television veteran, had bought his first cable system in Georgetown, Colorado after taking a $400 loan on his Volkswagen.\n\nRobin Amos: Robin Amos is an American keyboardist and founding member of the band Cul de Sac.  His first band was The Girls, a punk band that Amos founded in the late seventies with George Condo, Mark Dagley and Daved Hild.  He continued to explore that band's sound with his next band Shut Up, which he formed with guitarist Glenn Jones.\n\nFinesse (Glenn Jones album): Finesse is the first full-length album released by R&B/soul singer Glenn Jones.  Released in 1984, the album includes one of Jones' early hits, \"Show Me,\" along with the semi-hit \"Bring Back Your Love.\"\n\nInterstate (album): Interstate is the fifth album by American post-rock and instrumental rock band Pell Mell, released in 1995.  After issuing \"Flow\" in 1991, the band members wrote new material separately, sending each other ideas, until more concrete ideas were becoming formed, leading to the band recording \"Interstate\" between two studios in 1993 and 1994.  Defined by a breezy, wide-open sound, \"Interstate\" features sparse, rhythmic guitar riffs, organ playing, drums and thematic instrumentation, in addition to a distinctive compositional style that has been compared to \"the dynamics of a good conversation\" by one critic.  Additionally, the album has been considered a post-rock album and critics have noticed its display of krautrock influences.\n\nQuestion: The post-rock album The Epiphany of Glenn Jones is an album by which guitarist and composer?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"album_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the album.\"\n    },\n    \"artist_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of artist associated with the album.\"\n    },\n    \"artist_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the guitarist and composer.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the album was released.\"\n    }\n  },\n  \"required\": [\n    \"album_title\",\n    \"artist_type\",\n    \"artist_name\",\n    \"release_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "album_title": {
        "type": "string",
        "description": "The title of the album."
      },
      "artist_type": {
        "type": "string",
        "description": "The type of artist associated with the album."
      },
      "artist_name": {
        "type": "string",
        "description": "The name of the guitarist and composer."
      },
      "release_year": {
        "type": "integer",
        "description": "The year the album was released."
      }
    },
    "required": [
      "album_title",
      "artist_type",
      "artist_name",
      "release_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
