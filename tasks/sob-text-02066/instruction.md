{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJohn Anthony Walker: John Anthony Walker, Jr. (July 28, 1937 – August 28, 2014) was a United States Navy Chief Warrant Officer and communications specialist convicted of spying for the Soviet Union from 1968 to 1985.\n\nJerry Whitworth: Jerry Alfred Whitworth (born 1939) was sentenced to 365 years for his part in the Walker family spy ring, which, at the time of Whitworth's arrest, U.S. authorities described as \"the most damaging espionage ring uncovered in the United States in three decades\"\n\nMaster at Arms of the Navy: Master at Arms of the Navy is the most senior Warrant Officer in the South African Navy (SAN).  It is a singular appointment – it is only held by one person at any time.  The Master at Arms of the Navy holds the rank of Senior Chief Warrant Officer\n\nChief petty officer, 1st class: Chief petty officer, 1st class, CPO1, is the most senior non-commissioned member (NCM) rank of the Royal Canadian Navy.  It is equivalent to a chief warrant officer (CWO) in the Canadian Army and Royal Canadian Air Force.  It is immediately senior to the rank of chief petty officer 2nd-class and its equivalents, master warrant officer; it is part of the cadre of warrant officers.\n\nArmy Staff Senior Warrant Officer: The Army Staff Senior Warrant Officer (ARSTAF SWO) provides the Chief of Staff of the United States Army (CSA) with subject matter expertise on warrant officer training and development, to include proper balance of training, education and professional experience for warrant officers.  Additionally, the ARSTAF SWO communicates with commanders and warrant officers throughout the United States Army to ensure their concerns and recommendations are considered in decisions that will impact the future of the warrant officer corps.\n\nFrederick Edgar Ferguson: Frederick Edgar Ferguson (born August 18, 1939) is a former United States Army warrant officer and later officer, as well as a recipient of the United States military's highest decoration—the Medal of Honor—for his actions in the Vietnam War while a chief warrant officer 3.\n\nMichael Durant: Michael J. \"Mike\" Durant (born July 23, 1961) is an American pilot and author.  He was a member of the 160th Special Operations Aviation Regiment (Night Stalkers) as a Chief Warrant Officer 3.  He retired from the Army as a Chief Warrant Officer 4 Blackhawk helicopter Master Aviator in the 160th SOAR after participating in combat operations Prime Chance, Just Cause, and Desert Storm, and also Gothic Serpent, in which he was briefly held prisoner in 1993 after a raid in Somalia.  His awards include the Distinguished Service Medal, Distinguished Flying Cross with Oak Leaf Cluster, Bronze Star with Valor Device, Purple Heart, Meritorious Service Medal, three Air Medals, Prisoner of War Medal, and many others.\n\nChief warrant officer: Chief Warrant Officer is a military rank used by the United States Armed Forces, the Canadian Armed Forces, the Pakistan Air Force, the Israel Defense Forces, the South African National Defence Force, the Lebanese Armed Forces and, since 2012, the Singapore Armed Forces.  In the United States Armed Forces Chief Warrant Officers are actual officers, not NCOs like other NATO forces.\n\nMustang (military officer): A mustang is slang term in the United States Armed Forces, referring to a warrant officer or commissioned officer who began his or her career as an enlisted service member.  \"Mustang\" officers are generally older and more experienced than their peers-in-grade who entered the military, without prior enlisted service, via commissioning from one of the service academies (such as the United States Merchant Marine Academy, United States Military Academy, United States Air Force Academy, United States Naval Academy, or United States Coast Guard Academy), Officer Candidate School, or the Reserve Officer Training Corps.  During the Vietnam War, however, when some Army warrant officer pilots were offered a direct commission to 2nd or 1st Lieutenant, they were usually younger than 25 at the time of commission.  Department of Defense military pay tables authorize approximately ten percent pay premiums for officers in grades O-1, O-2 and O-3 who have credit for over four years of enlisted or warrant officer service prior to commissioning (Grades O-1E, O-2E, O-3E).\n\nRobert Cléroux: Chief Petty Officer 1st Class Robert 'Bob' Cléroux {'1': \", '2': \", '3': \", '4': \"} is a retired Royal Canadian Navy chief petty officer 1st class.  He served as the Canadian Forces Chief Warrant Officer from 2010 to 2013.\n\nQuestion: Who was the United States Navy Chief Warrant Officer that was convicted for what was described as \"the most damaging espionage ring uncovered in the United States in three decades?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the individual.\"\n    },\n    \"military_rank\": {\n      \"type\": \"string\",\n      \"description\": \"The military rank of the individual.\"\n    },\n    \"service_branch\": {\n      \"type\": \"string\",\n      \"description\": \"The branch of the military the individual served in.\"\n    },\n    \"crime_summary\": {\n      \"type\": \"string\",\n      \"description\": \"A summary of the crime the individual was convicted of.\"\n    },\n    \"espionage_ring_description\": {\n      \"type\": \"string\",\n      \"description\": \"The description given to the espionage ring the individual was part of.\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"military_rank\",\n    \"service_branch\",\n    \"crime_summary\",\n    \"espionage_ring_description\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The full name of the individual."
      },
      "military_rank": {
        "type": "string",
        "description": "The military rank of the individual."
      },
      "service_branch": {
        "type": "string",
        "description": "The branch of the military the individual served in."
      },
      "crime_summary": {
        "type": "string",
        "description": "A summary of the crime the individual was convicted of."
      },
      "espionage_ring_description": {
        "type": "string",
        "description": "The description given to the espionage ring the individual was part of."
      }
    },
    "required": [
      "person_name",
      "military_rank",
      "service_branch",
      "crime_summary",
      "espionage_ring_description"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
