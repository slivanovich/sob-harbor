{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBagdad Theatre: The Bagdad Theatre is a movie theater in the Hawthorne District of Portland, Oregon, United States.  It originally opened in 1927 and was the site of the gala premiere of \"One Flew Over the Cuckoo's Nest\" in 1975, and of \"My Own Private Idaho\" in 1991.\n\nBagdad Café: Bagdad Café (also known as Out of Rosenheim) is a 1987 German film directed by Percy Adlon.  It is a comedy-drama set in a remote truck-stop café and motel in the Mojave Desert in the US state of California.  Loosely based on Carson McCullers' novella \"The Ballad of the Sad Café\" (1951), the film centers on two women who have recently separated from their husbands, and the blossoming friendship that ensues.  It runs 95 minutes in the U.S. and 108 minutes in the German version.\n\nBagdad Cafe (TV series): Bagdad Cafe is an American television sitcom starring Whoopi Goldberg and Jean Stapleton that aired on CBS.  The series premiered March 30, 1990, and ran two seasons before being cancelled in winter 1990.  The last two episodes aired in July 1991.  The show is based on the 1987 Percy Adlon film \"Bagdad Cafe\".\n\nThe Thief of Bagdad (1952 film): The Thief of Bagdad (German: Die Diebin von Bagdad) is a 1952 German musical comedy directed by Karel Lamac and starring Theo Lingen, Paul Kemp, Sonja Ziemann and Rudolf Prack.  It is not a remake of the 1940 film of the same name, but a comedy about the magic tricks of a female thief in Bagdad.  It was filmed in Bendestorf, Lower Saxony.\n\nBrian McMenamin: Brian McMenamin (born 1957) is an American businessman and philanthropist in the state of Oregon.  A native of the state, he and his older brother Mike McMenamin founded the McMenamins restaurant and brewpub chain in 1983.  He serves as general manager and vice-president of the company which operates more than 50 locations that include music venues such as the Crystal Ballroom, movie theaters such as the Bagdad Theatre, historic buildings converted to brewpubs like the Cornelius Pass Roadhouse, and several hotels.\n\nArabian Nights (1942 film): Arabian Nights is a 1942 adventure film starring Sabu, Maria Montez, Jon Hall and Leif Erickson and directed by John Rawlins.  The film is derived from \"The Book of One Thousand and One Nights\" but owes more to the imagination of Universal Pictures than the original Arabian stories.  Unlike other films in the genre (\"The Thief of Bagdad\"), it features no monsters or supernatural elements.\n\nThe Thief of Bagdad (1924 film): The Thief of Bagdad is a 1924 American swashbuckler film directed by Raoul Walsh and starring Douglas Fairbanks.  Freely adapted from \"One Thousand and One Nights\", it tells the story of a thief who falls in love with the daughter of the Caliph of Bagdad.  In 1996, the film was selected for preservation in the United States National Film Registry by the Library of Congress as being \"culturally, historically, or aesthetically significant\".\n\nOne Flew Over the Cuckoo's Nest (film): One Flew Over the Cuckoo's Nest is a 1975 American comedy-drama film directed by Miloš Forman, based on the 1962 novel \"One Flew Over the Cuckoo's Nest\" by Ken Kesey.  The film stars Jack Nicholson, and features a supporting cast of Louise Fletcher, William Redfield, Will Sampson and Brad Dourif.\n\nThe Thief of Bagdad (1940 film): The Thief of Bagdad is a 1940 British Technicolor Arabian fantasy film produced by Alexander Korda and directed by Michael Powell, Ludwig Berger, and Tim Whelan, with additional contributions by Korda's brothers Vincent and Zoltán, and William Cameron Menzies.  The film starred child actor Sabu, Conrad Veidt, John Justin, and June Duprez.  It was distributed in the US and the UK by United Artists.\n\nBaghdad Thirudan: Baghdad Thirudan (English: \"The Thief of Bagdad\" ) is a 1960 Tamil-language swashbuckler film produced and directed by T. P. Sundaram.  The film starred M. G. Ramachandran and Vyjayanthimala in the lead with M. N. Nambiar, T. S. Balaiah, T. R. Ramachandran, S. A. Ashokan, M. N. Rajam, A. Sandhya and S. N. Lakshmi forms an ensemble cast.  The film was a remake of 1924 silent film The Thief of Bagdad and was inspired by 1951 Tony Curtis-starrer, \"The Prince Who Was A Thief\".\n\nQuestion: Who directed the film that premiered at The Bagdad Theatre in 1975?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film that premiered.\"\n    },\n    \"premiere_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the film premiered.\"\n    },\n    \"premiere_venue\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the venue where the film premiered.\"\n    },\n    \"director_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the director of the film.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"premiere_year\",\n    \"premiere_venue\",\n    \"director_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film that premiered."
      },
      "premiere_year": {
        "type": "integer",
        "description": "The year the film premiered."
      },
      "premiere_venue": {
        "type": "string",
        "description": "The name of the venue where the film premiered."
      },
      "director_name": {
        "type": "string",
        "description": "The name of the director of the film."
      }
    },
    "required": [
      "film_title",
      "premiere_year",
      "premiere_venue",
      "director_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
