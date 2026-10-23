{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDavid Mitton: David Nelson Godfrey Mitton (13 July 1938 – 16 May 2008) was a British television producer, director and writer, and an experienced model-maker and author, best known for producing and directing the children's TV programmes \"Thomas & Friends\" and \"Tugs\".  During the 1960s, he worked with Gerry and Sylvia Anderson as a special effects technician on series such as \"Thunderbirds\", \"Captain Scarlet and the Mysterons\", \"Joe 90\", \"The Secret Service\" and \"UFO\".\n\nPeter Greenwood: Peter Greenwood (born 17 October 1962 in Sydney, Australia) is an Australian screen and voice actor, special effects technician, researcher, designer and media consultant.  He is related to actress Joan Greenwood.  He attended Killara High School in Sydney, NSW.\n\nCasa d'appuntamento: Casa d'appuntamento (Translation: \"The House of Rendezvous\") is a 1972 giallo film directed by Ferdinando Merighi under the pseudonym \"F. L. Morris\", and edited by Bruno Mattei.  It was released as The French Sex Murders in the US, and The Bogey Man and the French Murders in the UK.  It stars Rosalba Neri, Anita Ekberg, Barbara Bouchet, Howard Vernon and Gordon Mitchell.  The actor who played the police inspector in this film (Robert Sacchi) was a professional Humphrey Bogart lookalike, which explains the alternate \"Bogey Man\" title.  Special effects technician Carlo Rambaldi handled the throat slashings and beheadings that take place in the movie.\n\nWalter Percy Day: Walter Percy Day O.B.E. (1878–1965) was a British painter best remembered for his work as a matte artist and special effects technician in the film industry.\n\nChristian Rivers: Christian Rivers is a New Zealand storyboard artist, visual effects supervisor, special effects technician and director.  He first met Peter Jackson as a 17-year-old, and storyboarded all of Jackson's films since \"Braindead\".  He also cameoed in \"\" as a Gondorian soldier and \"King Kong\" as a Soldier in Truck.  He will also direct the upcoming adaptation of \"Mortal Engines\" and the remake of \"The Dam Busters\", both produced by Peter Jackson.\n\nThe Pink Panther (1963 film): The Pink Panther is a 1963 American comedy film directed by Blake Edwards and co-written by Edwards and Maurice Richlin, starring David Niven, Peter Sellers, Robert Wagner, Capucine, and Claudia Cardinale.  The film introduced the cartoon character of the same name, in an opening credits sequence animated by DePatie-Freleng Enterprises.\n\nWilliam Butler (actor): William Butler is an actor, writer, director, make-up artist, special effects technician and producer.\n\nUb Iwerks: Ubbe Eert \"Ub\" Iwerks, A.S.C. ( ; March 24, 1901 – July 7, 1971) was an American animator, cartoonist, character designer, inventor, and special effects technician, who created Oswald the Lucky Rabbit and Mickey Mouse with Walt Disney.  The works Iwerks produced alongside Disney went on to win numerous awards, including multiple Academy Awards.\n\nLee Zavitz: Leland \"Lee\" Zavitz (August 20, 1904– June 2, 1977) was a special effects technician.  He was born in Mount Vernon, Washington.  His first major impact was for his work on John Ford's 1937 film, \"The Hurricane\".  Zavitz's work on the 1950 space fantasy film \"Destination Moon\" won the Academy Award for Best Visual Effects.  He also worked on films such as \"Around the World in Eighty Days\" (1956), \"The Alamo\" (1960), \"Sodom and Gomorrah\" (1963), \"The Pink Panther\" (1963) and John Frankenheimer's \"The Train\" (1964).  His last film was Sydney Pollack's wartime chiller \"Castle Keep\" in 1969.\n\nKevin Hutchinson: Kevin Hutchinson (October 10, 1974 – August 31, 2012) was a Canadian make-up artist, special effects technician and art director whose credits include Zach Snyder's \"Dawn of the Dead\" remake, Len Wiseman's \"Total Recall\" and posthumously \"Pacific Rim\".  Hutchinson died on August 31, 2012 at the age of 37.\n\nQuestion: What American comedy is directed by Blake Edwards and has special effects technician Leland \"Lee\" Zavitz woking on it?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"director\": {\n      \"type\": \"string\",\n      \"description\": \"The director of the film.\"\n    },\n    \"special_effects_technician\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the special effects technician who worked on the film.\"\n    },\n    \"film_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"director\",\n    \"special_effects_technician\",\n    \"film_genre\",\n    \"release_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "director": {
        "type": "string",
        "description": "The director of the film."
      },
      "special_effects_technician": {
        "type": "string",
        "description": "The name of the special effects technician who worked on the film."
      },
      "film_genre": {
        "type": "string",
        "description": "The genre of the film."
      },
      "release_year": {
        "type": "integer",
        "description": "The release year of the film."
      }
    },
    "required": [
      "film_title",
      "director",
      "special_effects_technician",
      "film_genre",
      "release_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
