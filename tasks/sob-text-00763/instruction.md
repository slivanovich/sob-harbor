{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nŽeljko Obradović: Želimir \"Željko\" Obradović (; born March 9, 1960) is a Serbian professional basketball head coach for Fenerbahçe of the Turkish Basketball Super League.  He is also a former professional basketball player.\n\nT. J. Cline: T. J. Cline (born July 22, 1994) is an American professional basketball player for Galatasaray of the Turkish Basketball Super League (BSL).  A power forward/center, he played college basketball at the University of Richmond.  Cline is the son of Naismith Memorial Basketball Hall of Fame player Nancy Lieberman.\n\nMalcolm Lee (basketball): Malcolm Toshio Lee (born May 22, 1990) is an American professional basketball player who last played for Trabzonspor of the Turkish Basketball Super League (BSL).  As a college basketball player with the UCLA Bruins, he received all-conference honors in the Pacific-10 (later known as the Pac-12).  After his junior year, he was selected in the second round of the 2011 NBA draft, and began his professional career with the Minnesota Timberwolves.\n\nTurkish Basketball President's Cup: The Turkish Basketball President's Cup (Turkish: Cumhurbaşkanlığı Kupası), or Turkish Basketball Super Cup, is the professional basketball men's club super cup competition that takes place each year in Turkey.  The Turkish President's Cup competition began in the year 1985.  It usually takes place between the winners of the Turkish Super League and the winners of the Turkish Cup.  If the same team wins both the Turkish Super League and the Turkish Cup in the same season, then the competition takes place between the two league finalists from the Turkish Super League.\n\nBasketbol Süper Ligi Finals MVP: The Basketbol Süper Ligi Finals MVP (English: Basketball Super League Finals MVP), is an annual basketball award that is presented to the most valuable player of the finals of the playoffs of the Türkiye Basketbol Süper Ligi (English: Turkish Basketball Super League), which is the top-tier level professional club basketball league in Turkey.\n\nTurkish basketball league system: The Turkish basketball league system or Turkish basketball league pyramid, is a series of interconnected competitions for professional basketball clubs in Turkey.  The system has a hierarchical format with a promotion and demotion system between competitions at different levels.  There are currently five different competitions on the pyramid: the 1st-tier Turkish Basketball Super League (BSL), the 2nd-tier Turkish Basketball First League (TBL), the 3rd-tier Turkish Basketball Second League (TB2L), the 4th-tier Turkish Men's Regional Basketball League (EBBL), and the 5th-tier Men's University League (Ünilig).\n\nIan Hummer: Ian MacDonald Hummer (born August 23, 1990) is an American professional basketball player for TED Ankara Kolejliler of the Turkish Basketball Super League.  He previously played professionally with the ratiopharm Ulm, the BG Göttingen and the Nilan Bisons Loimaa.  He is from Vienna, Virginia and completed his senior season of college basketball for the 2012–13 Princeton Tigers men's basketball team.  He was the 2009 \"The Washington Post\" Boys basketball Player of the Year for Gonzaga College High School as a senior in high school and the 2013 Ivy League Men's Basketball Player of the Year as a senior in college for Princeton.\n\nJeff Capel III: Felton Jeffrey \"Jeff\" Capel III (born February 12, 1975) is an American coach college basketball coach and former player.  He played for Duke University and was a head coach at Virginia Commonwealth University and University of Oklahoma.\n\nTony Crocker: Antonio Lamar \"Tony\" Crocker (born January 17, 1987) is an American professional basketball player for Tofaş of the Turkish Basketball Super League (BSL).  A native of Lawton, Oklahoma, he excelled at basketball while attending Earl Warren High School in San Antonio, Texas before attending prep school at The Patterson.  Crocker signed a letter of intent to play college basketball at the University of Oklahoma under Kelvin Sampson, and stuck to his commitment when coach Sampson left to Indiana University and coach Jeff Capel III became the new coach of the Sooners.  Crocker started 25 out of 31 games as a true freshman at Oklahoma and established himself as one of the top freshmen in the country.  Crocker has garnered attention for wearing a long-sleeved shirt underneath his uniform.\n\nKyle Weems: Kyle Jordan Weems (born August 23, 1989) is an American professional basketball player for Beşiktaş of the Turkish Basketball Super League (BSL).  He played collegiately for Missouri State University and was named Missouri Valley Conference Men's Basketball Player of the Year and an All-American in 2011.\n\nQuestion: Which American professional basketball player for the Turkish Basketball Super league played under the former head coach of Virginia Commonwealth University and University of Oklahoma?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"player_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the professional basketball player.\"\n    },\n    \"nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the player.\"\n    },\n    \"current_team\": {\n      \"type\": \"string\",\n      \"description\": \"The current team the player plays for in the Turkish Basketball Super League.\"\n    },\n    \"coach_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"coach_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the coach the player played under.\"\n        },\n        \"former_head_coach_universities\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"A list of universities where the coach was a head coach.\"\n        }\n      },\n      \"required\": [\n        \"coach_name\",\n        \"former_head_coach_universities\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"player_name\",\n    \"nationality\",\n    \"current_team\",\n    \"coach_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "player_name": {
        "type": "string",
        "description": "The full name of the professional basketball player."
      },
      "nationality": {
        "type": "string",
        "description": "The nationality of the player."
      },
      "current_team": {
        "type": "string",
        "description": "The current team the player plays for in the Turkish Basketball Super League."
      },
      "coach_details": {
        "type": "object",
        "properties": {
          "coach_name": {
            "type": "string",
            "description": "The name of the coach the player played under."
          },
          "former_head_coach_universities": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of universities where the coach was a head coach."
          }
        },
        "required": [
          "coach_name",
          "former_head_coach_universities"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "player_name",
      "nationality",
      "current_team",
      "coach_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
