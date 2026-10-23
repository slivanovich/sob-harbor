{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAlexander Lee (entertainer): Alexander Lee Eusebio (Korean: 알렉산더; Chinese:亚历山大; born on July 29, 1988 in Hong Kong), known as Alexander or Xander, is a half-Korean, quarter-Portuguese and quarter-Chinese singer, actor and host in South Korea.  He is a former member of the South Korean boy band U-KISS, and is known to speak 7 languages: English, Korean, Cantonese, Mandarin, Japanese, Spanish, and Portuguese; being fluent in the first four.  He debuted as an actor through a Channel A drama Immortal Classic (불후의 명작), and later as a movie actor through Singaporean film, \"3 Peas In A Pod\" in 2013.  He is currently active as a television host on Arirang TV's #StyleCast 2017 and is also a daily radio host for the Double Date show on tbs eFM.\n\nJB (South Korean singer): Lim Jae-beom (Hangul: 임재범; born January 6, 1994) commonly known by his stage name JB (Hangul: 제이비), is a South Korean singer, songwriter and actor.  He is a member of South Korean boyband Got7, and part of the duo JJ Project.  JB made his small-screen debut through the drama series \"Dream High 2\" in 2012.  He has also starred in MBC's \"When a Man Falls in Love\" as Seo-Min Joon.\n\nJoey Fatone: Joseph Anthony Fatone Jr. (born January 28, 1977), is an American singer, dancer, actor and television personality.  He is best known as a member of the boyband NSYNC, in which he sang baritone.  In 2007, he came in second place on the ABC reality show \"Dancing with the Stars\".  He was also the host of the U.S. and Australian versions of \"The Singing Bee\" which aired on NBC in the U.S. Currently Fatone is the host of Food Network's \"Rewrapped\", Live Well Network's \"My Family Recipe Rocks\" and is also guest host of \"The Price Is Right Live! \" at Bally's Las Vegas.\n\nPark Jin-young (entertainer, born 1994): Park Jin-young (born September 22, 1994), referred to as Jinyoung (formerly as Jr.), is a South Korean singer, songwriter, actor, dancer, and choreographer.  He is a member of the boy group Got7 and duo JJ Project.  Park made his acting debut in the drama \"Dream High 2\" (2012) followed by supporting roles in \"When a Man Falls in Love\" (2013) and \"Beloved Eun-dong\" (2015).  He made his film debut in the independent film \"A Stray Goat\" (2016).\n\nJamie Kaler: Jamie Kaler (born September 14, 1964) is an American stand-up comedian and actor who has gained fame by portraying the character Mike Callahan on the TBS comedy \"My Boys\".  Kaler is the current host of \"\" on American Heroes Channel.  \"He has appeared on such talk shows as the \"Late Late Show\" as well as having a role on the sitcom \"How I Met Your Mother\", and had a recurring role on \"Will and Grace\".  Kaler also lends his voice to the show \"Robot Chicken\", as the suicidal blooper host.  He is a member of the ACME Company, ACME Comedy Theatre's top-level sketch company and has also made guest appearances on \"Friends\", \"The King of Queens\", \"Shake It Up\" and \"Monk\".\n\nInkigayo: Inkigayo (Korean: 인기가요 ; English title: The Music Trend, previously Popular Song) is a South Korean music program broadcast by SBS.  It airs live every Sunday at 12:10 PM KST.  The show features some of the latest and most popular artists who perform on stage.  Since February 5, 2017, it is hosted by Park Jin-young, Kim Ji-soo and Kim Do-young.  It is broadcast from the SBS Open Hall in Deungchon-dong, Gangseo-gu, Seoul.\n\nMichelle Beisner: Michelle Beisner-Buck (born October 15, 1976) is a feature reporter for ESPN and is a member of the \"Monday Night Countdown\" crew.  She had an 8-year tenure at NFL Network being the host of NFL Weekly Countdown, and served as a field reporter for \"NFL Total Access\" and \"NFL GameDay Morning\".  She was also the host of \"NFL Network Now\", a news program on NFL Network.  She has been a reporter and has worked on \"NFL Quarterback Challenge\", and the \"Total Access On Location\" pre-game show at the Super Bowl.  Beisner also served as host of NFL.com Fantasy LIVE alongside Michael Fabiano, Adam Rank and Dave Dameshek.\n\nAndre Blaze: Andre Blaze Henshaw (born 14 August 1983) is a Nigerian radio personality, rapper, television host and executive producer.  He first gained notice as a member of the hip hop group Tuck Tyght Allstars.  His radio career began at Rhythm 93.7 FM Port Harcourt, where he worked for over six years before joining Nigezie as a TV host.  In May 2012, he quit his job at the cable TV channel after four years, later accepting an offer to host Nigeria's Got Talent.  Prior to this, he had hosted several other reality television talent shows including True Search, Battle of the Year and Peak Talent Show.  He is also an anchor for the Google Digital Skills for Africa Training Programme.\n\nBrent Musburger: Brent Woody Musburger ( ; born May 26, 1939) is an American sportscaster, lead broadcaster and managing editor at Vegas Stats and Information Network (VSiN).  He retired in January 2017 from the ESPN and ABC television networks.  Formerly with CBS Sports and one of the original members of their program \"The NFL Today\", Musburger has also covered the NBA, MLB, NCAA football and basketball, and NASCAR and served as a studio host for games, a play-by-play man, and halftime host.  He has also performed postgame wrap-up segments and covered championship trophy presentations.  He is a member of the Montana Broadcaster's Association Hall of Fame.\n\nMichael Shure: Michael Shure (born April 18, 1966) Shure is an original member of, and regular host on \"The Young Turks\" and was the host of that network's online 2012 election show, \"twenTYTwelve.\"  Most recently Shure served as Chief Political Correspondent for Al Jazeera America until the network's closure.  Shure was formerly the host of Current TV's \"The War Room with Michael Shure\", a one-hour political commentary program that aired live Monday through Thursday.  Shure has also occasionally appeared as an actor.\n\nQuestion: When was the host of Inkigayo who is also a member of Got7 born?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person who is the host of Inkigayo and a member of Got7.\"\n    },\n    \"hosted_show\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the show the person hosts.\"\n    },\n    \"member_of_group\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the music group the person is a member of.\"\n    },\n    \"birth_date\": {\n      \"type\": \"string\",\n      \"format\": \"date\",\n      \"description\": \"The full birth date of the person in YYYY-MM-DD format.\"\n    },\n    \"birth_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth year of the person.\"\n    },\n    \"birth_month\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth month of the person (1-12).\"\n    },\n    \"birth_day\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth day of the person (1-31).\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"hosted_show\",\n    \"member_of_group\",\n    \"birth_date\",\n    \"birth_year\",\n    \"birth_month\",\n    \"birth_day\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the person who is the host of Inkigayo and a member of Got7."
      },
      "hosted_show": {
        "type": "string",
        "description": "The name of the show the person hosts."
      },
      "member_of_group": {
        "type": "string",
        "description": "The name of the music group the person is a member of."
      },
      "birth_date": {
        "type": "string",
        "format": "date",
        "description": "The full birth date of the person in YYYY-MM-DD format."
      },
      "birth_year": {
        "type": "integer",
        "description": "The birth year of the person."
      },
      "birth_month": {
        "type": "integer",
        "description": "The birth month of the person (1-12)."
      },
      "birth_day": {
        "type": "integer",
        "description": "The birth day of the person (1-31)."
      }
    },
    "required": [
      "person_name",
      "hosted_show",
      "member_of_group",
      "birth_date",
      "birth_year",
      "birth_month",
      "birth_day"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
