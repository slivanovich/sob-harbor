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
Limestone College: Limestone College is a private four-year, coeducational liberal arts college located in Gaffney, South Carolina.  Limestone College is a Christian non-denominational college with programs leading to the Bachelor of Arts, Bachelor of Science, Bachelor of Social Work, Associate of Arts, Associate of Science, and Masters in Business Administration (MBA) degrees.

WCXZ: WCXZ (740 AM) is a radio station licensed to serve Harrogate, Tennessee, USA.  The station is owned by Lincoln Memorial University, a private four-year co-educational liberal arts college.

Bennett College: Bennett College is a private four-year historically black liberal arts college for women located in Greensboro, North Carolina.  It was founded in 1873 as a normal school to educate freedmen and train both men and women as teachers.  Originally coed, in 1926 it became a four-year women's college.  It is one of two historically black colleges that enroll women only.  Today it serves roughly 780 undergraduate students.

Lincoln Memorial University: Lincoln Memorial University (LMU) is a private four-year co-educational liberal arts college located in Harrogate, Tennessee, United States.  LMU's 1000 acre campus borders on Cumberland Gap National Historical Park.  As a whole, LMU is accredited by the Southern Association of Colleges and Schools (SACS).  In December 2014, the law school received provisional accreditation by the American Bar Association.

Macalester College: Macalester College ( ) is a private, coeducational liberal arts college located in Saint Paul, Minnesota, US.  It was founded in 1874 as a Presbyterian-affiliated but nonsectarian college.  Its first class entered September 15, 1885.  Macalester is exclusively an undergraduate four-year institution and enrolled 1,978 students in the fall of 2013 from 50 U.S. states and 90 countries.  In 2015, "U.S. News & World Report" ranked Macalester as tied for the 23rd best liberal arts college in the United States, 6th for undergraduate teaching at a national liberal arts college, and 19th for best value at a national liberal arts college.

Bacone College: Bacone College, formerly Bacone Indian University, is a private four-year liberal arts college in Muskogee, Oklahoma, United States.  Founded in 1880 as the Indian University by Almon C. Bacone, Bacone College is the oldest continuously operated institution of higher education in Oklahoma.  The college has strong historic ties to various tribal nations, including the Cherokee Nation and the Muscogee (Creek) Nation, and also to the American Baptist Churches USA.

Mark Powell (novelist): Mark Powell (born 1976) is an American novelist.  He is the author of the novels "The Dark Corner", "Blood Kin" and "Prodigals" (all with the University of Tennessee Press), as well as "The Sheltering" (Story River Books, an imprint of University of South Carolina Press).  He has received fellowships from the National Endowment for the Arts and the Breadloaf Writers' Conference.  Educated at The Citadel, The University of South Carolina, and Yale Divinity School, Powell teaches in the English Department at Appalachian State University in Boone, North Carolina.  He repeatedly serves as the fiction workshop leader for the Hindman Settlement School's Appalachian Writers Workshop and the Mountain Heritage Literary Festival at Lincoln Memorial University.  Powell's work has established him in the southern Appalachian tradition alongside writers such as Pamela Duncan, Silas House and Ron Rash.

Liberal arts college: A liberal arts college is a college with an emphasis on undergraduate study in the liberal arts and sciences.  A liberal arts college aims to impart a broad general knowledge and develop general intellectual capacities, in contrast to a professional, vocational, or technical curriculum.  Students in a liberal arts college generally major in a particular discipline while receiving exposure to a wide range of academic subjects, including sciences as well as the traditional humanities subjects taught as liberal arts.  Although it draws on European antecedents, the liberal arts college is strongly associated with American higher education, and most liberal arts colleges around the world draw explicitly on the American model.

Lincoln College (Illinois): Lincoln College (chartered Lincoln University) is a private, independent liberal arts college located in Lincoln, Illinois.  Lincoln College is a hybrid college offering both two-year and four-year degree programs for its students.  Lincoln College was established in 1865 by the Cumberland Presbyterian Church, but is now independent and has no formal church affiliation.  There were a few sites that were looked at as possibilities, and in December 1864, the site of Lincoln was selected.  Due to the Civil War, the denomination wanted to create a college in the North because the denomination's other schools were located in the South.  At this same time a movement started in the new community of Lincoln to start a college.  On February 6, 1865, the Illinois General Assembly granted the charter that established the university.  President Lincoln was aware the school would be named after him.  Lincoln University was the first institution named for Abraham Lincoln and the only one during his lifetime.  The groundbreaking for University Hall, the first college building, was held on the birthday of Abraham Lincoln, which was six days after the charter had been granted.  By September 1866, University Hall's construction was completed.  In November 1866, the college opened its doors to men and women alike.  In 1868, there were three people who received their degrees.

Gustavus Adolphus College: Gustavus Adolphus College ( ) is a private, coeducational liberal arts college.  A four-year, residential institution, Gustavus Adolphus College was founded in 1862 by Swedish Americans and is affiliated with the Evangelical Lutheran Church in America.  To this day the school retains Swedish and Lutheran heritage.  The premier event on campus is the annual Nobel Conference, which features Nobel Laureates and other scholars explaining their expertise to a general audience.  In 2015, "U.S. News & World Report" ranked Gustavus as the 64th best liberal arts college in the United States.  The college is ranked No. 38 for liberal arts colleges on Payscale's 2016-17 list of highest-paid graduates.

Question: American novelist, Mark Powell, is the author of the the novel "The Dark Corner", and serves as what for the private four-year co-education liberal arts college, Lincoln Memorial University?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "author_name": {
      "type": "string",
      "description": "The name of the American novelist."
    },
    "novel_title": {
      "type": "string",
      "description": "The title of the novel written by the author."
    },
    "college_name": {
      "type": "string",
      "description": "The name of the college mentioned in the question."
    },
    "college_attributes": {
      "type": "object",
      "properties": {
        "is_private": {
          "type": "boolean",
          "description": "Indicates if the college is private."
        },
        "is_four_year": {
          "type": "boolean",
          "description": "Indicates if the college is a four-year institution."
        },
        "is_coeducational": {
          "type": "boolean",
          "description": "Indicates if the college is coeducational."
        },
        "college_type": {
          "type": "string",
          "description": "The type of college, e.g., liberal arts."
        },
        "location": {
          "type": "string",
          "description": "The location of the college."
        }
      },
      "required": [
        "is_private",
        "is_four_year",
        "is_coeducational",
        "college_type",
        "location"
      ],
      "additionalProperties": false
    },
    "author_role_at_college": {
      "type": "string",
      "description": "The role of the author at the specified college."
    }
  },
  "required": [
    "author_name",
    "novel_title",
    "college_name",
    "college_attributes",
    "author_role_at_college"
  ],
  "additionalProperties": false
}
