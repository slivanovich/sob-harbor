{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThagaraaru: Thagaraaru (English: \"Fight\" ) is a 2013 Indian Tamil action mystery drama film written and directed by newcomer Ganesh Vinaayac and produced by Cloud Nine Movies.  The film stars Arulnithi and Poorna in the lead roles.  The soundtrack was composed by Dharan, while Praveen Sathya composed the score.  Dillraj was the cinematographer, and T. S. Suresh edited the film.  The film released on 6 December 2013 and received positive reviews from critics.The film did average business at the box office.\n\nGone Baby Gone: Gone Baby Gone is a 2007 American neo-noir mystery drama film directed by Ben Affleck.  In his feature-length directorial debut, Affleck cowrote the screenplay with Aaron Stockard based on the novel \"Gone, Baby, Gone\" by Dennis Lehane.  The film stars Casey Affleck and Michelle Monaghan as two private investigators hunting for a little girl who was abducted from the Boston neighborhood of Dorchester.  The supporting cast includes Morgan Freeman, Ed Harris and Amy Ryan.\n\nThe Sense of an Ending (film): The Sense of an Ending is a 2017 British-American mystery drama film directed by Ritesh Batra and written by Nick Payne, based on the novel of the same name by Julian Barnes.  The film stars Jim Broadbent, Charlotte Rampling, Harriet Walter, Emily Mortimer and Michelle Dockery.\n\nThe Falling (2014 film): The Falling is a 2014 British mystery drama film written and directed by Carol Morley.  It stars Maisie Williams and Florence Pugh as best friends at an all-girls school.  The film also stars Greta Scacchi, Monica Dolan, Maxine Peake, and Mathew Baynton.  Production began in October 2013.  The film premiered at the BFI London Film Festival on 11 October 2014 and was released theatrically on 24 April 2015 in the UK.  \"The Falling\" earned £468,762 on a £750,000 budget.\n\nThe Prestige (film): The Prestige is a 2006 British-American mystery thriller film directed by Christopher Nolan, from a screenplay adapted by Nolan and his brother Jonathan from Christopher Priest's 1995 novel of the same name.  Its story follows Robert Angier and Alfred Borden, rival stage magicians in London at the end of the 19th century.  Obsessed with creating the best stage illusion, they engage in competitive one-upmanship with tragic results.  The film stars Hugh Jackman as Robert Angier, Christian Bale as Alfred Borden, and David Bowie as Nikola Tesla.  It also stars Scarlett Johansson, Michael Caine, Piper Perabo, Andy Serkis, and Rebecca Hall.  The film reunites Nolan with actors Bale and Caine from \"Batman Begins\" and returning cinematographer Wally Pfister, production designer Nathan Crowley, film score composer David Julyan, and editor Lee Smith.\n\nNon-Stop (film): Non-Stop is a 2014 American mystery action thriller film directed by Jaume Collet-Serra and starring Liam Neeson, Julianne Moore, Michelle Dockery, Lupita Nyong'o, and Scoot McNairy.  An international co-production among France, the United States, and the United Kingdom, it was the first film from Silver Pictures since \"Weird Science\", and its first film to be distributed by Universal Pictures since the end of Universal's deal with Warner Bros..  The film received mixed to positive reviews from critics and was a box office success.\n\nLena Headey filmography: Lena Headey is an English actress and producer.  Headey studied acting at Shelley College where she performed in a number of school productions at the Royal National Theatre.  She made her film debut in the 1992 mystery drama \"Waterland\".  After appearing in a series of supporting parts throughout the 1990s, she went on to find fame for lead performances in big-budget films such as the fantasy film \"The Brothers Grimm\" (2005) and the action film \"300\" (2007), portraying Gorgo, Queen of Sparta, a role she yet again played in \"\" (2014).\n\nThe Great Muppet Caper: The Great Muppet Caper is a 1981 British-American mystery musical comedy film directed by Jim Henson, marking his feature directorial debut.  The film is about the Muppets who must travel to London to stop a jewel heist.  It is the second of a series of live-action musical feature films, starring Jim Henson's Muppets.  The film was a British-American venture produced by Henson Associates and ITC Entertainment, and originally released by Universal Pictures on 26 June 1981.  It is also the only Muppet feature film directed by Henson.  Shot in Great Britain in 1980, the film was released shortly after the final season of \"The Muppet Show\".\n\nMichelle Dockery: Michelle Suzanne Dockery (born 15 December 1981) is an English actress and singer.  She is most widely known for her performance as Lady Mary Crawley in the ITV (UK) and PBS (U.S.) television period drama series \"Downton Abbey\" (2010–15), for which she was nominated for three consecutive Emmy Awards in the category for Outstanding Lead Actress In Drama Series, and a Golden Globe Award nomination.  She made her professional stage debut in \"His Dark Materials\" in 2004.  For her role as Eliza Doolittle in the 2007 London revival of \"Pygmalion\", she was nominated for the Evening Standard Award.\n\nPossession (2002 film): Possession is a 2002 British-American romantic mystery drama film written and directed by Neil LaBute and starring Gwyneth Paltrow and Aaron Eckhart.  It is based on the 1990 by British author A. S. Byatt, who won the Booker Prize for it the year it was published.\n\nQuestion: The Sense of an Ending is an British-American mystery drama film, released in which year, it stars include Michelle Dockery, an English actress and singer?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the film was released.\"\n    },\n    \"genre\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"The genres of the film.\"\n    },\n    \"starring_actors\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"actor_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the actor.\"\n          },\n          \"is_featured_in_film\": {\n            \"type\": \"boolean\",\n            \"description\": \"Indicates if the actor is listed as starring in this specific film.\"\n          },\n          \"nationality\": {\n            \"type\": \"string\",\n            \"description\": \"The nationality of the actor.\"\n          },\n          \"profession\": {\n            \"type\": \"array\",\n            \"items\": {\n              \"type\": \"string\"\n            },\n            \"description\": \"The professions of the actor.\"\n          }\n        },\n        \"required\": [\n          \"actor_name\",\n          \"is_featured_in_film\"\n        ],\n        \"additionalProperties\": false\n      },\n      \"description\": \"Details about the actors starring in the film, specifically Michelle Dockery.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"genre\",\n    \"starring_actors\"\n  ],\n  \"additionalProperties\": false\n}"
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
      "starring_actors": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "actor_name": {
              "type": "string",
              "description": "The name of the actor."
            },
            "is_featured_in_film": {
              "type": "boolean",
              "description": "Indicates if the actor is listed as starring in this specific film."
            },
            "nationality": {
              "type": "string",
              "description": "The nationality of the actor."
            },
            "profession": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "description": "The professions of the actor."
            }
          },
          "required": [
            "actor_name",
            "is_featured_in_film"
          ],
          "additionalProperties": false
        },
        "description": "Details about the actors starring in the film, specifically Michelle Dockery."
      }
    },
    "required": [
      "film_title",
      "release_year",
      "genre",
      "starring_actors"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
