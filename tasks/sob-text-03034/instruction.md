{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nList of fashion events: This is the list of fashion weeks/events/shows held annually or two times a year all around the world.  There are six main events in the world: the London Fashion Week, Milan Fashion Week, New York Fashion Week, Paris Fashion Week, Feeric Fashion Week and Arab Fashion Week.  While the fashion scene turns more multipolar in the 21st century, other centers like Berlin, Los Angeles, Madrid, Rome, São Paulo, Shanghai and Tokyo host important fashion weeks and other events.\n\nWorld MasterCard Fashion Week: World MasterCard Fashion Week or WMCFW, formerly known as LG Fashion Week is an event held in Toronto, Canada in March (for fall/winter collections) and in October (for spring/summer collections) by IMG Fashion.  It is the biggest fashion week held in Canada and it is the second largest fashion week in North America after New York City.  It is a very important Fashion week in Canada and in the world because it shows Canadian culture and fashion.  It also has a lot of media attention.\n\nMiami Fashion Week: Miami Fashion Week is an annual fashion week held in Miami, Florida, United States.  Miami Fashion Week, not to be confused with the Mercedes-Benz Fashion Week Miami, takes place every year during the spring and is held in the Wynwood Arts District.  Miami Fashion Week was started in 1998 and is the world's largest fashion week for Latin American and the Caribbean fashion designers.\n\nDark Fantasy (song): \"Dark Fantasy\" is a song by American hip hop recording artist and producer Kanye West from his fifth studio album, \"My Beautiful Dark Twisted Fantasy\" (2010).  The song serves as the opening track of the album, and was written by West, Ernest Wilson, Jeff Bhasker, Mike Dean and Robert Diggs.  It features an opening narrative delivered by rapper Nicki Minaj, and singers Teyana Taylor and Justin Vernon contribute to the song's hook and provide background vocals.  The track is built around a sample of \"In High Places\" by Mike Oldfield (sung by Jon Anderson).  The song introduces several of the themes presented on the album and features numerous pop culture references, a gospel-inspired production style, and piano-driven composition.  The song received acclaim from music critics, who praised the song as a strong opener to \"My Beautiful Dark Twisted Fantasy\", complimenting West's vocal delivery and the song's production.\n\nTeyana Taylor: Teyana Taylor (born December 10, 1990), is an American actress, model, dancer, and a recording artist/rapper from Harlem, New York.  In 2007, Taylor signed a record deal with American musician Pharrell Williams' Star Trak Entertainment imprint, before making her first national appearance on MTV's \"My Super Sweet 16\".  In 2012, she signed to Kanye West's GOOD Music label through Def Jam, after asking for her release from Star Trak.  As an aspiring songwriter, Taylor has worked with and written records for major artists such as Usher, Chris Brown, and Omarion.  Taylor has appeared on runways during Fashion Week and has also landed high-profile features, such as on Kanye West’s \"My Beautiful Dark Twisted Fantasy\".\n\nMercedes-Benz Fashion Week Miami: Mercedes-Benz Fashion Week Miami is an annual fashion week held in Miami, Florida, United States.  Mercedes-Benz Fashion Week Miami, not to be confused with Miami Fashion Week, is held every year during the Summer at the Raleigh Hotel at 1775 Collins Avenue in South Beach, Miami Beach.  Mercedes-Benz Fashion Week Miami works together with New York Fashion Week, and is the country's largest, and most important fashion week for swimwear.  IMG whom first brought its runway event to South Beach in 2004, had an ongoing partnership with Mercedes-Benz.  However, due to changes in ownership, as IMG was acquired by William Morris Endeavor and Silver Lake Partners in a $2.2 billion deal, the agency lost Mercedes-Benz as a title sponsor.  The show was cancelled for 2015 but will resume in 2016 after re-branding the popular event.\n\nSunny Fong: Sunny Fong (born 1977) is a Canadian fashion designer who owns VAWK, a clothing brand.  He lives in Toronto, Ontario.  In 2009, he won the second season of \"Project Runway Canada\".  His collection from this competition was showcased at LG Fashion Week.  In both 2009 and 2010, Fong began the showings of his collections before the official start of LG Fashion Week, showcasing his work at Walker Court of the Art Gallery of Ontario.  His 2011 spring/summer collection combined the themes of bullfighting and safari.  Urban culture and Malayan mountaineering were the themes of his 2011 fall/winter collection.  This collection was showcased at LG Fashion Week, in contrast to Fong's previous few seasons' off-site showings.  At the following year's LG Fashion Week, Fong's spring/summer 2012 collection featured monokinis that critics from \"The London Free Press\" called \"even a bit tough for the models to pull off, much less mere mortals.\"  During the final fashion show of that October's LG Fashion Week, Fong had a model appear wearing a gold bullet bra as Madonna's \"Justify My Love\" played.\n\nAfrica Fashion Week New York: Africa Fashion Week (New York) is an annual fashion week held in New York, United States.  An official proclamation was given by Mayor Bloomberg, the mayor of New York City, in 2010.  Africa Fashion Week (New York) is not to be confused with South Africa Fashion Week and Arise Africa Fashion Week.\n\nBolivia Fashion Week: Bolivia Fashion Week took place for the first time in Bolivia on April 5 to 8, 2016 in the Bolivian city of Cochabamba.  Bolivia Fashion Week is an annual event that showcases both emerging designers, brands and cultural fashion innovators.  The presence of Agatha Ruiz de la Prada from Spain, and other world designers in the Bolivia Fashion Week 2016 event, highlighted the goal of the fashion week to connect talented local designers with the global fashion industry, as stated by Bolivia Fashion Week's founder, Pamela Alarcon.\n\nMila Chernikova: Mila Marie Chernikova (born July 9, 1994) is an American born Russian-Italian international fashion model and music artist.  Mila got started modeling at a young age and finally made her debut as a runway model in 2015/2016 when she walked for \"Araksi Balyan\" and \"Polina Zeynalian\" in LA fashion week 2016.  Soon after she was seen walking for \"Dauphine of France\" and \"Nina B Roze\" behind model Ava Capra from America's next top model (cycle 22) at Style week LA.\n\nQuestion: What fashion week runway model contributed to the hook of Kanye West's \"Dark Fantasy\"?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"model_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the fashion model.\"\n    },\n    \"song_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the song.\"\n        },\n        \"artist\": {\n          \"type\": \"string\",\n          \"description\": \"The artist of the song.\"\n        },\n        \"contribution_to_hook\": {\n          \"type\": \"string\",\n          \"description\": \"The specific contribution made to the song's hook.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"artist\",\n        \"contribution_to_hook\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"model_career_attributes\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"is_runway_model\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the person is a runway model.\"\n        },\n        \"has_appeared_on_fashion_week_runways\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the model has appeared on fashion week runways.\"\n        }\n      },\n      \"required\": [\n        \"is_runway_model\",\n        \"has_appeared_on_fashion_week_runways\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"model_name\",\n    \"song_details\",\n    \"model_career_attributes\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "model_name": {
        "type": "string",
        "description": "The name of the fashion model."
      },
      "song_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the song."
          },
          "artist": {
            "type": "string",
            "description": "The artist of the song."
          },
          "contribution_to_hook": {
            "type": "string",
            "description": "The specific contribution made to the song's hook."
          }
        },
        "required": [
          "title",
          "artist",
          "contribution_to_hook"
        ],
        "additionalProperties": false
      },
      "model_career_attributes": {
        "type": "object",
        "properties": {
          "is_runway_model": {
            "type": "boolean",
            "description": "Indicates if the person is a runway model."
          },
          "has_appeared_on_fashion_week_runways": {
            "type": "boolean",
            "description": "Indicates if the model has appeared on fashion week runways."
          }
        },
        "required": [
          "is_runway_model",
          "has_appeared_on_fashion_week_runways"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "model_name",
      "song_details",
      "model_career_attributes"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
