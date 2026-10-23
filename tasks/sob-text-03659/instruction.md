{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSacred Heart Church (Phoenix, Arizona): Sacred Heart Church, or the Historic Sacred Heart Church, is an unoccupied church located at 16th St and Buckeye Roads, which was placed on the National Register of Historic Places by the US Department of Interior with the efforts of the Braun Sacred Heart Center Inc. in 2012.  The lot the Sacred Heart Church sits on is owned by the City of Phoenix, Aviation Department.  Sacred Heart Church was the pillar of the Golden Gate Barrio, and the Braun Sacred Heart Center Inc. has been hosting a yearly Christmas Day Mass at noon for former residents since 1987, with the permission of the City of Phoenix.\n\nCoda (film): Coda is a 1987 Australian horror thriller film directed by Craig Lahiff who described it as \"very much a telefilm.  I suppose it's very Hitchcocky - and de Palma inspired.\"  It was the first of three films Lahiff had arranged finance for which were made in succession.\n\nCraig Lahiff: Craig Lahiff (April 23, 1947 – 2 February 2014) was an Australian film director.  He grew up in the Adelaide suburb of Somerton Park and studied science at Adelaide University, then trained as a systems consultant before studying arts in film at Flinders University.  He began working in the film industry on crews for movies such as \"Sunday Too Far Away\" and \"The Fourth Wish\".\n\nCullinane College: Cullinane College is an integrated, Co-Educational Secondary school in Wanganui, New Zealand for students in Year 9 to Year 13.  Cullinane College was founded in 2003, through the combining of Sacred Heart College (founded in 1880 and operated by the Sisters of St Joseph of Nazareth) and St Augustines College (founded in 1944 and operated by the priests and brothers of the Society of Mary).  The college is named after: Sister Vincent Cullinane RSJ and Sister Cuthbert Cullinane RSJ (both important teachers at Sacred Heart College); Father John Cullinane SM (an important teacher at St Augustine's College); and Bishop Peter James Cullinane, first Bishop of Palmerston North (1980-2012).  The Bishop of Palmerston North is the proprietor of the college.\n\nSacred Heart Girls' College, New Plymouth: Sacred Heart Girls' College had its origins in a school and boarding facility called Sacred Heart College, founded by the Sisters of Our Lady of the Missions in 1884.  The school was next to the present St Joseph’s Church in New Plymouth and catered for primary & secondary students.  In 1960 the school moved to its present site and was renamed Sacred Heart Girls’ College.  The boarding hostel for up to 78 boarders, now called \"Elizabeth House\", was added in 1970.\n\nSomerton Park, South Australia: Somerton Park is a suburb of Adelaide in South Australia.  The mainly residential seaside suburb is home to the Somerton Park Beach, and also to Sacred Heart College.\n\nSacred Heart College, Sorrento: Sacred Heart College in Sorrento, Perth, Western Australia is a Co-Education, Catholic, Secondary School offering education to Years 7–12.  The College was founded in 1967 by the Sisters of Our Lady of the Missions who originally operated the school in many areas around the Perth Metropolitan area and certain country areas.  When founded, the College was a single sex school for girls.  As the need for education due to population growth in local areas, Sacred Heart accepted a group of boys into the College in 1977.  This school provided boarding opportunities and the land to the North was sold to local residents in order to fund further development of the school.  To this day, there is an enrolment of around 1400 students with a Year 7 enrolment of 238.  The College is situated on an 8-hectare prime piece of land overlooking both the Indian Ocean and Hillary's Boat Harbour.  Facilities include extensive playing fields, hard courts for many sports, a Performing Arts Centre, Science Labs, Computer Labs, Gymnasium and specialised rooms for Engineering, Wood and Art.\n\nStuart Hall for Boys: Stuart Hall for Boys is a private Roman Catholic school located in San Francisco, California, and is part of the Schools of the Sacred Heart network.  Founded in 1887 as an independent, Catholic school, Schools of the Sacred Heart San Francisco carry on the educational mission of the Religious of the Sacred Heart.  It is associated with Stuart Hall High School, Convent of the Sacred Heart Elementary School and Convent of the Sacred Heart High School.  The schools are fully accredited by the Western Association of Schools and Colleges, the California Association of Independent Schools and the Network of Sacred Heart Schools and receive no financial support from either the Roman Catholic Church or the Society of the Sacred Heart.\n\nSacred Heart University Luxembourg: Sacred Heart University Luxembourg, abbreviated to SHU Luxembourg, is a business school, based in Luxembourg City, in southern Luxembourg.  The complete name is Jack Welch College of Business, Sacred Heart University Luxembourg.  It is the European branch of the Jack Welch College of Business at Sacred Heart University, Fairfield, CT, located north of New York City.  Sacred Heart’s Jack Welch College of Business has been in Luxembourg for more than two decades offering graduate level programs tailored to the needs of working professionals.\n\nSacred Heart College (Lucena): Sacred Heart College is an educational institution in Lucena City, Quezon, Philippines.  The first catholic learning institution in Quezon Province, it was founded on April 27, 1884.  It had its roots in the vision of a simple and saintly woman named Hermana Fausta Labrador whose exemplary life was moulded on the Vincentian spirituality.  The school grew and its status was changed from Academy to College in 1941.  It was formally turned-over to the Daughters of Charity of Saint Vincent de Paul on August 14, 1937.  In 2009, Sacred Heart College celebrated its 125th founding anniversary.\n\nQuestion: Which Australian home of Sacred Heart College is also the childhood home of Craig Lahiff? \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"common_location\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the location that is both the childhood home of Craig Lahiff and the home of a Sacred Heart College.\"\n    },\n    \"location_country\": {\n      \"type\": \"string\",\n      \"description\": \"The country where the common location is situated.\"\n    },\n    \"craig_lahiff_info\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the person.\"\n        },\n        \"role\": {\n          \"type\": \"string\",\n          \"description\": \"The primary role or occupation of the person.\"\n        },\n        \"grew_up_in_this_location\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if this location was Craig Lahiff's childhood home.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"role\",\n        \"grew_up_in_this_location\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"sacred_heart_college_info\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the educational institution.\"\n        },\n        \"located_in_this_location\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if a Sacred Heart College is located in this common location.\"\n        },\n        \"location_type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of geographical area the college is in (e.g., suburb).\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"located_in_this_location\",\n        \"location_type\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"common_location\",\n    \"location_country\",\n    \"craig_lahiff_info\",\n    \"sacred_heart_college_info\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "common_location": {
        "type": "string",
        "description": "The name of the location that is both the childhood home of Craig Lahiff and the home of a Sacred Heart College."
      },
      "location_country": {
        "type": "string",
        "description": "The country where the common location is situated."
      },
      "craig_lahiff_info": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the person."
          },
          "role": {
            "type": "string",
            "description": "The primary role or occupation of the person."
          },
          "grew_up_in_this_location": {
            "type": "boolean",
            "description": "Indicates if this location was Craig Lahiff's childhood home."
          }
        },
        "required": [
          "name",
          "role",
          "grew_up_in_this_location"
        ],
        "additionalProperties": false
      },
      "sacred_heart_college_info": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the educational institution."
          },
          "located_in_this_location": {
            "type": "boolean",
            "description": "Indicates if a Sacred Heart College is located in this common location."
          },
          "location_type": {
            "type": "string",
            "description": "The type of geographical area the college is in (e.g., suburb)."
          }
        },
        "required": [
          "name",
          "located_in_this_location",
          "location_type"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "common_location",
      "location_country",
      "craig_lahiff_info",
      "sacred_heart_college_info"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
