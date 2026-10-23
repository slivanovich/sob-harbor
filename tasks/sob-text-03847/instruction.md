{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLas Animas, Colorado: Las Animas is the Statutory City that is the county seat and the only incorporated municipality in Bent County, Colorado, United States.  The city population was 2,410 at the 2010 United States Census.  Las Animas is located in southeast Colorado east of Pueblo, near the historic Bent's Fort.\n\nHorseshoe Mountain (Colorado): Horseshoe Mountain is a high mountain summit in the Mosquito Range of the Rocky Mountains of North America.  The 13905 ft thirteener is located 11.5 km southeast by east (bearing 126°) of the City of Leadville, Colorado, United States, on the drainage divide separating San Isabel National Forest and Lake County from Pike National Forest and Park County.\n\nHigh Mountain Institute: The High Mountain Institute (HMI) is a non-profit educational organization located in Leadville, Colorado.  Founded in 1998 by Molly and Christopher Barnes, HMI focuses on educating teenagers through interaction with the natural world.  The school offers semester and summer programs for high-school students and programs for middle-schoolers and adults.\n\nDyer Mountain: Dyer Mountain is a high mountain summit in the Mosquito Range of the Rocky Mountains of North America.  The 13862 ft thirteener is located 9.5 km east (bearing 95°) of the City of Leadville, Colorado, United States, on the drainage divide separating San Isabel National Forest and Lake County from Pike National Forest and Park County.  The mountain was named in honor of frontier preacher John Lewis Dyer.\n\nMount Sherman: Mount Sherman is a high mountain summit in the Mosquito Range of the Rocky Mountains of North America.  The 14043 ft fourteener is located 11.0 km east by south (bearing 103°) of the City of Leadville, Colorado, United States, on the drainage divide separating San Isabel National Forest and Lake County from Pike National Forest and Park County.  The mountain was named in honor of General William Tecumseh Sherman.\n\nLeadville, Colorado: Leadville is the statutory city that is the county seat and only incorporated municipality in Lake County, Colorado, United States.  The city population was 2,602 at the 2010 United States Census.  Situated at an elevation of 10152 ft , Leadville is the highest incorporated city and the second highest incorporated municipality in the United States.  A former silver mining town that lies near the headwaters of the Arkansas River in the heart of the Rocky Mountains, the Leadville Historic District contains many historic structures and sites from its dynamic mining era.  In the late 19th century, Leadville was the second most populous city in Colorado, after Denver.\n\nLake County, Colorado: Lake County is one of the 64 counties in the U.S. state of Colorado.  As of the 2010 census, the population was 7,310.  The county seat and the only municipality in the county is Leadville.  The highest natural point in Colorado and the entire Rocky Mountains is the summit of Mount Elbert in Lake County at 14,440 feet (4401.2 meters) elevation.\n\nHMI Semester: The HMI Semester is a semester-long educational program for high school juniors located at the High Mountain Institute's campus in Leadville, Colorado.  HMI Semester welcomed its first class in 1998 with Molly and Christopher Barnes as its first directors.  Since its inception, the HMI Semester has served as a unique opportunity for talented high school juniors to spend a semester living, traveling, and studying in the mountains of central Colorado and the canyons of southeastern Utah, combining the academic program of a rigorous college preparatory boarding school with the adventure of a summer backpacking expedition.  Students spend five weeks over the course of the semester on three wilderness expeditions that focus on leadership and community-building and twelve weeks on campus completing a standard junior year curriculum.  Admission for HMI Semester's forty-eight spots is highly competitive, with the applicant pool centered on a group of customary \"sending schools\" that have supported the Institute from its start.  In June 2013, the HMI Semester celebrated its fifteen-year reunion on campus where alumni from all semesters were invited to reconnect and appreciate the HMI community.\n\nFrench Mountain: French Mountain is a high mountain summit in the Sawatch Range of the Rocky Mountains of North America.  The 13966 ft thirteener is located on the Elbert Massif in San Isabel National Forest, 20.9 km southwest by west (bearing 231°) of the City of Leadville in Lake County, Colorado, United States.\n\nTibetan Language Institute: The Tibetan Language Institute is a private, non-profit educational organization located in Hamilton, Montana.  Its mission is to present classes, seminars, workshops, and public lectures on Tibetan language, literature, and philosophy for the purpose of preserving Tibetan culture and enriching one's study of the Dharma.\n\nQuestion: The High Mountain Institute (HMI) is a non-profit educational organization located in Leadville, the statutory city that is the county seat, and only incorporated municipality, in Lake County, Colorado, in which country?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"organization_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the educational organization.\"\n    },\n    \"organization_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of the organization, e.g., non-profit educational organization.\"\n    },\n    \"location_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"city\": {\n          \"type\": \"string\",\n          \"description\": \"The city where the organization is located.\"\n        },\n        \"state\": {\n          \"type\": \"string\",\n          \"description\": \"The state where the organization is located.\"\n        },\n        \"country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the organization is located.\"\n        }\n      },\n      \"required\": [\n        \"city\",\n        \"state\",\n        \"country\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"city_context\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"city_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the city providing context.\"\n        },\n        \"county_seat_of\": {\n          \"type\": \"string\",\n          \"description\": \"The county for which the city is the county seat.\"\n        },\n        \"is_only_incorporated_municipality_in_county\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the city is the only incorporated municipality in its county.\"\n        }\n      },\n      \"required\": [\n        \"city_name\",\n        \"county_seat_of\",\n        \"is_only_incorporated_municipality_in_county\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"organization_name\",\n    \"organization_type\",\n    \"location_details\",\n    \"city_context\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "organization_name": {
        "type": "string",
        "description": "The name of the educational organization."
      },
      "organization_type": {
        "type": "string",
        "description": "The type of the organization, e.g., non-profit educational organization."
      },
      "location_details": {
        "type": "object",
        "properties": {
          "city": {
            "type": "string",
            "description": "The city where the organization is located."
          },
          "state": {
            "type": "string",
            "description": "The state where the organization is located."
          },
          "country": {
            "type": "string",
            "description": "The country where the organization is located."
          }
        },
        "required": [
          "city",
          "state",
          "country"
        ],
        "additionalProperties": false
      },
      "city_context": {
        "type": "object",
        "properties": {
          "city_name": {
            "type": "string",
            "description": "The name of the city providing context."
          },
          "county_seat_of": {
            "type": "string",
            "description": "The county for which the city is the county seat."
          },
          "is_only_incorporated_municipality_in_county": {
            "type": "boolean",
            "description": "Indicates if the city is the only incorporated municipality in its county."
          }
        },
        "required": [
          "city_name",
          "county_seat_of",
          "is_only_incorporated_municipality_in_county"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "organization_name",
      "organization_type",
      "location_details",
      "city_context"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
