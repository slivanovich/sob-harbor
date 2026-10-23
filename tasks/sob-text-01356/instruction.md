{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSlowdown (venue): Slowdown is an entertainment venue located at 729 North 14 Street in NoDo, a new development near the Near North Side neighborhood in Omaha, Nebraska.  A combination of a live music venue, shops, restaurants and apartments, the venue was developed by Saddle Creek Records as a direct competitor to the Sokol Auditorium in Little Bohemia.  Slowdown is said to be \"unlike anything in Omaha - or the Midwest\" because of its comprehensive, mixed-use design.  The venue is named after the group Slowdown Virginia (later renamed Cursive (band)), who have had a strong influence on \"The Omaha Sound\".  Slowdown has shows 3 to 4 nights per week as well as a weekly pub quiz.  The venue is open one hour before the event and stays open until around 2am, often offering a post-show Happy Hour.  Slowdown's shows are usually all ages unless otherwise specified, but on nights there is not an event the venue functions as a bar.  Slowdown is a place full of, \"Rock shows, socializing, dancing, going to the bathroom, sitting, standing, walking, pool, video games, board games, some light reading, etc.\"\n\nMargaret Court Arena: Margaret Court Arena is an Australian tennis and multi-purpose sports and entertainment venue located in Melbourne, Victoria.  The arena, which was built in 1987, has a capacity of 7,500.  The venue is part of the National Tennis Centre at Melbourne Park, which is part of the Melbourne Sports and Entertainment Precinct (MSEP).\n\nGranville Theatre, Ramsgate: The Granville Theatre complex is located in Victoria Parade, Ramsgate, Kent, and is the town's sole multi-purpose entertainment venue.  The theatre derived its name from the Granville Hotel, Ramsgate opposite.  The building is currently leased from Thanet District Council.\n\nMareel: Mareel is a multi-purpose entertainment venue located on the waterfront of Lerwick, the capital of Shetland.  Opening in 2012, the facility includes a music venue, cinema, conference rooms and educational facilities.\n\nBig Top Sydney: The Big Top (also known as the Big Top Auditorium and The Arena; commonly known as Big Top Sydney) is a multi-purpose entertainment venue located within Luna Park Sydney.  Opening in 2004, the venue was a part of the amusement park’s 2003 redevelopment plan.  It has a capacity of nearly 3,000, making it one of Sydney’s largest mid-sized venues.\n\nLuna Park Sydney: Luna Park Sydney (originally Luna Park Milsons Point, also known as Sydney's Luna Park) is an amusement park located in Sydney, New South Wales, Australia.  Luna Park is located at Milsons Point, on the northern shore of Sydney Harbour.\n\nKardinia Park (stadium): Kardinia Park (also known as Simonds Stadium due to naming rights) is a sporting and entertainment venue located within Kardinia Park, South Geelong, Victoria.  The stadium, which is owned and operated by the Kardinia Park Stadium Trust, is the home ground of the Geelong Football Club.  The capacity of Kardinia Park is 34,000, making it the largest capacity Australian stadium in a regional city (i.e., outside of a capital city).\n\nMeridian Park (Cleethorpes): Meridian Park is a multi-purpose entertainment venue in Cleethorpes, North East Lincolnshire, United Kingdom.  It hosted its first event organised by Solid Entertainments of Grimsby featuring The Zutons and The Proclaimers in August 2009 as part of the Cleethorpes Rocks Music Festival.\n\nThe Colosseum at Caesars Palace: The Colosseum at Caesars Palace is a theatre located on the Las Vegas Strip in Las Vegas, Nevada.  The theatre is the main entertainment venue for Caesars Palace.  Deemed the \"Home of the Greatest Entertainers in the World\", the theatre hosts numerous residency shows by Celine Dion, Elton John, Rod Stewart, Cher, Bette Midler, Shania Twain, and Mariah Carey.  Celine Dion has had the longest residency(1,110 shows as of June 2, 2018) at the venue grossing a total of $650 million since her arrival in 2003.  She also performed her record-breaking 1000th show at the venue on October 8, 2016.  The venue has an estimated seating capacity of 4,296 and is inspired by the architecture of ancient Rome along with aspects of contemporary architecture.  The cost of the theatre totaled $108 million, becoming the most expensive entertainment venue in Las Vegas, beating the \"O\" Theatre at the Bellagio Las Vegas.\n\nUptown Theater (Napa, California): The Uptown Theater is an entertainment venue located in Napa, California.  The theater is in an Art Deco style building which originally opened to the public in 1937.  It is currently utilized as a concert and entertainment venue with a seating capacity of 863.\n\nQuestion:  The Big Top is a multi-purpose entertainment venue located within a park on the northern shor of what harbour?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"venue_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the entertainment venue.\"\n        },\n        \"located_within_park\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the park where the venue is located.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"located_within_park\"\n      ]\n    },\n    \"park_location\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"shore_direction\": {\n          \"type\": \"string\",\n          \"description\": \"The direction of the shore where the park is located.\"\n        },\n        \"harbour_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the harbour.\"\n        }\n      },\n      \"required\": [\n        \"shore_direction\",\n        \"harbour_name\"\n      ]\n    },\n    \"final_answer\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the harbour.\"\n    }\n  },\n  \"required\": [\n    \"venue_details\",\n    \"park_location\",\n    \"final_answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "venue_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the entertainment venue."
          },
          "located_within_park": {
            "type": "string",
            "description": "The name of the park where the venue is located."
          }
        },
        "required": [
          "name",
          "located_within_park"
        ]
      },
      "park_location": {
        "type": "object",
        "properties": {
          "shore_direction": {
            "type": "string",
            "description": "The direction of the shore where the park is located."
          },
          "harbour_name": {
            "type": "string",
            "description": "The name of the harbour."
          }
        },
        "required": [
          "shore_direction",
          "harbour_name"
        ]
      },
      "final_answer": {
        "type": "string",
        "description": "The name of the harbour."
      }
    },
    "required": [
      "venue_details",
      "park_location",
      "final_answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
