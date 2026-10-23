{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nYoon Jin-seo: Yoon Jin-seo (born Yoon Soo-kyung, 5 August 1983) is a South Korean actress.  Yoon has starred in films such as \"Oldboy\", \"All for Love\", \"A Good Day to Have an Affair\", and \"Secret Love\".  She also appeared in a variety of TV series — historical drama \"The Return of Iljimae\", action comedy \"\", and cable romantic comedy \"Twelve Men in a Year\".\n\nCoffee Mate (film): Coffee Mate () is a 2016 South Korean melodrama film written and directed by Yi Hyun-ha, starring Yoon Jin-seo and Oh Ji-ho.\n\nSanta Barbara (film): Santa Barbara () is a 2014 South Korean romance film starring Lee Sang-yoon and Yoon Jin-seo.  It was written and directed by David Cho (also known as Cho Sung-kyu).\n\nThe Return of Iljimae: The Return of Iljimae () is a 2009 South Korean historical action television series, starring Jung Il-woo in the title role of Iljimae, Yoon Jin-seo, Kim Min-jong and Jung Hye-young.  It aired on MBC from January 21 to April 9, 2009 on Wednesdays and Thursdays at 21:55 for 24 episodes.\n\nTwelve Men in a Year: Twelve Men in a Year (, also known as 12 Signs of Love) is a 2012 South Korean television series, starring Yoon Jin-seo and On Joo-wan.  It aired on tvN from February 15 to April 5, 2012 on Wednesdays and Thursdays at 23:00 for 16 episodes.\n\nThe Girl Who Sees Smells: The Girl Who Sees Scents () is a 2015 South Korean television series adapted from the webtoon of the same title by Seo Soo-kyung a/k/a Man Chwi.  Starring Park Yoo-chun, Shin Se-kyung, Namgoong Min and Yoon Jin-seo, it aired on SBS on Wednesdays and Thursdays at 21:55 for 16 episodes from April 1 to May 21, 2015.\n\nTraces of Love: Traces of Love is a 2006 South Korean film directed by Kim Dae-seung, and starring Yoo Ji-tae, Kim Ji-soo, and Uhm Ji-won.  The film is based on the Sampoong Department Store collapse, which took place in 1995.\n\nJackpot (2016 TV series): Jackpot (), also known as The Royal Gambler, is a South Korean historical drama starring Jang Keun-suk, Yeo Jin-goo, Jun Kwang-ryul, Choi Min-soo, Yoon Jin-seo and Lim Ji-yeon.  It replaced \"Six Flying Dragons\" and aired on SBS on Mondays and Tuesdays at 22:00 (KST) from March 28, 2016 to June 14, 2016 for 24 episodes.\n\nYoo Ji-tae: Yoo Ji-tae (born April 13, 1976) is a South Korean actor, film director and screenwriter.  After a stint as a fashion model, Yoo launched his acting career in 1998 then rose to fame through the films \"Attack the Gas Station\" (1999) and \"Ditto\" (2000).  In the succeeding years, he gained acting recognition by working with acclaimed directors such as Hur Jin-ho in \"One Fine Spring Day\" (2001), Park Chan-wook in \"Oldboy\" (2003), and Hong Sang-soo in \"Woman is the Future of Man\" (2004).  Yoo began directing short films in 2003, which were well received in the film festival circuit.  His feature directorial debut \"Mai Ratima\" was released in 2013.\n\nSecret Love (2010 film): Secret Love () is a 2010 South Korean film starring Yoo Ji-tae and Yoon Jin-seo, who previously worked together in \"Oldboy\".\n\nQuestion: Yoon Jin-seo, is a South Korean actress, and has starred in films such as which 2010 South Korean film starring Yoo Ji-tae and Yoon Jin-seo, who previously worked together in \"Oldboy\"?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the film.\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the film was released.\"\n        },\n        \"country_of_origin\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the film was produced.\"\n        },\n        \"media_type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of media (e.g., film, TV series).\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"release_year\",\n        \"country_of_origin\",\n        \"media_type\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"starring_actors\": {\n      \"type\": \"array\",\n      \"description\": \"A list of the main actors starring in the film.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"actor_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of an actor.\"\n          }\n        },\n        \"required\": [\n          \"actor_name\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"collaboration_details\": {\n      \"type\": \"object\",\n      \"description\": \"Details about previous collaborations between the starring actors.\",\n      \"properties\": {\n        \"previous_collaboration_film_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the film where the main actors previously collaborated.\"\n        },\n        \"actors_involved_in_collaboration\": {\n          \"type\": \"array\",\n          \"description\": \"A list of actors who collaborated in the previous film.\",\n          \"items\": {\n            \"type\": \"string\"\n          }\n        }\n      },\n      \"required\": [\n        \"previous_collaboration_film_title\",\n        \"actors_involved_in_collaboration\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_details\",\n    \"starring_actors\",\n    \"collaboration_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the film."
          },
          "release_year": {
            "type": "integer",
            "description": "The year the film was released."
          },
          "country_of_origin": {
            "type": "string",
            "description": "The country where the film was produced."
          },
          "media_type": {
            "type": "string",
            "description": "The type of media (e.g., film, TV series)."
          }
        },
        "required": [
          "title",
          "release_year",
          "country_of_origin",
          "media_type"
        ],
        "additionalProperties": false
      },
      "starring_actors": {
        "type": "array",
        "description": "A list of the main actors starring in the film.",
        "items": {
          "type": "object",
          "properties": {
            "actor_name": {
              "type": "string",
              "description": "The name of an actor."
            }
          },
          "required": [
            "actor_name"
          ],
          "additionalProperties": false
        }
      },
      "collaboration_details": {
        "type": "object",
        "description": "Details about previous collaborations between the starring actors.",
        "properties": {
          "previous_collaboration_film_title": {
            "type": "string",
            "description": "The title of the film where the main actors previously collaborated."
          },
          "actors_involved_in_collaboration": {
            "type": "array",
            "description": "A list of actors who collaborated in the previous film.",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "previous_collaboration_film_title",
          "actors_involved_in_collaboration"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_details",
      "starring_actors",
      "collaboration_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
