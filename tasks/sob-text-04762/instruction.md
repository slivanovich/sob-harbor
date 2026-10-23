{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nEvita (1996 film): Evita is a 1996 American musical drama film based on the 1976 concept album of the same name produced by Tim Rice and Andrew Lloyd Webber, which also inspired a 1978 musical.  The film depicts the life of Eva Perón, detailing her beginnings, rise to fame, political career and death at the age of 33.  Directed by Alan Parker, and written by Parker and Oliver Stone, \"Evita\" stars Madonna as Eva, Jonathan Pryce as Eva's husband Juan Perón, and Antonio Banderas as Ché, an everyman who acts as the film's narrator.\n\nBugsy Malone: Bugsy Malone is a 1976 British musical gangster comedy film, directed by Alan Parker and featuring only child actors. Set in New York City, the film is loosely based on events in New York and Chicago from the early 1920s to 1931 during Prohibition, specifically the exploits of real-life gangsters like Al Capone and Bugs Moran, as dramatized in cinema.  Parker lightened the subject matter considerably for the children's market; in the U.S. the film received a G rating.\n\nPink Floyd – The Wall: Pink Floyd – The Wall is a 1982 British live-action/animated musical drama film directed by Alan Parker with animated segments by political cartoonist Gerald Scarfe, and is based on the 1979 Pink Floyd album of the same name.  The film centers around a confined rocker named Pink, who, after being driven into insanity by the death of his father and many depressive moments during his lifetime, constructs a metaphorical (and sometimes physical) wall to be protected from the world and emotional situations around him.  When this coping mechanism backfires he puts himself on trial and sets himself free.  The screenplay was written by Pink Floyd vocalist and bassist Roger Waters.\n\nList of accolades received by Evita (1996 film): \"Evita\" is a 1996 American musical drama film based on Tim Rice and Andrew Lloyd Webber's musical of the same name about First Lady of Argentina, Eva Perón.  Directed by Alan Parker and written by Parker and Oliver Stone, the film starred Madonna, Antonio Banderas, and Jonathan Pryce in the leading roles of Eva, Ché and Juan Perón respectively.  Rice and Webber composed the film's musical score, while Darius Khondji was the cinematographer.  Vincent Paterson created the choreography for the film and Gerry Hambling was responsible for editing.  Penny Rose designed and created the period costumes for the film, and Brian Morris was the set designer.\n\nThe Life of David Gale: The Life of David Gale is a 2003 American drama film directed by Alan Parker (in his final film as a director) and written by Charles Randolph.  The film is an international co-production, between the United States, Germany and the United Kingdom.\n\nEvita (soundtrack): Evita is the third soundtrack album by American singer Madonna.  It was released on November 12, 1996, by Warner Bros.  Records to promote the 1996 American musical drama film, \"Evita\".  The film was based on Tim Rice and Andrew Lloyd Webber's 1978 musical of the same name, about First Lady of Argentina, Eva Perón.  Additional performers on \"Evita\" include Antonio Banderas, Jonathan Pryce and Jimmy Nail, but it is considered a Madonna album since she sang majority of the songs.  After securing the title role in \"Evita\", Madonna underwent vocal training in order to enhance her singing abilities.  Director Alan Parker worked with Rice and Lloyd Webber to compose the soundtrack, reworking the original songs as well as write a new song, \"You Must Love Me\", for the film.\n\nAlan Parker (radio show): Alan Parker was a short radio series broadcast in February–March 1995.  There were 6 hour-long episodes that were broadcast on BBC Radio 1.  It starred Simon Munnery as Alan Parker, a left-wing character (not to be confused with the director of the same name).\n\nThe Commitments (film): The Commitments is a 1991 Irish-British-American musical comedy-drama film based on the 1987 novel of the same name by Roddy Doyle.  It was directed by Alan Parker, and written by Doyle, Dick Clement and Ian La Frenais.  Set in the Dublin Northside, the film tells the story of Jimmy Rabbitte (Robert Arkins), a young music fanatic who assembles a group of working-class youths to form a soul band named \"The Commitments\".\n\nAngeline Ball: Angeline Ball is an Irish actress who currently resides in London, England.  She is a trained dancer in ballet, tap and modern dance.  Her breakthrough role came in 1991 when she starred as backing singer Imelda Quirke in Alan Parker's \"The Commitments\".  Since then she has appeared in various films and television series both in Ireland and in America.  Most notably, she played Vada's mother in \"My Girl 2\" for which she sang a rendition of Charlie Chaplin's \"Smile\".  She worked with Alan Parker again when she sang backing vocals for the \"Evita\" soundtrack album.  Ian La Frenais and Dick Clement wrote the short-lived 1993 TV series \"Over the Rainbow\" for her.  She also wrote all the music for \"Over the Rainbow\".\n\nAndrew Strong: Andrew Strong (born 14 November 1973) is an Irish singer and the son of Irish musician and singing coach Robert (Rob) Strong.  He grew up in Omagh, County Tyrone (where his father lived while performing with showbands), and Naas, County Kildare.  He starred as Deco Cuffe in the 1991 cult film \"The Commitments\" based on the book by Roddy Doyle, having been cast at only 16 years of age with a voice sounding much older.  In 1991 he was nominated for a Grammy Award as a member of The Commitments.\n\nQuestion: Andrew Strong starred in which film directed by Alan Parker?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"director_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the film's director.\"\n    },\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor who starred in the film.\"\n    },\n    \"actor_role\": {\n      \"type\": \"string\",\n      \"description\": \"The character role played by the actor in the film.\"\n    },\n    \"film_release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"director_name\",\n    \"actor_name\",\n    \"actor_role\",\n    \"film_release_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "director_name": {
        "type": "string",
        "description": "The name of the film's director."
      },
      "actor_name": {
        "type": "string",
        "description": "The name of the actor who starred in the film."
      },
      "actor_role": {
        "type": "string",
        "description": "The character role played by the actor in the film."
      },
      "film_release_year": {
        "type": "integer",
        "description": "The release year of the film."
      }
    },
    "required": [
      "film_title",
      "director_name",
      "actor_name",
      "actor_role",
      "film_release_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
