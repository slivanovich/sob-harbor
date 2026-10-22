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
Azfar Hussain: Azfar Hussain (Bengali: আজফার হোসেন ) is a Bangladeshi theorist, critic, academic, bilingual writer, poet, translator, and activist.  He is Associate Professor of Liberal Studies/Interdisciplinary Studies at Grand Valley State University in Michigan, and Vice-President of the Global Center for Advanced Studies (GCAS) and Honorary GCAS Professor of English, World Literature, and Interdisciplinary Studies.  He taught English, World Literature, Ethnic Studies, and Cultural Studies at Washington State University, Bowling Green State University, and Oklahoma State University; while, in Bangladesh, he taught English at Jahangirnagar University and North South University.  He also worked as Scholar-in-Residence at the University of Liberal Arts Bangladesh.  He is an advisory editor of "Rhizomes: Cultural Studies in Emerging Knowledge".  He is also an editorial board member of the Bengali journals "Natun Diganta" and "Sarbajonakotha".

Colorado Christian University: Colorado Christian University (CCU) is a private, interdenominational Christian liberal arts university in Lakewood, Colorado in the United States.  CCU was founded in 1914 as the Denver Bible Institute.

Christian M. M. Brady: Christian M. M. Brady (born 1968) is an American scholar who specializes in biblical literature, rabbinic literature, and the targumim, especially Targum Lamentations and Targum Ruth.  He is the inaugural Dean of the Lewis Honors College at the University of Kentucky (2017) and was Dean of the Schreyer Honors College from 2006-2016.  He was formerly Associate Professor of Classical Studies and Jewish Studies at Tulane University.  His administrative roles at Tulane included, Associate Director of the Jewish Studies Program (1997-1998), Director of the Jewish Studies Program (1998-2003), and Director of the Honors Program (2004–2006).

Daniel Patte: Daniel Patte (born 1939) is a French American biblical scholar and author.  Patte has been Professor of Religious Studies and of New Testament & Early Christianity at Vanderbilt University since 1971.  He studied in both European and American schools: following his Baccalauréat in Philosophy (Grenoble, 1958) he received a Baccalauréat en Théologie (1960) from the Faculté de Théologie Protestante, Montpellier, France; Licence en Théologie, (équivalent to M.Th, 1964) from the University of Geneva, Switzerland, and a Th.D.  (1971) from the Jewish Christian Center at Chicago Theological Seminary.  Patte is one of the most engaging biblical scholars, calling for an ethics of biblical interpretation that involves acknowledging the contextual character of any interpretation of the Bible, as his numerous books and articles indicate.  In the 1970s-1980s Patte pioneered structural criticism in biblical studies, serving as a long time General Editor of "Semeia", a journal published by the Society of Biblical Literature (1992–98).  Patte also chaired programs of the Society of Biblical Literature, including on Semiotic and Exegesis, Romans Through History and Cultures, and, since 2007, Contextual Biblical Interpretation.  With colleagues of the Society of Biblical Literature and of the American Academy of Religion involved in these programs, he envisioned and edited The Cambridge Dictionary of Christianity (2010).

Allen Wikgren: Wikgren earned his Bachelor of Arts degree (in Greek) in 1928, his Master of Arts degree in 1929 and his Ph.D. in 1932, all from the University of Chicago.  His doctoral dissertation was entitled "A Comparative Study of the Theodotionic and Septuagint Versions of Daniel".  An ordained minister in the mainline Northern Baptist Convention, Wikgren then served as a minister at First Baptist Church in Belleville, Kansas and as a professor of New Testament literature at Kansas City Baptist Theological Seminary (now Central Baptist Theological Seminary in Shawnee, Kansas) (1935-1937) and of biblical literature and classics at Ottawa University in Ottawa, Kansas (1937-1940) before returning to Chicago to join the University of Chicago Divinity School as the J. M. Powis Smith Instructor in 1940.  At Chicago, Wikgren was a member of the Department of New Testament and Early Christian Literature in the university's Division of the Humanities, a department which he would later serve as chair.  His colleagues in New Testament studies during his long tenure administering the department (1953-1972) included figures such as Norman Perrin, Robert M. Grant and Markus Barth.

Oklahoma Christian University: Oklahoma Christian University (OC) is a private comprehensive coeducational Christian liberal arts university founded in 1950 by members of the Churches of Christ.  Oklahoma Christian University is located on a 240 acre campus in Oklahoma City, in the U.S. state of Oklahoma.  Enrollment for the fall 2014 semester was a record 2,479 students.  OC is ranked among the best "Regional Universities" in the 16-state West region by U.S. News and World Report and is listed by the Princeton Review as one of the best "Best Western Colleges."  The University reported a 45% acceptance rate for fall 2012 applicants.

Reinhardt University: Reinhardt University is a comprehensive liberal arts university located in Waleska, Georgia, United States, with an off-campus center in Alpharetta.  Select programs are also offered in Cartersville, Marietta, and Canton, and online.  Reinhardt is affiliated with the United Methodist Church.

Lee University: Lee University is a private University in Cleveland, Tennessee, historically affiliated with the Church of God (Cleveland, Tennessee), an evangelical Christian denomination.  Lee began as the Church of God Bible Training School in 1918, a small Bible institute of twelve students and one teacher.  The school grew and became Lee College, with a Bible college and junior college on its current site, in 1948.  Twenty years later, Lee received accreditation by the Southern Association of Colleges and Schools as a four-year liberal arts college.  In 1997, Lee made the transition from college to comprehensive liberal arts university granting graduate degrees.  The university is divided into five colleges and schools: the College of Arts & Sciences, the Helen DeVos College of Education, the School of Music, the School of Nursing, and the School of Religion.  The university also offers online degrees through the Division of Adult Learning.  Lee University is named for F.J. Lee, the institution's second president.

Brad H. Young: Bradford Humes Young, also known as Brad Young, is a professor of Biblical Literature in Judeo Christian Studies at the Graduate Department of Oral Roberts University (ORU).  He is also founder and president of the Gospel Research Foundation, Inc.

Oral Roberts University: Oral Roberts University (ORU), based in Tulsa, Oklahoma, in the United States, is an interdenominational, Christian, comprehensive liberal arts university with 4,000 students.  Founded in 1963, the university is named after its founder, evangelist Oral Roberts, and accredited by the Higher Learning Commission of the North Central Association of Colleges and Schools (NCA).

Question: Bradford Humes Young, also known as Brad Young, is a professor of Biblical Literature in Judeo Christian Studies at the Graduate Department of which university, based in Tulsa, Oklahoma, in the United States, is an interdenominational, Christian, comprehensive liberal arts university?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "professor_name": {
      "type": "string",
      "description": "The full name of the professor."
    },
    "university_name": {
      "type": "string",
      "description": "The name of the university where the professor teaches."
    },
    "university_location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string"
        },
        "state": {
          "type": "string"
        },
        "country": {
          "type": "string"
        }
      },
      "required": [
        "city",
        "state",
        "country"
      ],
      "additionalProperties": false
    },
    "university_characteristics": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Key characteristics describing the university."
    },
    "department": {
      "type": "string",
      "description": "The specific department or graduate department where the professor is employed."
    }
  },
  "required": [
    "professor_name",
    "university_name",
    "university_location",
    "university_characteristics",
    "department"
  ],
  "additionalProperties": false
}
