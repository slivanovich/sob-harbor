{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nProduction of Avengers: Infinity War and the untitled Avengers sequel: Production of Avengers: Infinity War and the untitled Avengers sequel\n\nNatasha Henstridge: Natasha Tonya Henstridge (born August 15, 1974) is a Canadian actress and former fashion model.  In 1995, she came to prominence with her debut movie role as the genetically engineered human-alien hybrid Sil in the science-fiction thriller \"Species\", then the human-alien hybrid Eve in \"Species II\" and \"Species III\".  Other notable on-screen roles include \"The Whole Nine Yards\", \"The Whole Ten Yards\", \"It Had to Be You\", \"Ghosts of Mars\", \"She Spies\", the television series \"Eli Stone\", and the Canadian miniseries \"Would Be Kings\", for which she won the Gemini Award for best actress.  Her most recent role is as Dawn Chamberlain on the television series \"The Secret Circle\".\n\nYoung Avengers: The Young Avengers is a fictional superhero team, appearing in American comic books published by Marvel Comics.  The team, created by Allan Heinberg and Jim Cheung, features numerous adolescent characters who typically have connections to established members of Marvel's primary superhero team, the Avengers.  The Young Avengers originally featured in a twelve issue run, later appearing in several notable Marvel crossover series, including the \"Civil War\" and \"\" events, before the series was relaunched in January 2013 as part of the Marvel NOW!  rebranding by writer Kieron Gillen and artist Jamie McKelvie.\n\nTara King: Tara King is a fictional character of British 1960s adventure television series \"The Avengers\", played by Canadian actress Linda Thorson.  Sixth partner of agent John Steed (and fourth female partner), she appeared in season six (in colour) of the series (1968–1969), playing in 33 episodes.  She is Emma Peel's successor.  She is also the first of John Steed's partners to be a real spy.  Viewers are not given any indication whether or not she is related to Dr. Martin King played by Jon Rollason one of Steed's partners from series 2.\n\nLinda Thorson: Linda Thorson (born Linda Robinson on 18 June 1947) is a Canadian actress, best known for playing Tara King in \"The Avengers\" (1968–69).  For her role in \"The Avengers\", Thorson received a special BAFTA at the 2000 BAFTA TV Awards along with the other three actresses from the series, Honor Blackman, Joanna Lumley and Diana Rigg.\n\nLisa Marcos: Lisa Marcos (born March 15, 1982) is a Canadian actress and former model.  She began her career as a model at the age of 14 years, but after 8 years as a model, she decided to pursue her passion for acting.  She knocked on the door of a talent agent.  Soon after her acting career began in 2002 with a guest role on \"Soul Food\".  She is best known as Charlie Marks in the television series \"The Listener\".\n\nThe Infinity War: The Infinity War is a six-issue comic book limited series published by Marvel Comics in 1992.  The series was written by Jim Starlin and penciled by Ron Lim, Ian Laughlin, Al Milgrom, Jack Morelli and Christie Scheele.\n\nAvengers vs. X-Men: Avengers vs. X-Men (abbreviated AvX and AvsX) is a 2012 crossover event that was featured in comic books published by Marvel Comics.  The event, consisting of an eponymous limited series and numerous tie-in books, involves the return of the Phoenix Force and the subsequent war between the Avengers and the X-Men.  The 12-issue twice-monthly series was first published in April 2012, and features a storyline by Jason Aaron, Brian Michael Bendis, Ed Brubaker, Jonathan Hickman and Matt Fraction, with a rotating team of artists including John Romita, Jr., Olivier Coipel and Adam Kubert.\n\nCobie Smulders: Jacoba Francisca Maria \"Cobie\" Smulders (born April 3, 1982) is a Canadian actress and model.  She is best known for her roles as Robin Scherbatsky on the television series \"How I Met Your Mother\" (2005–2014) and Maria Hill in the Marvel Cinematic Universe.\n\nAvengers: Infinity War: Avengers: Infinity War is an upcoming American superhero film based on the Marvel Comics superhero team the Avengers, produced by Marvel Studios and distributed by Walt Disney Studios Motion Pictures.  It is intended to be the sequel to 2012's \"Marvel's The Avengers\" and 2015's \"\" and the nineteenth film installment in the Marvel Cinematic Universe (MCU).  The film is directed by Anthony and Joe Russo, with a screenplay by Christopher Markus & Stephen McFeely, and features an ensemble cast that includes Robert Downey Jr., Josh Brolin, Mark Ruffalo, Tom Hiddleston, Chris Evans, Chris Hemsworth, Jeremy Renner, Chris Pratt, Elizabeth Olsen, Sebastian Stan, Benedict Cumberbatch, Paul Bettany, Cobie Smulders, Benedict Wong, Zoe Saldana, Karen Gillan, Vin Diesel, Dave Bautista, Bradley Cooper, Pom Klementieff, Scarlett Johansson, Benicio del Toro, Tom Holland, Anthony Mackie, Chadwick Boseman, Danai Gurira, Paul Rudd, and Don Cheadle.  In \"Avengers: Infinity War\", the Avengers join forces with the Guardians of the Galaxy to confront Thanos, who is trying to amass the Infinity Stones.\n\nQuestion: Avengers: Infinity War featured which Canadian actress and model?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actress_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the Canadian actress and model.\"\n    },\n    \"actress_nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the actress.\"\n    },\n    \"actress_professions\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of professions of the actress.\"\n    },\n    \"movie_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film in which the actress was featured.\"\n    },\n    \"character_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the character played by the actress in the Marvel Cinematic Universe.\"\n    }\n  },\n  \"required\": [\n    \"actress_name\",\n    \"actress_nationality\",\n    \"actress_professions\",\n    \"movie_title\",\n    \"character_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actress_name": {
        "type": "string",
        "description": "The full name of the Canadian actress and model."
      },
      "actress_nationality": {
        "type": "string",
        "description": "The nationality of the actress."
      },
      "actress_professions": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of professions of the actress."
      },
      "movie_title": {
        "type": "string",
        "description": "The title of the film in which the actress was featured."
      },
      "character_name": {
        "type": "string",
        "description": "The name of the character played by the actress in the Marvel Cinematic Universe."
      }
    },
    "required": [
      "actress_name",
      "actress_nationality",
      "actress_professions",
      "movie_title",
      "character_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
