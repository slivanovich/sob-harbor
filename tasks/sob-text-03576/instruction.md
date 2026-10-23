{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nWhen the Angels Swing: When the Angels Swing is a swing album by German pop group No Angels, released by Cheyenne Records and Polydor in association with Universal Music on November 29, 2002.  Recorded in promotion of a special big band concert at the Berlin Tränenpalast on October 2, 2002, the album differed highly from the group's previous, mainstream pop releases in that they performed their songs with blues and jazz arrangements.  Musicians Jens Kuphal and Till Brönner were consulted to work on the album which was inspired by the New York City Stork Club and several 1940s swing standards.  Aside from the title, \"When the Angel Swing\" is not directly associated with the No Angels's 2001 single, \"When the Angels Sing.\"\n\nSwing When You're Winning: Swing When You're Winning is a swing cover album by English singer-songwriter Robbie Williams, and his fourth studio album overall.  It was released in the United Kingdom on 19 November 2001 and peaked at number one on the UK Albums Chart.\n\nGirl Authority (album): Girl Authority is the debut cover album by pop girl group Girl Authority.  The album is a cover album of previous hit songs by other female solo singers and girl groups, with the exception of two songs, originally recorded by Smokey Robinson & the Miracles and ABBA.  The album was successful on many album charts, including Billboard Top Kid Audio (a chart that records sales of children's music albums), where it reached #9.  The album also managed reach #5 on the Top Heatseekers Chart, and eventually peaked at #167 on the \"Billboard\" 200, the main album chart.\n\nAAA discography: The discography of Japanese pop group AAA includes nine studio albums, six extended plays, seven compilation albums, eight live albums, one cover album, three remix albums, and 52 singles.  All of the group's releases have been with Avex Trax, a subsidiary of Avex Group.\n\nRobbie Williams: Robert Peter Williams (born 13 February 1974) is an English singer, songwriter and actor.  He was a member of the pop group Take That from 1990 to 1995 and again from 2009 to 2012.  He has also had commercial success as a solo artist.\n\nLive at the Albert: \"\"Robbie Williams: Live at the Albert\"\" is a DVD that was released in December 2001 of the show performed on 10 October 2001; concert that Robbie Williams gave at Royal Albert Hall a month before the release of the album Swing When You're Winning.  It has since been certified 6x Platinum in the United Kingdom and 2x Platinum in Germany.\n\nBeautiful Mess (Swing Out Sister album): Beautiful Mess is the title of the ninth studio album by the British pop group Swing Out Sister.  It was produced by group member Andy Connell, who has been with Swing Out Sister since its inception.\n\nUltimate Collection (No Angels album): Ultimate Collection is a box set by the German pop group No Angels, released by Polydor Records on June 30, 2003 (see 2003 in music) in German-speaking Europe.  It comprises both \"Special Winter Edition\" reissues of their first two albums \"Elle'ments\" (2001) and \"Now... Us! \" (2002), as well as a DVD, containing their \"When the Angels Swing\" (2002) swing concert.\n\nAre You Gonna Go My Way (song): \"Are You Gonna Go My Way\" is the first single to be released by Lenny Kravitz from the album \"Are You Gonna Go My Way\".  It was released in February 1993.  It was written by Lenny Kravitz and Craig Ross.  The single has been covered by numerous artists, such as Metallica, in a medley for \"MTV Hits\" at the 2003 MTV Music Video Awards, Tom Jones for the \"Jerky Boys OST\", Robbie Williams on Jones' 1999 album \"Reload\" and Melanie Brown in her solo section, on the Spice Girls Reunion Tour.  Serbian hard rock band Cactus Jack recorded a version on their live cover album \"DisCover\" in 2002.  A remixed version is played as the opening theme song in \"Gran Turismo 3\".  Adam Lambert covered the song in November 2012 in his swing through South Africa.  The song was featured in one episode of Fox animated series \"The Simpsons\".  It was also featured in the music video game \"Guitar Hero World Tour\".\n\nPå vårt sätt (Miio album): På vårt sätt is a 2003 cover album by teen pop group Miio from Sweden, consisting of recordings of several Swedish pop hits.  The album peaked at 15th position at the Swedish album chart placerade sig albumet som högst på 15:e plats.\n\nQuestion: What pop group was the singer-songwriter of the swing cover album Swing When You're Winning a part of from 1990 to 1995 and again from 2009 to 2012?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"artist_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the singer-songwriter.\"\n    },\n    \"album_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the swing cover album.\"\n    },\n    \"album_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of the album.\"\n    },\n    \"pop_group_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the pop group the artist was a member of.\"\n    },\n    \"group_membership_periods\": {\n      \"type\": \"array\",\n      \"description\": \"Periods during which the artist was a member of the pop group.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"start_year\": {\n            \"type\": \"integer\",\n            \"description\": \"The start year of the membership period.\"\n          },\n          \"end_year\": {\n            \"type\": \"integer\",\n            \"description\": \"The end year of the membership period.\"\n          }\n        },\n        \"required\": [\n          \"start_year\",\n          \"end_year\"\n        ],\n        \"additionalProperties\": false\n      }\n    }\n  },\n  \"required\": [\n    \"artist_name\",\n    \"album_title\",\n    \"album_type\",\n    \"pop_group_name\",\n    \"group_membership_periods\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "artist_name": {
        "type": "string",
        "description": "The name of the singer-songwriter."
      },
      "album_title": {
        "type": "string",
        "description": "The title of the swing cover album."
      },
      "album_type": {
        "type": "string",
        "description": "The type of the album."
      },
      "pop_group_name": {
        "type": "string",
        "description": "The name of the pop group the artist was a member of."
      },
      "group_membership_periods": {
        "type": "array",
        "description": "Periods during which the artist was a member of the pop group.",
        "items": {
          "type": "object",
          "properties": {
            "start_year": {
              "type": "integer",
              "description": "The start year of the membership period."
            },
            "end_year": {
              "type": "integer",
              "description": "The end year of the membership period."
            }
          },
          "required": [
            "start_year",
            "end_year"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": [
      "artist_name",
      "album_title",
      "album_type",
      "pop_group_name",
      "group_membership_periods"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
