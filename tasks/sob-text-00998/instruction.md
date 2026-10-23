{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nFrederick Detrick: Major Fredrick Louis Detrick, MD (April 21, 1889 in New Market, Maryland – June 3, 1931 in Baltimore, Maryland), was a U.S. Army physician, flight surgeon and pilot.  He is the namesake of Fort Detrick, Maryland (formerly, Detrick Field and Camp Detrick).  Detrick, who was a teaching surgeon on the faculty of the Johns Hopkins University Hospital, Baltimore, served in France during the First World War and was a member of the Maryland National Guard when he died of a heart attack in 1931.\n\nPakistan Army Medical Corps: The Pakistan Army Medical Corps, Urdu: ﺁرمى مڈيكل كور; \"Army Medical Corps\", abbreviated as the AMC and popularly known as Medical Corps, is a military administrative non-combatant staff corps, and a primary military medical command of the Pakistan Army.  Initially part of the Indian Army Medical Corps, it was born in 1947 and served since Pakistan's independence in 1947.  It is a vital part of Pakistan Army, serving in a support and military medical role.  The corps also has a secondary role of providing civil services in health, rehabilitation and disaster relief to the wider Pakistan community.\"\n\nTed Wong (general): M. Ted Wong is a retired major general in the United States Army.  General Wong commanded the Northern Regional Medical Command, a unit of the United States Army Medical Command.  He was also Chief of the U.S. Army Dental Corps.  He previously commanded the Southern Regional Medical Command.\n\nKevin C. Kiley: Major General (Ret.)  Kevin C. Kiley (born October 18, 1950) was the 41st Surgeon General of the United States Army and commander of the U.S. Army Medical Command, Fort Sam Houston, Texas.  He was commander of Walter Reed Army Medical Center and North Atlantic Regional Medical Command twice, from 2002 to 2004, and as acting commander, March 1–2, 2007.  He submitted his request to retire from the U.S. Army on March 11, 2007, in the wake of the Walter Reed Army Medical Center neglect scandal, and was removed from his nominative billet as a Lieutenant General.  Pending retirement, he was assigned to a temporary billet at the General Officer Management Office at the Pentagon in the grade Major General.  His retirement in the grade of Major General was subsequently approved.\n\nTripler Army Medical Center: Tripler Army Medical Center is the headquarters of the Pacific Regional Medical Command of the armed forces administered by the United States Army in the state of Hawaii.  It is the largest military hospital in the Asian and Pacific Rim region and serves a military sphere of jurisdiction that spans over 52% of the Earth's surface.  Located on the slopes of Moanalua Ridge overlooking the Honolulu neighborhoods of Moanalua and Salt Lake, Tripler Army Medical Center's massive coral pink structure can be seen from any point in the Honolulu District.\n\nEric Schoomaker: Eric B. Schoomaker (born September 15, 1948) is a former United States Army lieutenant general who served as the 42nd Surgeon General of the United States Army and Commanding General, United States Army Medical Command, and a practicing hematologist.  He previously served as Commanding General, North Atlantic Regional Medical Command and Walter Reed Army Medical Center.  He assumed the post of U.S. Army Surgeon General on December 11, 2007.\n\nArmy Reserve Medical Command: The Army Reserve Medical Command (AR-MEDCOM) vision is to be the Army Reserve's premier Medical Command, supporting the United States' national military strategy.  The Army Reserve Medical Command mission is to provide trained, equipped, ready, skill-rich Citizen-Soldiers, to meet medical requirements across full spectrum military operations.  ARMEDCOM provides command and control for table of distribution and allowance (TDA) reserve medical units within the contiguous United States.\n\nDwight D. Eisenhower Army Medical Center: The Dwight D. Eisenhower Army Medical Center (EAMC) is a 93-bed medical treatment facility located on Fort Gordon, Ga., located near Augusta, Georgia that previously served as the headquarters of the Army's Southeast Regional Medical Command (SERMC).  SERMC oversaw the Army's hospitals and clinics within the southeastern United States and Puerto Rico.  SERMC was renamed Southern Regional Medical Command (SRMC) and was relocated to San Antonio in 2009.\n\nGeorge W. Weightman: Major General George W. Weightman was a U.S. Army Family Medicine physician who was commander of the North Atlantic Regional Medical Command and Walter Reed Army Medical Center (WRAMC).  He was relieved of his WRAMC command on March 1, 2007, in the wake of the Walter Reed Army Medical Center neglect scandal.  He took command of the U.S. Army Medical Research and Materiel Command in November 2007 and retired from active duty on 31 March 2009.\n\nFort Detrick: Fort Detrick is a United States Army Medical Command installation located in Frederick, Maryland.  Historically, Fort Detrick was the center of the US biological weapons program from 1943 to 1969.  Since the discontinuation of that program, it has hosted most elements of the United States biological defense program.\n\nQuestion: What year did the namesake of the Army Medical Command Installation in Frederick, Maryland die?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"installation_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the Army Medical Command installation.\"\n        },\n        \"location\": {\n          \"type\": \"string\",\n          \"description\": \"The location of the installation.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"location\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"namesake_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the person the installation is named after.\"\n        },\n        \"profession\": {\n          \"type\": \"string\",\n          \"description\": \"The profession of the namesake.\"\n        },\n        \"death_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the namesake died.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"profession\",\n        \"death_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"answer_death_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the namesake of the installation died.\"\n    }\n  },\n  \"required\": [\n    \"installation_details\",\n    \"namesake_details\",\n    \"answer_death_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "installation_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the Army Medical Command installation."
          },
          "location": {
            "type": "string",
            "description": "The location of the installation."
          }
        },
        "required": [
          "name",
          "location"
        ],
        "additionalProperties": false
      },
      "namesake_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the person the installation is named after."
          },
          "profession": {
            "type": "string",
            "description": "The profession of the namesake."
          },
          "death_year": {
            "type": "integer",
            "description": "The year the namesake died."
          }
        },
        "required": [
          "name",
          "profession",
          "death_year"
        ],
        "additionalProperties": false
      },
      "answer_death_year": {
        "type": "integer",
        "description": "The year the namesake of the installation died."
      }
    },
    "required": [
      "installation_details",
      "namesake_details",
      "answer_death_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
