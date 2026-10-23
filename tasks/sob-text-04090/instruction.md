{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nOfficer training: Officer training refers to the training that most military officers must complete before acquiring an officer rank.  A potential recruit becomes an officer cadet, someone in training.  An officer in training can either be trained in a military college, such as West Point, or taken from the enlisted ranks.  After this training is complete, the recruit in question becomes a fully fledged officer, taking on a commanding position in his or her military branch.\n\nArmy: An army (from Latin \"arma\" \"arms, weapons\" via Old French \"armée\", \"armed\" (feminine)) or ground force is a fighting force that fights primarily on land.  In the broadest sense, it is the land-based military branch, service branch or armed service of a nation or state.  It may also include other branches of the military such as the air force via means of aviation corps.  Within a national military force, the word army may also mean a field army.  They differ from army reserves who are activated only during such times as war or natural disasters.\n\nCentral Military Commission (China): The Central Military Commission (CMC) refers to the parallel national defense organizations of the Communist Party of China and the People's Republic of China: the Central Military Commission of the Communist Party of China, a Party organ under the CPC Central Committee, and the Central Military Commission of the People's Republic of China, a central state organ under the National People's Congress, being the military branch of the national government.\n\nSulejman Vokshi: Sulejman Vokshi (1815 - 1890) was an Albanian military commander and leader of the League of Prizren.  A member of the central committee of the league as head of the finances commission, Vokshi also was an important leader of the organization's military branch and an officer of its military staff.\n\nMedical corps: A medical corps is generally a military branch or officer corps responsible for medical care for serving military personnel.  Such officers are typically military physicians.\n\nCyber force: A cyber force is a military branch devoted to cyberwarfare, cybersecurity and counter-cyberwarfare.  An example of a cyber force is the Norwegian Cyber Defence Force.  A Cyber force can be part of a military branch or a combined command.\n\nCyber and Information Space Command (Germany): The Cyber and Information Space Command (German: \"Kommando Cyber- und Informationsraum\") (Kdo CIR) is the youngest branch of Germany's military the Bundeswehr.  The decision to form new military branch was presented by Defense Minister Ursula von der Leyen on 26 April 2016, with the command becoming operational on 1 April 2017.  The command's headquarter is Bonn.\n\nRoyal Norwegian Air Force: The Royal Norwegian Air Force (RNoAF) (Norwegian: \"Luftforsvaret\" ) is the air force of Norway.  It was established as a separate arm of the Norwegian armed forces on 10 November 1944.  The RNoAF's peacetime establishment is approximately 1,430 employees (officers, enlisted staff and civilians).  600 personnel also serve their draft period in the RNoAF.  After mobilization the RNoAF would consist of approximately 5,500 personnel.\n\nUkrainian Airmobile Forces: The Ukrainian Airmobile Forces or VDV (from \"Vysokomobil'ni desantni viyska Ukrayiny\", Ukrainian: Високомобільні десантні війська України, ВДВ; High-mobile Airborne Forces of Ukraine) is the military branch of the Armed Forces of Ukraine.  The airmobile forces consist of formations, units and elements of the Army and the Army aviation, trained for combined activities behind the enemy lines.  The airmobile forces are in constant combat readiness and are the high mobility branch of forces.\n\nChristian Roy Kaldager: Christian Roy Kaldager (18 March 1908 – 23 June 2005) was a Royal Norwegian Air Force officer.\n\nQuestion: When was the military branch, for which Christian Roy Kaldager served, established?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"officer_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the military officer.\"\n    },\n    \"military_branch\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the military branch.\"\n        },\n        \"establishment_date\": {\n          \"type\": \"string\",\n          \"description\": \"The date when the military branch was established.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"establishment_date\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"service_confirmed\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the officer's service in the specified branch is confirmed.\"\n    }\n  },\n  \"required\": [\n    \"officer_name\",\n    \"military_branch\",\n    \"service_confirmed\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "officer_name": {
        "type": "string",
        "description": "The name of the military officer."
      },
      "military_branch": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the military branch."
          },
          "establishment_date": {
            "type": "string",
            "description": "The date when the military branch was established."
          }
        },
        "required": [
          "name",
          "establishment_date"
        ],
        "additionalProperties": false
      },
      "service_confirmed": {
        "type": "boolean",
        "description": "Indicates if the officer's service in the specified branch is confirmed."
      }
    },
    "required": [
      "officer_name",
      "military_branch",
      "service_confirmed"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
