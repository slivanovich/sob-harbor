{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBabes on Broadway: Babes on Broadway is a 1941 American musical film starring Mickey Rooney and Judy Garland and directed by Busby Berkeley, with Vincente Minnelli directing Garland's big solo numbers.  The film, which features Fay Bainter and Virginia Weidler, was the third in the \"Backyard Musical\" series about kids who put on their own show, following \"Babes in Arms\" (1939) and \"Strike Up the Band\" (1940).  Songs in the film include \"Babes on Broadway\" by Burton Lane (music) and E.Y. \"Yip\" Harburg (lyrics), and \"How About You? \" by Lane with lyrics by Ralph Freed, the brother of producer Arthur Freed.  The movie ends with a minstrel show performed by the main cast in blackface.\n\nMary Martin: Mary Virginia Martin (December 1, 1913 – November 3, 1990) was an American actress, singer, and Broadway star.  A muse of Rodgers and Hammerstein, she originated many leading roles over her career including Nellie Forbush in \"South Pacific\" and Maria von Trapp in \"The Sound of Music\".  She was named a Kennedy Center Honoree in 1989.  She was the mother of actor Larry Hagman.\n\nSailors on Leave: Sailors on Leave is a 1941 American musical film directed by Albert S. Rogell and written by Art Arthur and Malcolm Stuart Boylan.  The film stars William Lundigan, Shirley Ross, Chick Chandler, Ruth Donnelly, Mae Clarke and Cliff Nazarro.  The film was released on September 30, 1941, by Republic Pictures.\n\nWashington Chamber Symphony: The Washington Chamber Symphony (WCS) was an American chamber orchestra based in Washington, D.C. which was active during the last quarter of the 20th century.  Founded in 1976 by conductor Stephen Simon, the orchestra was originally titled the Handel Festival Orchestra.  Initially the orchestra was essentially the resident ensemble for the annual Handel Festival at the John F. Kennedy Center for the Performing Arts.  However, as time went on the orchestra began to expand its repertoire beyond Handel into a broad range of works from a variety of musical periods, including contemporary works.  When the Kennedy Center's Handel Festival ceased in 1987, the orchestra changed its name to the Washington Chamber Symphony and continued to offer an annual concert series at the Kennedy Center Terrace Theater.  The orchestra disbanded suddenly in July 2002, citing post 9/11 financial difficulties as the reason.\n\nBirth of the Blues: Birth of the Blues is a 1941 American musical film directed by Victor Schertzinger and starring Bing Crosby, Mary Martin and Brian Donlevy.\n\nHonolulu Lu: Honolulu Lu is a 1941 American musical film directed by Charles Barton and written by Eliot Gibbons.  The film stars Lupe Velez, Bruce Bennett, Leo Carrillo, Marjorie Gateson, Don Beddoe and Forrest Tucker.  The film was released December 11, 1941, by Columbia Pictures.\n\nNice Girl?: Nice Girl?  is a 1941 American musical film directed by William A. Seiter and starring Deanna Durbin, Franchot Tone, Walter Brennan, Robert Stack, and Robert Benchley.  Based on the play \"Nice Girl?\"  by Phyllis Duganne, the film is about a young girl who finds herself attracted to one of her father's business partners who comes to town to give her father a scholarship for his dietary studies.\n\nMoonlight in Hawaii: Moonlight in Hawaii is a 1941 American musical film comedy starring Jane Frazee.\n\nThe Chocolate Soldier (film): The Chocolate Soldier is a 1941 American musical film directed by Roy Del Ruth.  Using the original music by Oscar Straus the plot is somewhat loosely based on the Ferenc Molnár play entitled \"Testőr\" and is unrelated to either the original play or the Oscar Straus operetta.\n\nMark Twain Prize for American Humor: The Mark Twain Prize for American Humor is an American award for humor awarded by the John F. Kennedy Center for the Performing Arts annually since 1998.  It is named after the 19th century novelist, essayist and humorist Mark Twain and is presented to an individual who has made a significant contribution to American humor.  The prize is presented and the show is taped in the Kennedy Center Concert Hall in Washington DC, during which the honoree is celebrated by his or her peers.  The event is a significant fundraiser to benefit the Kennedy Center, which sells tickets as well as access to dinners and after-parties featuring the celebrities.\n\nQuestion: Who co starred in a 1941 American musical film with a Kennedy Center Honeree?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the American musical film.\"\n    },\n    \"film_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"film_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the film.\"\n    },\n    \"kennedy_center_honoree\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the Kennedy Center Honoree.\"\n        },\n        \"award_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the individual was named a Kennedy Center Honoree.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"award_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"co_star_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor who co-starred with the Kennedy Center Honoree in the film.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"film_year\",\n    \"film_genre\",\n    \"kennedy_center_honoree\",\n    \"co_star_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the American musical film."
      },
      "film_year": {
        "type": "integer",
        "description": "The release year of the film."
      },
      "film_genre": {
        "type": "string",
        "description": "The genre of the film."
      },
      "kennedy_center_honoree": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the Kennedy Center Honoree."
          },
          "award_year": {
            "type": "integer",
            "description": "The year the individual was named a Kennedy Center Honoree."
          }
        },
        "required": [
          "name",
          "award_year"
        ],
        "additionalProperties": false
      },
      "co_star_name": {
        "type": "string",
        "description": "The name of the actor who co-starred with the Kennedy Center Honoree in the film."
      }
    },
    "required": [
      "film_title",
      "film_year",
      "film_genre",
      "kennedy_center_honoree",
      "co_star_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
