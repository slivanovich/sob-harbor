{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nNoah (2014 film): Noah is a 2014 American epic biblical drama film directed by Darren Aronofsky and inspired by the Biblical story of Noah's Ark from the \"Book of Genesis\".  The film, which was co-written by Aronofsky and Ari Handel, stars Russell Crowe as Noah, along with Jennifer Connelly, Emma Watson, Ray Winstone, Logan Lerman, Douglas Booth, and Anthony Hopkins.  The film was released in North American theaters on March 28, 2014, in 2D and IMAX, while a version of the film converted to 3D and IMAX 3D was released in several other countries.\n\nDarren Aronofsky's unrealized projects: The following is a list of unproduced Darren Aronofsky projects in roughly chronological order.  During his long career, American film director Darren Aronofsky has worked on a number of projects which never progressed beyond the pre-production stage under his direction.  Some of these projects fell in development hell or were cancelled.\n\nRequiem for a Dream: Requiem for a Dream is a 2000 American psychological drama film directed by Darren Aronofsky and starring Ellen Burstyn, Jared Leto, Jennifer Connelly, and Marlon Wayans.  The film is based on the novel of the same name by Hubert Selby, Jr., with whom Aronofsky wrote the screenplay.\n\nAri Handel: Ari Handel (born in Zürich, Switzerland) is an American neuroscientist, film producer, and writer.  He is known for co-writing the films \"Noah\" and \"The Fountain\" with his Harvard Dunster House suitemate Darren Aronofsky and for helping to produce these films along with two other Darren Aronofsky films, \"The Wrestler\" and \"Black Swan\".  He started co-writing the film \"Noah\" around 2003.\n\nThe Fountain (soundtrack): The Fountain: Music from the Motion Picture is the soundtrack album to the 2006 film \"The Fountain\" directed by Darren Aronofsky.  Released on November 27, 2006, through Nonesuch Records, the album is a collaboration between contemporary classical composer and frequent Aronofsky collaborator Clint Mansell, classical string quartet the Kronos Quartet, and post-rock band Mogwai.  The score received mixed reviews from critics and was nominated for several awards.\n\nMother!: Mother!  (stylized as mother!)  is a 2017 American psychological horror film, written and directed by Darren Aronofsky and starring Jennifer Lawrence, Javier Bardem, Ed Harris, and Michelle Pfeiffer.  The plot follows a young woman whose tranquil life with her husband at their country home is disrupted by the arrival of a mysterious couple.\n\nPi (film): Pi, also titled π , is a 1998 American surrealist psychological thriller film written and directed by Darren Aronofsky in his directorial debut.  The film earned Aronofsky the Directing Award at the 1998 Sundance Film Festival, the Independent Spirit Award for Best First Screenplay and the Gotham Open Palm Award.  The title refers to the mathematical constant pi.  The film is notable for its covering of an array of themes including religion, mysticism and the relationship of the universe to mathematics.\n\nMatthew Libatique: Matthew Libatique (born July 19, 1968) is an American cinematographer who is best known for his work with director Darren Aronofsky on the films \"π\" (1998), \"Requiem for a Dream\" (2000), \"The Fountain\" (2006), \"Black Swan\" (2010), \"Noah\" (2014) and \"Mother! \" (2017).\n\nBelow (film): Below is a 2002 American World War II mystery horror film directed by David Twohy, written by Darren Aronofsky, Lucas Sussman, and Twohy, and stars Bruce Greenwood, Olivia Williams, Matthew Davis, Holt McCallany, Scott Foley, Zach Galifianakis, Jason Flemyng, and Dexter Fletcher.  The film tells the story of a United States Navy submarine that experiences a series of supernatural events while on patrol in the Atlantic Ocean in 1943.\n\nJames Chinlund: James Chinlund (born March 17, 1971) was born and raised in New York City.  He studied Fine Art at CalArts in Los Angeles, with a focus on sculpture and large scale installation work.  After graduating, Chinlund returned to New York and started his career in film, first as a carpenter, before finding opportunities as a Production Designer on music videos and independent films.  During this period he first worked with frequent collaborator Darren Aronofsky (\"Requiem for a Dream\", \"The Fountain\") in addition to other directors in the New York independent film world including: Todd Solondz (\"Storytelling\"), Paul Schrader (\"Auto Focus\") and Spike Lee (\"25th Hour\").  Over the years James has been active in the worlds of commercials and fashion as well.  Collaborators include: Inez van Lamsweerde and Vinoodh Matadin, Rupert Sanders, Spike Jonze, Fredrik Bond, Lance Acord, Gus Van Sant and Harmony Korine.  In 2010 he won both the Art Directors Guild and the AICP awards for \"Absolut World\", a commercial collaboration with director Rupert Sanders.  After a short break from features to care for his young daughter, Chinlund returned to the feature world in 2012 to work on \"The Avengers\" for Marvel which set a record for the highest grossing opening weekend of all time.  In 2015 he was nominated for an Art Director’s Guild Award and the Saturn Award for his work on the Fox film \"Dawn of the Planet of the Apes\" directed by Matt Reeves.  Most recently James has completed work on the next film in the Apes series \"War for the Planet of the Apes\".\n\nQuestion: What 2017 movie did Darren Aronofsky and Matthew Libatique work together to film?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"movie_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the movie.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the movie was released.\"\n    },\n    \"director\": {\n      \"type\": \"string\",\n      \"description\": \"The director of the movie.\"\n    },\n    \"cinematographer\": {\n      \"type\": \"string\",\n      \"description\": \"The cinematographer of the movie.\"\n    },\n    \"genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the movie.\"\n    }\n  },\n  \"required\": [\n    \"movie_title\",\n    \"release_year\",\n    \"director\",\n    \"cinematographer\",\n    \"genre\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "movie_title": {
        "type": "string",
        "description": "The title of the movie."
      },
      "release_year": {
        "type": "integer",
        "description": "The year the movie was released."
      },
      "director": {
        "type": "string",
        "description": "The director of the movie."
      },
      "cinematographer": {
        "type": "string",
        "description": "The cinematographer of the movie."
      },
      "genre": {
        "type": "string",
        "description": "The genre of the movie."
      }
    },
    "required": [
      "movie_title",
      "release_year",
      "director",
      "cinematographer",
      "genre"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
