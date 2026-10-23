{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nHistoric Saint Louis Street Association: Incorporated in 1999, the Historic Saint Louis Street Association (HSSA) is a non-profit organization; the mission of which is to protect and preserve Historic Saint Louis Street and its community.  Located in Edwardsville, Illinois, Historic Saint Louis Street was placed on the National Register of Historic Places in 1983.  Saint Louis Street is a mile long National Historic District, which dates back to 1809.  It is a residential street with over 50 historic homes that are from the middle 18th Century to early 19th Century.\n\nSaint Louis University Ice Pavilion: The Saint Louis University Ice Pavilion is a proposed project by Saint Louis University to build an indoor ice and sports facility to be constructed in concert with another project already in progress, the Chaifetz Arena.  The university is planning to build an on-campus ice arena, to be named 'SLU Ice Pavilion.'  The facility will host youth, high school, college hockey as well as special events; it will have a seating capacity of 2,300, and offer four youth hockey locker rooms, Saint Louis University Locker rooms (D1 and D2), four Prep School Locker rooms, conditioning and weight room.  As well as common and quiet study lounges for students and private offices and two private suites to be used for special events and/or VIP use.  The Ice Pavilion will also offer activities such as public skating, figure skating clubs, speed skating clubs, intramural broomball, intramural hockey, curling clubs, and learn-to-skate opportunities for the students and faculty.  The plans for this new Ice Pavilion were in response to the need for a closer facility to the Saint Louis University campus.  The current facility in use, the Summit Center in Chesterfield, MO, is approximately 21 miles away from SLU's campus, with average crowd sizes of 250-400 in attendance.\n\nTheatre of Blood: Theatre of Blood (also known in the United States as Theater of Blood) is a 1973 horror film starring Vincent Price as vengeful actor Edward Lionheart and Diana Rigg as his daughter Edwina.  The cast includes distinguished actors Harry Andrews, Coral Browne, Robert Coote, Jack Hawkins, Ian Hendry, Michael Hordern, Arthur Lowe, Joan Hickson, Robert Morley, Milo O'Shea, Diana Dors and Dennis Price.  It was directed by Douglas Hickox.\n\nDave Garroway: David Cunningham \"Dave\" Garroway (July 13, 1913 – July 21, 1982) was an American television personality.  He was the founding host and anchor of NBC's \"Today\" from 1952 to 1961.  His easygoing and relaxing style belied a lifelong battle with depression.  Garroway has been honored for his contributions to radio and television with a star for each on the Hollywood Walk of Fame as well as the St. Louis Walk of Fame, the city where he spent part of his teenage years and early adulthood.\n\nWilliam B. Ittner: William Butts Ittner (September 4, 1864 – 1936) was an architect in St. Louis, Missouri.  He designed many school buildings in Missouri and other areas, was president of the St. Louis Chapter of the American Institute of Architects from 1893–95, was awarded an honorary degree by the University of Missouri in 1930, served as president of the Architectural League of America during 1903–04, and at the time of his death was president of the St. Louis Plaza Commission, a fellow and life member of the American Institute of Architects, and a thirty-third degree Mason.  He was described as the most influential man in school architecture in the United States and has a star on the St. Louis Walk of Fame.  He was appointed St. Louis School Board commissioner in 1897 and is said to have designed open buildings that featured \"natural lighting, inviting exteriors, and classrooms tailored to specific needs.\"\n\n1991 Saint Louis Billikens men's soccer team: The 1991 Saint Louis Billikens men's soccer team represented Saint Louis University during the 1991 NCAA Division I men's soccer season.  The Billikens played their first season in the now-defunct Great Midwest Conference, where they were the inaugural regular-season and tournament champions.  Saint Louis earned an automatic bid to the 1991 NCAA Division I Men's Soccer Tournament, where they had their best NCAA tournament appearance since 1974.  Saint Louis reached the College Cup before losing to the eventual national champions, Virginia.\n\nCathedral Basilica of Saint Louis (St. Louis): The Cathedral Basilica of Saint Louis, also known as the Saint Louis Cathedral, is a cathedral of the Roman Catholic Church located in the Central West End area of St. Louis, Missouri.  Completed in 1914, it is the mother church of the Archdiocese of St. Louis and the seat of its archbishop, currently Robert James Carlson.  The cathedral is named for Saint Louis and was designated a basilica by Pope John Paul II in 1997.\n\nSaint Louis College La Union: Saint Louis College (SLC) is a college in City of San Fernando, La Union, Philippines.  It was founded by the Congregatio Immaculati Cordis Mariae (CICM).  There are also sister schools of SLC, like Saint Louis University(SLU) in Baguio, University of Saint Louis Tuguegarao (USL) in Tuguegarao City, Saint Louis College of Cebu in Mandaue, Cebu, Saint Mary's University (Philippines) in Bayombong, Nueva Vizcaya, and Maryhill School of Theology in Quezon City.\n\nSaint Louis, Virginia: Saint Louis is an unincorporated community in southern Loudoun County, Virginia.  Saint Louis lies on Saint Louis Road (Virginia Secondary Route 611) and is an old African American community with many African Americans still living in it today.  Banneker Elementary School is located in Saint Louis.\n\nVincent Price: Vincent Leonard Price Jr. (May 27, 1911 – October 25, 1993) was an American actor, well known for his distinctive voice and performances in horror films.  His career spanned other genres, including film noir, drama, mystery, thriller, and comedy.  He appeared on stage, television, radio, and more than one hundred films.  He has two stars on the Hollywood Walk of Fame: one for motion pictures, and one for television.  Born and raised in the Saint Louis, Missouri, area, Price also has a star on the Saint Louis Walk of Fame.\n\nQuestion: What star of Theatre of Blood has a star on the Saint Louis Walk of Fame?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor.\"\n    },\n    \"movie_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the movie the actor starred in.\"\n        },\n        \"role\": {\n          \"type\": \"string\",\n          \"description\": \"The character played by the actor in the movie.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"role\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"walk_of_fame_honors\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"location\": {\n            \"type\": \"string\",\n            \"description\": \"The location of the Walk of Fame.\"\n          },\n          \"category\": {\n            \"type\": \"string\",\n            \"description\": \"The category of the star, if specified.\"\n          }\n        },\n        \"required\": [\n          \"location\"\n        ],\n        \"additionalProperties\": false\n      },\n      \"description\": \"A list of Walk of Fame honors received by the actor.\"\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"movie_details\",\n    \"walk_of_fame_honors\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The name of the actor."
      },
      "movie_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the movie the actor starred in."
          },
          "role": {
            "type": "string",
            "description": "The character played by the actor in the movie."
          }
        },
        "required": [
          "title",
          "role"
        ],
        "additionalProperties": false
      },
      "walk_of_fame_honors": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "The location of the Walk of Fame."
            },
            "category": {
              "type": "string",
              "description": "The category of the star, if specified."
            }
          },
          "required": [
            "location"
          ],
          "additionalProperties": false
        },
        "description": "A list of Walk of Fame honors received by the actor."
      }
    },
    "required": [
      "actor_name",
      "movie_details",
      "walk_of_fame_honors"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
