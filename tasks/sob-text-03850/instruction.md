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
BOSM (festival): BITS Open Sports Meet (BOSM) is the annual sports festival of Birla Institute of Technology and Science, Pilani campus.  This sports meet, usually held around mid-September is a prominent showcase of sporting talents from around the country and abroad too.

Higher education in Portugal: Higher education in Portugal is divided into two main subsystems: university and polytechnic education.  It is provided in autonomous public universities, private universities, public or private university institutes, polytechnic institutions and higher education institutions of other types.  Higher education in state-run educational establishments is provided on a competitive basis, a system of "numerus clausus" is enforced through a national database on student admissions.  In addition, every higher education institution offers also a number of additional vacant places through other extraordinary admission processes for sportsmen, mature applicants (over 23 years old), international students, foreign students from the Lusosphere, degree owners from other institutions, students from other institutions (academic transfer), former students (readmission), and course change, which are subject to specific standards and regulations set by each institution or course department.  Portuguese universities have existed since 1290.  The oldest such institution, the University of Coimbra, was first established in Lisbon before moving to Coimbra.  Historically, within the scope of the now defunct Portuguese Empire, the Portuguese founded in 1792 the oldest engineering school of Latin America (the Real Academia de Artilharia, Fortificação e Desenho), as well as the oldest medical college of Asia (the Escola Médico-Cirúrgica de Goa) in 1842.

School of Planning and Architecture: The Schools of Planning and Architecture (SPAs) are a group of autonomous public institutes of higher education under Ministry of Human Resource Development, Government of India.  The SPAs lists three institutes located at Bhopal, New Delhi and Vijayawada.  They were established with the objectives of providing quality Architecture and physical planning education.  The SPAs primarily offer undergraduate, postgraduate, doctoral and executive education programmes.

Indian Institutes of Technology: The Indian Institutes of Technology (IITs) are autonomous public institutes of higher education, located in India.  They are governed by the "Institutes of Technology Act, 1961 " which has declared them as institutions of national importance alongside National Institutes of Technology and lays down their powers, duties, and framework for governance etc.  The Institutes of Technology Act, 1961 lists twenty-three institutes (after the last amendment in 2016).  Each IIT is an autonomous institution, linked to the others through a common IIT Council, which oversees their administration.  The Minister of Human Resource Development is the ex-officio Chairperson of IIT Council.  As of 2017, the total number of seats in all IITs is 11,032.

Roses Tournament: The Roses Tournament is an annual sports competition between Lancaster University and the University of York in England, and is the largest inter-university sports tournament in Europe.  It is organised by their respective Students' Unions, YUSU and LUSU.  It takes its name from the 15th Century civil war, The Wars of the Roses, between the House of Lancaster and the House of York.  The competition is held every summer, alternating its venue between the two universities.

Inter IIT Sports Meet: Inter IIT Sports Meet is the annual sports tournament of the Indian Institutes of Technology.  It is organized in December every year, with the Aquatics events held separately in October.  The seven old IITs take turns hosting the event.

Indian Institute of Technology Jammu: The Indian Institute of Technology Jammu (abbreviated IIT Jammu) is a public research university located in Jammu, Jammu and Kashmir, India. The Institute came into existence in 2016 when a Memorandum of Understanding (MoU) between Department of Higher Education, Government of Jammu & Kashmir and Department of Higher Education, MHRD, Government of India, was signed, setting the ball rolling to set up an IIT campus at village Jagti, Tehsil Nagrota at Jammu.

National Institutes of Technology: The National Institutes of Technology (NITs) are autonomous public institutes of higher education, located in India.  They are governed by the "National Institutes of Technology Act, 2007", which declared them as institutions of national importance alongside Indian Institutes of Technology.  These institutes of national importance receive special recognition from the Government of India.  The NIT Council is the supreme governing body of India's National Institutes of Technology (NIT) system and all 31 NITs are funded by the Government of India.  These institutes are among the top ranked engineering colleges in India and have one of the lowest acceptance rates for engineering institutes, of around 2 to 3 percent, second only to the Indian Institutes of Technology (IITs) in India.  All NITs are autonomous which enables them to set up their own curriculum.  The language of instruction is English at all these institutes.

Government degree colleges in India: Government degree colleges in India are public-sector educational institutes managed mainly through rule and regulations of government accompanied by University Grants Commission (India) (UGC).  Education in India has been categorized into elementary, secondary and higher education.  The aim behind the formation of the government degree colleges is to provide higher education to undergraduates, postgraduates and doctoral research scholars in various streams and courses recognized by UGC of India.  Presently, the standards have been set up for the classifications of the institutes in 2 (f) and 12 (b) category, which is certified by the UGC, New Delhi to maintain the excellence in higher education.  The government degree colleges are fully managed by government, either central or at state level, and affiliated to the universities for course structures.  Moreover, the government degree college as the institute of higher education, are administered and controlled by the principal who serves as the head.  Teachers (Assistant Professor, Associate Professor, and Professor) are appointed through Public Service Commissions (a government body under the articles from 315-323 of the Constitution of India) of central and state governments.  The teachers appointed through the public service commissions are government servants with Group A post and are gazetted in nature.  Education is the matter of concurrent lists in India; the government from the centre or from the states has the right to formulate law on higher education.

Madina Central College: Madina Central College is a school situated in Kandy district, Madawala, Sri Lanka.  It is a mixed school which currently has about 3150 students and teachers about 120.  The current principal and vice principal are A.H.M.Azeez and Mr.J.M.Zarook respectively.This school offers both primary and secondary education.  This school has all the essential fascilities.  Madawala has gained reputation and popularity because of this school.  Students from far away places like Digana, Udathalawinna, Kandy, Katugastota come here due its popularity and perfection.The school holds cricket matches with Azhar college every year,but it has now stopped for a while due to some inevitable circumstance.  At the beginning of every year, the school holds the annual sports meet and in every end of the year the school holds its annual price giving.  The students have achieved a lot in studies and as well as in sports.The school holds a vast background.

Question: Inter IIT Sports Meet is the annual sports tournament of what autonomous public insititutes of higher education in India?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "tournament_name": {
      "type": "string",
      "description": "The name of the annual sports tournament."
    },
    "host_institution_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the autonomous public institutes of higher education."
        },
        "type": {
          "type": "string",
          "description": "The classification of the institutions (e.g., autonomous public institutes of higher education)."
        },
        "location_country": {
          "type": "string",
          "description": "The country where the institutions are located."
        }
      },
      "required": [
        "name",
        "type",
        "location_country"
      ],
      "additionalProperties": false
    },
    "relationship_to_tournament": {
      "type": "string",
      "description": "Describes the relationship between the institutions and the tournament."
    }
  },
  "required": [
    "tournament_name",
    "host_institution_details",
    "relationship_to_tournament"
  ],
  "additionalProperties": false
}
