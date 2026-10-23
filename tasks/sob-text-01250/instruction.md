{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nFrances Slocum: Frances Slocum (March 4, 1773 – March 9, 1847) (Ma-con-na-quah, \"Young Bear\" or \"Little Bear\") was an adopted member of the Miami people.  Slocum was born into a Quaker family that migrated from Warwick, Rhode Island, in 1777 to the Wyoming Valley in Luzerne County, Pennsylvania.  On November 2, 1778, when Slocum was five years old, she was captured by three Delaware warriors at the Slocum family farm near Wilkes-Barre, Pennsylvania.  Slocum was raised among the Delaware in what is now Ohio and Indiana.  With her marriage to Shepoconah (Deaf Man), who later became a Miami chief, Slocum joined the Miami and took the name Maconaquah.  She settled with her Miami family at Deaf Man's village along the Mississinewa River near Peru, Indiana.\n\nGene Wilder: Jerome Silberman (June 11, 1933 – August 29, 2016), known professionally as Gene Wilder, was an American actor, screenwriter, director, producer, singer-songwriter and author.\n\nBeverly School for the Deaf: Beverly School for the Deaf was founded in 1876 by William Benjamin Swett in Beverly, Massachusetts.  Mr. Swett was a deaf man with a deaf daughter and saw a need for educational and vocational services for deaf children and young adults of the North Shore area of Boston.  In 1879 with a small legacy and the help of his close friend, the Reverend Dr. Thomas Gallaudet, a 57 acre parcel of land was purchased overlooking the tidal waters of the Bass River in Beverly.  The vision of Mr. Swett was organized and incorporated under the laws of the Commonwealth of Massachusetts as the \"New England Industrial School for Deaf Mutes.\"\n\nGerry Hughes (sailor): Gerry Hughes is a British sailor who became the first profoundly deaf man to sail single-handed across the Atlantic Ocean.  He crossed the finishing line off Castle Hill, Newport at 11:30 am local time (4:30 pm UTC) on Saturday 3 July 2005 after 35 days of sailing.  Hughes also became the world's first deaf yachtsman to sail single-handed around the world to pass the five great capes - he departed Troon, Scotland on 1 September 2012 and returned to Troon on 8 May 2013.\n\nBlack Paintings: The Black Paintings (Spanish: Pinturas negras) is the name given to a group of fourteen paintings by Francisco Goya from the later years of his life, likely between 1819 and 1823.  They portray intense, haunting themes, reflective of both his fear of insanity and his bleak outlook on humanity.  In 1819, at the age of 72, Goya moved into a two-story house outside Madrid that was called \"Quinta del Sordo\" (\"Deaf Man's Villa\").  Although the house had been named after the previous owner, who was deaf, Goya too was nearly deaf at the time as a result of an illness he had suffered when he was 46.  The paintings originally were painted as murals on the walls of the house, later being \"hacked off the walls and attached to canvas.\"  Currently they are held in the Museo del Prado in Madrid.\n\nSee No Evil, Hear No Evil: See No Evil, Hear No Evil is a 1989 American comedy film directed by Arthur Hiller.  The film stars Richard Pryor as a blind man and Gene Wilder as a deaf man who work together to thwart a trio of murderous thieves.  This is the third film featuring Wilder and Pryor, who had appeared previously in the 1976 film \"Silver Streak\" and the 1980 film \"Stir Crazy\".  The film was released in the United States on May 12, 1989.\n\nThe Deaf Man: The Deaf Man is a character in the 87th Precinct series of police procedurals by author Ed McBain (pseudonym of Evan Hunter).  A criminal mastermind who delights in creating complex schemes, The Deaf Man is usually pitted against the men of the 87th Precinct as he creates havoc in the fictional city of Isola.\n\nThree wise monkeys: The three wise monkeys (Japanese: 三猿 , Hepburn: san'en sanzaru , alternatively 三匹の猿 \"sanbiki no saru\", literally \"three monkeys\") , sometimes called the three mystic apes, are a pictorial maxim.  Together they embody the proverbial principle \"see no evil, hear no evil, speak no evil\".  The three monkeys are Mizaru, covering his eyes, who sees no evil; Kikazaru, covering his ears, who hears no evil; and Iwazaru, covering his mouth, who speaks no evil.\n\nChild of deaf adult: A child of deaf adult, often known by the acronym \"CODA\", is a person who was raised by one or more deaf parents or guardians.  Millie Brother coined the term and founded the organization CODA, which serves as a resource and a center of community for children of deaf adults.  Many CODAs are bilingual, speaking both an oral and a sign language, and bicultural, identifying with both deaf and hearing cultures.  CODAs must navigate the border between the deaf and hearing worlds, serving as liaisons between their deaf parents and the hearing world in which they reside.  Ninety percent of children born to deaf adults can hear normally, resulting in a significant and widespread community of CODAs around the world.  The acronym KODA (Kid of Deaf Adult) is sometimes used to refer to CODAs under the age of 18.\n\nWhat the Deaf Man Heard: What the Deaf Man Heard is a 1997 \"Hallmark Hall of Fame\" television movie that aired on CBS television on November 23, 1997.  It concerns Sammy, a man who pretends to be deaf and mute, when in reality he can hear and speak perfectly well.  The movie starred Matthew Modine and James Earl Jones.\n\nQuestion: In what year was the actor who is starred as a deaf man in \"See No Evil, Hear No Evil\" born?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor who played the deaf man.\"\n    },\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film mentioned in the question.\"\n    },\n    \"role_description\": {\n      \"type\": \"string\",\n      \"description\": \"Description of the character's condition in the film.\"\n    },\n    \"birth_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth year of the actor.\"\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"film_title\",\n    \"role_description\",\n    \"birth_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The name of the actor who played the deaf man."
      },
      "film_title": {
        "type": "string",
        "description": "The title of the film mentioned in the question."
      },
      "role_description": {
        "type": "string",
        "description": "Description of the character's condition in the film."
      },
      "birth_year": {
        "type": "integer",
        "description": "The birth year of the actor."
      }
    },
    "required": [
      "actor_name",
      "film_title",
      "role_description",
      "birth_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
