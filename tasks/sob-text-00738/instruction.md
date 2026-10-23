{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBishop Gorman High School: Bishop Gorman High School (also commonly referred to as Gorman High School or BGHS) is a Roman Catholic, private, preparatory school located in Summerlin, Nevada.  The school is administered by the Diocese of Las Vegas, and has been serving Clark County and the Las Vegas Valley for over 50 years.  The school opened in 1954 and its mascot is a Gael, or mounted Irish Knight.\n\nUniversity of Nevada, Las Vegas: The University of Nevada, Las Vegas (UNLV) is an American public research university in the Las Vegas suburb of Paradise, Nevada.  The 332 acre campus is about 1.6 mi east of the Las Vegas Strip.  The university includes the Shadow Lane Campus, just east of the University Medical Center of Southern Nevada, which houses the School of Dental Medicine— the only dental school in Nevada.  In addition, UNLV's law school, the William S. Boyd School of Law, is also the only law school in the state.\n\nUNLV Rebels football: The UNLV Rebels football program is a college football team that represents the University of Nevada, Las Vegas (UNLV).  The team is currently a member of the Mountain West Conference, which is a Division I Bowl Subdivision (formerly Division I-A) conference of the National Collegiate Athletics Association (NCAA).  The program which began on September 14, 1968, is coached by former Bishop Gorman High School head coach, Tony Sanchez.  The team's home games are played at Sam Boyd Stadium in Whitney, Nevada.\n\nTony Sanchez (American football): Anthony Phillip Sanchez (born January 25, 1974) is the head coach of the UNLV Rebels.  Sanchez was hired by the Rebels on December 8, 2014.  He was previously the head football coach at Bishop Gorman High School.\n\nVijay P. Parashar: Vijay P. Parashar, BDS, MDS, DDS, is an oral and maxillofacial radiologist working as faculty at Midwestern University in Glendale, Arizona.  Prior to joining Midwestern University as Associate Professor, Parashar was the Assistant Professor of Biomedical and Diagnostic Sciences at University of Detroit Mercy in Detroit, Michigan.  Parashar won the 2006 Howard R. Raper and 2012 William H Rollins Oral and Maxillofacial Radiology Awards given by American Academy of Oral and Maxillofacial Radiology.  Parashar received Doctor of Dental Surgery (DDS) from the University of Detroit Mercy School of Dentistry, Master of Dental Science from the University of Connecticut School of Dental Medicine, Certification in Oral and Maxillofacial Radiology from the University of Connecticut School of Dental Medicine and Bachelor of Dental Surgery from Manipal College of Dental Sciences, Manipal.  Parashar is on the scientific editorial board of peer-reviewed journals such as \"Journal of Oral Health and Community\", \"India Dentistry\", \"International Journal of Oral Implantology and Clinical Research, India\", and \"American Journal of Esthetic Dentistry\", USA.  Parashar's positions with ADEA include,:\n\nVashti Cunningham: Vashti Cunningham (born January 18, 1998) is an American track and field athlete specializing in the high jump.  She is the daughter of retired National Football League (NFL) quarterback Randall Cunningham, niece of retired NFL fullback Sam Cunningham, and the younger sister of Randall Cunningham II.  Her mother is Felicity de Jager Cunningham a former ballerina with the Dance Theatre of Harlem.  Vashti, like her brother two years ahead of her in school, jumped for Bishop Gorman High School in Las Vegas, Nevada until March 2016 when she signed with Nike.  She announced she will continue her education at a university while competing as a professional athlete.\n\nUNLV School of Dental Medicine: University of Nevada, Las Vegas (UNLV) School of Dental Medicine is the dental school of the University of Nevada Las Vegas (UNLV).  The school is located on the Shadow Lane Campus, located just east of University Medical Center of Southern Nevada on Charleston and Shadow Lane, in Las Vegas, Nevada.  The school enrolls, on average, 80 freshmen per year.\n\nCase School of Dental Medicine: Case School of Dental Medicine (CSDM) is one of the graduate schools of Case Western Reserve University.  It is an American dental school located in Cleveland, Ohio.  Case School of Dental Medicine is one of the clinically oriented dental schools in the country, and has been ranked consistently high with its affiliated medical school.  Admission to Case Dental School is highly competitive with an acceptance rate at 2.1%.  Over 3700 applications for admission are received every year and 300 applicants are interviewed for the limited 75 positions.  The most recently admitted class had a mean undergraduate GPA of 3.81 and a mean DAT of 20 (~90th percentile).\n\nDurango High School (Nevada): Durango High School is a public high school in Spring Valley, Nevada, USA, with an enrollment of approximately 2600 students.  It is a part of the Area 4 region of the Clark County School District, which is the fifth largest school district in the United States.  Durango High School's main sports rivals are Bishop Gorman High School and Spring Valley High School.\n\nJoe Kristosik: Joe Kristosik (born c. 1974) is a former American football player.  After graduating from Bishop Gorman High School in Summerlin, Nevada, he entered the working world as a door-to-door salesman and a valet before enrolling at the University of Nevada, Las Vegas.  He was a walk-on to the UNLV Rebels football team and, after a redshirt season in 1994, he became the starting punter for the Rebels from 1995 to 1998.  As a senior, he led the NCAA with an average of 46.2 yards on 76 punts.  His average of 46.2 yards per punt was, at the time, the second-highest in NCAA history for a punter with at least 75 career attempts.  Kristosik was a consensus first-team selection for the 1998 College Football All-America Team.  He was inducted into the UNLV Athletic Hall of Fame in 2008.\n\nQuestion: an American public research university in the Las Vegas suburb of Paradise, Nevada which houses the School of Dental Medicine represents which program which began on September 14, 1968 and is coached by former Bishop Gorman High School head coach, Tony Sanchez?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"program_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the athletic program.\"\n    },\n    \"university_affiliation\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the university the program represents.\"\n        },\n        \"type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of university (e.g., public research).\"\n        },\n        \"location\": {\n          \"type\": \"string\",\n          \"description\": \"The location of the university.\"\n        },\n        \"houses_dental_school\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the university houses a school of dental medicine.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"type\",\n        \"location\",\n        \"houses_dental_school\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"program_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"start_date\": {\n          \"type\": \"string\",\n          \"description\": \"The date the program began.\"\n        },\n        \"coach\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"name\": {\n              \"type\": \"string\",\n              \"description\": \"The name of the program's head coach.\"\n            },\n            \"previous_role\": {\n              \"type\": \"string\",\n              \"description\": \"The coach's previous position before coaching this program.\"\n            },\n            \"previous_school\": {\n              \"type\": \"string\",\n              \"description\": \"The school where the coach held their previous role.\"\n            }\n          },\n          \"required\": [\n            \"name\",\n            \"previous_role\",\n            \"previous_school\"\n          ],\n          \"additionalProperties\": false\n        }\n      },\n      \"required\": [\n        \"start_date\",\n        \"coach\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"program_name\",\n    \"university_affiliation\",\n    \"program_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "program_name": {
        "type": "string",
        "description": "The name of the athletic program."
      },
      "university_affiliation": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the university the program represents."
          },
          "type": {
            "type": "string",
            "description": "The type of university (e.g., public research)."
          },
          "location": {
            "type": "string",
            "description": "The location of the university."
          },
          "houses_dental_school": {
            "type": "boolean",
            "description": "Indicates if the university houses a school of dental medicine."
          }
        },
        "required": [
          "name",
          "type",
          "location",
          "houses_dental_school"
        ],
        "additionalProperties": false
      },
      "program_details": {
        "type": "object",
        "properties": {
          "start_date": {
            "type": "string",
            "description": "The date the program began."
          },
          "coach": {
            "type": "object",
            "properties": {
              "name": {
                "type": "string",
                "description": "The name of the program's head coach."
              },
              "previous_role": {
                "type": "string",
                "description": "The coach's previous position before coaching this program."
              },
              "previous_school": {
                "type": "string",
                "description": "The school where the coach held their previous role."
              }
            },
            "required": [
              "name",
              "previous_role",
              "previous_school"
            ],
            "additionalProperties": false
          }
        },
        "required": [
          "start_date",
          "coach"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "program_name",
      "university_affiliation",
      "program_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
