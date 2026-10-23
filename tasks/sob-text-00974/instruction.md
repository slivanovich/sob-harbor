{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nIce Quake (film): Ice Quake is a 2010 television action film written by David Ray and directed by Paul Ziller and shown on the Syfy channel.  It stars a reputable cast including Brendan Fehr, Holly Dignard, Jodelle Ferland, Ryan Grantham and Rob LaBelle.\n\nThe Cabin in the Woods: The Cabin in the Woods is a 2012 American horror comedy film directed by Drew Goddard in his directorial debut, produced by Joss Whedon, and written by Whedon and Goddard.  The film stars Kristen Connolly, Chris Hemsworth, Anna Hutchison, Fran Kranz, Jesse Williams, Richard Jenkins, and Bradley Whitford.  The plot follows a group of college students who retreat to a remote forest cabin where they fall victim to backwoods zombies and the two technicians who manipulate the ongoing events from an underground facility.\n\nJodelle Ferland: Jodelle Micah Ferland (born October 9, 1994) is a Canadian actress.  She is known for her portrayals of Mary Jensen in the 2004 ABC television series \"Kingdom Hospital\", Bree Tanner in the 2010 film \"\", and Five in the 2015 Syfy television series \"Dark Matter\".  She is also known by her roles in multiple horror or horror-related films, such as Sharon/Alessa in \"Silent Hill\", Lillith Sullivan in \"Case 39\", Jenny in \"The Tall Man\", Patience Buckner in \"The Cabin in the Woods\", and Agatha Prenderghast in \"ParaNorman\".\n\nCase 39: Case 39 is a 2009 American supernatural psychological horror film directed by Christian Alvart, and starring Renée Zellweger, Jodelle Ferland, Bradley Cooper and Ian McShane.\n\nParaNorman: ParaNorman is a 2012 American 3D stop-motion animated comedy horror film produced by Laika, distributed by Focus Features and was released on August 17, 2012.  It stars the voices of Kodi Smit-McPhee, Tucker Albrizzi, Anna Kendrick, Casey Affleck, Christopher Mintz-Plasse, Leslie Mann, Jeff Garlin, Elaine Stritch, Bernard Hill, Jodelle Ferland, Tempestt Bledsoe, Alex Borstein and John Goodman.  It is the first stop-motion film to use a 3D color printer to create character faces and only the second to be shot in 3D.  The film mainly received positive reviews and was a modest box office success, earning $107 million against its budget of $60 million.  The film received nominations for the 2012 Academy Award for Best Animated Feature and BAFTA Award for Best Animated Film.\n\nSilent Hill (film): Silent Hill is a 2006 horror film directed by Christophe Gans and written by Roger Avary, Gans, and Nicolas Boukhrief.  The film is an adaptation of Konami's video game series \"Silent Hill\".  It stars Radha Mitchell, Sean Bean, Laurie Holden, Deborah Kara Unger, Kim Coates, Tanya Allen, Alice Krige, and Jodelle Ferland.\n\n400 Boys: 400 Boys is a Canadian/Chinese action-fantasy thriller film directed, written and produced by Alastair Paton and starring Jodelle Ferland, Li Bingbing, Maria Valverde and Charlie Rowe.\n\nHome Alone: The Holiday Heist: Home Alone: The Holiday Heist (also known as Home Alone 5 or Home Alone 5: The Holiday Heist ) is a 2012 American comedy television film and the fifth installment in the \"Home Alone\" franchise.  It stars Christian Martyn, Jodelle Ferland, Malcolm McDowell, Debi Mazar, Eddie Steeples.  The film premiered on ABC Family on November 25, 2012, during the network's annual \"Countdown to 25 Days of Christmas\" programming block.  It is the second film, after \"Home Alone 3\", not to focus on the McCallister family.  It is also the first film in the series not to be set in Chicago, apart from the majority of \"\".  There are numerous homages to the previous movies throughout the film.\n\nWonderful World (2009 film): Wonderful World is a 2009 dark comedy-drama film directed and written by Joshua Goldin, who in this movie makes his directorial debut.  The film stars Matthew Broderick, Sanaa Lathan, Michael K. Williams and Jodelle Ferland.\n\nPictures of Hollis Woods (film): Pictures of Hollis Woods is a film that debuted on CBS as a \"Hallmark Hall of Fame\" film on December 2, 2007.  The film is directed by Tony Bill and is based on the Newbery Honor winning novel of the same name by Patricia Reilly Giff.  It stars child actress Jodelle Ferland as the title character along with Sissy Spacek.\n\nQuestion: Jodelle Ferland had a role in which 2012 American Horror film directed by Drew Goddard? \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the film was released.\"\n    },\n    \"director\": {\n      \"type\": \"string\",\n      \"description\": \"The director of the film.\"\n    },\n    \"genres\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of genres the film belongs to.\"\n    },\n    \"jodelle_ferland_in_cast\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if Jodelle Ferland had a role in the film.\"\n    },\n    \"notable_cast_members\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of other notable cast members in the film.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"director\",\n    \"genres\",\n    \"jodelle_ferland_in_cast\",\n    \"notable_cast_members\"\n  ],\n  \"additionalProperties\": false\n}"
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
      "director": {
        "type": "string",
        "description": "The director of the film."
      },
      "genres": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of genres the film belongs to."
      },
      "jodelle_ferland_in_cast": {
        "type": "boolean",
        "description": "Indicates if Jodelle Ferland had a role in the film."
      },
      "notable_cast_members": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of other notable cast members in the film."
      }
    },
    "required": [
      "film_title",
      "release_year",
      "director",
      "genres",
      "jodelle_ferland_in_cast",
      "notable_cast_members"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
