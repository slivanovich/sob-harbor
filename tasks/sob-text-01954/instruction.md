{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAnthony Clarvoe: Anthony Clarvoe is an American playwright born in 1958.\n\nEdward Locke: Edward Locke (1869–1945) was an American playwright born in England.\n\nLondon Suite (play): London Suite is a play by Neil Simon, consisting of four one-act plays.  \"London Suite\" also was a 1996 television movie.  It is in a similar style to Simon's earlier works \"Plaza Suite\" and \"California Suite\".\n\nJen Silverman: Jen Silverman is an American playwright born in the United States.  She grew up living and traveling in Scandinavia, Asia, and Europe as well as the United States.  She completed a BA in comparative literature at Brown University, a MFA in playwriting at the University of Iowa, and also studied at Juilliard.\n\nVinegar Tom: Vinegar Tom is the title of a 1976 play by the British playwright Caryl Churchill.  The play examines gender and power relationships through the lens of 17th century witchcraft trials in England.  The script employs features of the epic theater associated with German playwright Bertolt Brecht, particularly the realistic use of songs.  The play's title comes from the name of one character's pet cat, supposed to be her familiar spirit, likely inspired by the supposed imp of one Elizabeth Clarke, a woman tried and executed for witchcraft in Essex in 1645.  The play was inspired by the Women's Rights Act in 1970 and explored the thought that women were treated unequally to men in England, both at the time in which the play takes place, and the time in which the play was written.\n\nCalifornia Suite: California Suite is a 1976 play by Neil Simon.  Similar in structure to his earlier \"Plaza Suite\", the comedy is composed of four playlets set in Suite 203-04, which consists of a living room and an adjoining bedroom with an ensuite bath, in The Beverly Hills Hotel.\n\nThe Vietnamization of New Jersey: The Vietnamization of New Jersey (subtitled \"A American Tragedy\" [\"sic\"] ) is a 1976 play written by American playwright Christopher Durang.\n\nEden (Steve Carter play): Eden is a 1976 play by American playwright Steve Carter.  Set in the 1920s, it is the first of Carter's Caribbean trilogy.  \"Eden\" explores intra-racial conflicts between recent immigrants from the Caribbean and the African-American population.  The West Coast premiere of this critically acclaimed play received five Los Angeles Drama Critics Circle Awards.\n\nCalifornia Suite (film): California Suite is a 1978 American comedy film directed by Herbert Ross.  The screenplay by Neil Simon is based on his play of the same name.  Similar to his earlier \"Plaza Suite\", the film focuses on the dilemmas of guests staying in a suite in a luxury hotel.  Maggie Smith won the Academy Award for Best Supporting Actress for her performance in the film.\n\nNeil Simon: Marvin Neil Simon (born July 4, 1927) is an American playwright, screenwriter and author.  He has written more than thirty plays and nearly the same number of movie screenplays, mostly adaptations of his plays.  He has received more combined Oscar and Tony nominations than any other writer.\n\nQuestion: California Suite is a 1976 play by an american playwright born in what year?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"play_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the play.\"\n    },\n    \"play_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the play was released.\"\n    },\n    \"playwright\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the playwright.\"\n        },\n        \"nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the playwright.\"\n        },\n        \"birth_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The birth year of the playwright.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"nationality\",\n        \"birth_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"answer\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth year of the playwright who wrote the specified play.\"\n    }\n  },\n  \"required\": [\n    \"play_title\",\n    \"play_year\",\n    \"playwright\",\n    \"answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "play_title": {
        "type": "string",
        "description": "The title of the play."
      },
      "play_year": {
        "type": "integer",
        "description": "The year the play was released."
      },
      "playwright": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the playwright."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the playwright."
          },
          "birth_year": {
            "type": "integer",
            "description": "The birth year of the playwright."
          }
        },
        "required": [
          "name",
          "nationality",
          "birth_year"
        ],
        "additionalProperties": false
      },
      "answer": {
        "type": "integer",
        "description": "The birth year of the playwright who wrote the specified play."
      }
    },
    "required": [
      "play_title",
      "play_year",
      "playwright",
      "answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
