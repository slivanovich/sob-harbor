{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDermot Murnaghan: Dermot Murnaghan (born 26 December 1957) is a British broadcaster.  A presenter for Sky News, he was a news presenter at CNBC Europe, Independent Television News and BBC News.  He has presented news programmes in a variety of time slots since joining Sky News in 2007.\n\nJames Burke (science historian): James Burke (born 22 December 1936) is a British broadcaster, science historian, author, and television producer, who is known, among other things, for his documentary television series \"Connections\" (1978), and for its more philosophically oriented companion series, \"The Day the Universe Changed\" (1985), which is about the history of science and technology.  \"The Washington Post\" called him \"one of the most intriguing minds in the Western world\".\n\nIn Search of the Pope's Children: In Search of the Pope's Children is an Irish television programme based on the book \"The Pope's Children\", aired by the state broadcaster RTÉ and British broadcaster BBC Four.  The programme is a three-part true lives documentary, presented by economist David McWilliams.  The show comments on the Irish economy and the social attitudes surrounding it.  The show is marketed as being sharp, witty and argumentative.\n\nJoan Shenton: Joan Alicia Shenton (born 16 March 1943) is a British broadcaster who has produced and presented programmes for network radio and television over a period of 50 years.\n\nAlex Lester: Alex Lester (born Alexander Norman Charles Lester; 11 May 1956 in Walsall, England) is a British broadcaster.  He presented the weekday overnight/early-morning programme on BBC Radio 2 from 1990 until 2014.  From October 2014 until January 2017, he presented the midnight to 3.00am programme every Friday, Saturday and Sunday.  He also temporarily replaced Russell Brand on Saturday evenings in late 2008, between 9 and 11pm, following Brand's resignation over his infamous prank calls row.\n\nLee McKenzie (male sports broadcaster): Lee McKenzie is a British broadcaster who specialises in sport.  He has worked for BBC TV and Radio and Sky Sports.  From June 2001 for two years he was the BBC's full-time radio horse racing commentator, succeeding Peter Bromley.  McKenzie has presented the daily sports round-up on BBC South on the weekday evening BBC South Today programme, and the Saturday afternoon show \"Sportstime\" on BBC Radio Solent.  On the same radio station, he co-hosted the Sunday morning music and phone-in show \"Sunday Scene\".\n\nBox for One: Box for One is a live television play which has been presented three times, twice on British broadcaster BBC and once on Australian broadcaster ABC.  It is a drama about a \"spiv\", and the entire 30-minute drama takes place in a London telephone box.  It was written by Peter Brook.\n\nConnections (TV series): Connections is a 10-episode documentary television series and 1978 book (\"Connections\", based on the series) created, written, and presented by science historian James Burke.  The series was produced and directed by Mick Jackson of the BBC Science and Features Department and first aired in 1978 (UK) and 1979 (USA).  It took an interdisciplinary approach to the history of science and invention, and demonstrated how various discoveries, scientific achievements, and historical world events were built from one another successively in an interconnected way to bring about particular aspects of modern technology.  The series was noted for Burke's crisp and enthusiastic presentation (and dry humour), historical re-enactments, and intricate working models.\n\nThe Naked Pilgrim: The Naked Pilgrim is documentary series produced by British broadcaster Five and presented by art critic Brian Sewell.  First broadcast in 2003, the series follows Sewell on the Catholic pilgrimage to Santiago de Compostela.\n\nHunted (2012 TV series): Hunted is a 2012 British television drama series created and written by Frank Spotnitz and produced by Kudos Film and Television and Big Light Productions for British broadcaster BBC, for its main channel BBC One and American premium cable broadcaster Cinemax.  The series premiered on Thursday 4 October 2012 on BBC One and on Friday 19 October 2012 on Cinemax.\n\nQuestion: Connections is presented by which British broadcaster and historian?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"presenter_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person who presented the series.\"\n    },\n    \"presenter_nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the presenter.\"\n    },\n    \"presenter_professions\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of professions held by the presenter, as described in the context.\"\n    },\n    \"series_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the television series.\"\n    },\n    \"series_first_broadcast_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the series was first aired.\"\n    }\n  },\n  \"required\": [\n    \"presenter_name\",\n    \"presenter_nationality\",\n    \"presenter_professions\",\n    \"series_title\",\n    \"series_first_broadcast_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "presenter_name": {
        "type": "string",
        "description": "The name of the person who presented the series."
      },
      "presenter_nationality": {
        "type": "string",
        "description": "The nationality of the presenter."
      },
      "presenter_professions": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of professions held by the presenter, as described in the context."
      },
      "series_title": {
        "type": "string",
        "description": "The title of the television series."
      },
      "series_first_broadcast_year": {
        "type": "integer",
        "description": "The year the series was first aired."
      }
    },
    "required": [
      "presenter_name",
      "presenter_nationality",
      "presenter_professions",
      "series_title",
      "series_first_broadcast_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
