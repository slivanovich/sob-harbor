{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nWalking the Halls: Walking the Halls is a 2012 television film directed by Doug Campbell.  Originally aired on Lifetime, the film was written by Christine Conradt and Ken Sanders, and features Jamie Luner and Caitlin Thompson.\n\nList of songs recorded by Alyssa Milano: American actress and singer Alyssa Milano has recorded songs for four studio albums, two compilation albums, and an exercise video.  She first came to prominence within the entertainment industry for her portrayal of Samantha Micelli in the television sitcom \"Who's the Boss? \", which premiered in September 1984.  While acting on the television series, she recorded and released music exclusively in Japan through the Japanese record label Pony Canyon, Inc. Pony Canyon, Inc. signed Milano to a five-album deal based on her appearance and personality, which was a common practice by Japanese record labels in their efforts to produce Japanese idols.  The label also choose Milano due to her popularity in Asia from her role as Jenny Matrix in the 1985 film \"Commando\".  Throughout her musical career, Milano had little involvement with the songwriting and production of her albums.  She did not express any interest in releasing her music in the United States, and said: \"A lot of actors who release albums here are laughed at, I'm not interested in crossing over.  I'd much rather have it released where it's appreciated than laughed at.\"\n\nJust the Ten of Us: Just the Ten of Us is an American sitcom starring stand-up comedian Bill Kirchenbauer as Coach Graham Lubbock, a teacher and the head of a large Catholic family with eight children living in Eureka, California.  The series is a spin-off of \"Growing Pains\", in which Kirchenbauer portrayed the same character on a recurring basis.  As the series progressed, Coach Lubbock's four eldest daughters, the teenagers Marie (Heather Langenkamp), Cindy (Jamie Luner), Wendy (Brooke Theiss), and Connie (JoAnn Willette), became the primary focus of the show.\n\nConfessions of a Sorority Girl: Confessions of a Sorority Girl (also known as Confessions of Sorority Girls) is a 1994 American television film that debuted on Showtime on July 29, 1994.  Directed by Uli Edel, the stars include Alyssa Milano and Jamie Luner.\n\nThe Very Best of Alyssa Milano: The Very Best Of Alyssa Milano is a compilation album recorded by Alyssa Milano during her pursuit, mainly in Japan, of a singing career.  A more complete collection of Milano's greatest hits and other singles than the previously released \"\" remix collection.  The album was only released as a promotional CD.\n\nAlyssa Milano discography: American actress and singer Alyssa Milano has released: four studio albums, one reissue, two compilation albums, two video albums, five music videos and thirteen singles (including three charity singles).  Milano debuted as an actress in the television sitcom \"Who's the Boss? \", which premiered in September 1984.  While acting she signed a five-album deal with Japanese record label Pony Canyon, Inc. Prior to her record contract, Milano had contributed to the charity single \"We Are The World\" as part of a group of child stars.  She also released an exercise video, entitled \"Alyssa Milano's Teen Steam\", and recorded its theme song along with a rap.\n\nAlyssa Milano: Alyssa Jayne Milano (born December 19, 1972) is an American actress, activist, producer and former singer.  She is best known for her roles in \"Who's the Boss? \", \"Melrose Place\", \"Charmed\", \"My Name is Earl\", \"Mistresses\" and \"\".\n\nLook in My Heart: Look In My Heart is Alyssa Milano's first album, released March 21, 1989, when she was 16 years old.  It was also released as a Color Picture Label CD and later as a 24Krt Gold Edition, which comes with a bonus track \"Look In My Heart\" (extended dance remix) identical to the version on \"The Best In The World\" album.  Videos were filmed for the three singles that were released.  A VHS video was also released entitled Look In My Heart that included the three videos and a short documentary, \"Alyssa's Backstage Memories\".  After the credits roll, Alyssa's Japanese commercial for pasta can be seen—she is singing \"Look In My Heart\" in the commercial.\n\nJamie Luner: Jamie Michelle Luner (born May 12, 1971) is an American actress who first came to prominence on the ABC sitcom \"Just the Ten of Us\", but is perhaps better known for her role as Lexi Sterling on \"Melrose Place\".  She also starred on television as Rachel Burke in the final season of \"Profiler\".  Luner portrayed Liza Colby on the ABC soap opera \"All My Children\" from April 2009 until its final episode on September 23, 2011.  Luner is also well known for her lead roles in many Lifetime movies.\n\nLiza Colby: Liza Colby is a fictional character on the American soap opera, \"All My Children\", portrayed by actress Jamie Luner from April 2009 until September 2011.  She was previously played by actress Marcy Walker from 1981–1984, and then again from 1995–2005, although the role was also briefly portrayed by Alice Haining.  Liza is a resident of the fictional town of Pine Valley, Pennsylvania.\n\nQuestion: who was the actress in \"who's the boss\" Alyssa Milano or Jamie Luner?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"show_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the television show in question.\"\n    },\n    \"actress_in_show\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actress who starred in the specified show.\"\n    },\n    \"actress_in_show_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The full name of the actress.\"\n        },\n        \"prominent_role_in_show\": {\n          \"type\": \"string\",\n          \"description\": \"The specific role the actress played in the show.\"\n        },\n        \"other_notable_roles\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"A list of other notable shows or roles the actress is known for.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"prominent_role_in_show\",\n        \"other_notable_roles\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"other_actress_mentioned\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The full name of the other actress mentioned in the question.\"\n        },\n        \"known_for_shows\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"A list of shows the other actress is known for.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"known_for_shows\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"show_title\",\n    \"actress_in_show\",\n    \"actress_in_show_details\",\n    \"other_actress_mentioned\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "show_title": {
        "type": "string",
        "description": "The title of the television show in question."
      },
      "actress_in_show": {
        "type": "string",
        "description": "The name of the actress who starred in the specified show."
      },
      "actress_in_show_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The full name of the actress."
          },
          "prominent_role_in_show": {
            "type": "string",
            "description": "The specific role the actress played in the show."
          },
          "other_notable_roles": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of other notable shows or roles the actress is known for."
          }
        },
        "required": [
          "name",
          "prominent_role_in_show",
          "other_notable_roles"
        ],
        "additionalProperties": false
      },
      "other_actress_mentioned": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The full name of the other actress mentioned in the question."
          },
          "known_for_shows": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of shows the other actress is known for."
          }
        },
        "required": [
          "name",
          "known_for_shows"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "show_title",
      "actress_in_show",
      "actress_in_show_details",
      "other_actress_mentioned"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
