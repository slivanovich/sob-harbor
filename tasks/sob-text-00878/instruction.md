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
Vernonia School District: The Vernonia School District is a public school district that serves students in the communities of Vernonia and Mist in the U.S. state of Oregon.  Vernonia Elementary School, Vernonia Middle School, and Vernonia High School are contained in separate wings of a single building in Vernonia constructed on high ground after floods in 1996 and 2007 severely impacted the city.  The new building was built above the floodplain to prevent future flooding.

National Treasury Employees Union v. Von Raab: National Treasury Employees Union v. Von Raab, 489 U.S. 656 (1989) , was a United States Supreme Court case involving the Fourth Amendment and its implication on drug testing programs.  The majority of the Court upheld the drug testing program in United States Customs Service.

Arlington Elementary School District: Arlington School District 47 is a public school district based in Maricopa County, Arizona.  It feeds into Buckeye Union High School District.

Vernonia School District 47J v. Acton: Vernonia School District 47J v. Acton, 515 U.S. 646 (1997) was a U.S. Supreme Court decision which upheld the constitutionality of random drug testing regimen implemented by the local public schools in Vernonia, Oregon.  Under that regimen, student athletes were required to submit to random drug testing before being allowed to participate in sports.  During the season, 10% of all athletes were selected at random for testing.  The Supreme Court held that although the tests were searches under the Fourth Amendment, they were reasonable in light of the schools' interest in preventing teenage drug use.

Board of Education v. Earls: Board of Education v. Earls, 536 U.S. 822 (2002) , was a United States Supreme Court case in which the Court upheld the constitutionality of mandatory drug testing by public schools of students participating in extracurricular activities.  The legal challenge to the practice was brought by two students, Lindsay Earls and Daniel James, and their families against the school board of Tecumseh, Oklahoma, alleging that their policy requiring students to consent to random urinalysis testing for drug use violated the Fourth Amendment to the United States Constitution.

School District 47 Powell River: School District 47 Powell River is a school district in British Columbia.  It covers the community of Powell River as well as Texada Island.  The current Powell River School Board serves until December 2014.  The board is composed of five elected trustees.  They are Steve Formosa, Mary James, Aaron Reid, Jeanette Scott (chair) and Doug Skinner.

Escobedo v. Illinois: Escobedo v. Illinois, 378 U.S. 478 (1964), was a United States Supreme Court case holding that criminal suspects have a right to counsel during police interrogations under the Sixth Amendment.  The case was decided a year after the court held in "Gideon v. Wainwright", 372 U.S. 335 (1963) that indigent criminal defendants had a right to be provided counsel at trial.

Acton-Boxborough Regional High School: Acton-Boxborough Regional High School (ABRHS) is an open enrollment high school in Acton, Massachusetts.  A part of the Acton-Boxborough Regional School District, it serves the Massachusetts towns of Acton and Boxborough and has students in grades 9 through 12.  It is situated downhill from the Raymond J. Grey Junior High School, at 36 Charter Road in Acton.  Raymond J. Grey Junior High School occupies the facility that, until 1973, was the high school.  ABRHS underwent an $80 million renovation and expansion in 2005.

Elliot R. Peters: Elliot R. Peters is a trial attorney at San Francisco law firm Keker, Van Nest & Peters LLP, who frequently works on cases of national significance.  He led the defenses of internet activist Aaron Swartz and cyclist Lance Armstrong.  He represented the Major League Baseball Players Association in successfully challenging DOJ seizures of baseball players’ drug testing records, in the seminal computer search case, "United States v Comprehensive Drug Testing", 579 F.3d 989 (2009).  He has also defended financier Frank Quattrone, securities litigator William Lerach and CEO Bruce Karatz.  He has represented top international law firms defending malpractice claims and technology companies defending intellectual property claims.  Elliot has been named “Attorney of the Year” in California three times, twice for freeing indigent men, serving life sentences for murder, but whose convictions were wrongful and who were actually innocent.

Danny Escobedo: Danny Escobedo (born c. 1937) was a Chicago petitioner in the Supreme Court case of "Escobedo v. Illinois", which established a criminal suspect's right to remain silent and have an attorney present during questioning.  This case was an important precedent to the famous "Miranda v. Arizona" decision.

Question: Were both Escobedo v. Illinois and Vernonia School District 47J v. Acton cases about drug testing?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_about_drug_testing": {
      "type": "boolean",
      "description": "Indicates if the user's question is related to drug testing."
    },
    "case_details": {
      "type": "array",
      "description": "Details for each Supreme Court case mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "case_name": {
            "type": "string",
            "description": "The name of the Supreme Court case."
          },
          "is_about_drug_testing": {
            "type": "boolean",
            "description": "True if the case was about drug testing, false otherwise."
          },
          "primary_topic": {
            "type": "string",
            "description": "The main legal topic or issue addressed in the case."
          }
        },
        "required": [
          "case_name",
          "is_about_drug_testing",
          "primary_topic"
        ],
        "additionalProperties": false
      }
    },
    "both_cases_about_drug_testing": {
      "type": "boolean",
      "description": "The final answer to whether both specified cases were about drug testing."
    }
  },
  "required": [
    "question_about_drug_testing",
    "case_details",
    "both_cases_about_drug_testing"
  ],
  "additionalProperties": false
}
