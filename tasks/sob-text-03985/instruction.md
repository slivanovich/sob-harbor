{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nList of Scooby-Doo characters: This is a list of \"Scooby-Doo\" characters.  Scooby-Doo is an American animated franchise based around several animated television series and animated, as well as live action, movies.  There are five main characters in the franchise: Scooby-Doo Shaggy Rogers, Fred Jones, Velma Dinkley, and Daphne Blake—known as \"Mystery Incorporated\".  There are also several recurring characters throughout the franchise, including their parents, friends, allies, and enemies.\n\nScooby-Doo: Scooby-Doo is an American animated cartoon franchise, comprising several animated television series produced from 1969 to the present day.  The original series, \"Scooby-Doo, Where Are You! \", was created for Hanna-Barbera Productions by writers Joe Ruby and Ken Spears in 1969.  This Saturday-morning cartoon series featured four teenagers—Fred Jones, Daphne Blake, Velma Dinkley, and Norville \"Shaggy\" Rogers—and their talking brown Great Dane named Scooby-Doo, who solve mysteries involving supposedly supernatural creatures through a series of antics and missteps.\n\nRory Culkin: Rory Hugh Culkin (born July 21, 1989) is an American actor who is known for his roles in \"Scream 4\", \"You Can Count on Me\" and M. Night Shyamalan's \"Signs\" and is the younger brother of actors Macaulay Culkin and Kieran Culkin.\n\nParty Monster (film): Party Monster is a 2003 American factually based biographical drama film directed by Fenton Bailey and Randy Barbato, and starring Macaulay Culkin as the drug-addled \"king of the Club Kids\".  The film tells the story of rise and fall of the infamous New York City party promoter Michael Alig.  This was Macaulay Culkin's first film in nearly nine years since his starring role in the 1994 film \"Richie Rich\".\n\nWhat's New, Scooby-Doo?: What's New, Scooby-Doo?  is an American animated sitcom mystery comedy series produced by Warner Bros.  Animation for The WB television network; it is the ninth incarnation of the \"Scooby-Doo\" franchise that began with Hanna-Barbera's \"Scooby-Doo, Where Are You! \" and the first of such since the previous incarnation, \"A Pup Named Scooby-Doo\", ended in 1991.  The series revives the format of \"Scooby-Doo, Where Are You!\" , in which the title character and his companions, Fred Jones; Daphne Blake; Velma Dinkley and Shaggy Rogers, travel to varying locations solving mysteries; this format is modernized for \"What's New, Scooby-Doo?\" , in which the characters utilize technology that did not exist at the time \"Scooby-Doo, Where Are You!\"  first aired.  It is the first television series in the franchise in which Frank Welker, Grey DeLisle and Mindy Cohn respectively portrayed the voices of Scooby-Doo, Daphne and Velma; and the final one in which Casey Kasem portrayed Shaggy, having originally quit the role following a dispute regarding the portrayal of the character.\n\nRichie Rich (film series): The Richie Rich films is a series of American family films consist of two, based on the character of the same name, who was originally featured in Harvey Comics.  The first film was theatrical release directed by Donald Petrie, that stars Macaulay Culkin.  Its sequel was a direct-to-video feature directed by John Murlowski, starring David Gallagher replacing Macaulay Culkin.  Both films were distributed by Warner Bros.\n\nFrank Welker: Franklin Wendell Welker (born March 12, 1946) is an American actor, who for most of his career has specialized as a voice actor.  He is best known for his role as Fred Jones from the \"Scooby-Doo\" franchise since its conception in 1969, as the only original voice actor still with the \"Scooby-Doo\" franchise, along with the voice of Megatron in the \"Transformers\" franchise, specifically \"Transformers G1\" and \"\", as well as Scooby-Doo since 2002.  He is also well known as both the vocal effects and the voice of Nibbler in \"Futurama\".\n\nRichie Rich (film): Richie Rich (sometimes stylized as \"Ri¢hie Ri¢h\") is a 1994 American comedy film directed by Donald Petrie, based on the Harvey Comics cartoon character of the same name created by Alfred Harvey and Warren Kremer.  The film stars Macaulay Culkin, John Larroquette, Edward Herrmann, Jonathan Hyde, and Christine Ebersole while Reggie Jackson, Claudia Schiffer, and Ben Stein appear in cameo roles.  Culkin's younger brother, Rory Culkin, played the part of young Richie.  While in theaters, the film was shown with a Wile E. Coyote and The Road Runner cartoon called \"Chariots of Fur\".\n\nList of What's New, Scooby-Doo? episodes: \"What's New, Scooby-Doo? \" is an American animated mystery-comedy series.  The show was broadcast from September 14, 2002 to July 21, 2006 on Kids WB, a Saturday morning children's programming block on The WB Television Network.  This is the ninth incarnation of the \"Scooby-Doo\" franchise, and features the main characters - Fred Jones, Daphne Blake, Velma Dinkley, Shaggy Rogers and Scooby-Doo - investigating appearances of supernatural creatures.\n\nThe Pagemaster: The Pagemaster is a 1994 American live-action/animated fantasy adventure film starring Macaulay Culkin, Christopher Lloyd, Whoopi Goldberg, Patrick Stewart, Leonard Nimoy, and Frank Welker.  The film was produced by Turner Pictures and released by 20th Century Fox on November 23, 1994.\n\nQuestion: The actor that voices Fred Jones in the \"Scooby-Doo\" franchise also appears wtih Macaulay Culkin in a 1994 adventure film produced by what company?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the adventure film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"main_actors\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"List of main actors in the film.\"\n    },\n    \"voice_actor_in_film\": {\n      \"type\": \"string\",\n      \"description\": \"The voice actor who also voices Fred Jones in Scooby-Doo.\"\n    },\n    \"production_company\": {\n      \"type\": \"string\",\n      \"description\": \"The company that produced the film.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"main_actors\",\n    \"voice_actor_in_film\",\n    \"production_company\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the adventure film."
      },
      "release_year": {
        "type": "integer",
        "description": "The release year of the film."
      },
      "main_actors": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "List of main actors in the film."
      },
      "voice_actor_in_film": {
        "type": "string",
        "description": "The voice actor who also voices Fred Jones in Scooby-Doo."
      },
      "production_company": {
        "type": "string",
        "description": "The company that produced the film."
      }
    },
    "required": [
      "film_title",
      "release_year",
      "main_actors",
      "voice_actor_in_film",
      "production_company"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
