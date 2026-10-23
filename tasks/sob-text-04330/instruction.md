{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSpecial Tony Award: The Special Tony Award category includes the Lifetime Achievement Award and Special Tony Award.  These are non-competitive honorary awards, and the titles have changed over the years.  The Tony Award for Lifetime Achievement in the Theatre is to \"honor an individual for the body of his or her work.\"  (The Tony Award for Best Special Theatrical Event was a competitive award, given from 2001 to 2009.)  Another non-competitive Tony award is the Tony Honors for Excellence in Theatre, to \"recognize the achievements of individuals and organizations that do not fit into any of the competitive categories.\"\n\nJoanna Lumley: Joanna Lamond Lumley, {'1': \", '2': \", '3': \", '4': \"} (born 1 May 1946) is an English actress, former model, author and activist.  She won two BAFTA TV Awards for her role as Patsy Stone in the BBC sitcom \"Absolutely Fabulous\" (1992–2012), and was nominated for the 2011 Tony Award for Best Featured Actress in a Play for the Broadway revival of \"La Bête\".  In 2013, she received the Special Recognition Award at the National Television Awards and in 2017, she was honoured with the BAFTA Fellowship award.\n\nLouis Jenkins: Louis Jenkins (born October 28, 1942) is an American prose poet from Enid, Oklahoma.  He lived in Duluth, Minnesota, for over 30 years with his wife Ann.  His poems have been published in a number of literary magazines and anthologies.  Jenkins has been a guest on \"A Prairie Home Companion\" numerous times and has also been featured on \"The Writer's Almanac\".  The author's book, \"Nice Fish\", was winner of the Minnesota Book Award in 1995.  His book \"Just Above Water\" won the Northeastern Minnesota Book Award in 1997.  In 1996, Jenkins was a featured poet at the Geraldine R. Dodge Poetry Festival.  Actor Mark Rylance recited works by Jenkins in lieu of formal acceptance speeches after winning a Tony Award and a Drama Desk Award for the play \"Boeing-Boeing\" (in 2008) and after winning his Tony Award for the play \"Jerusalem\" (in 2011).\n\nList of Jewish American entertainers: Persons listed with a double asterisk (**) are producers who have won the Tony Award for Best Musical and/or the Tony Award for Best Play.  Those listed with a triple asterisk (***) have won the Tony Award for Best Direction of a Musical and/or Play.  Those listed with a quadruple asterisk (****) have won the Tony Award for Best Actor or Best Actress in a Musical or Play.\n\nTony Award for Best Featured Actor in a Play: The Tony Award for Best Performance by an Actor in a Featured Role in a Play is an honor presented at the Tony Awards, a ceremony established in 1947 as the Antoinette Perry Awards for Excellence in Theatre, to actors for quality supporting roles in a Broadway play.  Honors in several categories are presented at the ceremony annually by the Tony Award Productions, a joint venture of The Broadway League and the American Theatre Wing, to \"honor the best performances and stage productions of the previous year.\"  Originally called the Tony Award for Actor, Supporting or Featured (Dramatic), it was later changed to its current title in 1976.  Before 1956, nominees' names were not made public.  The change was made by the awards committee to \"have a greater impact on theatregoers\".\n\nMark Rylance: Sir David Mark Rylance Waters (born 18 January 1960) is an English actor, theatre director, and playwright.  He was the first artistic director of Shakespeare's Globe in London, from 1995 to 2005.  His film appearances include \"Prospero's Books\" (1991), \"Angels and Insects\" (1995), \"Institute Benjamenta\" (1996), and \"Intimacy\" (2001).  Rylance won the Academy Award and the BAFTA Award for Best Supporting Actor for his portrayal of Rudolf Abel in \"Bridge of Spies\" (2015).\n\nJohn Benjamin Hickey: John Benjamin Hickey (born June 25, 1963) is an American actor with a career in stage, film and television.  He won the 2011 Tony Award for Best Performance by a Featured Actor in a Play for his performance as Felix Turner in \"The Normal Heart\".\n\nHarvey Fierstein: Harvey Forbes Fierstein (born June 6, 1954) is an American actor, playwright, and voice actor.  Fierstein has won the Tony Award for Best Actor in a Play for his own play \"Torch Song Trilogy\" (about a gay drag-performer and his quest for true love and family) and the Tony Award for Best Actor in a Musical for playing Edna Turnblad in \"Hairspray\".  He also wrote the book for the musical \"La Cage aux Folles\", for which he won the Tony Award for Best Book of a Musical, and wrote the book for the Tony Award-winning \"Kinky Boots\".  He was inducted into the American Theater Hall of Fame in 2007.\n\nNina Arianda: Nina Arianda Matijcio (born September 18, 1984) is an American actress.  She won the 2012 Tony Award for Best Actress in a Play for her performance as Vanda Jordan in \"Venus in Fur\", and was nominated for the 2011 Tony Award for Best Actress in a Play for portraying Billie Dawn in \"Born Yesterday\".  In 2016, she began starring in Amazon Studios' legal series \"Goliath\".\n\nGood People (play): Good People is a 2011 play by David Lindsay-Abaire.  The world premiere was staged by the Manhattan Theatre Club in New York City.  The production was nominated for two 2011 Tony Awards – Best Play and Best Leading Actress in a Play (Frances McDormand), with the latter winning.\n\nQuestion: What English actor won a 2011 Tony Award?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the actor.\"\n    },\n    \"actor_nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the actor.\"\n    },\n    \"awards_won\": {\n      \"type\": \"array\",\n      \"description\": \"A list of awards won by the actor in the specified year.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"award_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the award won.\"\n          },\n          \"award_year\": {\n            \"type\": \"integer\",\n            \"description\": \"The year the award was won.\"\n          },\n          \"winning_work\": {\n            \"type\": \"string\",\n            \"description\": \"The work for which the award was received.\"\n          }\n        },\n        \"required\": [\n          \"award_name\",\n          \"award_year\",\n          \"winning_work\"\n        ],\n        \"additionalProperties\": false\n      }\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"actor_nationality\",\n    \"awards_won\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The full name of the actor."
      },
      "actor_nationality": {
        "type": "string",
        "description": "The nationality of the actor."
      },
      "awards_won": {
        "type": "array",
        "description": "A list of awards won by the actor in the specified year.",
        "items": {
          "type": "object",
          "properties": {
            "award_name": {
              "type": "string",
              "description": "The name of the award won."
            },
            "award_year": {
              "type": "integer",
              "description": "The year the award was won."
            },
            "winning_work": {
              "type": "string",
              "description": "The work for which the award was received."
            }
          },
          "required": [
            "award_name",
            "award_year",
            "winning_work"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": [
      "actor_name",
      "actor_nationality",
      "awards_won"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
