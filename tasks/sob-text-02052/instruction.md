{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Stars Are Ours!: The Stars Are Ours!  is a 1954 science fiction novel by American writer Andre Norton.  It describes the first interstellar voyage, undertaken to escape the tyranny that rules the Earth.  Norton wrote a sequel, \"Star Born\", which was published in 1957.\n\nThe Choice (2016 film): The Choice is a 2016 American romantic drama film directed by Ross Katz and written by Bryan Sipe, based on Nicholas Sparks' 2007 novel of the same name about two neighbors who fall in love at their first meeting.  The movie stars Benjamin Walker, Teresa Palmer, Maggie Grace, Alexandra Daddario, Tom Welling and Tom Wilkinson.\n\nMarta Ribera: Marta Ribera is a Spanish theatrical actress star born in 1971.  She is perhaps best known for her roles in the Frank Wildhorn musical Jekyll & Hyde (musical) in the starring role of Lucy Harris and her most recent role as The Lady of the Lake in Monty Python's Spamalot.  She has also appeared as Sally Bowles in Cabaret (musical), amongst other roles.\n\nRené Pedroli: René Pedroli (Montignies-sur-Sambre, Belgium, 19 July 1914 — Charleroi, Belgium, 17 July 1986) was a Swiss professional road bicycle racer.  Although Pedroli was born and raised in Belgium, his parents were of Swiss nationality, and so was Pedroli.  Pedroli was the winner of stage 12B in the 1937 Tour de France.\n\nColin Kazim-Richards: Colin Kazim-Richards (born 26 August 1986), also known as Colin Kâzım, Kâzım or Kâzım Kâzım, is a professional footballer who plays as a forward for Corinthians and internationally for the Turkey national team.  Born and raised in England, he qualified for Turkish nationality through his mother's heritage.  An anglicised form of the Turkish given name Kâzım was intended to be a middle name, which would have rendered his full name as Colin-Kazim Richards, but due to an error, he was legally registered as Colin Kazim-Richards.\n\nConstance Talmadge: Constance Alice Talmadge (April 19, 1898 – November 23, 1973) was an American silent movie star born in Brooklyn, New York.  She was the sister of actresses Norma and Natalie Talmadge.\n\nRomain Grosjean: Romain Grosjean (] ; born 17 April 1986) is a racing driver, currently racing for the Haas F1 Team.  He races under the French flag in Formula One although he was born in Geneva and holds dual Franco-Swiss nationality.\n\nStar Born: Star Born is a science fiction novel by American writer Andre Norton, first published in 1957 by World Publishing Company of Cleveland.  This is the sequel to \"The Stars Are Ours! \" and continues that adventure three generations on.\n\nGaylord Silly: Gaylord Lucien D. Silly (] ; born 20 February 1986) is a French-Seychellois long distance runner who represents Seychelles internationally.  Born in Vendôme, France, to a Seychelloise mother and a French father, he holds dual nationality.\n\nTeresa Palmer: Teresa Mary Palmer (born 26 February 1986) is an Australian actress, writer, producer and model.  Palmer made her film debut in 2006, when she appeared in the suicide drama \".\"  In 2013, she played the leading role in the zombie romantic comedy \"Warm Bodies\"; later on, Palmer portrayed the fictional character of Rebecca in the 2016 supernatural horror film \"Lights Out\".  She has also appeared in films such as \"December Boys\", \"The Sorcerer's Apprentice\", \"I Am Number Four\", \"Take Me Home Tonight\", \"Love and Honor\", \"The Ever After\" (which she co-wrote and co-produced with her husband, Mark Webber), \"Kill Me Three Times\", the 2015 remake of \"Point Break\", \"Triple 9\", \"The Choice\", and the Mel Gibson-directed war film \"Hacksaw Ridge\".\n\nQuestion: What is the nationality of \"The choice\" star born in 1986 ?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"movie_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film mentioned in the question.\"\n    },\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor who starred in the film and was born in the specified year.\"\n    },\n    \"birth_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth year of the identified actor.\"\n    },\n    \"nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the identified actor.\"\n    }\n  },\n  \"required\": [\n    \"movie_title\",\n    \"actor_name\",\n    \"birth_year\",\n    \"nationality\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "movie_title": {
        "type": "string",
        "description": "The title of the film mentioned in the question."
      },
      "actor_name": {
        "type": "string",
        "description": "The name of the actor who starred in the film and was born in the specified year."
      },
      "birth_year": {
        "type": "integer",
        "description": "The birth year of the identified actor."
      },
      "nationality": {
        "type": "string",
        "description": "The nationality of the identified actor."
      }
    },
    "required": [
      "movie_title",
      "actor_name",
      "birth_year",
      "nationality"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
