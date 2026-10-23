{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nTequan Richmond: Tequan Richmond (\"Tuh-kwon\"; born October 30, 1992), also known by his stage name, T-Rich, is an American actor and rapper.  Tequan is best known for his role as Drew Rock on the UPN/CW sitcom \"Everybody Hates Chris\".  Richmond played Ray Charles, Jr. (son of singer/musician Ray Charles) in the motion picture \"Ray\".  He currently plays TJ Ashford on the ABC serial \"General Hospital\" since November 2012 and was nominated for a Daytime Emmy for Outstanding Young Actor in 2013 for the drama.\n\nGold Digger (Kanye West song): \"Gold Digger\" is a song recorded by American rapper Kanye West featuring guest vocals by Jamie Foxx.  Released as the second single from West's second album, \"Late Registration\" (2005), \"Gold Digger\" peaked at number one on the US \"Billboard\" Hot 100 on September 6, 2005, becoming West's and Foxx's second number one single.  Co-produced with Jon Brion, the song contains samples of Ray Charles' \"I Got a Woman\".\n\nConfession Blues: \"Confession Blues\" is a song by The Maxin Trio released in 1949 as a single on the Down Beat Records label (later known as Swing Time).  The single featured American rhythm and blues (R&B) musician Ray Charles on piano and vocals.  The song was written by Charles under his birth name Ray Charles Robinson (listed on the recording credits as R. C. Robinson).\n\nModern Sounds in Country and Western Music: Modern Sounds in Country and Western Music is a studio album by American R&B singer-songwriter and musician Ray Charles.  It was recorded by Charles in February 1962 at Capitol Studios in New York City and at United Recording Studios in Hollywood, before being released in April of that year by ABC-Paramount Records.  The album was produced entirely by Charles and conductor Sid Feller, and departed stylistically from the singer's previous rhythm and blues music.  It featured country, folk, and Western music standards reworked by Charles in popular song forms of the time, including R&B, pop, and jazz.\n\nGenius Loves Company: Genius Loves Company is the final studio album by rhythm and blues and soul musician Ray Charles, posthumously released August 31, 2004 on Concord Records.  Recording sessions for the album took place between June 2003 and March 2004.  The album consists of rhythm and blues, soul, country, blues, jazz and pop standards performed by Charles and several guest musicians, such as Natalie Cole, Elton John, James Taylor, Norah Jones, B.B. King, Gladys Knight, Diana Krall, Van Morrison, Willie Nelson and Bonnie Raitt.  \"Genius Loves Company\" was the last album recorded and completed by Charles before his death in June 2004.  This album was released as a double LP in 2014, for a better and warmer sound than CD.\n\nLove You Down: \"Love You Down\" is the title of an R&B song written by Melvin Riley Jr.  Riley's former band, Ready for the World, originally recorded the song in 1986 and released it as the lead single from their second album, \"Long Time Coming\" produced by Gary Spaniola.  A slow jam, \"Love You Down\" was a hit on the \"Billboard\" pop and R&B charts, spending two weeks atop the R&B chart in December 1986 and peaking at #9 on the pop chart in early 1987.  This was Ready for the World's second R&B chart-topper, following the success of \"Oh Sheila\" in 1985.  It also reached #24 on the \"Billboard\" adult contemporary chart.  The song charted in the United Kingdom at #60 on the UK Singles Chart.  The song has been covered by artists such as R&B singer INOJ and neo soul musician Me'shell Ndegeocello.\n\nEddie Reeves: Edward Benton \"Eddie\" Reeves (born November 17, 1939) is an American songwriter, recording artist, music publisher, artist manager, record company executive, and author.  He wrote several hit songs including \"All I Ever Need Is You\" co-written with Jimmy Holiday and recorded by many artists including Ray Charles, Sonny & Cher, Ray Sanders, Andre Hazes, Tom Jones, Sammi Smith, Chet Atkins & Jerry Reed and Kenny Rogers & Dottie West; \"Rings\", co-written with Alex Harvey and recorded by Cymarron, Lobo, Reuben Howell, Leo Kottke, Twiggy, Tompall and The Glaser Brothers, Lonnie Mack (a vocal rendition from the guitar man of “Memphis” hit record fame), and other artists; \"Don't Change on Me\" co-written with Jimmy Holiday and recorded by Ray Charles, B.B. King, Van Morrison (recorded for Warner Bros. but available only on an Italian bootleg album), and by Alan Jackson; \"If You Wouldn't Be My Lady\", co-written with Jimmy Holiday and recorded by both Ray Charles and Charlie Rich; and \"It’s a Hang Up Baby\", recorded by both Jerry Lee Lewis and Z.Z. Hill.  The song was also performed on November 6, 1969 by Tom Jones with musical backing by the Moody Blues on his national television show, \"This Is Tom Jones\".\n\nVolcanic Action of My Soul: Volcanic Action of My Soul is a studio album by Ray Charles released in April 1971 on Charles' Tangerine Records label.\n\nHallelujah I Love Her So: \"Hallelujah I Love Her So\" is the debut single from American musician Ray Charles.  The jazz and rhythm and blues song was written and released by Charles in 1956 on the Atlantic label, and in 1957 it was included on his self-titled debut LP, also released on Atlantic.  The song peaked at number five on the \"Billboard\" R&B chart.  It is loosely based on 'Get It Over Baby' by Ike Turner (1953).\n\nI Got a Woman: \"I Got a Woman\" (originally titled \"I've Got a Woman\") is a song co-written and recorded by American R&B and soul musician Ray Charles.  Atlantic Records released the song as a single in December 1954, with \"Come Back Baby\" as the B-side.  Both songs later appeared on the 1957 album \"Ray Charles\" (subsequently reissued as \"Hallelujah I Love Her So\").\n\nQuestion: What is the title of the song co-written and recorded by American R&B and soul musician Ray Charles released in 1954 a part of which was contained in the song \"Gold Digger?\"\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"song_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the song.\"\n    },\n    \"artist\": {\n      \"type\": \"string\",\n      \"description\": \"The artist who co-wrote and recorded the song.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the song was released.\"\n    },\n    \"sampled_in_song\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the song that sampled this song.\"\n    },\n    \"sampled_song_artist\": {\n      \"type\": \"string\",\n      \"description\": \"The artist of the song that sampled this song.\"\n    }\n  },\n  \"required\": [\n    \"song_title\",\n    \"artist\",\n    \"release_year\",\n    \"sampled_in_song\",\n    \"sampled_song_artist\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "song_title": {
        "type": "string",
        "description": "The title of the song."
      },
      "artist": {
        "type": "string",
        "description": "The artist who co-wrote and recorded the song."
      },
      "release_year": {
        "type": "integer",
        "description": "The year the song was released."
      },
      "sampled_in_song": {
        "type": "string",
        "description": "The title of the song that sampled this song."
      },
      "sampled_song_artist": {
        "type": "string",
        "description": "The artist of the song that sampled this song."
      }
    },
    "required": [
      "song_title",
      "artist",
      "release_year",
      "sampled_in_song",
      "sampled_song_artist"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
