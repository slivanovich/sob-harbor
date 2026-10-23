{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCopenhagen Open: The Copenhagen Open was a tennis tournament on the World Championship Tennis (WCT) circuit and ATP Tour.  It was first held in February 1973 as part of the WCT tour and featured renowned players such as Ken Rosewall, Fred Stolle, Arthur Ashe and Tom Okker.  It was played indoors on a carpet surface.\n\nNenad Zimonjić: Nenad Zimonjić (Serbian Cyrillic: , ] ; born June 4, 1976) is a Serbian professional tennis player who was ranked World No. 1 in 2008 in doubles.  He is the second tennis doubles player from Serbia to hold the World No. 1, after Slobodan Živojinović.  While Zimonjić is known as a doubles specialist (winning 3 Grand Slams in men's doubles and 5 in mixed doubles), he has recorded two big wins in his singles career.  A 22 year span consisting of 54 Davis Cup ties including 43 victories has resulted in him becoming the most accomplished Davis Cup player in his nations history.  His strongest weapon is very powerful first serve that he can hit at up to 235 km/h (146 mph).\n\nFausto Gardini: Fausto Gardini (8 March 1930 – 17 September 2008) was an Italian tennis player.  He was an Italian Davis Cup player and later captain.  Gardini had long arms and legs, was renowned for keeping the ball in play and was very determined.  \"I could not help but admire Gardini because he always tried\" said Ken Rosewall.  This is how William McHale described Gardini \"A stringy, expressive, cavorting clown, Gardini uses the crowd as his personal cheering section\".  Gardini made his Grand Slam debut at Roland Garros in 1949, where he lost in round three to Eric Sturgess.  At Roland Garros in 1951, Gardini lost in the last 16 to Dick Savitt.  At Wimbledon Gardini beat Gardnar Mulloy before losing to Frank Sedgman in the last 16.  At Roland Garros in 1952, Gardini beat 17 year old Ken Rosewall and Tony Mottram before losing to Jaroslav Drobny in the last 16.  At Wimbledon he lost to Straight Clark in round three.  At the 1953 Australian championships, Gardini lost in round two to Ian Ayre.  At Roland Garros, Gardini reached the quarter finals before losing to Drobny.  At Wimbledon he lost in round one to Istvan Sikorski.  The highlight of Gardini's career was when he won the title at Rome in 1955, beating Herbert Flam, Enrique Morea and Giuseppe Merlo.  The final was a dramatic match.  Merlo led by 2 sets to 1 and had two championship points in the fourth set, but suffered from cramps and was forced to retire at 6-6 in the fourth set.  After that, Gardini played less and concentrated on running his family's bakery business.  By the early 1960s he was playing mainly in Italian tournaments and Davis Cup.\n\n1968 Men's National Tennis League: The 1968 Men's National Tennis League (NTL) was the inaugural series of professional tennis tournaments founded by George McCall, among others: Rod Laver, Roy Emerson, Ken Rosewall, Andrés Gimeno, Pancho Gonzales and Fred Stolle.\n\n1964 Australian Championships – Men's Singles: Roy Emerson defeated Fred Stolle 6–3, 6–4, 6-2 in the final to win the Men's Singles tennis title at the 1964 Australian Championships.\n\n2001 Canada Masters – Doubles: The 2001 Canada Masters – Doubles was the men's doubles event of the one hundred and twelfth edition of the Canada Masters; a WTA Tier I tournament and the most prestigious men's tennis tournament held in Canada.  Sébastien Lareau and Daniel Nestor were the defending champions but they competed with different partners that year, Lareau with Justin Gimelstob and Nestor with Sandon Stolle.  Gimelstob and Lareau lost in the first round to Mark Knowles and Brian MacPhie, as did Nestor and Stolle to Jan-Michael Gambill and Simon Larose.  Jiří Novák and David Rikl won in the final 6–4, 3–6, 6–3 against Donald Johnson and Jared Palmer.\n\n1965 Australian Championships – Men's Singles: Roy Emerson defeated Fred Stolle 7–9, 2–6, 6–4, 7–5, 6–1 in the final to win the Men's Singles tennis title at the 1965 Australian Championships.\n\nFred Stolle: Frederick Sydney Stolle, AO (born 8 October 1938) is an Australian former tennis player and commentator.  He was born in Hornsby, New South Wales, Australia.  He is the father of former Australian Davis Cup player Sandon Stolle.\n\nSandon Stolle: Sandon Stolle (born 13 July 1970) is a former professional male tennis player and at one time ranked No. 2 in World doubles.\n\nPieter Aldrich: Pieter (\"Piet\") Aldrich (born 7 September 1965) is a former professional tennis player from South Africa.  A doubles specialist, he won 2 Grand Slam men's doubles titles (1 Australian Open and 1 US Open).  Aldrich reached the World No. 1 doubles ranking in 1990.\n\nQuestion: Which tennis player, Pieter Aldrich or Fred Stolle,  is the father of former Australian Davis Cup player Sandon Stolle?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"father_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the father.\"\n    },\n    \"child_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the child.\"\n    },\n    \"child_description\": {\n      \"type\": \"string\",\n      \"description\": \"A description of the child's tennis career or role.\"\n    },\n    \"father_nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the father.\"\n    },\n    \"father_birth_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth year of the father.\"\n    }\n  },\n  \"required\": [\n    \"father_name\",\n    \"child_name\",\n    \"child_description\",\n    \"father_nationality\",\n    \"father_birth_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "father_name": {
        "type": "string",
        "description": "The full name of the father."
      },
      "child_name": {
        "type": "string",
        "description": "The full name of the child."
      },
      "child_description": {
        "type": "string",
        "description": "A description of the child's tennis career or role."
      },
      "father_nationality": {
        "type": "string",
        "description": "The nationality of the father."
      },
      "father_birth_year": {
        "type": "integer",
        "description": "The birth year of the father."
      }
    },
    "required": [
      "father_name",
      "child_name",
      "child_description",
      "father_nationality",
      "father_birth_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
