{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSwing ride: The swing ride or chair swing ride (sometimes called a swing carousel, wave swinger, yo-yo, Chair-O-Planes or swinger) is a fairground ride that is a variation on the carousel in which the chairs are suspended from the rotating top of the carousel.  On some versions, particularly on the Wave Swingers, the rotating top of the carousel also tilts for additional variations of motion.\n\nLinus' Launcher: Linus' Launcher is an amusement ride that is a variation on a swing ride.  The ride is meant to simulate flight.  The ride is themed to Peanuts and is located in the kid's area of the parks.  Linus' Launcher is located at three different Cedar Fair parks.\n\nAir Jumbo: Air Jumbo (formerly Jumbo) is a Telecombat-style ride located in the Adventure Alley themed section of Six Flags Great Adventure in Jackson, New Jersey.  The attraction opened to the public on May 23, 2012, along with three other attractions including SkyScreamer.\n\nRanger (ride): A Ranger is an inverting pendulum ride first manufactured by HUSS Machinenfabrik in 1981.  Many of the design elements were later used in the HUSS Rainbow, and the term 'Ranger' has become synonymous with inverting pendulum rides.  It was the first inverting swing ride designed since Lee Eyerly's Loop-O-Plane and set the standard for many other attractions using the inverting pendulum ride system, such as the Rainbow, the Kamikaze (ride), and the Inverter.\n\nWindSeeker: WindSeeker (known as SteelHawk at Worlds of Fun) is a 301 ft swing ride at several Cedar Fair parks.  The rides are Wind Seeker models manufactured by Mondial.  They opened for the 2011 season at Canada's Wonderland in Ontario, Cedar Point and Kings Island in Ohio, and Knott's Berry Farm in California.  Carowinds in North Carolina and Kings Dominion in Virginia opened their WindSeekers in 2012.  The first four each cost US$5,000,000, and the next two each cost $6,500,000.  Cedar Fair relocated the Knott's Berry Farm WindSeeker to Worlds of Fun in 2014, where it is known as SteelHawk.\n\nSkyScreamer: SkyScreamer is an amusement ride located at several Six Flags theme parks in North America.  Designed by Funtime, an Australian ride manufacturer, the attraction is one of their \"Star Flyer\" models.  Since 2011, Six Flags has installed SkyScreamers in nine of their parks.\n\nAdventure Alley: Adventure Alley is one of several \"themed sections\" and is exclusive to the Six Flags Great Adventure in Jackson, New Jersey, open on April 5, 2012.  One of the most popular attractions in the Adventure Alley, \"Big Wheel\" that was originally opened in 1974 and SkyScreamer, an 242 ft Swing ride that opened in 2012.\n\nRush (Thorpe Park): Rush is a giant swing ride at Thorpe Park in Chertsey, Surrey which opened at the park alongside another S&S Power thrill ride, Slammer, in 2005.  At this time it was the tallest ride of its type in the world.  Smoke can be seen at the top of the ride's canisters.\n\nDelirium (ride): Delirium is a Giant Frisbee ride located at Kings Island in Mason, Ohio.  Designed by HUSS Park Attractions, the ride first opened on April 12, 2003, as the largest Frisbee ride of its kind in the world.  The record-setting ride is able to swing 50 passengers up to 76 mph reaching a height of 137 ft above ground.\n\nTower 270: Tower 270 (also known as 270 Broadway, Arthur Levitt State Office Building, 80 Chambers Street, and 86 Chambers Street) is a 28-story mixed use building in Civic Center, New York City having 350785 sqft of floor space on a plot with 50 ft facing Broadway and 242 ft on Chambers Street.\n\nQuestion: Who designed a 242 ft Swing ride located in Adventure Alley?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"ride_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the ride.\"\n        },\n        \"type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of the ride.\"\n        },\n        \"height_ft\": {\n          \"type\": \"integer\",\n          \"description\": \"The height of the ride in feet.\"\n        },\n        \"location\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"themed_section\": {\n              \"type\": \"string\",\n              \"description\": \"The themed section where the ride is located.\"\n            },\n            \"park_name\": {\n              \"type\": \"string\",\n              \"description\": \"The name of the amusement park.\"\n            },\n            \"park_city\": {\n              \"type\": \"string\",\n              \"description\": \"The city where the park is located.\"\n            },\n            \"park_state\": {\n              \"type\": \"string\",\n              \"description\": \"The state where the park is located.\"\n            }\n          },\n          \"required\": [\n            \"themed_section\",\n            \"park_name\",\n            \"park_city\",\n            \"park_state\"\n          ],\n          \"additionalProperties\": false\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"type\",\n        \"height_ft\",\n        \"location\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"designer_info\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the ride designer.\"\n        },\n        \"country_of_origin\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the designer is from.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"country_of_origin\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"final_answer\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the designer of the specified ride.\"\n    }\n  },\n  \"required\": [\n    \"ride_details\",\n    \"designer_info\",\n    \"final_answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "ride_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the ride."
          },
          "type": {
            "type": "string",
            "description": "The type of the ride."
          },
          "height_ft": {
            "type": "integer",
            "description": "The height of the ride in feet."
          },
          "location": {
            "type": "object",
            "properties": {
              "themed_section": {
                "type": "string",
                "description": "The themed section where the ride is located."
              },
              "park_name": {
                "type": "string",
                "description": "The name of the amusement park."
              },
              "park_city": {
                "type": "string",
                "description": "The city where the park is located."
              },
              "park_state": {
                "type": "string",
                "description": "The state where the park is located."
              }
            },
            "required": [
              "themed_section",
              "park_name",
              "park_city",
              "park_state"
            ],
            "additionalProperties": false
          }
        },
        "required": [
          "name",
          "type",
          "height_ft",
          "location"
        ],
        "additionalProperties": false
      },
      "designer_info": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the ride designer."
          },
          "country_of_origin": {
            "type": "string",
            "description": "The country where the designer is from."
          }
        },
        "required": [
          "name",
          "country_of_origin"
        ],
        "additionalProperties": false
      },
      "final_answer": {
        "type": "string",
        "description": "The name of the designer of the specified ride."
      }
    },
    "required": [
      "ride_details",
      "designer_info",
      "final_answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
