{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSerializer: serializer.net was an online artist collective that was active from 2002 to 2012.  Serializer included many well-known award-winning alternative artists like Tom Hart (Xeric Award winner), Eric Millikin (Pulitzer Prize winner), Shaenon K. Garrity (Lulu Award winner), James Kochalka (Eisner Award winner), Dean Haspiel (Emmy Award winner), Howard Cruse (Prix de la critique winner), Chris Onstad (Ignatz Award winner), Nick Bertozzi (Harvey Award winner), and Jen Sorenson (Herblock Prize winner).  Each artist created, and sometimes collaborated on, serialized webcomics.\n\nGary Sinise: Gary Alan Sinise ( ; born March 17, 1955) is an American actor, director, and musician.  Among other awards, he has won an Emmy Award, a Golden Globe Award, a star on Hollywood Walk of Fame and has been nominated for an Academy Award.\n\nGeoffrey Rush: Geoffrey Roy Rush {'1': \", '2': \", '3': \", '4': \"} (born 6 July 1951) is an Australian actor and film producer.  Rush is the youngest amongst the few people who have won the \"Triple Crown of Acting\": the Academy Award, the Primetime Emmy Award, and the Tony Award.  He has won one Academy Award for acting (from four nominations), three British Academy Film Awards (from five nominations), two Golden Globe Awards and four Screen Actors Guild Awards. Rush is the founding President of the Australian Academy of Cinema and Television Arts and was named the 2012 Australian of the Year.  He is also the first actor to win the Academy Award, BAFTA Award, Critics' Choice Movie Award, Golden Globe Award, and Screen Actors Guild Award for a single performance in film for his performance in \"Shine\" (1996).\n\nBlythe Danner: Blythe Katherine Danner (born February 3, 1943) is an American actress.  She won two Primetime Emmy Awards for Best Supporting Actress in a Drama Series for her role as Izzy Huffstodt on \"Huff\" (2004–2006), and a Tony Award for Best Featured Actress in a Play for her performance in \"Butterflies Are Free\" (1969–1972).  Danner was nominated for two Primetime Emmy Awards for Outstanding Guest Actress in a Comedy Series for portraying Marilyn Truman on \"Will & Grace\" (2001–2006), and the Primetime Emmy Award for Outstanding Lead Actress in a Miniseries or a Movie for her roles in \"We Were the Mulvaneys\" (2002) and \"Back When We Were Grownups\" (2004).  For the latter, she was also nominated for the Golden Globe Award for Best Actress – Miniseries or Television Film.\n\nDamian Lewis: Damian Watcyn Lewis, {'1': \", '2': \", '3': \", '4': \"} (born 11 February 1971) is an English actor and producer.  He played U.S. Army Major Richard Winters in the HBO miniseries \"Band of Brothers\", which earned him a Golden Globe nomination, and also portrayed U.S. Marine Sergeant Nicholas Brody in the Showtime series \"Homeland\" (which earned him a Primetime Emmy Award and a Golden Globe Award).  His performance as Henry VIII in \"Wolf Hall\" earned him his third Primetime Emmy nomination and fourth Golden Globe nomination.\n\nSônia Braga: Sônia Maria Campos Braga (] born June 8, 1950) is a Brazilian-American actress.  She is known in the English-speaking world for her Golden Globe Award nominated performances in \"Kiss of the Spider Woman\" (1985) and \"Moon over Parador\" (1988).  She also received a BAFTA Award nomination in 1981 for \"Dona Flor and Her Two Husbands\" (first released in 1976).  For the 1994 television film \"The Burning Season\", she was nominated for an Emmy Award and a third Golden Globe Award.  Her other television credits include \"The Cosby Show\" (1986), \"Sex and the City\" (2001), \"American Family\" (2002), and \"Alias\" (2005).\n\nThe Woman He Loved: The Woman He Loved is a 1988 HTV romantic drama television about the abdication of Edward VIII.  Directed by Charles Jarrott, it stars Anthony Andrews, Jane Seymour and Olivia de Havilland.  Jane Seymour was nominated for a Golden Globe Award for Best Actress – Miniseries or Television Film at the 46th Golden Globe Awards and Olivia de Havilland was nominated for a Primetime Emmy Award for Outstanding Supporting Actress in a Miniseries or a Movie.  Costume designer Robin Fraser-Paye was also nominated for Primetime Emmy Award for Outstanding Costume Design for a Miniseries or a Special.\n\nTruman (1995 film): Truman is a multi-award-winning 1995 HBO movie based on David McCullough's Pulitzer Prize-winning book, \"Truman\".  Starring Gary Sinise as Harry S. Truman, the film centers on Truman's rise to the presidency from humble beginnings, World War II, and his decision to use the first atomic bomb.  The film's tagline is \"\"It took a farmer's hand to shape a nation.\"\"\n\nList of awards and nominations received by Lost: Lost is an American drama series that aired on ABC from September 22, 2004 until May 23, 2010.  It has been nominated for a variety of different awards, including 54 Primetime Emmy Awards (eleven wins), 48 Saturn Awards (thirteen wins), 33 Teen Choice Awards, 17 Television Critics Association Awards (four wins), 12 Golden Reel Awards (five wins), eight Satellite Awards (one win), seven Golden Globe Awards (one win), six Producers Guild of America Awards (one win), six Writers Guild of America Awards (one win), five Directors Guild of America Awards, two NAACP Image Awards (one win), two Screen Actors Guild Awards (one win), and one BAFTA Award.  Amongst the wins for the series are a Primetime Emmy Award for Outstanding Drama Series, a Golden Globe Award for Best Television Series – Drama, a Screen Actors Guild Award for Outstanding Performance by an Ensemble in a Drama Series, and a Peabody Award.\n\nA Woman of Independent Means: A Woman of Independent Means is an 1995 American television miniseries starring Sally Field.  Sally Field also producer.  Field was nominated for Emmy Award, Golden Globe Award and Screen Actors Guild Awards.  The series was also nominated in the category Primetime Emmy Award for Outstanding Miniseries and Primetime Emmy Award for Outstanding Casting for a Miniseries, Movie, or a Special and won Emmy for Outstanding Individual Achievement in Costume Design for a Miniseries or a Special in 1995.\n\nQuestion: Who is the Emmy Award and Golden Globe Award winner who is in the movie \"Truman\"?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the individual who meets the criteria.\"\n    },\n    \"awards_received\": {\n      \"type\": \"array\",\n      \"description\": \"A list of specific awards won by the person, as mentioned in the question.\",\n      \"items\": {\n        \"type\": \"string\"\n      }\n    },\n    \"movie_details\": {\n      \"type\": \"object\",\n      \"description\": \"Details about the movie the person appeared in.\",\n      \"properties\": {\n        \"movie_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the movie.\"\n        },\n        \"role_played\": {\n          \"type\": \"string\",\n          \"description\": \"The role played by the person in the movie.\"\n        }\n      },\n      \"required\": [\n        \"movie_title\",\n        \"role_played\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"awards_received\",\n    \"movie_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the individual who meets the criteria."
      },
      "awards_received": {
        "type": "array",
        "description": "A list of specific awards won by the person, as mentioned in the question.",
        "items": {
          "type": "string"
        }
      },
      "movie_details": {
        "type": "object",
        "description": "Details about the movie the person appeared in.",
        "properties": {
          "movie_title": {
            "type": "string",
            "description": "The title of the movie."
          },
          "role_played": {
            "type": "string",
            "description": "The role played by the person in the movie."
          }
        },
        "required": [
          "movie_title",
          "role_played"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "person_name",
      "awards_received",
      "movie_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
