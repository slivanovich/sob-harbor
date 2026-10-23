{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nTrey Songz: Tremaine Aldon Neverson (born November 28, 1984), better known as Trey Songz, is an American singer, songwriter, rapper and actor.  His debut album, \"I Gotta Make It\", was released in 2005 through Atlantic Records.  His follow-up album, \"Trey Day\", spawned his first top 20 single, \"Can't Help but Wait\".  Songz released his third album \"Ready\" in 2009 and a single from the album, \"Say Aah\", peaked at No. 9 on the \"Billboard\" Hot 100 making it Songz's first top 10 hit.  \"Ready\" was nominated for Best Male R&B Vocal Performance at the 2008 Grammy Awards.  The following year saw Songz's highest charting song to date, \"Bottoms Up\" featuring rapper Nicki Minaj from his fourth studio album, \"Passion, Pain & Pleasure\".\n\nNick Fowler: Nicholas Russel Fowler is a singer, songwriter, novelist, journalist, poet and actor born in Fürth, Germany.\n\nBawitdaba: \"Bawitdaba\" is a song by American singer-songwriter and rapper Kid Rock, the third single off his Atlantic Records debut \"Devil Without a Cause\", released in 1998.\n\nJoivan Jiménez: Joivan Jiménez (born October 25, 1980) is a singer-songwriter, musician and actor born in Panama City, Panama.  He is a Dove Award-nominated singer and songwriter for the Spanish-Language Recorded Song of The Year \"“Generación de Fuego.”\"  In 2004 he was a member of the group Ordained Praise produced by record producer Justin Boller.  The group was signed to a Christian independent record label, Sereniti Records.  In 2008 after the group disbanded, Jiménez became a solo artist.  In 2012 he played the role of Juan Carlos Reymundo in the Independent film \"\"Stand Your Ground\"” filmed in Atlanta.  Jiménez is the 2012 National Vanheusen Fashion Superbowl “In Style” sweepstakes winner, featured in ESPN The Next Magazine, GQ Magazine, with others who had been inducted into the Hall of Fame, such as Jerry Rice, Steve Young and Deion Sanders.\n\nScream (Timbaland song): \"Scream\" is a song performed by American producer, songwriter and rapper Timbaland, released as the fifth and final single from his second studio album \"Shock Value\" (2007).  The song features vocals from American singer and songwriter Keri Hilson and the lead singer of the Pussycat Dolls Nicole Scherzinger.  Mosley and Hilson co-wrote the song with American producer Danja, who co-produced the song with Timbaland.  Mosley Music Group, in association with Blackground Records and Interscope Records, serviced the song to mainstream radios in the United States on December 11, 2007.\n\nKid Rock: Robert James Ritchie (born January 17, 1971), known professionally as Kid Rock, is an American singer, rapper, songwriter, musician, record producer, and actor.  His 1998 album \"Devil Without a Cause\" sold 14 million copies worldwide.  He is a five-time Grammy Award nominee and has sold 25 million albums in the U.S. according to Nielsen SoundScan.  The RIAA certified him selling 23.5 million albums.  He has sold over 35 million records worldwide.\n\nGive It to Me (Timbaland song): \"Give It to Me\" is a song performed by American producer, songwriter and rapper Timbaland, released as the first single from his second studio album \"Shock Value\" (2007).  The song features vocals by Canadian singer and songwriter Nelly Furtado and American singer Justin Timberlake.  All three artists co-wrote the song together with American rapper Attitude and American producer Danja, who produced the song with Timbaland.  Mosley Music Group, in association with Blackground Records and Interscope Records, serviced the song to contemporary hit and rhythmic radios in the United States on 4 February 2007 and later to urban radios on 10 March 2007.  \"Give It to Me\" is an electro song that embodies the sensibilities of club music.  The song features the protagonists addressing their critics about their successes in the music industry.\n\nTyga discography: The discography of Tyga, an American rapper, consists of four studio albums, two compilation albums, fourteen mixtapes, eight singles (including four as a featured artist) and forty-eight music videos.  In 2008, Tyga released his first studio album, \"No Introduction\", on the record label Decaydance Records.  The album featured the single \"Coconut Juice\", which features singer Travie McCoy; the song peaked at number 94 on the US \"Billboard\" Hot 100, becoming Tyga's first song to appear on the chart.  In 2010, Tyga and American singer Chris Brown released the collaborative mixtape \"Fan of a Fan\", which included the single \"Deuces\": the song peaked at number 14 on the \"Billboard\" Hot 100 and became Tyga's first song to chart on the US Hot R&B/Hip-Hop Songs chart, peaking at number thirty.  Tyga also appeared on the song \"Loyalty\", a single by fellow rapper Birdman, and collaborated with rapper Lil Wayne on the non-album single \"I'm on It\", both of which failed to chart on the \"Billboard\" Hot 100.\n\nJive Jones: Jive Jones, JIVEjones, or simply JIVE (born August 30, 1980) is a singer, songwriter, producer, model, and actor born and raised as Denny Kleinman in Miami, Florida.  He released his debut solo album \"Me, Myself, & I\" on Jive Records.  Singles released from the album include the title track and \"I Belong\", a guitar-driven love song.  His single \"Me, Myself, & I\" was featured on the 2001 compilation album \"Now That's What I Call Music!  8\".\n\nLil Zane: Zane R. Copeland Jr. (born July 11, 1982), better known as Lil Zane, is an American rapper and actor born in Yonkers, New York and raised in Atlanta, Georgia.  He is best known for his debut album \"\", released in 2000, which featured the single \"Callin' Me\" featuring 112.\n\nQuestion: When was the American singer, rapper, songwriter and actor born who's song is \"Bawitdaba\"?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"artist_name\": {\n      \"type\": \"string\",\n      \"description\": \"The professional name of the artist.\"\n    },\n    \"song_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the song mentioned in the question.\"\n    },\n    \"artist_birth_date\": {\n      \"type\": \"string\",\n      \"description\": \"The birth date of the artist.\"\n    },\n    \"artist_nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the artist.\"\n    },\n    \"artist_occupations\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of occupations of the artist.\"\n    }\n  },\n  \"required\": [\n    \"artist_name\",\n    \"song_title\",\n    \"artist_birth_date\",\n    \"artist_nationality\",\n    \"artist_occupations\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "artist_name": {
        "type": "string",
        "description": "The professional name of the artist."
      },
      "song_title": {
        "type": "string",
        "description": "The title of the song mentioned in the question."
      },
      "artist_birth_date": {
        "type": "string",
        "description": "The birth date of the artist."
      },
      "artist_nationality": {
        "type": "string",
        "description": "The nationality of the artist."
      },
      "artist_occupations": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of occupations of the artist."
      }
    },
    "required": [
      "artist_name",
      "song_title",
      "artist_birth_date",
      "artist_nationality",
      "artist_occupations"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
