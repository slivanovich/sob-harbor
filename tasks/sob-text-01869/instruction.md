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
Hossein Sadri: Dr. Hossein Sadri (born October 9, 1979) is an Iranian architect, critic and activist.  He is currently working as an associate professor of architecture at Girne American University where he was holding the position of the dean of the Faculty of Architecture, Design & Fine Arts between 2012-2016 He studied architecture and received his Master of Science degree at Islamic Azad University of Tabriz in 2005.  He completed his Ph.D. studies at Gazi University in 2010 with a TUBITAK Ph.D.  Fellowship., His Ph.D. dissertation entitled Architecture and Human Rights was an interdisciplinary studies and the first thesis which introduced the main motivation of human rights in the field of architecture.  He is one of the founding members of AUMME (Architecture and Urbanism in the Mediterranean and the Middle East), the regional academic and professional network in the field of architecture and the chair of its 2nd conference in 2014.  As the chair of the second CAUMME-Contemporary Architecture and Urbanism in the Mediterranean and the Middle-East International Conference, he introduced the concept of Post-Professionalism in the field of architecture.

M. Jaffar-ur-Rehman: He topped Quaid-i-Azam University by setting an all-time Computer Science Department record of a cumulative grade point average (CGPA) of 4.9 on a scale of 5.0.  In result, he was awarded the Quaid-e-Azam Scholarship for higher studies abroad, which he used to receive his Master of Science (M.Sc) degree and his Ph.D. in computer science in the United States.  He completed his M.Sc.  in just one year at the University of Pennsylvania by securing a CGPA of 3.9 on a scale of 4.0.  He taught in Australia for around three years during his Ph.D.  He came back to Pakistan after fully completing his Ph.D., where he taught at Quaid-e-Azam University, Bahauddin Zakariya University, Lahore University of Management Sciences (LUMS), and then Mohammad Ali Jinnah University.

John L. McNulty: The Very Right Reverend Monsignor John L. McNulty, Ph.D., (b. 1898) was an American Roman Catholic Domestic prelate and the 13th President of Seton Hall University.  McNulty received an A.B. (1921) and an M.A. (1922) from Seton Hall.  He received his Ph.D. from NYU in 1935 and a Dipl.  from d’ Écoles Supérieures at the Lille Catholic University in 1937.  McNulty was ordained a priest of the Roman Catholic Church in 1925.  He was an educator at Seton Hall University from 1928 and its president from 1949 - 1959.  McNulty was invested as a Domestic Prelate of His Holiness Pius XII in 1950.  Seton Hall University’s McNulty Hall, which is the University’s Technology and Research Center containing the famed “Atomic Wall” artwork depicting the gift of scientific knowledge from man to god, is named for the Right Reverend Dr. John McNulty.  Monsignor John Laurence McNulty established Seton Hall University’s Institute of Far Eastern Studies in 1951 in the midst of the Korean War.

Li Feng (sinologist): Li Feng (; born 1962), or Feng Li, is a professor of Early Chinese History and Archaeology at Columbia University, where he is director of graduate studies for the Department of East Asian Languages and Culture.  He received his MA in 1986 from the Institute of Archaeology, Chinese Academy of Social Sciences, and his Ph.D. in 2000 from the University of Chicago.  He also did Ph.D. work in the University of Tokyo (1991).  He is both a field archaeologist and an historian of Early China with primary interest in bronze inscriptions of the Shang-Zhou period.  Li founded the Columbia Early China Seminar in 2002, and directed Columbia’s first archaeological field project in China, in the Shandong Peninsula, in 2006-2011.

Taede A. Smedes: Taede Anne Smedes (born July 3, 1973 in Drachten) is a Dutch philosopher of religion.  He received a Ph.D degree from the University of Groningen in 2004 for a thesis on "Avoiding Balaam's Mistake: Exploring Divine Action in an Age of Scientism".

University of Groningen: The University of Groningen (abbreviated as UG; Dutch: "Rijksuniversiteit Groningen" , abbreviated as "RUG") is a public research university in the city of Groningen in the Netherlands.  The university was founded in 1614 and is one of the oldest universities in the Netherlands as well as one of its largest.  Since its inception more than 200,000 students have graduated.  It is a member of the distinguished international Coimbra Group of European universities.

Herman Quirmbach: Herman C. Quirmbach, Ph.D. (born October 6, 1950) is the Iowa State Senator from the 23rd District.  A Democrat, he has served in the Iowa Senate since 2003 and served on the Ames City Council from 1995 to 2003.  He received his B.A. from Harvard College and his M.A. and Ph.D. from Princeton University, the Ph.D. in 1983, and is an associate professor of economics at Iowa State University.  

Anil Nerode: Anil Nerode (born 1932) is an American mathematician.  He received his undergraduate education and a Ph.D. in mathematics from the University of Chicago, the latter under the directions of Saunders Mac Lane.  He enrolled in the Hutchins College at the University of Chicago in 1947 at the age of 15, and received his Ph.D. in 1956.  His Ph.D. thesis was on an algebraic abstract formulation of substitution in many-sorted free algebras and its relation to equational definitions of the partial recursive functions.

Anna Krylov: Anna Krylov is the Gabilan Distinguished Professor in Science and Engineering and a Professor of Chemistry at the University of Southern California (USC) working in the area of theoretical and computational quantum chemistry.  Born in Donetsk, Ukraine (May 6, 1967), Krylov received her M.Sc.  (with honors) in Chemistry from Moscow State University and later her Ph.D. (summa cum laude) from The Hebrew University of Jerusalem, working under the supervision of Professor Robert Benny Gerber.  Her Ph.D. research at the Fritz Haber Center focused on molecular dynamics in rare gas clusters and matrices.  Upon completing her Ph.D. in 1996, she joined the group of Prof. Martin Head-Gordon at the University of California, Berkeley as a postdoctoral research associate, where she became involved with electronic structure method development.  In 1998, she joined the Department of Chemistry at USC.

Levette J. Davidson: Levette J. Davidson was a nationally acclaimed expert in folklore, especially that of Colorado and the West.  He was born in Eureka, Illinois May 16, 1894, one of four children.  Because his grand uncle was past-President of Eureka College, a Christian seminary, Davidson was "reared in the school's shadow" with the option of becoming "either a teacher or a preacher."  He chose teaching and was awarded his B.A. from Eureka in 1915.  A year later he received his A.M. degree from the University of Illinois where he received Phi Beta Kappa honors.  In 1917 he earned his M.A. in social science and history at Harvard University.  __During World War I, he served with the Tenth Infantry of the Forty-Sixth Division and also served as an army sergeant in Intelligence.  Davidson and his wife Mary, also a graduate of Eureka, were married in 1918.  At the end of the war, Davidson simultaneously taught and studied at the University of Michigan where he earned a Ph.D. in languages and literatures in 1922.  He arrived in Denver later that year and began teaching at the University of Denver.  Before arriving in Colorado, his academic specialty was eighteenth century England.  Once in Denver, he realized that Western literature and folklore would be his life work.  Davidson taught at the University of Denver until his death in 1957.  His course topics ranged from studies of Shakespeare and other English literature, to folklore in the West.  He began teaching news writing and eventually founded the journalism department at the University as well as the board of publications and the press club.  He was the first faculty member elected to serve as president of the University Senate.  In 1940 he became head of the English Department and from March to August 1953 he served as interim Chancellor.  At the time of assuming his post, he remarked: "There is hardly an organization on campus that I have not been connected with at one time or another."  Davidson was named University Lecturer for 1956.  Davidson was a director of the Colorado State Historical Society, the Modern Languages Association, the American Folklore Society, and the American Dialect Society.  He was a charter member of the Denver Posse of the Westerners, an organization devoted to western folklore.  In spare moments, Davidson conducted research, wrote outlines for plays, and authored a large number of articles.  He contributed to a wide range of magazines from "Western American" to "Shakespeare Quarterly".  Additionally, Davidson authored several books on folklore.  The most widely recognized is "Rocky Mountain Tales", which presents regional folklore as well as true accounts of early events in the area.  Levette Davidson died May 14, 1957.

Question: In what year was the university where Taede A. Smedes received his Ph.D founded?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person who received the Ph.D."
    },
    "university_name": {
      "type": "string",
      "description": "The name of the university where the person received their Ph.D."
    },
    "university_founding_year": {
      "type": "integer",
      "description": "The year the university was founded."
    }
  },
  "required": [
    "person_name",
    "university_name",
    "university_founding_year"
  ],
  "additionalProperties": false
}
