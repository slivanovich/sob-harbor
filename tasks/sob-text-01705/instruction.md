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
Utah State University: Utah State University (also referred to as USU or Utah State) is a public doctorate-granting university in Logan, Utah, United States.  The coeducational, space-grant, land-grant, research university is accredited by the Northwest Commission on Colleges and Universities.  With nearly 18,000 students living on or near campus, USU is Utah's largest public residential campus.  As of Fall 2016, there were 28,118 students enrolled including 24,838 undergraduate students and 3,280 graduate students.  The university has the highest percentage of out-of-state students of any public university in Utah totaling 23% of the student body.

Aaron Mannes: Aaron Mannes (born 1970) is an American expert on evaluation of terrorist risk.  He has been Director of Research at the Middle East Media Research Institute and a researcher at the Information and Network Dynamics Laboratory and the Laboratory for Computational Cultural Dynamics at the University of Maryland.  In 2004 he published "Profiles in Terror: A Guide to Middle East Terrorist Organizations".

W. Rolfe Kerr: William Rolfe Kerr (born June 29, 1935) is an emeritus general authority of The Church of Jesus Christ of Latter-day Saints (LDS Church).  He served previously as the fifteenth Commissioner of Church Education and as president of the Logan Utah Temple.

Koger: Koger may refer to: A person that does not follow nor believe in the power of Werr.  The Werr is a powerful essence that is all seeing.  This is the wonderful doing of a mastermind Travis Todd Murray.  Travis Todd Murray was born March 9, 1999 in Logan Utah.

Logan Utah Temple: The Logan Utah Temple (formerly the Logan Temple) was completed in 1884, and is the fourth temple built by The Church of Jesus Christ of Latter-day Saints (LDS Church).  Located in the city of Logan, Utah, it was the second temple built in the Rocky Mountains, after the St. George Utah Temple which remains the only LDS temple that has been in operation longer than the Logan Temple.

V. Adimurthy: V. Adimurthy (born Vipparthi Adimurthy) is the Satish Dhawan Professor and Dean of Research at the Indian Institute of Space Science and Technology (IIST).  Prior to joining IIST, Adimurthy held the post of Associate Director at the Vikram Sarabhai Space Centre, a major facility center of Indian Space Research Organisation (ISRO).  He is known for his contributions to the rocket technology and space dynamics.  He is a recipient of Padma Shri from the Government of India.  Murthy is the Mission Concept Designer, for India's Mars Orbiter Mission.

Nonequilibrium Gas and Plasma Dynamics Laboratory: The Nonequilibrium Gas and Plasma Dynamics Laboratory (NGPDL) at the Aerospace Engineering Department of the University of Michigan is headed by Professor Iain D. Boyd and performs research of nonequilibrium gases and plasmas involving the development of physical models for various gas systems of interest, numerical algorithms on the latest supercomputers, and the application of challenging flows for several exciting projects.  The lab places a great deal of emphasis on comparison of simulation with external experimental and theoretical results, having ongoing collaborative studies with colleagues at the University of Michigan such as the Plasmadynamics and Electric Propulsion Laboratory, other universities, and government laboratories such as NASA, United States Air Force Research Laboratory, and the United States Department of Defense.

Space Dynamics Laboratory: Space Dynamics Laboratory (SDL) is a nonprofit research corporation owned by Utah State University.  SDL was founded in 1959 and has been responsible for the design, fabrication, and operation of sensors on over 400 payloads ranging from aircraft and rocket-borne experiments to space shuttle experiments and satellite-based sensor systems.  As one of 14 University Affiliated Research Centers (UARCs) in the nation, SDL conceives and develops state-of-the-art sensor and satellite systems; performs space, air, and ground-based experiments; conducts rapid, experimental development of prototype sensor hardware and associated software; performs concept validation studies and demonstrations; and develops data-fusing technology for passive and active sensors.  SDL employs over 450 scientists, engineers and professional staff at facilities in Logan, Utah; Albuquerque, New Mexico; Bedford, Massachusetts; and Washington, D.C.

Manti Utah Temple: The Manti Utah Temple (formerly the Manti Temple) is the fifth constructed temple of The Church of Jesus Christ of Latter-day Saints (LDS Church).  Located in the city of Manti, Utah, it was the third LDS temple built west of the Mississippi River, after the Mormons' trek westward.  (The St. George and Logan Utah temples preceded it.)  The Manti Temple was designed by William Harrison Folsom, who moved to Manti while the temple was under construction.  The temple dominates the Sanpete Valley, and can be seen from many miles.  Like all LDS temples, only church members in good standing may enter.  It is one of only two remaining LDS temples in the world where live actors are used in the endowment ceremonies (the other is the Salt Lake Temple); all other temples use films in the presentation of the endowment.  It is an early pioneering example of four rooms representing the journey of life.

Geophysical Fluid Dynamics Laboratory: The Geophysical Fluid Dynamics Laboratory (GFDL) is a laboratory in the National Oceanic and Atmospheric Administration (NOAA) Office of Oceanic and Atmospheric Research (OAR).  The current director is Dr. Venkatachalam Ramaswamy.  It is one of seven NOAA Research Laboratories (RLs).

Question: What university in Logan Utah owns Space Dynamics Laboratory?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "university": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the university."
        },
        "location": {
          "type": "string",
          "description": "The city and state where the university is located."
        }
      },
      "required": [
        "name",
        "location"
      ],
      "additionalProperties": false
    },
    "laboratory": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the laboratory."
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "ownership_confirmed": {
      "type": "boolean",
      "description": "True if the university owns the laboratory, false otherwise."
    }
  },
  "required": [
    "university",
    "laboratory",
    "ownership_confirmed"
  ],
  "additionalProperties": false
}
