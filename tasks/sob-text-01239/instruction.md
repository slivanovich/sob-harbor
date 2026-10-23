{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCatch Me If You Can (Girls' Generation song): \"Catch Me If You Can\" is a song recorded in two languages (Japanese and Korean) by South Korean girl group Girls' Generation.  The Korean version was released by S.M. Entertainment and KT Music on April 10, 2015, while the Japanese version was released on April 22 by EMI and Universal Music Japan.  The song was composed by Erik Lidbom and Jin Choi, with the Korean lyrics written by Mafly and Choe A-Leum, and the Japanese lyrics written by Junji Ishiwatari and Jeff Miyahara.  Musically, it was described by critics as an EDM track.  The song marked the first release of Girls' Generation as an eight-member group following the dismissal of member Jessica Jung in September 2014.\n\nParty (Girls' Generation song): \"Party\" is a song recorded by South Korean girl group Girls' Generation for their fifth Korean studio album \"Lion Heart\" (2015).  It was released as the lead single from the album by S.M. Entertainment on July 7, 2015.  The lyrics were written by Cho Yoon-kyung and the music was composed by Albi Albertsson, Chris Young, and Shin Agnes.  \"Party\" is a bubblegum pop and electropop song that features synthesizers, guitar, and Auto-Tune in its instrumentation.  To promote the song and the album, Girls' Generation performed \"Party\" on several South Korean music programs, including \"Music Bank\", \"Show!  Music Core\" and \"Inkigayo\".  A music video for the track, directed by Hong Won-ki, was also released on July 7.\n\nHimnaera Him!: Girls' Generation's Himnaera Him!  (; lit.  Girls' Generation's Cheer Up!) , is a South Korean television reality show starring the South Korean girl group Girls' Generation.  The show and cast operated under the goal of being the Republic of Korea's cheering squad, with the intention of cheering up the citizens during an economic slump.\n\nGirls &amp; Peace: Girls' Generation II ~Girls & Peace~ is the second Japanese album (fifth overall) by South Korean girl group Girls' Generation.  It was released on November 28, 2012 through Nayutawave Records.  \"Girls & Peace\" is the first release by all the members since their third Korean studio album \"The Boys\" (2011), after the group entered a semi-hiatus to pursue solo activities in South Korea, in which time Girls' Generation-TTS, the group's first subunit, was created.  Continuing the electro-influenced sound from their first Japanese album, \"Girls & Peace\" features a wide range of contribution from producers, including long-time collaborator, Kenzie, as well as multiple new producers such as Miles Walker, Deekay and Dapo Torimiro.  The album sold over 116,000 copies in its first week, reaching the third spot on the Oricon Album chart, and has since received a Platinum certification from the RIAJ.\n\nGirls' Generation's Phantasia: Girls' Generation's Phantasia was the fourth concert tour by South Korean girl group Girls' Generation.  The tour was officially announced in October 2015.  This is the first tour without former member Jessica Jung, who left the group on September 30, 2014.\n\nJessica Jung: Jessica Jung (born April 18, 1989), known professionally as Jessica, is an American singer, songwriter, actress, model, fashion designer, and businesswoman currently based in South Korea.  Jung was born and raised in San Francisco, California.  At the age of eleven, she was discovered by South Korean entertainment agency S.M. Entertainment and subsequently moved to South Korea.  In 2007, Jung debuted as a member of the South Korean girl group Girls' Generation.  The group later became one of the best-selling artists in South Korea, and one of South Korea's most popular girl groups nationwide and worldwide.\n\nGirls' Generation videography: This is the videography of the South Korean girl group Girls' Generation.  Girls' Generation have been in the music business ever since debuting in August 2007.  The group is composed of eight members: Taeyeon, Sunny, Tiffany, Hyoyeon, Yuri, Sooyoung, Yoona and Seohyun.  Former member Jessica was dismissed from the group in 2014.\n\nGirls' Generation Japan 3rd Tour 2014: Girls' Generation Japan 3rd Tour 2014 is the third concert tour by South Korean girl group Girls' Generation to promote their third Japanese album, \"Love & Peace\".  It gathered an audience of more than 200,000.  This is the final tour to include former member Jessica Jung, who left the group on September 30, 2014.\n\nFly (Jessica song): \"Fly\" is a Korean song recorded by South Korean singer Jessica Jung featuring Fabolous, taken from Jessica's debut With Love, J EP.  It was written by herself, and produced by Eric Fernandez, Karriem Mack.  It was released digitally by Coridel Entertainment on May 17, 2016 in conjunction with the release of the EP\n\nKim Tae-yeon discography: Kim Tae-yeon, better known by the mononym Taeyeon, is a South Korean singer.  Her discography consists of one studio album, two extended plays (EPs), twenty singles (including four as featured artist), and three promotional singles.  She debuted as a member of South Korean girl group Girls' Generation in August 2007 and initially gained some popularity as a singer upon recording soundtrack songs \"If\" for \"Hong Gil Dong\" and \"Can You Hear Me\" for \"Beethoven Virus\" (2008).  She subsequently established herself as one of the most renowned vocalist on the South Korean music scene with further soundtrack recordings, notably \"I Love You\" for \"\" (2010), \"Missing You like Crazy\" for \"The King 2 Hearts\", \"Closer\" for \"To the Beautiful You\" (2012), and \"And One\" for \"That Winter, the Wind Blows\" (2013), all of which managed to enter the top ten of South Korea's Gaon Digital Chart.  Apart from soundtrack recordings, Taeyeon has also recorded duets with other artists, most notably \"Like a Star\" with The One and \"Different\" with Kim Bum-soo, which peaked at numbers one and two on the Gaon Digital Chart, respectively.\n\nQuestion: Former member of the popular South Korean girl group Girls' Generation, which singer wrote and recorded the song \"Fly\"?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"singer_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the singer.\"\n    },\n    \"song_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the song.\"\n    },\n    \"roles\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Roles performed by the singer for the song (e.g., 'recorded', 'wrote').\"\n    },\n    \"former_group\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the group the singer was formerly a member of.\"\n    }\n  },\n  \"required\": [\n    \"singer_name\",\n    \"song_title\",\n    \"roles\",\n    \"former_group\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "singer_name": {
        "type": "string",
        "description": "The name of the singer."
      },
      "song_title": {
        "type": "string",
        "description": "The title of the song."
      },
      "roles": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Roles performed by the singer for the song (e.g., 'recorded', 'wrote')."
      },
      "former_group": {
        "type": "string",
        "description": "The name of the group the singer was formerly a member of."
      }
    },
    "required": [
      "singer_name",
      "song_title",
      "roles",
      "former_group"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
