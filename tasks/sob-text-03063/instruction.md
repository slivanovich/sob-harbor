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
University College of The Caribbean: The University College of The Caribbean (UCC), is Jamaica's largest privately held tertiary education consortium.  UCC was established in January 2004 from an amalgamation of the Institute of Management Sciences (IMS) and the Institute of Management and Production (IMP).  In preparing students for an increasingly complex and diverse society, the UCC has developed a number of programmes to provide the knowledge and skills to help students succeed wiprogrammes(not authorised as a college for master's degree by UCJ.  All masters program are unaccredited) ld community.  Their range of programmes cover local Associate and bachelor's degrees and overseas bachelor's and master's degree programmes, offered in partnership with internationally recognized universities such as the Florida International University, Florida Memorial University and the University of London

Clive Baldock: Clive Baldock (born 1962) is a British-born Australian professor.  He graduated with a BSc (hons) in Physics from the University of Sussex, an MSc in Radiation Physics from St Bartholomew's Hospital Medical College, University of London, a PhD in Medical Physics from King's College London and a Masters of Tertiary Education Management from the University of Melbourne.  He is Pro Vice-Chancellor for Researcher Development and Dean of Graduate Research at the University of Tasmania.  His research interests are in the fields of gel dosimetry, radiation therapy, dosimetry, and medical imaging in which he has published over 150 research journal papers.  He has been awarded Fellowships of the Australian Institute of Physics, the Australasian College of Physical Scientists and Engineers in Medicine, the Institute of Physics (UK) and the Institute of Physics and Engineering in Medicine (UK).

Education in Mauritius: Education in Mauritius is managed by the Ministry of Education & Human Resources, which controls the development and administration of state schools funded by government, but also has an advisory and supervisory role in respect of private schools.  The Tertiary education is maintained by the Ministry of Tertiary Education, Science, Research and Technology.  The government of Mauritius provides free education to its citizens from pre-primary to tertiary levels.  Since July 2005, the government also introduced free transport for all students.  Schooling is compulsory up to the age of 16.  Mauritian students consistently rank top in the world each year for the Cambridge International O Level, International A and AS level examinations.

Takoradi Polytechnic: Takoradi Technical University is a public tertiary education institution (university) located in Sekondi-Takoradi, the capital of the Western Region of Ghana.  Takoradi Technical University was established as a Government Technical Institute in 1954, and became part of the State Tertiary Education System.  Later after the passage of the Polytechnic Law of 1992 (PNDCL 321).  It was replaced by Polytechnics Law (Act 745) in 2007.  In 2016, the Bill to convert six out of the 10 polytechnics (including Takoradi Polytechnic) into a fully fledged university received a unanimous approval of Ghanaian legislators.

University of Melbourne: The University of Melbourne (informally Melbourne University) is a public research university located in Melbourne, Australia.  Founded in 1853, it is Australia's second oldest university and the oldest in Victoria.  Times Higher Education ranks Melbourne as 33rd in the world, while the Academic Ranking of World Universities places Melbourne 40th in the world (both first in Australia).

Polytechnic (United Kingdom): A polytechnic was a tertiary education teaching institution in England, Wales and Northern Ireland offering higher diplomas, undergraduate degree and post graduate education (masters and PhDs) that was governed and administered at the national level by the Council for National Academic Awards.  At the outset the focus of Polytechnics was on STEM subjects with a special emphasis on engineering.  After the passage of the Further and Higher Education Act 1992 they became independent universities which meant they could award their own degrees.  The comparable institutions in Scotland were collectively referred to as Central Institutions. Like polytechnics or technological universities (institute of technology) in other countries, their aim was to teach both purely academic and professional vocational degrees (engineering, computer science, law, architecture, management, business, accounting, journalism, town planning) etc.  Their original focus was applied education for professional work and their original roots concentrated on advanced engineering and applied science (STEM subjects), though soon after being founded they also created departments concerned with the humanities.  The polytechnic legacy was to advance and excel in undergraduate and post graduate degrees in engineering and technology (STEM) education that now form a core faculty at most universities in the UK.  While many former polytechnics have advanced their research focus many have stayed true to their original ethos by focusing on teaching for professional practice.

Association for Tertiary Education Management: The Association for Tertiary Education Management Inc. (ATEM Inc) is a professional body in Australasia for tertiary education administrators and managers.  It was established in 1976 as the Australian Institute of Tertiary Education Administrators (AITEA), changing its name in 1996.

Education in the British Virgin Islands: Education in the British Virgin Islands is largely free and is a requirement for children ages 5 to 17.  The British Virgin Islands has a total of 15 public primary schools and 4 secondary public schools.  In addition to the public schools, there are 10 primary private schools and 3 secondary private schools.  The School year is from September to June.  The British Virgin Islands is a part of the British Overseas Territories and therefore the educational system is very similar to the traditional learning system in the United Kingdom.  Primary schools are focused on establishing the basics of an academic curriculum and host students between the ages of 5 to 12.  After the completion of Primary school, students move on to Secondary school.  Secondary school is for students between the ages of 13 and 17.  Following the completion of secondary education, students may write their Caribbean secondary education certificate examination.  There are approximately 2,700 students who attend primary school for the first 7 years of their required education, however less than 1,800 students successfully finish the following 5 required years of secondary school and complete their certificate exam.  Tertiary Education is by no means required in the British Virgin Islands.  Students who chose to continue their education after Secondary Education may move on to an additional 2 years of schooling.  After 2 years of Tertiary Education is completed, students may take their Caribbean advanced placement examinations.  Passing the exams entitles students the right to continue their studies even further at the University of the Virgin Island.  This University is the only tertiary education institution in the British Virgin Islands.  At the University, students can obtain associate, bachelors, and master's degrees in the departments of business, education, liberal arts and social sciences, or science and mathematic.

Education in Melbourne: Education in Melbourne may be divided into four groups: pre-school, primary education, secondary education and tertiary education.  Melbourne is home to some of Australia's largest university and prominent independent schools.  Entry to tertiary education for most students is through the Victorian secondary school system where students are ranked by the Australian Tertiary Admission Rank (ATAR) upon completion of Year 12.

Education in Ballarat: Education in Ballarat may be divided into a four groups: pre-school, primary education, secondary education and tertiary education.  Ballarat is home to two universities and many primary and secondary schools.  Entry to tertiary education for most students is through the Victorian secondary school system where students are ranked by the Australian Tertiary Admission Rank (ATAR) upon completion of Year 12.

Question: In what year was the University that Clive Baldock received his Masters of Tertiary Education Management degree from founded?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "university_name": {
      "type": "string",
      "description": "The name of the university."
    },
    "degree_obtained": {
      "type": "string",
      "description": "The specific degree obtained from the university."
    },
    "founding_year": {
      "type": "integer",
      "description": "The year the university was founded."
    },
    "university_location_country": {
      "type": "string",
      "description": "The country where the university is located."
    }
  },
  "required": [
    "university_name",
    "degree_obtained",
    "founding_year",
    "university_location_country"
  ],
  "additionalProperties": false
}
