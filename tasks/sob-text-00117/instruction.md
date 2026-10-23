{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMapletown, Pennsylvania: Mapletown is an unincorporated community and census-designated place in Monongahela Township, Greene County, Pennsylvania, in the United States.  It is located 1 mi west of the Monongahela River in southeastern Greene County.  As of the 2010 census the population was 130.\n\nShawnee Hills, Greene County, Ohio: Shawnee Hills is a census-designated place (CDP) in Greene County, Ohio, United States.  Shawnee Hills consists of a planned community centered on the 250 acre Shawnee Lake.  The population was 2,171 at the 2010 census, down from 2,355 at the 2000 census.  It is part of the Dayton Metropolitan Statistical Area, and should not be confused with the incorporated village of Shawnee Hills in Delaware County.\n\nMather, Pennsylvania: Mather is an unincorporated community and census-designated place in Morgan Township, Greene County, Pennsylvania, in the United States.  The community is located 1 mi northwest of the borough of Jefferson, near Pennsylvania Route 188.  It is 5 mi northeast of Waynesburg, the Greene County seat.  As of the 2010 census the population of Mather was 737.\n\nWest Waynesburg, Pennsylvania: West Waynesburg is a census-designated place in Franklin Township, Greene County, Pennsylvania, in the United States.  It is located next to the western border of Waynesburg, the Greene County seat, within a mile of downtown, along Pennsylvania Routes 18 and 21.  As of the 2010 census the population of West Waynesburg was 446.\n\nWind Ridge, Pennsylvania: Wind Ridge is an unincorporated community and census-designated place (CDP) in Richhill Township, Greene County, Pennsylvania, United States.  It is located along Pennsylvania Route 21, 18 mi west of Waynesburg, the Greene County seat, and 5 mi east of the West Virginia border.  As of the 2010 census the population was 215.\n\nWaynesburg Historic District: Waynesburg Historic District is a national historic district located at Waynesburg, Greene County, Pennsylvania.  The district includes 183 contributing buildings in the central business district and surrounding residential areas of Waynesburg.  The buildings include notable examples of High Victorian Italianate, Second Empire, Queen Anne, and Georgian Revival style architecture.  Notable non-residential buildings include 10 buildings associated with Waynesburg University, 7 churches, the Greene County Courthouse, Greene County Jail, and Waynesboro Borough Building.  Among the buildings at Waynesburg University are the separately listed Hanna Hall and Miller Hall.\n\nRick Comegy: Rick Comegy (born September 24, 1953) is an American football coach and former player.  On January 21, 2014, Comegy was introduced as the head coach at Mississippi Valley State.  He previously served as the head football coach at Jackson State University in Jackson, Mississippi from 2006 to 2013.  He was named JSU head coach on December 9, 2005 after ten years as head coach of Tuskegee University, where he compiled a 90–26 record.  He has also served as head coach of Cheyney University and Central State University, where he won the NAIA national football championship in 1995.  He served as an assistant coach at Central State University under former Cheyney/Central State/Florida A&M coach Billy Joe in the 80s and 90s.\n\nRogersville, Pennsylvania: Rogersville is an unincorporated community and census-designated place (CDP) in Center Township, Greene County, Pennsylvania, United States.  It is located 6 mi west of the borough of Waynesburg (the Greene County seat) along Pennsylvania Route 18.  As of the 2010 census the population was 249.\n\nCentral State University: Central State University (CSU) is a historically black university (HBCU) located in Wilberforce, Ohio, United States.  It is a member-school of the Thurgood Marshall College Fund.\n\nWilberforce, Ohio: Wilberforce is a census-designated place (CDP) in Greene County, Ohio, United States.  The population was 2,271 at the 2010 census, up from 1,579 at the 2000 census.  The community was named for the English statesman William Wilberforce, who worked for the abolition of slavery and achieved the end of the slave trade in the United Kingdom and its empire.  The community is home to Wilberforce University and Central State University, two historically black universities.\n\nQuestion: What is the first name of the English statesman, who worked for the abolition of slavery, whose surname is now a census-designated place in Greene County, Ohio which is home to Central State University?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"statesman_first_name\": {\n      \"type\": \"string\",\n      \"description\": \"The first name of the statesman.\"\n    },\n    \"statesman_surname\": {\n      \"type\": \"string\",\n      \"description\": \"The surname of the statesman, which is also the name of the census-designated place.\"\n    },\n    \"cdp_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the census-designated place.\"\n        },\n        \"county\": {\n          \"type\": \"string\",\n          \"description\": \"The county where the CDP is located.\"\n        },\n        \"state\": {\n          \"type\": \"string\",\n          \"description\": \"The state where the CDP is located.\"\n        },\n        \"home_to_university\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the university located in the CDP.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"county\",\n        \"state\",\n        \"home_to_university\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"statesman_contribution\": {\n      \"type\": \"string\",\n      \"description\": \"A description of the statesman's work related to slavery abolition.\"\n    }\n  },\n  \"required\": [\n    \"statesman_first_name\",\n    \"statesman_surname\",\n    \"cdp_details\",\n    \"statesman_contribution\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "statesman_first_name": {
        "type": "string",
        "description": "The first name of the statesman."
      },
      "statesman_surname": {
        "type": "string",
        "description": "The surname of the statesman, which is also the name of the census-designated place."
      },
      "cdp_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the census-designated place."
          },
          "county": {
            "type": "string",
            "description": "The county where the CDP is located."
          },
          "state": {
            "type": "string",
            "description": "The state where the CDP is located."
          },
          "home_to_university": {
            "type": "string",
            "description": "The name of the university located in the CDP."
          }
        },
        "required": [
          "name",
          "county",
          "state",
          "home_to_university"
        ],
        "additionalProperties": false
      },
      "statesman_contribution": {
        "type": "string",
        "description": "A description of the statesman's work related to slavery abolition."
      }
    },
    "required": [
      "statesman_first_name",
      "statesman_surname",
      "cdp_details",
      "statesman_contribution"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
