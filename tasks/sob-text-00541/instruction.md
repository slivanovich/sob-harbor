{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDi'Anno: Di'Anno was a band featuring former Iron Maiden singer Paul Di'Anno, whom the band was named after.\n\nCSN (album): CSN is the third studio album by Crosby, Stills & Nash released in 1977.  It is the second release by the trio configuration and the first without Neil Young since his entry into the band.  It peaked at #2 on the \"Billboard\" Top Pop Albums chart; two singles taken from the album, Nash's \"Just a Song Before I Go\" and Stills' \"Fair Game\" peaked at #7 and #43 respectively on the \"Billboard\" Hot 100.  It is currently the trio configuration's best selling record, outselling 1969's \"Crosby, Stills & Nash\" by 200,000 copies.  It has been certified quadruple platinum by RIAA.\n\nPieces (Manassas album): Pieces is a compilation of alternate takes and outtakes by Stephen Stills’s band Manassas released in 2009.\n\nVoKee: VoKee is an alternative rock, California-based band featuring former Apex Theory vocalist and ex-System of a Down drummer, Ontronik (formerly known by the nickname \"Andy\").\n\nCrosby, Stills, Nash &amp; Young discography: The core discography of American/British/Canadian supergroup Crosby, Stills, Nash & Young consists of eight studio albums, five live albums, six compilation albums, four video albums, and nineteen singles.  Originally formed in 1968, the group released one album as the trio Crosby, Stills & Nash before recruiting Neil Young into the band for their first concerts in 1969.  Of the band's eight studio albums, three have also included Young; and of the group's numerous tours, the quartet configuration has made concert tours in 1970, 1974, 2000, 2002, and 2006.\n\nLynch Mob (band): Lynch Mob is an American hard rock band featuring former Dokken guitarist George Lynch, who has been the band's only permanent member.\n\nSo Far (album): So Far is the fourth album by Crosby, Stills & Nash, their third as Crosby, Stills, Nash & Young, and the first compilation album released by the group.  Shipping as a gold record and peaking at #1 on the \"Billboard\" Top Pop Albums chart, it was the band's third chart-topping album in a row.  It has been certified six times platinum by the RIAA.\n\nStephen Stills: Stephen Arthur Stills (born January 3, 1945) is an American singer and multi-instrumentalist best known for his work with Buffalo Springfield and Crosby, Stills, Nash & Young.\n\nThe Cobra (novel): The Cobra is a 2010 thriller novel by Frederick Forsyth about the international cocaine trade.  In it an unnamed Obama-like (said to have a wife named 'Michelle' and a deceased Kenyan father) U.S. president colludes with an unnamed Cameron-like (having a wife named 'Sam') U.K. Prime Minister to put an end to the international cocaine trade and brings in ex-CIA director Paul Devereaux who is basically given carte blanche to accomplish this task by any means necessary.  The book re-introduces some of the characters from Forsyth's book \"Avenger\".\n\n7 Walkers: 7 Walkers was an American rock band featuring former Grateful Dead drummer Bill Kreutzmann, guitarist Papa Mali, multi-instrumentalist Matt Hubbard and bassist George Porter, Jr.\n\nQuestion: What is the name of the band featuring former Crosby, Still, Nash & Young singer who put out a compilation named 'Pieces'?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"band_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the band that released the album.\"\n    },\n    \"featured_member\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"member_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the member who was formerly in Crosby, Stills, Nash & Young.\"\n        },\n        \"previous_band_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the member's previous band.\"\n        }\n      },\n      \"required\": [\n        \"member_name\",\n        \"previous_band_name\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"album_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"album_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the album released by the band.\"\n        },\n        \"album_type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of the album (e.g., compilation, studio album).\"\n        }\n      },\n      \"required\": [\n        \"album_title\",\n        \"album_type\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"band_name\",\n    \"featured_member\",\n    \"album_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "band_name": {
        "type": "string",
        "description": "The name of the band that released the album."
      },
      "featured_member": {
        "type": "object",
        "properties": {
          "member_name": {
            "type": "string",
            "description": "The name of the member who was formerly in Crosby, Stills, Nash & Young."
          },
          "previous_band_name": {
            "type": "string",
            "description": "The name of the member's previous band."
          }
        },
        "required": [
          "member_name",
          "previous_band_name"
        ],
        "additionalProperties": false
      },
      "album_details": {
        "type": "object",
        "properties": {
          "album_title": {
            "type": "string",
            "description": "The title of the album released by the band."
          },
          "album_type": {
            "type": "string",
            "description": "The type of the album (e.g., compilation, studio album)."
          }
        },
        "required": [
          "album_title",
          "album_type"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "band_name",
      "featured_member",
      "album_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
