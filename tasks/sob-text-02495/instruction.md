{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nUs3: Us3 is a jazz-rap group founded in London in 1992.  Their name was inspired by a Horace Parlan recording produced by Alfred Lion, the founder of Blue Note Records.  On their debut album, \"Hand on the Torch\", Us3 exclusively used samples from the Blue Note Records catalogue, all originally produced by Lion.\n\nEctoslavia: Ectoslavia was a band formed at the University of Virginia during the mid-1980s.  It was composed of pre-Silver Jews, Yo La Tengo, and Pavement members David Berman, James McNew, Stephen Malkmus and Bob Nastanovich.  UVA alumnus Gate Pratt was also a member of the band.  The music of Ectoslavia used a great deal of noise and static underneath melodic pop-rock songs, not unlike early Pavement EPs like Perfect Sound Forever and Slay Tracks (1933–1969).  The music of the group also used samples of known classical music, often directly over sheets of static or noise.  Ectoslavia was referred to in the \"Slow Century\" DVD and also in the book \"Perfect Sound Forever\".\n\nAmoebic Dysentery (band): Amoebic Dysentery are a goregrind band from Atlanta, Georgia.  They are noteworthy for being the first goregrind band to wear white HAZMAT suits on stage during performances and their occasional clean vocals.  They've used samples from South Park, Beavis and Butthead, Happiness and .  All their songs are made about gore and sex in a jokingly fashion, some of their song titles on Floaters and Sinkers involving Steve Urkel in purposely disgusting ways such as 'Steve Urkel's Adventures in Bestiality the Violation of Lassie'.\n\nSara Ayers: Sara Ayers is an ambient music artist who uses her voice as a sound source.  The Chemical Brothers used samples of Ayers' \"Everyday We Die a Little\" on their song \"Come Inside\" from their album \"Push the Button.\"  VH1 used samples of \"Angel #3\" for the soundtrack of \"Behind the Music: Britney Spears.\"  The Russian electronic trio Figura constructed an entire album, \"The Sara Ayers Remixes\", around her vocals.\n\nJackie (Elisa Fiorillo song): \"Jackie\" is a song written by Billy Steinberg and Tom Kelly for the 1987 film, \"Summer School\".  It was originally recorded by Elisa Fiorillo and included on the \"Summer School\" soundtrack.  In 1988, \"Jackie\" was recorded by Lisa Stansfield's band, Blue Zone for their 1988 album, \"Big Thing\".  It was released as a single and peaked at number fifty-four on the US \"Billboard\" Hot 100 and number thirty-seven on the Hot Dance Club Songs.  In 1998, \"Jackie\" was recorded by Joanne, who used samples from the Blue Zone version.  It was issued as B.Z. featuring Joanne and reached number three in Australia and number five in New Zealand.  Another cover by Redzone peaked at number thirty-seven in Australia.\n\nVisegrád Group: The Visegrad Group, also called the Visegrad Four, or V4 is a cultural and political alliance of four Central European statesthe Czech Republic, Hungary, Poland and Slovakiafor the purposes of furthering their European integration, as well as for advancing military, economic and energy cooperation with one another.  The group used to be occasionally referred to as the Visegrád Triangle, due to the fact that it was originally an alliance of three states – the term has not been valid since 1993, but does continue to appear sometimes.\n\nCorona (band): Corona is an Italian eurodance act, fronted by Olga Maria De Souza.  Originally produced by Francesco \"Checco\" Bontempi (a.k.a. Lee Marrow) (1st-2nd album), it found success in 1993 with the worldwide hits ”The Rhythm of the Night” and “Baby Baby”.  Later producers include Francesco Conte and Paolo Dughero.\n\nMy Life (Slaughterhouse song): \"My Life\" is the second single of the hip hop group Slaughterhouse from their album \"\".  The song features artist Cee Lo Green and production by Streetrunner and Sarom.  The song samples Corona's song \"The Rhythm of The Night\".  It was available to purchase on iTunes on May 15, 2012.\n\nOh! (Girls' Generation song): \"Oh!\"  is the lead single from \"Oh! \", the second studio album by South Korean girl group Girls' Generation.  The single was digitally released on January 25, 2010 and came to be a huge hit song in South Korea.  The group used a cheerleader concept for the song's promotional activities.  The song hit #1 on various charts, and won several times on the Korean music chart shows \"Music Bank\" and \"The Music Trend\".  The song ranked #4 on \"Gaon Chart Top 10 Digital Songs of the Year\" and it was also the second best selling single in that year, selling over 3.3 million copies.  Music site \"Monkey3\" named \"Oh!\"  the best song in 2010.\n\nAsa-Chang &amp; Junray: Asa Chang & Junray is the band of the Japanese percussionist Asa Chang, who was the founder and original bandmaster of Tokyo Ska Paradise Orchestra.  After leaving that group in 1993, he formed Asa Chang & Junray in 1998 with programmer and guitarist Hidehiko Urayama.  They were joined in 2000 by tabla player U-zhaan.  Live, the group used a portable soundsystem called 'Jun-Ray Tronics', hence the name — although the word 'junray' also means 'pilgrimage'.\n\nQuestion: What group used samples of the song that was originally produced in 1993?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"sampling_group\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the group that used the samples.\"\n        }\n      },\n      \"required\": [\n        \"name\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"sampled_song_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the song that was sampled.\"\n        },\n        \"original_artist\": {\n          \"type\": \"string\",\n          \"description\": \"The artist who originally performed the sampled song.\"\n        },\n        \"original_production_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the sampled song was originally produced.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"original_artist\",\n        \"original_production_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"context_of_sampling\": {\n      \"type\": \"string\",\n      \"description\": \"A brief description of how the sampling occurred, including the song by the sampling group.\"\n    }\n  },\n  \"required\": [\n    \"sampling_group\",\n    \"sampled_song_details\",\n    \"context_of_sampling\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "sampling_group": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the group that used the samples."
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      },
      "sampled_song_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the song that was sampled."
          },
          "original_artist": {
            "type": "string",
            "description": "The artist who originally performed the sampled song."
          },
          "original_production_year": {
            "type": "integer",
            "description": "The year the sampled song was originally produced."
          }
        },
        "required": [
          "title",
          "original_artist",
          "original_production_year"
        ],
        "additionalProperties": false
      },
      "context_of_sampling": {
        "type": "string",
        "description": "A brief description of how the sampling occurred, including the song by the sampling group."
      }
    },
    "required": [
      "sampling_group",
      "sampled_song_details",
      "context_of_sampling"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
