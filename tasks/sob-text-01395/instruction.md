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
Encyclopedia of Appalachia: The Encyclopedia of Appalachia is the first encyclopedia dedicated to the region, people, culture, history, and geography of Appalachia.  Appalachia is a region of the United States named for the significant mountain system which stretches through fourteen states: Alabama, Georgia, Kentucky, Maryland, Massachusetts, Mississippi, New York, North Carolina, Ohio, Pennsylvania, South Carolina, Tennessee, Virginia and West Virginia.  The encyclopedia is 1,864 pages long and contains over 2,000 entries.  Produced by the Center for Appalachian Studies and Services at East Tennessee State University, Rudy Abramson and Dr. Jean Haskell, are the two main editors of the encyclopedia.  It was published in March 2006 by the University of Tennessee Press.

Jean Lipman-Blumen: Dr. Jean Lipman-Blumen is the Thornton F. Bradhshaw Professor of Public Policy and Professor of Organizational Behavior at Claremont Graduate University in Claremont, California.  She is an expert on leadership, achieving styles, crisis management, "hot groups" organizational behavior, and gender roles.  Prof. Lipman-Blumen is director and co-founder of CGU's Institute for Advanced Studies in Leadership.  She is president and co-founder, with the late Prof. Harold J. Leavitt, the Kilpatrick Professor of Organizational Behavior, at Stanford Graduate School of Business, of the Connective Leadership Institute (formerly the Achieving Styles Institute), a leadership development, research, and management consulting firm, in Pasadena, California.

Dr. Jean: Jean Rosenberg Feldman, (born in Milan, Tennessee, (1947--) 15, 1947 (age 70 ) ) better known as Dr. Jean, is a teacher, author, and musical artist.  She is well known for her children's learning songs.  Dr. Jean has a Ph.D. in Curriculum and Instruction, an M.A. in Early Childhood from Georgia State University, and a D.A.S.T from Emory University.  Dr. Jean has been educating for over 40 years and has created many resources for teachers in the classroom with their students.  She releases her songs under the record label, Music Design Record Company.

Joseph W. Bruno: Joseph W. Bruno (born July 6, 1955) is an American academic and former university administrator.  He became the 18th president of Marietta College on July 1, 2012.  Dr. Bruno took over for Dr. Jean A. Scott, who retired after 12 years.  Formerly, he was the Vice President for Academic Affairs at Wesleyan University (2006–2010), Dean of Natural Sciences and Mathematics at Wesleyan (2003–06) and worked at Wesleyan since 1984, beginning as a chemistry professor

Jean Malecki: Dr. Jean Marie Malecki is an American public health official who was among the first physicians to deal with a bioterrorism attack in the United States.  Dr. Malecki has been the Director of the Palm Beach County Health Department since 1991 and is the Chair of the Department of Preventive Medicine at Nova Southeastern University College of Osteopathic Medicine.

Jean Pierre Soulier: Dr. Jean Pierre Soulier (14 September 1915 – 18 January 2003) was a French physician and haematologist.  He was the General Director of Centre National de Transfusion Sanguine (CNTS) Paris and professor of haematology at the University of Paris, at the Necker Hospital for Sick Children.

Alta Partners: Alta Partners is a venture capital firm based in San Francisco, CA.  The company was founded in 1996 by Dr. Jean Deleage, Ph.D., who was also a founder of the venture capital firms Burr, Egan, Deleage & Co. (BEDCO) and Sofinnova, together with Garrett Gruener, a former general partner at BEDCO.

Jean Dunbabin: Dr. Jean Dunbabin is an honorary fellow of St Anne's College, University of Oxford.  Dunbabin specialises in medieval political communities in France c. 1000-c.1350, and in southern Italy and Sicily 1250-1310, and medieval political thought.  She is a fellow of the British Academy.

Emory University: Emory University is a private research university in metropolitan Atlanta, located in the Druid Hills section of DeKalb County, Georgia, United States.  The university was founded as Emory College in 1836 in Oxford, Georgia by the Methodist Episcopal Church and was named in honor of Methodist bishop John Emory.  In 1915, the college relocated to metropolitan Atlanta and was rechartered as Emory University.  The university is the second-oldest private institution of higher education in Georgia and among the fifty oldest private universities in the United States.  Emory is frequently cited as one of the world's leading research universities and one of the top institutions in the United States.

Jean Ellis: Dr. Jean Ellis (November 23, 1946 – May 15, 2006) was a 59-year-old emergency department physician who practiced the latter part of his career at St. Vincent Healthcare located in Billings, Montana and was nationally known for his accomplishments as a climber.

Question: In what city is the university from which Dr. Jean Rosenberg Feldman as a D.A.S.T.?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The full name of the person."
    },
    "degree_obtained": {
      "type": "string",
      "description": "The specific degree obtained by the person."
    },
    "university_details": {
      "type": "object",
      "properties": {
        "university_name": {
          "type": "string",
          "description": "The name of the university."
        },
        "university_city": {
          "type": "string",
          "description": "The city where the university is located."
        },
        "university_state": {
          "type": "string",
          "description": "The state where the university is located."
        }
      },
      "required": [
        "university_name",
        "university_city",
        "university_state"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_name",
    "degree_obtained",
    "university_details"
  ],
  "additionalProperties": false
}
