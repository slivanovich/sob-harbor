{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMississippi Masala: Mississippi Masala is a 1991 romantic drama film directed by Mira Nair, based upon a screenplay by Sooni Taraporevala, starring Denzel Washington, Sarita Choudhury, and Roshan Seth.  Set primarily in rural Mississippi, the film explores interracial romance between African Americans and Indian Americans in the United States.\n\nPart 2, Sounder: Part 2, Sounder is a 1976 American drama film directed by William A. Graham.  It is the sequel to the 1972 Oscar-nominated film \"Sounder\", which in turn is based on William H. Armstrong's Newbery Award-winning novel of the same name.  Although Lonne Elder III and Robert B. Radnitz returned as screenwriter and producer respectively, neither Martin Ritt nor any of the cast members from the first film participated in the sequel, with the exception of Taj Mahal, who reprised his role as Ike and returned as composer.  According to Bob McCann, the film was \"barely released.\"\n\nSooni Taraporevala: Sooni Taraporevala (born 1957) is an Indian screenwriter, photographer and filmmaker who is best known as the screenwriter of \"Mississippi Masala\", \"The Namesake\" and Oscar-nominated \"Salaam Bombay\" (1988), all directed by Mira Nair.\n\nHowards End (film): Howards End is a 1992 British romantic drama film based upon the novel of the same name by E. M. Forster (published in 1910), a story of class relations in turn-of-the-20th-century England.  The film—produced by Merchant Ivory Productions as their third adaptation of a Forster novel (following \"A Room with a View\" in 1985 and \"Maurice\" in 1987)—was the first film to be released by Sony Pictures Classics.  The screenplay was written by Ruth Prawer Jhabvala, directed by James Ivory and produced by Ismail Merchant.\n\nLittle Zizou: Little Zizou is an 2008 Indian film in Hindi, Gujarati, and English, written and directed by Sooni Taraporevala.  \"Little Zizou\" is a fast-paced, exuberant, yet poignant comedy about how two battling Mumbai families finally come to terms.\n\nDuel of Hearts: Duel of Hearts is a 1991 romantic television film directed by John Hough.  Terence Feely penned the screenplay, based on the Barbara Cartland novel, \"A Duel of Hearts\".  The film stars Alison Doody, Michael York, Geraldine Chaplin and Benedict Taylor.\n\nThe Namesake (film): The Namesake is a 2006 Indian-American drama film which was released in the United States on 9 March 2007, following screenings at film festivals in Toronto and New York City.  It was directed by Mira Nair and is based upon the novel of the same name by Jhumpa Lahiri, who appeared in the movie.  Sooni Taraporevala wrote the screenplay.  The film received positive reviews from American critics.  The film stars Tabu, Irrfan Khan, Kal Penn and Sahira Nair.\n\nLone Scherfig: Lone Scherfig (born 2 May 1959) is a Danish film director and screenwriter who has been involved with the Dogme 95 film movement and who has been widely critically acclaimed for several of her movies, including the Oscar-nominated film \"An Education\" (2009).  Scherfig's movies are generally romantic comedies, including her film \"One Day\" (2011), based on the David Nicholls novel.  Through both experimenting with creative constraints and her astute attention to detail, she has come to be recognized as a blossoming talent in the film industry.\n\nParineeta (2005 film): Parineeta (\"The Married Woman\") is a 2005 Indian musical romantic drama film adaptation of the 1914 Bengali novella, \"Parineeta\" by Sarat Chandra Chattopadhyay.  Directed by debutant Pradeep Sarkar, it was based upon a screenplay by the film's producer, Vidhu Vinod Chopra.  The film featured Vidya Balan (In her Bollywood Debut), Saif Ali Khan and Sanjay Dutt in the lead roles.  Raima Sen plays the supporting role of Lalita's chirpy cousin.  Sabyasachi Chakrabarty plays the pivotal role of Shekhar's father.  Diya Mirza, with a cameo appearance as Shekhar's fiancé and Rekha, with a cameo performance of a night club (Moulin Rouge) singer, are other notable performances.\n\nSuch a Long Journey (film): Such a Long Journey is a 1998 Indo-Canadian english language film based on the novel of the same name written by Rohinton Mistry.  The film is directed by Sturla Gunnarsson with a screenplay by Sooni Taraporevala.  The film received twelve Genie Awards nominations including the Best Picture, Best Director, and Best Actor.  The film was screened at the Toronto International Film Festival.\n\nQuestion: Which Oscar-nominated film was written by the screenwriter who wrote a 1991 romantic drama based upon a screenplay by Sooni Taraporevala?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"linking_film\": {\n      \"type\": \"object\",\n      \"description\": \"The film that establishes the connection to the screenwriter.\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"Title of the linking film.\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"Release year of the linking film.\"\n        },\n        \"genre\": {\n          \"type\": \"string\",\n          \"description\": \"Genre of the linking film.\"\n        },\n        \"screenwriter\": {\n          \"type\": \"string\",\n          \"description\": \"The screenwriter of the linking film.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"release_year\",\n        \"genre\",\n        \"screenwriter\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"screenwriter_details\": {\n      \"type\": \"object\",\n      \"description\": \"Details about the identified screenwriter.\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"Name of the screenwriter.\"\n        },\n        \"other_notable_screenplays\": {\n          \"type\": \"array\",\n          \"description\": \"Other notable screenplays by this writer mentioned in the context.\",\n          \"items\": {\n            \"type\": \"string\"\n          }\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"other_notable_screenplays\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"oscar_nominated_film\": {\n      \"type\": \"object\",\n      \"description\": \"The Oscar-nominated film written by the identified screenwriter.\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"Title of the Oscar-nominated film.\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"Release year of the Oscar-nominated film.\"\n        },\n        \"director\": {\n          \"type\": \"string\",\n          \"description\": \"Director of the Oscar-nominated film.\"\n        },\n        \"is_oscar_nominated\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the film was Oscar-nominated.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"release_year\",\n        \"director\",\n        \"is_oscar_nominated\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"linking_film\",\n    \"screenwriter_details\",\n    \"oscar_nominated_film\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "linking_film": {
        "type": "object",
        "description": "The film that establishes the connection to the screenwriter.",
        "properties": {
          "title": {
            "type": "string",
            "description": "Title of the linking film."
          },
          "release_year": {
            "type": "integer",
            "description": "Release year of the linking film."
          },
          "genre": {
            "type": "string",
            "description": "Genre of the linking film."
          },
          "screenwriter": {
            "type": "string",
            "description": "The screenwriter of the linking film."
          }
        },
        "required": [
          "title",
          "release_year",
          "genre",
          "screenwriter"
        ],
        "additionalProperties": false
      },
      "screenwriter_details": {
        "type": "object",
        "description": "Details about the identified screenwriter.",
        "properties": {
          "name": {
            "type": "string",
            "description": "Name of the screenwriter."
          },
          "other_notable_screenplays": {
            "type": "array",
            "description": "Other notable screenplays by this writer mentioned in the context.",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "name",
          "other_notable_screenplays"
        ],
        "additionalProperties": false
      },
      "oscar_nominated_film": {
        "type": "object",
        "description": "The Oscar-nominated film written by the identified screenwriter.",
        "properties": {
          "title": {
            "type": "string",
            "description": "Title of the Oscar-nominated film."
          },
          "release_year": {
            "type": "integer",
            "description": "Release year of the Oscar-nominated film."
          },
          "director": {
            "type": "string",
            "description": "Director of the Oscar-nominated film."
          },
          "is_oscar_nominated": {
            "type": "boolean",
            "description": "Indicates if the film was Oscar-nominated."
          }
        },
        "required": [
          "title",
          "release_year",
          "director",
          "is_oscar_nominated"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "linking_film",
      "screenwriter_details",
      "oscar_nominated_film"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
