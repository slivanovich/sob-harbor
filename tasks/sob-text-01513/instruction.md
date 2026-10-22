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
Jacq van den Berg: Jacob Ralph "Jacq" van den Berg (December 19, 1916, Birmingham) is a sailor from the Netherlands, who represented his country at the 1960 Summer Olympics in Naples.  Van den Berg, as crew on the Dutch Dragon took the 13th place with helmsman Wim van Duyl and fellow crew member Biem Dudok van Heel.

Janwillem van den Berg: Janwillem van den Berg (26 November 1920 in Akkrum – 18 October 1985 in Groningen) was a Dutch speech scientist and medical physicist who played a major role in establishing the myoelastic-aerodynamic theory of voice production.  The most notable aspect of van den Berg's theory is its impact on modern speech science in providing a foundation for modern models of vocal fold function.

Claude Nicollier: Claude Nicollier (born 2 September 1944 in Vevey, Switzerland) is the first astronaut from Switzerland.  He has flown on four Space Shuttle missions.  His first spaceflight (STS-46) was in 1992, and his final spaceflight (STS-103) was in 1999.  He took part in two servicing missions to the Hubble Space Telescope (called STS-61 and STS-103).  During his final spaceflight he participated in a spacewalk, becoming the first European Space Agency astronaut to do so during a Space Shuttle mission (previous ESA astronauts conducted spacewalks aboard "Mir", see List of spacewalks and moonwalks 1965–1999).  In 2000 he was assigned to the Astronaut Office Extravehicular Activity Branch, while maintaining a position as Lead ESA Astronaut in Houston.  Nicollier retired from ESA in April 2007.

L.W.C van den Berg: Lodewijk Willem Christiaan van den Berg (October 19, 1845 – March 2, 1927), or more commonly known as L.W.C. van den Berg, was a Dutch oriental scholar in the Dutch colonial era famous with his research on Arab Indonesians of Hadhrami descent, which was the first detailed research of its kind in the world at the time.

Wilma van den Berg: Wilhelmina Catharina Maria Martina "Wilma" van Gool (née van den Berg on 11 August 1947, commonly known as Wilma van den Berg) is a retired sprinter from the Netherlands.  In 1969–1970 she won two European medals and two medals at the 1970 Summer Universiade in various individual sprint events.  She competed at the 1968 and 1972 Summer Olympics in the 100 m and 200 m sprint and 4 × 100 m relay and finished in fourth place in the relay in 1968; individually, she failed to reach the finals.

Martin J. Fettman: Martin Joseph Fettman (B.S., D.V.M., M.S., Ph.D., Diplomate, ACVP) is an American pathologist and researcher who flew on NASA Space Shuttle mission STS-58 aboard the Space Shuttle Columbia as a Payload Specialist.

Gert van den Berg: Gert van den Berg, Gert van den Bergh or Gerrit van den Berg may refer to:

Lodewijk van den Berg: Lodewijk van den Berg (] ; born March 24, 1932) is a Dutch American chemical engineer, specializing in crystal growth, who flew on a 1985 Space Shuttle "Challenger" mission as a Payload Specialist.

STS-51-G: STS-51-G was the eighteenth flight of NASA's Space Shuttle program, and the fifth flight of Space Shuttle "Discovery".  The seven-day mission launched from Kennedy Space Center, Florida, on June 17, 1985, and landed at Edwards Air Force Base, California, on June 24.  Sultan Salman Al Saud of Saudi Arabia was on board as a payload specialist; Al Saud became the first Arab, the first Muslim, and the first member of a royal family to fly into space.  It was also the first Space Shuttle mission which flew without at least one astronaut from the pre-Shuttle era among its crew.

De Speld: De Speld ("The Pin") is a Dutch news satire website.  The website publishes satirical articles and videos parodying the style and content of regular news outlets.  "De Speld" was founded in 2007 by Jochem van den Berg and Melle van den Berg (no relationship).  Since its inception, the website's office has been based in Amsterdam.  In 2014 and 2015 De Speld was the 'most viral website' of The Netherlands.

Question:  Who flew on a 1985 Space Shuttle "Challenger" mission as a Payload Specialist, Claude Nicollier or  Lodewijk van den Berg?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person who flew on the mission."
    },
    "mission_year": {
      "type": "integer",
      "description": "The year the space shuttle mission took place."
    },
    "space_shuttle_name": {
      "type": "string",
      "description": "The name of the Space Shuttle used for the mission."
    },
    "role": {
      "type": "string",
      "description": "The role of the person during the space mission."
    },
    "nationality": {
      "type": "string",
      "description": "The nationality of the person."
    },
    "specialization": {
      "type": "string",
      "description": "The professional specialization of the person."
    }
  },
  "required": [
    "person_name",
    "mission_year",
    "space_shuttle_name",
    "role",
    "nationality",
    "specialization"
  ],
  "additionalProperties": false
}
