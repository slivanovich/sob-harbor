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
Education in Kansas: Education in Kansas is governed at the primary and secondary school level by the Kansas State Board of Education.  The state's public colleges and universities are supervised by the Kansas Board of Regents.

List of Emporia State University people: Emporia State University is a public university in Emporia, Kansas, United States, east of the Flint Hills.  Established in March 1863 and originally known as the Kansas State Normal School, Emporia State is the third oldest public university in the state of Kansas.  Emporia State is one of six public universities governed by the Kansas Board of Regents.

Kansas City Kansas Community College: Kansas City Kansas Community College (KCKCC) is a public two year community college located in Kansas City, Kansas, United States.  The college is accredited by the Higher Learning Commission, a commission of the North Central Association and the Kansas Board of Regents.

George Karras: George Karras (c. 1929 – March 6, 2017) was an American football player, coach, scout and executive.  He served as the head football coach at Wichita State University from 1965 to 1966, compiling a record of 4–15.  He left Wichita in 1966 to be the line coach at the University of Massachusetts Amherst.  He was previously the defensive coach there before coming to Wichita in 1964.  Karras played college football as a guard at Villanova University from 1953 to 1955.  Karras attended high school in Etna, Pennsylvania.  He later worked for the United Scouting Combine and as the chief scout in the Northeastern United States for the Denver Broncos of the National Football League (NFL).  In 1987, he was named the director of pro personnel for the NFL's Los Angeles Raiders.  Karras died on March 6, 2017.

President of Emporia State University: The President of Emporia State University is the chief administrator of the university.  Each is appointed by and is responsible to the other members of that body, who delegate to him or her the day-to-day running of the university.  The president of Emporia State is selected by the Kansas Board of Regents, the governing board for public universities in the state of Kansas, after a nationwide search.

Emporia State University: Emporia State University, often referred to as Emporia State or ESU, is a public university in Emporia, Kansas, United States, east of the Flint Hills.  Established in March 1863 and originally known as the Kansas State Normal School, Emporia State is the third oldest public university in the state of Kansas.  Emporia State is one of six public universities governed by the Kansas Board of Regents.

North Central Kansas Technical College: The Kansas Board of Regents governs six universities and coordinates and supervises Kansas’ 19 community colleges, five technical colleges, and five technical schools.  Institutions that wish to deliver approved programs or courses within the service area governed by the North Central Kansas Technical College Board of Trustees.

Wichita State University: Wichita State University (WSU) is a public research university in Wichita, Kansas, United States.  It is the third-largest university governed by the Kansas Board of Regents.

Fort Hays State University: Fort Hays State University (FHSU) is a public, co-educational university located in Hays, Kansas, United States.  It is the third-largest of the six state universities governed by the Kansas Board of Regents, with an enrollment of approximately 11,200 students (4,000 undergraduate, 1,200 graduate, and 6,000 online students).

Pittsburg State University: Pittsburg State University, also called Pitt State or PSU, is a public university with approximately 7,479 students (6,000 undergraduates and 1,400 graduate students) located in Pittsburg, Kansas, United States.  A large percentage of the student population consists of residents within the Pittsburg region; the gender proportion is relatively equal.  Almost 89% of the students are Americans.  Pitt State also has a 19:1 student-to-faculty ratio.  It is a member of the Kansas Board of Regents.  Currently, it has an endowment of around $74,000,000.  The student newspaper of Pittsburg State University is the "Collegio."

Question: Who served as a coach for the third-largest university governed by the Kansas Board of Regents?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "coach_name": {
      "type": "string",
      "description": "The name of the coach."
    },
    "university_info": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the university."
        },
        "governing_body": {
          "type": "string",
          "description": "The body that governs the university."
        },
        "size_description": {
          "type": "string",
          "description": "How the university's size was described in relation to its governing body."
        }
      },
      "required": [
        "name",
        "governing_body",
        "size_description"
      ],
      "additionalProperties": false
    },
    "coaching_details": {
      "type": "object",
      "properties": {
        "role": {
          "type": "string",
          "description": "The coaching role held at the university."
        },
        "start_year": {
          "type": "integer",
          "description": "The start year of the coaching tenure."
        },
        "end_year": {
          "type": "integer",
          "description": "The end year of the coaching tenure."
        }
      },
      "required": [
        "role",
        "start_year",
        "end_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "coach_name",
    "university_info",
    "coaching_details"
  ],
  "additionalProperties": false
}
