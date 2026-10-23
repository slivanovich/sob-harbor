{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nFlight of Fear: Flight of Fear (previously known as The Outer Limits: Flight of Fear) is an enclosed launched roller coaster at two Cedar Fair parks, Kings Island in Mason, Ohio and Kings Dominion in Doswell, Virginia.  Both Flight of Fear roller coasters first opened in 1996 and were the world's first roller coasters to feature a linear induction motor (LIM) launch.  Flight of Fear has won three awards from the International Association of Amusement Parks and Attractions, including one for Major Theme/Amusement Park Ride/Attraction and two for Technology Applied to Amusements.\n\nHalloWeekends: HalloWeekends is an annual Halloween event at Cedar Point amusement park in Sandusky, Ohio.  It was introduced in 1997, and takes place during the Halloween season, usually from the second Friday after Labor Day until the Sunday before Halloween.  The event is open on Friday nights, Saturdays and Sundays.  It is included free with park admission.  As of 2014, HalloWeekends features 11 haunted houses and nighttime scare zones, and there are several children's attractions including a parade that takes place on the main midway.  It is advised that children under 13 years old be accompanied by an adult.  HalloWeekend's yearly slogan is \"All You Fear is Here!\" .  Other Cedar Fair parks including Dorney Park, Valley Fair, and Worlds of Fun all have formerly used the HalloWeekends name.  The name has changed to Halloween Haunt at all 3 parks.  Cedar Point is the only Cedar Fair park that still uses the HalloWeekends name.\n\nDominator (roller coaster): Dominator is a floorless roller coaster located at Kings Dominion in Doswell, Virginia.  Built by Bolliger & Mabillard, it originally opened as Batman: Knight Flight at Six Flags Ohio on May 5, 2000.  Cedar Fair Entertainment Company purchased the park in 2004 and renamed it Dominator.  Following the park's permanent closure in 2007, the roller coaster was relocated to Kings Dominion where it opened on May 24, 2008, in the International Street section of the park.\n\nDinosaurs Alive! (attraction): Dinosaurs Alive!  is an animatronic dinosaur themed area located at several Cedar Fair parks.  Kings Island was the first park to open the attraction in 2011, while the other parks opened their attraction in 2012 or 2013.  The version of this attraction at Kings Island is the world's largest animatronic dinosaur park.  A $5–6.00 fee is required in order to enter the attraction.  At Kings Island, Worlds of Fun, Carowinds and Kings Dominion, admission is free with a Gold or Platinum Pass.  Each park also features \"Dinostore\", a gift shop filled with dinosaur toys and souvenirs.\n\nWindSeeker: WindSeeker (known as SteelHawk at Worlds of Fun) is a 301 ft swing ride at several Cedar Fair parks.  The rides are Wind Seeker models manufactured by Mondial.  They opened for the 2011 season at Canada's Wonderland in Ontario, Cedar Point and Kings Island in Ohio, and Knott's Berry Farm in California.  Carowinds in North Carolina and Kings Dominion in Virginia opened their WindSeekers in 2012.  The first four each cost US$5,000,000, and the next two each cost $6,500,000.  Cedar Fair relocated the Knott's Berry Farm WindSeeker to Worlds of Fun in 2014, where it is known as SteelHawk.\n\nBoo Blasters on Boo Hill: Boo Blasters on Boo Hill is an interactive family dark ride designed and manufactured by Sally Corporation.  The ride is located at four Cedar Fair amusement parks — Canada's Wonderland, Carowinds, Kings Dominion, and Kings Island.  Originally themed to Hanna-Barbera's \"Scooby-Doo\", Cedar Fair rebranded the rides shortly after purchasing the parks from Paramount.  Each ride's new theme debuted in 2010 at all four parks.\n\nAction Theater: The Action Theater (spelled Action Theatre at Canada's Wonderland), is a motion simulator ride that debuted in 1993.  It is found at several Cedar Fair amusement parks including California's Great America, Canada's Wonderland, Carowinds, Kings Dominion, and Kings Island.  The attraction was previously known as \"Paramount Action F/X Theater\" before being renamed following the purchase of the Paramount Parks chain by Cedar Fair in 2006.\n\nXtreme Skyflyer: Xtreme Skyflyer (known as RipCord at Carowinds ) is a Skycoaster at several Cedar Fair parks.  The Carowinds and Kings Island models opened in 1995, while the Canada's Wonderland and Kings Dominion models opened in 1996 followed by California's Great America which opened their model in 1997.  In order to ride the attraction, guests must pay an extra fee.\n\nKings Dominion: Kings Dominion is an amusement park in Doswell, Virginia 20 mi north of Richmond and 75 mi south of Washington, D.C., off Interstate 95.\n\nThe Crypt (Kings Dominion): The Crypt (formerly Tomb Raider: Firefall) is a HUSS Park Attraction suspended Top Spin ride located at Kings Dominion in Doswell, Virginia.  The Crypt was also the name of a giant top spin at Kings Dominion's sister park, Kings Island (Kings Island's version closed on October 30, 2011 while the Kings Dominion version still operates).  Both rides were originally themed after the movie , until Kings Dominion, Kings Island, and the other three Paramount Parks were sold to the Cedar Fair Entertainment Company.\n\nQuestion: WindSeeker (known as SteelHawk at Worlds of Fun) is a 301 ft swing ride at several Cedar Fair parks, Kings Dominion in Virginia opened their WindSeeker in 2012, Kings Dominion is an amusement park, in Doswell, in which US state?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"park_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the amusement park.\"\n    },\n    \"park_location\": {\n      \"type\": \"string\",\n      \"description\": \"The city where the amusement park is located.\"\n    },\n    \"state\": {\n      \"type\": \"string\",\n      \"description\": \"The US state where the amusement park is located.\"\n    },\n    \"featured_ride\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"ride_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the ride mentioned in the question.\"\n        },\n        \"ride_type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of the ride.\"\n        },\n        \"height_ft\": {\n          \"type\": \"integer\",\n          \"description\": \"The height of the ride in feet.\"\n        },\n        \"opening_year_at_park\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the ride opened at this specific park.\"\n        }\n      },\n      \"required\": [\n        \"ride_name\",\n        \"ride_type\",\n        \"height_ft\",\n        \"opening_year_at_park\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"park_name\",\n    \"park_location\",\n    \"state\",\n    \"featured_ride\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "park_name": {
        "type": "string",
        "description": "The name of the amusement park."
      },
      "park_location": {
        "type": "string",
        "description": "The city where the amusement park is located."
      },
      "state": {
        "type": "string",
        "description": "The US state where the amusement park is located."
      },
      "featured_ride": {
        "type": "object",
        "properties": {
          "ride_name": {
            "type": "string",
            "description": "The name of the ride mentioned in the question."
          },
          "ride_type": {
            "type": "string",
            "description": "The type of the ride."
          },
          "height_ft": {
            "type": "integer",
            "description": "The height of the ride in feet."
          },
          "opening_year_at_park": {
            "type": "integer",
            "description": "The year the ride opened at this specific park."
          }
        },
        "required": [
          "ride_name",
          "ride_type",
          "height_ft",
          "opening_year_at_park"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "park_name",
      "park_location",
      "state",
      "featured_ride"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
