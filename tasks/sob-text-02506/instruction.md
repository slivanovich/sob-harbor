{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Ugly: The Ugly is a 1997 New Zealand horror film, the first feature directed and written by Scott Reynolds.  The film starred Paolo Rotondo, Rebecca Hobbs, Jennifer Ward-Lealand, and Roy Ward.  The film is about a psychiatrist that is meeting with a serial killer to determine whether or not he has been successfully cured.  They delve into a journey through his past and his victims, and through this \"The Ugly,\" a distorted allusion to The Ugly Duckling, is revealed.  It was nominated for best film awards at festivals in New Zealand, Portugal and the United States.\n\nTriumphs of a Man Called Horse: Triumphs of a Man Called Horse is a 1983 American Western film directed by John Hough and starring Richard Harris, Michael Beck and Ana De Sade.  Harris reprised his role as British aristocrat John Morgan, 8th Earl of Kildare, who becomes a member of the Lakota Sioux.  It was the final film of the trilogy after \"A Man Called Horse\" (1970) and \"The Return of a Man Called Horse\" (1976).\n\nList of The Almighty Johnsons episodes: \"The Almighty Johnsons\" is a New Zealand fantasy comedy-drama television series, which was created by James Griffin and Rachel Lang and is produced by South Pacific Pictures.  It began airing its first series of ten episodes in New Zealand on 7 February 2011.  The second series of 13 episodes began broadcasting on 29 February 2012.  A third series of 13 episodes premiered on 4 July 2013.\n\n2012 New Zealand Television Awards: The 2012 New Zealand Television Awards were the new name of the New Zealand television industry awards, following the demise of the Aotearoa Film and Television Awards.  The awards were held on Saturday 3 November at The Great Room of the Langham hotel in Auckland, New Zealand, with highlights screening on TV ONE on Sunday 4 November.  The New Zealand Television Awards took a similar format to the previous Qantas Television Awards, honouring excellence in New Zealand television and television journalism.  This was the final New Zealand television awards presentation organised by Think TV, after Television New Zealand withdrew its support in 2013.\n\nThe Hunchback (1997 film): The Hunchback is a 1997 New Zealand fantasy television film based on Victor Hugo's iconic 1831 novel \"The Hunchback of Notre-Dame\", directed by Peter Medak and produced by Stephane Reichel.  It stars Richard Harris as Claude Frollo, Salma Hayek as Esmeralda and Mandy Patinkin as Quasimodo, the titular hunchback of Notre Dame.\n\nThe Almighty Johnsons: The Almighty Johnsons is a New Zealand fantasy comedy/drama television series, which was created by James Griffin and Rachel Lang and was produced by South Pacific Pictures and aired from 7 February 2011 to 23 September 2013.\n\nRichard Harris: Richard St John Harris (1 October 1930 – 25 October 2002) was an Irish actor and singer.  He appeared on stage and in many films, appearing as Frank Machin in \"This Sporting Life\", for which he was nominated for the Academy Award for Best Actor, King Arthur in the 1967 film \"Camelot\" and the subsequent 1981 revival of the show.  He played an aristocrat and prisoner in \"A Man Called Horse\" (1970), a gunfighter in Clint Eastwood's Western film \"Unforgiven\" (1992), Emperor Marcus Aurelius in \"Gladiator\" (2000), and Albus Dumbledore in the first two \"Harry Potter\" films: \"the Philosopher's Stone\" (2001) and \"the Chamber of Secrets\" (2002).  Harris had a number one hit in Australia and Canada and a top ten hit in the United Kingdom and United States with his 1968 recording of Jimmy Webb's song \"MacArthur Park\".\n\n1997 New Zealand NBL season: The 1997 New Zealand National Basketball League season was the 16th running of the competition.  The early 1990s held dwindling fortunes New Zealand basketball, with TV coverage reduced, sponsorships dwindled and crowd numbers on the decline.  At the end of the 1996 season, both the Wellington Saints and the Hutt Valley Lakers were struggling to survive.  They amalgamated for the 1997 season and succeeded in signing a naming rights sponsorship deal with TransAlta.\n\nA Man Called Horse (film): A Man Called Horse is a 1970 American Western film starring Richard Harris and directed by Elliot Silverstein.  Based on a short story by Dorothy M. Johnson, \"A Man Called Horse\", published in 1950 in \"Collier's\" magazine and again in 1968 in Johnson's book \"Indian Country\".  The basic story was used in a 1958 episode of the TV show \"Wagon Train\" titled \"A Man Called Horse\".  Partially spoken in Sioux, the film tells the story of an English aristocrat who is captured by the Sioux people.\n\nSV Nilaya: SV Nilaya is a 16-metre long steel yacht built in Auckland, New Zealand in 1997.  The vessel is a custom steel pilothouse yacht built to superyacht standards.  \"SV Nilaya's\" systems are 'works of art' and were designed for ease of maintenance and operation.  In 2012, it was believed to be sailing towards Antarctica crewed by Jarle Andhøy and Samuel Massie, among others.  Their intention appears to be to investigate the disappearance of their yacht \"Berserk II\", which sank in February 2011 killing three people.  New Zealand authorities are searching for the yacht, as there is no authority issued for the journey to Antarctica.  The vessel was reregisterd under a Russian flag.  It left Auckland New Zealand on 23 January 2012.  new Zealand Customs attempted a search.\n\nQuestion: The Hunchback is a 1997 New Zealand fantasy television film starring, among others, Richard Harris, who played an aristocrat and prisoner in what film? \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor.\"\n    },\n    \"role_description\": {\n      \"type\": \"string\",\n      \"description\": \"Description of the role played by the actor.\"\n    },\n    \"film_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the film.\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the film.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"release_year\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"role_description\",\n    \"film_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The name of the actor."
      },
      "role_description": {
        "type": "string",
        "description": "Description of the role played by the actor."
      },
      "film_details": {
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
      }
    },
    "required": [
      "actor_name",
      "role_description",
      "film_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
