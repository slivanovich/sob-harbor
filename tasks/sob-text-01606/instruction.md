{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJapan Paralympic Committee: Japan Paralympic Committee (JPC) is a National Paralympic Committee (NPC) of Japan.  The committee was established on August 20, 1999, and is recognized by International Paralympic Committee (IPC), Asian Paralympic Committee (APC) and Ministry of Health.\n\nAsian Paralympic Committee: The Asian Paralympic Committee (APC) is an organization based in United Arab Emirates.  Its members are the 43 National Paralympic Committees of the Asian region, who are also members of the International Paralympic Committee (IPC).\n\nParalympic Committee of the Philippines: The Philippine Paralympic Committee (PPC) (formerly known as Philippine Sports Association for the Differently Abled—National Paralympic Committee of the Philippines), is the national sports association for physically impaired athletes, tasked to spearhead developing sport competency for Filipino persons with disabilities.  It is the Philippine National Paralympic Committee recognized by the International Paralympic Committee\n\nUnited Arab Emirates at the Paralympics: The United Arab Emirates started actively participating in the Paralympic community during the 1990s.  They made their debut at the 1992 Summer Paralympics.  Since that time, they have won several Paralympic medals.  The country had their debut on the international Paralympic stage at the 1990 Stoke Mandeville Games.  Some of the country's Paralympic competitors are internationally ranked.  The United Arab Emirates have competed at several other Paralympic events including the Arab Paralympic Games, Asian Paralympic Games, IWAS World Games, Stoke Mandeville Games, and World Semi-Olympic Championship.  (The country has never participated at the Winter Paralympic Games.)  The United Arab Emirates Paralympic Committee is the national organisation, gaining its International Paralympic Committee recognition in 1995 and have subsequently made winning medals and hosting events a priority.\n\nHellenic Paralympic Committee: Hellenic Paralympic Committee (Greek: Ελληνική Παραολυμπιακή Επιτροπή ) is the National Paralympic Committee in Greece for the Paralympic Games movement.  It is a non-profit organisation that selects teams, and raises funds to send Greek competitors to Paralympic events organised by the International Paralympic Committee (IPC).\n\nFinnish Paralympic Committee: Finnish Paralympic Committee (Finnish: \"Suomen paralympiakomitea\" ) is the National Paralympic Committee in Finland for the Paralympic Games movement.  It is a non-profit organisation that selects teams, and raises funds to send Finnish competitors to Paralympic events organised by the International Paralympic Committee (IPC).\n\nKorean Paralympic Committee: Korean Paralympic Committee (KPC)(Hangul: 대한장애인체육회 ; Hanja: 大韓障碍人體育會 ) is a National Paralympic Committee (NPC) of South Korea.  The committee was established on May 12, 2006, and is recognized by International Paralympic Committee (IPC) and Asian Paralympic Committee (APC).\n\nGeorgian Paralympic Committee: Georgian Paralympic Committee is the National Paralympic Committee in Georgia for the Paralympic Games movement.  It is a non-profit organisation that selects teams, and raises funds to send Georgian competitors to Paralympic events organised by the International Paralympic Committee (IPC).\n\nParalympic Committee of Thailand: The Paralympic Committee of Thailand (PCT, Thai: คณะกรรมการพาราลิมปิกแห่งประเทศไทย ) is the national Paralympic committee in Thailand for the Paralympic Games movement, based in Bangkok, Thailand.  It is a non-profit organisation that selects teams and raises funds to send Thailand competitors to Paralympic events organised by the International Paralympic Committee (IPC), Asian Para Games events organised by the Asian Paralympic Committee (APC) and ASEAN Para Games events organised by the ASEAN Para Sports Federation (APSF).\n\nPara-shooting classification: Paralympic Shooting classification is the shooting classification in place for the Paralympic Games to help establish fair competition.  Classification is governed by the International Paralympic Committee's IPC Shooting.  While there are currently three classifications, there were originally five in international competitions.  People with physical disabilities as defined by the International Paralympic Committee are eligible to compete.\n\nQuestion: Japan Paralympic Committee is recognized by International Paralympic Committee (IPC), Ministry of Health and what other committee?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"committee_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the Paralympic Committee being discussed.\"\n    },\n    \"recognized_by_list\": {\n      \"type\": \"array\",\n      \"description\": \"A list of all entities that recognize the committee.\",\n      \"items\": {\n        \"type\": \"string\"\n      }\n    },\n    \"additional_recognizing_committee\": {\n      \"type\": \"string\",\n      \"description\": \"The specific committee identified as the answer to the question.\"\n    }\n  },\n  \"required\": [\n    \"committee_name\",\n    \"recognized_by_list\",\n    \"additional_recognizing_committee\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "committee_name": {
        "type": "string",
        "description": "The name of the Paralympic Committee being discussed."
      },
      "recognized_by_list": {
        "type": "array",
        "description": "A list of all entities that recognize the committee.",
        "items": {
          "type": "string"
        }
      },
      "additional_recognizing_committee": {
        "type": "string",
        "description": "The specific committee identified as the answer to the question."
      }
    },
    "required": [
      "committee_name",
      "recognized_by_list",
      "additional_recognizing_committee"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
