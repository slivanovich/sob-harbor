{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nA Little Game: A Little Game is a 1971 ABC Movie of the Week that was first broadcast on October 30, 1971, starring Mark Gruner as a young boy who will do anything to get what he wants.  In the movie, the plot suggests that he might be responsible for the death of a fellow student at the military academy he attends, yet his mother (Diane Baker) refuses to believe that he could be guilty of anything.  His stepfather (Ed Nelson) begins to wonder if the boy wants to get rid of him.  It was based on the 1968 novel of the same name by Fielden Farrington, who also wrote the screenplay.  The film was directed by Paul Wendkos, who would film another of Farrington's novels for television the following year (\"The Strangers in 7A\").\n\nMa Fleur: Ma Fleur (\"my flower\", in French) is the fourth full-length release and third proper studio album by The Cinematic Orchestra, released on 7 May 2007.  The North American version of the album contains 10 tracks in a different sequence from the UK version and omits \"Child Song\".  The song \"To Build a Home\" was used in an award winning 2008 Schweppes Lemonade advertisement called \"Burst\" and in the 2010 Australian-French film The Tree, and the similar shorter song \"That Home\" in the trailer for 2011 film \"Another Earth\".\n\nRobin Lord Taylor: Robin Lord Taylor (born June 4, 1978) is an American film and television actor and director, known for \"Accepted\" (2006), \"Another Earth\" (2011) and \"Would You Rather\" (2012).  He stars in the television drama series \"Gotham\" as Oswald Cobblepot.\n\nLetters from the Earth: Letters from the Earth is a posthumously published work of celebrated American author Mark Twain (1835–1910).  It comprises essays written during a difficult time in Twain's life (1904–09), when he was deeply in debt and had recently lost his wife and one of his daughters.  The content concerns morality and religion and strikes a sarcastic — Twain's own term throughout the book — tone.  Initially, another of his daughters, Clara Clemens, objected to its publication in March 1939, probably because of its controversial and iconoclastic views on religion, claiming it presented a \"\"distorted\"\" view of her father.  Henry Nash Smith helped change her position in 1960.  Clara explained her change of heart in 1962 saying that \"\"Mark Twain belonged to the world\"\" and that public opinion had become more tolerant.  She was also influenced to release the papers by her annoyance with Soviet reports that her father's ideas were being suppressed in the United States.  The papers were selected, edited and sequenced for the book in 1939 by Bernard DeVoto.\n\nWilliam Mapother: William Reibert Mapother Jr. ( ; born April 17, 1965) is an American actor, best known for his role as Ethan Rom on the television series \"Lost\".\n\nWarrior of the Lost World: Warrior of the Lost World (also known as Mad Rider) is a 1983 Italian post-apocalyptic science fiction film written and directed by David Worth, starring Robert Ginty, Persis Khambatta, and Donald Pleasence.  It was created and first released in Italy under the title Il Giustiziere della terra perduta (\"Vigilante of the Lost Earth\") in 1983 during the wide popularity of the \"Mad Max\" films, and many subsequently created post-apocalyptic films of the 1980s.  Later the film was given another Italian title for VHS and television markets, I predatori dell'anno Omega (\"Raiders of the Omega year\").\n\nAnother Earth: Another Earth is a 2011 American independent science fiction-drama film directed by Mike Cahill.  It stars Brit Marling, William Mapother, and Robin Lord Taylor.  It premiered at the 27th Sundance Film Festival in January 2011, and was distributed by Fox Searchlight Pictures.\n\nWT1190F: WT1190F (9U01FF6, UDA34A3, or UW8551D) was a small temporary satellite of Earth that impacted Earth on 13 November 2015 at 06:18:34.3 (±1.3 seconds) UTC.  It is thought to have been space debris from the trans-lunar injection stage of the 1998 Lunar Prospector mission, It was first discovered on 18 February 2013 by the Catalina Sky Survey.  It was then lost, and reacquired on 29 November 2013.  It was again discovered on 3 October 2015, and the object was soon identified to be the same as the two objects previously sighted by the team, who have been sharing their data through the International Astronomical Union's Minor Planet Center (MPC).  An early orbit calculation showed that it was orbiting Earth in an extremely elliptical orbit, taking it from within the geosynchronous satellite ring to nearly twice the distance of the Moon.  It was also probably the same object as 9U01FF6, another object on a similar orbit discovered on 26 October 2009.\n\nBrit Marling: Brit Heyworth Marling (born August 7, 1982) is an American actress, screenwriter and film producer.  She first gained recognition in 2004 with the documentary \"Boxers and Ballerinas\" and later became a Sundance star with the Searchlight films \"Sound of My Voice\" (2011), \"Another Earth\" (2011) and \"The East\" (2013) which she co-wrote in addition to playing the lead role.  She starred in the 2016 Netflix series \"The OA\", which she co-created with Zal Batmanglij.\n\nList of Robotech characters: This is a list of the major characters in \"Robotech\", the American adaptation of three Japanese animated series: \"The Super Dimension Fortress Macross\", \"The Super Dimension Cavalry Southern Cross\", and \"Genesis Climber Mospeada\", as a single TV series.  The series is divided into parts called \"generations\" which are subtitled \"The Macross Saga\", \"The Second Generation\", and \"The New Generation\".  A fourth series was planned but was canceled, with only a few episodes being produced which were later combined into a movie \"\".  In 2006, a new feature film was released called \"\" as well as a prelude comic \"\".  The story mainly follows members of the Robotech Armed Forces, a fictional military force depicted in the series.  After the events of the Macross saga the Robotech Expeditionary Force is formed which leaves Earth to hunt for the Robotech Masters.  In the later part of the series they are involved with battles against the Invid.  In the fictional world of Robotech, the characters are also involved in four Robotech Wars.  They begin with the first battle between the SDF-1 and Zentradi (First Robotech War) and continue after the Robotech Masters try to Invade Earth (Second Robotech War).  The third Robotech War is fought against the Invid, and the Fourth and final war is fought against another alien race known as the Haydonites.\n\nQuestion: Which actor from \"Lost\" is also in the film Another Earth?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the actor.\"\n    },\n    \"film_appearances\": {\n      \"type\": \"array\",\n      \"description\": \"List of films the actor appeared in.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"title\": {\n            \"type\": \"string\",\n            \"description\": \"The title of the film.\"\n          }\n        },\n        \"required\": [\n          \"title\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"tv_series_appearances\": {\n      \"type\": \"array\",\n      \"description\": \"List of TV series the actor appeared in, with their role.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"title\": {\n            \"type\": \"string\",\n            \"description\": \"The title of the TV series.\"\n          },\n          \"role\": {\n            \"type\": \"string\",\n            \"description\": \"The character role played in the TV series.\"\n          }\n        },\n        \"required\": [\n          \"title\",\n          \"role\"\n        ],\n        \"additionalProperties\": false\n      }\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"film_appearances\",\n    \"tv_series_appearances\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The full name of the actor."
      },
      "film_appearances": {
        "type": "array",
        "description": "List of films the actor appeared in.",
        "items": {
          "type": "object",
          "properties": {
            "title": {
              "type": "string",
              "description": "The title of the film."
            }
          },
          "required": [
            "title"
          ],
          "additionalProperties": false
        }
      },
      "tv_series_appearances": {
        "type": "array",
        "description": "List of TV series the actor appeared in, with their role.",
        "items": {
          "type": "object",
          "properties": {
            "title": {
              "type": "string",
              "description": "The title of the TV series."
            },
            "role": {
              "type": "string",
              "description": "The character role played in the TV series."
            }
          },
          "required": [
            "title",
            "role"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": [
      "actor_name",
      "film_appearances",
      "tv_series_appearances"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
