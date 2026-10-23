{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nKill Your Friends (film): Kill Your Friends is a 2015 British dark comedy crime-thriller film directed by Owen Harris, script written by John Niven based on his own written 2008 novel of the same name.  The film stars Nicholas Hoult, Craig Roberts, Tom Riley, and Georgia King.  The film was selected to be shown in the City to City section of the 2015 Toronto Film Festival.  The film was released on 6 November 2015 by StudioCanal.\n\nEk Khiladi Ek Haseena (film): Ek Khiladi Ek Haseena, released in 2005, is an Indian Hindi erotic crime-thriller film directed by Suparn Verma.  It is a remake of the 2003 Hollywood crime drama movie Confidence.  This movie was another movie in which the father-son duo Fardeen Khan and Feroz Khan had worked.  Before this they have worked in 2003 movie Janasheen.  This movie was 1st lead role for actress Koena Mitra who was seen in small roles.\n\nSimenona Martinez: Simenona Martinez is an American actress, singer-songwriter and film director from Los Angeles, California.  She made her television debut in on the WB20 in San Francisco, California.  She is most well known for her work on the Disney Channel's Playhouse Disney show Behind the Ears and for her role in \"Alex Cross\" alongside Tyler Perry.\n\nA Man Named Rocca: A Man Named Rocca (French: \"Un nommé La Rocca\" , Italian: \"Quello che spara per primo\" ) is a 1961 French-Italian crime-thriller film directed by Jean Becker and starring Jean Paul Belmondo.  It is based on the 1968 novel \"L'Excommunié\" by José Giovanni.  Belmondo appeared in another film version of this novel in 1972, directed by Giovanni, called \"Bad Luck\".\n\nCompany (film): Company is a 2002 Indian crime-thriller film directed by Ram Gopal Varma.  The film stars Mohanlal, Manisha Koirala, Vivek Oberoi, Ajay Devgn, and Antara Mali in pivotal roles.  It is a fictional exposé of the Mumbai underworld, loosely based on the Indian mafia organization D-Company, known to be run by Dawood Ibrahim.  It is the second film in the Indian \"Gangster\" trilogy, and a sequel to the blockbuster \"Satya\".  Upon release, the film received positive reviews from critics as well as audience, having won seven Filmfare Awards; three IIFA Awards, and went on to become one of the highest grossing Bollywood film(s) of 2002.\n\nAlex Cross (film): Alex Cross is a 2012 American action crime-thriller film directed by Rob Cohen and starring Tyler Perry as the title character and Matthew Fox as the villain Picasso.  The adapted screenplay was written by Marc Moss and Kerry Williamson.  This is the third film appearance of the character Alex Cross, the lead of a series of novels by James Patterson.  Cross was previously portrayed by Morgan Freeman in \"Kiss the Girls\" (1997) and \"Along Came a Spider\" (2001).  In 2010, Idris Elba was hired to play Cross, but was replaced by Perry.  Filming took place in 2011, and \"Alex Cross\" was released on October 19, 2012 in the United States and Canada.\n\nKrodham: Krodham (English: \"Fury\") is 1982 Tamil Crime-thriller film directed by A. Jagannathan.  The film screenplay and story were written by Prem Menon and dialogue written by K. Rangarajan respectively.  Music by Sankar Ganesh assets to the film.  The film starring Prem Menon lead with Rani Padmini, S. A. Ashokan played pivotal role.  The film was heavily inspired from the American vigilante-action film \"Death Wish\" (1974), directed by Michael Winner and starring Charles Bronson.  In 2000, Prem acted and directed the sequel this film \"Krodham 2\".\n\nThe Lady in Question (1999 film): The Lady in Question is a 1999 American made-for-television mystery crime-thriller film directed by Joyce Chopra.  It represents the last leading role and film for Gene Wilder and his last credit as screenwriter.  As the previous \"Murder in a Small Town\" Wilder plays the amateur detective Larry \"Cash\" Carter.\n\nCanne mozze: Canne mozze (\"\"Sawed-off Shotgun\"\") is a 1977 Italian crime-thriller film written and directed by Mario Imperoli.  It was the last film directed by Imperoli, who died in December 1977.\n\nSamrat (film): Samrat is a 1997 Tamil crime-thriller film directed by C. Dhinakaran.  The film features Ramki, Vineetha and newcomer Rukma in the lead roles, with Mohan Natarajan, R. Sundarrajan, Thalaivasal Vijay, Sabitha Anand, Vasuki, Rajasekhar and Veera Pandiyan playing supporting roles.  The film, produced by Lakshmi Karan, had musical score by Manoj Saran and was released on 10 October 1997.  The film is based on the novel \"A Kiss Before Dying\" written by Ira Levin.  The film became a failure at the box-office.\n\nQuestion: Simenona Martinez had a role in the 2012 crime-thriller film directed by whom?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"film_release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"film_genres\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"The genres of the film.\"\n    },\n    \"director_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the film's director.\"\n    },\n    \"actress_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actress who had a role in the film.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"film_release_year\",\n    \"film_genres\",\n    \"director_name\",\n    \"actress_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "film_release_year": {
        "type": "integer",
        "description": "The release year of the film."
      },
      "film_genres": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "The genres of the film."
      },
      "director_name": {
        "type": "string",
        "description": "The name of the film's director."
      },
      "actress_name": {
        "type": "string",
        "description": "The name of the actress who had a role in the film."
      }
    },
    "required": [
      "film_title",
      "film_release_year",
      "film_genres",
      "director_name",
      "actress_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
