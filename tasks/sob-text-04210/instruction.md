{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nNada Sōsō: \"Nada Sōsō\" (涙そうそう , Great Tears Are Spilling) is a song written by Japanese band Begin and singer Ryoko Moriyama.  It was first released by Moriyama in 1998, but achieved popularity through the cover version by Rimi Natsukawa in 2001.\n\nBBC Radio 1 Live in Concert (New Order album): BBC Radio 1 Live in Concert is a live album by the English band New Order.  The album is an edited recording of the band's headline performance at Glastonbury CND Festival '87.  It was first released as a live album in 1992.  The live album charted at number thirty-three on the UK Albums Chart and was certified as Silver (60,000 units sold) by the BPI.  The live album received mixed reviews and was first released as a LP, CD and Cassette in February 1992.  The live album was released in June 2000 with new artwork by The Peter Saville Studio with photography by Jon Wozencroft.  The original sleeve was designed by Mental Block.\n\nDriven to Tears: \"Driven to Tears\" is a song written by Sting and first released by The Police on their 1980 album \"Zenyatta Mondatta\".  Although not released as a single, the song reached #35 on the \"Billboard\" Mainstream Rock Tracks chart.  The political overtones of the song represent the beginning of the political activism that would recur throughout much of Sting's and the Police's subsequent music.\n\nAge of Consent (band): Age of Consent is an English band from London, England.  The indie pop duo consists of Joe Reeves and Darren Cullen who both started the band a year after the disbandment of their first group, SHITDISCO, a Glasgow-based dance-punk band.  The band is named after the song of the same name by New Order.  Reeves and Cullen play a version of electronic dance music considered to fall under the gothic pop label and their self-described sound is considered “guitar-crazy and danceable.”  The band became well-known when their music was featured in the 2013 hit video game, Grand Theft Auto V.  The game features two songs by the band including \"Colours\", an original song written for the game and is featured on the game's soundtrack, and their 2012 second single \"Heartbreak\" both featured in the in-game's indie radio station Radio Mirror Park.\n\nI'm So Happy I Can't Stop Crying: \"I'm So Happy I Can't Stop Crying\" is a song written and recorded by English rock singer Sting.  It was released from his 1996 album \"Mercury Falling\".  The song was also released as a single, and reached number 94 and number 54 on the U.S. and UK singles charts, respectively.  Sting also recorded the song as a duet with country music artist Toby Keith on Keith's 1997 \"Dream Walkin'\" album.  This version reached number 2 on the US Hot Country Songs charts and number 84 on the U.S. \"Billboard\" Hot 100 charts, and gave Sting his only country hit.\n\nEverybody Wants to Rule the World: \"Everybody Wants to Rule the World\" is a song by English band Tears for Fears.  Originally released in the UK on 22 March 1985 it was the band's ninth single release in the United Kingdom and the third from their second LP \"Songs from the Big Chair\".  It was their seventh UK Top 30 chart hit, peaking at number two in April 1985, and thus becoming the group's highest-charting UK single.  In the US, it was the lead single from the album and gave the band their first \"Billboard\" Hot 100 number-one hit on 8 June 1985, remaining there for two weeks.  It also reached number one on both the Hot Dance Club Play and Hot Dance Music/Maxi-Singles Sales charts in the US.  The song has since become the pinnacle of Tears for Fears' chart success.\n\nWoman in Chains: \"Woman in Chains\" is a song by the English band Tears for Fears, released as the second single from their 1989 album \"The Seeds of Love\".\n\nIf You Gotta Go, Go Now: \"If You Gotta Go, Go Now\" (sometimes subtitled \"(Or Else You Got to Stay All Night)\") is a song written by Bob Dylan in 1964.  The first released version was as a single in the US by the UK group The Liverpool Five in July 1965, but this went uncharted in the US despite receiving much airplay, particularly in the Pacific Northwest.  Another English band, Manfred Mann, then issued the song as a single in September 1965; this version reached number 2 on the UK charts.\n\nDemolition Man (song): \"Demolition Man\" is a song written by Sting and performed by Grace Jones as the A-side of a 1981 single.  Sting's band, the Police, later released their rendition of the song on their album \"Ghost in the Machine\", as did Manfred Mann's Earth Band.\n\nThe Police: The Police were an English new wave band formed in London in 1977.  For most of their history the band consisted of Sting (lead vocals, bass guitar, primary songwriter), Andy Summers (guitar) and Stewart Copeland (drums, percussion).  The Police became globally popular in the late 1970s and early 1980s and are generally regarded as one of the first new-wave groups to achieve mainstream success, playing a style of rock influenced by punk, reggae, and jazz.  They are also considered one of the leaders of the Second British Invasion of the United States.  They disbanded in 1986, but reunited in early 2007 for a one-off world tour that ended in August 2008.\n\nQuestion: Driven to Tears is a song written by Sting and first released by an English band that formed in what year?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"song_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the song in question.\"\n    },\n    \"releasing_band\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the band that first released the song.\"\n        },\n        \"nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the band.\"\n        },\n        \"formation_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the band was formed.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"nationality\",\n        \"formation_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"band_formation_year_answer\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the band that first released the song was formed, which is the answer to the question.\"\n    }\n  },\n  \"required\": [\n    \"song_title\",\n    \"releasing_band\",\n    \"band_formation_year_answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "song_title": {
        "type": "string",
        "description": "The title of the song in question."
      },
      "releasing_band": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the band that first released the song."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the band."
          },
          "formation_year": {
            "type": "integer",
            "description": "The year the band was formed."
          }
        },
        "required": [
          "name",
          "nationality",
          "formation_year"
        ],
        "additionalProperties": false
      },
      "band_formation_year_answer": {
        "type": "integer",
        "description": "The year the band that first released the song was formed, which is the answer to the question."
      }
    },
    "required": [
      "song_title",
      "releasing_band",
      "band_formation_year_answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
