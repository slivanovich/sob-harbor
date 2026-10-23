{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAngélica Vale: Angélica Vale (born Angélica María Vale Hartman on November 11, 1975 in Mexico City, Mexico) is a Mexican actress, singer, and comedian known also as the daughter of Angélica María, \"La Novia de Mexico\" (Mexico's Sweetheart), and as the daughter of comedian Raúl Vale.  She has been working as an actress for almost 30 years, but achieved fame in 2006 when she became the protagonist of \"La Fea Más Bella\" (\"The Prettiest Ugly Girl\"), a Mexican telenovela, with her real-life mother.  She starred in the webnovela \"No me hallo\" as Luchita Guerra a young woman with a big dream of becoming a singer.  Early in 2012, Vale was a team captain on the Mexican TV Show \"Parodiando\", of Televisa network.\n\nThom Tuck: Thom Tuck (born 28 March 1982) is a British actor and comedian known for being one third of comedy troupe The Penny Dreadfuls and as a Stand-up comedian nominated for the Best Newcomer award at the 2011 Edinburgh Festival Fringe.\n\nJosh Widdicombe: Joshua Michael \"Josh\" Widdicombe ( ; born 8 April 1983) is an English comedian and radio and television presenter, best known for his appearances on \"The Last Leg\" (2012–present), \"Fighting Talk\" (2014–2016), \"Insert Name Here\" (2016–present), \"Have I Got News for You\" (2014–present) and his BBC Three sitcom \"Josh\" (2015–present).\n\nAlan King: Alan King (born Irwin Alan Kniberg; December 26, 1927 – May 9, 2004) was an American actor and comedian known for his biting wit and often angry humorous rants.  King became well known as a Jewish comedian and satirist.  He was also a serious actor who appeared in a number of movies and television shows.  King wrote several books, produced films, and appeared in plays.  In later years, he helped many philanthropic causes.\n\nMark Steel: Mark Steel (born 4 July 1960) is an English comedian, broadcaster, newspaper columnist and author.  A stand-up comedian known for his left-wing beliefs (he was a long-standing member of the Socialist Workers Party) he has made many appearances on radio and television shows as a guest panellist, and has written regular columns in \"The Guardian\" and \"The Independent\".  He is perhaps best known for presenting \"The Mark Steel Lectures\", \"The Mark Steel Revolution\", \"The Mark Steel Solution\" and \"Mark Steel's in Town\".\n\nLeslie Mann: Leslie Mann (born March 26, 1972) is an American actress and comedian known for her roles in comedic films such as \"The Cable Guy\" (1996), \"George of the Jungle\" (1997), \"Big Daddy\" (1999), \"Timecode\" (2000), \"Perfume\" (2001), \"Stealing Harvard\" (2002), \"The 40-Year-Old Virgin\" (2005), \"Knocked Up\" (2007), \"17 Again\" (2009), \"Funny People\" (2009), \"Rio\" (2011), \" The Change-Up\" (2011), \"This Is 40\" (2012), \"The Bling Ring\" (2013), \"The Other Woman\" (2014), \"Vacation\" (2015), and \"How to Be Single\" (2016).\n\nSanket Bhosale: Dr.\"Sanket Bhosale\"'(born 9 May 1988) is an Indian comedian known for his works predominantly in Hindi Television.  He is able to mimic voices of many Bollywood and Hollywood actors.  He is a mimicry artist, actor, comedian, show anchor and a doctor.  He made his mimicry debut with the 2012 Laugh India Laugh.  Bhosale was among of top 10 finalists in Laugh India Laugh.  Recently he has been in the lime light by training Ranbir Kapoor to adopt the style and mannerism of Sanjay Dutt in the Bio-pic Dutt (film).\n\nBu Laia: Bu Laʻia (born as Shawn Kaui Hill in Waimanalo, Hawaii) is a Hawaiian comedian known for his use of Hawaiian pidgin and for wearing a large \"afro style\" wig and blacking out one of his front teeth while performing.  He starred in a cable television show in the early 1990s and released two comic musical albums entitled \"False Crack???\"  and \"Hawaii's Most Wanted.\"  He also attained fame—or notoriety—when he ran for governor of Hawaiʻi in 1994 (when he was too young to legally do so) and again as a member of the Natural Law Party in 2002.  He also attracted attention when he was arrested for riding a skateboard at Honolulu International Airport.  Bu is pidgin for \"Bull\".  The name \"Bu Laʻia\" is a homophone of \"Bull Liar\", a phrase meaning \"an outrageous liar\".  His name is reminiscent of the character created by Hawaiian comedian Kent Bowman, “K.K. Kaumanua” (K.K. Cow–Manure) famous for his \"Pidgin English Children's Stories,\" although Bowman's character uses the pidgin English of an earlier generation.\n\nJosh (TV series): Josh is a British sitcom created by and starring Josh Widdicombe.  A pilot episode aired in 2014 as part of the BBC \"Comedy Feeds\", and a full six-episode series aired from 11 November to 16 December 2015 on BBC Three.  A second series of \"Josh\" was released from 22 September 2016 on Three's now online-only channel.  The day of the final episode of series two on BBC One was released, the BBC announced it had commissioned a third series.\n\nThe Sinbad Show: The Sinbad Show was an American sitcom starring comedian Sinbad that premiered on September 16, 1993 on Fox.  The show's main plot is about a bachelor taking in two orphaned children.  Chuck Brown performed this sitcom's theme music.  It was canceled after one season on April 21, 1994, with two episodes left unaired.\n\nQuestion: Josh is a sitcom starring a comedian known for appearing on what during 2014-2016?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"comedian_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"birth_year\": {\n          \"type\": \"integer\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"birth_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"sitcom_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\"\n        },\n        \"starring_comedian_name\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"starring_comedian_name\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"comedian_appearances_in_period\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"show_title\": {\n            \"type\": \"string\"\n          },\n          \"run_start_year\": {\n            \"type\": \"integer\"\n          },\n          \"run_end_year\": {\n            \"type\": \"integer\"\n          }\n        },\n        \"required\": [\n          \"show_title\",\n          \"run_start_year\",\n          \"run_end_year\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"answer_show_title\": {\n      \"type\": \"string\"\n    }\n  },\n  \"required\": [\n    \"comedian_details\",\n    \"sitcom_details\",\n    \"comedian_appearances_in_period\",\n    \"answer_show_title\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "comedian_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "birth_year": {
            "type": "integer"
          }
        },
        "required": [
          "name",
          "birth_year"
        ],
        "additionalProperties": false
      },
      "sitcom_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string"
          },
          "starring_comedian_name": {
            "type": "string"
          }
        },
        "required": [
          "title",
          "starring_comedian_name"
        ],
        "additionalProperties": false
      },
      "comedian_appearances_in_period": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "show_title": {
              "type": "string"
            },
            "run_start_year": {
              "type": "integer"
            },
            "run_end_year": {
              "type": "integer"
            }
          },
          "required": [
            "show_title",
            "run_start_year",
            "run_end_year"
          ],
          "additionalProperties": false
        }
      },
      "answer_show_title": {
        "type": "string"
      }
    },
    "required": [
      "comedian_details",
      "sitcom_details",
      "comedian_appearances_in_period",
      "answer_show_title"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
