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
Indiana University – Purdue University Fort Wayne: Indiana University – Purdue University Fort Wayne (IPFW) is a coeducational public university in Fort Wayne, Indiana, United States.  Founded in 1964, IPFW is a cooperatively-managed regional campus of two state university systems: Indiana University and Purdue University.  IPFW enrolls 13,459 undergraduate and postgraduate students in nine colleges and schools, including a branch of the Indiana University School of Medicine.  IPFW offers more than 200 graduate and undergraduate degree programs through IU or Purdue universities.  The university's 14 men's and women's athletic teams compete in Division I of the NCAA Summit League and, since the 2016–17 school year, are known as the Fort Wayne Mastodons.

IUPUI University Library: IUPUI University Library is the university library of Indiana University–Purdue University Indianapolis.  IUPUI is an urban campus of Indiana University and Purdue University in Indianapolis, Indiana.  Indiana University is the managing partner.  IUPUI offers undergraduate, graduate and professional degrees from both universities.

Lawrence Jegen: Lawrence A. Jegen III (born 1934) is the Thomas F. Sheehan Professor of Tax Law and Policy at the Indiana University Robert H. McKinney School of Law.  He joined the faculty in 1962 as an Assistant Professor and was made full professor in 1964.  Among numerous honors, he has twice received the Thomas Hart Benton Mural Medallion from Indiana University, its highest award, in 1993 and 2005, and three times the Sagamore of the Wabash Award for humanity in living, wisdom and counsel, and inspiration and leadership from governors of Indiana, in 1980, 1988 and 1997.  In 2006 the Lawrence A. Jegen III Professorship was created and funded at Indiana University Foundation by Michael D. McCormick, which professorship is to be awarded to an active scholar and teacher at the Indiana University Robert H. McKinney School of Law in Indianapolis.

University of Washington: The University of Washington (commonly referred to as UW, simply Washington, or informally "U-Dub") is a large, public flagship research university in Seattle, Washington, established in 1861.

Indiana University: Indiana University (IU) is a multi-campus public university system in the state of Indiana, United States.  Indiana University has a combined student body of more than 110,000 students, including approximately 46,000 students enrolled at the Indiana University Bloomington campus and approximately 31,000 students enrolled at the Indiana University – Purdue University Indianapolis (IUPUI) campus.

Indiana University Bloomington: Indiana University Bloomington (abbreviated "IU Bloomington" and colloquially referred to as "IU" or simply "Indiana") is a public research university located in Bloomington, Indiana, United States.  With over 48,000 students, IU Bloomington is the flagship institution of the Indiana University system and its largest university.

Indiana University High School: Indiana University High School (IUHS) is a co-educational, non-denominational, distance education high school with its offices located on the campus of Indiana University Bloomington, in Bloomington, Indiana, United States.  It serves students around the world and provides individual courses and diploma programs to students, online or through the mail.  IUHS also offers student services, such as career counselling and "life experience credits" for non-academic achievement.  Indiana University High School is the founding member of the Indiana Virtual Learning Consortium and was ranked as the "second best online high school" by The Best Schools.  IUHS is a 21st Century Scholarship School.

Vincennes University: Vincennes University (VU) is a public university with its main campus in Vincennes, Indiana, in the United States.  Founded in 1801 as Jefferson Academy, VU is the oldest public institution of higher learning in the Northwest Territory and in Indiana.  In 1889, VU was chartered by the State of Indiana as a two-year university.  In 2005, VU began offering baccalaureate degrees in seven select areas, including education, nursing, technology, homeland security, and health information management.  VU's campus in Vincennes is a residential campus nestled along the banks of the Wabash River.  Other VU sites include a campus in Jasper, Indiana, the Center for Advanced Manufacturing and Logistics in Fort Branch, Indiana, along with centers for Aviation, Logistics, Advanced Manufacturing, and American Sign Language, in the Indianapolis area.  VU was chartered in 1806 as the Indiana Territory's four-year university and remained the state of Indiana's sole publicly funded four-year university until the establishment of Indiana University in 1820.  From 1999 to 2005, Vincennes University was in a state-mandated partnership with what became the Ivy Tech Community College.

2007–08 Indiana Hoosiers men's basketball team: The 2007–08 Indiana Hoosiers men's basketball team represented Indiana University during the 2007-08 NCAA Division I men's basketball season.  Indiana was a member of the Big Ten Conference.  They played their home games in Assembly Hall in Bloomington, Indiana.  The interim head coach at the end of the season was Dan Dakich.  Indiana University announced on February 22, 2008, that Kelvin Sampson accepted a $750,000 buyout of his contract and resigned as the Indiana University men’s basketball coach.

Lynda Delph: Lynda Delph is a Distinguished Professor of Biology and Section Associate Chair of the Evolution, Ecology, and Behavior Program at Indiana University - Bloomington.  Delph began her education at the University of Arizona, where she completed her undergraduate education in 1979 and masters in 1983.  In 1988, she completed her Ph.D. from the University of Canterbury, which was followed by a post doctoral fellowship at Rutgers University.  After she completed her fellowship, Delph began her career at Indiana University as an assistant professor in 1990, becoming a full professor in 2002 and a distinguished professor in 2017.  In addition to her faculty appointments, she served as a senior fellow of the Indiana Molecular Biology Institute and Executive Director of Science Outreach for the Indiana University College of Arts and Sciences.  Delph has also served as an officer in scientific societies in her field, acting as secretary of the Society for the Study of Evolution, Vice President of the American Society of Naturalists, and Council Member and later President of the American Genetic Association.

Question: Between Indiana University and University of Washington, which institution has more campuses?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "institution_with_more_campuses": {
      "type": "string",
      "description": "The name of the institution that has more campuses."
    },
    "institutions_details": {
      "type": "array",
      "description": "Details about each institution mentioned in the comparison.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the institution."
          },
          "is_multi_campus_system": {
            "type": "boolean",
            "description": "Indicates if the institution is described as a multi-campus system."
          },
          "campus_description": {
            "type": "string",
            "description": "A description of its campus structure from the context."
          }
        },
        "required": [
          "name",
          "is_multi_campus_system",
          "campus_description"
        ],
        "additionalProperties": false
      }
    },
    "comparison_summary": {
      "type": "string",
      "description": "A summary of why one institution has more campuses based on the context."
    }
  },
  "required": [
    "institution_with_more_campuses",
    "institutions_details",
    "comparison_summary"
  ],
  "additionalProperties": false
}
