{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nOctober Sky (disambiguation): October Sky is a 1999 American biographical film directed by Joe Johnston based on the memoir by Homer Hickam, Jr.\n\nI Spit on Your Grave (2010 film): I Spit on Your Grave is a 2010 American rape-and-revenge horror film, and a remake of the controversial 1978 cult film \"Day of the Woman\" (better known by its re-release title, \"I Spit on Your Grave\").  It was directed by Steven R. Monroe, and stars Sarah Butler, Chad Lindberg, Daniel Franzese, Rodney Eastman, Jeff Branson, and Andrew Howard.\n\nA Midsummer Night's Rave: A Midsummer Night's Rave is a film adapted from Shakespeare's \"A Midsummer Night's Dream\" released in 2002.  The film stars Corey Pearson, Lauren German, Andrew Keegan, Chad Lindberg, and Sunny Mabrey; and was directed by Gil Cates Jr..  It is set at a rave rather than a forest, as in the original.  The film received little attention from professional movie critics, but is considered a success with teen audiences, and has been used as an exemplar for a category of movies (the \"McShakespeare\", an example of McDonaldization) in more academic publications.\n\nMy Big Break: My Big Break is a 2009 documentary film directed by Tony Zierra starring Wes Bentley, Tony Zierra, Brad Rowe, Chad Lindberg and Greg Fawcett.  The film was produced by MBB Group, Elizabeth Yoffe and Tony Zierra.\n\nThe Fast and the Furious (2001 film): The Fast and the Furious is a 2001 action crime film directed by Rob Cohen, produced by Neal H. Moritz and written by Gary Scott Thompson and David Ayer.  It is the first installment in \"The Fast and the Furious\" franchise.  The film stars Paul Walker, Vin Diesel, Michelle Rodriguez, Jordana Brewster, Rick Yune, Chad Lindberg, Johnny Strong, and Matt Schulze.  The film follows undercover cop Brian O'Conner, who is tasked with stopping a group of unknown hijackers using high-performance racecars to hijack 18-wheelers.  It is an international co-production between the United States and Germany.\n\nOctober Sky: October Sky is a 1999 American biographical film directed by Joe Johnston, starring Jake Gyllenhaal, Chris Cooper, Chris Owen, and Laura Dern.  It is based on the true story of Homer H. Hickam, Jr., a coal miner's son who was inspired by the launch of \"Sputnik 1\" in 1957 to take up rocketry against his father's wishes and eventually became a NASA engineer.\n\nChad Lindberg: Chad Tyler Lindberg (born November 1, 1976) is an American actor.  He is known for his film roles in \"The Fast and the Furious\" and \"October Sky\", as well as television roles on \"Sons of Anarchy\" and \"Supernatural\".  Lindberg was the co-host of the television series, \"Ghost Stalkers\".\n\nSecurity (film): Security is a 2017 American action thriller film directed by Alain Desrochers and written by Tony Mosher and John Sullivan.  The film stars Antonio Banderas, Gabriella Wright, Ben Kingsley, and Chad Lindberg.\n\nRise of the Zombies: Rise of the Zombies, also known as Dead Walking, is a 2012 American zombie horror film from The Asylum and directed by Nick Lyon.  Written by Keith Allan and Delondra Williams, the film was initially titled \"Dead Walking\", but was eventually changed to \"Rise of the Zombies\".  The film stars Mariel Hemingway, Chad Lindberg, LeVar Burton, and Heather Hemmens, and first aired on Syfy on October 27, 2012.\n\nGreg Fawcett: Greg Wendell Fawcett (born November 30, 1969 in Minneapolis, Minnesota) is an American film and television actor Producer and Screenwriter.  Attended private boarding school on the east coast and Graduated with his BA from the dramatic arts program at University of Southern California'.  He has appeared and worked alongside some of Hollywoods biggest names...was in several episodes of \"The New Adventures of Robin Hood\", \"Point Pleasant\" and \"Fashion House\", \"Sunset Beach\" as well as the films \"Ca$h\" \"Street\" \"Jack Woody\" )|Beyond the Wall of Sleep]]\", in 2015 Gregory Executive produced Street which went on to have a world wide success on Netflix Street 2 is in development for 2018 Fawcett starred in an uncredited role as a Handsome Young Man in Fox's 1992 Halloween special \"Count DeClues' Mystery Castle\" starring Max Maven.  He took part in Tony Zierra's 2011 documentary \"My Big Break\" which follows the early careers of Fawcett, Wes Bentley, Chad Lindberg and Brad Rowe.\n\nQuestion: What was the biographical film that was directed by Joe Johnston and starred Chad Lindberg in an acting role?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the biographical film.\"\n    },\n    \"film_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the film, confirming it is biographical.\"\n    },\n    \"director\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the film's director.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the film was released.\"\n    },\n    \"actor_of_interest\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the actor in question.\"\n        },\n        \"is_in_film\": {\n          \"type\": \"boolean\",\n          \"description\": \"True if the actor is confirmed to be in the film.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"is_in_film\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"other_notable_actors\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Other prominent actors mentioned in the film's description.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"film_genre\",\n    \"director\",\n    \"release_year\",\n    \"actor_of_interest\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the biographical film."
      },
      "film_genre": {
        "type": "string",
        "description": "The genre of the film, confirming it is biographical."
      },
      "director": {
        "type": "string",
        "description": "The name of the film's director."
      },
      "release_year": {
        "type": "integer",
        "description": "The year the film was released."
      },
      "actor_of_interest": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the actor in question."
          },
          "is_in_film": {
            "type": "boolean",
            "description": "True if the actor is confirmed to be in the film."
          }
        },
        "required": [
          "name",
          "is_in_film"
        ],
        "additionalProperties": false
      },
      "other_notable_actors": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Other prominent actors mentioned in the film's description."
      }
    },
    "required": [
      "film_title",
      "film_genre",
      "director",
      "release_year",
      "actor_of_interest"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
