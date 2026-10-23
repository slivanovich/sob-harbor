{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGuys and Dolls (film): Guys and Dolls is a 1955 musical film starring Marlon Brando, Jean Simmons, Frank Sinatra and Vivian Blaine.  The film was made by Samuel Goldwyn Productions and distributed by MGM.  It was directed by Joseph L. Mankiewicz, who also wrote the screenplay.  The film is based on the 1950 Broadway musical by composer and lyricist Frank Loesser, with a book by Jo Swerling and Abe Burrows based on \"The Idyll Of Miss Sarah Brown\" and \"Blood Pressure\", two short stories by Damon Runyon.  Dances were choreographed by Michael Kidd, who had also staged the dances for the Broadway production.\n\nJohn Houseman: John Houseman (born Jacques Haussmann; September 22, 1902October 31, 1988) was a British-American actor and producer who became known for his highly publicized collaboration with director Orson Welles from their days in the Federal Theatre Project through to the production of \"Citizen Kane\" and his storied collaboration with writer Raymond Chandler's intoxicated screenplay rendering as producer of \"The Blue Dahlia.\"  He is perhaps best known for his role as Professor Charles W. Kingsfield in the film \"The Paper Chase\" (1973), for which he won the Academy Award for Best Supporting Actor.  He reprised his role as Kingsfield in the subsequent television series adaptation of \"The Paper Chase\".  Houseman was also known for his commercials for the brokerage firm Smith Barney.  He had a distinctive Mid-Atlantic English accent, in common with many actors of his generation.\n\nWilliam Kellner: William Kellner (30 July 1900 – May, 1996) was an Austrian-born art director who worked primarily on British films in the 1940s and 1950s.  He began his career as a draughtsman working for Michael Powell and Emeric Pressburger on their films \"A Canterbury Tale\" (1944) and \"I Know Where I'm Going! \" (1945) and on David Lean's \"Brief Encounter\" in 1946.  He was also art director on two Ealing Comedies, \"Kind Hearts and Coronets\" (1949) and \"the Lavender Hill Mob\" (1951).  Kellner was nominated for two Oscars, in 1949 for Basil Dearden's \"Saraband for Dead Lovers\" and in 1959 for Joseph L. Mankiewicz's adaptation of Tennessee Williams' \"Suddenly Last Summer\".  He worked on two Anthony Asquith all-star productions, \"The V.I.P.s\" and \"The Yellow Rolls-Royce\", both in 1964, before retiring in 1965.\n\nCleopatra (1963 film): Cleopatra is a 1963 American epic historical drama film chronicling the struggles of Cleopatra VII, the young Queen of Egypt, to resist the imperial ambitions of Rome.  It was directed by Joseph L. Mankiewicz and shot in the 70 mm Todd-AO format, with a screenplay adapted by Mankiewicz, Ranald MacDougall and Sidney Buchman from a book by Carlo Maria Franzero.  The film stars Elizabeth Taylor, Richard Burton, Rex Harrison, Roddy McDowall, and Martin Landau.\n\nJulius Caesar (1953 film): Julius Caesar is a 1953 epic Metro-Goldwyn-Mayer film adaptation of the play by Shakespeare, directed by Joseph L. Mankiewicz, who also wrote the uncredited screenplay, and produced by John Houseman.  The original music score is by Miklós Rózsa.  The film stars Marlon Brando as Mark Antony, James Mason as Brutus, John Gielgud as Cassius, Louis Calhern as Julius Caesar, Edmond O'Brien as Casca, Greer Garson as Calpurnia, and Deborah Kerr as Portia.\n\nFrancis Mankiewicz: Francis Mankiewicz (March 15, 1944 in Shanghai, China – August 14, 1993 in Montreal, Quebec, Canada) was a Canadian film director, screenwriter and producer.  In 1945, his family moved to Montreal, where Francis spent all his childhood.  His father was a second cousin to the famous Hollywood brothers, Joseph L. Mankiewicz and Herman J. Mankiewicz.\n\nSleuth (1972 film): Sleuth is a 1972 British mystery thriller film directed by Joseph L. Mankiewicz and starring Laurence Olivier and Michael Caine.  The screenplay by playwright Anthony Shaffer was based on his 1970 Tony Award-winning play.  Both Olivier and Caine were nominated for Academy Awards for their performances.  This was Mankiewicz's final film.  Critics gave the film overwhelmingly positive reviews, and would later note similarities between it and Caine's 1982 film \"Deathtrap\".\n\nPeople Will Talk: People Will Talk is a 1951 romantic comedy/drama film directed by Joseph L. Mankiewicz and produced by Darryl F. Zanuck from a screenplay by Mankiewicz, based on the German play by Curt Goetz, which had been made into a movie in Germany (\"Doctor Praetorius\", 1950).  Released by Twentieth Century Fox, the film stars Cary Grant and Jeanne Crain, with supporting performances by Hume Cronyn, Finlay Currie, Walter Slezak, and Sidney Blackmer.\n\nEdward Carfagno: Edward Carfagno (November 28, 1907 – December 28, 1996) was an art director who established himself in the 1950s with his Oscar-winning work on such films as Vincente Minnelli's \"The Bad and the Beautiful\" (1952), Joseph Mankiewicz's \"Julius Caesar\" (1953) and William Wyler's \"Ben-Hur\" (1959).  Carfagno went on to work consistently on a variety of films, including five collaborations with Clint Eastwood including \"Tightrope\" (1984) and \"Heartbreak Ridge\" (1987).\n\nDragonwyck (film): Dragonwyck is a 1946 American period drama film made by Twentieth Century-Fox.  It was directed by Joseph L. Mankiewicz and produced by Darryl F. Zanuck and Ernst Lubitsch (uncredited) from a screenplay by Mankiewicz, based on the novel \"Dragonwyck\" by Anya Seton.  The music score was by Alfred Newman and the cinematography by Arthur C. Miller.  The film stars Gene Tierney, Walter Huston and Vincent Price.\n\nQuestion: Edward Carfagno, was an art director who established himself in the 1950s with his Oscar-winning work on such films as which 1953 epic Metro-Goldwyn-Mayer film adaptation of the play by Shakespeare, directed by Joseph L. Mankiewicz, who also wrote the uncredited screenplay, and produced by John Houseman?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the film was released.\"\n    },\n    \"director\": {\n      \"type\": \"string\",\n      \"description\": \"The director of the film.\"\n    },\n    \"producer\": {\n      \"type\": \"string\",\n      \"description\": \"The producer of the film.\"\n    },\n    \"studio\": {\n      \"type\": \"string\",\n      \"description\": \"The studio that produced or distributed the film.\"\n    },\n    \"based_on_play_by\": {\n      \"type\": \"string\",\n      \"description\": \"The author of the play the film is adapted from.\"\n    },\n    \"art_director_contribution\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the art director.\"\n        },\n        \"oscar_winning_work\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the art director's work on this film was Oscar-winning.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"oscar_winning_work\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"director\",\n    \"producer\",\n    \"studio\",\n    \"based_on_play_by\",\n    \"art_director_contribution\"\n  ],\n  \"additionalProperties\": false\n}"
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
        "description": "The year the film was released."
      },
      "director": {
        "type": "string",
        "description": "The director of the film."
      },
      "producer": {
        "type": "string",
        "description": "The producer of the film."
      },
      "studio": {
        "type": "string",
        "description": "The studio that produced or distributed the film."
      },
      "based_on_play_by": {
        "type": "string",
        "description": "The author of the play the film is adapted from."
      },
      "art_director_contribution": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the art director."
          },
          "oscar_winning_work": {
            "type": "boolean",
            "description": "Indicates if the art director's work on this film was Oscar-winning."
          }
        },
        "required": [
          "name",
          "oscar_winning_work"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_title",
      "release_year",
      "director",
      "producer",
      "studio",
      "based_on_play_by",
      "art_director_contribution"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
