{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\n1974 World Championship Tennis Finals: The 1974 World Championship Tennis Finals was a men's tennis tournament played on indoor carpet courts.  It was the 4th edition of the WCT Finals and was part of the 1974 World Championship Tennis circuit.  The tournament was played at the Moody Coliseum in Dallas, Texas in the United States and was held from May 8 through May 12, 1974.  John Newcombe won the singles title.\n\n1972 World Championship Tennis Finals: The 1972 World Championship Tennis Finals was a men's tennis tournament played on indoor carpet courts.  It was the 2nd edition of the WCT Finals and was the season-ending tournament of the 1972 World Championship Tennis circuit.  The top eight points winners of the circuit qualified for the tournament which was played at the Moody Coliseum in Dallas, Texas in the United States and ran from May 8 through May 14, 1972.  Ken Rosewall won the singles title and the $50,000 first prize.  The final was broadcast live in the United States by NBC and watched by an estimated 21.3 million viewers.  In his book, \"The Education of a Tennis Player\", finalist Rod Laver commented \"I think if one match can be said to have made tennis in the United States, this was it.\" .\n\n1978 World Championship Tennis Finals: The 1978 World Championship Tennis Finals was a men's tennis tournament played on indoor carpet courts.  It was the 8th edition of the WCT Finals and was part of the 1978 Colgate-Palmolive Grand Prix, as the World Championship Tennis and the Grand Prix circuits were now combined.  It was played at the Moody Coliseum in Dallas, Texas in the United States and was held from May 9 through May 14, 1978.  Third-seeded Vitas Gerulaitis won the title and $100,000 first-prize money.\n\n1975 World Championship Tennis Finals: The 1975 World Championship Tennis Finals was a men's tennis tournament played on indoor carpet courts.  It was the 5th edition of the WCT Finals and was part of the 1975 World Championship Tennis circuit.  The event was played at the Moody Coliseum in Dallas, Texas in the United States and was held from May 7 through May 11, 1975.  The draw consisted of the eight best performing players of the 1975 WCT season.  First-seeded Arthur Ashe won the tournament and the accompanying $50,000 first-prize money.\n\n1976 World Championship Tennis Finals: The 1976 World Championship Tennis Finals was a tennis tournament played on indoor carpet courts.  It was the 6th edition of the WCT Finals and was part of the 1976 World Championship Tennis circuit.  It was played at the Moody Coliseum in Dallas, Texas, in the United States and was held from May 4 through May 9, 1976.\n\n1984 World Championship Tennis Finals: The 1984 World Championship Tennis Finals, also known by its sponsored name Buick WCT Finals, was a tennis tournament played on indoor carpet courts.  It was the 14th edition of the WCT Finals and was part of the 1984 World Championship Tennis circuit.  It was played at the Reunion Arena in Dallas, Texas in the United States and was held from April 24 through April 30, 1984.  First-seeded and defending champion John McEnroe won the title and the accompanying $150,000 first-prize money.  It was his fourth WCT Finals title, a record, and his sixth successive final.\n\n1977 World Championship Tennis Finals: The 1977 World Championship Tennis Finals was a tennis tournament played on indoor carpet courts.  It was the 7th edition of the WCT Finals and was part of the 1977 World Championship Tennis circuit.  It was played at the Moody Coliseum in Dallas, Texas in the United States and was held from May 10 through May 15, 1977.\n\nNeil Armstrong: Neil Alden Armstrong (August 5, 1930 – August 25, 2012) was an American astronaut, engineer, and the first person to walk on the Moon.  He was also an aerospace engineer, naval aviator, test pilot, and university professor.  Before becoming an astronaut, Armstrong was an officer in the U.S. Navy and served in the Korean War.  After the war, he earned his bachelor's degree at Purdue University and served as a test pilot at the National Advisory Committee for Aeronautics (NACA) High-Speed Flight Station, where he logged over 900 flights.  He later completed graduate studies at the University of Southern California.\n\n1973 World Championship Tennis Finals: The 1973 World Championship Tennis Finals was a tennis tournament played on indoor carpet courts.  It was the 3rd edition of the WCT Finals and was part of the 1973 World Championship Tennis circuit.  It was played at the Moody Coliseum in Dallas, Texas in the United States and was held from May 7 through May 13, 1973.\n\n1971 World Championship Tennis Finals: The 1971 World Championship Tennis Finals was a men's tennis tournament played on indoor Sportface carpet courts.  It was the first edition of the WCT Finals and the concluding event of the 1971 World Championship Tennis circuit.  The eight top players in points qualified for the event.  The quarterfinals and semifinals were played at the Hofheinz Pavilion in Houston, Texas from November 19 through November 21 while the final, watched by 8,200 spectators, was played at the Memorial Auditorium in Dallas, Texas, United States on November 26.  Ken Rosewall win the event and the accompanying $50,000 first-prize money.  Neil Armstrong presented the prizes.\n\nQuestion: Where did the celebrity who presented the prizes at the 1971 World Championship Tennis Finals earn his bachelor's degree ?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"celebrity_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the celebrity who presented the prizes.\"\n    },\n    \"event_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year of the World Championship Tennis Finals event.\"\n    },\n    \"degree_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"degree_type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of degree earned by the celebrity.\"\n        },\n        \"university_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the university where the degree was earned.\"\n        }\n      },\n      \"required\": [\n        \"degree_type\",\n        \"university_name\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"celebrity_name\",\n    \"event_year\",\n    \"degree_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "celebrity_name": {
        "type": "string",
        "description": "The name of the celebrity who presented the prizes."
      },
      "event_year": {
        "type": "integer",
        "description": "The year of the World Championship Tennis Finals event."
      },
      "degree_details": {
        "type": "object",
        "properties": {
          "degree_type": {
            "type": "string",
            "description": "The type of degree earned by the celebrity."
          },
          "university_name": {
            "type": "string",
            "description": "The name of the university where the degree was earned."
          }
        },
        "required": [
          "degree_type",
          "university_name"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "celebrity_name",
      "event_year",
      "degree_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
