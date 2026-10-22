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
Robert F. Overmyer: Robert Franklyn "Bob" Overmyer (July 14, 1936 – March 22, 1996), (Col, USMC), was an American test pilot, naval aviator, aeronautical engineer, physicist, United States Marine Corps officer, and USAF/NASA astronaut.  He was born in Lorain, Ohio, but considered Westlake, Ohio his hometown.  Overmyer was selected by the United States Air Force as an astronaut for its Manned Orbiting Laboratory in 1966.  Upon cancellation of this program in 1969, he became a NASA astronaut and served support crew duties for the Skylab program and Apollo-Soyuz Test Project.  In 1976, he was assigned to the Space Shuttle program, and flew as pilot on STS-5 in 1982, and as commander on STS-51-B in 1985.  He was selected as a lead investigator into the Space Shuttle "Challenger" disaster, and retired from NASA in 1986.  Ten years later, Overmyer died in Duluth, Minnesota while testing the Cirrus VK-30 composite homebuilt aircraft.

Theodore Freeman: Theodore Cordy "Ted" Freeman (February 18, 1930 – October 31, 1964), was an American aeronautical engineer, U.S. Air Force officer, test pilot, and NASA astronaut.  Selected in third group of NASA astronauts in 1963, he was killed a year later in the crash of a T-38 jet, marking the first fatality among the NASA Astronaut Corps.  At the time of his death, he held the rank of captain.

Alan Bean: Alan LaVern Bean (born March 15, 1932), (CAPT, USN, Ret.) , is an American former naval officer and Naval Aviator, aeronautical engineer, test pilot, and NASA astronaut; he was the fourth person to walk on the Moon.  He was selected to become an astronaut by NASA in 1963 as part of Astronaut Group 3.  He made his first flight into space aboard Apollo 12, the second manned mission to land on the Moon, at the age of thirty-seven years in November 1969.  He made his second and final flight into space on the Skylab 3 mission in 1973, the second manned mission to the Skylab space station.  After retiring from the United States Navy in 1975 and NASA in 1981, he pursued his interest in painting, depicting various space-related scenes and documenting his own experiences in space as well as that of his fellow Apollo program astronauts.

NASA Astronaut Group 5: NASA's Astronaut Group 5 was selected by NASA in April 1966.  Of the six Lunar Module Pilots that walked on the Moon, three came from Group 5.  The group as a whole is roughly split between the half who flew to the Moon (nine in all) and the other half who flew Skylab and Shuttle, providing the core of Shuttle Commanders early in that program.  This group is also distinctive in being the only time when NASA hired a person into the astronaut corps who had already earned astronaut wings, X-15 pilot Joe Engle.  John Young labelled the group the "Original Nineteen" in parody of the original seven Mercury astronauts.

European Astronaut Corps: The European Astronaut Corps is a unit of the European Space Agency (ESA) that selects, trains, and provides astronauts as crew members on U.S. and Russian space missions.  As of Nov 2014, 24 ESA astronauts are now able to go board the ISS.  There are currently 47 members of the Corps, 26 currently active.  The European Astronaut Corps is based at the European Astronaut Centre in Cologne, Germany.  They can be assigned to various projects both in Europe (at ESTEC, for instance) or elsewhere in the world, at NASA Johnson Space Center or Star City.

Joseph R. Tanner: Joseph Richard "Joe" Tanner (born January 21, 1950) is an American instructor at the University of Colorado Boulder, mechanical engineer, a former naval officer and aviator, and a former NASA astronaut.  He was born in Danville, Illinois.  He is unusual among astronauts as he did not have a background in flight test nor did he earn any advanced academic degrees.  Typically those who did not do military flight test have an M.D. or Ph.D., if not a master's, whereas Tanner's path to becoming an astronaut followed operational military flying and then into NASA for operational jet training before being selected into the NASA Astronaut Corps in 1992, following an unsuccessful application in 1987.

Joe Engle: Joe Henry Engle (born August 26, 1932), (Maj Gen, USAF, Ret.) , is an American pilot who served in the United States Air Force, test pilot for the North American X-15 program, aeronautical engineer, and a former NASA astronaut.  As of 2017, he is the last living pilot of the X-15 program.

Dante Ross: Dante Ross (born October 11, 1965 in San Francisco, California) is an American music industry executive, A&R representative, and producer.  He was named one of the top-25 greatest A&R representatives in hip hop by "Complex" magazine.  Ross started his A&R career at Tommy Boy records, at which he signed and handled the careers of such artists as De La Soul, Queen Latifah, and Digital Underground.  Ross was then hired by Elektra Records and was the first person ever hired by a major label to be specifically a hip hop A and R man.  Ross became the architect of Elektra Records hip hop roster where he signed acts Brand Nubian, Grand Puba, Pete Rock & C.L Smooth, KMD, Leaders of the New School, Busta Rhymes and Ol’ Dirty Bastard.  He is currently a SVP of A&R ADA Music the independent distribution company owned by the Warner Music Group.  He also serves as SVP of A and R for the newly re-activated Asylum records.

Luca Parmitano: Luca Parmitano (born 27 September 1976 in Paternò, Sicily) is an Italian engineer and astronaut in the European Astronaut Corps for the European Space Agency (ESA).  The astronauts work on missions at the International Space Station.  He was selected as an ESA astronaut in May 2009.

Riding Rockets: Riding Rockets: The Outrageous Tales of a Space Shuttle Astronaut is a 2006 book by retired astronaut Richard "Mike" Mullane.  The book describes Mullane's experiences in the NASA astronaut corps from 1978 to 1990, including his flights on the Space Shuttle and his personal relationships with other astronauts, including Judy Resnik, who perished in the "Challenger" accident.  The book gives a critical glimpse into the culture of NASA and the astronaut corps.

Question: What aeronautical engineer ,born in 1932, was the only  person ever hired into the astronaut corps who had already earned astronaut wings?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "astronaut_name": {
      "type": "string",
      "description": "The full name of the astronaut."
    },
    "birth_year": {
      "type": "integer",
      "description": "The year the astronaut was born."
    },
    "professions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of professions held by the astronaut."
    },
    "unique_distinction": {
      "type": "string",
      "description": "The specific unique achievement or characteristic of the astronaut related to their selection."
    },
    "nasa_astronaut_group": {
      "type": "string",
      "description": "The NASA Astronaut Group the individual was part of."
    }
  },
  "required": [
    "astronaut_name",
    "birth_year",
    "professions",
    "unique_distinction",
    "nasa_astronaut_group"
  ],
  "additionalProperties": false
}
