{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nIke Mahoney: Frank John Mahoney Jr. (October 25, 1901 – November 21, 1961) was an American football back who played five seasons with the Chicago Cardinals of the National Football League.  He played college football at Creighton University and attended the Omaha High School of Commerce in Omaha, Nebraska.  He was a member of the Chicago Cardinals team that were NFL champions in 1925.  He also played baseball, basketball and participated in track and field.  Mahoney played for the Chicago Bruins of the American Basketball League.  He had received an offer to play baseball for the Pittsburgh Pirates but opted to play football for the Chicago Cardinals.\n\nLove Hurts (Cher album): Love Hurts is the twentieth studio album by American singer-actress Cher, released on June 11, 1991 by Geffen Records.  The RIAA certified it Gold on August 27, 1991.  It is the final studio album with the record label Geffen.  The lead single from the album was, \"Love and Understanding\" and the follow-up singles were \"Save Up All Your Tears\", \"Love Hurts\", \"Could've Been You\" and \"When Lovers Become Strangers\".  It debuted at #48 on the Billboard Top 200 Albums chart with the sales of 19,000.  In November 2011, \"Billboard\" stated that \"Love Hurts\" has sold 600,000 copies in the US.\n\nLove Hurts Tour: The Love Hurts Tour was the third solo concert tour by American recording artist Cher.  The tour supported her twenty first studio album, \"Love Hurts\" and the soundtrack, \"Mermaids\".  The tour reached Europe and North America.  It played in arenas and followed the previous sold-out Heart of Stone Tour.\n\nMike Mahoney (catcher): Michael John Mahoney (born December 5, 1972 in Des Moines, Iowa) is a Major League Baseball catcher, formerly with the St. Louis Cardinals.  He made his major league debut on September 8, 2000 with the Chicago Cubs, and after two seasons in Chicago, he was released and eventually signed with St. Louis.  He started a stretch of games while primary catcher Yadier Molina was injured in , but was not re-signed by the Cardinals after the season.  Related to Mike Mahoney, the producer & writer from New Jersey.  Most recently, he played for the Iowa Cubs in .\n\nWhen Love Hurts: \"When Love Hurts\" is a song recorded by American recording artist JoJo for her third studio album and is included on her \"tringle\" extended play (EP), \"III. \" (2015).  The song was written by Ammar Malik, Benny Blanco, Daniel Omelio, Jason Evigan, creative team \"The XX\" and Ryn Weaver, while Blanco and Evigan also handled the production.  \"When Love Hurts\" is expected to be the first song from the tringle to be promoted to radio via Atlantic Records.  An official remix package was released on October 2, 2015.  The song will officially impact Mainstream radio in the U.S. on November 17, 2015.\n\nShort Cut Draw Blood: Short Cut Draw Blood is the third studio album by the British musician Jim Capaldi, released by Island Records in 1975.  It marked a major turning point in Capaldi's career: it was his first album recorded after the breakup of Traffic, and more importantly it was his commercial breakthrough.  While Capaldi's first two solo albums had been moderately successful in the United States (in fact, in \"Short Cut Draw Blood\" was his least successful album in the United States thus far, with both the album itself and the single \"Love Hurts\" barely scraping into the Billboard charts), \"Short Cut Draw Blood\" enteredthe charts in several other countries for the first time.  This was particularly evident in his native United Kingdom; the single \"It's All Up to You\", released a year before the album, became his first top 40 hit there, only to be overshadowed the following year by his cover of \"Love Hurts\", which went all the way to number 4.\n\nLove Hurts (1991 film): Love Hurts is a comedy-drama film, released in late 1990 in the United Kingdom and 1991 in the United States.  Co-produced and directed by Bud Yorkin, it stars Jeff Daniels, Cynthia Sikes, Cloris Leachman, Judith Ivey and John Mahoney.\n\nChris Mahoney (baseball): Christopher John Mahoney (June 11, 1885 – July 15, 1954) was a pitcher/center fielder in Major League Baseball who played briefly for the Boston Red Sox during the 1910 season.  Listed at 5 ft , 160 lb., Mahoney batted and threw right-handed.  A native of Milton, Massachusetts, he studied at Fordham University and Manhattan College.\n\nJock Mahoney: Jock Mahoney (February 7, 1919 – December 14, 1989) was an American actor and stuntman.  Born Jacques Joseph O'Mahoney, he was credited variously as Jock Mahoney, Jack O'Mahoney or Jock O'Mahoney.  He starred in two western television series, \"The Range Rider\" and \"Yancy Derringer\".  He played Tarzan in two feature films and was associated in various capacities with several other Tarzan productions.\n\nJohn Mahoney: John Mahoney (born 20 June 1940) is a British-American actor.  Born in Blackpool, Lancashire, England, Mahoney started his career on the stage in 1977 as the body double for Steve McQueen and moved into film in 1980.  He played Martin Crane in the American sitcom \"Frasier\" on NBC from 1993 to 2004.  He has also worked as a voice actor, and performed on Broadway and in Chicago theatre.\n\nQuestion: Where was John Mahoney who starred in  Love Hurts, born at?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the actor.\"\n    },\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film the actor starred in.\"\n    },\n    \"birth_location\": {\n      \"type\": \"string\",\n      \"description\": \"The birthplace of the actor.\"\n    },\n    \"birth_date\": {\n      \"type\": \"string\",\n      \"description\": \"The birth date of the actor.\"\n    },\n    \"nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the actor.\"\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"film_title\",\n    \"birth_location\",\n    \"birth_date\",\n    \"nationality\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The full name of the actor."
      },
      "film_title": {
        "type": "string",
        "description": "The title of the film the actor starred in."
      },
      "birth_location": {
        "type": "string",
        "description": "The birthplace of the actor."
      },
      "birth_date": {
        "type": "string",
        "description": "The birth date of the actor."
      },
      "nationality": {
        "type": "string",
        "description": "The nationality of the actor."
      }
    },
    "required": [
      "actor_name",
      "film_title",
      "birth_location",
      "birth_date",
      "nationality"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
