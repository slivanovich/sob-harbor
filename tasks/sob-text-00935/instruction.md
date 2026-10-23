{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJon Voight: Jonathan Vincent Voight ( ; born December 29, 1938) is an American actor.  He is the winner of one Academy Award, having been nominated for four.  He has also won four Golden Globe Awards and was nominated for eleven.  He is the father of actress Angelina Jolie and actor James Haven.\n\nIn the Land of Blood and Honey: In the Land of Blood and Honey is a 2011 American war film written, produced, and directed by Angelina Jolie and starring Zana Marjanović, Goran Kostić, and Rade Šerbedžija.  The film, Jolie's first commercial release as a director, depicts a love story set against the background of the Bosnian War.  It opened in the United States on December 23, 2011, in a limited theatrical release.\n\nFirst They Killed My Father (film): First They Killed My Father (Khmer: មុន​ដំបូង​ខ្មែរ​ក្រហម​សម្លាប់​ប៉ា​របស់​ខ្ញុំ \"Moun​ dambaung​ Khmer​ Krahm​ samleab​ ba​ robsa​ khnhom\") is a 2017 biographical historical thriller film directed by Angelina Jolie and written by Jolie and Loung Ung, based on Ung's memoir of the same name.  Set in 1975, the film depicts 5-year-old Ung who is forced to be trained as a child soldier while her siblings are sent to labor camps during the Khmer Rouge regime.\n\nAptostichus angelinajolieae: The Angelina Jolie trapdoor spider (\"Aptostichus angelinajolieae\", often misspelled \"angelinajoleae\") is a species of Euctenizidae, nocturnal arthropods who seize their prey after leaping out of their burrows and inject it with venom.  It was described by the Auburn University professor Jason Bond in 2008, who named it after the American actress Angelina Jolie in recognition of her work on the United Nations High Commission for Refugees.  It was one of only seven described species of \"Aptostichus\" until 2012, when it was joined by Bono's Joshua Tree trapdoor spider and 32 other species.\n\nCyborg 2: Cyborg 2, released in some countries as Glass Shadow, is a 1993 American science fiction action film directed by Michael Schroeder and starring Elias Koteas, Angelina Jolie, Billy Drago, Karen Sheperd and Jack Palance.  It is an unrelated sequel to the 1989 film \"Cyborg\", although footage from the original is used in a dream sequence.  It was also Jolie's film debut in a starring role (she had previously made an earlier film, \"Lookin' to Get Out\", as a child actress).  It was followed by the 1995 direct-to-video release \"\".\n\nBy the Sea (2015 film): By the Sea is a 2015 American romantic drama film written and directed by Angelina Jolie, and produced by and starring Jolie and Brad Pitt.  The film was released on November 13, 2015, by Universal Pictures.\n\nAngelina Jolie: Angelina Jolie Pitt ( ; née Voight; born June 4, 1975) is an American actress, filmmaker, and humanitarian.  She has received an Academy Award, two Screen Actors Guild Awards, and three Golden Globe Awards, and has been cited as Hollywood's highest-paid actress.  Jolie made her screen debut as a child alongside her father, Jon Voight, in \"Lookin' to Get Out\" (1982).  Her film career began in earnest a decade later with the low-budget production \"Cyborg 2\" (1993), followed by her first leading role in a major film, \"Hackers\" (1995).  She starred in the critically acclaimed biographical cable films \"George Wallace\" (1997) and \"Gia\" (1998), and won an Academy Award for Best Supporting Actress for her performance in the drama \"Girl, Interrupted\" (1999).\n\nAngelina Jolie filmography: Angelina Jolie is an American actress and filmmaker.  As a child, she made her screen debut in the 1982 comedy film \"Lookin' to Get Out\", acting alongside her father Jon Voight.  Eleven years later she appeared in her next feature, the low-budget film \"Cyborg 2\", a commercial failure.  She then starred as a teenage hacker in the 1995 science fiction thriller \"Hackers\", which went on to be a cult film despite performing poorly at the box-office.  Jolie's career prospects improved with a supporting role in the made-for-television film \"George Wallace\" (1997), for which she received the Golden Globe Award for Best Supporting Actress – Television Film.  She made her breakthrough the following year in HBO's television film \"Gia\" (1998).  For her performance in the title role of fashion model Gia Carangi, she won the Golden Globe Award for Best Actress – Television Film.\n\nSalt (2010 film): Salt is a 2010 American action thriller film directed by Phillip Noyce, written by Kurt Wimmer, and starring Angelina Jolie, Liev Schreiber, Daniel Olbrychski, August Diehl, and Chiwetel Ejiofor.  Jolie plays Evelyn Salt, who is accused of being a Russian sleeper agent and goes on the run to try to clear her name.\n\nFour Christmases: Four Christmases (Four Holidays in Australia and New Zealand, Anywhere But Home in the Netherlands, Norway, United Arab Emirates and in South Africa) is a Christmas-themed romantic comedy film about a couple visiting all four of their divorced parents' homes on Christmas Day.  The film is produced by Spyglass Entertainment released by New Line Cinema on November 26, 2008, the day before Thanksgiving, and distributed by Warner Bros.  Pictures.  It stars Vince Vaughn and Reese Witherspoon, with Sissy Spacek, Mary Steenburgen, Robert Duvall, Jon Voight, Jon Favreau, Tim McGraw, Dwight Yoakam, and Kristin Chenoweth as supporting cast.  The film is director Seth Gordon's first studio feature film.  The DVD and Blu-ray Disc was released on November 24, 2009.\n\nQuestion: In what year was a Christmas movie starring the father of Angelina Jolie released?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"movie_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the Christmas movie.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the movie was released.\"\n    },\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of Angelina Jolie's father who starred in the movie.\"\n    },\n    \"relationship_to_angelina_jolie\": {\n      \"type\": \"string\",\n      \"description\": \"The relationship of the actor to Angelina Jolie.\"\n    },\n    \"movie_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the movie.\"\n    }\n  },\n  \"required\": [\n    \"movie_title\",\n    \"release_year\",\n    \"actor_name\",\n    \"relationship_to_angelina_jolie\",\n    \"movie_genre\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "movie_title": {
        "type": "string",
        "description": "The title of the Christmas movie."
      },
      "release_year": {
        "type": "integer",
        "description": "The year the movie was released."
      },
      "actor_name": {
        "type": "string",
        "description": "The name of Angelina Jolie's father who starred in the movie."
      },
      "relationship_to_angelina_jolie": {
        "type": "string",
        "description": "The relationship of the actor to Angelina Jolie."
      },
      "movie_genre": {
        "type": "string",
        "description": "The genre of the movie."
      }
    },
    "required": [
      "movie_title",
      "release_year",
      "actor_name",
      "relationship_to_angelina_jolie",
      "movie_genre"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
