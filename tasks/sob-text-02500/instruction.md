{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Company of Snakes: The Company of Snakes were an English rock band formed in 1998, by former members of the English rock band Whitesnake who were also members of The Snakes.  They released two albums before morphing into M3 during 2004.\n\nMick Green: Michael Robert \"Mick\" Green (22 February 1944 – 11 January 2010) was an English rock and roll guitarist who played with The Pirates (with and without Johnny Kidd), Billy J. Kramer and the Dakotas, and Cliff Bennett and the Rebel Rousers.\n\nBilly J. Kramer: William Howard Ashton, (born 19 August 1943), better known by his stage name Billy J. Kramer is an English pop singer.  In the 1960s, Kramer was managed by Brian Epstein, who also managed The Beatles, and he recorded several original Lennon and McCartney compositions.\n\nThe Dakotas (band): The Dakotas is a group of British musicians, which initially convened as a backing band in Manchester, England.  However, they are most closely associated with the singer Billy J. Kramer, a Liverpudlian who was the lead vocalist for the group during the 1960s.  In the U.S., they are regarded as part of the British Invasion.\n\nThe Wombats: The Wombats are an English rock band formed in Liverpool in 2003.  The band is composed of lead vocalist and guitarist Matthew Murphy, drummer Dan Haggis, and bassist Tord Øverland Knudsen, and has been since its inception.  The band is signed to 14th Floor Records in the United Kingdom and Bright Antenna in the United States.  The Wombats' albums have sold over 1 million copies worldwide.\n\nLittle Children (album): Little Children is the second album by the English rock band Billy J. Kramer & The Dakotas.  It was released by Imperial Records in the United States in 1964.  There never was a British version.\n\nThe Beatles: The Beatles were an English rock band formed in Liverpool in 1960.  With members John Lennon, Paul McCartney, George Harrison and Ringo Starr, they became widely regarded as the foremost and most influential act of the rock era.  Rooted in skiffle, beat and 1950s rock and roll, the Beatles later experimented with several musical styles, ranging from pop ballads and Indian music to psychedelia and hard rock, often incorporating classical elements and unconventional recording techniques in innovative ways.  In 1963 their enormous popularity first emerged as \"Beatlemania\", and as the group's music grew in sophistication in subsequent years, led by primary songwriters Lennon and McCartney, they came to be perceived as an embodiment of the ideals shared by the counterculture of the 1960s.\n\nCultural impact of the Beatles: The Beatles were an English rock band, formed in Liverpool in 1960.  With members John Lennon, Paul McCartney, George Harrison and Ringo Starr, they became widely regarded as the foremost and most influential act of the rock era.  In the early 1960s, their enormous popularity first emerged as \"Beatlemania\", but as the group's music grew in sophistication, led by primary songwriters Lennon and McCartney, they came to be perceived as an embodiment of the ideals shared by the counterculture of the 1960s.\n\nIan and the Zodiacs: Ian and the Zodiacs were an English rock and roll band formed in 1958, originally known as The Zodiacs, in Liverpool, England.  Led by Ian Edwards (1943–2007), the band existed in relative obscurity until relocating to Germany in 1964 where they achieved national success.  During the band's three-year stint in Germany, they released three albums under their name, exclusive to the country until their re-release.  They also released two cover albums featuring material by The Beatles with the name, The Koppykats.\n\nEcho &amp; the Bunnymen: Echo & the Bunnymen are an English rock band formed in Liverpool in 1978.  The original line-up consisted of vocalist Ian McCulloch, guitarist Will Sergeant and bassist Les Pattinson, supplemented by a drum machine.  By 1980, Pete de Freitas joined as the band's drummer.\n\nQuestion: What was the name of the manager of both Billy J. Kramer and an English rock  band formed in Liverpool in 1960?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"manager_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the manager.\"\n    },\n    \"managed_entities\": {\n      \"type\": \"array\",\n      \"description\": \"A list of artists or bands managed by this person.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"entity_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the artist or band.\"\n          },\n          \"entity_type\": {\n            \"type\": \"string\",\n            \"description\": \"The type of entity, e.g., 'singer' or 'band'.\"\n          },\n          \"formation_location\": {\n            \"type\": \"string\",\n            \"description\": \"The city where the band was formed (if applicable).\"\n          },\n          \"formation_year\": {\n            \"type\": \"integer\",\n            \"description\": \"The year the band was formed (if applicable).\"\n          }\n        },\n        \"required\": [\n          \"entity_name\",\n          \"entity_type\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"management_period_description\": {\n      \"type\": \"string\",\n      \"description\": \"A description of the period during which the management occurred.\"\n    }\n  },\n  \"required\": [\n    \"manager_name\",\n    \"managed_entities\",\n    \"management_period_description\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "manager_name": {
        "type": "string",
        "description": "The name of the manager."
      },
      "managed_entities": {
        "type": "array",
        "description": "A list of artists or bands managed by this person.",
        "items": {
          "type": "object",
          "properties": {
            "entity_name": {
              "type": "string",
              "description": "The name of the artist or band."
            },
            "entity_type": {
              "type": "string",
              "description": "The type of entity, e.g., 'singer' or 'band'."
            },
            "formation_location": {
              "type": "string",
              "description": "The city where the band was formed (if applicable)."
            },
            "formation_year": {
              "type": "integer",
              "description": "The year the band was formed (if applicable)."
            }
          },
          "required": [
            "entity_name",
            "entity_type"
          ],
          "additionalProperties": false
        }
      },
      "management_period_description": {
        "type": "string",
        "description": "A description of the period during which the management occurred."
      }
    },
    "required": [
      "manager_name",
      "managed_entities",
      "management_period_description"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
