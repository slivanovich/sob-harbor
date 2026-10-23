{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMustang (military officer): A mustang is slang term in the United States Armed Forces, referring to a warrant officer or commissioned officer who began his or her career as an enlisted service member.  \"Mustang\" officers are generally older and more experienced than their peers-in-grade who entered the military, without prior enlisted service, via commissioning from one of the service academies (such as the United States Merchant Marine Academy, United States Military Academy, United States Air Force Academy, United States Naval Academy, or United States Coast Guard Academy), Officer Candidate School, or the Reserve Officer Training Corps.  During the Vietnam War, however, when some Army warrant officer pilots were offered a direct commission to 2nd or 1st Lieutenant, they were usually younger than 25 at the time of commission.  Department of Defense military pay tables authorize approximately ten percent pay premiums for officers in grades O-1, O-2 and O-3 who have credit for over four years of enlisted or warrant officer service prior to commissioning (Grades O-1E, O-2E, O-3E).\n\nAn Officer and a Gentleman: An Officer and a Gentleman is a 1982 American romantic drama film starring Richard Gere, Debra Winger and Louis Gossett, Jr., who won the Academy Award for Best Supporting Actor for the film.  It tells the story of Zack (Gere), a U.S. Navy Aviation Officer Candidate who is beginning his training at Aviation Officer Candidate School.  While Zack meets his first true girlfriend during his training, a local young woman named Paula (Winger), he also comes into conflict with the hard-driving Marine Corps Gunnery Sergeant (Gossett, Jr.), the drill instructor training his class.\n\nRobert Reimann (United States Navy officer): Robert T. Reimann (c. 1936-June 29, 2014) is a retired U.S. Navy rear admiral.  Born in Cambridge, Massachusetts, he graduated from Boston University in 1958.  He then attended the Officer Candidate School at Newport, Rhode Island, and was commissioned into the United States Naval Reserve as an ensign on 1 May 1959.\n\nWarrant Officer Basic Course: Warrant Officer Basic Course (WOBC) is the technical training program a newly appointed U.S. Army Warrant Officer receives after attending Warrant Officer Candidate School.  WOBC is designed to certify warrant officers as technically and tactically competent to serve in a designated military occupation specialty.  WOBC is the first major test a newly appointed officer must pass to continue serving in the Army as a warrant officer, as WO1 appointments and award of a Warrant Officer MOS are contingent upon successfully completing WOBC.\n\nOfficer Training Command Newport: Naval Officer Training Command Newport (or more simply, Officer Training School) is a unit of Naval Education and Training Command, located on Naval Station Newport in Newport, Rhode Island that is responsible to the Chief of Naval Education and Training for the development of civilians, enlisted, and newly commissioned personnel for service in the fleet as Naval Officers.  Outside of the requisite physical readiness testing, the programs are academic in nature, and with the exception of the student enrolled in the Naval Science Institute or Officer Candidate School, personnel will come to Officer Training School having already received their commission or warrant.\n\nAir Force Officer Training School: Officer Training School (OTS) is a United States Air Force commissioning program located at Maxwell Air Force Base in Montgomery, Alabama.  It is the current \"de facto\" officer candidate school (OCS) program for the U.S. Air Force, analogous to the OCS programs operated by the other branches of the U.S. armed forces.\n\nCOMDESPAC: Destroyer Force, United States Pacific Fleet, usually known as COMDESPAC, was a type command of the United States Pacific Fleet from 1940 until the Destroyer Force was combined with Cruisers, Pacific Fleet and in 1975 type command functions of both were transferred to Commander, Naval Surface Forces Pacific.  The Pacific Fleet Destroyer Force comprised the Destroyers of the fleet (DD) operating in Pacific Fleet area of responsibility.  The Commander, Destroyers, Pacific Fleet supervised the assignments, basing, maintenance of the destroyers, the training of crews and reported to the Commander in Chief, United States Pacific Fleet (CinCPac), on Destroyer operations.\n\nOfficer Candidate School – Philippines: The Officer Candidate School (OCS) is a military institution located at Camp O'Donnell, Capas, Tarlac for the Training and Doctrine Command, Philippine Army; Fernando Air Base in Lipa City, Batangas for the Philippine Air Force Officer Candidate School; and Naval Station Leovigildo Gantioqui in San Antonio, Zambales for the Philippine Navy Officer Candidate School.  It was established in the Philippines for training future officers of the Armed Forces of the Philippines (AFP).\n\nKorea Army Officer Candidate School: Korea Army Officer Candidate School (KAOCS, Hangul: 육군 학사사관, Hanja: 陸軍 學士士官) provides training to become a commissioned officer in the Republic of Korea Army.  Korea Army Officer Candidate School was first proposed on 28 June 1981.  Between 1981 and 2014, over 48,273 candidates were enrolled in 59 KAOCS classes and were commissioned as Second Lieutenants.\n\nNaval Station Newport: The Naval Station Newport (NAVSTA Newport) is a United States Navy base located in the city of Newport and the town of Middletown, Rhode Island.  Naval Station Newport is home to the Naval War College and the Naval Justice School.  It once was the homeport for Cruiser Destroyer Force Atlantic (COMCRUDESLANT), which relocated to Naval Station Norfolk in the early 1970s.  Newport now maintains inactive ships at its pier facilities, along with the United States Coast Guard.  In BRAC 2005 (Base Realignment and Closure), NAVSTA Newport gained over five hundred billets, in addition to receiving, again, the Officer Candidate School (OCS), the Naval Supply Corps School (in 2011), and several other activities, to include a few Army Reserve units.\n\nQuestion: Robert Reimann attended the Officer Candidate School in what city that was once homeport for Cruiser Destroyer Force Atlantic (COMCRUDESLANT)?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"officer_candidate_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the officer who attended the school.\"\n    },\n    \"school_attended\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the officer training school attended.\"\n    },\n    \"location\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"city\": {\n          \"type\": \"string\",\n          \"description\": \"The city where the school is located.\"\n        },\n        \"state\": {\n          \"type\": \"string\",\n          \"description\": \"The state where the school is located.\"\n        }\n      },\n      \"required\": [\n        \"city\",\n        \"state\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"historical_connection\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"entity_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the entity historically connected to the location.\"\n        },\n        \"event_description\": {\n          \"type\": \"string\",\n          \"description\": \"Description of the historical event or status.\"\n        }\n      },\n      \"required\": [\n        \"entity_name\",\n        \"event_description\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"officer_candidate_name\",\n    \"school_attended\",\n    \"location\",\n    \"historical_connection\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "officer_candidate_name": {
        "type": "string",
        "description": "The name of the officer who attended the school."
      },
      "school_attended": {
        "type": "string",
        "description": "The name of the officer training school attended."
      },
      "location": {
        "type": "object",
        "properties": {
          "city": {
            "type": "string",
            "description": "The city where the school is located."
          },
          "state": {
            "type": "string",
            "description": "The state where the school is located."
          }
        },
        "required": [
          "city",
          "state"
        ],
        "additionalProperties": false
      },
      "historical_connection": {
        "type": "object",
        "properties": {
          "entity_name": {
            "type": "string",
            "description": "The name of the entity historically connected to the location."
          },
          "event_description": {
            "type": "string",
            "description": "Description of the historical event or status."
          }
        },
        "required": [
          "entity_name",
          "event_description"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "officer_candidate_name",
      "school_attended",
      "location",
      "historical_connection"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
