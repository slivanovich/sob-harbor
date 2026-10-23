{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Stanford Prison Experiment (film): The Stanford Prison Experiment is a 2015 American thriller film directed by Kyle Patrick Alvarez and written by Tim Talbott.  The film stars Billy Crudup, Michael Angarano, Ezra Miller, Tye Sheridan, Keir Gilchrist, Olivia Thirlby, and Nelsan Ellis.  The plot tells the story of the 1971 Stanford prison experiment conducted at Stanford University under supervision of psychology professor Philip Zimbardo in which students play the role of a prisoner or a prison guard.\n\nDas Experiment: Das Experiment (English: The Experiment) is a 2001 German thriller film directed by Oliver Hirschbiegel.  It is based on Mario Giordano's novel \"Black Box\" and deals with a social experiment which resembles Philip Zimbardo's Stanford prison experiment of 1971.\n\nC.O.G.: C.O.G. is an American comedy-drama film directed and written by Kyle Patrick Alvarez, and starring Jonathan Groff.  The film is based on a David Sedaris short story from his book of collected essays, \"Naked\".  It marks the first time one of Sedaris' stories has been adapted for film.  It co-stars Denis O'Hare, Casey Wilson, Dean Stockwell, Troian Bellisario, and Corey Stoll.\n\nEasier with Practice: Easier with Practice is a 2009 American drama film written and directed by Kyle Patrick Alvarez.  It stars Brian Geraghty, Kel O'Neill, Marguerite Moreau, Jeanette Brox, Jenna Gavigan and Katie Aselton.  The story is based on a 2006 GQ Article written by Davy Rothbart.\n\nTye Sheridan: Tye Kayle Sheridan (born November 11, 1996) is an American actor.  Sheridan made his feature film debut in Terrence Malick's experimental drama film \"The Tree of Life\" (2011) and had his first leading role in Jeff Nichols's film \"Mud\" (2012).  He also co-starred in David Gordon Green's drama \"Joe\" (2013).  In 2015, he starred in the drama \"The Stanford Prison Experiment\".  Sheridan played Cyclops in the 2016 film \"\", and will portray the lead character, Wade Watts, in Steven Spielberg's adaptation of Ernest Cline's \"Ready Player One\", which is scheduled for a March 30, 2018 release. .  He will also be reprising his role as Cyclops in the upcoming film \"\".\n\nBlackway: Blackway (also known as Go With Me) is a 2015 American thriller film directed by Daniel Alfredson and written by Joseph Gangemi and Gregory Jacobs, based on the 2008 novel \"Go with Me\" by Castle Freeman, Jr. The film stars Anthony Hopkins, Julia Stiles, Ray Liotta, and Alexander Ludwig.  Filming began on November 12, 2014, in Enderby, British Columbia.  Although screened as \"Go with Me\" at the Venice Film Festival in 2015, it was not released for public viewing in the U.S. until 10 June 2016.\n\nThe Experiment (2010 film): The Experiment is a 2010 American drama thriller film directed by Paul T. Scheuring and starring Adrien Brody, Forest Whitaker, Cam Gigandet, Clifton Collins, Jr., and Maggie Grace, about an experiment which resembles Philip Zimbardo's Stanford prison experiment in 1971.\n\nStanford Prison Experiment (band): Stanford Prison Experiment was an American punk band based in Los Angeles, California, whose name was a reference to the Stanford prison experiment conducted by psychologist Philip Zimbardo in 1971.  The band represented various subgenres such as hardcore, post-hardcore, and grunge.  Its leader learned about the SPE as an employee for the audio/visual dept at UCLA (He set up/played the film for a class).\n\nChristina Maslach: Christina Maslach (born January 21, 1946) is an American social psychologist and professor of psychology at the University of California, Berkeley, known for her research on occupational burnout.  When she was in graduate school, Maslach was instrumental in stopping the Stanford prison experiment.\n\nEzra Miller: Ezra Matthew Miller (born September 30, 1992) is an American actor and singer.  He made his feature film debut in the film \"Afterschool\" (2008).  He starred as the title character in the drama \"We Need to Talk About Kevin\" (2011) and co-starred in the film adaptation of \"The Perks of Being a Wallflower\" (2012).  In 2015, he co-starred in the drama \"The Stanford Prison Experiment\" and in the comedy \"Trainwreck\".  He plays Barry Allen / The Flash in the DC Extended Universe where he first appeared as Flash in \"\" (2016) and also played Credence Barebone in \"Fantastic Beasts and Where to Find Them\" (2016).\n\nQuestion: The Stanford Prison Experiment is a 2015 American thriller film directed by Kyle Patrick Alvarez, the  film stars which American actor and singer, born on September 30, 1992?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"film_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"film_director\": {\n      \"type\": \"string\",\n      \"description\": \"The director of the film.\"\n    },\n    \"actor_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"actor_name\": {\n          \"type\": \"string\",\n          \"description\": \"The full name of the actor.\"\n        },\n        \"birth_date\": {\n          \"type\": \"string\",\n          \"format\": \"date\",\n          \"description\": \"The birth date of the actor in YYYY-MM-DD format.\"\n        },\n        \"nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the actor.\"\n        },\n        \"professions\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"A list of professions for the actor.\"\n        }\n      },\n      \"required\": [\n        \"actor_name\",\n        \"birth_date\",\n        \"nationality\",\n        \"professions\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"film_year\",\n    \"film_director\",\n    \"actor_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "film_year": {
        "type": "integer",
        "description": "The release year of the film."
      },
      "film_director": {
        "type": "string",
        "description": "The director of the film."
      },
      "actor_details": {
        "type": "object",
        "properties": {
          "actor_name": {
            "type": "string",
            "description": "The full name of the actor."
          },
          "birth_date": {
            "type": "string",
            "format": "date",
            "description": "The birth date of the actor in YYYY-MM-DD format."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the actor."
          },
          "professions": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of professions for the actor."
          }
        },
        "required": [
          "actor_name",
          "birth_date",
          "nationality",
          "professions"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_title",
      "film_year",
      "film_director",
      "actor_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
