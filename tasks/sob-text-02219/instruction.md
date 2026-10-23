{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGary Alexander (sound engineer): Gary Alexander is an American sound engineer.  He won the Academy Award for Best Sound for the film \"Out of Africa\".  He worked on over 300 films from 1976 to 2011.\n\nAlexander Neville (scholar): Alexander Neville (1544–1614) was an English scholar, known as a historian and translator and a Member of the House of Commons.\n\nAlexander Neville: Alexander Neville (c. 1340–1392) was a late medieval prelate who served as Archbishop of York from 1374 to 1388.\n\nSalford City F.C.: Salford City Football Club is a professional football club in the Kersal area of Salford, Greater Manchester, England, which plays in National League North, the sixth tier of English football.\n\nMartin Hinshelwood: Martin Hinshelwood (born 16 June 1953) is an English former professional footballer and football club coach and manager.  He is currently an academy coach at Lewes and was Interim Manager at Crawley Town F.C. alongside Gary Alexander, following the sacking of manager Richie Barker.\n\nGary Alexander (martial art pioneer): Gary Alexander is an American martial artist, karate fighter, author and actor.  He was Black Belt Magazine's Co-Instructor of the Year (1974) and is known as the \"First International Bare Knuckle Contact Karate Champion.\n\nAlexander Neville (disambiguation): Alexander Neville was a bishop.\n\nGary Loizzo: Gary Alexander Loizzo (August 16, 1945 – January 16, 2016) was an American guitarist, singer, recording engineer, and record producer.  He is best known for being the lead singer with The American Breed.\n\nGary Goldstone: Gary Alexander Goldstone (born 27 July 1976 in Durban, KwaZulu-Natal) is a South African football (soccer) defender for Premier Soccer League club Bloemfontein Celtic.\n\nGary Neville: Gary Alexander Neville (born 18 February 1975) is an English football coach and former player who until recently served as assistant manager for the England national football team, and as co-owner of Salford City.  Since retiring from football in 2011, Neville went into punditry and was a commentator for Sky Sports until he took over the head coach position at Valencia.  After being sacked by the club in 2016, he returned to his position as a pundit for Sky Sports later that year.\n\nQuestion: In what area of Salford is the club Gary Alexander Neville co-owns located?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"club_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the football club.\"\n    },\n    \"co_owner_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the co-owner of the club.\"\n    },\n    \"club_location\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"area\": {\n          \"type\": \"string\",\n          \"description\": \"The specific area within the city where the club is located.\"\n        },\n        \"city\": {\n          \"type\": \"string\",\n          \"description\": \"The city where the club is located.\"\n        },\n        \"region\": {\n          \"type\": \"string\",\n          \"description\": \"The greater region or county where the club is located.\"\n        },\n        \"country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the club is located.\"\n        }\n      },\n      \"required\": [\n        \"area\",\n        \"city\",\n        \"region\",\n        \"country\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"club_name\",\n    \"co_owner_name\",\n    \"club_location\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "club_name": {
        "type": "string",
        "description": "The name of the football club."
      },
      "co_owner_name": {
        "type": "string",
        "description": "The name of the co-owner of the club."
      },
      "club_location": {
        "type": "object",
        "properties": {
          "area": {
            "type": "string",
            "description": "The specific area within the city where the club is located."
          },
          "city": {
            "type": "string",
            "description": "The city where the club is located."
          },
          "region": {
            "type": "string",
            "description": "The greater region or county where the club is located."
          },
          "country": {
            "type": "string",
            "description": "The country where the club is located."
          }
        },
        "required": [
          "area",
          "city",
          "region",
          "country"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "club_name",
      "co_owner_name",
      "club_location"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
