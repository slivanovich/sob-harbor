{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMichael J. Smith (astronaut): Michael John Smith (April 30, 1945 – January 28, 1986), (Capt, USN), was an American astronaut—pilot of the Space Shuttle \"Challenger\" when it was destroyed during the STS-51-L mission.  All seven crew members died.\n\nHyde railway disaster: The Hyde railway disaster occurred on 4 June 1943 near the small settlement of Hyde, New Zealand on a bend of the Otago Central Railway.  At the time, it was New Zealand's worst railway accident; of the 113 passengers on board, 21 were killed and a further 47 were injured.  But just over ten years later, the Tangiwai disaster took 151 lives on 24 December 1953.  The Hyde disaster remains as the second worst railway accident in New Zealand's history.\n\nTurkish Airlines Flight 278: Turkish Airlines Flight 278, operated by a Boeing 737-4Y0 registered TC-JES and named \"Mersin\", was a domestic scheduled flight from Ankara Esenboğa Airport to Van Ferit Melen Airport in eastern Turkey that crashed on 29 December 1994 during its final approach to land in driving snow.  Five of the seven crew and 52 of the 69 passengers lost their lives, while two crew members and 17 passengers survived with serious injuries.\n\nGeorge Symons (sailor): George Thomas Macdonald Symons (23 February 1888 – 3 December 1950) was a British sailor who worked as a lookout on board the ill-fated RMS \"Titanic\".  Symons, who was 24 at the time of the sinking of the ship, was put in charge of one of the first lifeboats to be launched, lifeboat #1.  The boat was an emergency cutter which was launched with only 12 people on board, including seven crew members, and had gained notoriety after the disaster.\n\n51827 Laurelclark: 51827 Laurelclark (2001 OH ) is an asteroid named for astronaut Laurel Clark, who was killed in the STS-107 (Columbia) space shuttle reentry disaster on February 1, 2003.  51827 Laurelclark was discovered on July 20, 2001 at Palomar Observatory by the JPL Near Earth Asteroid Tracking Program.\n\nSpace Shuttle Columbia disaster: On February 1, 2003, the Space Shuttle \"Columbia\" disintegrated upon reentering Earth's atmosphere, killing all seven crew members.\n\n1966 Palomares B-52 crash: The 1966 Palomares B-52 crash, or the Palomares incident, occurred on 17 January 1966, when a B-52G bomber of the United States Air Force's Strategic Air Command collided with a KC-135 tanker during mid-air refuelling at 31000 ft over the Mediterranean Sea, off the coast of Spain.  The KC-135 was completely destroyed when its fuel load ignited, killing all four crew members.  The B-52G broke apart, killing three of the seven crew members aboard.\n\nChallenger (1990 film): Challenger is a 1990 American disaster drama television film based on the events surrounding the Space Shuttle \"Challenger\" disaster.  Its production was somewhat controversial as the families of the astronauts generally objected to it.  The film concentrates on the safety inspections and arguments surrounding the O-rings that ultimately were blamed for the explosion of \"Challenger\".  While doing this, it also aims to show the personal humanity of the seven crew members.  Generally, the film supports the Space Shuttle program and the dedication of NASA personnel in general while criticizing NASA management.\n\nVisa requirements for crew members: Visa requirements for crew members are administrative entry restrictions imposed by the countries for the pilot or a member of the crew during a transit.  The crew visas are associated with the request for permission to enter a country for a short duration and perform the predefined duties in the given areas, distinct from actual formal permission for an alien to enter and remain in the country.  Validity of transit visas for crew members is usually limited by short terms such as several hours to 10 days depending on the size of the country and the circumstances.  The visa policy for crew members is set by the country and applies to during the transit or to join the vessel.  It is illegal for the crew members to perform repairs or similar work without work permits in port, or traveling in the waters.  By law, only a few countries that offer a visa waiver program or do not issue a crew visa, but allow their entry for a limited time with mandatory clearance documents.  Most of the countries permit crew members to travel within the Common Travel Area by carrying a passport or a national identity card.\n\nKalpana Chawla: Kalpana Chawla (March 17, 1962 – February 1, 2003) was an American astronaut and the first woman of Indian origin in space.  She first flew on Space Shuttle Columbia in 1997 as a mission specialist and primary robotic arm operator.  In 2003, Chawla was one of the seven crew members who died in the Space Shuttle \"Columbia\" disaster when the craft disintegrated during its re-entry into the Earth's atmosphere.  Chawla is a recipient of the Congressional Space Medal of Honor.\n\nQuestion: What 2003 disaster took the lives of seven crew members, including the astronaut for which asteroid 51827 Laurelclark is named for?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"disaster_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the disaster.\"\n    },\n    \"disaster_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the disaster occurred.\"\n    },\n    \"crew_fatalities_count\": {\n      \"type\": \"integer\",\n      \"description\": \"The total number of crew members who died in the disaster.\"\n    },\n    \"astronaut_honored_by_asteroid\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the astronaut for whom the asteroid is named.\"\n        },\n        \"asteroid_designation\": {\n          \"type\": \"string\",\n          \"description\": \"The designation of the asteroid named after the astronaut.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"asteroid_designation\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"disaster_name\",\n    \"disaster_year\",\n    \"crew_fatalities_count\",\n    \"astronaut_honored_by_asteroid\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "disaster_name": {
        "type": "string",
        "description": "The name of the disaster."
      },
      "disaster_year": {
        "type": "integer",
        "description": "The year the disaster occurred."
      },
      "crew_fatalities_count": {
        "type": "integer",
        "description": "The total number of crew members who died in the disaster."
      },
      "astronaut_honored_by_asteroid": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the astronaut for whom the asteroid is named."
          },
          "asteroid_designation": {
            "type": "string",
            "description": "The designation of the asteroid named after the astronaut."
          }
        },
        "required": [
          "name",
          "asteroid_designation"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "disaster_name",
      "disaster_year",
      "crew_fatalities_count",
      "astronaut_honored_by_asteroid"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
