{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nStefan Mihajlović: Stefan Mihajlović (; born 24 June 1994) is a Serbian footballer, who plays for Vojvodina.  He is a son of former Bosnian Serb footballer Radmilo Mihajlović.\n\nMomčilo Krajišnik: Momčilo Krajišnik (Serbian Cyrillic: ; born 20 January 1945) is a former Bosnian Serb political leader, who along with Radovan Karadžić co-founded the Bosnian Serb nationalist Serb Democratic Party (SDS).  Between 1990-92, he was Speaker of the People's Assembly of Republika Srpska.  Between June and December 1992, he also served as member of the expanded Presidency of Republika Srpska.\n\nTihomir Ognjanov: Tihomir \"Bata\" Ognjanov (Serbian Cyrillic: Тихомир Огњанов; 2 March 1927 – 2 July 2006) was a Serbian footballer who was part of Yugoslavia national football team at the 1950 and 1954 FIFA World Cup.  He later became a manager.  He played for Spartak Subotica (in three different periods), Partizan (when he was in the Yugoslav Army although he only played in friendly matches) and Red Star.  With Red Star he won 2 national championships (1951, 1953) and 2 Yugoslav cups (1949, 1950).\n\nHaris Smajić: Haris Smajić (born 8 March 1960) is a former Bosnian footballer.  He played for Yugoslavia national under-20 football team at the 1979 FIFA World Youth Championship, but was never capped for Yugoslavia at full international level.\n\nStojan Malbašić: Stojan Malbašić (, born 15 September 1959) is a former Bosnian Serb footballer and now a coach at FK Borac Banja Luka.\n\nRadmilo Mihajlović: Radmilo Mihajlović (born 19 November 1964) is a former Bosnian Serb footballer who played for the Yugoslavia national football team.\n\nRanko Golijanin: Ranko Golijanin (Serbian Cyrillic: ; born January 18, 1975) is a Bosnian Serb footballer who played in the First League of FR Yugoslavia, Segunda División, USL A-League, and the Canadian Soccer League.\n\nBoško Antić: Božidar \"Boško\" Antić (Serbian Cyrillic: Божидар \"Бошко\" Антић; born January 7, 1944 in Sarajevo, Vrhbosna County, Independent State of Croatia, now Bosnia and Herzegovina) was a Bosnian Serb footballer who played for SFR Yugoslavia.\n\nYugoslavia national football team: The Yugoslavia national football team represented the Kingdom of Yugoslavia (1918–1941, \"until 1929 as Kingdom of Serbs, Croats and Slovenes\"), and the Socialist Federal Republic of Yugoslavia (1943–1992, \"until November 29, 1945 as Democratic Federal Yugoslavia\", \"29 November 1945–1963 as Federal People's Republic of Yugoslavia\") in association football.  It enjoyed success in international competition.  In 1992, during the Yugoslav wars, the team was suspended from international competition as part of a United Nations sanction.  In 1994, when the boycott was lifted, it was succeeded by the Federal Republic of Yugoslavia national football team.\n\nMitar Lukić: Mitar Lukić (born 22 October 1957) is a former Bosnian Serb footballer and current manager of FK Sloga Doboj.\n\nQuestion: Stefan Mihajlović ( born 24 June 1994) is a Serbian footballer, who plays for which team, he is a son of Radmilo Mihajlovi, a former Bosnian Serb footballer, who played for the Yugoslavia national football team?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"player_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the footballer.\"\n    },\n    \"player_nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the footballer.\"\n    },\n    \"player_birth_date\": {\n      \"type\": \"string\",\n      \"description\": \"The birth date of the footballer.\"\n    },\n    \"current_team\": {\n      \"type\": \"string\",\n      \"description\": \"The current team the footballer plays for.\"\n    },\n    \"parent_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the parent.\"\n        },\n        \"nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the parent.\"\n        },\n        \"former_profession\": {\n          \"type\": \"string\",\n          \"description\": \"The former profession of the parent.\"\n        },\n        \"played_for_national_team\": {\n          \"type\": \"string\",\n          \"description\": \"The national team the parent played for.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"nationality\",\n        \"former_profession\",\n        \"played_for_national_team\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"player_name\",\n    \"player_nationality\",\n    \"player_birth_date\",\n    \"current_team\",\n    \"parent_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "player_name": {
        "type": "string",
        "description": "The name of the footballer."
      },
      "player_nationality": {
        "type": "string",
        "description": "The nationality of the footballer."
      },
      "player_birth_date": {
        "type": "string",
        "description": "The birth date of the footballer."
      },
      "current_team": {
        "type": "string",
        "description": "The current team the footballer plays for."
      },
      "parent_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the parent."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the parent."
          },
          "former_profession": {
            "type": "string",
            "description": "The former profession of the parent."
          },
          "played_for_national_team": {
            "type": "string",
            "description": "The national team the parent played for."
          }
        },
        "required": [
          "name",
          "nationality",
          "former_profession",
          "played_for_national_team"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "player_name",
      "player_nationality",
      "player_birth_date",
      "current_team",
      "parent_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
