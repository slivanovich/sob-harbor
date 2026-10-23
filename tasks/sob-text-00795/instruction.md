{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe End Tour: The End Tour was the farewell tour of the heavy metal band Black Sabbath, featuring founding members Ozzy Osbourne, Tony Iommi and Geezer Butler.  The tour concluded Sabbath's 40+ year career.  The final show was February 4, 2017, in their home city of Birmingham, UK.\n\nGeoff Nicholls: Geoffrey James \"Geoff\" Nicholls (28 February 1948 – 28 January 2017) was a British musician and keyboardist, and longtime member of the heavy metal band Black Sabbath, until 2004.  Nicholls also played in the NWOBHM band Quartz, before joining Black Sabbath.  In the 1960s/early 1970s, Geoff played lead guitar for the Birmingham bands The Boll Weevils, The Seed, Johnny Neal and the Starliners and keyboards for World Of Oz.\n\nOzzy Osbourne: John Michael \"Ozzy\" Osbourne (born 3 December 1948) is an English singer, songwriter, and actor.  He rose to prominence in the early 1970s as the lead vocalist of the heavy metal band Black Sabbath.  He was fired from Black Sabbath in 1979 and went on to have a successful solo career, releasing 11 studio albums, the first seven of which were all awarded multi-platinum certifications in the US.  Osbourne has since reunited with Black Sabbath on several occasions, recording the album \"13\" in 2013.  His longevity and success have earned him the informal title of \"Godfather of Heavy Metal\".\n\nSabbath Bloody Sabbath (song): \"Sabbath Bloody Sabbath\" is a song by British heavy metal band Black Sabbath.  It is the title track of the band's fifth album \"Sabbath Bloody Sabbath\".  It was released on the album in 1973.  The song is the opening track on the album.\n\nHand of Doom (Black Sabbath song): \"Hand of Doom\" is a song by the English heavy metal band Black Sabbath, originally appearing as the sixth song on their second album \"Paranoid\", released in 1970.  It has been performed in many of Black Sabbath's live concerts.  The lyrics were written by Geezer Butler while the music was written by the four members.  \"Hand of Doom\" is accepted as one of the best songs on the album by many fans of Black Sabbath.  It is the second longest song on the album behind \"War Pigs\".\n\nPsycho Circus World Tour: Psycho Circus World Tour was a Kiss concert tour in 1998–2000.  It was the first concert tour in history to have 3-D visual effects.  The Smashing Pumpkins opened at the Dodger Stadium show only, in costume as The Beatles for the Halloween night performance.  The Dodger Stadium show was streamed live on the internet as well as a radio broadcast.  Two songs, \"Psycho Circus\" and \"Shout It Out Loud\", were screened live on Fox television as part of the \"Kiss Live: The Ultimate Halloween Party\" special.  The vast majority of songs in the setlist were played on the previous Alive/Worldwide concert dates, leading to some frustration from fans expecting the return of classic songs not played on the previous tour.  Peter Criss was quoted in Metal Edge magazine at the time as wanting to add \"Parasite\" to the setlist.  The tour was initially hyped as having circus-style acts as pre-show entertainment.  This ultimately happened only at the first concert at Dodger Stadium.  Peter Criss later said that it didn't work out because the circus performers wanted equal billing and that some had even wanted to use KISS' backstage dressing room.  \"2,000 Man\" was played to bring in the new Millennium at the 1999/2000 New Year's Eve show at Vancouver, advertised at the time as being recorded for Alive IV.  The Vancouver show was also notable as being the first time the original members had played non-original band era material live in concert – \"I Love It Loud\", \"Lick It Up\" and \"Heaven's on Fire\" were added to the setlist and subsequently played on the Farewell Tour.  \"Forever\" was listed on concert setlists at the Vancouver show but was not played.  It was thought at the time it may have been intended as a Paul Stanley solo version prior to \"Black Diamond\".  One notable show on the tour was the March 12 Bremen, Germany, show.  After the opening song, Paul Stanley announced that the local fire marshall had banned Kiss from using any pyrotechnics during the show.  They used a translator on stage to let the crowd understand exactly what Stanley was saying.  At the end of the performance, the band ignited all of the pyrotechnics at once; as a result, they were banned from performing in Bremen.  Ticket sales for this tour were notably slower than the previous Reunion Tour, with many of the smaller market shows underselling and a second North American leg for the summer of 1999 cancelled all together, the band ultimatly decided on embarking on a Farewell tour in the new millennium.\n\nThe Collection (Black Sabbath album): The Collection is a compilation album released by English heavy metal band Black Sabbath in 1992.  The album was released on the label Castle, who released two CD versions of this album in the UK, both with the same cover art and songs.  The album includes greatest songs of Black Sabbath with Ozzy Osbourne prior to his dismissal in 1979, from the eponymous album to \"Never Say Die! \".  The album has 15 tracks, two from \"Black Sabbath\", two from \"Paranoid\", one from \"Master of Reality\", two from \"Black Sabbath Vol.  4\", two from \"Sabbath Bloody Sabbath\", two from \"Sabotage\", two from \"Technical Ecstasy\" and two from \"Never Say Die! \".\n\nThe End (EP): The End is an EP by English heavy metal band Black Sabbath, released on January 20, 2016.  It was only available at dates on their final tour The End.  The EP's first four tracks are unreleased songs from the \"13\" sessions, and the rest were recorded live on that album's tour in 2013–2014.\n\nThe Black Sabbath Story, Vol. 2: The Black Sabbath Story Vol.  2 - 1978-1992 is a documentary video about the biography of the heavy metal band Black Sabbath.  It is the follow-up to \"The Black Sabbath Story Vol.  1 - 1970-1978\", and it's about their story from the leaving of Ozzy Osbourne to the recording of Dehumanizer, discussing the line-up changes Black Sabbath experienced during the period between 1978 and 1992.  In addition to comments by the storic members Geezer Butler and Tony Iommi, there are interviews with other people that have been in the band, like Ronnie James Dio, Ian Gillan, Cozy Powell and Vinny Appice.  There are also live clips and video clips of various songs.  In 2002 a DVD Version has been released, with 19 min of never-seen footage, not included in the previous VHS Version.\n\nBlack Sabbath (album): Black Sabbath is the debut album by the English rock band Black Sabbath.  Released on 13 February 1970 in the United Kingdom and on 1 June 1970 in the United States, the album reached number eight on the UK Albums Charts and number 23 on the \"Billboard\" charts.  Although it was poorly received by most contemporary music critics at the time, \"Black Sabbath\" is now widely considered the first heavy metal album.\n\nQuestion: What was the name of the farewell tour of the heavy metal band Black Sabbath which shares its name with their EP released on January 2016 and was only available on this tour?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"tour_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the farewell tour.\"\n    },\n    \"band_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the band that conducted the tour.\"\n    },\n    \"ep_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"ep_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the EP that shares its name with the tour.\"\n        },\n        \"release_date\": {\n          \"type\": \"string\",\n          \"format\": \"date\",\n          \"description\": \"The release date of the EP.\"\n        },\n        \"availability_restriction\": {\n          \"type\": \"string\",\n          \"description\": \"Description of how the EP was exclusively available.\"\n        }\n      },\n      \"required\": [\n        \"ep_name\",\n        \"release_date\",\n        \"availability_restriction\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"tour_name\",\n    \"band_name\",\n    \"ep_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "tour_name": {
        "type": "string",
        "description": "The name of the farewell tour."
      },
      "band_name": {
        "type": "string",
        "description": "The name of the band that conducted the tour."
      },
      "ep_details": {
        "type": "object",
        "properties": {
          "ep_name": {
            "type": "string",
            "description": "The name of the EP that shares its name with the tour."
          },
          "release_date": {
            "type": "string",
            "format": "date",
            "description": "The release date of the EP."
          },
          "availability_restriction": {
            "type": "string",
            "description": "Description of how the EP was exclusively available."
          }
        },
        "required": [
          "ep_name",
          "release_date",
          "availability_restriction"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "tour_name",
      "band_name",
      "ep_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
