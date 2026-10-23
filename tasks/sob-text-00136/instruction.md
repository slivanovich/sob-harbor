{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPlain Truth (film): Plain Truth is a 2004 TV drama directed by Paul Shapiro, starring Mariska Hargitay, Alison Pill and Jan Niklas.  The film is based on Jodi Picoult's book \"Plain Truth\", where an Amish teen hides a pregnancy, gives birth in secret, and then flatly denies it all when the baby's body is found, urban defense attorney Ellie Harrison decides to defend her.\n\nMy Sister's Keeper (film): My Sisters's Keeper is a 2009 American drama film directed by Nick Cassavetes and starring Cameron Diaz, Abigail Breslin, Sofia Vassilieva, and Alec Baldwin.  Based on Jodi Picoult's novel of the same name, On June 26, 2009 the film was released to cinemas in the United States, Canada, Ireland, Mexico, and the United Kingdom.\n\nSon of the Mask: Son of the Mask is a 2005 American fantasy comedy film directed by Lawrence Guterman.  The film stars Jamie Kennedy as Tim Avery, an aspiring cartoonist from Fringe City who has just had his first child born with the powers of the Mask.  It is the stand-alone sequel to the successful 1994 film \"The Mask\", an adaptation of Dark Horse Comics which starred Jim Carrey and Cameron Diaz.\n\nAny Given Sunday: Any Given Sunday is a 1999 American sports drama film directed by Oliver Stone depicting a fictional professional American football team.  The film features an ensemble cast, including Al Pacino, Cameron Diaz, Dennis Quaid, Jamie Foxx, James Woods, LL Cool J, Ann-Margret, Lauren Holly, Matthew Modine, John C. McGinley, Charlton Heston, Bill Bellamy, Lela Rochon, Aaron Eckhart, Elizabeth Berkley, Marty Wright, and NFL players Jim Brown and Lawrence Taylor.  It is partly based on the novel \"On Any Given Sunday\" by famed NFL defensive end Pat Toomay; the title is derived from a line in the book (also used in the film) that a team can win or lose on \"any given Sunday\", said by the fictitious coach Tony D'Amato.\n\nCameron Diaz: Cameron Michelle Diaz-Madden (born August 30, 1972) is an American actress, comedian, producer, former fashion model and author.  She rose to stardom with roles in \"The Mask\" (1994), \"My Best Friend's Wedding\" (1997) and \"There's Something About Mary\" (1998), and is also known for voicing the character of Princess Fiona in the \"Shrek\" series (2001–2010).  Other high-profile films include \"Charlie's Angels\" (2000) and its sequel \"\" (2003), \"The Sweetest Thing\" (2002), \"In Her Shoes\" (2005), \"The Holiday\" (2006), \"What Happens in Vegas\" (2008), \"My Sister's Keeper\" (2009), \"Knight and Day\" (2010), \"The Green Hornet\" (2011), \"Bad Teacher\" (2011), \"What to Expect When You're Expecting\" (2012), \"The Counselor\" (2013), \"The Other Woman\", \"Sex Tape\", and \" Annie\" (all 2014).\n\nThe Tenth Circle (film): The Tenth Circle is a 2008 Canadian mystery film.  It is based on a Jodi Picoult novel of the same name.  It was shot, in part, in Windsor, Nova Scotia.\n\nThe Invisible Circus (film): The Invisible Circus is a 2001 American drama film written and directed by Adam Brooks and starring Cameron Diaz, Jordana Brewster, and Christopher Eccleston.  Based on the 1995 novel \"The Invisible Circus\" by Jennifer Egan, the film is about a teenage girl who travels to Europe in 1976 in search of answers to her older sister's suicide.  During her search, she falls in love with her dead sister's former boyfriend.  The film premiered at the Sundance Film Festival on January 11, 2001, and was released in the United States on February 2, 2001.\n\nAnnie (2014 film): Annie is a 2014 American musical comedy-drama film directed by Will Gluck and produced by Village Roadshow Pictures and Will Smith's Overbrook Entertainment for Sony Pictures' Columbia Pictures.  A contemporary adaptation of the 1977 Broadway musical of the same name, the film stars Quvenzhané Wallis, Jamie Foxx, Rose Byrne, Bobby Cannavale, and Cameron Diaz.  The third film adaptation, following Columbia's 1982 theatrical film and Disney's 1999 television film, \"Annie\" began production in August 2013 and opened on December 19, 2014 to generally negative reviews, and was not a box office success, grossing only $133 million against a below-line production cost of over $65 million.\n\nThe Mask (film): The Mask is a 1994 American superhero fantasy comedy film directed by Charles Russell, produced by Bob Engelman, and written by Mike Werb, based on the comic series of the same name distributed by Dark Horse Comics.  The film stars Jim Carrey, Peter Greene, Amy Yasbeck, Peter Riegert, Richard Jeni, Ben Stein, Joely Fisher, and Cameron Diaz in her film debut.  It revolves around an unlucky bank clerk finding a mask that grants the wearer cartoon-like superpowers.\n\nIn Her Shoes (film): In Her Shoes is a 2005 American comedy-drama film based on the novel of the same name by Jennifer Weiner.  It is directed by Curtis Hanson with an adapted screenplay by Susannah Grant and stars Cameron Diaz, Toni Collette, and Shirley MacLaine.  The film focuses on the relationship between two sisters and their grandmother.\n\nQuestion: Cameron Diaz rose to stardom in \"The Mask\" (1994), who directed the drama film that was based on Jodi Picoult's novel of the same name?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the drama film based on a Jodi Picoult novel of the same name.\"\n    },\n    \"director_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the director of the identified film.\"\n    },\n    \"based_on_author\": {\n      \"type\": \"string\",\n      \"description\": \"The author whose novel the film is based on.\"\n    },\n    \"film_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the film.\"\n    },\n    \"stars_cameron_diaz\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates whether Cameron Diaz stars in this film.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"director_name\",\n    \"based_on_author\",\n    \"film_genre\",\n    \"stars_cameron_diaz\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the drama film based on a Jodi Picoult novel of the same name."
      },
      "director_name": {
        "type": "string",
        "description": "The name of the director of the identified film."
      },
      "based_on_author": {
        "type": "string",
        "description": "The author whose novel the film is based on."
      },
      "film_genre": {
        "type": "string",
        "description": "The genre of the film."
      },
      "stars_cameron_diaz": {
        "type": "boolean",
        "description": "Indicates whether Cameron Diaz stars in this film."
      }
    },
    "required": [
      "film_title",
      "director_name",
      "based_on_author",
      "film_genre",
      "stars_cameron_diaz"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
