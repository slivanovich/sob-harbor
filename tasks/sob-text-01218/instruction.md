{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRose Marie: Rose Marie Mazetta (born August 15, 1923), known professionally as Rose Marie, is an American actress.  As a child performer she had a successful singing career as Baby Rose Marie.  A veteran of vaudeville and one of its last surviving stars, her career includes film, radio, records, theater, night clubs and television.  Her most famous role was television comedy writer Sally Rogers on the CBS situation comedy \"The Dick Van Dyke Show\".  She later portrayed Myrna Gibbons on \"The Doris Day Show\" and was also a frequent panelist on the game show \"Hollywood Squares\".  She was the first major star to be known simply by her first names and is the subject of a documentary film \"Wait for Your Laugh\" (2017) which features interviews from numerous co-stars, including Carl Reiner, Dick Van Dyke, Peter Marshall and Tim Conway.\n\nAnother Time (Andrew's Song): \"Another Time (Andrew's Song)\" is a song by American singer Annaleigh Ashford and her close friend and music artist, Will Van Dyke.  The song was written by Van Dyke and produced by Derik Lee.  It was released on iTunes and Van Dyke's website on January 14, 2014.  It was written for Van Dyke's fiancé, casting associate Andrew Femenella, and is featured in Ashford's cabaret show, \"Lost in the Stars\" .  \"Another Time (Andrew's Song)\" is an Easy Listening track.  In addition to writing music and lyrics, Van Dyke is featured on piano on the single.  The track also features Michael Aarons (guitar), Steve Gilewski (bass), Sammy Merendino (drums), Philip Payton (violin/viola), and Allison Seidner (cello).  It was recorded at Harlem Parlour Recording, NYC by Derik Lee, who also mixed and mastered the recording.\n\nTop Banana (film): Top Banana is a 1954 musical film based on the musical of the same name, starring Phil Silvers, and featuring Rose Marie, Judy Lynn, Jack Albertson and Joey Faye, all of whom reprised their roles from the Broadway production of the musical.\n\nThe New Dick Van Dyke Show: The New Dick Van Dyke Show is an American sitcom starring Dick Van Dyke that aired on CBS from 1971 to 1974.  It was Van Dyke's first return to series television since \"The Dick Van Dyke Show\".\n\nList of The Dick Van Dyke Show episodes: \"The Dick Van Dyke Show\" is an American television sitcom starring Dick Van Dyke as Rob Petrie, Mary Tyler Moore as Laura Petrie, Morey Amsterdam as Buddy Sorrell, Rose Marie as Sally Rogers, and Richard Deacon as Mel Cooley.\n\nBarry Van Dyke: Barry Van Dyke (born July 31, 1951) is an American actor and the second son of actor and entertainer Dick Van Dyke as well as the stepson of makeup artist Arlene Silver-Van Dyke and nephew of Jerry Van Dyke.  He was best known to audiences as Lieutenant Detective Steve Sloan, a homicide detective and the son of (played by Dick Van Dyke) on \"\".  In the show, the characters' relatives were frequently played by real-life family members.\n\nThe Van Dyke Show: The Van Dyke Show is an American sitcom starring Dick Van Dyke and his son Barry Van Dyke which aired on CBS from October 26 to December 7, 1988.  The series marked the first time the real-life father-son actors worked together.\n\nThe Dick Van Dyke Show: The Dick Van Dyke Show is an American television sitcom that initially aired on CBS from October 3, 1961 to June 1, 1966, with a total of 158 half-hour episodes spanning over five seasons.  The show was created by Carl Reiner and starred Dick Van Dyke, Rose Marie, Morey Amsterdam, Larry Mathews, and Mary Tyler Moore.  It centered on the work and home life of television comedy writer Rob Petrie (Van Dyke).  The show was produced by Reiner with Bill Persky and Sam Denoff.  The music for the show's theme song was written by Earle Hagen.\n\nList of The New Dick Van Dyke Show episodes: This is a list of episodes for the CBS television series \"The New Dick Van Dyke Show\" (not to be confused with \"The Dick Van Dyke Show\").\n\nKelly Jean Van Dyke: Kelly Jean Van Dyke (June 5, 1958 – November 17, 1991) was an American actress and adult film performer.  She was the daughter of actor Jerry Van Dyke, niece of the actor Dick Van Dyke, and cousin once removed of Shane Van Dyke.\n\nQuestion: Which cast member of the musical film, \"Top Banana\", played a comedy writer on \"The Dick Van Dyke Show\"?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the musical film.\"\n    },\n    \"tv_show_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the television show.\"\n    },\n    \"cast_member\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the cast member.\"\n        },\n        \"role_on_tv_show\": {\n          \"type\": \"string\",\n          \"description\": \"The character played by the cast member on the TV show.\"\n        },\n        \"character_profession\": {\n          \"type\": \"string\",\n          \"description\": \"The profession of the character played on the TV show.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"role_on_tv_show\",\n        \"character_profession\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"tv_show_title\",\n    \"cast_member\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the musical film."
      },
      "tv_show_title": {
        "type": "string",
        "description": "The title of the television show."
      },
      "cast_member": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the cast member."
          },
          "role_on_tv_show": {
            "type": "string",
            "description": "The character played by the cast member on the TV show."
          },
          "character_profession": {
            "type": "string",
            "description": "The profession of the character played on the TV show."
          }
        },
        "required": [
          "name",
          "role_on_tv_show",
          "character_profession"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_title",
      "tv_show_title",
      "cast_member"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
