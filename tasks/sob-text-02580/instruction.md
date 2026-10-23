{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nTask Force 121: Task Force 121 was a United States Department of Defense special operations task force.  TF121 was a multi-service force from Joint Special Operations Command, made up of operators from the U.S. Army's Delta Force, 75th Ranger Regiment, and 160th Special Operations Aviation Regiment, the U.S. Navy's SEAL Team Six ,the CIA's Special Activities Division, U.S. Air Force Combat Controllers, Pararescuemen, Tactical Air Control Party operators, and Special Operations Weather Technicians, the Aviation Tactics Evaluation Group (AvTEG), and the Joint Communications Unit.  Two Troops from the U.S. Army 1st Squadron, 1st Cavalry Regiment provided armor support for the Task Force.\n\nUnited States Navy SEALs in popular culture: This is a list of depictions of U.S. Navy SEALs in popular culture.  The United States Navy's Navy SEALs are the U.S. Navy's principal special operations force and a part of the Naval Special Warfare Command and United States Special Operations Command.\n\nUnited States Navy SEALs: The United States Navy's \"Sea, Air, and Land\" Teams, commonly abbreviated as the Navy SEALs, are the U.S. Navy's primary special operations force and a component of the Naval Special Warfare Command.  Among the SEALs' main functions are conducting small-unit maritime military operations that originate from, and return to, a river, ocean, swamp, delta, or coastline.  The SEALs are trained to operate in all environments (Sea, Air, and Land) for which they are named.  The SEALs are widely considered one of the most effective special operations forces units in the world, if not the most effective.\n\nLithuanian Special Operations Force: The Lithuanian Special Operations Force (LITHSOF) (Lithuanian: \"Lietuvos Specialiųjų Operacijų Pajėgos\" ) is a special operation unit of the Lithuanian Armed Forces, formed exclusively of carefully selected, motivated and specially trained professionals.  The main tasks of the Special Operations Force are counter terrorism, special reconnaissance, and hostage rescue.\n\nList of United States Navy SEALs: This is a list of notable current and former members of the United States Navy SEALs and Underwater Demolition Teams.  Founded in 1962, the SEALs are the U.S. Navy's principal special operations force.  The name \"SEALs\" represents the environments in which they operate: sea, air and land.  Navy SEALs are trained and have been deployed in a wide variety of missions, including direct action, special reconnaissance, unconventional warfare, foreign internal defense, hostage rescue, counter-terrorism, and other missions.\n\nSpecial Forces (United States Army): The United States Army Special Forces; colloquially known as the Green Berets (due to their distinctive service headgear), are a special operations force tasked with five primary missions: unconventional warfare (the original and most important mission of Special Forces), foreign internal defense, special reconnaissance, direct action, and counter-terrorism.  The first two emphasize language, cultural, and training skills in working with foreign troops.  Other duties include combat search and rescue (CSAR), counter-narcotics, counter-proliferation, hostage rescue, humanitarian assistance, humanitarian demining, information operations, peacekeeping, psychological operations, security assistance, and manhunts; other components of the United States Special Operations Command (USSOCOM) or other U.S. government activities may also specialize in these secondary areas.  Many of their operational techniques are classified, but some nonfiction works and doctrinal manuals are available.\n\nUnited States Air Force Special Tactics Officer: A United States Air Force Special Tactics Officer (AFSC 13CX) is a United States Air Force Special Operations Command (AFSOC) officer who manages the training and equipping of U.S. Air Force ground special operations.  Special Tactics Officers deploy as team leaders or mission commanders in combat, seizing and controlling airstrips, combat search and rescue, guiding airstrikes and fire support using air assets for special operations and tactical weather observations and forecasting.  Special Tactics Officers are not pararescuemen or Combat Controllers, but they lead the Special Tactics Squadrons and Groups and thoroughly understand how to conduct, manage, and provide these special operations missions to both conventional and joint special operations missions needed within Joint Special Operations Command (JSOC) and United States Special Operations Command (SOCOM).\n\nRescue of Jessica Buchanan and Poul Hagen Thisted: On January 25, 2012, a team of United States Navy SEALs raided a compound 12 miles north of the Somali town of Adow, killing nine Somali pirates and freeing their hostages, U.S. citizen Jessica Buchanan and Danish citizen Poul Hagen Thisted.\n\nJoint Task Force 2: Joint Task Force 2 (JTF2) (French: \"Force opérationnelle interarmées 2, FOI 2\" ) is an elite special operations force of the Canadian Armed Forces.  JTF2 serves alongside the Canadian Special Operations Regiment, the Canadian Joint Incident Response Unit and 427 Special Operations Aviation Squadron as part of the Canadian Special Operations Forces Command.  The unit is currently based at Dwyer Hill, near Ottawa, Ontario, and plans to move to a new facility to be built at CFB Trenton by 2019.\n\nNavy SEALs (disambiguation): The Navy SEALs are the U.S. Navy's primary special operations force.\n\nQuestion: What hostage U.S. citizen did the U.S. Navy's primary special operations force free 12 miles north of the Somali town of Adow on January 25, 2012?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"rescuing_force_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the special operations force that conducted the rescue.\"\n        },\n        \"affiliation\": {\n          \"type\": \"string\",\n          \"description\": \"The military branch or command the force belongs to.\"\n        },\n        \"force_type\": {\n          \"type\": \"string\",\n          \"description\": \"The general type of the force, e.g., 'primary special operations force'.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"affiliation\",\n        \"force_type\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"rescue_operation_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"date\": {\n          \"type\": \"string\",\n          \"format\": \"date\",\n          \"description\": \"The date when the rescue operation took place.\"\n        },\n        \"location_description\": {\n          \"type\": \"string\",\n          \"description\": \"A description of the location where the rescue occurred.\"\n        },\n        \"hostages_freed\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"object\",\n            \"properties\": {\n              \"name\": {\n                \"type\": \"string\",\n                \"description\": \"The name of the hostage.\"\n              },\n              \"nationality\": {\n                \"type\": \"string\",\n                \"description\": \"The nationality of the hostage.\"\n              }\n            },\n            \"required\": [\n              \"name\",\n              \"nationality\"\n            ],\n            \"additionalProperties\": false\n          },\n          \"description\": \"A list of individuals freed during the operation.\"\n        }\n      },\n      \"required\": [\n        \"date\",\n        \"location_description\",\n        \"hostages_freed\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"us_citizen_hostage_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the U.S. citizen hostage freed in the operation.\"\n    }\n  },\n  \"required\": [\n    \"rescuing_force_details\",\n    \"rescue_operation_details\",\n    \"us_citizen_hostage_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "rescuing_force_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the special operations force that conducted the rescue."
          },
          "affiliation": {
            "type": "string",
            "description": "The military branch or command the force belongs to."
          },
          "force_type": {
            "type": "string",
            "description": "The general type of the force, e.g., 'primary special operations force'."
          }
        },
        "required": [
          "name",
          "affiliation",
          "force_type"
        ],
        "additionalProperties": false
      },
      "rescue_operation_details": {
        "type": "object",
        "properties": {
          "date": {
            "type": "string",
            "format": "date",
            "description": "The date when the rescue operation took place."
          },
          "location_description": {
            "type": "string",
            "description": "A description of the location where the rescue occurred."
          },
          "hostages_freed": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string",
                  "description": "The name of the hostage."
                },
                "nationality": {
                  "type": "string",
                  "description": "The nationality of the hostage."
                }
              },
              "required": [
                "name",
                "nationality"
              ],
              "additionalProperties": false
            },
            "description": "A list of individuals freed during the operation."
          }
        },
        "required": [
          "date",
          "location_description",
          "hostages_freed"
        ],
        "additionalProperties": false
      },
      "us_citizen_hostage_name": {
        "type": "string",
        "description": "The name of the U.S. citizen hostage freed in the operation."
      }
    },
    "required": [
      "rescuing_force_details",
      "rescue_operation_details",
      "us_citizen_hostage_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
