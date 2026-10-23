{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDavid Lightfoot: David Lightfoot worked on the horror films \"Wolf Creek\" and \"Rogue\".\n\nLeigh Blackmore: Leigh (David) Blackmore (born 1959) is an Australian horror writer, critic, editor, occultist and musician.  He served as the second President of the Australian Horror Writers Association (2010–2011).  His work has been nominated four times for the Ditmar Award, once for fiction and three times for the William Atheling Jr.  Award for criticism.  .  He has contributed entries to such encyclopedias as S.T. Joshi and Stefan J. Dziemianowicz (eds) \"Supernatural Literature of the World\" (Greenwood Press, 2005, 3 vols) and June Pulliam and Tony Fonseca (eds), \"Ghosts in Popular Culture and Legend\" (ABC-Clio, 2016).\n\nBeast No More (Film): Beast No More is a 2018 Australian horror film starring Dan Ewing, Jessica Tovey and Taya Calder-Mason.  The story revolves around Mary Jane (Jessica Tovey) a young biologist who ventures into Australian bush land to escape after the sudden death of her 5 year old son.  When she becomes uncontactable her husband, Jake (Dan Ewing) and her visually impaired sister (Taya Calder-Mason) take it upon themselves to find her.\n\nThree Dollars: Three Dollars is a 2005 Australian film, directed by Robert Connolly and based on a novel of the same name by Elliot Perlman.  It won the 2005 Australian Film Institute Award for Best Adapted Screenplay.\n\nJewboy: Jewboy is a 2005 Australian film directed by Tony Krawitz.  The film stars Ewen Leslie, Chris Haywood, Saskia Burmeister, and Nicholas Eadie.  It won the 2005 Australian Film Institute Awards for Best Short Fiction Film, Best Cinematography and Best Screenplay in a Short.\n\nNight of Fear (film): Night of Fear is a 1972 Australian horror film, directed by Terry Bourke.  It was written by Bourke and produced by Rod Hay.  It is about a woman who is terrorised by a serial killer in the woods.  Its theme and style bears a resemblance to the horror classic \"The Texas Chain Saw Massacre\", released two years later.  The film is notable for having no dialogue or character names.  It has been called \"the first Australian horror movie of the renaissance\".\n\nWolf Creek (film): Wolf Creek is a 2005 Australian horror film written, co-produced, and directed by Greg McLean, and starring John Jarratt.  The story revolves around three backpackers who find themselves taken captive and after a brief escape, hunted down by Mick Taylor in the Australian outback.  The film was ambiguously marketed as being \"based on true events\"; the plot bore elements reminiscent of the real-life murders of tourists by Ivan Milat in the 1990s and Bradley Murdoch in 2001.\n\nCassandra Magrath: Cassandra Magrath (born 8 January 1981 in Melbourne) is an Australian actress.  She played Miranda Gibson in the Australian ABC 1998–2000 television series \"SeaChange\" and Liz Hunter in the 2005 Australian horror film \"Wolf Creek\".\n\nCoffin Rock: Coffin Rock is an Australian melodramatic thriller film directed by Rupert Glasson and produced by David Lightfoot.  The movie stars Lisa Chappell, Robert Taylor and Sam Parsonson.\n\nThirst (1979 film): Thirst is a 1979 Australian horror film directed by Rod Hardy and starring Chantal Contouri and Max Phipps and British actor David Hemmings.  It has been described as a blend of vampire and science fiction genres, influenced by the 1973 film \"Soylent Green\" as well as drawing on the vampire folklore of Elizabeth Báthory – one of several vampire films in the 1970s to do so.\n\nQuestion:  David Lightfoot worked on a 2005 Australian horror film starring who?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the film.\"\n    },\n    \"country_of_origin\": {\n      \"type\": \"string\",\n      \"description\": \"The country where the film was produced.\"\n    },\n    \"person_involved\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the person involved.\"\n        },\n        \"role\": {\n          \"type\": \"string\",\n          \"description\": \"The role of the person in the film production.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"role\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"starring_actors\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of actors starring in the film.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"genre\",\n    \"country_of_origin\",\n    \"person_involved\",\n    \"starring_actors\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "release_year": {
        "type": "integer",
        "description": "The release year of the film."
      },
      "genre": {
        "type": "string",
        "description": "The genre of the film."
      },
      "country_of_origin": {
        "type": "string",
        "description": "The country where the film was produced."
      },
      "person_involved": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the person involved."
          },
          "role": {
            "type": "string",
            "description": "The role of the person in the film production."
          }
        },
        "required": [
          "name",
          "role"
        ],
        "additionalProperties": false
      },
      "starring_actors": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of actors starring in the film."
      }
    },
    "required": [
      "film_title",
      "release_year",
      "genre",
      "country_of_origin",
      "person_involved",
      "starring_actors"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
