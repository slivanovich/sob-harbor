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
Van Allen Building: The Van Allen Building, also known as Van Allen and Company Department Store, is a historic commercial building at Fifth Avenue and South Second Street in Clinton, Iowa.  The four-story building was designed by Louis Sullivan and commissioned by John Delbert Van Allen (October 5, 1850 – December 30, 1928).  Constructed 1912–1914 as a department store, it now has upper floor apartments with ground floor commercial space.  The exterior has brick spandrels and piers over the structural steel skeletal frame.  Terra cotta is used for horizontal accent banding and for three slender, vertical applied mullion medallions on the front facade running through three stories, from ornate corbels at the second-floor level to huge outbursts of vivid green terra cotta foliage in the attic.  There is a very slight cornice.  Black marble facing is used around the glass show windows on the first floor.  The walls are made of long thin bricks in a burnt gray color with a tinge of purple.  Above the ground floor all the windows are framed by a light gray terra cotta.  The tile panels in Dutch blue and white pay tribute to Mr. Van Allen's Dutch heritage of which he was quite proud.  (Mr. Van Allen was accepted for membership in the Holland Society of New York in 1908).  The Van Allen Building was declared a National Historic Landmark in 1976 for its architecture.

Manhattan Project: The Manhattan Project was a research and development undertaking during World War II that produced the first nuclear weapons.  It was led by the United States with the support of the United Kingdom and Canada.  From 1942 to 1946, the project was under the direction of Major General Leslie Groves of the U.S. Army Corps of Engineers.  Nuclear physicist Robert Oppenheimer was the director of the Los Alamos Laboratory that designed the actual bombs.  The Army component of the project was designated the Manhattan District; "Manhattan" gradually superseded the official codename, Development of Substitute Materials, for the entire project.  Along the way, the project absorbed its earlier British counterpart, Tube Alloys.  The Manhattan Project began modestly in 1939, but grew to employ more than 130,000 people and cost nearly US $2 billion (about $ in 2016 dollars).  Over 90% of the cost was for building factories and to produce fissile material, with less than 10% for development and production of the weapons.  Research and production took place at more than 30 sites across the United States, the United Kingdom, and Canada.

Clarence Larson: Clarence Edward Larson (September 20, 1909 – February 15, 1999) was an American chemist, nuclear physicist and industrial leader.  He was involved in the Manhattan Project, and was later director of Oak Ridge National Laboratory and commissioner of the U.S. Atomic Energy Commission.

James Van Allen: James Alfred Van Allen (September 7, 1914August 9, 2006) was an American space scientist at the University of Iowa.  He was instrumental in establishing the field of magnetospheric research in space.

X-10 Graphite Reactor: The X-10 Graphite Reactor at Oak Ridge National Laboratory in Oak Ridge, Tennessee, formerly known as the Clinton Pile and X-10 Pile, was the world's second artificial nuclear reactor (after Enrico Fermi's Chicago Pile-1), and the first designed and built for continuous operation.  It was built during World War II as part of the Manhattan Project.

Alvin M. Weinberg: Alvin Martin Weinberg (April 20, 1915 – October 18, 2006) was an American nuclear physicist who was the administrator at Oak Ridge National Laboratory (ORNL) during and after the Manhattan Project.  He came to Oak Ridge, Tennessee, in 1945 and remained there until his death in 2006.  He was the first to use the term "Faustian bargain" to describe nuclear energy.

Ed Westcott: James Edward Westcott (born January 20, 1922) is a photographer who worked for the United States government in Oak Ridge, Tennessee, during the Manhattan Project and the Cold War.  As one of the few people permitted to have a camera in the Oak Ridge area during the Manhattan Project, he created the main visual record of the construction and operation of the Oak Ridge production facilities and of civilian life in the enclosed community of Oak Ridge.

Clinton Engineer Works: The Clinton Engineer Works (CEW) was the production installation of the Manhattan Project that during World War II produced the enriched uranium used in the 1945 bombing of Hiroshima, as well as the first examples of reactor-produced plutonium.  It consisted of production facilities arranged at three major sites, various utilities including a power plant, and the town of Oak Ridge.  It was in East Tennessee, about 18 mi west of Knoxville, and was named after the town of Clinton, 8 mi to the north.  The production facilities were mainly in Roane County, and the northern part of the site was in Anderson County.  The Manhattan District Engineer, Kenneth Nichols, moved the Manhattan District headquarters from Manhattan to Oak Ridge in August 1943.  During the war, Clinton's advanced research was managed for the government by the University of Chicago.

Y-12 National Security Complex: The Y-12 National Security Complex is a United States Department of Energy National Nuclear Security Administration facility located in Oak Ridge, Tennessee, near the Oak Ridge National Laboratory.  It was built as part of the Manhattan Project for the purpose of enriching uranium for the first atomic bombs.  In the years after World War II, it has been operated as a manufacturing facility for nuclear weapons components and related defense purposes.

Nicholas M. Smith, Jr.: Nicholas Monroe Smith, Jr. (23 March 1914 – 7 August 2003), nuclear physicist and research consultant.  Smith was a nuclear physicist, an expert in the field of nuclear and reactor physics, developer of operations research/computer modeling and computer applications consultant.  He had ties to the Manhattan Project at Chicago and Oak Ridge, and worked with Samuel Allison and James Van Allen.  Smith was a pioneer in the field of operations research.

Question: Nicholas Monroe Smith, Jr., was a nuclear physicist and research consultant, he had ties to the Manhattan Project at Chicago and Oak Ridge, and worked with James Van Allen, he was an American space scientist at which organization? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_of_interest": {
      "type": "string",
      "description": "The name of the person whose organization is being sought."
    },
    "person_role": {
      "type": "string",
      "description": "The professional role or title of the person of interest."
    },
    "associated_organization": {
      "type": "string",
      "description": "The organization where the person of interest worked."
    },
    "collaborator_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the collaborator mentioned in the context."
        },
        "relationship_description": {
          "type": "string",
          "description": "Description of the relationship or collaboration between the person of interest and the collaborator."
        }
      },
      "required": [
        "name",
        "relationship_description"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_of_interest",
    "person_role",
    "associated_organization",
    "collaborator_details"
  ],
  "additionalProperties": false
}
