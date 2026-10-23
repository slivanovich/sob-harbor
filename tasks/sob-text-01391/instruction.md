{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nFulton County School System: The Fulton County School System is a school district headquartered in Atlanta, Georgia, United States.  The system serves the area of Fulton County outside the Atlanta city limits (which are served by Atlanta Public Schools).  Fulton County Schools serve the cities of Alpharetta, Johns Creek, Milton, Mountain Park, Roswell, and Sandy Springs north of Atlanta, and Chattahoochee Hills, College Park, East Point, Fairburn, Hapeville, Palmetto, Union City, and Fulton's remaining unincorporated areas in the south.  Fulton County is the fourth-largest school system in Georgia.\n\nJackson County Public Schools (North Carolina): Jackson County Public Schools is a public school district serving Jackson County, North Carolina, USA.  It is headquartered in the county seat of Sylva.  The Jackson County School system is unique in the way that is still has a K-8 System with combined Elementary and Middle Schools, with one central High School and one combined K-12 Elementary/Middle/High School.  The county school system has eight schools, all with different histories and stories behind why they are the way they are today.  The school system includes four Kindergarten through 8th Grade Schools, two Kindergarten through 12th Grade Schools, one traditional 9th through 12th Grade High School, and one alternative 9th through 12th Grade High School Early College.\n\nJohns Creek, Georgia: Johns Creek is a city located in Fulton County in the U.S. state of Georgia.  According to the 2010 U.S. Census, the population was 76,728.  The city is an affluent northeastern suburb of Atlanta.  In 2017 Johns Creek ranked third on the \"USA TODAY\" list of \"50 best cities to live in.\"\n\nFeldwood High School: Feldwood High School was a public high school in unincorporated Fulton County, Georgia, United States.  It was a part of the Fulton County School System.  The school opened in the fall of 1976 as a result of growth and split class sessions at M.D. Collins High School.  In recognition of the bicentennial year, the colors selected for the school were red, white, and blue.\n\nBanneker High School (Georgia): Benjamin Banneker High School is a public high school in unincorporated Fulton County, Georgia, United States.  It is a part of Fulton County School System.  The school opened in fall 1988 as a result of the merger of M.D. Collins High School and Feldwood High School.  The school uses the former Feldwood High campus.  Collins High became Ronald E. McNair Middle School in the same year.  The merger happened as a result of a consolidation plan to reduce the costs of the school system, comply with new state laws mandating minimum attendance numbers for government funded schools, and upgrade the course offerings of all schools in the county.\n\nTri-Cities High School: Tri-Cities High School is a public high school in East Point, Georgia, United States.  It is a part of the Fulton County School System.  The school opened in 1988 under the leadership of principal Dr. Herschel Robinson.  It was originally formed by combining four schools: Woodland High School, Russell High School, College Park High School, and Hapeville High School.  Tri-Cities serves sections of East Point and College Park, and all of Hapeville.  The current principal is Termerion McCrary-Lakes.\n\nFayette County School System (Georgia): Fayette County School System is a public school district based in Fayetteville, Georgia, United States and covering residents of Fayette County.  The county is included in the Atlanta-Sandy Springs-Roswell Metropolitan Statistical Area.  The school system serves all of Fayette County.\n\nMobile County Public School System: Mobile County Public School System (MCPSS) is a school district based in Mobile County, Alabama United States.  The system currently serves all areas of Mobile County, including the city of Mobile, with the exception of the cities of Saraland, Satsuma and Chickasaw.  Saraland voted to separate its schools from Mobile County in 2006, with Satsuma and Chickasaw following suit in 2012.  The system serves urban, suburban, and rural areas.  All schools in the system are required to adopt school uniform policies.  It is the largest school system in Alabama and the 56th largest school system in the United States.\n\nRoswell High School (Georgia): Roswell High School (RHS) is a public high school in Roswell, Georgia, United States which opened in 1949.  It serves the entire city of Roswell west of Georgia 400 and the city of Mountain Park, as well as small portions of Alpharetta and Milton.  With a population of over of 2,233 students in the 2013–2014 school year, RHS is one of the largest schools in the Fulton County School System.  Roswell High School neighbors both Fellowship Christian School and Blessed Trinity Catholic High School.  It is also the second oldest of Fulton County's schools in the northern portion of the county, opening between Milton High School (1921), and Chattahoochee High School (1991).  Roswell is currently on its third campus, which opened in 1990.  The current building is the oldest in-use high school building in north Fulton.\n\nJohns Creek High School: Johns Creek High School is a public high school in Johns Creek, Georgia, United States, serving grades 9-12.  The school is a part of the Fulton County School System.  Its students primarily reside inside the city of Johns Creek, though the school also serves part of Alpharetta.  Students from Autrey Mill Middle School attend Johns Creek.  The school was opened in the fall of 2009 and as of 2017 has an enrollment around 2,076.\n\nQuestion: Fulton County School System serves what city ranked third on the \"USA TODAY\" list of \"50 best cities to live in\"?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"city_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the city.\"\n    },\n    \"school_system\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the school system serving the city.\"\n    },\n    \"ranking_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"rank\": {\n          \"type\": \"integer\",\n          \"description\": \"The rank of the city on the list.\"\n        },\n        \"list_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the list the city was ranked on.\"\n        },\n        \"source\": {\n          \"type\": \"string\",\n          \"description\": \"The publication or entity that published the list.\"\n        }\n      },\n      \"required\": [\n        \"rank\",\n        \"list_name\",\n        \"source\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"city_name\",\n    \"school_system\",\n    \"ranking_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "city_name": {
        "type": "string",
        "description": "The name of the city."
      },
      "school_system": {
        "type": "string",
        "description": "The name of the school system serving the city."
      },
      "ranking_details": {
        "type": "object",
        "properties": {
          "rank": {
            "type": "integer",
            "description": "The rank of the city on the list."
          },
          "list_name": {
            "type": "string",
            "description": "The name of the list the city was ranked on."
          },
          "source": {
            "type": "string",
            "description": "The publication or entity that published the list."
          }
        },
        "required": [
          "rank",
          "list_name",
          "source"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "city_name",
      "school_system",
      "ranking_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
