{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nChris Sheridan (writer): Christopher \"Chris\" Sheridan (born September 19, 1967) is an American television writer, producer, and occasional voice actor.  Born in the Philippines, Sheridan grew up in New Hampshire.  He attended Gilford High School, where he decided that he wanted to become a writer.  After graduating from Union College, he moved back to his home, where he worked at several short-term jobs before relocating to California to start his career.  His first job came in 1992 when he was hired as a writer's assistant for the Fox sitcom \"Shaky Ground\".  Following that, he was hired as an assistant on \"Living Single\", a Fox sitcom, where he was eventually promoted to writer.  He stayed with the show until its cancellation in 1998.\n\nThe Book of Life (2014 film): The Book of Life is a 2014 American 3D computer-animated musical fantasy adventure comedy film produced by Reel FX Creative Studios and distributed by 20th Century Fox.  Co-written and directed by Jorge R. Gutierrez, it was produced by Aaron Berger, Brad Booker, Guillermo del Toro and Carina Schulze.  The film stars the voices of Diego Luna, Zoe Saldana, Channing Tatum, Christina Applegate, Ice Cube, Ron Perlman and Kate del Castillo.  Based on an original idea by Gutierrez, the story follows a bullfighter who, on the Day of the Dead, embarks on an afterlife adventure to fulfill the expectations of his family and friends.\n\nPaget Brewster: Paget Valerie Brewster ( ; born March 10, 1969) is an American actress and singer.  She was first recognized for her recurring role as Kathy on the fourth season of the NBC sitcom \"Friends\".  Her breakthrough role came as Special Agent Emily Prentiss on the CBS crime drama \"Criminal Minds\", on which she appeared regularly from 2006 to 2012 and has since returned to for guest appearances before returning regularly in 2016.  Her other roles include Elise and Mr. Mumbles on The Hub's \"Dan Vs.\", Frankie Dart on Yahoo's \"Community\", Sadie Doyle on the \"Thrilling Adventure Hour\" segment \"Beyond Belief\" and Sara Kingsley on the Fox sitcom \"Grandfathered\".  She has also made numerous guest appearances on \"Two and a Half Men\", \"\" and \"Modern Family\".  She currently stars as Dodo Bellacourt on the Comedy Central series \"Another Period\".\n\nTed Bundy (film): Ted Bundy is a 2002 American biographical crime film directed and co-written by Matthew Bright.  The film dramatizes the crimes of serial killer Ted Bundy.  It stars Michael Reilly Burke in the title role, and Boti Bliss as Bundy's girlfriend, Lee (a character based on Elizabeth Kloepfer, Bundy's real life girlfriend during his killing spree).\n\nTichina Arnold: Tichina Rolanda Arnold (born June 28, 1969) is an American actress, comedian, model and singer.  She began her career as a child actor, appearing in supporting roles in \"Little Shop of Horrors\" (1986) and \"How I Got into College\" (1989) before being cast as Pamela James on the FOX sitcom \"Martin\", which she played from 1992 to the series' conclusion in 1997.  She also played the family matriarch Rochelle on the UPN/CW sitcom \"Everybody Hates Chris\" from 2005 to 2009, and portrayed Judi Mann in the TV Land original sitcom \"Happily Divorced\" from 2011 to 2013.  Beginning 2014, she has played the lead role of Cassie Calloway on \"Survivor's Remorse\".\n\nDavid Faustino: David Anthony Faustino (born March 3, 1974) is an American actor and rapper primarily known for his role as Bud Bundy on the FOX sitcom \"Married... with Children\".\n\nMae Whitman: Mae Margaret Whitman (born June 9, 1988) is an American actress, voice actress and singer.  After making her film debut in \"When a Man Loves a Woman\" (1994), she had other supporting roles in films such as \"One Fine Day\" (1996), \"Independence Day\" (1996), and \"Hope Floats\" (1998).  Thereafter, Whitman ventured into television, with her most notable roles including Ann Veal on the Fox sitcom \"Arrested Development\" (2004–2006) and Amber Holt on the NBC drama \"Parenthood\" (2010–2015).  She also had supporting roles in the films \"Scott Pilgrim vs. the World\" (2010) and \"The Perks of Being a Wallflower\" (2012).  Whitman made her leading role film debut in \"The DUFF\" (2015).\n\nMichael Strahan: Michael Anthony Strahan ( ; born November 21, 1971) is a media personality and former American football defensive end who spent his entire 15-year career with the New York Giants of the National Football League (NFL).  Strahan set a record for the most sacks in a season in 2001, and helped the Giants win Super Bowl XLII over the New England Patriots in his final season in 2007.  After retiring from the NFL, Strahan became a media personality.  He is currently a football analyst on \"Fox NFL Sunday\", and has also served as co-host on the syndicated morning talk show \"Live!  with Kelly and Michael\" with co-host Kelly Ripa from 2012 to 2016, where he was a two-time Daytime Emmy Award winner.  In 2014, he became a regular contributor on the ABC morning television show \"Good Morning America\", and in 2016 the network announced that Strahan would be leaving \"Live!\"  to join \"GMA\" on a full-time basis.  He starred in and produced the short-lived Fox sitcom \"Brothers\" and appeared as host for \"Pros vs. Joes\" alongside fellow Fox football analyst Jay Glazer.  On February 1, 2014, he was elected to the Pro Football Hall of Fame.  As of 2016, he is the host of the ABC game show \"The $100,000 Pyramid\".\n\nChristina Applegate: Christina Applegate (born November 25, 1971) is an American actress and dancer who, as an adolescent actress, started playing the role of Kelly Bundy on the Fox sitcom \"Married... with Children\" (1987–97).  In her adult years, Applegate established a film and television career, winning an Emmy and earning Tony and Golden Globe nominations.  She is also known for doing the voice of Brittany in the \"Alvin and the Chipmunks\" film series.\n\nKim Fields: Kim Victoria Fields (born May 12, 1969) is an American actress and television director.  Fields is known for her roles as Dorothy \"Tootie\" Ramsey on the NBC sitcom \"The Facts of Life\" (1979–88), and as Regina \"Regine\" Hunter on the Fox sitcom \"Living Single\" (1993–98).  Fields is the daughter of actress/director Chip Fields and older sister of actress Alexis Fields.\n\nQuestion: The Book of Life is a film that stars the voice of an American actress who played the roll of Kelly Bundy on what Fox sitcom?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the film.\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the film.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"release_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"actress\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the actress who voiced a character in the film and played the specified role.\"\n        },\n        \"birth_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The birth year of the actress.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"birth_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"sitcom_role\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"character_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the character played by the actress in the sitcom.\"\n        },\n        \"sitcom_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the Fox sitcom.\"\n        },\n        \"network\": {\n          \"type\": \"string\",\n          \"description\": \"The network on which the sitcom aired.\"\n        },\n        \"start_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The start year of the sitcom.\"\n        },\n        \"end_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The end year of the sitcom.\"\n        }\n      },\n      \"required\": [\n        \"character_name\",\n        \"sitcom_title\",\n        \"network\",\n        \"start_year\",\n        \"end_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"final_answer\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the Fox sitcom where the actress played the specified role.\"\n    }\n  },\n  \"required\": [\n    \"film\",\n    \"actress\",\n    \"sitcom_role\",\n    \"final_answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the film."
          },
          "release_year": {
            "type": "integer",
            "description": "The release year of the film."
          }
        },
        "required": [
          "title",
          "release_year"
        ],
        "additionalProperties": false
      },
      "actress": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the actress who voiced a character in the film and played the specified role."
          },
          "birth_year": {
            "type": "integer",
            "description": "The birth year of the actress."
          }
        },
        "required": [
          "name",
          "birth_year"
        ],
        "additionalProperties": false
      },
      "sitcom_role": {
        "type": "object",
        "properties": {
          "character_name": {
            "type": "string",
            "description": "The name of the character played by the actress in the sitcom."
          },
          "sitcom_title": {
            "type": "string",
            "description": "The title of the Fox sitcom."
          },
          "network": {
            "type": "string",
            "description": "The network on which the sitcom aired."
          },
          "start_year": {
            "type": "integer",
            "description": "The start year of the sitcom."
          },
          "end_year": {
            "type": "integer",
            "description": "The end year of the sitcom."
          }
        },
        "required": [
          "character_name",
          "sitcom_title",
          "network",
          "start_year",
          "end_year"
        ],
        "additionalProperties": false
      },
      "final_answer": {
        "type": "string",
        "description": "The title of the Fox sitcom where the actress played the specified role."
      }
    },
    "required": [
      "film",
      "actress",
      "sitcom_role",
      "final_answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
