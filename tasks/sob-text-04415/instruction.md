{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nTonight and Every Night: Tonight and Every Night is a 1945 American musical film directed by Victor Saville and starring Rita Hayworth, Lee Bowman and Janet Blair.  The film portrays wartime romance and tragedy in a London musical show, loosely modelled on the Windmill Theatre in Soho, that determined not to miss a single performance during the Blitz.  Hayworth plays an American showgirl who falls in love with an RAF pilot played by Bowman.\n\nWartime Romance: Wartime Romance (Russian: Военно-полевой роман , translit.  Voenno-polevoy roman) is a 1983 Soviet film directed by Pyotr Todorovsky.  It tells the story of a soldier and a nurse separated by World War II and briefly reunited in 1950.\n\nMy Reputation: My Reputation is a 1946 film, directed by Curtis Bernhardt, about a wartime love story.  Barbara Stanwyck portrayed Jessica Drummond, an upper-class widow from Chicago who innocently falls in love with an army officer (George Brent), much to the consternation of her gossipy friends and domineering mother (Lucile Watson).  Her romance also pits her against her two teenage sons (Scotty Beckett and Bobby Cooper).  Screenwriter and novelist Catherine Turney wrote the script, which she adapted from Clare Jaynes' 1942 novel \"Instruct My Sorrows\".  Barbara Stanwyck's costumes were designed by Edith Head.\n\nNatalya Andrejchenko: Natalya Eduardovna Andrejchenko, Honored Artist of the RSFSR (1984) (Russian: Ната́лья Эдуа́рдовна Андре́йченко ; born May 3, 1956) is an actress.  Her most famous roles include the title character in \"Mary Poppins, Goodbye\" and Lyuba in \"Wartime Romance\".\n\nFor the Moment (film): For the Moment is a 1993 film written and directed by Aaron Kim Johnston and starring Russell Crowe and Christianne Hirt.  The plot revolves around airmen training in rural Manitoba, Canada, with the British Commonwealth Air Training Plan during the Second World War.  The main focus of the story is the wartime romance between Russell Crowe's character and a local girl.  Johnston was inspired to write the screenplay based upon the stories of his father who was an instructor and bomber pilot in the war, and his mother's experiences as a young woman on the home front.\n\nTortilla Soup: Tortilla Soup is a 2001 American comedy-drama film directed by María Ripoll.  The screenplay by Tom Musca, Ramón Menéndez and Vera Blasi is based on the film \"Eat Drink Man Woman\", which was written by Hui-Ling Wang, Ang Lee, and James Schamus.\n\nThe Crossing (2014 film): The Crossing (Chinese: 太平轮) is a 2014 Chinese-Hong Kong epic historical romance-war drama (part 1) and disaster film (part 2) directed by John Woo and written by Hui-Ling Wang.  The film stars Zhang Ziyi, Takeshi Kaneshiro, Song Hye-kyo, Huang Xiaoming, Tong Dawei and Masami Nagasawa.  The film is based on the sinking of the steamer \"Taiping\" in 1949.  The incident led to the deaths of over 1,500 passengers and crew.  The film's first part was released in China on December 2, 2014.  Part two was released on July 30, 2015.\n\nApril Rhapsody: April Rhapsody is a 2000 TV series written by Wang Hui-ling, based on the romantic life of Xu Zhimo, one of China's most renowned poets in the 20th century.\n\nThe Legend of Eileen Chang: The Legend of Eileen Chang is a 2004 biographical drama TV series written by Wang Hui-ling and produced by Hsu Li-kong, starring Rene Liu as Eileen Chang, one of China's greatest authors in the 20th century.\n\nWang Hui-ling: Hui-Ling Wang or Wang Hui-Ling is a Taiwanese screenwriter.  In 2001 she was nominated for Academy Award for Best Writing for the Crouching Tiger, Hidden Dragon.  In 2013 she wrote the script for The Crossing directed by John Woo, scheduled to be released in 2014.\n\nQuestion: Wang Hui-ling wrote the script for the epic wartime romance The Crossing. Who directed?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"movie_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"director\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the director.\"\n        }\n      },\n      \"required\": [\n        \"name\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"screenwriter\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the screenwriter.\"\n        }\n      },\n      \"required\": [\n        \"name\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the first part of the film.\"\n    },\n    \"genres\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of genres associated with the film.\"\n    }\n  },\n  \"required\": [\n    \"movie_title\",\n    \"director\",\n    \"screenwriter\",\n    \"release_year\",\n    \"genres\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "movie_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "director": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the director."
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      },
      "screenwriter": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the screenwriter."
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      },
      "release_year": {
        "type": "integer",
        "description": "The release year of the first part of the film."
      },
      "genres": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of genres associated with the film."
      }
    },
    "required": [
      "movie_title",
      "director",
      "screenwriter",
      "release_year",
      "genres"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
