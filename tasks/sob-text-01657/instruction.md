{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nTennessee Valley Authority: The Tennessee Valley Authority (TVA) is a federally owned corporation in the United States created by congressional charter on May 18, 1933 to provide navigation, flood control, electricity generation, fertilizer manufacturing, and economic development to the Tennessee Valley, a region particularly affected by the Great Depression.  The enterprise was a result of the efforts of Senator George W. Norris of Nebraska.  TVA was envisioned not only as a provider, but also as a regional economic development agency that would use federal experts and electricity to rapidly modernize the region's economy and society.\n\nGeorge W. Norris House: Senator George William Norris House, also known as George W. Norris House, is a house built in 1899 in McCook, Nebraska.  It was a home of U.S. Senator George W. Norris.  It was designated a National Historic Landmark in 1967.\n\nNorris Lake (Tennessee): Norris Lake is a reservoir that is located in Anderson, Campbell, Claiborne, Grainger, and Union counties in Tennessee.  The lake was created by the Norris Dam at the Cove Creek Site on the Clinch River in 1936 by the TVA for flood control.  The dam was the first major project taken on by the TVA.  The lake, dam and the town of Norris, Tennessee are named after George W Norris, who was a United States senator from Nebraska and wrote the legislation that created the TVA.\n\nRock Creek Park: Rock Creek Park is a large urban park that bisects the Northwest quadrant of Washington, D.C.  The park was created by an Act of Congress in 1890, and today is administered by the National Park Service.  In addition to the park proper, the Rock Creek administrative unit of the National Park Service administers various other federally owned properties in the District of Columbia located to the north and west of the National Mall, including Meridian Hill Park on 16th Street, N.W., the Old Stone House in Georgetown, and certain of the Fort Circle Parks, a series of batteries and forts encircling the District of Columbia for its defense during the U.S. Civil War.\n\nMichael W. Jackson: Michael W. Jackson is an Alabama District Attorney was born in Fayetteville, Tennessee on November 18, 1963.  He received his undergraduate degree at Centre College (Danville, Kentucky) with a double major in Economics/Management and Government in 1985.  He received his Juris Doctor in 1988 from Florida State University College of Law.\n\nSylvester Commercial Historic District: Sylvester Commercial Historic District is a historic district in Sylvester, Georgia that was listed on the National Register of Historic Places (NRHP) in 1987.  It includes the Worth County Local Building which is separately NRHP-listed.  Its boundaries were increased in 2002 to include some federally owned property.  The expanded district included 65 contributing buildings and 16 noncontributing buildings.\n\nNorris–La Guardia Act: The Norris–La Guardia Act (also known as the Anti-Injunction Bill) is a 1932 United States federal law on US labor law.  It banned yellow-dog contracts, barred the federal courts from issuing injunctions against nonviolent labor disputes, and created a positive right of noninterference by employers against workers joining trade unions.  The common title comes from the names of the sponsors of the legislation: Senator George W. Norris of Nebraska and Representative Fiorello H. La Guardia of New York, both Republicans.\n\nNorris School District 160: School District #160 is a consolidated public school district located predominantly in Lancaster County but also extending into Gage County, Nebraska, United States.  It serves a number of small communities including Roca, Hickman, Firth, Cortland, Panama, Princeton, Holland, Cheney, and Rokeby.  The school district was founded on June 1, 1964, and was named in honor of Senator George William Norris, who represented the state of Nebraska in the United States Senate from 1913 to 1943.  The school district currently enrolls just under 2000 students in grades K-12.\n\nDowntown Florence Historic District: The Florence Downtown Historic District is a historic district in Florence, Alabama.  Florence was founded in 1818 by the Cypress Land Company, who counted among its trustees Creek War General John Coffee, future Governor of Alabama Thomas Bibb, early Huntsville settler LeRoy Pope, and future United States Senator and Supreme Court Justice John McKinley.  The company hired Italian surveyor Ferdinand Sannoner, who divided the land into over 400 lots and named the town after Florence, Italy.  The first Lauderdale County Courthouse was completed in 1822, and the oldest extant building in the district, the Gothic Revival First Presbyterian Church, was completed two years later.  Most of the early buildings was destroyed by a fire in 1866.  Development resumed in earnest in the 1880s as Florence's industrial economy developed with the addition of several cotton mills, and the Florence Wagon Works, among others.  Other booms occurred in the 1920s with the construction of Wilson Dam, the establishment of the Tennessee Valley Authority in the 1930s, and during World War II as metals and chemical plants were drawn to the area.\n\nNorris Dam: Norris Dam is a hydroelectric and flood control structure located on the Clinch River in Anderson County and Campbell County, Tennessee, United States.  Its construction in the mid-1930s was the first major project for the Tennessee Valley Authority, which had been created in 1933 to bring economic development to the region and control the rampant flooding that had long plagued the Tennessee Valley.  The dam was named in honor of Nebraska Senator George Norris (1861–1944), a longtime supporter of government-owned power in general, and supporter of TVA in particular.  The project infrastructure was listed on the National Register of Historic Places in 2016.\n\nQuestion: In which year wast the historic Alabama district that is home to the federally owned corporation pushed by the efforts of Senator George W. Norris founded?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"entity_founded\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the town or district that was founded.\"\n    },\n    \"founding_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the entity was founded.\"\n    },\n    \"location_state\": {\n      \"type\": \"string\",\n      \"description\": \"The U.S. state where the entity is located.\"\n    },\n    \"associated_corporation\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the federally owned corporation.\"\n        },\n        \"creation_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the corporation was created.\"\n        },\n        \"senator_who_pushed_for_creation\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"name\": {\n              \"type\": \"string\",\n              \"description\": \"The name of the senator who pushed for the corporation's creation.\"\n            },\n            \"state_represented\": {\n              \"type\": \"string\",\n              \"description\": \"The state the senator represented.\"\n            }\n          },\n          \"required\": [\n            \"name\",\n            \"state_represented\"\n          ],\n          \"additionalProperties\": false\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"creation_year\",\n        \"senator_who_pushed_for_creation\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"entity_founded\",\n    \"founding_year\",\n    \"location_state\",\n    \"associated_corporation\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "entity_founded": {
        "type": "string",
        "description": "The name of the town or district that was founded."
      },
      "founding_year": {
        "type": "integer",
        "description": "The year the entity was founded."
      },
      "location_state": {
        "type": "string",
        "description": "The U.S. state where the entity is located."
      },
      "associated_corporation": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the federally owned corporation."
          },
          "creation_year": {
            "type": "integer",
            "description": "The year the corporation was created."
          },
          "senator_who_pushed_for_creation": {
            "type": "object",
            "properties": {
              "name": {
                "type": "string",
                "description": "The name of the senator who pushed for the corporation's creation."
              },
              "state_represented": {
                "type": "string",
                "description": "The state the senator represented."
              }
            },
            "required": [
              "name",
              "state_represented"
            ],
            "additionalProperties": false
          }
        },
        "required": [
          "name",
          "creation_year",
          "senator_who_pushed_for_creation"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "entity_founded",
      "founding_year",
      "location_state",
      "associated_corporation"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
