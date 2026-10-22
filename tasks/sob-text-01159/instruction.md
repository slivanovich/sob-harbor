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
Virginia ballot measures, 2004: The 2004 Virginia State Elections took place on Election Day, November 2, 2004, the same day as the Presidential and the U.S. House elections in the state.  The only statewide elections on the ballot were two constitutional referendums to amend the Virginia State Constitution.  Because Virginia state elections are held on off-years, no statewide officers or state legislative elections were held.  All referendums were referred to the voters by the Virginia General Assembly.

Zellers v. Huff: The Dixon School Case (Zellers v. Huff) was a lawsuit started in 1948 in New Mexico contesting the use of nuns, religious brothers and priests as teachers in publicly supported schools under the First Amendment to the United States Constitution.  The case involved thirty schools in eleven New Mexico counties, twenty-eight plaintiffs, two hundred defendants, and public expenditures to the schools of over $600,000 annually.  Following on the heels of the U.S. Supreme Court's decision in "Everson v. Board of Education", which applied First Amendment freedoms to state as well as federal law, the Dixon School Case was the first state case to implement separation of church and state in public schools, and was watched with interest nationally.

Virginia ballot measures, 2010: The 2010 Virginia State Elections took place on Election Day, November 2, 2010, the same day as the U.S. House elections in the state.  The only statewide elections on the ballot were three constitutional referendums to amend the Virginia State Constitution.  Because Virginia state elections are held on off-years, no statewide officers or state legislative elections were held.  All referendums were referred to the voters by the Virginia General Assembly.

Saving American Democracy Amendment: The Saving American Democracy Amendment is a United States constitutional amendment proposed in December 2011 by Senators Mark Begich (D-Alaska) and Bernie Sanders (I-Vermont) "to expressly exclude for-profit corporations from the rights given to natural persons by the Constitution of the United States, prohibit corporate spending in all elections, and affirm the authority of Congress and the States to regulate corporations and to regulate and set limits on all election contributions and expenditures."  The Saving American Democracy Amendment was meant to overturn the 2010 United States Supreme Court decision Citizens United v. Federal Election Commission, which stated that freedom of speech prohibited the government from restricting independent political expenditures by a nonprofit corporation.  This was the first constitutional amendment proposed by Sanders in his two decades in Congress.  The text of the amendment reads as follows:

Harper v. Virginia State Board of Elections: Harper v. Virginia Board of Elections, 383 U.S. 663 (1966) , was a case in which the U.S. Supreme Court found that Virginia's poll tax was unconstitutional under the equal protection clause of the 14th Amendment.  In the late 19th and early 20th centuries, eleven southern states established poll taxes as part of their disenfranchisement of most blacks and many poor whites.  The Twenty-fourth Amendment to the United States Constitution (1964) prohibited poll taxes in federal elections; five states continued to require poll taxes for voters in state elections.  By this ruling, the Supreme Court banned the use of poll taxes in state elections.

Virginia ballot measures, 2006: The 2006 Virginia State Elections took place on Election Day, November 7, 2006, the same day as the U.S. House and the U.S. Senate elections in the state.  The only statewide elections on the ballot were three constitutional referendums to amend the Virginia State Constitution.  Because Virginia state elections are held on off-years, no statewide officers or state legislative elections were held.  All referendums were referred to the voters by the Virginia General Assembly.

Everson v. Board of Education: Everson v. Board of Education, 330 U.S. 1 (1947) was a landmark decision of the United States Supreme Court which applied the Establishment Clause in the country's Bill of Rights to State law.  Prior to this decision the First Amendment words, "Congress shall make no law respecting an establishment of religion" imposed limits only on the federal government, while many states continued to grant certain religious denominations legislative or effective privileges.  This was the first Supreme Court case incorporating the Establishment Clause of the First Amendment as binding upon the states through the Due Process Clause of the Fourteenth Amendment.  The decision in "Everson" marked a turning point in the interpretation and application of disestablishment law in the modern era.

OneVirginia2021: On September 14, 2015, OneVirginia2021 filed a suit in "Vesilind v. Virginia State Board of Elections" claiming 11 Virginia state districts fail the criteria of compactness outlined by the Virginia State Constitution.  In an official release, OneVirginia2021 executive director Brian Cannon says, “Far from having a standard, the legislature effectively ignored the Constitution on this point, and gave us distorted, weirdly shaped districts that break up communities and rig elections by depriving voters of meaningful competition”

Virginia ballot measures, 2014: The 2014 Virginia State Elections took place on Election Day, November 4, 2014, the same day as the U.S. Senate and U.S. House elections in the state.  The only statewide election on the ballot was one constitutional referendum to amend the Virginia State Constitution.  Because Virginia state elections are held on off-years, no statewide officers or state legislative elections were held.  The referendum was referred to the voters by the Virginia General Assembly.  The amendment easily passed, although final vote totals await the final certification of results by the state board of elections.

California State Board of Education: The California State Board of Education is the governing and policy-making body of the California Department of Education.  The State Board of Education sets K-12 education policy in the areas of standards, instructional materials, assessment, and accountability.  The State Board of Education adopts textbooks for grades K-8, adopts regulations to implement legislation, and has authority to grant waivers of the Education Code.  Content standards are designed to encourage the highest achievement of every student, by defining the knowledge, concepts, and skills that students should acquire at each grade level.  The State Board of Education has eleven members, including one student member, all appointed by the Governor of California.  The student member is selected from a group of three students nominated by the board.  Those are picked from the delegation of the Student Advisory Board on Education, a conference run by the California Association of Student Councils.

Question: What constitutional amendment did Harper v. Virginia State Board of Elections and Everson v. Board of Education apply

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "constitutional_amendment_name": {
      "type": "string",
      "description": "The name of the constitutional amendment."
    },
    "constitutional_amendment_number": {
      "type": "integer",
      "description": "The numerical identifier of the constitutional amendment."
    },
    "cases_of_application": {
      "type": "array",
      "description": "A list of Supreme Court cases that applied this constitutional amendment.",
      "items": {
        "type": "object",
        "properties": {
          "case_name": {
            "type": "string",
            "description": "The full name of the Supreme Court case."
          },
          "specific_clause_applied": {
            "type": "string",
            "description": "The specific clause of the amendment that was applied in the case."
          }
        },
        "required": [
          "case_name",
          "specific_clause_applied"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "constitutional_amendment_name",
    "constitutional_amendment_number",
    "cases_of_application"
  ],
  "additionalProperties": false
}
