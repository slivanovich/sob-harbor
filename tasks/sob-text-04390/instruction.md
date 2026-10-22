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
Carl W. McIntosh: Carl Weston McIntosh, Jr. (December 1, 1914 – January 19, 2009) was an American professor of forensics and acting.  He served as president of Idaho State College (now Idaho State University) from 1947 to 1959.  He was acting executive dean when the college achieved its independence from the University of Idaho in March 1947, and he elevated it into a four-year, bachelor's degree-granting institution in December 1948.  He left Idaho in 1959 to become president of Long Beach State College (now known as California State University, Long Beach).  He oversaw the college's rapid growth from less than 10,000 students to 28,000 and two name changes (to California State College at Long Beach in 1964 and to California State College, Long Beach in 1968).  He was named president of Montana State University in 1970.  He established the university's nursing and pre-medical education programs and completed its first football stadium and creative arts complex, but also faced a years of fiscal austerity imposed by the state legislature.  He retired in 1977.

Chico State Wildcats: The Chico State Wildcats (also CSU Chico Wildcats and Cal State Chico Wildcats) are the athletic teams that represent California State University, Chico, located in Chico, California, in NCAA Division II intercollegiate sports.  The Wildcats compete as an associate member of the California Collegiate Athletic Association for all 13 varsity sports.  Since 1998, Chico State’s athletic teams have won 99 NCAA Championship berths, 40 CCAA titles, 24 West Region titles, and 15 National titles.  The school finished third in the 2004–2005 NACDA Director's Cup.

California State University, Chico: California State University, Chico (also known as CSU Chico or Chico State), is the second-oldest campus in the 23-campus California State University system.  It is located in Chico, California, about ninety miles north of Sacramento.  As of the Fall 2016 semester, the university had a total enrollment of 17,557 students.  The university offers 126 types of bachelor's degrees, 35 types of master's degrees, and four types of teaching credentials.  The university does not confer doctoral degrees.

Associated Students, Chico: Associated Students, Chico (AS.)  is the student government at California State University, Chico.  With assets of over $13 million and annual revenue over $30 million, Associated Students, Chico is one of the largest non-profit organizations in Northern California Associated Students, Chico is a 501(c)(3) nonprofit public-benefit corporation with 16,934 members.  The organization owns and operates several student services on-campus including all vending machines, and foodservices, as well as the campus bookstore.  The students of CSU Chico also own their own student union building named the Bell Memorial Union which houses the "Marketplace Cafe", the "AS Bookstore", and the student government offices.

CSUSB College of Natural Sciences: The California State University, San Bernardino College of Natural Sciences is the San Bernardino region's largest center for science education and research.  Comprising nine departments and various specialties, the College offers bachelor's and master's, as well as curricula for pre-professional students in medicine, veterinary medicine and dentistry.  The College strives to produce scientifically educated graduates who possess both a fundamental understanding of their fields and the essential professional skills needed by local and regional industries.  The College provides scientific literacy for all California State University, San Bernardino graduates as well as participating in the training of future mathematics and science teachers.

CSUSB College of Social and Behavioral Sciences: The California State University, San Bernardino College of Social and Behavioral Sciences is one of six academic colleges at CSUSB located in San Bernardino, California, United States.  Comprising ten departments/schools and various specialties, the College offers bachelor's and master's.  The College strives to produce educated graduates who possess both a fundamental understanding of their fields and the essential professional skills needed by local and regional industries.  The College provides business information for all California State University, San Bernardino graduates.  The College has many accredited programs.

Nettleton Stadium: Nettleton Stadium is a baseball stadium in Chico, California on the campus of California State University, Chico.  It is the home field for the CSU Chico Baseball team, the Wildcats, and the Chico Heat collegiate wood bat league team.  It also served as the former home of the now-defunct Chico Heat and Chico Outlaws professional baseball teams.  It holds 4,200 people.  The stadium was named for majority owner of the Chico Heat, Steve Nettleton and his wife Kathy Nettleton.  The Nettleton family donated the 4.5 million dollar facility to CSU.

Institute of Space Technology: Institute of Space Technology (also known as IST) is a public research university located in Islamabad, Pakistan focused on the study of astronomy, aerospace engineering and astronautics.

Cal Poly Pomona College of Environmental Design: The Cal Poly Pomona College of Environmental Design (CENV) is a college part of the California State Polytechnic University, Pomona (Cal Poly Pomona).  The college houses over 1,600 students; making it one of largest environmental design programs in the United States.  The college offers bachelor's degrees in five departments, as well as three master's degree programs.  It is the only academic unit within the California State University system to be associated with a Pritzker Prize laureate (often referred to as "The Nobel Prize in Architecture").

Gayatri Vidya Parishad College of Engineering: The Gayatri Vidya Parishad College of Engineering(Autonomous) or GVP ("G"ā"yatri Vidy"ā" Parishad)" is a private, co-education engineering institute established in the year 1996.  The educational trust is formed,managed and promoted by academicians, philanthropists and technocrats in Visakhapatnam, India.  The college offers instruction to 1200 undergraduate students in seven branches of Engineering: Chemical, Civil, Computer science and Engineering, Electronics and communication engineering, Electrical engineering, Mechanical engineering and Information Technology(IT).  The institution also offers Master of Computer Applications program affiliated to Jawaharlal Nehru Technological University, Kakinada.  All the under graduation programs are accredited by NBA in 2006 The college also offers 13 Postgraduate education programs, where the candidates are selected based on the marks secured in Graduate Aptitude Test in Engineering.  The institute is accredited by All India Council for Technical Education(AICTE) and re-accredited by National Assessment and Accreditation Council by 'A' grade with a CGPA of 3.47/4.00.  Along with this, the college is sanctioned the extension of autonomy until 2020 by University Grants Commission (India).

Question: What college offers more programs California State University, Chico or the Institute of Space Technology? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "college_with_more_programs": {
      "type": "string",
      "description": "The name of the college identified as offering more programs."
    },
    "colleges_information": {
      "type": "array",
      "description": "Detailed information for each college involved in the comparison.",
      "items": {
        "type": "object",
        "properties": {
          "college_name": {
            "type": "string",
            "description": "The full name of the college."
          },
          "degrees_offered": {
            "type": "object",
            "description": "Specific counts of different types of degrees and credentials offered, if available.",
            "properties": {
              "bachelor_degrees": {
                "type": "integer",
                "description": "The number of bachelor's degrees offered."
              },
              "master_degrees": {
                "type": "integer",
                "description": "The number of master's degrees offered."
              },
              "teaching_credentials": {
                "type": "integer",
                "description": "The number of teaching credentials offered."
              },
              "total_degree_programs": {
                "type": "integer",
                "description": "The total combined number of bachelor's, master's, and teaching credentials offered."
              }
            },
            "required": [
              "bachelor_degrees",
              "master_degrees",
              "teaching_credentials",
              "total_degree_programs"
            ],
            "additionalProperties": false
          },
          "focus_areas": {
            "type": "array",
            "description": "Areas of study or focus mentioned for the college, if specific program counts are not provided.",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "college_name"
        ],
        "additionalProperties": false
      }
    },
    "comparison_basis": {
      "type": "string",
      "description": "Explanation of how the comparison was made, especially if data for one college is less specific."
    }
  },
  "required": [
    "college_with_more_programs",
    "colleges_information",
    "comparison_basis"
  ],
  "additionalProperties": false
}
