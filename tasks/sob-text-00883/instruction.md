{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJon Snow (character): Jon Snow is a fictional character in the \"A Song of Ice and Fire\" series of fantasy novels by American author George R. R. Martin, and its television adaptation \"Game of Thrones\".  He is a prominent point of view character in the novels, and has been called one of the author's \"finest creations\" and most popular characters by \"The New York Times\".  Jon is a main character in the TV series, and his storyline in the 2015 season 5 finale generated a strong reaction among viewers.  Speculation about the character's parentage has also been a popular topic of discussion among fans of both the books and the TV series.\n\nAmbassador Magma: Ambassador Magma (マグマ大使 , Maguma Taishi ) is the title and protagonist of a manga and tokusatsu TV series created by Osamu Tezuka, the writer of \"Mighty Atom\" (\"Astro Boy\" in English) and \"Jungle Emperor\" (\"Kimba the White Lion\" in English).  The TV series, produced by P Productions, was aired on Fuji TV from July 4, 1966 to September 25, 1967, lasting a total of 52 episodes.  It is the first color tokusatsu TV series in Japan, beating Tsuburaya Productions' \"Ultraman\" to the airwaves by 6 days.  The show later aired in the U.S., dubbed in English, as \"The Space Giants\".\n\nThe Saint (2017 film): The Saint is a 2017 espionage thriller TV movie directed by Ernie Barbarash and starring Adam Rayner in the title role of Simon Templar, created by Leslie Charteris.  This was Sir Roger Moore's final film appearance and the film was dedicated to his memory; Moore portrayed Templar in a 1960s TV series of the same title.  Filmed in 2013 as a television pilot for a proposed TV series, the film was not originally intended for release when the series was not picked up.  It eventually saw release direct-to-video in 2017 when it was released in tribute to Moore following his death.  Ian Ogilvy, who portrayed Templar in a 1970s TV series titled \"Return of the Saint\", also appears.\n\nDamon Dark: Damon Dark is an independent public access TV series and web series from Australia about a heroic and obsessive investigator of UFO incidents and other strange cases, created by Australian writer, actor and film maker Adrian Sherlock.  Damon James Dark became a dedicated alien investigator after a close encounter during his teenage years.  He is associated with both the secret service and friendly aliens, including a character called Vincent Kosmos (an alien time traveller) and Trans-Dimensional Control (an alien law enforcement agency).  The character of Damon Dark has appeared in a 5-week TV series on Community TV 31 in Melbourne Australia, a self-published novel (\"Biodome\") on Amazon's createspace platform and a long running web series on YouTube.  He has also been involved in related web series \"Young Damon Dark\" and \"Vincent Kosmos.\"  He has also been the focus of a one actor stage drama.  The character of Damon Dark has been played by Adrian Sherlock, Bruce Hughes, Aiden Sherlock and Jack Knoll.  Damon Dark is a loner, dresses in black, has a huge experience of aliens and their technology.  Damon is characterized by his high intelligence, idealistic moral outlook and wry sense of humor.  His best friend in the series is the long-suffering Gary Sutton, played by actor Robert Trott.  Damon Dark began in 1999, with a five-part weekly series on Melbourne's Community TV 31, (although the pilot was shot in 1996 and the show had been in development since 1990) following a screening of a 65-minute version of the story \"Maddox\" at the 57th World Science Fiction Convention (Aussiecon Three) held in Melbourne.  The series was later revived as a YouTube webseries which inspired several related webseries, including \"The Young Damon Dark Adventures\" in which the character is played as a teenager, and Vincent Kosmos, (created by and starring Chris Heaven, , an Italian actor and musician, about a renegade alien character who is a friend of Damon.\n\nElf-ban Kakyūsei: Elf-ban Kakyūsei (エルフ版　下級生 , Erufuban Kakyūsei, lit.  \"Elf Version Underclassmates\" ) is an anime.  It is unrelated to a different series of the same title, Kakyūsei, also produced by Pink Pineapple in 1995.  It was based on a game originally created by Masato Hiruta more popularly known as Elf, and had a TV series produced after success of the OVA.  The 14th episode of the TV series was never aired on television.  The TV series produced further sequels and spin offs that were considerably more explicit than their earlier versions.\n\nSharongate: \"Sharongate\" is the term used for a storyline in the BBC soap opera \"EastEnders\", which reached its climax on 24 October 1994, attracting 25.3 million viewers.  The plot was written by \"EastEnders\" scriptwriter Tony Jordan.  In the storyline, Sharon Mitchell (Letitia Dean) confessed on tape that she had sex with her husband's brother, Phil (Steve McFadden).  The truth comes out in the middle of The Queen Victoria pub.  Sharon's husband Grant (Ross Kemp) attacked his brother and Phil was lucky to survive.\n\nKamen Rider Kabuto: God Speed Love: Kamen Rider Kabuto the Movie: God Speed Love (劇場版 仮面ライダーカブト GOD SPEED LOVE , Gekijōban Kamen Raidā Kabuto Goddo Supīdo Rabu ) is the theatrical film adaptation of the \"Kamen Rider Kabuto\" TV series directed by Hidenori Ishida and written by Shōji Yonemura.  Unlike many others Kamen Rider movies, it does not follow the TV series's storyline.  Instead, it is more like a prologue.  The movie shows an alternate timeline where the close relations between Riders did not exist and the impact of the first meteor evaporated all of Earth's oceans.  Seven years after the meteor hit Earth, ZECT pretends to use a passing comet to refill the Earth's oceans, while in fact they are pulling another meteor to crash on Earth, one large enough to wipeout all of humanity.\n\nSue Ball: Susan Gabrielle \"Sue\" Ball (born March 2, 1967, in Philadelphia, Pennsylvania) is an American actress.  She is best known for her starring role in \"Leo and Liz in Beverly Hills\", which was created by Steve Martin.  She has had many guest starring and recurring roles, most notably \"Rags to Riches\" (TV series), \"Perfect Strangers\" (TV series), \"Valerie\" (TV series), and \"It's a Living\" (1980 TV series).\n\nStar Trek: Challenger: Star Trek: Challenger is a spin-off series of \"Star Trek\" novels published by Pocket Books in the United States as part of Pocket’s line.  Based on the titular TV series created by Gene Roddenberry, the series was created by Pocket editor John J. Ordover and writer Diane Carey, and was a continuation of the six-book storyline, \"\".  The sixth and final \"New Earth\" book was subtitled \"Challenger\", and served as a springboard for \"Star Trek: Challenger\".  It was published on August 1, 2000.\n\nEastEnders: EastEnders is a long-running British soap opera created by Julia Smith and Tony Holland which has been broadcast on BBC One since 1985.  Set in the East End of London in the fictional Borough of Walford, the programme follows the stories of local residents and their families as they go about their daily lives in Albert Square.  The series was initially screened as two 30-minute episodes per week; however, since 2001, episodes have been broadcast every day apart from Wednesdays and weekends.  Same-day repeats of the series were previously shown on BBC Three and omnibus editions were shown on BBC Two, however, since 2016 these have been broadcast on UK-based TV channel W.\n\nQuestion: Who created the TV series which had the storyline Sharongate ?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"storyline_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the storyline.\"\n    },\n    \"tv_series_info\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the TV series.\"\n        },\n        \"creators\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"object\",\n            \"properties\": {\n              \"name\": {\n                \"type\": \"string\",\n                \"description\": \"The name of a creator of the TV series.\"\n              }\n            },\n            \"required\": [\n              \"name\"\n            ],\n            \"additionalProperties\": false\n          },\n          \"description\": \"A list of individuals who created the TV series.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"creators\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"number_of_creators\": {\n      \"type\": \"integer\",\n      \"description\": \"The total number of creators for the TV series.\"\n    }\n  },\n  \"required\": [\n    \"storyline_name\",\n    \"tv_series_info\",\n    \"number_of_creators\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "storyline_name": {
        "type": "string",
        "description": "The name of the storyline."
      },
      "tv_series_info": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the TV series."
          },
          "creators": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string",
                  "description": "The name of a creator of the TV series."
                }
              },
              "required": [
                "name"
              ],
              "additionalProperties": false
            },
            "description": "A list of individuals who created the TV series."
          }
        },
        "required": [
          "name",
          "creators"
        ],
        "additionalProperties": false
      },
      "number_of_creators": {
        "type": "integer",
        "description": "The total number of creators for the TV series."
      }
    },
    "required": [
      "storyline_name",
      "tv_series_info",
      "number_of_creators"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
