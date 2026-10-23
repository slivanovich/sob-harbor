{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nA Matter of Honor: \"A Matter of Honor\" is the eighth episode of the of the American science fiction television series \"\", the 34th episode overall, first broadcast on February 6, 1989.  The teleplay is written by Burton Armus, based on a story by Armus, Wanda M. Haight and Gregory W. Amos, and directed by Rob Bowman.\n\nThe Battle (Star Trek: The Next Generation): \"The Battle\" is the ninth episode of the of the American science fiction television series \"\" and was originally aired on November 16, 1987, in broadcast syndication.  The episode was written by Herbert Wright, based on a story by Larry Forrester, and directed by Rob Bowman.\n\nHarry Potter and the Goblet of Fire (film): Harry Potter and the Goblet of Fire is a 2005 British-American fantasy film directed by Mike Newell and distributed by Warner Bros.  Pictures.  It is based on the novel of the same name by J. K. Rowling.  The film, which is the fourth instalment in the \"Harry Potter\" film series, was written by Steve Kloves and produced by David Heyman.  The story follows Harry Potter's fourth year at Hogwarts as he is chosen by the Goblet of Fire to compete in the Triwizard Tournament.\n\nThe X-Files (film): The X-Files (also known as The X-Files: Fight the Future) is a 1998 American science fiction thriller film directed by Rob Bowman.  Chris Carter wrote the screenplay.  The story is by Carter and Frank Spotnitz.  It is the first feature film based on Carter's television series \"The X-Files, \" which revolves around fictional unsolved cases called the X-Files and the characters solving them.  Five main characters from the television series appear in the film: David Duchovny, Gillian Anderson, Mitch Pileggi, John Neville, and William B. Davis reprise their respective roles as FBI agents Fox Mulder and Dana Scully, FBI Assistant Director Walter Skinner, Well-Manicured Man, and the Cigarette-Smoking Man.  The film was promoted with the tagline \"Fight the Future\".\n\nMorning Patrol: Morning Patrol (Greek: \"Πρωϊνή Περίπολος\" , tr.  \"Proini Peripolos\") is a 1987 Greek dramatic experimental independent surrealist underground art film directed by Nikos Nikolaidis.  It introduced a new iconography to Nikolaidis' work and contains several elements somewhat resembling the thriller genre and post-apocalyptic science fiction.  The film has an elaborate yet simple script of strongly contrasting moods.  The film's dialogue contains excerpts taken from published works authored by Daphne du Maurier, Philip K. Dick, Raymond Chandler, and Herman Raucher.  It received the Best Director Award and the Greek National Ministry of Culture Award at the Thessaloniki Festival of Greek Cinema in October 1987, where Dinos Katsouridis also won the Best Cinematographer Award and Marie-Louise Bartholomew also won the Best Art Director Award.  The film went on further to be officially selected for screening at Fantasporto in February 1989 where it was nominated for the International Fantasy Film Award and it was also officially selected for screening at the Avoriaz Fantastic Film Festival in January 1987 where it was nominated for the Grand Prize.\n\nElektra (2005 film): Elektra is a 2005 Canadian-American superhero film directed by Rob Bowman.  It is a spin-off from the 2003 film \"Daredevil\", starring the Marvel Comics character Elektra Natchios (portrayed by Jennifer Garner).  The story follows Elektra, an assassin who must protect a man and his prodigy daughter from another assassin who was hired by The Hand.\n\nWhere No One Has Gone Before: \"Where No One Has Gone Before\" is the sixth episode of the American science fiction television series \"\", (episode 1 - 'Encounter at Farpoint' is a two part episode) originally aired October 26, 1987, in broadcast syndication in the United States.  A high-definition, remastered version of the episode received limited theatrical release for one day (with the episode \"Datalore\") to celebrate the 25th anniversary of the series on July 23, 2012.  The story was originally developed with the title \"Where None Have Gone Before\" and was based on Diane Duane's book, \"The Wounded Sky\".  Duane and Michael Reaves pitched the idea to David Gerrold and Gene Roddenberry, and then submitted a script.  Their script was subsequently rewritten by Maurice Hurley, whose first effort was poorly received; however, he subsequently rewrote it again and that version was filmed.  The episode was the first of the series directed by Rob Bowman, who went on to direct twelve more episodes.  It was the only TNG assignment for writers Duane and Reaves.\n\nToo Short a Season: \"Too Short a Season\" is the 16th episode of the of the American science fiction television series \"\".  It first aired on February 8, 1988, in broadcast syndication.  The teleplay was written by Michael Michaelian and D. C. Fontana, based on a story by Michaelian, and the episode was directed by Rob Bowman.\n\nReign of Fire (video game): Reign of Fire is an action-adventure video game released in 2002 by Kuju Entertainment.  The game is based on the movie of the same name, in which dragons have annihilated the majority of the human race, and the survivors attempt to fight back using scavenged military hardware.  However, the plot differs significantly from the film.\n\nReign of Fire (film): Reign of Fire is a 2002 post-apocalyptic fantasy film directed by Rob Bowman and starring Matthew McConaughey and Christian Bale, with the screenplay written by Matt Greenberg, Gregg Chabot, and Kevin Peterka.  The film also features Izabella Scorupco and Gerard Butler.\n\nQuestion: Reign of Fire is what, based on a 2002 post-apocalyptic fantasy film directed by Rob Bowman?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"entity_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the entity being described.\"\n    },\n    \"entity_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of the entity, e.g., 'video game', 'film'.\"\n    },\n    \"based_on_film\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"film_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the film the entity is based on.\"\n        },\n        \"film_release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the film.\"\n        },\n        \"film_genre\": {\n          \"type\": \"string\",\n          \"description\": \"The genre of the film.\"\n        },\n        \"film_director\": {\n          \"type\": \"string\",\n          \"description\": \"The director of the film.\"\n        }\n      },\n      \"required\": [\n        \"film_title\",\n        \"film_release_year\",\n        \"film_genre\",\n        \"film_director\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"game_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"game_genre\": {\n          \"type\": \"string\",\n          \"description\": \"The genre of the video game.\"\n        },\n        \"game_release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the video game.\"\n        },\n        \"developer\": {\n          \"type\": \"string\",\n          \"description\": \"The developer of the video game.\"\n        }\n      },\n      \"required\": [\n        \"game_genre\",\n        \"game_release_year\",\n        \"developer\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"entity_name\",\n    \"entity_type\",\n    \"based_on_film\",\n    \"game_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "entity_name": {
        "type": "string",
        "description": "The name of the entity being described."
      },
      "entity_type": {
        "type": "string",
        "description": "The type of the entity, e.g., 'video game', 'film'."
      },
      "based_on_film": {
        "type": "object",
        "properties": {
          "film_title": {
            "type": "string",
            "description": "The title of the film the entity is based on."
          },
          "film_release_year": {
            "type": "integer",
            "description": "The release year of the film."
          },
          "film_genre": {
            "type": "string",
            "description": "The genre of the film."
          },
          "film_director": {
            "type": "string",
            "description": "The director of the film."
          }
        },
        "required": [
          "film_title",
          "film_release_year",
          "film_genre",
          "film_director"
        ],
        "additionalProperties": false
      },
      "game_details": {
        "type": "object",
        "properties": {
          "game_genre": {
            "type": "string",
            "description": "The genre of the video game."
          },
          "game_release_year": {
            "type": "integer",
            "description": "The release year of the video game."
          },
          "developer": {
            "type": "string",
            "description": "The developer of the video game."
          }
        },
        "required": [
          "game_genre",
          "game_release_year",
          "developer"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "entity_name",
      "entity_type",
      "based_on_film",
      "game_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
