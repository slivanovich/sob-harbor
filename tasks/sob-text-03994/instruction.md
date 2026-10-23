{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRoadies (TV series): Roadies is an American comedy-drama television series created by Cameron Crowe.  A ten-episode first season premiered on Showtime on June 26, 2016.  The pilot episode was written and directed by Crowe.\n\nCameron Crowe: Cameron Bruce Crowe (born July 13, 1957) is an American director, producer, screenwriter, journalist, author, and actor.  Before moving into the film industry, Crowe was a contributing editor at \"Rolling Stone\" magazine, for which he still frequently writes.\n\nAloha (film): Aloha is a 2015 American romantic comedy-drama film written, produced and directed by Cameron Crowe.  The film, starring Bradley Cooper, Emma Stone, Rachel McAdams, Bill Murray, John Krasinski, Danny McBride and Alec Baldwin, was released on May 29, 2015.  The film received negative reviews from critics and has grossed only $26 million against a budget of $37 million, making the film a box office bomb.\n\nPushing Hands (film): Pushing Hands () is a film directed by Ang Lee.  Released in 1992, it was his first feature film.  Together with Ang Lee's two following films, \"The Wedding Banquet\" (1993) and \"Eat Drink Man Woman\" (1994), it forms his \"Father Knows Best\" trilogy, each of which deals with conflicts between an older and more traditional generation and their children as they confront a world of change.\n\nFast Times at Ridgemont High: Fast Times at Ridgemont High is a 1982 American coming-of-age comedy film directed by Amy Heckerling and written by Cameron Crowe, adapted from his 1981 book of the same name.  Crowe went undercover at Clairemont High School in San Diego and wrote about his experiences.\n\nJoe Hutshing: Joe Hutshing is an American film editor who grew up in San Diego, California and is best known for working multiple times with film director, Oliver Stone and well as with film director Cameron Crowe (who is also from San Diego, California).  Hutshing graduated from the University of Oregon in 1980.\n\nAmerican Hot Wax: American Hot Wax is a 1978 biopic film directed by Floyd Mutrux and written by John Kaye, telling the story of pioneering disc jockey Alan Freed, who was instrumental in introducing and popularizing rock and roll in the 1950s.  Freed is often credited with coining the term \"Rock 'n' Roll.\"  The film starred Tim McIntire as Freed, and Fran Drescher as Freed's feisty secretary, Laraine Newman as a young aspiring songwriter, Melanie Chartoff as a young singer, Jeff Altman as a sleazy record promoter who is told off by everybody he approaches, Jay Leno as Freed's mischievous limousine driver, Moosie Drier in a warmly reviewed performance as the head of a Buddy Holly fan club with at least 5,000 members, and a walk-on part by a teenaged Cameron Crowe.  It also featured performances by Chuck Berry, Jerry Lee Lewis, Frankie Ford, Screamin' Jay Hawkins, and the Brooklyn Dreams as \"Professor La Plano and The Planotones\".  The film was not a box-office success.\n\nPearl Jam Twenty: Pearl Jam Twenty (also known as PJ20) is a 2011 American rockumentary directed by Cameron Crowe about the band Pearl Jam.  Preliminary footage was being shot as of June 2010.  Crowe completed filming in April 2011, after using 12,000 hours of footage of the band for the documentary.  The film premiered at the 2011 Toronto International Film Festival and also had an accompanying book and soundtrack.\n\nAng Lee: Ang Lee  (; born October 23, 1954) is a Taiwanese film director, screenwriter and producer.\n\nAlmost Famous: Almost Famous is a 2000 American comedy-drama film written and directed by Cameron Crowe, and starring Billy Crudup, Kate Hudson and Patrick Fugit.  It tells the fictional story of a teenage journalist writing for \"Rolling Stone\" magazine in the early 1970s while covering the fictitious rock band Stillwater, and his efforts to get his first cover story published.  The film is semi-autobiographical, as Crowe himself was a teenage writer for \"Rolling Stone\".\n\nQuestion: Are Ang Lee and Cameron Crowe of the same nationality?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_1\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"nationality\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"nationality\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"person_2\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"nationality\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"nationality\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"are_nationalities_same\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if both individuals have the same nationality, false otherwise.\"\n    }\n  },\n  \"required\": [\n    \"person_1\",\n    \"person_2\",\n    \"are_nationalities_same\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_1": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "nationality": {
            "type": "string"
          }
        },
        "required": [
          "name",
          "nationality"
        ],
        "additionalProperties": false
      },
      "person_2": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "nationality": {
            "type": "string"
          }
        },
        "required": [
          "name",
          "nationality"
        ],
        "additionalProperties": false
      },
      "are_nationalities_same": {
        "type": "boolean",
        "description": "True if both individuals have the same nationality, false otherwise."
      }
    },
    "required": [
      "person_1",
      "person_2",
      "are_nationalities_same"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
