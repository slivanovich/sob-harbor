{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMatthew C. Horner: Matthew Charles Horner (March 10, 1901 – June 27, 1972) was an Officer of the United States Marine Corps with the rank of Major General, who served as Supply Officer of 4th Marine Division and later as Commanding General of the Marine Corps Recruit Depot Parris Island.  The Major General Matthew C. Horner Chair of Military Theory is named in his honor.\n\nRobert B. Johnston: Robert B. Johnston (born October 6, 1937) is a retired United States Marine Corps lieutenant general whose last duty assignment was as Commander, Marine Forces Atlantic Marine Forces Europe and II Marine Expeditionary Force.  During the Gulf War, he served as the CENTCOM Chief-of-Staff.  He retired from the U.S. Marine Corps in 1995 after over 34 years of active duty service.\n\nGeorge R. Christmas: George Ronald Christmas (born March 11, 1940) is a retired United States Marine Corps lieutenant general.  Christmas was awarded the Navy Cross and Purple Heart for his valor in 1968 during the Vietnam War.  He served on active duty in the Marine Corps for 34 years, retiring in 1996.  He served as President and CEO of the Marine Corps Heritage Foundation.\n\nUSS Daly (DD-519): USS \"Daly\" (DD-519), a \"Fletcher\"-class destroyer, was a ship of the United States Navy named for Marine Sergeant Major Daniel Daly, (1873–1937), one of the very few people to be \"twice\" awarded the Medal of Honor.\n\nSmedley Butler: Smedley Darlington Butler (July 30, 1881June 21, 1940) was a United States Marine Corps major general, the highest rank authorized at that time, and at the time of his death the most decorated Marine in U.S. history.  During his 34-year career as a Marine, he participated in military actions in the Philippines, China, in Central America and the Caribbean during the Banana Wars, and France in World War I.  Butler is well known for having later become an outspoken critic of U.S. wars and their consequences, as well as exposing the Business Plot, an alleged plan to overthrow the U.S. government.\n\nDaniel Daly: Sergeant Major Daniel Joseph \"Dan\" Daly (November 11, 1873 – April 27, 1937) was an Irish American United States Marine and one of only nineteen men (including seven Marines) to have received the Medal of Honor twice.  Of the Marines who are double recipients, only Daly and Major General Smedley Butler received their Medals of Honor in two, separate, conflicts.\n\nRay L. Smith: Ray L. Smith is a retired United States Marine Corps major general.  Smith is a highly decorated Marine who has commanded infantry units at all levels.  His awards received for service in combat during the Vietnam War include the Navy Cross, two Silver Stars, the Bronze Star, and three Purple Hearts. MajGen Smith retired from the Marine Corps in 1999 after almost 34 years of service.  In 2003, after nearly four years of retirement, Smith went to Iraq with the 1st Marine Division; and penned an eyewitness account of the march from Kuwait to Baghdad — \"The March Up: Taking Baghdad with the 1st Marine Division.\"\n\nPeter Talleri: Major General Peter J. Talleri retired in September, 2013, after serving 34 years in the United States Marine Corps.  At retirement, Maj. Gen. Talleri was the U. S. Marine Corps senior logistics professional in the Pacific.  In 2013, he was also a recipient of the National Safety Council’s “CEOs Who Get It” award.\n\nJames E. Livingston: Major General James Everett Livingston (born January 12, 1940) is a retired United States Marine Corps major general.  He was awarded the United States' highest military decoration—the Medal of Honor—for heroic actions in 1968 during the Vietnam War.  Livingston served on active duty in the Marine Corps over 33 years before retiring on September 1, 1995.  His last assignment was the Commanding General of Marine Forces Reserve in New Orleans, Louisiana.\n\nCross-country skiing at the 1936 Winter Olympics: The 1936 Winter Olympics were held in Garmisch-Partenkirchen, Germany.  The games began on February 6, 1936, and ended on February 16th, 1936.  There were three Cross-Country skiing events held, in which only men competed.  There were 109 male competitors from 22 different nations.  The youngest participant was 17-year-old Resat Erces from Turkey, while the oldest participant was Nils Backstrom from the United States of America at 34 years old.  The athletes whom collected the most medals were Oddbjorn Hagen of Norway, and Erik Larsson of Sweden- each received two medals.  Sweden collected more medals than any other country in the Cross-Country skiing events at a total of 5.\n\nQuestion: Which Major General was a Marine for 34 years and has received two separate Medals of Honor like Marine Daniel Daly?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"marine_officer_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the Marine officer.\"\n    },\n    \"rank\": {\n      \"type\": \"string\",\n      \"description\": \"The highest rank achieved by the officer.\"\n    },\n    \"years_of_service\": {\n      \"type\": \"integer\",\n      \"description\": \"The total number of years the officer served in the Marine Corps.\"\n    },\n    \"medal_of_honor_recipient\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the officer received the Medal of Honor.\"\n    },\n    \"number_of_medals_of_honor\": {\n      \"type\": \"integer\",\n      \"description\": \"The count of Medals of Honor received by the officer.\"\n    },\n    \"medals_awarded_in_separate_conflicts\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the Medals of Honor were awarded for actions in two separate conflicts.\"\n    },\n    \"comparison_to_daniel_daly\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"daniel_daly_medal_of_honor_count\": {\n          \"type\": \"integer\",\n          \"description\": \"The number of Medals of Honor received by Daniel Daly.\"\n        },\n        \"daniel_daly_medals_in_separate_conflicts\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if Daniel Daly's Medals of Honor were received in separate conflicts.\"\n        }\n      },\n      \"required\": [\n        \"daniel_daly_medal_of_honor_count\",\n        \"daniel_daly_medals_in_separate_conflicts\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"marine_officer_name\",\n    \"rank\",\n    \"years_of_service\",\n    \"medal_of_honor_recipient\",\n    \"number_of_medals_of_honor\",\n    \"medals_awarded_in_separate_conflicts\",\n    \"comparison_to_daniel_daly\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "marine_officer_name": {
        "type": "string",
        "description": "The full name of the Marine officer."
      },
      "rank": {
        "type": "string",
        "description": "The highest rank achieved by the officer."
      },
      "years_of_service": {
        "type": "integer",
        "description": "The total number of years the officer served in the Marine Corps."
      },
      "medal_of_honor_recipient": {
        "type": "boolean",
        "description": "Indicates if the officer received the Medal of Honor."
      },
      "number_of_medals_of_honor": {
        "type": "integer",
        "description": "The count of Medals of Honor received by the officer."
      },
      "medals_awarded_in_separate_conflicts": {
        "type": "boolean",
        "description": "Indicates if the Medals of Honor were awarded for actions in two separate conflicts."
      },
      "comparison_to_daniel_daly": {
        "type": "object",
        "properties": {
          "daniel_daly_medal_of_honor_count": {
            "type": "integer",
            "description": "The number of Medals of Honor received by Daniel Daly."
          },
          "daniel_daly_medals_in_separate_conflicts": {
            "type": "boolean",
            "description": "Indicates if Daniel Daly's Medals of Honor were received in separate conflicts."
          }
        },
        "required": [
          "daniel_daly_medal_of_honor_count",
          "daniel_daly_medals_in_separate_conflicts"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "marine_officer_name",
      "rank",
      "years_of_service",
      "medal_of_honor_recipient",
      "number_of_medals_of_honor",
      "medals_awarded_in_separate_conflicts",
      "comparison_to_daniel_daly"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
