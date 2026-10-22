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
Christa McAuliffe: Sharon Christa McAuliffe (September 2, 1948 – January 28, 1986) was an American teacher from Concord, New Hampshire, and was one of the seven crew members killed in the Space Shuttle "Challenger" disaster.

STS-51-L: STS-51-L was the 25th flight of the American Space Shuttle program, and disastrous final mission of the Space Shuttle "Challenger", which lifted-off from Launch Complex 39-B, at the Kennedy Space Center in Florida, on January 28, 1986.  The mission ended in catastrophic failure with the destruction of "Challenger", starting at 73 seconds after lift-off, and the death of all seven crew members.  The Rogers Commission determined that the cause of the destruction was due to the failure of an O-ring seal on the starboard Solid Rocket Booster (SRB).

Alvin Drew: Colonel Benjamin Alvin Drew (born November 5, 1962) is a United States Air Force officer and a NASA astronaut.  He has been on two spaceflights; the first was the Space Shuttle mission STS-118 to the International Space Station, in August 2007.  Drew's second spaceflight took place in March 2011 on STS-133, another mission to the International Space Station.  STS-133 was Space Shuttle "Discovery"'s final mission.  Drew took part in two spacewalks while docked to the station.  Drew was the final African-American to fly on board a Space Shuttle, as the final two Space Shuttle missions, STS-134 and STS-135, had no African-American crew members.

STS-61-C: STS-61-C was the twenty-fourth mission of NASA's Space Shuttle program, and the seventh mission of Space Shuttle "Columbia".  It was the first time that "Columbia", the first operational orbiter to be constructed, had flown since STS-9.  The mission launched from Florida's Kennedy Space Center on 12 January 1986, and landed six days later on 18 January.  STS-61-C's seven-person crew included the second African-American shuttle pilot, future NASA Administrator Charles Bolden, the first Costa Rican-born astronaut, Franklin Chang-Diaz, and the second sitting politician to fly in space, Representative Bill Nelson (D-FL).  It was the last shuttle mission before the Space Shuttle "Challenger" disaster, which occurred just ten days after STS-61-C's landing.

Kalpana Chawla: Kalpana Chawla (March 17, 1962 – February 1, 2003) was an American astronaut and the first woman of Indian origin in space.  She first flew on Space Shuttle Columbia in 1997 as a mission specialist and primary robotic arm operator.  In 2003, Chawla was one of the seven crew members who died in the Space Shuttle "Columbia" disaster when the craft disintegrated during its re-entry into the Earth's atmosphere.  Chawla is a recipient of the Congressional Space Medal of Honor.

Challenger (1990 film): Challenger is a 1990 American disaster drama television film based on the events surrounding the Space Shuttle "Challenger" disaster.  Its production was somewhat controversial as the families of the astronauts generally objected to it.  The film concentrates on the safety inspections and arguments surrounding the O-rings that ultimately were blamed for the explosion of "Challenger".  While doing this, it also aims to show the personal humanity of the seven crew members.  Generally, the film supports the Space Shuttle program and the dedication of NASA personnel in general while criticizing NASA management.

Space Shuttle Columbia: Space Shuttle "Columbia" (Orbiter Vehicle Designation: OV-102) was the first space-rated orbiter in NASA's Space Shuttle fleet.  It launched for the first time on mission STS-1 on April 12, 1981, the first flight of the Space Shuttle program.  Over 22 years of service it completed 27 missions before disintegrating during re-entry near the end of its 28th mission, STS-107 on February 1, 2003, resulting in the deaths of all seven crew members.

Space Shuttle Challenger: Space Shuttle "Challenger" (Orbiter Vehicle Designation: OV-099) was the second orbiter of NASA's space shuttle program to be put into service following "Columbia".  The shuttle was built by Rockwell International's Space Transportation Systems Division in Downey, California.  Its maiden flight, STS-6, started on April 4, 1983.  It launched and landed nine times before breaking apart 73 seconds into its tenth mission, STS-51-L, on January 28, 1986, resulting in the death of all seven crew members, including a civilian school teacher.  It was the first of two shuttles to be destroyed in flight, the other being "Columbia" in 2003.  The accident led to a two-and-a-half year grounding of the shuttle fleet; flights resumed in 1988 with STS-26 flown by "Discovery".  "Challenger" itself was replaced by "Endeavour" which was built using structural spares ordered by NASA as part of the construction contracts for "Discovery" and "Atlantis".

STS-26: STS-26 was the 26th NASA Space Shuttle mission and the seventh flight of the orbiter "Discovery".  The mission launched from Kennedy Space Center, Florida, on 29 September 1988, and landed four days later on 3 October.  STS-26 was declared the "Return to Flight" mission, being the first mission after the Space Shuttle "Challenger" disaster of 28 January 1986.  It was the first mission since STS-9 to use the original STS numbering system, the first to have all its crew members wear pressure suits for launch and landing since STS-4, and the first mission with bailout capacity since STS-4.  STS-26 was also the first all-veteran crew mission since Apollo 11, with all of its crew members having flown at least one prior mission.

Educator Astronaut Project: The Educator Astronaut Project is a NASA program designed to educate students and spur excitement in math,science, and space exploration.  It is a successor to the Teacher in Space Project of the 1980s that was cancelled after Christa McAuliffe died in the Space Shuttle "Challenger" disaster (STS-51-L).  NASA halted the teachers project amid concerns surrounding the risk of sending civilians to space.

Question: Who as one of the seven crew members killed in the Space Shuttle "Challenger" disaster, who's death lead to the cancellation of the Teacher in Space Project ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The full name of the person."
    },
    "person_role": {
      "type": "string",
      "description": "The primary role or profession of the person."
    },
    "disaster_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the space shuttle disaster."
        },
        "mission_identifier": {
          "type": "string",
          "description": "The mission designation of the disaster."
        },
        "date": {
          "type": "string",
          "description": "The date the disaster occurred."
        },
        "crew_fatalities_count": {
          "type": "integer",
          "description": "The total number of crew members killed in the disaster."
        }
      },
      "required": [
        "name",
        "mission_identifier",
        "date",
        "crew_fatalities_count"
      ],
      "additionalProperties": false
    },
    "project_affected": {
      "type": "object",
      "properties": {
        "project_name": {
          "type": "string",
          "description": "The name of the project that was cancelled."
        },
        "cancellation_result": {
          "type": "boolean",
          "description": "Indicates if the project was cancelled."
        },
        "reason_for_cancellation_mention": {
          "type": "string",
          "description": "The specific reason mentioned in the context for the project's cancellation."
        }
      },
      "required": [
        "project_name",
        "cancellation_result",
        "reason_for_cancellation_mention"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_name",
    "person_role",
    "disaster_details",
    "project_affected"
  ],
  "additionalProperties": false
}
