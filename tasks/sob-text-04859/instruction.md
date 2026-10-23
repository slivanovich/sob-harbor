{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nShawn Hatosy: Shawn Wayne Hatosy (born December 29, 1975) is an American film and television actor.  He is perhaps best known for his roles in the films \"In & Out\", \"The Faculty\", \"Outside Providence\", \"Anywhere but Here\", \"\", \"The Cooler\", and \"Alpha Dog\".  He is also known for role as Detective Sammy Bryant on the TNT crime drama series \"Southland\" and is currently starring as Pope Cody in the TNT crime drama series, \"Animal Kingdom\", based on the Australian film of the same name.\n\nJake Weary: Jacob \"Jake\" Weary (born February 14, 1990) is an American actor, musician, singer-songwriter and music producer.  He is best known for his roles as Luke Snyder on the CBS soap opera \"As the World Turns\", Vince Keeler in NBC's action-drama series \"Chicago Fire\", and for his role as Kevin Dawg in \"\" (2010) and its two sequels and television adaptation, Nickelodeon's \"\".  He currently stars as Deran Cody in the TNT drama series \"Animal Kingdom\", based on the Australian film of the same name.\n\nEllen Barkin: Ellen Rona Barkin (born April 16, 1954) is an American actress and film producer.  Her breakthrough role was in the 1982 comedy-drama film \"Diner\", and the following years she had starring roles in films include \"Tender Mercies\" (1983), \"The Adventures of Buckaroo Banzai Across the 8th Dimension\" (1984), and \"The Big Easy\" (1987).\n\nFilm Critics Circle of Australia Awards 2011: The 19th Film Critics Circle of Australia Awards, honoring the best in films from 2010, were presented on 13 March 2011 at North Sydney Leagues Club in Cammeray, New South Wales and hosted by Rod Quinn.  The nominees were announced on 8 February 2011 with \"Animal Kingdom\" receiving ten nominations.  \"Animal Kingdom\" won six awards, including Best Film and Best Director.\n\nList of Animal Kingdom episodes: \"Animal Kingdom\" is an American drama television series developed by Jonathan Lisco, based on the 2010 Australian film by David Michôd.  The series follows a 17-year-old boy, who, after the death of his mother, moves in with the Codys, a criminal family clan governed by matriarch Janine \"Smurf\" Cody (Ellen Barkin).  \"Animal Kingdom\" debuted on TNT on June 14, 2016.\n\nBreakthrough role: A breakthrough role, also known as breakout role, is a term in the film industry to describe the performance of an actor or actress in a film or television show which contributed significantly to the development of their career and beginning of critical recognition.  Such a moment in an actor's career may often occur some time after they begin acting as their roles become more substantial.  Often a breakthrough role is a significant increase in importance in the actor's part in the film moving up from a minor character or extra to one of the leading cast, or a \"high impact\" role in a film which has mainstream success and results in the widespread recognition or popularity of the actor.  Martin Shingler defines a breakthrough performance as one which \"attracts the attention of film critics, or receives rave reviews and is subsequently nominated for a major film award.\"\n\nAnne Hathaway on screen and stage: Anne Hathaway is an American actress who has appeared in film and stage.  She made her acting debut in the short lived television series \"Get Real\" (1999-2000).  Hathaway's breakthrough role came with the role of Mia Thermopolis in the successful Disney comedy \"The Princess Diaries\" (2001).  The role established her as a teen idol and she later reprised the role in its .  This was followed by a string of family-oriented films, including \"Nicholas Nickleby\" (2002) and \"Ella Enchanted\" (2004), all of which were unsuccessful.  In 2005, she voiced the lead character in the highly successful animated film \"Hoodwinked! \".  The same year, she made transition to more mature roles with the acclaimed \"Brokeback Mountain\".  In 2006, Hathaway starred opposite Meryl Streep in the comedy-drama \"The Devil Wears Prada\" and portrayed Jane Austen in the biographical drama \"Becoming Jane\", the following year.\n\nAnimal Kingdom (TV series): Animal Kingdom is an American drama television series developed by Jonathan Lisco.  It is based on the 2010 Australian film by David Michôd, who is executive producer for the series, alongside Liz Watts who also produced the movie.  The series follows a 17-year-old boy, who, after the death of his mother, moves in with the Codys, a criminal family clan governed by matriarch Smurf.  Ellen Barkin portrays the leading role of Janine \"Smurf\" Cody, played by Jacki Weaver in the 2010 film.  \"Animal Kingdom\" debuted on TNT on June 14, 2016, and was renewed for a second season on July 6, 2016, of thirteen episodes that premiered on May 30, 2017.  On July 27, 2017, TNT renewed the series for a third season.\n\nJames Frecheville: James Aitken Frecheville (pronounced \"\"fresh-ville\"\"; born 1991) is an Australian actor known for his lead role in the Australian film \"Animal Kingdom\" as Joshua \"J\" Cody, a confused teenager and youngest member of a criminal family in Melbourne's underworld.\n\nAnimal Kingdom (horse): Animal Kingdom (foaled in Kentucky on March 20, 2008) is an American Thoroughbred racehorse best known for winning the 137th Kentucky Derby and the 2013 Dubai World Cup.  His Derby win took place on May 7, 2011, before a record crowd of 164,858.  After the Derby, Animal Kingdom finished second in the Preakness Stakes and sixth in the Belmont Stakes before his career was disrupted by injury.  He returned to finish second in the 2012 Breeders' Cup Mile before winning the Dubai World Cup as a five-year-old in 2013.  Animal Kingdom is the first Kentucky Derby winner to win a Grade 1 race at the age of five.  He has won Grade 1 races on both dirt and synthetic surfaces.\n\nQuestion: In what film did  the American actress who portrayed Janine \"Smurf\" Cody in \"Animal Kingdom\" play her breakthrough role?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actress_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actress.\"\n    },\n    \"character_played\": {\n      \"type\": \"string\",\n      \"description\": \"The character played by the actress in 'Animal Kingdom'.\"\n    },\n    \"tv_series_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the TV series where the character was played.\"\n    },\n    \"breakthrough_role_film\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film that was the actress's breakthrough role.\"\n    },\n    \"breakthrough_role_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the breakthrough role film was released.\"\n    }\n  },\n  \"required\": [\n    \"actress_name\",\n    \"character_played\",\n    \"tv_series_name\",\n    \"breakthrough_role_film\",\n    \"breakthrough_role_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actress_name": {
        "type": "string",
        "description": "The name of the actress."
      },
      "character_played": {
        "type": "string",
        "description": "The character played by the actress in 'Animal Kingdom'."
      },
      "tv_series_name": {
        "type": "string",
        "description": "The name of the TV series where the character was played."
      },
      "breakthrough_role_film": {
        "type": "string",
        "description": "The title of the film that was the actress's breakthrough role."
      },
      "breakthrough_role_year": {
        "type": "integer",
        "description": "The year the breakthrough role film was released."
      }
    },
    "required": [
      "actress_name",
      "character_played",
      "tv_series_name",
      "breakthrough_role_film",
      "breakthrough_role_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
