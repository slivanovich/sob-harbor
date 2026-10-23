{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGulaab Gang: Gulaab Gang is a 2014 Indian crime drama film centered on the struggle of women in the country, directed by Soumik Sen and produced by Anubhav Sinha.  It stars Madhuri Dixit and Juhi Chawla.  The film was released on 7 March 2014.  Upon its release the film received positive-to-mixed reviews from critics; however, the critics raved about Chawla's performance in the film, calling it the best performance of the year.  The makers declared the film a flop on its opening day itself.\n\nKedi (2010 film): Kedi (English: \"Conman\" ) is a 2010 Telugu film produced by D.Sivaprasad Reddy under the Kamakshi Movies banner and directed by Kiran Kumar.  The film stars Nagarjuna Akkineni and Mamta Mohandas with Ankur Vikal (\"Slumdog Millionaire\") in the role of the antagonist.  The music score is by Sandeep Chowtha, who previously wrote music for Nagarjuna's films \"Ninne Pelladutha\" (1996), \"Chandralekha\" (1998) and \"Super\" (2005).  The film was released on 12 February 2010.  It was dubbed into Hindi as \"Gambler No. 1\".  The film was recorded as a \"flop\" at the box-office.\n\nKalankini Kankabati: Kalankini Kankabati (English:Stigmatized Kankabati) is a 1981 Bengali language Indian crime drama film directed by Uttam Kumar, starring Mithun Chakraborty, Sharmila Tagore, Supriya Choudhury, Asitbaran and Uttam Kumar\n\nThee (1981 film): Thee (English: Fire ) is a 1981 Tamil-language Indian crime drama film directed R. Krishnamurthy.  Rajinikanth plays the lead role and Suman plays the role of his brother.  It is a remake of the classic Hindi film Deewar starring Bollywood Mega Star Amitabh Bachchan with Shashi Kapoor, Neetu Singh and Parveen Babi.  The Hindi film was directed by Yash Chopra.\n\nAnkur Bhatia: Ankur Bhatia (born 24 May 1982) is an Indian actor and model.  He grew up in Bhopal, India and currently resides in Mumbai and New York.  He made his acting debut in 2010 in Payal Sethi's Grant St. Shaving Co which was produced by Mira Nair.  In 2012, he won the Best Actor Commendation Award at the NYU Tisch School of the Arts Film Festival for Coconut Grove.  In 2013, Ankur played a negative role in a Bollywood/Tollywood film \"Zanjeer (2013 film)\"/\"Toofan\", remake of \"Zanjeer.\"  He is currently shooting for Apoorva Lakhia's , starring Shraddha Kapoor, which will be released in theatres on 18 August 2017.\n\nParinda: Parinda (English: The Bird) is a 1989 Indian crime drama film directed and produced by Vidhu Vinod Chopra.  It is considered by many to be the turning point in reality in Hindi cinema, as the theme of the film discusses the real life of Indian underworld gangsters and the general life of residents in the city of Mumbai.  The film stars Nana Patekar, Jackie Shroff, Anil Kapoor and Madhuri Dixit in the lead roles.  It won two National Film Awards and five Filmfare Awards, and was India's official entry for the 1990 Academy Award for Best Foreign Language Film.  The film was titled \"Kabutarkhana\" but later changed and release as \"Parinda\". This movie has been remade in Hollywood as Broken Horses.  and also been listed as one of 100 greatest Indian Films of all time.\n\nThe Forest (2009 film): The Forest is a 2009 Indian film written and directed by Ashvin Kumar and produced by Kumar and Judith James.  The lead role is to Ankur Vikal and the film is shot at the Corbett National Park.\n\nJass Bhatia: Jass Bhatia (born Jaskaran Singh Bhatia on 29 June 1988) is an Indian actor and model.  He began his career by working in several television commercials and print ads.  He made his Bollywood debut with a supporting role in the Indian romantic drama film \"Mausam\" in 2011.  He followed it with a role in the less successful film \"I Don't Luv U\".  In 2013, the Indian biographical sports drama film \"Bhaag Milkha Bhaag\" directed by Rakeysh Omprakash Mehra proved to be his first commercially successful film in 5 years.  In 2014, Bhatia portrayed Parineeti Chopra's friend named \"Chimsy\" in Shaad Ali's Indian crime drama film \"Kill Dil\".  In the television circuit, Jass featured as Happy in \"Rab Se Sona Ishq\" and played the character Bakshish in \"Firangi Bahu\".\n\nMaqbool: Maqbool is a 2003 Indian crime drama film directed by Vishal Bhardwaj and starring Pankaj Kapur, Irrfan Khan, Tabu and Masumeh Makhija in an adaptation of the play \"Macbeth\" by Shakespeare.\n\nAnkur Vikal: Ankur Vikal is an Indian film and theatre actor.  He graduated from the National School of Drama (NSD), New Delhi in 2000, after studying Architecture at M.S. University, Baroda.  He has acted in the Motley Theatre Group in plays such as \"Manto Ismat Haazir Hain\", \"Safed Jhooth Kaali Shalwar\", \"Katha Kollage II\", \"All Thieves\",\" The Caine Mutiny Court-Martial\", and \"Salome\".  His film career began with the Indian ground-breaking film \"Mango Soufflé\", followed by the highly acclaimed films \"Maqbool\" and \"Missed Call\".\n\nQuestion: Which Indian crime drama is an adaptation of Macbeth in which Ankur Vikal is an actor?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the Indian crime drama film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the film.\"\n    },\n    \"is_macbeth_adaptation\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the film is an adaptation of Shakespeare's Macbeth.\"\n    },\n    \"director\": {\n      \"type\": \"string\",\n      \"description\": \"The director of the film.\"\n    },\n    \"actors\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of prominent actors in the film, including the one mentioned in the question.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"genre\",\n    \"is_macbeth_adaptation\",\n    \"director\",\n    \"actors\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the Indian crime drama film."
      },
      "release_year": {
        "type": "integer",
        "description": "The release year of the film."
      },
      "genre": {
        "type": "string",
        "description": "The genre of the film."
      },
      "is_macbeth_adaptation": {
        "type": "boolean",
        "description": "Indicates if the film is an adaptation of Shakespeare's Macbeth."
      },
      "director": {
        "type": "string",
        "description": "The director of the film."
      },
      "actors": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of prominent actors in the film, including the one mentioned in the question."
      }
    },
    "required": [
      "film_title",
      "release_year",
      "genre",
      "is_macbeth_adaptation",
      "director",
      "actors"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
