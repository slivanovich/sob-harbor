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
Wale Adebanwi: Professor Wale Adebanwi, (born 1969), is a Nigerian - born first Black African Rhodes Professor at Oxford University

Despoina: In Greek mythology, Despoina, Despoena or Despoine, was the daughter of Demeter and Poseidon and sister of Arion.  She was the goddess of mysteries of Arcadian cults worshipped under the title "Despoina", "the mistress" alongside her mother Demeter, one of the goddesses of the Eleusinian mysteries.  Her real name could not be revealed to anyone except those initiated to her mysteries.  Pausanias spoke of Demeter as having two daughters; Kore being born first, then later Despoina.  With Zeus being the father of Kore, and Poseidon as the father of Despoina.  Pausanias made it clear that Kore is Persephone, though he wouldn't reveal Despoina's proper name.

Michael S. Hopkins: Michael Scott Hopkins (born December 28, 1968) is a Colonel in the U.S. Air Force, and a current NASA astronaut.  Hopkins was selected in June 2009 as a member of the NASA Astronaut Group 20.  He made his first spaceflight as a Flight Engineer on Soyuz TMA-10M/Expedition 37/Expedition 38, from September 2013 until March 2014.  He was the first member of his astronaut class to fly in space.

List of Lab Rats characters: "Lab Rats", also known as "Lab Rats: Bionic Island" for its fourth season, is an American television sitcom that premiered on February 27, 2012, on Disney XD.  It focuses on the life of teenager Leo Dooley, whose mother, Tasha, marries billionaire genius Donald Davenport.  He meets Adam, Bree, and Chase, three bionic superhumans, with whom he develops an immediate friendship.  It should be noted that the names of the Lab Rats imply that they were originally known as subjects A, B, C and D. Adam was born first, then Bree, then Chase, and finally Daniel.

Claude Nicollier: Claude Nicollier (born 2 September 1944 in Vevey, Switzerland) is the first astronaut from Switzerland.  He has flown on four Space Shuttle missions.  His first spaceflight (STS-46) was in 1992, and his final spaceflight (STS-103) was in 1999.  He took part in two servicing missions to the Hubble Space Telescope (called STS-61 and STS-103).  During his final spaceflight he participated in a spacewalk, becoming the first European Space Agency astronaut to do so during a Space Shuttle mission (previous ESA astronauts conducted spacewalks aboard "Mir", see List of spacewalks and moonwalks 1965–1999).  In 2000 he was assigned to the Astronaut Office Extravehicular Activity Branch, while maintaining a position as Lead ESA Astronaut in Houston.  Nicollier retired from ESA in April 2007.

Frank De Winne: Frank, Viscount De Winne (born 25 April 1961, in Ledeberg, Belgium) is a Belgian Air Component officer and an ESA astronaut.  He is Belgium's second person in space (after Dirk Frimout).  He was the first ESA astronaut to command a space mission when he served as commander of ISS Expedition 21.  ESA astronaut de Winne serves currently as Head of the European Astronaut Centre of the European Space Agency in Cologne/Germany (Köln).

Augustine of Canterbury: Augustine of Canterbury (born first third of the 6th century – died probably 26 May 604) was a Catholic Benedictine monk who became the first Archbishop of Canterbury in the year 597.  He is considered the "Apostle to the English" and a founder of the Catholic Church in England.

Michael Foale: Colin Michael Foale, CBE (born 6 January 1957) is a British-American astrophysicist and former NASA astronaut.  He is a veteran of six Space Shuttle missions and extended missions on both Mir and the International Space Station.  He was the first Briton to perform a space walk, and until 17 April 2008, he held the record for most time spent in space by a US citizen: 374 days, 11 hours, 19 minutes.  He still holds the cumulative-time-in-space record for a UK citizen.

STS-63: STS-63 was the first mission of the US/Russian Shuttle-Mir Program, which carried out the first rendezvous of the American Space Shuttle with Russia's space station "Mir".  Known as the 'Near-Mir' mission, the flight used Space Shuttle "Discovery", which lifted off from launch pad 39B on 3 February 1995 from Kennedy Space Center, Florida.  A night launch and the 20th mission for "Discovery", it marked the first time a Space Shuttle mission had a female pilot, Eileen Collins, the first EVAs for both a UK born astronaut Michael Foale and a US astronaut of African heritage Bernard A. Harris, Jr. and it also carried out the successful deployment and retrieval of the Spartan-204 platform, along with the scheduled rendezvous and flyaround of "Mir", in preparation for STS-71, the first mission to dock with "Mir".

Franco Malerba: Franco Egidio Malerba (born October 10, 1946, in Busalla, Metropolitan City of Genoa, Italy) is an astronaut.  He was the first citizen of Italy to travel to space.

Question: Which astronaut was born first Franco Malerba or Michael Foale?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "astronauts_compared": {
      "type": "array",
      "description": "Details of the astronauts being compared.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The full name of the astronaut."
          },
          "birth_year": {
            "type": "integer",
            "description": "The birth year of the astronaut."
          }
        },
        "required": [
          "name",
          "birth_year"
        ],
        "additionalProperties": false
      }
    },
    "first_born_astronaut_name": {
      "type": "string",
      "description": "The name of the astronaut who was born first."
    },
    "first_born_astronaut_birth_year": {
      "type": "integer",
      "description": "The birth year of the astronaut who was born first."
    }
  },
  "required": [
    "astronauts_compared",
    "first_born_astronaut_name",
    "first_born_astronaut_birth_year"
  ],
  "additionalProperties": false
}
