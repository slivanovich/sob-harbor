{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nEl Pampero: El Pampero is a live album by Argentinian jazz composer and saxophonist Gato Barbieri featuring performances recorded at the Montreux Jazz Festival in 1971 and first released on the Flying Dutchman label.\n\nUnder Fire (album): Under Fire is an album by Argentinian jazz composer and saxophonist Gato Barbieri featuring performances recorded in New York in 1971 and first released on the Flying Dutchman label in 1973.\n\nThe Third World (album): The Third World is an album by Argentinian jazz composer and saxophonist Gato Barbieri featuring performances recorded in 1969 and first released on the Flying Dutchman label.\n\nSwiss Suite: Swiss Suite is a live album by American jazz composer/arranger Oliver Nelson featuring performances by a big band with soloists Gato Barbieri (tenor sax) and Eddie \"Cleanhead\" Vinson (alto sax).  The album was recorded at the Montreux Jazz Festival in 1971 for the Flying Dutchman label.\n\nCape Town International Jazz Festival: The Cape Town International Jazz Festival is an annual music festival held in Cape Town, South Africa.  The first one was held in 2000 to 2005 and is recognised as the fourth largest jazz festival in the world and the largest jazz festival on the African continent.  The festival used to be called the Cape Town North Sea Jazz Festival due to its association with the North Sea Festival in the Netherlands.\n\nYesterdays (Gato Barbieri album): Yesterdays is an album by Argentinian jazz composer and saxophonist Gato Barbieri featuring performances recorded in New York in 1974 and first released on the Flying Dutchman label.  The album was rereleased in 1988 as \"The Third World Revisited\" with two additional tracks from \"El Pampero\".\n\nMontreal International Jazz Festival: The Festival International de Jazz de Montréal (English: Montreal International Jazz Festival ) is an annual jazz festival held in Montreal, Quebec, Canada.  The Montreal Jazz Fest holds the 2004 Guinness World Record as the world's largest jazz festival.  Every year it features roughly 3,000 artists from 30-odd countries, more than 650 concerts (including 450 free outdoor performances), and welcomes over 2 million visitors (12.5% of whom are tourists) as well as 300 accredited journalists.  The festival takes place at 20 different stages, which include free outdoor stages and indoor concert halls.\n\nBolivia (Gato Barbieri album): Bolivia is a live album by Argentinian jazz composer and saxophonist Gato Barbieri featuring performances recorded in New York in 1973 and first released on the Flying Dutchman label.\n\nFenix (album): Fenix is an album by Argentinian jazz composer and saxophonist Gato Barbieri featuring performances recorded in 1971 and first released on the Flying Dutchman label.\n\nMontreux Jazz Festival: The Montreux Jazz Festival (formerly Festival de Jazz Montreux and Festival International de Jazz Montreux) is a music festival in Switzerland, held annually in early July in Montreux on the Lake Geneva shoreline.  It is the second largest annual jazz festival in the world after Canada's Montreal International Jazz Festival.\n\nQuestion: What year was the album released by Gato Barbieri which features live performances recorded at the second largest jazz festival in the world?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"album_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the album.\"\n    },\n    \"artist_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the artist who released the album.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the album was first released.\"\n    },\n    \"recording_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"festival_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the jazz festival where the performances were recorded.\"\n        },\n        \"festival_world_ranking\": {\n          \"type\": \"integer\",\n          \"description\": \"The world ranking of the jazz festival by size.\"\n        },\n        \"recording_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the performances were recorded.\"\n        },\n        \"is_live_album\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the album is a live recording.\"\n        }\n      },\n      \"required\": [\n        \"festival_name\",\n        \"festival_world_ranking\",\n        \"recording_year\",\n        \"is_live_album\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"album_title\",\n    \"artist_name\",\n    \"release_year\",\n    \"recording_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "album_title": {
        "type": "string",
        "description": "The title of the album."
      },
      "artist_name": {
        "type": "string",
        "description": "The name of the artist who released the album."
      },
      "release_year": {
        "type": "integer",
        "description": "The year the album was first released."
      },
      "recording_details": {
        "type": "object",
        "properties": {
          "festival_name": {
            "type": "string",
            "description": "The name of the jazz festival where the performances were recorded."
          },
          "festival_world_ranking": {
            "type": "integer",
            "description": "The world ranking of the jazz festival by size."
          },
          "recording_year": {
            "type": "integer",
            "description": "The year the performances were recorded."
          },
          "is_live_album": {
            "type": "boolean",
            "description": "Indicates if the album is a live recording."
          }
        },
        "required": [
          "festival_name",
          "festival_world_ranking",
          "recording_year",
          "is_live_album"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "album_title",
      "artist_name",
      "release_year",
      "recording_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
