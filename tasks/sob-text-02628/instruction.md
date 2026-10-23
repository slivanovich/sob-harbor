{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nIt's Pat: It's Pat is a 1994 American comedy film directed by Adam Bernstein and starring Julia Sweeney, Dave Foley, Charles Rocket, and Kathy Griffin.  The film was based on the \"Saturday Night Live\" (SNL) character Pat, created by Sweeney, an androgynous misfit whose gender is never revealed.\n\nLet's Kill Ward's Wife: Let's Kill Ward's Wife is a 2014 American black comedy film written and directed by Scott Foley.  Marking Foley's feature-film directorial debut, the film stars Patrick Wilson, Foley, Donald Faison, and James Carpinello.  Foley, Wilson, and Carpinello produced the film, along with Joe Hardesty.  The film follows three friends (Wilson, Foley, and Carpinello) who plan to kill their friend Ward's (Faison) abusive wife, Stacy (Dagmara Domińczyk).\n\nHot Fuzz: Hot Fuzz is a 2007 action comedy film directed by Edgar Wright, written by Wright and Simon Pegg, and starring Pegg and Nick Frost.  The three and the film's producer Nira Park had previously worked together on the television series \"Spaced\" and the 2004 film \"Shaun of the Dead\".  The film follows two police officers attempting to solve a series of mysterious deaths in an English village.\n\nBlast from the Past (film): Blast from the Past is a 1999 American romantic comedy film based on a story and directed by Hugh Wilson, and starring Brendan Fraser, Alicia Silverstone, Christopher Walken, Sissy Spacek and Dave Foley.\n\nPostal (film): Postal is a 2007 action comedy film co-written and directed by Uwe Boll.  The film stars Zack Ward, Dave Foley, Chris Coppola, Jackie Tohn, J.K. Simmons, Verne Troyer, Larry Thomas, David Huddleston, and Seymour Cassel.\n\nLet's Be Cops: Let's Be Cops is a 2014 American action comedy film co-written and directed by Luke Greenfield.  The film stars Jake Johnson and Damon Wayans, Jr. as two friends who pretend to be Los Angeles police officers.  Co-starring Nina Dobrev, Rob Riggle, James D'Arcy and Keegan-Michael Key, the film was released on August 13, 2014.\n\nA Bug's Life: A Bug's Life is a 1998 American computer-animated adventure comedy film produced by Pixar Animation Studios for Walt Disney Pictures.  Directed by John Lasseter, the film involves a misfit ant named Flik that is looking for \"tough warriors\" to save his colony from greedy grasshoppers, only to recruit a group of bugs that turn out to be an inept circus troupe.  The film stars the voices of Dave Foley, Kevin Spacey and Julia Louis-Dreyfus.\n\nDave Foley: David Scott \"Dave\" Foley (born January 4, 1963) is a Canadian actor, stand-up comedian, director, producer and writer.  He is known as a co-founder of the comedy group \"The Kids in the Hall\", responsible for their eponymous sketch show and the feature-length film \"\".  He played Dave Nelson in the sitcom \"NewsRadio\", voiced Flik in \"A Bug's Life\" and hosted the game show \"Celebrity Poker Showdown\".\n\nThe Wrong Guy: The Wrong Guy is a 1997 Canadian comedy film directed by David Steinberg.  It was co-written by Dave Foley of \"The Kids in the Hall\" and \"Newsradio\" fame, along with David Anthony Higgins and Jay Kogen (the latter of \"The Simpsons\" writing fame).  Foley also stars in the picture, along with David Anthony Higgins, Jennifer Tilly, Colm Feore and Joe Flaherty.\n\nFreeloaders (film): Freeloaders is an American ensemble comedy film directed by Dan Rosen and written by Rosen and singer Dave Gibbs.  The film is produced by the Broken Lizard comedy troupe and is independently financed.  \"Freeloaders\" stars Clifton Collins Jr., Josh Lawson, Kevin Sussman, Zoe Boyle, Nat Faxon, Warren Hutcherson, Jane Seymour, Olivia Munn, Dave Foley and Counting Crows lead singer Adam Duritz.  It follows a group of friends who find their luxurious lifestyle threatened when the rock star they freeload off decides to sell his home.\n\nQuestion: Postal is a 2007 action comedy film co-written and directed by who, the film stars includes Dave Foley?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the film was released.\"\n    },\n    \"genre\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"The genres of the film.\"\n    },\n    \"director\": {\n      \"type\": \"string\",\n      \"description\": \"The director of the film.\"\n    },\n    \"is_dave_foley_in_cast\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if Dave Foley is listed in the film's cast.\"\n    },\n    \"other_cast_members\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Other notable cast members of the film.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"genre\",\n    \"director\",\n    \"is_dave_foley_in_cast\",\n    \"other_cast_members\"\n  ],\n  \"additionalProperties\": false\n}"
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
        "description": "The year the film was released."
      },
      "genre": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "The genres of the film."
      },
      "director": {
        "type": "string",
        "description": "The director of the film."
      },
      "is_dave_foley_in_cast": {
        "type": "boolean",
        "description": "Indicates if Dave Foley is listed in the film's cast."
      },
      "other_cast_members": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Other notable cast members of the film."
      }
    },
    "required": [
      "film_title",
      "release_year",
      "genre",
      "director",
      "is_dave_foley_in_cast",
      "other_cast_members"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
