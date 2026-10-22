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
Linux Users' Group of Davis: Linux Users' Group of Davis (commonly known as "LUGOD") is a users' group of students and faculty from the University of California, Davis, Information technology professionals from the Sacramento region, and hobbyists interested in Linux and free and open-source software.  It holds regular meetings in Davis, California, and holds installfests on a regular basis.  Its members participate with each other online in numerous mailing lists and via Internet Relay Chat.

Angus Ellis Taylor: Angus Ellis Taylor (October 13, 1911 – April 6, 1999) was a mathematician and professor at various universities in the University of California system.  He earned his undergraduate degree at Harvard "summa cum laude" in 1933 and his PhD at Caltech in 1936 under Aristotle Michal with a dissertation on analytic functions. By 1944 he had risen to full professor at UCLA, whose mathematics department he later chaired (1958–1964).  Taylor was also an astute administrator and eventually rose through the UC system to become provost and then chancellor of UC Santa Cruz.  He authored a number of mathematical texts, one of which, "Advanced Calculus" (1955, Ginn and Co.), became a standard for a generation of mathematics students.

University of California Student Association: The University of California Student Association (UCSA) is an active 501(c)(3) unincorporated association, purposed as a student association of all University of California (UC) students.  Its charter states that it "shall exist to: serve the interests of the current and future students of the University of California and promotes ["sic"] cooperation between various student governments of the University and student organizations concerned with higher education."  The Association is not a public agency, but its leadership is composed of representatives of UC student governments, which are "official units of the University" system (with one exception).  UCSA participates in various aspects of the UC system's governance, notably including the selection of the student representative on the UC Board of Regents.

Will Lotter: Williard Lotter (born c. 1925) is a former American football, baseball, and soccer coach, and a university faculty member and administrator.  He served as the head football coach for three stints at University of California, Davis (UC Davis)—known as the Northern Branch of the College of Agriculture before 1959—in 1954, from 1956 to 1957, and from 1959 to 1963, compiling a record of 26–42–3.  Lotter was the head baseball coach at the school, serving from 1953 to 1958 and tallying a mark of 45–98.  He also head coach of the men's soccer team as UC Davis from 1972 to 1987.  Lotter played college football at the University of California, Berkeley.  He graduated from Berkeley with a bachelor's degree in physical education in 1949, earned a Master of Education from California State University, Sacramento in 1955, and received a Doctor of Education from Berkeley in 1960.  Lotter served as a faculty member of the Physical Education Department at UC Davis from 1952 to 1993.  He was also the acting Dean of Students at UC Davis from 1969 to 1970.

Kevin Johnson (academic): Kevin R. Johnson is the Dean of the UC Davis School of Law (King Hall).  Before becoming a professor, he was a student at Harvard Law School where he served as an editor of the Harvard Law Review, served as a clerk to Judge Stephen Reinhardt of the United States Court of Appeals for the Ninth Circuit and worked for law firm Heller Ehrman White & McAuliffe.  Johnson joined the faculty at the UC Davis School of Law (King Hall) in 1989, was named Associate Dean in 1998, and the Dean in 2008.  Of Mexican American ancestry, he is the first Latino to head a law school in the UC system.

Robert D. Grey: Robert D. Grey is a long-time academic administrator and researcher and educator in the field of cellular and molecular biology.  He has spent the majority of his career in positions in the University of California system, including interim provost of the UC system, acting chancellor at UC Riverside and provost and executive vice chancellor at UC Davis.  He was also a well-regarded and award-winning faculty member at UC Davis.

University of California, Davis: The University of California, Davis (also referred to as UCD, UC Davis, or Davis), is a public research university and land-grant university as well as one of the 10 campuses of the University of California (UC) system.  It is located in Davis, California, just west of Sacramento, and has the third-largest enrollment in the UC System after UCLA and UC Berkeley.  The university has been labeled one of the "Public Ivies", a publicly funded university considered to provide a quality of education comparable to those of the Ivy League.

University of California, Berkeley: The University of California, Berkeley (also referred to as UC Berkeley, Berkeley, and Cal ) is a public research university located in Berkeley, California.  Founded in 1868, Berkeley is the oldest of the ten research universities affiliated with the University of California system (although UCSF was founded in 1864 and predates the establishment of the UC system) and is ranked as one of the world's leading research universities and the top public university in the United States.

California Digital Library: The California Digital Library (CDL) was founded by the University of California in 1997 to take advantage of emerging technologies that were transforming the way digital information was being published and accessed.  Since then, in collaboration with the ten University of California Libraries and other partners, CDL has assembled one of the world’s largest digital research libraries and changed the ways that faculty, students, and researchers discover and access information.  CDL facilitates the licensing of online materials and develops shared services used throughout the UC system.  Building on the foundations of the Melvyl Catalog (UC’s union catalog), CDL has developed one of the largest online library catalogs in the country and works in partnership with the UC campuses to bring the treasures of California's libraries, museums, and cultural heritage organizations to the world.  CDL continues to explore how services such as digital curation, scholarly publishing, archiving and preservation support research throughout the information lifecycle.

University of California finances: The University of California public university system is funded through both public and private money.  Some funds are given directly to each of the system's 10 campuses, while the rest are distributed through the central UC Office of the President.  Support given by the state of California to its three-tier higher education system (comprising the University of California, California State University, and California Community College) is presented by the governor every January, and approved by the state legislator at the end of the fiscal year in June.  Traditionally, the state of California has been the largest public supporter of the UC system.  In response to state budget woes, UC Berkeley Chancellor Robert Birgeneau in 2011 made the claim that his own university is turning into a federal and not a state institution because of the inversion of the proportion of funds given by each jurisdiction since he became Chancellor in 2004.

Question: What is the users' group of students and faculty from California's third-largest enrollment in the UC System?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "group_name": {
      "type": "string",
      "description": "The name of the users' group."
    },
    "associated_university": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the university."
        },
        "uc_system_enrollment_rank": {
          "type": "integer",
          "description": "The enrollment rank of the university within the UC system."
        }
      },
      "required": [
        "name",
        "uc_system_enrollment_rank"
      ],
      "additionalProperties": false
    },
    "member_composition": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Types of members that form the group."
    }
  },
  "required": [
    "group_name",
    "associated_university",
    "member_composition"
  ],
  "additionalProperties": false
}
