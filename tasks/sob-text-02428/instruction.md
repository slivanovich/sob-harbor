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
Hillary Rodham senior thesis: In 1969, Hillary Rodham wrote a 92-page senior thesis for Wellesley College about community organizer Saul Alinsky entitled "There Is Only the Fight . . . : An Analysis of the Alinsky Model."  The thesis is now available.

Alan Schechter: Alan Schechter (born 1936) is a Professor Emeritus of Political Science at Wellesley College in Massachusetts.  He was educated at Amherst College, where he received his AB, and at Columbia University, where he earned his PhD.  He is a distinguished and award-winning political scientist.  He was also Hillary Rodham's advisor during her years at Wellesley College and supervised her senior thesis; Susan Estrich's book "The Case for Hillary Clinton" mentions her experience also writing an honors thesis for Professor Schechter (at a different time).  He remains involved with the college, running the Wellesley in Washington internship program, in which Rodham participated as a student and which continues to send approximately twenty women to Washington for internships each summer.  Professor Schechter is the former Chairman, Vice-Chairman, and member of the J. William Fulbright Foreign Scholarship Board (Fulbright Program), a Presidential appointment.

Wellesley, Massachusetts: Wellesley is a town in Norfolk County, Massachusetts, United States.  Wellesley is part of Greater Boston.  The population was 27,982 at the time of the 2010 census.  Wellesley has the 5th highest median household and family incomes in all of Massachusetts.  It is best known as the home of Wellesley College, Babson College, and a campus of Massachusetts Bay Community College.

Wellesley College Botanic Gardens: The Wellesley College Botanic Gardens (22 acres) are botanical gardens located on the campus of Wellesley College in Wellesley, Massachusetts.  They are open daily without charge.

Wellesley College: Wellesley College is a private women's liberal arts college located west of Boston in the town of Wellesley, Massachusetts, United States.  Founded in 1870 by Henry and Pauline Durant, it is a member of the original Seven Sisters Colleges.  Wellesley is home to 56 departmental and interdepartmental majors spanning the liberal arts, as well as over 150 student clubs and organizations.  The college is also known for allowing its students to cross-register at Massachusetts Institute of Technology, Brandeis University, Babson College and Franklin W. Olin College of Engineering.  Wellesley athletes compete in the NCAA Division III New England Women's and Men's Athletic Conference.

List of Stitchers episodes: "Stitchers" is an American science fiction crime drama series created by Jeffrey Alan Schechter.  The series follows Kirsten (Emma Ishta), who has been recruited into a government agency to be "stitched" into the memories of people recently deceased to investigate murders and mysteries that otherwise would have gone unsolved.  Cameron (Kyle Harris), a brilliant neuroscientist, assists Kirsten in the secret program headed by Maggie (Salli Richardson-Whitfield), a skilled covert operator.  The program also includes Linus (Ritesh Rajan) a bioelectrical engineer and communications technician.  Camille (Allison Scagliotti), Kirsten's roommate and a computer science graduate student, is also recruited to assist Kirsten as a "stitcher".

Jeffrey Alan Schechter: Jeffrey Alan Schechter (usually credited as Jeff Schechter) is a screenwriter whose work has been nominated for two Emmy awards, a Writers Guild of America award, and a Writers Guild of Canada award.  His writing credits include "Strange Days at Blake Holsey High", "Overruled! ", the Disney Channel original film "Brink! ", "" and "Dennis the Menace Strikes Again".  In 2015, he created the ABC Family science fiction crime drama "Stitchers".

Wellesley College Senate bus: The Wellesley College Senate bus is a shuttle bus service that connects Wellesley College to the Massachusetts Institute of Technology and Harvard University.

Davis Scholar: The Davis Degree Program at Wellesley College is a degree program serving women who are older than traditional college-age students.  These students are called "Davis Scholars" and are fully integrated into the Wellesley community; they take the same classes as traditional students and can choose to live on campus.  According to the Wellesley web site, Davis Scholars' "diverse backgrounds, experiences and perspectives enrich the lives of the whole student body."

Whitin Observatory: Whitin Observatory is an astronomical observatory owned and operated by Wellesley College.  Built in 1900, with additions in 1906, 1967, and 20102011, it is located in Wellesley, Massachusetts and named after Wellesley College trustee Mrs. John Crane Whitin (Sarah Elizabeth Whitin) of Whitinsville, who donated the funds for the observatory.  Astronomer Sarah Frances Whiting was the first director of the new Wellesley College Astronomy Department.

Question: Alan Schechter is Professor at Wellesley College and supervised what 92-page paper for a former student?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "thesis_title": {
      "type": "string",
      "description": "The full title of the senior thesis."
    },
    "page_count": {
      "type": "integer",
      "description": "The number of pages in the thesis."
    },
    "student_details": {
      "type": "object",
      "properties": {
        "student_name": {
          "type": "string",
          "description": "The name of the student who wrote the thesis."
        },
        "college_name": {
          "type": "string",
          "description": "The college where the student wrote the thesis."
        }
      },
      "required": [
        "student_name",
        "college_name"
      ],
      "additionalProperties": false
    },
    "advisor_details": {
      "type": "object",
      "properties": {
        "advisor_name": {
          "type": "string",
          "description": "The name of the professor who supervised the thesis."
        },
        "advisor_role": {
          "type": "string",
          "description": "The role of the professor in relation to the thesis."
        }
      },
      "required": [
        "advisor_name",
        "advisor_role"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "thesis_title",
    "page_count",
    "student_details",
    "advisor_details"
  ],
  "additionalProperties": false
}
