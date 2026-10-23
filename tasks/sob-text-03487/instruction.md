{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nIronclad (film): Ironclad is a 2011 action adventure war film directed by Jonathan English.  Written by English and Erick Kastel, based on a screenplay by Stephen McDool, the cast includes James Purefoy, Brian Cox, Kate Mara, Paul Giamatti, Vladimir Kulich, Mackenzie Crook, Jason Flemyng, Derek Jacobi and Charles Dance.  The film chronicles the siege of Rochester Castle by King John in 1215.  The film was shot entirely in Wales in 2009 and produced on a budget of $25 million.\n\nPintel and Ragetti: Pintel and Ragetti are recurring characters in the \"Pirates of the Caribbean\" film series, primarily providing comic relief throughout each film.  Pintel is portrayed by Lee Arenberg and Mackenzie Crook portrays Ragetti.\n\nMackenzie Crook: Paul James \"Mackenzie\" Crook (born 29 September 1971) is an English actor, director, comedian and BAFTA-winning writer.  He is best known for playing Gareth Keenan in \"The Office\", Ragetti in the \"Pirates of the Caribbean\" films, and Orell in the HBO series \"Game of Thrones\", and is the creator and star of BBC Four's \"Detectorists\".\n\nMonkey Trousers: Monkey Trousers is a television comedy series on ITV first broadcast in 2005, featuring Alistair McGowan, John Thomson, Ronni Ancona, Mackenzie Crook, Griff Rhys Jones, Neil Morrissey, Vic Reeves, Bob Mortimer, Marc Wootton and Steve Coogan.  It is directed by David Kerr and produced by Bob Mortimer and Vic Reeves' production company, Pett Productions.\n\nThe Office Christmas specials: \"The Office\" Christmas Specials are the two-part final episode of the British mockumentary comedy television series \"The Office\".  The specials were commissioned after the series' creators, Ricky Gervais and Stephen Merchant, announced that they would not write a full third series of the show.  The first 45-minute part was broadcast on BBC One on 26 December 2003, and the second 50-minute part was shown the following evening.  The episodes are presented in the style of \"revisited\" documentaries common on British television, in which popular \"docusoaps\" (e.g. \"Airport\"), are brought back for one-off specials several years after the series concluded.  David Brent (Gervais), forcibly made redundant at the end of the second series, is now a travelling salesman of cleaning supplies.  Tim Canterbury (Martin Freeman) and Gareth Keenan (Mackenzie Crook) are still working at the offices of Wernham Hogg, and former Wernham Hogg receptionist Dawn Tinsley (Lucy Davis) now lives in Florida, though is flown back to Britain by the documentary crew to reunite with her old colleagues.\n\nCity of Ember: City of Ember is a 2008 American science fantasy film based on the 2003 novel \"The City of Ember\" by Jeanne DuPrau.  It was produced by Walden Media, Playtone, Seth Hanchett, Gary Goetzman, Tom Hanks and Steven Shareshian, directed by Gil Kenan, distributed by 20th Century Fox, written by Caroline Thompson with music by Andrew Lockington and stars Saoirse Ronan, Harry Treadaway, Bill Murray, Mackenzie Crook, Martin Landau, Mary Kay Place, Toby Jones and Tim Robbins.  It was theatrically released in October 10, 2008 by 20th Century Fox, just two months after the release of the final book in the series; \"The Diamond of Darkhold\".  The film received mixed reviews from critics and was a box office flop.\n\nCarl Prekopp: Carl James Prekopp (born Sheffield, 1979) is a British actor.  He played Richard III at the Riverside Studios (2010) and originated the part of Lawrence in Tim Firth's stage adaptation of \"Calendar Girls\".  He has appeared in BBC Radio 4 adaptations of Terry Pratchett's \"Mort\" (as the title character), \"Small Gods\" (as Brutha) and \"Night Watch\" (as young Sam Vimes).  He was also a supporting actor in the 2007 British feature film \"I Want Candy\" with Mackenzie Crook, He directed the Afternoon Play \"Taken\" by Suzanne Heathcote for BBC Radio 4, and is a singer/songwriter and founding member of folk/rock band The Fircones featuring The Likely Lads actress Brigit Forsyth on Cello.  .  In 2015-2016, Prekopp appeared as William III of England and Daniel Defoe in the Royal Shakespeare Company's production of Helen Edmundson's \"Queen Anne\".\n\nDark Ascension (film): Dark Ascension is an upcoming action/fantasy film directed by Gene Fallaize, executive produced by Scott Spiegel, and starring Tara Reid, Brian Blessed, Paul Blackthorne, and Jillian Murray, along with Sean Young, Mackenzie Crook, Tony Cook and Serena Lorien.\n\nPirates of the Caribbean (film series): Pirates of the Caribbean is a series of American fantasy swashbuckler films produced by Jerry Bruckheimer and based on Walt Disney's theme park ride of the same name.\n\nGareth Keenan: Gareth Keenan is a fictional paper salesman on BBC's comedy \"The Office\".  He is portrayed in the series by Mackenzie Crook as a gaunt, self-important team leader proud of his alleged lieutenant status in the Territorial Army.  He spends his days annoying his co-workers at Wernham Hogg with his steadfast enforcement of the rules and sycophantic attitudes towards David Brent, whom he views as a friend.  Despite this, Brent often acts otherwise and corrects Keenan when he omits the \"to the\" in his job title: \"Assistant \"to the\" Regional Manager\".  His counterpart on the US series is Dwight Schrute.  The character was originally meant to be a tough and fierce character in the mockumentary, but after Mackenzie Crook's audition, Ricky Gervais and Steven Merchant had to change his lines to fit his new personality\n\nQuestion: Who produced the film series in which Mackenzie Crook played Ragetti?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor.\"\n    },\n    \"character_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the character played by the actor.\"\n    },\n    \"film_series_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the film series.\"\n    },\n    \"producer_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the producer of the film series.\"\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"character_name\",\n    \"film_series_name\",\n    \"producer_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The name of the actor."
      },
      "character_name": {
        "type": "string",
        "description": "The name of the character played by the actor."
      },
      "film_series_name": {
        "type": "string",
        "description": "The name of the film series."
      },
      "producer_name": {
        "type": "string",
        "description": "The name of the producer of the film series."
      }
    },
    "required": [
      "actor_name",
      "character_name",
      "film_series_name",
      "producer_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
