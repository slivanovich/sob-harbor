{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nZ. Z. Hill: Arzell J. Hill (September 30, 1935 – April 27, 1984), known as Z. Z. Hill (pronounced \"Zee Zee\"), was an American blues singer best known for his recordings in the 1970s and early 1980s, including his 1982 album for Malaco Records, \"Down Home\", which stayed on the Billboard soul album chart for nearly two years.  The track \"Down Home Blues\" has been called the best-known blues song of the 1980s.  According to the Texas State Historical Association, Hill \"devised a combination of blues and contemporary soul styling and helped to restore the blues to modern black consciousness.\"\n\nTow Law: Tow Law is a town and civil parish in County Durham, England.  According to the 2001 census it had a population of 1,952, increasing to 2,138 at the 2011 Census.  It is situated a few miles to the south of Consett.  Tow Law Town football team are based in the town.  The town constituted an urban district from 1894 until 1974.  The town is mentioned in the Mark Knopfler song \"Hill Farmer's Blues\" from his album \"The Ragpicker's Dream\".\n\nPhilip Trevelyan: Philip Erasmus Trevelyan (born 22 August 1943) is a British organic hill farmer, entrepreneur and former film and television director, most noted for the 1971 documentary film \"The Moon and the Sledgehammer\".\n\nBill Dillard: Bill Dillard (born July 20, 1911 – 1995) was an American swing music jazz trumpeter, actor and singer born in Pennsylvania, probably better known for his work with the big bands of Benny Carter, Luis Russell and Teddy Hill, among others.  He also had an acting career on Broadway.\n\nGeorges Dimou: Georges Dimou (Greek: Γιώργος Δήμου ; born 1931) is a Greek singer born in Thessaloniki.  He studied dramatic and vocal art in Athens and from the beginning he was successful as actor and singer with international repertoire.\n\nMounira El Mahdeya: Mounira El Mahdeya (born Zakiyya Hassan) (Arabic: منيرة المهدية‎ ‎ ) was an Egyptian singer born in 1885 in Alexandria; she died in 1965.  The singer, better known under the nickname of \"Sultana of the song\" or \"The Sultana\", was considered to be the leading Egyptian singer between the two wars.\n\nDiana Trask: Diana Trask (born 23 June 1940) is an Australian country and pop singer born in Melbourne, Australia.  She was a popular country singer during the 1970s in the United States and also was a popular star in her native Australia.  In the U.S., she charted eighteen singles on the country charts, of which the highest was the number 13 \"Lean It All on Me\" in 1974.\n\nMark Knopfler: Mark Freuder Knopfler, {'1': \", '2': \", '3': \", '4': \"} (born 12 August 1949) is a British singer-songwriter, guitarist, record producer and film score composer.  He was born in Glasgow but raised near Newcastle upon Tyne, England.  He is best known for having been the lead guitarist, lead singer and songwriter for the rock band Dire Straits, which he co-founded with his younger brother, David Knopfler, in 1977.\n\nKing Cotton (performer): King Cotton is the stage name of Dicky Sony, a Texas blues singer born in 1945 in Navasota, Texas.  He was the lead vocalist and founding member of the blues/rock band Navasota in 1969.\n\nKiki Dee: Pauline Matthews (born 6 March 1947), better known by her stage name Kiki Dee, is an English singer born in Little Horton, Bradford, West Riding of Yorkshire.  Known for her blue-eyed soul vocals, she was the first female singer from the UK to sign with Motown's Tamla Records.\n\nQuestion: Where was \"Hill Farmer's Blues\" singer born? \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"song_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the song mentioned in the question.\"\n    },\n    \"artist_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the artist who performed the song.\"\n        },\n        \"birth_location\": {\n          \"type\": \"string\",\n          \"description\": \"The city where the artist was born.\"\n        },\n        \"birth_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the artist was born.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"birth_location\",\n        \"birth_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"artist_role\": {\n      \"type\": \"string\",\n      \"description\": \"The role of the artist in relation to the song (e.g., singer, songwriter).\"\n    }\n  },\n  \"required\": [\n    \"song_title\",\n    \"artist_details\",\n    \"artist_role\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "song_title": {
        "type": "string",
        "description": "The title of the song mentioned in the question."
      },
      "artist_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the artist who performed the song."
          },
          "birth_location": {
            "type": "string",
            "description": "The city where the artist was born."
          },
          "birth_year": {
            "type": "integer",
            "description": "The year the artist was born."
          }
        },
        "required": [
          "name",
          "birth_location",
          "birth_year"
        ],
        "additionalProperties": false
      },
      "artist_role": {
        "type": "string",
        "description": "The role of the artist in relation to the song (e.g., singer, songwriter)."
      }
    },
    "required": [
      "song_title",
      "artist_details",
      "artist_role"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
