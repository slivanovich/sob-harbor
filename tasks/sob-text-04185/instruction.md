{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBrigham Young College: Brigham Young College was a college and high school in Logan, Utah.  It was founded by Brigham Young on 6 August 1877, 23 days before his death.  He deeded several acres of land to a board of trustees for the development of a college.  This was just two years after he founded Brigham Young Academy in Provo in 1875, which became Brigham Young University in 1903.\n\nBYU Creamery: The Brigham Young University Creamery is a grocery store for Brigham Young University students living in residence halls on campus.  Students may purchase food and other items using their Signature Card accounts (an on-campus debit card system) or traditional payment methods.  BYU Creamery has four locations in Provo, Utah: Creamery on Ninth East, Helaman Creamery, Wyview Creamery, and the Creamery Outlet.\n\nList of Brigham Young University–Idaho alumni: This list of Brigham Young University alumni includes notable graduates, non-graduate former students, and current students of Brigham Young University–Idaho (also known as BYU–Idaho or BYU–I), a four-year private college owned by The Church of Jesus Christ of Latter-day Saints (LDS Church) located in Rexburg, Idaho, United States that prior to 2001 was a two-year junior college known as Ricks College.  As of August 2008, BYU–Idaho/Ricks College has approximately 150,000 alumni.  Many of the alumni, in particular those before 2001, graduated with a two-year associate's degree or simply attended two years before moving on to another institution to complete their bachelor's degree.\n\nYork College of Pennsylvania: York College of Pennsylvania is a private, coeducational, 4-year college located in south central Pennsylvania that offers more than 50 baccalaureate majors in professional programs, the sciences, and humanities to its 4,600 full-time undergraduate students.  York also offers master's programs in business, education, and nursing, along with a doctoral program in nursing practice.\n\nList of Brigham Young University alumni: This list of Brigham Young University alumni includes notable graduates, non-graduate former students, and current students of Brigham Young University (BYU), a private, coeducational research university owned by The Church of Jesus Christ of Latter-day Saints (LDS Church) located in Provo, Utah, United States.  It is the oldest existing institution within the LDS Church Educational System, is America's largest religious university, and has the second-largest private university enrollment in the United States.  Approximately 98% of the 34,000 students at BYU are Mormon; two-thirds of its American students come from outside the state of Utah.  In addition to its undergraduate program, BYU offers graduate degrees in 47 departments and includes two graduate schools: the Marriott School of Management and the J. Reuben Clark Law School.  BYU has approximately 370,000 living alumni.\n\nGeorge H. Brimhall: George Henry Brimhall (December 9, 1852 – July 29, 1932) was President of Brigham Young University from 1904 to 1921.  After graduating from Brigham Young Academy, Brimhall served as principal of Spanish Fork schools and then as district superintendent of Utah County schools, finally returning to Brigham Young Academy.  In April 1904, Brimhall became president of the school, which had become Brigham Young University (BYU) in October 1903.  As President of BYU, Brimhall helped institute the collegiate program, departments for specific subjects, and an emphasis on religious learning.\n\nList of presidents of Brigham Young University: The following people have served as presidents of Brigham Young University and principals of Brigham Young Academy, which split to become Brigham Young University and Brigham Young High School in 1903.  This list does not include presidents of Brigham Young University-Hawaii or Brigham Young University–Idaho.\n\nBrigham Young University: Brigham Young University (BYU), sometimes referred to colloquially as The Y, is a private research university located in Provo, Utah, United States.  It is owned and operated by The Church of Jesus Christ of Latter-day Saints (LDS Church), and excluding online students, is the largest religious university and the third largest private university in the United States, with 33,363 on-campus students.  Approximately 99 percent of the students are members of the LDS Church, and one-third of its U.S. students are from Utah.\n\nChurch Educational System Honor Code: The Church Educational System (CES) Honor Code is a set of standards by which students and faculty attending a school owned and operated by The Church of Jesus Christ of Latter-day Saints (LDS Church) are required to live.  The most widely known university that is part of the Church Educational System (CES) that has adopted the honor code is Brigham Young University (BYU), located in Provo, Utah.  The standards are largely derived from codes of conduct of the LDS Church, and were not put into written form until the 1940s.  Since then, they have undergone several changes.  The CES Honor Code also applies for students attending BYU's sister schools Brigham Young University–Idaho, Brigham Young University–Hawaii, and LDS Business College.\n\nBrigham Young High School: Brigham Young High School was a private high school in Provo, Utah, United States, first known as Brigham Young Academy.  The school later became attached to Brigham Young University (BYU) with its official name being Brigham Young University High School, and commonly called B Y High.  It operated under the Church Educational System of The Church of Jesus Christ of Latter-day Saints (LDS Church).\n\nQuestion: Which has more students, Brigham Young University or York College of Pennsylvania?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"comparison_summary\": {\n      \"type\": \"string\",\n      \"description\": \"A summary statement of which university has more students.\"\n    },\n    \"universities\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the university.\"\n          },\n          \"student_count\": {\n            \"type\": \"integer\",\n            \"description\": \"The number of students at the university.\"\n          },\n          \"student_count_description\": {\n            \"type\": \"string\",\n            \"description\": \"A description clarifying the type of student count (e.g., on-campus, full-time undergraduate).\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"student_count\",\n          \"student_count_description\"\n        ],\n        \"additionalProperties\": false\n      },\n      \"description\": \"Details for each university involved in the comparison.\"\n    },\n    \"university_with_more_students\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the university that has more students.\"\n    }\n  },\n  \"required\": [\n    \"comparison_summary\",\n    \"universities\",\n    \"university_with_more_students\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "comparison_summary": {
        "type": "string",
        "description": "A summary statement of which university has more students."
      },
      "universities": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the university."
            },
            "student_count": {
              "type": "integer",
              "description": "The number of students at the university."
            },
            "student_count_description": {
              "type": "string",
              "description": "A description clarifying the type of student count (e.g., on-campus, full-time undergraduate)."
            }
          },
          "required": [
            "name",
            "student_count",
            "student_count_description"
          ],
          "additionalProperties": false
        },
        "description": "Details for each university involved in the comparison."
      },
      "university_with_more_students": {
        "type": "string",
        "description": "The name of the university that has more students."
      }
    },
    "required": [
      "comparison_summary",
      "universities",
      "university_with_more_students"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
