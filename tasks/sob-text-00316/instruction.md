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
Sugrue: Sugŕue is an Irish surname, which is an anglicized form of the old Gaelic name Ó Siochfhrádha, meaning "descendant of Siochfhrádh", or Ó Siochŕu the modern Gaelic equivalent of Ó Sugŕue, which in turn is a Gaelic version of the old norse German given first name Siegfried, meaning "victory and peace".

Endang (name): Endang is a common given first name for women in Indonesia and occasionally for men.  Notable people with the first name Endang include:

Columbia Hills (Mars): The Columbia Hills are a range of low hills inside Gusev crater on Mars.  They were observed by the Mars Exploration Rover "Spirit" when it landed within the crater in 2004.  They were promptly given an unofficial name by NASA since they were the most striking nearby feature on the surface.  The hills lie approximately 3 km away from the rover's original landing position.  The range is named to memorialize the Space Shuttle "Columbia" disaster.  On February 2, 2004, the individual peaks of the Columbia Hills were named after the seven astronauts who died in the disaster.  "Spirit" spent a few years exploring the Columbia Hills until it ceased to function in 2010.  It is also considered a potential landing site for the "Mars 2020" rover.

Zander (surname): Zander is a surname, a nickname for the name Alexander, and an uncommonly given first name, and may refer to:

NASA Astronaut Group 7: Astronaut Group 7, referred to in some documents as the USAF MOL Transfer, was announced by NASA on August 14, 1969, and was the last group to be selected during the Apollo era.  After the USAF Manned Orbiting Laboratory (MOL) project was cancelled, NASA hired seven of the astronauts selected for that program to form this "Group 7", roughly the younger half of the MOL astronauts.  By the time they joined NASA, all Apollo flight assignments had been lined up, but four were given non-flying support assignments for Apollo.  Others were also given support assignments for Skylab and the Apollo-Soyuz Test Project, with Bobko and Crippen participating in the Skylab Medical Experiment Altitude Test.  Group 7 went on to form the core of early Space Shuttle pilots, upgrading to commander after their first flight, flying 17 STS missions between them, plus the Approach and Landing Tests of "Enterprise" (OV-101) .

Troy (given name): Troy is a male given first name used in English-speaking countries, and derives from the Irish Gaelic "Troightheach", meaning "foot soldier".  Troy can also be an informal form of the female name Gertrude (often shortened to Trude) in Dutch.  The name Troy may refer to:

Scott Carpenter: Malcolm Scott Carpenter (May 1, 1925 – October 10, 2013), (Cmdr, USN), was an American naval officer and aviator, test pilot, aeronautical engineer, astronaut, and aquanaut.  He was one of the original seven astronauts selected for NASA's Project Mercury in April 1959.  Carpenter was the second American (after John Glenn) to orbit the Earth and the fourth American in space, following Alan Shepard, Gus Grissom, and Glenn.

Gordon Cooper: Leroy Gordon "Gordo" Cooper Jr. (March 6, 1927 – October 4, 2004), (Col, USAF), better known as Gordon Cooper, was an American aerospace engineer, test pilot, United States Air Force pilot, and one of the seven original astronauts in Project Mercury, the first manned space program of the United States.

Mercury Seven: The Mercury Seven were the group of seven Mercury astronauts announced by NASA on April 9, 1959.  They are also referred to as the Original Seven or Astronaut Group 1.  They piloted the manned spaceflights of the Mercury program from May 1961 to May 1963.  These seven original American astronauts were Scott Carpenter, Gordon Cooper, John Glenn, Gus Grissom, Wally Schirra, Alan Shepard, and Deke Slayton.

Deke Slayton: Donald Kent "Deke" Slayton (March 1, 1924 – June 13, 1993), (Major, USAF) was an American World War II pilot, aeronautical engineer, test pilot who was selected as one of the original NASA Mercury Seven astronauts, and became NASA's first Chief of the Astronaut Office.

Question: Which member of the group of seven astronauts announced by NASA in 1959 had Leroy as his given first name?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "astronaut_details": {
      "type": "object",
      "properties": {
        "full_name": {
          "type": "string",
          "description": "The full name of the astronaut."
        },
        "given_first_name_matched": {
          "type": "string",
          "description": "The specific given first name that was matched in the query."
        }
      },
      "required": [
        "full_name",
        "given_first_name_matched"
      ],
      "additionalProperties": false
    },
    "astronaut_group_details": {
      "type": "object",
      "properties": {
        "group_name": {
          "type": "string",
          "description": "The name of the astronaut group."
        },
        "announcement_year": {
          "type": "integer",
          "description": "The year the astronaut group was announced by NASA."
        }
      },
      "required": [
        "group_name",
        "announcement_year"
      ],
      "additionalProperties": false
    },
    "final_answer": {
      "type": "string",
      "description": "The full name of the astronaut who matches the criteria."
    }
  },
  "required": [
    "astronaut_details",
    "astronaut_group_details",
    "final_answer"
  ],
  "additionalProperties": false
}
