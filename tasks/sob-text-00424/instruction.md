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
University System of Georgia: The University System of Georgia (USG) is the State of Georgia Government Agency that includes 28 public institutions of higher learning in the U.S. state of Georgia.  The System is governed by the Georgia Board of Regents.  It sets goals and dictates general policy to educational institutions as well as administering Public Library Service of the state which includes 58 public library systems.  The USG also dispenses public funds (allocated by the state's legislature) to the institutions but not the lottery-funded HOPE Scholarship.  The USG is the fifth largest university system in the United States by total student enrollment, with 318,027 students in 28 public institutions.  The four larger systems are the University System of Ohio, City University of New York, California State University, and the State University of New York.  USG institutions are divided into four categories depending on their mission statements.  The categories include research universities, state universities, state colleges and regional universities.

Jack Gelber: Jack Gelber (April 12, 1932 – May 9, 2003) was an American playwright best known for his 1959 drama "The Connection", depicting the life of drug-addicted jazz musicians.  The first great success of the Living Theatre, the play was translated into five languages and produced in ten nations.  Gelber continued to work and write in New York, where he also taught writing, directing and drama as a professor, chiefly at Brooklyn College, City University of New York, where he created the MFA program in playwriting.  In 1999 he received the Edward Albee Last Frontier Playwright Award in recognition of his lifetime of achievements in theatre.

Eastern Connecticut State University: Eastern Connecticut State University (Eastern) is a public, coeducational liberal arts university and a member of the Council of Public Liberal Arts Colleges.  Founded in 1889, it is the second-oldest campus in the Connecticut State University System and third-oldest public university in the state.  Eastern is located on Windham Street (Campus Map) in Willimantic, Connecticut, on 182 acre 30 minutes from Hartford, lying midway between New York City and Boston.  Although the majority of courses are held on the main campus, select classes take place at Manchester Community College, Capital Community College, and a satellite center in Groton.

Academic ranks in Argentina: Professors are usually categorized as "ordinario" or "concursado" (tenured, selected by a jury composed of tenured professors or other reputed authorities on the subject, after a selection process involving academic background evaluation and a public dissertation), "interino" (non-tenure, but stable position, the professor is proposed by the director of the corresponding department – sometimes after different selection processes – and accepted by the Consejo Directivo of the corresponding school), or "suplente" (substitute, hired through the same process as interinos).  In most cases, classes are taught by a professorial team (a "cátedra", chair), formed by one or two professors and auxiliars, which generally also functions as a research team.  Regardless of the rank, professors in public universities (and in many private ones) must perform research.  This ranking system is the one used at the Universidad de Buenos Aires (the largest Argentine university) and by most of the public universities, but not all of them; being autonomous, they can choose their own scale.  Private universities have their own rank in each case, sometimes based on the public university system, although as a general rule they have less ranks or hold a higher ranking as the starting point for a teaching career (devoting auxiliar ranks to undergraduates).

Lee Gelber: Lee Gelber (b. Bronx, New York) is an American tour guide and urban historian whose primary expertise is New York City and its environs.  Gelber is a graduate of the City University of New York and former toy industry executive who went into the tour business following the occasion of the firm that he was working for having been subsumed by a larger entity in a merger.  With an earlier tenure as a Big Apple Greeter under his belt, he became a tour guide for Gray Line in 1994.  His breadth of knowledge and tour guide finesse soon led him to become a trainer of other guides for Grayline and then a subsequent series of other outfits.  Therein he is popularly known as the so-called (New York City) "Dean of Guides" and has been referred to as such in reflective attribution by among other publications the Chicago Tribune and the New York Times.  He is a former Co-President of The Guides Association of New York City (GANYC) an organization which honored him in March of 2016 with their inaugural "Guiding Spirit Award" at the second annual apple awards.  in 1993, while still a toy executive, Gelber was a contestant on the seniors edition of the American game show Jeopardy! and finished second on the episode on which he appeared with a total of $10,400.

List of City University of New York institutions: The City University of New York (CUNY) system is the public university system of New York City.  CUNY consists of three types of institutions: senior colleges, which grant bachelor's degrees and occasionally master's and associate's degrees; community colleges, which grant associate degrees; and graduate or professional schools.  s of 2009 , CUNY is the United States's largest urban public university, with an enrollment of over 270,000 students.

University of Massachusetts: The University of Massachusetts is the five-campus public university system and the only public research system in the Commonwealth of Massachusetts.  The University system includes five campuses (Amherst, Boston, Dartmouth, Lowell, and a medical school in Worcester), and a satellite campus, with system administration in Boston and Shrewsbury.  The system is accredited by the New England Association of Schools and Colleges and across its campuses enrolls 73,000 students.

James Milliken: James B. (“J.B.”) Milliken is chancellor of the City University of New York - the nation's largest urban university system.  Prior, Milliken served as president of the University of Nebraska from 2004 to 2014, where he was also a professor at the School of Public Affairs and at the College of Law.  Milliken previously served as senior vice president of the University of North Carolina's 16-campus system, from 1998 to 2004.  Before his career in academic administration, Milliken practiced law in New York City.

York College, City University of New York: York College of The City University of New York is one of eleven senior colleges in the City University of New York (CUNY) system.  It is located in Jamaica, Queens in New York City.  Founded in 1966, York was the first senior college founded under the newly formed CUNY system, which united several previously independent public colleges into a single public university system in 1961.  The college is a member-school of Thurgood Marshall College Fund.

City University of New York: The City University of New York (CUNY; pron.: ) is the public university system of New York City, and the largest urban university system in the United States.  CUNY and the State University of New York (SUNY) are separate and independent university systems, despite both public institutions receiving funding from New York State.  CUNY, however, is only located in the city, while SUNY is located in the entire state, including the city.

Question: Jack Gelber was a professor at what public university system of New York City?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "professor_name": {
      "type": "string",
      "description": "The name of the professor."
    },
    "professor_role": {
      "type": "string",
      "description": "The academic role held by the individual."
    },
    "affiliated_institution": {
      "type": "string",
      "description": "The specific institution where the professor chiefly taught within the system."
    },
    "university_system_name": {
      "type": "string",
      "description": "The name of the public university system."
    },
    "system_type": {
      "type": "string",
      "description": "The type of the university system (e.g., public, urban)."
    },
    "system_location_city": {
      "type": "string",
      "description": "The city where the university system is located."
    }
  },
  "required": [
    "professor_name",
    "professor_role",
    "affiliated_institution",
    "university_system_name",
    "system_type",
    "system_location_city"
  ],
  "additionalProperties": false
}
