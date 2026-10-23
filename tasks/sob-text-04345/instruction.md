{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Last Days on Mars: The Last Days on Mars is a 2013 science fiction-horror film directed by Ruairí Robinson with a screenplay by Clive Dawson, based on the short story \"The Animators\" by Sydney J. Bounds.  It was screened in the Directors' Fortnight section at the 2013 Cannes Film Festival.  The film received a limited release on 6 December 2013 in the United States and 11 April 2014 in the United Kingdom.  It stars Liev Schreiber, Elias Koteas, Romola Garai, Goran Kostić, Johnny Harris, Tom Cullen, Yusra Warsama, and Olivia Williams.  It is an international co-production between Ireland and the UK.\n\nChristopher Lee: Sir Christopher Frank Carandini Lee {'1': \", '2': \", '3': \", '4': \"} (27 May 1922 – 7 June 2015) was an English character actor, singer, and author.  With a career spanning nearly 70 years, Lee was well known for portraying villains and became best known for his role as Count Dracula in a sequence of Hammer Horror films.  His other film roles include Francisco Scaramanga in the James Bond film \"The Man with the Golden Gun\" (1974), Saruman in \"The Lord of the Rings\" film trilogy (2001–2003) and \"The Hobbit\" film trilogy (2012–2014), and Count Dooku in the second and third films of the \"Star Wars\" prequel trilogy (2002 & 2005).\n\nStranded (2013 film): Stranded is a 2013 science fiction-horror film directed and co-written by Roger Christian starring Christian Slater, Brendan Fehr, Amy Matysio, and Michael Therriault.  Astronauts stranded on a lunar mining base attempt to survive an attack by a shapeshifting alien life form.  Filming was at the Canada Saskatchewan Production Studios by Regina, Saskatchewan based Minds Eye Entertainment.  The film was one of the last financed by the province's cancelled film employment tax credit and was produced entirely in Saskatchewan.\n\nSon of Ingagi: Son of Ingagi is a 1940 American film directed by Richard C. Kahn.  It was the first science fiction-horror film to feature an all-black cast.  It was written by Spencer Williams based on his own short story, \"House of Horror\".  Although the film's title appears to suggest that it is a sequel to the 1930 movie \"Ingagi\", it is not.  (The latter is an exploitation film in the guise of an ethnographic film in which purported African women are given over to gorillas as sex slaves.)\n\nVillage of the Damned (1995 film): John Carpenter's Village of the Damned is a 1995 American science fiction-horror film directed by John Carpenter and a remake of the 1960 film of the same name which in turn is based on the novel \"The Midwich Cuckoos\" by John Wyndham.  The 1995 remake is set in Northern California, whereas the book and original film were both set in the United Kingdom.  The 1995 film was marketed with the tagline, \"Beware the Children\", and stars Christopher Reeve, Kirstie Alley, Linda Kozlowski, Michael Pare, Mark Hamill, and Meredith Salenger.\n\nThe Return of Doctor X: The Return of Doctor X (also billed as The Return of Dr. X) is a 1939 American science fiction-horror film directed by Vincent Sherman and starring Wayne Morris, Rosemary Lane, and Humphrey Bogart as the title character.  It was based on the short story \"The Doctor's Secret\" by William J. Makin.  Despite supposedly being a sequel to \"Doctor X\" (1933), also produced by Warner Bros., the films are unrelated.\n\nPlan 9 from Outer Space: Plan 9 from Outer Space (originally titled Grave Robbers from Outer Space) is a 1959 American independent black and white science fiction-horror film, written, produced, directed, and edited by Ed Wood, that stars Gregory Walcott, Mona McKinnon, Tor Johnson, and Vampira.  The film also posthumously bills Bela Lugosi as a star (silent footage of the actor had actually been shot by Wood for another, unfinished film just prior to Lugosi's death in August 1956).  \"Plan 9 from Outer Space\" was released theatrically in 1959 by Distributors Corporation of America (as Valiant Pictures).\n\n+1 (film): +1 (also known as Plus One and Shadow Walkers) is a 2013 American science fiction-horror film directed by Dennis Iliadis.  It premiered on March 10, 2013, at SXSW and stars Ashley Hinshaw, Rhys Wakefield, and Natalie Hall. \" +1\" was released in theaters, iTunes, and VOD on September 20, 2013.  For the VOD release Iliadis worked on fine-tuning elements of the film, as he felt that the SXSW release was too \"rushed\".\n\nMonster Shark: Monster Shark (Italian: \"Shark - Rosso nell'oceano\" ) is a 1984 Italian-French science fiction-horror film directed by Lamberto Bava.  It was also released in various countries as \"Devil Fish\", \"Monster from the Red Ocean\", \"Devouring Waves\" and \"Shark: Red in the Ocean\".  The script was co-written by Dardano Sacchetti, based on a story idea contributed by Luigi Cozzi and producer Sergio Martino.\n\nHorror Express: Horror Express, a.k.a Pánico en el Transiberiano in Spain (\"Panic on the Trans-Siberian Express\"), is a 1972 Spanish-British science fiction-horror film produced by Bernard Gordon and Gregorio Sacristan, directed by Eugenio Martín, that stars Christopher Lee, Peter Cushing, Alberto de Mendoza, Silvia Tortosa and Telly Savalas.  The screenplay was written by Arnaud d'Usseau and Julian Zimet (credited as Julian Halevy).\n\nQuestion: The actor who played Saruman in \"The Lord of the Rings\" trilogy also starred in a 1972 science fiction-horror film directed by whom?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor who played Saruman in 'The Lord of the Rings' trilogy.\"\n    },\n    \"role_in_trilogy\": {\n      \"type\": \"string\",\n      \"description\": \"The specific role played by the actor in 'The Lord of the Rings' trilogy.\"\n    },\n    \"related_film\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the science fiction-horror film.\"\n        },\n        \"year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the film.\"\n        },\n        \"genre\": {\n          \"type\": \"string\",\n          \"description\": \"The genre of the film.\"\n        },\n        \"director\": {\n          \"type\": \"string\",\n          \"description\": \"The director of the film.\"\n        },\n        \"other_stars\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"Other notable actors starring in the film.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"year\",\n        \"genre\",\n        \"director\",\n        \"other_stars\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"role_in_trilogy\",\n    \"related_film\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The name of the actor who played Saruman in 'The Lord of the Rings' trilogy."
      },
      "role_in_trilogy": {
        "type": "string",
        "description": "The specific role played by the actor in 'The Lord of the Rings' trilogy."
      },
      "related_film": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the science fiction-horror film."
          },
          "year": {
            "type": "integer",
            "description": "The release year of the film."
          },
          "genre": {
            "type": "string",
            "description": "The genre of the film."
          },
          "director": {
            "type": "string",
            "description": "The director of the film."
          },
          "other_stars": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Other notable actors starring in the film."
          }
        },
        "required": [
          "title",
          "year",
          "genre",
          "director",
          "other_stars"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "actor_name",
      "role_in_trilogy",
      "related_film"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
