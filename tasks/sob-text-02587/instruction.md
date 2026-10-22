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
Bill Bradley (basketball, born 1941): William Bradley (June 16, 1941) was an American basketball player.  He attended Central High School in Louisville, Kentucky.

Central Visual and Performing Arts High School: Central Visual and Performing Arts High School (also known as Central VPA High School or Central High School) is a magnet high school in St. Louis, Missouri, part of the St. Louis Public Schools.  Founded in 1853, Central is the oldest public high school west of the Mississippi River, although it has moved several times and merged with a magnet school in 1984.  Central VPA specializes in the arts, with students taking courses in three art majors, including visual art, musical art, and performing art, with focuses on ceramics, drawing and painting, photography, instrumental music, vocal music, dance, and theater.

Union County Academy for Allied Health Sciences: The Union County Academy for Allied Health Sciences (UCAAHS) is a full-time Vocational public high school, located in Scotch Plains, in Union County, New Jersey, United States.  This school serves students in ninth through twelfth grades from across Union County as a career academy on the Union County Vocational Technical Schools Campus, which also includes the Academy for Information Technology, Union County Magnet High School, Academy for Performing Arts, and the Union County Vocational Technical High School.

The Academy @ Shawnee: The Academy @ Shawnee (formerly, Shawnee High School Magnet Career Academy [MCA]), is a magnet middle school and high school (grades 6-12) in the Jefferson County Public School District in Louisville, Kentucky, with a focus in Aerospace, which is the number one export in the state of Kentucky.  Qualifying students choose from Aerospace-Flight, Aerospace Engineering, Navy Junior Reserve Officers Training Corps (NJROTC).  The Academy offers the Advance Program and Advanced Placement (AP) courses, as well as some dual-credit and a pre-engineering course via Project Lead the Way.  It is one of five West Louisville schools selected as part of the Signature Partnership initiative with the University of Louisville.  The Academy@ Shawnee also houses the Challenger Learning Center, which offers science, technology, engineering, and math (STEM) student learning exercises, or missions, which are housed in a realistic looking environment that was modeled after the Challenger space shuttle and control room.

Southern High School (Kentucky): Southern High School Magnet Career Academy (MCA) was built in 1951, and the first graduating class was in 1952.  Its mission is to prepare students to be "productive members of a technologically advanced society."

Union County Vocational-Technical High School: The Union County Vocational-Technical High School (UC Tech) is a full-time vocational public high school, located in Scotch Plains in Union county, New Jersey, United States.  This school serves students in ninth through twelfth grades from across Union county as a career academy on the Union County Vocational Technical Schools Campus, which also includes the Union County Academy for Allied Health Sciences, Academy for Information Technology, Union County Magnet High School and the Academy for Performing Arts.

Central High School (Louisville, Kentucky): Formally known as Louisville Central High School Magnet Career Academy, Central High School is a public high school in downtown Louisville, Kentucky, United States.

Seneca High School MCA: Seneca High School MCA (Magnet Career Academy) is a Louisville, Kentucky, USA, public school.  It is located at 3510 Goldsmith Lane, Louisville, Kentucky 40220, in the Hikes Point neighborhood and is part of Jefferson County Public Schools.

Central High School (Springfield, Missouri): Central High School is a high school located in uptown Springfield, Missouri.  The school was Springfield's first high school to be built.  Construction of the building was completed in 1893.  The first graduating class graduated a year later in 1894 consisting of two out of the 76 seniors that were enrolled.  The school was renamed Central High School after the construction of Springfield's second oldest high school, Parkview High School, in 1956.  Central's mascot is a Bulldog, named Pug by the students at the time of his creation.  Central is also the home to the Kiltie Drum and Bugle Corps.  This corps was created by Dr. Robert Ritchie Robertson in 1926, and has the distinction of being the first all-female Scottish pipe and drum corps in the country.  U.S. News & World Report ranked Central High School as the 4th best school in Missouri in 2011.

Austin Community Academy High School: Austin High School (now known as Austin College and Career Academy High School) is a public 4–year high school located at 231 North Pine Avenue in the Austin neighborhood on the west side of Chicago, Illinois, United States.  Operated by the Chicago Public Schools, Austin opened in 1876 and was named in honor of Henry W. Austin, a Chicago real estate developer In 2004, the online newsletter "Chicago-Catalyst. org" called it the yellow brick fortress.  Austin Polytech shared its campus with two smaller schools; Austin Business & Entrepreneurship Academy High and V.O.I.S.E. Academy High School.  After the 2015–2016 school year, the small schools converted into one school and was renamed Austin College and Career Academy High School.

Question: In which year was the basketball player who attended the school formally known as Louisville Central High School Magnet Career Academy born?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The full name of the basketball player."
    },
    "player_birth_year": {
      "type": "integer",
      "description": "The birth year of the basketball player."
    },
    "attended_school": {
      "type": "object",
      "properties": {
        "school_current_name": {
          "type": "string",
          "description": "The current name of the school attended by the player."
        },
        "school_formal_name": {
          "type": "string",
          "description": "The formal name of the school as mentioned in the question."
        },
        "school_location": {
          "type": "string",
          "description": "The city and state where the school is located."
        }
      },
      "required": [
        "school_current_name",
        "school_formal_name",
        "school_location"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "player_name",
    "player_birth_year",
    "attended_school"
  ],
  "additionalProperties": false
}
