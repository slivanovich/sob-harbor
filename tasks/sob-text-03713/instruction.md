{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMercury 13: Mercury 13 refers to thirteen American women who, as part of a privately funded program, underwent some of the same physiological screening tests as the astronauts selected by NASA on April 9, 1959 for Project Mercury.  The term was coined in 1995 by Hollywood producer James Cross as a comparison to the Mercury Seven name given to the selected male astronauts; however, the Mercury 13 were not part of NASA's astronaut program, never flew in space and never met as a group.\n\nProject Mercury: Project Mercury was the first human spaceflight program of the United States, running from 1958 through 1963.  An early highlight of the Space Race, its goal was to put a man into Earth orbit and return him safely, ideally before the Soviet Union.  Taken over from the U.S. Air Force by the newly created civilian space agency NASA, it conducted twenty unmanned developmental flights (some using animals), and six successful flights by astronauts.  The program, which took its name from Roman mythology, cost $277 million in 1965 US dollars, and involved the work of 2 million people.  The astronauts were collectively known as the \"Mercury Seven\", and each spacecraft was given a name ending with a \"7\" by its pilot.\n\nSoyuz 18: Soyuz 18 (Russian: Союз 18 , \"Union 18\") was a 1975 Soviet manned mission to Salyut 4, the second and final crew to man the space station.  Pyotr Klimuk and Vitali Sevastyanov set a new Soviet space endurance record of 63 days and the mark for most people in space simultaneously (seven) was tied during the mission.\n\nGordon Cooper: Leroy Gordon \"Gordo\" Cooper Jr. (March 6, 1927 – October 4, 2004), (Col, USAF), better known as Gordon Cooper, was an American aerospace engineer, test pilot, United States Air Force pilot, and one of the seven original astronauts in Project Mercury, the first manned space program of the United States.\n\nPete Conrad: Charles \"Pete\" Conrad Jr. (June 2, 1930 – July 8, 1999), (Captain, USN), was an American NASA astronaut, naval officer and aviator, test pilot, and during the Apollo 12 mission became the third man to walk on the Moon.  He set an eight-day space endurance record along with his Command Pilot Gordon Cooper on the Gemini 5 mission, and commanded the Gemini 11 mission.  After Apollo, he commanded the Skylab 2 mission (the first manned one), on which he and his crewmates repaired significant launch damage to the Skylab space station.  For this, President Jimmy Carter awarded him the Congressional Space Medal of Honor in 1978.\n\nThe Right Stuff (book): The Right Stuff is a 1979 book by Tom Wolfe about the pilots engaged in U.S. postwar research with experimental rocket-powered, high-speed aircraft as well as documenting the stories of the first Project Mercury astronauts selected for the NASA space program.  \"The Right Stuff\" is based on extensive research by Wolfe, who interviewed test pilots, the astronauts and their wives, among others.  The story contrasts the \"Mercury Seven\" and their families with test pilots such as Chuck Yeager, who was considered by many contemporaries as the best of them all, but who was never selected as an astronaut.\n\nModular Equipment Transporter: The Modular Equipment Transporter (MET) was a two-wheeled, hand-pulled vehicle that was used as an equipment hauling device on traverses across the lunar surface.  Designed after Apollo 12 astronauts Pete Conrad and Alan Bean had difficulties lugging their equipment significant distances to and from their Lunar Module, the MET primarily functioned as a portable workbench with a place for hand tools and their carrier, cameras, spare camera magazines, rock sample bags, environmental sample containers, and the portable magnetometer with its sensor and tripod.  It was carried on Apollo 14 and planned to be used on Apollo 15, but was used only on Apollo 14, since Apollo 15's mission was changed to be the first to employ the motorized Lunar Roving Vehicle, which transported both astronauts and equipment.\n\nSoyuz 9: Soyuz 9 (Russian: Союз 9 , \"Union 9\") was a 1970 Soviet manned space flight.  The two-man crew of Andrian Nikolayev and Vitali Sevastyanov broke the five-year-old space endurance record held by Gemini 7, with their nearly 18-day flight.  The mission paved the way for the Salyut space station missions, investigating the effects of long-term weightlessness on crew, and evaluating the work that the cosmonauts could do in orbit, individually and as a team.  It was also the last flight of the first-generation Soyuz 7K-OK spacecraft, as well as the first manned space launch to be conducted at night.  To date, Soyuz 9 marks the longest manned flight by a solo spacecraft.\n\nWally Schirra: Walter Marty \"Wally\" Schirra Jr. (March 12, 1923 – May 3, 2007), (CAPT, USN), was an American naval officer and aviator, aeronautical engineer, test pilot, and one of the original seven astronauts chosen for Project Mercury, United States first effort to put humans in space.  He flew the six-orbit, nine-hour Mercury-Atlas 8 mission on October 3, 1962, becoming the fifth American, and the ninth human, to ride a rocket into space.  In the two-man Gemini program, he achieved the first space rendezvous, station-keeping his Gemini 6A spacecraft within 1 ft of the sister Gemini 7 spacecraft in December 1965.  In October 1968, he commanded Apollo 7, an 11-day low Earth orbit shakedown test of the three-man Apollo Command/Service Module.  He was the first person to go into space three times, and the only person to have flown in Mercury, Gemini, and Apollo, logging a total of 295 hours and 15 minutes in space.  He retired from the U.S. Navy at the rank of Captain and from NASA after his Apollo flight, becoming a consultant to CBS News for its coverage of the subsequent Apollo flights.  He joined Walter Cronkite as co-anchor for the seven Moon landing missions.\n\nMercury Seven: The Mercury Seven were the group of seven Mercury astronauts announced by NASA on April 9, 1959.  They are also referred to as the Original Seven or Astronaut Group 1.  They piloted the manned spaceflights of the Mercury program from May 1961 to May 1963.  These seven original American astronauts were Scott Carpenter, Gordon Cooper, John Glenn, Gus Grissom, Wally Schirra, Alan Shepard, and Deke Slayton.\n\nQuestion: Who was one of the seven original astronauts in Project Mercury and also set an eight-day space endurance record along with Pete Conrad?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"astronaut_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the astronaut who meets the criteria.\"\n    },\n    \"project_mercury_status\": {\n      \"type\": \"string\",\n      \"description\": \"Description of the astronaut's involvement with Project Mercury.\"\n    },\n    \"endurance_record_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"mission_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the mission during which the endurance record was set.\"\n        },\n        \"duration_days\": {\n          \"type\": \"integer\",\n          \"description\": \"The duration of the space endurance record in days.\"\n        },\n        \"co_pilot_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the astronaut who shared the endurance record.\"\n        }\n      },\n      \"required\": [\n        \"mission_name\",\n        \"duration_days\",\n        \"co_pilot_name\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"astronaut_name\",\n    \"project_mercury_status\",\n    \"endurance_record_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "astronaut_name": {
        "type": "string",
        "description": "The name of the astronaut who meets the criteria."
      },
      "project_mercury_status": {
        "type": "string",
        "description": "Description of the astronaut's involvement with Project Mercury."
      },
      "endurance_record_details": {
        "type": "object",
        "properties": {
          "mission_name": {
            "type": "string",
            "description": "The name of the mission during which the endurance record was set."
          },
          "duration_days": {
            "type": "integer",
            "description": "The duration of the space endurance record in days."
          },
          "co_pilot_name": {
            "type": "string",
            "description": "The name of the astronaut who shared the endurance record."
          }
        },
        "required": [
          "mission_name",
          "duration_days",
          "co_pilot_name"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "astronaut_name",
      "project_mercury_status",
      "endurance_record_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
