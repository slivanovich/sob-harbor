{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJoel Blum: Joel Blum is an American stage actor.  He was nominated for the Tony Award for Best Featured Actor in a Musical twice.  The first was in 1995 for his role as Frank in the Broadway revival of \"Show Boat\".  The second nomination was in 1997 for playing Buddy Becker in the original production of \"Steel Pier\".  He was also nominated for the Drama Desk Award for Outstanding Featured Actor in a Musical for his role in \"Golf: The Musical\".  He was also part of the original production of \"42nd Street\".  Other Broadway roles include \"Stardust, The Music Man\" and \"Debbie Reynolds On Broadway\".  He also played George in the second U.S. national tour of \"Billy Elliot the Musical\". , and Detective Marks/Man in the Off-Broadway musical \"Kid Victory\". .\n\nWhat They Had: What They Had is an upcoming American drama film written and directed by Elizabeth Chomko.  It stars Hilary Swank, Michael Shannon, Robert Forster, Blythe Danner, and Taissa Farmiga.  The film will be released in the United States by Bleecker Street.\n\nRichard Griffiths: Richard Thomas Griffiths, OBE (31 July 1947 – 28 March 2013) was an English actor of film, television, and stage.  He received the Laurence Olivier Award for Best Actor, the Drama Desk Award for Outstanding Actor in a Play, the Outer Critics Circle Award for Best Featured Actor and the Tony Award for Best Performance by a Leading Actor in a Play, all for his role in \"The History Boys\".  For the 2006 film adaptation, Griffiths was nominated for the BAFTA Award for Best Actor in a Leading Role.\n\nAirline Highway (play): Airline Highway is an American play, written by Lisa D'Amour and set in New Orleans.  Commissioned by the Steppenwolf Theatre Company, the play made its Broadway debut in April 2015.  It received four Tony Award nominations, including Best Featured Actor in a Play for K. Todd Freeman and Best Featured Actress in a Play for Julie White.  Additionally, it received three Drama Desk Award nominations, winning one for Freeman.  Its final performance was on June 7, 2015.\n\nArian Moayed: Arian Moayed (born April 15, 1980) is an Iranian-born American actor and theater producer.  Moayed received a Tony Award nomination for Best Featured Actor in a Play in 2011 for his performance as Musa in \"Bengal Tiger at the Baghdad Zoo\".\n\nMichael Cerveris: Michael Cerveris (born November 6, 1960) is an American actor, singer, and guitarist.  He has performed in many stage musicals and plays, including several Stephen Sondheim musicals: \"Assassins\", \"Sweeney Todd\", \"Road Show\", and \"Passion\".  In 2004, Cerveris won the Tony Award as Best Featured Actor in a Musical for \"Assassins\" as John Wilkes Booth.  In 2015, he won his second Tony Award as Best Actor in a Musical for \"Fun Home\" as Bruce Bechdel.\n\nKen Howard: Kenneth Joseph \"Ken\" Howard Jr. (March 28, 1944 – March 23, 2016) was an American actor, best known for his roles as Thomas Jefferson in \"1776\" and as basketball coach and former Chicago Bulls player Ken Reeves in the television show \"The White Shadow\" (1978–1981).  Howard won the Tony Award for Best Featured Actor in a Play in 1970 for his performance in \"Child's Play\", and later won the Primetime Emmy Award for Outstanding Supporting Actor in a Miniseries or a Movie for his work in \"Grey Gardens\" (2009).\n\nMichael Shannon: Michael Corbett Shannon (born August 7, 1974) is an American actor and musician.  He has been nominated twice for the Academy Award for Best Supporting Actor for his roles in \"Revolutionary Road\" (2008) and \"Nocturnal Animals\" (2016), further earning Screen Actors Guild Award and Golden Globe Award nominations for his role in \"99 Homes\" (2014).  He received a Tony Award nomination for Best Featured Actor in a Play for \"Long Day's Journey into Night\" (2016).\n\nNick Cordero: Nick Cordero is a Canadian actor.  He appeared on Broadway in 2014 in the musical \"Bullets Over Broadway\" in the role of Cheech, for which he was nominated for the Tony Award for Best Featured Actor in a Musical and the Drama Desk Award for Outstanding Featured Actor in a Musical.  He won the Outer Critics Circle Award for Outstanding Featured Actor in a Musical and a Theater World Award for the role.  He originated the title role in the Off-Broadway production of \"The Toxic Avenger\".  He also played the role of Dennis in \"Rock of Ages\" on Broadway in 2012 and on tour.  In March 2016, he joined the Broadway production of \"Waitress\", playing the role of Earl.  He left \"Waitress\" to join the Broadway premier of the musical \"A Bronx Tale\", as \"Sonny\" at the Longacre Theatre starting on November 3, 2016.\n\nBiloxi Blues: Biloxi Blues is a semi-autobiographical play by Neil Simon.  It portrays the conflict of Sergeant Merwin J. Toomey and Arnold Epstein, one of many privates enlisted in the military stationed in Biloxi, Mississippi, seen through the eyes of Eugene Jerome, one of the other soldiers.  This play is the second chapter in what is known as his \"Eugene trilogy\", following \"Brighton Beach Memoirs\" and preceding \"Broadway Bound\", and is the only one in which Eugene is not the central character.  The play won the Tony Award for Best Play, and Barry Miller won a Tony Award for Best Featured Actor in a Play for his performance as Arnold Epstein.\n\nQuestion: What american actor, who starred in the film What They Had, also received a Tony Award nomination for Best Featured Actor in a Play in 2016?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the American actor.\"\n    },\n    \"film_starred_in\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the film the actor starred in.\"\n    },\n    \"award_nomination\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"award_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the award.\"\n        },\n        \"award_category\": {\n          \"type\": \"string\",\n          \"description\": \"The specific category of the award nomination.\"\n        },\n        \"nomination_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the award nomination was received.\"\n        },\n        \"production_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the production for which the actor was nominated.\"\n        },\n        \"production_type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of production (e.g., 'play', 'musical').\"\n        }\n      },\n      \"required\": [\n        \"award_name\",\n        \"award_category\",\n        \"nomination_year\",\n        \"production_name\",\n        \"production_type\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"film_starred_in\",\n    \"award_nomination\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The name of the American actor."
      },
      "film_starred_in": {
        "type": "string",
        "description": "The name of the film the actor starred in."
      },
      "award_nomination": {
        "type": "object",
        "properties": {
          "award_name": {
            "type": "string",
            "description": "The name of the award."
          },
          "award_category": {
            "type": "string",
            "description": "The specific category of the award nomination."
          },
          "nomination_year": {
            "type": "integer",
            "description": "The year the award nomination was received."
          },
          "production_name": {
            "type": "string",
            "description": "The name of the production for which the actor was nominated."
          },
          "production_type": {
            "type": "string",
            "description": "The type of production (e.g., 'play', 'musical')."
          }
        },
        "required": [
          "award_name",
          "award_category",
          "nomination_year",
          "production_name",
          "production_type"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "actor_name",
      "film_starred_in",
      "award_nomination"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
