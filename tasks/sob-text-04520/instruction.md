{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nTim David Kelly: Tim David Kelly is an American musician, songwriter, record producer, composer & owner of the music library http://www.ultradosemusic.com.  He is the singer, guitarist and songwriter for the alternative rock band Kicking Harold whose still popular song \"Gasoline\" from \"Space Age Breakdown\" was featured as the main theme for five seasons on TLC's automobile make-over show, \"Overhaulin'\".  Kelly has written many songs for others, including co-writing \"Money For That\" for the band Shiny Toy Guns.  He has produced several albums, including co-producing \"Lightning Strikes Again\" by Dokken.  Kelly has composed main themes and music cues used in television and film including \"Gene Simmons Family Jewels\" (A&E) &\n\nDavid Kelly (United States Virgin Islands sailor): David Kelly (born February 4, 1955) is a sailor from United States Virgin Islands.  Kelly represented his country at the 1972 Summer Olympics in Kiel.  Kelly took 24th place in the Soling with Dick Holmberg as helmsman and David Jones as fellow crew member.\n\nDavid Kelly Campbell: David Kelly Campbell from the Boston University, was awarded the status of Fellow in the American Physical Society, after they were nominated by their American Physical Society in 1990, for \"significant contributions in theoretical physics to quantum field theory, condensed-matter physics, computational physics, and non-linear science, and for his leadership role in the development of institutional programs in nonlinear science both at Los Alamos and internationally.\"\n\nAlastair Campbell: Alastair John Campbell (born 25 May 1957) is a British journalist, broadcaster, political aide and author, best known for his work as Tony Blair's spokesman and campaign director (1994–1997), followed by Downing Street Press Secretary (1997–2000), for Labour Prime Minister Tony Blair.  He then became Director of Communications and spokesman for the Labour Party (2000–2003).  He resigned in August 2003 during the Hutton Inquiry into the death of David Kelly.  He published his twelfth book in 2016.  He is editor at large of The New European and chief interviewer for GQ magazine.  He continues to act as a consultant strategist and as an ambassador for Time To Change and other mental health charities.\n\nWaking Ned: Waking Ned (titled Waking Ned Devine in North America) is a 1998 comedy film by English writer and director Kirk Jones.  It stars Ian Bannen, David Kelly, and Fionnula Flanagan.  Kelly was nominated for a Screen Actors' Guild award for his role as Michael O'Sullivan.  The film is set in Ireland but was filmed in the Isle of Man.  It was produced by Canal+ and the British studio Tomboy Films and distributed by the American company Fox Searchlight Pictures.\n\nMystics (film): Mystics is a 2003 film starring Milo O'Shea and David Kelly, and directed by David Blair.\n\nRon Neil: Ronald John Baillie Neil CBE (born 1941 or 1942) is a former BBC television journalist and news editor, who rose to become the BBC's overall director of news and current affairs in the late 1980s.  He retired in 1998, but was recalled in 2004 to review BBC journalism and values in response to the criticisms made by the Hutton inquiry into the circumstances surrounding the death of Dr David Kelly.\n\nStephen Kelly (footballer): Stephen Michael David Kelly (born 6 September 1983) is an Irish professional footballer who last played for Championship club Rotherham United.  He plays as a defender, primarily at right back.  He was part of the team that secured the Republic of Ireland's qualification for UEFA Euro 2012.\n\nDavid Kelly (actor): David Kelly (11 July 1929 – 12 February 2012) was an Irish actor who had regular roles in several film and television works from the 1950s onwards.  One of the most recognisable voices and faces of Irish stage and screen, Kelly was known for his roles as Rashers Tierney in \"Strumpet City\", Cousin Enda in \"Me Mammy\", the builder Mr O'Reilly in \"Fawlty Towers\", and Grandpa Joe in the film \"Charlie and the Chocolate Factory\".  Another notable role was as Michael O'Sullivan in \"Waking Ned\" .\n\nKelly Nunataks: The Kelly Nunataks ( ) are the nunataks that mark the eastern extremity of the Clark Mountains, in the Ford Ranges of Marie Byrd Land, Antarctica.  They were mapped by the United States Geological Survey from surveys and U.S. Navy air photos, 1959–65, and were named by the Advisory Committee on Antarctic Names for John David Kelly, a United States Antarctic Research Program ionospheric physicist at Byrd Station, 1968.\n\nQuestion: Who was the director of a film where  David Kelly had a role as Michael O'Sullivan?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the film.\"\n        },\n        \"director_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the director of the film.\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the film.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"director_name\",\n        \"release_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"actor_role\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"actor_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the actor.\"\n        },\n        \"role_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the role played by the actor in the film.\"\n        }\n      },\n      \"required\": [\n        \"actor_name\",\n        \"role_name\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"answer\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the director who directed the specified film.\"\n    }\n  },\n  \"required\": [\n    \"film_details\",\n    \"actor_role\",\n    \"answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the film."
          },
          "director_name": {
            "type": "string",
            "description": "The name of the director of the film."
          },
          "release_year": {
            "type": "integer",
            "description": "The release year of the film."
          }
        },
        "required": [
          "title",
          "director_name",
          "release_year"
        ],
        "additionalProperties": false
      },
      "actor_role": {
        "type": "object",
        "properties": {
          "actor_name": {
            "type": "string",
            "description": "The name of the actor."
          },
          "role_name": {
            "type": "string",
            "description": "The name of the role played by the actor in the film."
          }
        },
        "required": [
          "actor_name",
          "role_name"
        ],
        "additionalProperties": false
      },
      "answer": {
        "type": "string",
        "description": "The name of the director who directed the specified film."
      }
    },
    "required": [
      "film_details",
      "actor_role",
      "answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
