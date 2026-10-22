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
KSLU (Saint Louis University): KSLU is a Student Media Organization at Saint Louis University (SLU) in Saint Louis, Missouri.  The organization, which is affiliated with the College of Arts & Sciences' Department of Communication, provides "Saint Louis University and the St. Louis community with a student-run, tangible media outlet; providing new music, talk radio, written publication, as well as other student needs".  Its studios and offices are located in the University's Busch Student Center building.

Saint Louis College La Union: Saint Louis College (SLC) is a college in City of San Fernando, La Union, Philippines.  It was founded by the Congregatio Immaculati Cordis Mariae (CICM).  There are also sister schools of SLC, like Saint Louis University(SLU) in Baguio, University of Saint Louis Tuguegarao (USL) in Tuguegarao City, Saint Louis College of Cebu in Mandaue, Cebu, Saint Mary's University (Philippines) in Bayombong, Nueva Vizcaya, and Maryhill School of Theology in Quezon City.

Saint Louis University Ice Pavilion: The Saint Louis University Ice Pavilion is a proposed project by Saint Louis University to build an indoor ice and sports facility to be constructed in concert with another project already in progress, the Chaifetz Arena.  The university is planning to build an on-campus ice arena, to be named 'SLU Ice Pavilion.'  The facility will host youth, high school, college hockey as well as special events; it will have a seating capacity of 2,300, and offer four youth hockey locker rooms, Saint Louis University Locker rooms (D1 and D2), four Prep School Locker rooms, conditioning and weight room.  As well as common and quiet study lounges for students and private offices and two private suites to be used for special events and/or VIP use.  The Ice Pavilion will also offer activities such as public skating, figure skating clubs, speed skating clubs, intramural broomball, intramural hockey, curling clubs, and learn-to-skate opportunities for the students and faculty.  The plans for this new Ice Pavilion were in response to the need for a closer facility to the Saint Louis University campus.  The current facility in use, the Summit Center in Chesterfield, MO, is approximately 21 miles away from SLU's campus, with average crowd sizes of 250-400 in attendance.

University of Missouri System: The University of Missouri System is a state university system providing centralized administration for four universities, a health care system, an extension program, and ten research and technology parks.  Nearly 70,000 students are currently enrolled at its four campuses.  The health care system operates several hospitals and clinics in central Missouri, while the extension program provides distance learning and other educational initiatives statewide.

The Grove, St. Louis: The Grove is a business district located between Vandeventer and Kingshighway in the Forest Park East neighborhood of St. Louis, Missouri.  It is near Barnes-Jewish Hospital, Washington University School of Medicine, Saint Louis University Hospital, Saint Louis University School of Medicine, Forest Park, and Tower Grove Park.

Saint Louis University Museum of Art: The Saint Louis University Museum of Art is the formal art museum for Saint Louis University.  It is located at 3663 Lindell Boulevard in St. Louis, Missouri and is also known as O'Donnell Hall.

Saint Louis University School of Medicine: Saint Louis University School of Medicine (SLUSOM) is a private, American Medical School within Saint Louis University.  Located in the city of St. Louis, Missouri, Saint Louis University School of Medicine was established in 1836 and has the distinction of awarding the first M.D. degree west of the Mississippi River.

Saint Louis University: Saint Louis University (SLU, ) is a private Roman Catholic four-year research university with campuses in St. Louis, Missouri, United States and Madrid, Spain.  Founded in 1818 by the Most Reverend Louis Guillaume Valentin Dubourg, It is the oldest university west of the Mississippi River and the second-oldest Jesuit university in the United States.  It is one of 28 member institutions of the Association of Jesuit Colleges and Universities.  The university is accredited by the North Central Association of Colleges and Secondary Schools.  SLU's athletic teams compete in NCAA's Division I and are a member of the Atlantic 10 Conference.  It has an enrollment of 13,505 students, including 8,687 undergraduate students and 4,818 graduate students that represents all 50 states and more than 70 foreign countries.  Its average class size is 23.8 and the student-faculty ratio is 12:1.

Saint Louis University School of Law: Saint Louis University School of Law, also known as SLU LAW, is a private American law school located in St. Louis, Missouri.  It is one of the professional graduate schools of Saint Louis University.  Opened in 1843, it is the first law school west of the Mississippi River.  The school has been ABA approved since 1924 and is a member of the Association of American Law Schools.  Housed in Scott Hall, the law school has the highest enrollment of law students in Missouri .  It offers both full- and part-time programs.  The school is also home to Saint Louis University's Vincent C. Immel Law Library, which is one of the largest law libraries in the state of Missouri.  Supreme Court Justice Clarence Thomas studied for his bar exam at the old Omer Poos Law Library on the main SLU campus.

Saint Louis University Madrid Campus: Saint Louis University - Madrid Campus (SLU-Madrid), founded in 1967, is a 4-year American university in Spain.  Saint Louis University is a highly ranked Jesuit institution with campuses in St. Louis, Missouri, and Madrid, Spain.  SLU-Madrid offers fully accredited American undergraduate and graduate degrees that can be completed in Spain or combined with studies at the St. Louis campus.

Question: Which university has more students enrolled, Saint Louis University or the University of Missouri System?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "comparison_entities": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "student_enrollment": {
            "type": "integer"
          }
        },
        "required": [
          "name",
          "student_enrollment"
        ],
        "additionalProperties": false
      }
    },
    "entity_with_more_students": {
      "type": "string"
    },
    "enrollment_difference": {
      "type": "integer"
    }
  },
  "required": [
    "comparison_entities",
    "entity_with_more_students",
    "enrollment_difference"
  ],
  "additionalProperties": false
}
