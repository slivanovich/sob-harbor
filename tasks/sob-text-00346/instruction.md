{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJake Spanner, Private Eye: Jake Spanner, Private Eye is a 1989 American television crime film written and directed by Lee H. Katzin and starring Robert Mitchum and Ernest Borgnine.\n\nDebbie Burton: Debbie Burton was an American singer.  She is best known for dubbing the singing voice of the young Baby Jane Hudson (played by child actress Julie Allred) in the 1962 film \"What Ever Happened to Baby Jane? \", singing the song \"I've Written a Letter to Daddy\".  Burton also sang a duet with Bette Davis, the rock and roll song \"What Ever Happened to Baby Jane?\" , written by Frank DeVol and Lukas Heller.  It was released as a promotional single, with Burton's rendition of \"I've Written a Letter to Daddy\" on the flipside.  An instrumental version of \"What Ever Happened to Baby Jane?\"  can be heard in the movie.\n\nThe Shopping Bag Lady: The Shopping Bag Lady is a 1975 American short film directed by Bert Salzman and starring Mildred Dunnock.\n\nRestraining Order (film): Restraining Order is a 1999 crime thriller film directed by Lee H. Katzin and starring Eric Roberts and Hannes Jaenicke.\n\nWhat Ever Happened to Aunt Alice?: What Ever Happened to Aunt Alice?  is a 1969 American thriller film directed by Lee H. Katzin with Bernard Girard (uncredited), and starring Geraldine Page, Ruth Gordon, Rosemary Forsyth, Robert Fuller and Mildred Dunnock.  The screenplay by Theodore Apstein, based on the novel \"The Forbidden Garden\" by Ursula Curtiss, focuses on an aging Arizona widow who hires elderly female housekeepers and cons them out of their money before murdering them.\n\nWhat Ever Happened to...: What Ever Happened to... is a 1991 American made-for-television thriller drama film directed by David Greene and adapted for the small screen by Brian Taggert, based on the novel \"What Ever Happened to Baby Jane? \" by Henry Farrell and the 1962 theatrical film of the same name.  It stars real-life sisters Lynn Redgrave as Baby Jane Hudson and Vanessa Redgrave as Blanche Hudson, in the roles previously played by Bette Davis and Joan Crawford in the 1962 adaptation.\n\nHeaven with a Gun: Heaven with a Gun is a 1969 American western film starring Glenn Ford.  directed by Lee H. Katzin.\n\nMildred Dunnock: Mildred Dorothy Dunnock (January 25, 1901 – July 5, 1991) was an American theater, film and television actress.\n\nThe Salzburg Connection: The Salzburg Connection is a 1972 American DeLuxe Color thriller film directed by Lee H. Katzin, starring Barry Newman and Anna Karina in Panavision.  It is based on a novel by Helen MacInnes.\n\nThe Party Crashers: The Party Crashers is a 1958 American drama film directed by Bernard Girard and written by Bernard Girard and Dan Lundberg.  The film stars Mark Damon, Bobby Driscoll, Connie Stevens, Frances Farmer (in her last feature film role), Doris Dowling, and Gary Gray.  The film was released in September 1958, by Paramount Pictures.\n\nQuestion: What Ever Happened to Aunt Alice?, is a 1969 American thriller film directed by Lee H. Katzin with Bernard Girard, and starring Mildred Dorothy Dunnock, was an American theater, film and television actress, and passed away on which date?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film mentioned in the question.\"\n    },\n    \"film_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"director_names\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Names of the directors of the film.\"\n    },\n    \"actress_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The full name of the actress.\"\n        },\n        \"profession\": {\n          \"type\": \"string\",\n          \"description\": \"The profession of the actress.\"\n        },\n        \"death_date\": {\n          \"type\": \"string\",\n          \"description\": \"The date the actress passed away, in YYYY-MM-DD format.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"profession\",\n        \"death_date\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"film_year\",\n    \"director_names\",\n    \"actress_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film mentioned in the question."
      },
      "film_year": {
        "type": "integer",
        "description": "The release year of the film."
      },
      "director_names": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Names of the directors of the film."
      },
      "actress_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The full name of the actress."
          },
          "profession": {
            "type": "string",
            "description": "The profession of the actress."
          },
          "death_date": {
            "type": "string",
            "description": "The date the actress passed away, in YYYY-MM-DD format."
          }
        },
        "required": [
          "name",
          "profession",
          "death_date"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_title",
      "film_year",
      "director_names",
      "actress_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
