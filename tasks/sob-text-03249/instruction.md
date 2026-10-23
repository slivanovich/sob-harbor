{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nTumbleweed Connection (musical): Tumbleweed Connection is a musical that tells a story largely made up by the songs contained on Elton John's Tumbleweed Connection album.  The musical opened to the public on October 19th, 2007 at the Clark Center of Performing Arts in Arroyo Grande, California.  Incorporating dance, songs written by Elton John and Bernie Taupin, and original dialog by playwright Christopher Kahn, Tumbleweed Connection is set at the dawn of the twentieth century.  The play centers on two brothers, a family secret, and the pressures of the era, including looming war.  Original choreography by Suzy Miller, continuing the story line and character development through the dances.\n\nJerry Layne: Jerry Blake Layne (born September 28, 1958) is an umpire in Major League Baseball who has worked in the National League between 1989 and 1999, and throughout both major leagues since 2000.  He wore uniform number 24 in the NL, but when MLB merged the AL and NL umpiring staffs in 2000, Layne was forced to switch to number 26, as AL umpire Al Clark, who wore 24 in the junior circuit, had more seniority.  When Clark was fired midway through the 2001 season by MLB, Layne reclaimed number 24 and has worn it ever since.\n\nChopper (film): Chopper is a 2000 Australian crime drama film written and directed by Andrew Dominik and based on the autobiographical books by Mark \"Chopper\" Read.  The film stars Eric Bana as the title character and co-stars Vince Colosimo, Simon Lyndon, Kate Beahan and David Field.  It has a cult following.\n\nAl Clark (American football): Al Clark (February 29, 1948 – June 4, 2004) was an American football defensive back who played six seasons in the National Football League with the Detroit Lions, Los Angeles Rams and Philadelphia Eagles.  He was drafted by the Detroit Lions in the third round of the 1971 NFL Draft.  He first enrolled at Grambling State University before transferring to Northern Arizona University and lastly Eastern Michigan University.  Clark attended Greenville Park High School in Hammond, Louisiana.\n\nAl Clark (Blackwater): Al Clark, along with Erik Prince, was the founder of the private security firm Blackwater.\n\nThe Book of Revelation (film): The Book of Revelation is a 2006 Australian film directed by Ana Kokkinos, which she adapted with Andrew Bovell to screen from the novel by Rupert Thomson.  It was produced by Al Clark, with original music by Cezary Skubiszewski.  The movie was unique for its detailed visuals of a non statutory female on male rape.\n\nVirgin Films: Virgin Films was a film production company of the early 1980s best known for making \"1984\" (1984).  It was part of the Virgin Group and was headed by Al Clark.  Nik Powell worked for the company before going over to Palace Films.\n\nAl Clark (producer): Al Clark is an Australian film producer known for his work on \"The Adventures of Priscilla, Queen of the Desert\" and \"Chopper\".\n\nAl Clark (film editor): Al Clark was a prolific editor whose career spanned four decades, most of which was spent at Columbia Pictures.  He was nominated for 5 Academy Awards and 1 Emmy during his career.  He is credited with editing over 120 films, and towards the end of his career, in the 1960s, he also edited several television series.\n\nViola Lawrence: Viola Mallory Lawrence (December 2, 1894, New York City – November 20, 1973) is considered by many to be the first woman film editor in Hollywood.  She was nominated twice for the Academy Award for Best Film Editing: for \"Pal Joey\" (1957), with Jerome Thoms; and for \"Pepe\" (1960), with Al Clark.\n\nQuestion: What is Al Clark connection to Chopper?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person whose connection is being described.\"\n    },\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film in question.\"\n    },\n    \"connection_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"role\": {\n          \"type\": \"string\",\n          \"description\": \"The specific role or connection the person has to the film.\"\n        },\n        \"film_genre\": {\n          \"type\": \"string\",\n          \"description\": \"The genre of the film.\"\n        },\n        \"film_release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the film.\"\n        }\n      },\n      \"required\": [\n        \"role\",\n        \"film_genre\",\n        \"film_release_year\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"film_title\",\n    \"connection_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the person whose connection is being described."
      },
      "film_title": {
        "type": "string",
        "description": "The title of the film in question."
      },
      "connection_details": {
        "type": "object",
        "properties": {
          "role": {
            "type": "string",
            "description": "The specific role or connection the person has to the film."
          },
          "film_genre": {
            "type": "string",
            "description": "The genre of the film."
          },
          "film_release_year": {
            "type": "integer",
            "description": "The release year of the film."
          }
        },
        "required": [
          "role",
          "film_genre",
          "film_release_year"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "person_name",
      "film_title",
      "connection_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
