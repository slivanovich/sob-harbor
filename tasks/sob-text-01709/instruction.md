{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\n2008 South Carolina Learjet 60 crash: The 2008 South Carolina Learjet 60 crash occurred just before midnight on September 19, 2008, when a Learjet 60 (registration N999LJ ) crashed while taking off from Columbia Metropolitan Airport in South Carolina.  The weather at the time was cool, dry, and clear.  The plane hit runway lights and crashed through the boundary fence, crossing South Carolina Highway 302 (SC 302/Edmund Highway/Airport Boulevard), and came to rest on an embankment by the side of the highway.  No one on the ground was hurt, but four of the six people on the plane (including both pilots) died in the crash, while the other two, Travis Barker and Adam Goldstein, suffered severe burns.  The plane was a charter flight taken by Barker, Goldstein and their entourage following a performance by their musical group TRV$DJAM at a free concert in Five Points earlier that night to Van Nuys, California.\n\nSnell Memorial Foundation: The Snell Memorial Foundation is a nonprofit organization created to provide a high quality standard of safety for helmets. Founded in 1957, the foundation is named after William \"Pete\" Snell, a popular sports car racer who died in 1956 of head injuries he received when the racing helmet he wore failed to protect his head.  A group of friends, scientists, physicians, and others joined together to create a group that would promote research and education as well as test and develop standards to improve the effectiveness of helmets.  Helmets with british standard approval is also snell approved.\n\nJohn Snell (disambiguation): John Snell (died 1679) was founder of the Snell Exhibitions at the University of Oxford.\n\nSnell Exhibition: The Snell Exhibition is an annual scholarship awarded to students of the University of Glasgow to allow them to undertake postgraduate study at Balliol College, Oxford.  The award was founded by the bequest of Sir John Snell in a will made in 1677, although the original stipulation referred to the University of Oxford, rather than Balliol in particular.  Snell died on 6 August 1679, but wrangling over the will meant that it was nearly twenty years before the first scholarships were awarded; the first four Snell Exhibitioners were admitted to Balliol in mid-1699.\n\nSouthern Airways Flight 242: Southern Airways Flight 242 was a DC-9-31 jet, registered N1335U, that executed a forced landing on a highway in New Hope, Paulding County, Georgia, United States after suffering hail damage and losing thrust on both engines in a severe thunderstorm on April 4, 1977.\n\nDudley Snell: Frederick Dudley Snell (14 December 1924 – 14 December 1988) was an Australian electrical engineer and tramways administrator.  He grew up in Bendigo and following his education worked for the State Electricity Commission of Victoria.  After serving in the Royal Australian Air Force during World War II, he commenced work at the Melbourne and Metropolitan Tramways Board (MMTB) in 1953, being appointed the MMTB's fifth and last Chairman in 1976.  Following the dissolving of the MMTB into the Metropolitan Transit Authority (MTA) in 1983, he became General Manager of the MTA Bus and Tram Division.  Snell worked for the MMTB, MTA, and Leighton on Hong Kong's Tuen Mun light rail system, and died in Hong Kong in 1988.\n\nVarig Flight 254: Varig Flight 254 was a Boeing 737-241, c/n 21006/398, registration PP-VMK, on a scheduled passenger flight from São Paulo, Brazil, to Belém, Pará, Brazil, with several intermediate stopovers, on 3 September 1989.  Prior to takeoff from Marabá, Pará, towards the final destination, the crew entered an incorrect heading into the flight computer.  Instead of flying northeast toward its destination, the plane flew due west and after some time was over a remote area of the Amazon jungle.  Attempts to reach an alternative airport were unsuccessful, and the plane eventually ran out of fuel.  The pilot made a belly landing in the jungle, 1050 mi northwest of Rio de Janeiro.  There were 54 occupants on board—48 passengers and a crew of six; 13 passengers died, and many more sustained serious injuries.  The survivors were rescued two days later.\n\nAnnette Snell: Annette Snell (March 22, 1945 – April 4, 1977) was an American rhythm and blues singer who recorded in the 1960s and 1970s.  She died in the Southern Airways Flight 242 crash.\n\nToa Domestic Airlines Flight 63: Toa Domestic Airlines Flight 63, registration JA8764, was a NAMC YS-11A-217 en route from Chitose Airport near Sapporo, Japan to Hakodate Airport.  The plane left Chitose Airport on a scheduled flight at 08:30.  After arriving in Hakodate airspace, the plane was descending below 1800 metres when it crashed at 09:05 into the south face of Yokotsudake (Yokotsu Mountain).  All 64 passengers and four crew on board perished.  The cause of the crash was determined to be pilot error that followed strong winds pushing the plane off course.\n\nPacific Southwest Airlines Flight 1771: PSA Flight 1771 was a British Aerospace 146-200A, registration N350PS, on a scheduled flight from Los Angeles, California to San Francisco.  On December 7, 1987, it crashed in Cayucos, California, as a result of a murder–suicide by one of the passengers.  All 43 passengers and crew aboard the plane died, five of whom, including the two pilots, were presumably shot dead before the plane crashed.  The man who caused the crash, David A. Burke, was a disgruntled former employee of USAir, the parent company of PSA.  A dramatization of the incident was portrayed on the TV documentary series \"Mayday\".\n\nQuestion: What was the registration of the plane on which Annette Snell died?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person who died.\"\n    },\n    \"event_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the event (plane crash) in which the person died.\"\n    },\n    \"aircraft_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of aircraft involved in the event.\"\n    },\n    \"aircraft_registration\": {\n      \"type\": \"string\",\n      \"description\": \"The registration number of the aircraft.\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"event_name\",\n    \"aircraft_type\",\n    \"aircraft_registration\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the person who died."
      },
      "event_name": {
        "type": "string",
        "description": "The name of the event (plane crash) in which the person died."
      },
      "aircraft_type": {
        "type": "string",
        "description": "The type of aircraft involved in the event."
      },
      "aircraft_registration": {
        "type": "string",
        "description": "The registration number of the aircraft."
      }
    },
    "required": [
      "person_name",
      "event_name",
      "aircraft_type",
      "aircraft_registration"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
