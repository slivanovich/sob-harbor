{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Fourth Protocol (film): The Fourth Protocol is a 1987 British Cold War spy film featuring Michael Caine and Pierce Brosnan, based on the novel \"The Fourth Protocol\" by Frederick Forsyth.\n\nNicholas Young (actor): He was trained at the Corona Stage School London and made his professional debut in 1964 playing a lead in the film \"Eagle Rock\".  He made numerous television appearances during the 1960s including featured roles in individual dramas and in series such as \"Front Page Story\", \"Kate\" and \"The Flying Swan\" as well as film roles in \"The Haunted House of Horror\" (1969), \"The Day Of The Jackal\" (1973), \"Three for All\" (1975), \"Eskimo Nell\" (1975), \"It Could Happen to You\" (1975), \"Adventures of a Private Eye\" (1977), \"Home Before Midnight\" (1979) and \"S.O.S. Titanic\" (1979).  His stage work included playing at the Traverse Theatre Edinburgh in 1966 and a leading role in the West End production of Alan Bennett's \"40 Years On\".\n\nAugust 1 (film): August 1 is a 1988 Malayalam film directed by Sibi Malayil, written by S. N. Swamy, and starring Mammootty, Sukumaran, Captain Raju and Urvashi.  The film was produced and distributed by M. Mani under the banner of Sunitha Productions.  \"August 1\" is loosely based on the 1971 British novel \"The Day of the Jackal\" by Frederick Forsyth.\n\nLove Never Dies (musical): Love Never Dies is a romantic musical composed by Andrew Lloyd Webber with lyrics by Glenn Slater and a book by Lloyd Webber, Ben Elton, Frederick Forsyth and Slater.  It is a sequel to the long-running musical \"The Phantom of the Opera\" loosely adapted from the 1999 novel \"The Phantom of Manhattan\", by Forsyth.\n\nThe Cobra (novel): The Cobra is a 2010 thriller novel by Frederick Forsyth about the international cocaine trade.  In it an unnamed Obama-like (said to have a wife named 'Michelle' and a deceased Kenyan father) U.S. president colludes with an unnamed Cameron-like (having a wife named 'Sam') U.K. Prime Minister to put an end to the international cocaine trade and brings in ex-CIA director Paul Devereaux who is basically given carte blanche to accomplish this task by any means necessary.  The book re-introduces some of the characters from Forsyth's book \"Avenger\".\n\nAvenger (film): Avenger is a 2006 television film starring Sam Elliott and Timothy Hutton, based on the novel \"Avenger\" by Frederick Forsyth.\n\nThe Devil's Alternative: The Devil's Alternative is a novel by British writer Frederick Forsyth first published in 1979.  It was his fourth full-length novel and marked a new direction in his work, setting the story in the near-future (in 1982) rather than in the recent past.  The work evolved from an unfilmed screenplay entitled \"No Alternative\".\n\nThe Day of the Jackal (film): The Day of the Jackal is a 1973 Anglo-French political thriller film directed by Fred Zinnemann and starring Edward Fox and Michel Lonsdale.  Based on the 1971 novel \"The Day of the Jackal\" by Frederick Forsyth, the film is about a professional assassin known only as the \"Jackal\" who is hired to assassinate French president Charles de Gaulle in the summer of 1963.\n\nIcon (film): Icon (or \"Frederick Forsyth's Icon\") is a 2005 made-for-television thriller film directed by Charles Martin Smith and very loosely based on the novel by Frederick Forsyth.  The film premiered on Hallmark Channel May 30, 2005.  It is set in the period 1985 to 1999.\n\nThe Dogs of War (film): The Dogs of War is a 1980 war film based upon the 1974 novel of the same name by Frederick Forsyth.  Largely filmed in Belize, it was directed by John Irvin and starred Christopher Walken and Tom Berenger.  In it a small mercenary unit of soldiers is privately hired to depose the president of a fictional African country so that a British tycoon can gain access to a platinum deposit.\n\nQuestion: What film based off a novel by Frederick Forsyth did Nicholas Young star in?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor who starred in the film.\"\n    },\n    \"source_novel\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the novel the film is based on.\"\n        },\n        \"author\": {\n          \"type\": \"string\",\n          \"description\": \"The author of the source novel.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"author\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"film_release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the film was released.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"actor_name\",\n    \"source_novel\",\n    \"film_release_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "actor_name": {
        "type": "string",
        "description": "The name of the actor who starred in the film."
      },
      "source_novel": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the novel the film is based on."
          },
          "author": {
            "type": "string",
            "description": "The author of the source novel."
          }
        },
        "required": [
          "title",
          "author"
        ],
        "additionalProperties": false
      },
      "film_release_year": {
        "type": "integer",
        "description": "The year the film was released."
      }
    },
    "required": [
      "film_title",
      "actor_name",
      "source_novel",
      "film_release_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
