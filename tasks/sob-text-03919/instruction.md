Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Ronald Evans (astronaut): Ronald Ellwin Evans Jr. (November 10, 1933 – April 7, 1990), (Capt, USN), was an American naval officer and aviator, electrical engineer, aeronautical engineer, and NASA astronaut, also one of only 24 people to have flown to the Moon.

Mackin (crater): Mackin is a feature on Earth's Moon, a crater in Taurus-Littrow valley.  Astronauts Eugene Cernan and Harrison Schmitt landed north of it in 1972, on the Apollo 17 mission, but did not visit it.

Roger B. Chaffee: Roger Bruce Chaffee ( , February 15, 1935 – January 27, 1967) was an American naval officer and naval aviator, aeronautical engineer, and NASA astronaut in the Apollo program.

Jon McBride: Jon Andrew McBride (born August 14, 1943), (Capt, USN, Ret.) , is a retired American naval officer and aviator, fighter pilot, test pilot, aeronautical engineer, and a former NASA astronaut.

John S. Bull: John Sumter Bull, Ph.D. (September 25, 1934 – August 11, 2008), (Lt Cmdr, USN), was an American naval officer and aviator, fighter pilot, test pilot, mechanical and aeronautical engineer, and NASA astronaut.

Neil Armstrong: Neil Alden Armstrong (August 5, 1930 – August 25, 2012) was an American astronaut, engineer, and the first person to walk on the Moon.  He was also an aerospace engineer, naval aviator, test pilot, and university professor.  Before becoming an astronaut, Armstrong was an officer in the U.S. Navy and served in the Korean War.  After the war, he earned his bachelor's degree at Purdue University and served as a test pilot at the National Advisory Committee for Aeronautics (NACA) High-Speed Flight Station, where he logged over 900 flights.  He later completed graduate studies at the University of Southern California.

Alan Bean: Alan LaVern Bean (born March 15, 1932), (CAPT, USN, Ret.) , is an American former naval officer and Naval Aviator, aeronautical engineer, test pilot, and NASA astronaut; he was the fourth person to walk on the Moon.  He was selected to become an astronaut by NASA in 1963 as part of Astronaut Group 3.  He made his first flight into space aboard Apollo 12, the second manned mission to land on the Moon, at the age of thirty-seven years in November 1969.  He made his second and final flight into space on the Skylab 3 mission in 1973, the second manned mission to the Skylab space station.  After retiring from the United States Navy in 1975 and NASA in 1981, he pursued his interest in painting, depicting various space-related scenes and documenting his own experiences in space as well as that of his fellow Apollo program astronauts.

Eugene Cernan: Eugene Andrew Cernan ( ; March 14, 1934 – January 16, 2017) was an American astronaut, naval aviator, electrical engineer, aeronautical engineer, and fighter pilot.  On Apollo 17, Cernan became the eleventh person to walk on the Moon and, as the last man to re-enter the Lunar Module, he is as of 2017 the last man to have walked on its surface.

Gregory R. Wiseman: Gregory Reid Wiseman (born November 11, 1975) is an American astronaut, engineer, and naval aviator.  Wiseman was selected in June 2009 as a member of the NASA Astronaut Group 20 and qualified as an astronaut in 2011.  Wiseman took part in his first spaceflight as part of the crew of Expedition 40/41, which launched to the International Space Station on May 28, 2014, and returned on November 10, 2014.  Before joining NASA, Wiseman was a Naval Aviator and test pilot.

Robert F. Overmyer: Robert Franklyn "Bob" Overmyer (July 14, 1936 – March 22, 1996), (Col, USMC), was an American test pilot, naval aviator, aeronautical engineer, physicist, United States Marine Corps officer, and USAF/NASA astronaut.  He was born in Lorain, Ohio, but considered Westlake, Ohio his hometown.  Overmyer was selected by the United States Air Force as an astronaut for its Manned Orbiting Laboratory in 1966.  Upon cancellation of this program in 1969, he became a NASA astronaut and served support crew duties for the Skylab program and Apollo-Soyuz Test Project.  In 1976, he was assigned to the Space Shuttle program, and flew as pilot on STS-5 in 1982, and as commander on STS-51-B in 1985.  He was selected as a lead investigator into the Space Shuttle "Challenger" disaster, and retired from NASA in 1986.  Ten years later, Overmyer died in Duluth, Minnesota while testing the Cirrus VK-30 composite homebuilt aircraft.

Question: Which American astronaut, naval aviator, electrical engineer, aeronautical engineer, and fighter pilot landed north of Mackin?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "astronaut_name": {
      "type": "string",
      "description": "The full name of the astronaut."
    },
    "professions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of the astronaut's professions."
    },
    "mission_details": {
      "type": "object",
      "properties": {
        "mission_name": {
          "type": "string",
          "description": "The name of the mission during which the landing occurred."
        },
        "landing_location_relative_to_mackin": {
          "type": "string",
          "description": "Description of the landing location relative to the Mackin crater."
        },
        "year_of_landing": {
          "type": "integer",
          "description": "The year the landing occurred."
        }
      },
      "required": [
        "mission_name",
        "landing_location_relative_to_mackin",
        "year_of_landing"
      ],
      "additionalProperties": false
    },
    "walked_on_moon": {
      "type": "boolean",
      "description": "Indicates if the astronaut walked on the Moon."
    }
  },
  "required": [
    "astronaut_name",
    "professions",
    "mission_details",
    "walked_on_moon"
  ],
  "additionalProperties": false
}
