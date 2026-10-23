{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nNew Hampshire gubernatorial election, 1996: The 1996 New Hampshire gubernatorial election took place on November 5, 1996.  State Senator Jeanne Shaheen won the election.\n\nNew Hampshire gubernatorial election, 1992: The 1992 New Hampshire gubernatorial election took place on November 3, 1992.  Republican nominee Steve Merrill won the election.\n\nNew Hampshire gubernatorial election, 2016: The 2016 New Hampshire gubernatorial election took place on November 8, 2016, to elect the Governor of New Hampshire, concurrently with the 2016 U.S. presidential election, as well as elections to the United States Senate, elections to the United States House of Representatives and various state and local elections.\n\nNew Hampshire gubernatorial election, 2012: The 2012 New Hampshire gubernatorial election took place on November 6, 2012, concurrently with the 2012 U.S. presidential election, U.S. House elections, and various state and local elections.\n\nNew Hampshire gubernatorial election, 1990: The 1990 New Hampshire gubernatorial election took place on November 6, 1990.  Incumbent Governor Judd Gregg won reelection to a second term that would be his last, as he ran for and won election to the United States Senate in 1992.\n\nMontana gubernatorial election, 1996: The 1996 Montana gubernatorial election took place on November 5, 1996.  Incumbent Governor of Montana Marc Racicot, who was first elected in 1992, ran for re-election.  After winning the Republican primary against a conservative activist, he moved on to the general election, where he was set to face Chet Blaylock, a former State Senator and the Democratic nominee.  However, on October 23, 1996, Blaylock died of a heart attack, and the Montana Democratic Party selected his running mate, State Senator Judy Jacobson, to replace him as the gubernatorial nominee, and she therefore appeared on the ballot as both the gubernatorial nominee and the lieutenant gubernatorial nominee.  Ultimately, however, Racicot was able to defeat Jacobson in a landslide to win re-election to his second and final term as governor.\n\nNew Hampshire gubernatorial election, 2006: The 2006 New Hampshire gubernatorial election took place on November 7, 2006.  Incumbent Democrat John Lynch defeated Republican James B. Coburn and won a second term as Governor of New Hampshire.\n\nNew Hampshire gubernatorial election, 1994: The 1994 New Hampshire gubernatorial election took place on November 8, 1994.  Incumbent Governor Steve Merrill won the election.\n\nJeanne Shaheen: Cynthia Jeanne Shaheen (née Bowers; January 28, 1947) is the senior United States Senator from New Hampshire, since 2009.\n\nMinnesota lieutenant gubernatorial election, 1970: The 1970 Minnesota lieutenant gubernatorial election took place on November 3, 1970.  State Senator Rudy Perpich of the Minnesota Democratic-Farmer-Labor Party defeated Duluth Mayor Ben Boo of the Republican Party of Minnesota.  The 1970 lieutenant gubernatorial election was the final lieutenant gubernatorial election held before the Minnesota Constitution was amended to provide for elections of the Governor and Lieutenant Governor on a joint ticket.\n\nQuestion: The 1996 New Hampshire gubernatorial election took place on November 5, 1996, who won the election for Senator?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"election_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the election took place.\"\n    },\n    \"election_date\": {\n      \"type\": \"string\",\n      \"description\": \"The specific date of the election.\"\n    },\n    \"election_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of election (e.g., gubernatorial).\"\n    },\n    \"winner_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the person who won the election.\"\n        },\n        \"role_at_time_of_election\": {\n          \"type\": \"string\",\n          \"description\": \"The political role or office held by the winner at the time of the election.\"\n        },\n        \"office_won\": {\n          \"type\": \"string\",\n          \"description\": \"The office that was won in this election.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"role_at_time_of_election\",\n        \"office_won\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"election_year\",\n    \"election_date\",\n    \"election_type\",\n    \"winner_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "election_year": {
        "type": "integer",
        "description": "The year the election took place."
      },
      "election_date": {
        "type": "string",
        "description": "The specific date of the election."
      },
      "election_type": {
        "type": "string",
        "description": "The type of election (e.g., gubernatorial)."
      },
      "winner_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the person who won the election."
          },
          "role_at_time_of_election": {
            "type": "string",
            "description": "The political role or office held by the winner at the time of the election."
          },
          "office_won": {
            "type": "string",
            "description": "The office that was won in this election."
          }
        },
        "required": [
          "name",
          "role_at_time_of_election",
          "office_won"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "election_year",
      "election_date",
      "election_type",
      "winner_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
