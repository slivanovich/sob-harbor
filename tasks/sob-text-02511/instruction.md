{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJason Alexander: Jason Scott Greenspan (born September 23, 1959), known by his stage name Jason Alexander, is an American actor, voice actor, comedian and director.\n\nGet Lamp: Get Lamp is a two-disc documentary about interactive fiction (a genre that includes text adventures) filmed by computer historian Jason Scott of textfiles.com.  Scott conducted the interviews between February 2006 and February 2008, and the documentary was released in July 2010.\n\nJason Scott: Jason Scott Sadofsky (born September 13, 1970), more commonly known as Jason Scott, is an American archivist, historian of technology, and filmmaker.  Scott has been known by the online pseudonyms \"Sketch,\" \"SketchCow,\" and \"The Slipped Disk.\"\n\nJason Merrells: Jason Scott Merrells (born 2 November 1968 in Epping, Essex) is an English actor, who is best known for his roles as receptionist Matt Hawley in \"Casualty\", stylist Gavin Ferraday in \"Cutting It\", Head Teacher Jack Rimmer in \"Waterloo Road\" and Home Farm's owner Declan Macey in \"Emmerdale\".  More recently Jason plays the role of David in ITV's Safe House\n\nSoldier (1998 American film): Soldier is a 1998 American science fiction action film directed by Paul W. S. Anderson, written by David Webb Peoples, and starring Kurt Russell, Jason Scott Lee, Jason Isaacs, Connie Nielsen, Sean Pertwee and Gary Busey.  The film tells the story of a highly skilled genetically advanced soldier defying his commanders and facing a relentless and brutal rival soldier.\n\nCedartown, Georgia: Cedartown is a city in Polk County, Georgia, United States.  As of the 2010 census, the city had a population of 9,750.  The city is the county seat of Polk County.  Cedartown is the principal city of and is included in the Cedartown, Georgia Micropolitan Statistical Area, which is included in the Atlanta-Sandy Springs-Gainesville, Georgia-Alabama (part) Combined Statistical Area.\n\nDracula III: Legacy: Dracula III: Legacy is a 2005 horror film and the sequel to \"Dracula 2000\" and \"\".  The film was directed by Patrick Lussier and stars Jason Scott Lee, Jason London, Roy Scheider, and Diane Neal.  It was released direct-to-video on July 12, 2005.\n\nJason Floros: Jason Scott Floros (born 24 November 1990 in Woden Valley, Australian Capital Territory) is an Australian cricketer.  He currently plays for Queensland in the Sheffield Shield and Ryobi One Day Cup, and for the Brisbane Heat in the Big Bash League.  He is of Greek descendant.  He is the son of a Greek father and Australian mother.\n\nJason Wilkes (musician): Jason Scott Wilkes (born September 12, 1984), better known as Jason Wilkes, was born in Cedartown, Georgia, United States.  He is a musician, singer and songwriter in the genre of Christian rock.  He is currently the lead vocalist of his own solo venture, WILKES.\n\nJason Scott case: The Jason Scott case was a United States civil suit, brought against deprogrammer Rick Ross, two of his associates, and the Cult Awareness Network (CAN), for the abduction and failed deprogramming of Jason Scott, a member of a Pentecostalist church.  Scott was eighteen years old at the time of the abduction and thus legally an adult.  CAN was a co-defendant because a CAN contact person had referred Scott's mother to Rick Ross.  In the trial, Jason Scott was represented by Kendrick Moxon, a prominent Scientologist attorney.\n\nQuestion: In which county was Jason Scott Wilkes born?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the person.\"\n    },\n    \"birth_city\": {\n      \"type\": \"string\",\n      \"description\": \"The city where the person was born.\"\n    },\n    \"birth_state\": {\n      \"type\": \"string\",\n      \"description\": \"The state where the person was born.\"\n    },\n    \"birth_county\": {\n      \"type\": \"string\",\n      \"description\": \"The county where the person was born.\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"birth_city\",\n    \"birth_state\",\n    \"birth_county\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The full name of the person."
      },
      "birth_city": {
        "type": "string",
        "description": "The city where the person was born."
      },
      "birth_state": {
        "type": "string",
        "description": "The state where the person was born."
      },
      "birth_county": {
        "type": "string",
        "description": "The county where the person was born."
      }
    },
    "required": [
      "person_name",
      "birth_city",
      "birth_state",
      "birth_county"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
