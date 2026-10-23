{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGosford Park: Gosford Park is a 2001 British mystery film directed by Robert Altman and written by Julian Fellowes.  The film stars an ensemble cast, which includes Eileen Atkins, Bob Balaban, Alan Bates, Charles Dance, Stephen Fry, Michael Gambon, Richard E. Grant, Derek Jacobi, Kelly Macdonald, Helen Mirren, Jeremy Northam, Clive Owen, Ryan Phillippe, Maggie Smith, Kristin Scott Thomas, and Emily Watson.  The story follows a party of wealthy Britons and an American, and their servants, who gather for a shooting weekend at Gosford Park, an English country house.  A murder occurs after a dinner party, and the film goes on to present the subsequent investigation from the servants' and guests' perspectives.\n\nOne Life to Live storylines (1990–99): \"One Life to Live\" is an American soap opera that has been broadcast on the ABC network since 1968.  The series starts with \"One Life to Live\" storylines (1968–1979).  The plot continues in \"One Life to Live\" storylines (1980–1989).  The plot in the next decade is outlined in \"One Life to Live\" storylines (1990–1999) and the story concludes in \"One Life to Live\" storylines (2000—2012).\n\nOne Life to Live storylines (1980–89): \"One Life to Live\" is an American soap opera that has been broadcast on the ABC network since 1968.  The series starts with \"One Life to Live\" storylines (1968–1979).  The plot continues in \"One Life to Live\" storylines (1980–1989).  The plot in the next decade is outlined in \"One Life to Live\" storylines (1990–1999) and the story concludes in \"One Life to Live\" storylines (2000—2012).\n\nIndependent Spirit Robert Altman Award: The Independent Spirit Robert Altman Award is presented to the ensemble cast, director and casting director of a film by the Film Independent, a non-profit organization dedicated to independent film and independent filmmakers.  It is named after director, screenwriter, and producer Robert Altman, who is considered a \"maverick\" in naturalistic films.\n\nSuicide Is Painless: \"Song from M*A*S*H (Suicide Is Painless)\" is a song written by Johnny Mandel (music) and Mike Altman (lyrics), which was the theme song for both the movie and TV series \"M*A*S*H\".  Mike Altman is the son of the original film’s director, Robert Altman, and was 14 years old when he wrote the song’s lyrics.  During an appearance on \"The Tonight Show Starring Johnny Carson\" in the 1980s, Robert Altman said that while he only made $70,000 for having directed the movie, his son had earned more than $1 million for having co-written the song.\n\nOne Life to Live storylines (1968–79): \"One Life to Live\" is an American soap opera that has been broadcast on the ABC network since 1968.  The series starts with \"One Life to Live\" storylines (1968–1979).  The plot continues in \"One Life to Live\" storylines (1980–1989).  The plot in the next decade is outlined in \"One Life to Live\" storylines (1990–1999) and the story concludes in \"One Life to Live\" storylines (2000—2012).\n\nThe Late Show (film): The Late Show is a 1977 American neo-noir mystery film written and directed by Robert Benton and produced by Robert Altman.  It stars Art Carney, Lily Tomlin, Bill Macy, Eugene Roche, and Joanna Cassidy.\n\nOne Life to Live storylines (2000–13): \"One Life to Live\" was an American soap opera that was broadcast on the ABC network from 1968-2013, and online from April–August 2013.  The series starts with \"One Life to Live\" storylines (1968–79).  The plot continues in \"One Life to Live\" storylines (1980–89).  The plot in the next decade is outlined in \"One Life to Live\" storylines (1990–99) and the story concludes in \"One Life to Live\" storylines (2000–13).\n\nA Wedding (opera): A Wedding is a comic opera based on Robert Altman's 1978 film \"A Wedding\" and was composed by William Bolcom with a libretto written by Robert Altman and Arnold Weinstein.\n\nRyan Phillippe: Matthew Ryan Phillippe ( ; born September 10, 1974) is an American actor, director, and writer.  After appearing as Billy Douglas on the soap opera \"One Life to Live\", he came to fame in the late 1990s with starring roles in a string of films, including \"I Know What You Did Last Summer\", \"Cruel Intentions\", and \"54\".  In the 2000s, he appeared in several films, including \"Gosford Park\" (2001), \"Crash\" (2004), and war drama \"Flags of Our Fathers\" (2006), \"Breach\" (2007), and \"Stop-Loss\" (2008).  In 2010, Phillippe starred as Pulitzer Prize-winning photographer Greg Marinovich in \"The Bang-Bang Club\".  He stars in the lead role of Bob Lee Swagger in the USA Network thriller drama \"Shooter\".\n\nQuestion: What mystery film by Robert Altman included a performance by a \"One Life To Live\" star?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the mystery film directed by Robert Altman.\"\n    },\n    \"director_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the film's director.\"\n    },\n    \"film_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the film.\"\n    },\n    \"actor_from_soap_opera\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"actor_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the actor who appeared in both the film and the soap opera.\"\n        },\n        \"soap_opera_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the soap opera the actor was in.\"\n        },\n        \"film_appearance_confirmed\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the actor's appearance in the film is confirmed by the context.\"\n        }\n      },\n      \"required\": [\n        \"actor_name\",\n        \"soap_opera_title\",\n        \"film_appearance_confirmed\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"director_name\",\n    \"film_genre\",\n    \"actor_from_soap_opera\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the mystery film directed by Robert Altman."
      },
      "director_name": {
        "type": "string",
        "description": "The name of the film's director."
      },
      "film_genre": {
        "type": "string",
        "description": "The genre of the film."
      },
      "actor_from_soap_opera": {
        "type": "object",
        "properties": {
          "actor_name": {
            "type": "string",
            "description": "The name of the actor who appeared in both the film and the soap opera."
          },
          "soap_opera_title": {
            "type": "string",
            "description": "The title of the soap opera the actor was in."
          },
          "film_appearance_confirmed": {
            "type": "boolean",
            "description": "Indicates if the actor's appearance in the film is confirmed by the context."
          }
        },
        "required": [
          "actor_name",
          "soap_opera_title",
          "film_appearance_confirmed"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_title",
      "director_name",
      "film_genre",
      "actor_from_soap_opera"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
