{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSpycraft: The Great Game: Spycraft (also known by its full title, Spycraft: The Great Game) is an adventure CD-ROM game published by Activision in 1996.  It details the attempted assassination of the President of the United States and the CIA and SVR attempts to save him.  Although the game was not approved by either organization, it tends to favour realism due to its coordination with former CIA director William Colby and former KGB Major-General Oleg Kalugin, who also appear in the game as themselves.  The game also stars James Karen, Dennis Lipscomb, Joseph Ruskin, Tim De Zarn, Kirk B.R. Woller, Allan Kolman and Charles Napier in prominent roles.\n\nHardbodies 2: Hardbodies 2 is a 1986 adult comedy movie sequel to the 1984 film \"Hardbodies\".  It was directed by Mark Griffiths and featured Brad Zutaut, Fabiana Udenio, James Karen and Alba Francesca.  The plot\n\nWillow Smith: Willow Camille Reign Smith (born October 31, 2000), known professionally as Willow, is an American singer, actress and dancer.  She is the daughter of Will Smith and Jada Pinkett Smith, the younger sister of Jaden Smith and the half-sister of Willard Carroll \"Trey\" Smith III.  Smith made her acting debut in 2007 in the film \"I Am Legend\" and later appeared in \"\" alongside Abigail Breslin.  She received a Young Artist Award for her performance.\n\nFrankenstein Meets the Space Monster: Frankenstein Meets the Space Monster (sometimes stylized as Frankenstein Meets the Spacemonster) (1965) is a science fiction cult film, directed by Robert Gaffney and starring Marilyn Hanold, James Karen, and Lou Cutell.  It was filmed in Florida and Puerto Rico in 1964\n\nMorris Carnovsky: Morris Carnovsky (September 5, 1897 – September 1, 1992) was an American stage and film actor.  He was one of the founders of the Group Theatre (1931-1940) in New York City and had a thriving acting career both on Broadway and in films until, in the early 1950s, professional colleagues told the House Un-American Activities Committee that Carnovsky had been a Communist Party member.  He was blacklisted and worked less frequently for a few years, but then re-established his acting career, taking on many Shakespearean roles at the Stratford Shakespeare Festival and performing the title roles in college campus productions of \"King Lear\" and \"The Merchant of Venice\".  Carnovsky's nephew is veteran character actor and longtime \"Pathmark Guy\" James Karen.\n\nThe Pursuit of Happyness: The Pursuit of Happyness is a 2006 American biographical drama film based on entrepreneur Chris Gardner's nearly one-year struggle being homeless.  Directed by Gabriele Muccino, the film features Will Smith as Gardner, a homeless salesman.  Smith's son Jaden Smith co-stars, making his film debut as Gardner's son, Christopher Jr.\n\nJourney into Medicine: Journey into Medicine is a 1947 American documentary-style film.  The film stars James Karen as Michael Kenneth Marshall, a young medical student who goes through medical training at Columbia and Cornell.  During his internship in pediatrics, Marshall loses one of his patients, a young girl to diphtheria.  This case inspires him to enroll in the Johns Hopkins School of Public Health and pursue a career in public health.  While studying at Johns Hopkins, Marshall helps battle an outbreak of diphtheria in Baltimore, which confirms to him his chosen vocation.\n\nJames Karen: James Karen (born Jacob Karnofsky; November 28, 1923) is an American character actor of Broadway, film and television.  Karen is best remembered for his roles in \"Poltergeist\", \"The Return of the Living Dead\", \"Invaders from Mars\", and in \"The Pursuit of Happyness\".\n\nSam's Son: Sam's Son is a 1984 American semi-autobiographical coming-of-age drama film written and directed by Michael Landon loosely based on his early life and is also the only feature film ever made by him.  The film stars Eli Wallach, Anne Jackson, Timothy Patrick Murphy, Hallie Todd, Jonna Lee, James Karen, and even Landon in a cameo at the beginning and the end.  The film was produced independently by Landon himself and released by Utah-based distributor Invictus Entertainment.\n\nThe Return of the Living Dead: The Return of the Living Dead is a 1985 American horror comedy film written and directed by Dan O'Bannon, and starring Clu Gulager, James Karen, and Don Calfa.  The film tells the story of how a warehouse owner accompanied by his two employees, mortician friend, and a group of teenage punks deal with the accidental release of a horde of brain-hungry zombies onto an unsuspecting town.\n\nQuestion: Which film that stars Will Smith is James Karen known for acting in?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"film_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the film.\"\n    },\n    \"main_actors\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of prominent actors in the film.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"film_genre\",\n    \"main_actors\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "release_year": {
        "type": "integer",
        "description": "The release year of the film."
      },
      "film_genre": {
        "type": "string",
        "description": "The genre of the film."
      },
      "main_actors": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of prominent actors in the film."
      }
    },
    "required": [
      "film_title",
      "release_year",
      "film_genre",
      "main_actors"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
