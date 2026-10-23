{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nWindermere, Florida: Windermere is a town in Orange County, Florida, United States.  As of the 2010 census, the town population was 2,462.  It is part of the Orlando–Kissimmee Metropolitan Statistical Area.\n\nBalša Koprivica: Balša Koprivica (; born May 1, 2000) is a Serbian basketball player who attends Windermere Preparatory School in Lake Butler, Orange County, Florida.  He is considered one of the top ten college recruits in the Class of 2019.\n\nRexford College Preparatory School: Rexford College Preparatory High School was a small private school which originated in the early 1950s in Beverly Hills, California and was originally known as \"Rexford Junior and Senior High School\".  The owners and originators of the school were David and Pearl Axlerod.  The school was known for its small class size and individual attention in academia for students.  Rexford College Preparatory High School consisted of grades 7 through 12 originally, then in later years consisted of grades 9 through 12.  The school was sold in 1971, and later became known as Concord.  The school had many celebrities and families of the elite.  \"Rexford\" was located at 9250 Olympic Boulevard, Beverly Hills, California 90210 in a Classic Spanish style Duplex typical and symbolic of the architecture of Los Angeles in the 1940s.  It is now part of Beverly Hills Preparatory School.\n\nIona Preparatory School: Iona Preparatory School (commonly known as Iona Prep) is an independent, Roman Catholic, all-male, college preparatory school located in the north end of New Rochelle, New York, in suburban Westchester County.  Iona Prep consists of the Upper School for grades 9 through 12 and the Lower School (formerly Iona Grammar School) for grades kindergarten through eighth grade.  The primary and secondary schools are located on separate and nearby campuses less than a mile apart on Stratton Road.  Named for the Scottish island of Iona, the school was founded in 1916 by the Congregation of Christian Brothers.  Iona is a privately owned independent school without parochial affiliation and is located within the Archdiocese of New York.\n\nRutgers Preparatory School: Rutgers Preparatory School (also known as Rutgers Prep or RPS) is a private, coeducational, college preparatory day school serving students in pre-kindergarten through twelfth grade, located on a 41 acre campus along the banks of the Delaware and Raritan Canal in the Somerset section of Franklin Township, in Somerset County, New Jersey, United States.  Established in 1766, Rutgers Preparatory School is the oldest independent school in the state of New Jersey and the 16th-oldest in the country.\n\nStanton College Preparatory School: Stanton College Preparatory School is an academically renowned public high school in Jacksonville, Florida.  The school's history dates to the 1860s when it was begun as an elementary school serving the African-American population under the then-segregated education system.  It now serves secondary students (grades 9-12) within the Duval County Public Schools of Duval County, Florida.  The school offers special curricula which include Honors courses, Advanced Placement, and International Baccalaureate courses.  In 2005, the Advanced Placement Report to the Nation officially recognized Stanton College Preparatory School as the best large size high school for Advanced Placement European History and Advanced Placement English Literature and Composition in the world.\n\nPaxon School for Advanced Studies: Paxon School for Advanced Studies (PSAS) is one of three International Baccalaureate senior high schools (the others being Stanton College Preparatory School, and Jean Ribault High School) in Duval County, Florida.  According to the College Board's Advanced Placement Report, Paxon has one of the strongest math and science Advanced Placement programs in the state of Florida, right behind their rival school Stanton College Preparatory School.  Because of this accomplishment, Paxon is one of a select group of Florida schools invited to apply for the Siemens Advanced Placement High School Award.  Only ten to fifteen schools per state are invited to apply.  Some valedictorians have been accepted to the United States Naval Academy and different Ivy League schools.\n\nSherborne Preparatory School: Sherborne Preparatory School is a non-selective coeducational preparatory school in the town of Sherborne, Dorset in southern England.  It is not officially affiliated with Sherborne School, located just down the street, although they once shared the same campus and many boys transfer to the school after finishing at the prep school.  Pupils generally go on to other independent schools around the county, mainly the nearby Sherborne School and Sherborne Girls as well as other schools in South West England.\n\nRiviera Schools: Riviera Schools is a private, independent school with two separate campuses, both in Miami-Dade County, Florida.  It is composed of Riviera Day School and Riviera Preparatory School, with the campuses located under four miles apart.  The co-educational, college preparatory school serves students from pre-school through 12th grade.\n\nWindermere Preparatory School: Windermere Preparatory School is a private, coeducational PK-12 college preparatory school in Lake Butler, an unincorporated area in Orange County, Florida, within the Orlando metropolitan area.  Established in 2000 and in proximity to the Town of Windermere, it is accredited by the Southern Association of Colleges and Schools, Southern Association of Independent Schools, Florida Council of Independent Schools, and International Baccalaureate World School.  It is a part of the Nord Anglia Education network.\n\nQuestion: Windermere Preparatory school is located in windermere a small town in which county of florida?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"school_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the preparatory school.\"\n    },\n    \"location_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"county\": {\n          \"type\": \"string\",\n          \"description\": \"The county where the school is located.\"\n        },\n        \"state\": {\n          \"type\": \"string\",\n          \"description\": \"The state where the school is located.\"\n        },\n        \"is_in_proximity_to_town\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the school is in proximity to the town mentioned in the question.\"\n        }\n      },\n      \"required\": [\n        \"county\",\n        \"state\",\n        \"is_in_proximity_to_town\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"town_of_interest\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the town mentioned in the question.\"\n    }\n  },\n  \"required\": [\n    \"school_name\",\n    \"location_details\",\n    \"town_of_interest\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "school_name": {
        "type": "string",
        "description": "The name of the preparatory school."
      },
      "location_details": {
        "type": "object",
        "properties": {
          "county": {
            "type": "string",
            "description": "The county where the school is located."
          },
          "state": {
            "type": "string",
            "description": "The state where the school is located."
          },
          "is_in_proximity_to_town": {
            "type": "boolean",
            "description": "Indicates if the school is in proximity to the town mentioned in the question."
          }
        },
        "required": [
          "county",
          "state",
          "is_in_proximity_to_town"
        ],
        "additionalProperties": false
      },
      "town_of_interest": {
        "type": "string",
        "description": "The name of the town mentioned in the question."
      }
    },
    "required": [
      "school_name",
      "location_details",
      "town_of_interest"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
