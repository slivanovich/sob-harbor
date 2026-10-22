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
LaVoy Finicum: Robert LaVoy Finicum (January 27, 1961 – January 26, 2016) was a spokesman for the Citizens for Constitutional Freedom, who seized and occupied the Malheur National Wildlife Refuge in the State of Oregon, United States, on January 2, 2016.

Article 10 of the Constitution of Malaysia: Article 10 of the Constitution of Malaysia guarantees Malaysian citizens the right to freedom of speech, freedom of assembly and freedom of association.  Unlike comparable provisions in constitutional law such as the First Amendment to the United States Constitution, Article 10 entitles citizens to such freedoms as are not restricted by the government, instead of absolutely guaranteeing those freedoms.

Freedom of religion in Lebanon: The Constitution provides for freedom of religion and the freedom to practice all religious rites provided that the public order is not disturbed.  The Constitution declares equality of rights and duties for all citizens without discrimination or preference but establishes a balance of power among the major religious groups.  The Government generally respected these rights; however, there were some restrictions, and the constitutional provision for apportioning political offices according to religious affiliation may be viewed as inherently discriminatory.  There were no reports of societal abuses or discrimination based on religious belief or practice.  There were, however, periodic reports of tension between religious groups, attributable to competition for political power, and citizens continued to struggle with the legacy of a 15-year civil war that was fought largely along sectarian lines.  Despite sectarian tensions caused by the competition for political power, churches, mosques, and other places of worship continued to exist side-by-side, extending a centuries-long national heritage as a place of refuge for those fleeing religious intolerance.

Citizens for Constitutional Freedom: Citizens for Constitutional Freedom (C4CF), later also known as People for Constitutional Freedom (P4CF), was the name taken on January 4, 2016, by an armed private U.S. militia that occupied the U.S. Fish and Wildlife Service's Malheur National Wildlife Refuge headquarters in the U.S. state of Oregon from January 2 to February 11, 2016.  The leader of the organization was Ammon Bundy, son of Cliven D. Bundy, who engaged in a standoff with the federal government over grazing rights on federal land.

Ammon Bundy: Ammon Edward Bundy (born September 1, 1975) is an American car fleet manager who led armed militants in the 2016 occupation of the Malheur National Wildlife Refuge.

Human rights in Mali: According to the U.S. Department of State's annual report on human rights in Mali for 2003, Mali's government generally respects the human rights of its citizens and observes relevant constitutional provisions (e.g., freedom of speech and of the press, freedom of assembly and association, freedom of religion) and prohibitions (e.g., arbitrary arrest and detention, forced exile, torture, and discrimination based on race, sex, disability, language, or social status).

Fundamental rights in India: Fundamental Rights are the basic rights of the people and the charter of rights contained in of Constitution of India.  It guarantees civil liberties such that all Indians can lead their lives in peace and harmony as citizens of India.  These include individual rights common to most liberal democracies, such as equality before law, freedom of speech and expression, religious and cultural freedom and peaceful assembly, freedom to practice religion, and the right to constitutional remedies for the protection of civil rights by means of writs such as habeas corpus, Mandamus, Prohibition, Certiorariand Quo Warranto.  Violation of these rights result in punishments as prescribed in the Indian Penal Code or other special laws, subject to discretion of the judiciary.  The Fundamental Rights are defined as basic human freedoms that every Indian citizen has the right to enjoy for a proper and harmonious development of personality.  These rights universally apply to all citizens, irrespective of race, place of birth, religion, caste or gender.  Aliens (persons who are not citizens) are also considered in matters like equality before law.  They are enforceable by the courts, subject to certain restrictions.  Though the rights conferred by the constitution other than fundamental rights are equally valid, their enforcement in case of violation shall be secured from the judiciary in a time consuming legal process.  However in case of fundamental rights violation, Supreme court of India can be approached directly for ultimate justice per .  The Rights have their origins in many sources, including England's Bill of Rights, the United States Bill of Rights and France's Declaration of the Rights of Man.

Saving American Democracy Amendment: The Saving American Democracy Amendment is a United States constitutional amendment proposed in December 2011 by Senators Mark Begich (D-Alaska) and Bernie Sanders (I-Vermont) "to expressly exclude for-profit corporations from the rights given to natural persons by the Constitution of the United States, prohibit corporate spending in all elections, and affirm the authority of Congress and the States to regulate corporations and to regulate and set limits on all election contributions and expenditures."  The Saving American Democracy Amendment was meant to overturn the 2010 United States Supreme Court decision Citizens United v. Federal Election Commission, which stated that freedom of speech prohibited the government from restricting independent political expenditures by a nonprofit corporation.  This was the first constitutional amendment proposed by Sanders in his two decades in Congress.  The text of the amendment reads as follows:

National Board of Review: The National Board of Review of Motion Pictures was founded in 1909 for Nestor Film Company in New York City, just 14 years after the birth of cinema, to protest New York City Mayor George B. McClellan, Jr.'s revocation of moving-picture exhibition licenses on Christmas Eve 1908.  The mayor (son of the famed Civil War general) believed that the new medium degraded the morals of community.  To assert their constitutional freedom of expression, theatre owners led by Marcus Loew and film distributors (Edison, Biograph, Pathé and Gaumont) joined John Collier of the People's Institute at Cooper Union and established the New York Board of Motion Picture Censorship, which soon changed its name to the National Board of Review of Motion Pictures to avoid the taint of the word "censorship".

Freedom of movement under United States law: Freedom of movement under United States law is governed primarily by the Privileges and Immunities Clause of the United States Constitution which states, "The Citizens of each State shall be entitled to all Privileges and Immunities of Citizens in the several States."  As far back as the circuit court ruling in "Corfield v. Coryell," 6 Fed.  Cas.  546 (1823), freedom of movement has been judicially recognized as a fundamental Constitutional right.  In "Paul v. Virginia," 75 U.S. 168 (1869), the Court defined freedom of movement as "right of free ingress into other States, and egress from them."  However, the Supreme Court did not invest the federal government with the authority to protect freedom of movement.  Under the "privileges and immunities" clause, this authority was given to the states, a position the Court held consistently through the years in cases such as "Ward v. Maryland," 79 U.S. 418 (1871), the "Slaughter-House Cases," 83 U.S. 36 (1873) and "United States v. Harris," 106 U.S. 629 (1883).

Question: When was the leader of "Citizens for Constitutional Freedom" born? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "organization_name": {
      "type": "string",
      "description": "The name of the organization."
    },
    "leader_name": {
      "type": "string",
      "description": "The name of the leader of the organization."
    },
    "leader_birth_date": {
      "type": "string",
      "format": "date",
      "description": "The full birth date of the leader in YYYY-MM-DD format."
    },
    "leader_birth_year": {
      "type": "integer",
      "description": "The birth year of the leader."
    },
    "leader_birth_month": {
      "type": "string",
      "description": "The birth month of the leader."
    },
    "leader_birth_day": {
      "type": "integer",
      "description": "The birth day of the leader."
    }
  },
  "required": [
    "organization_name",
    "leader_name",
    "leader_birth_date",
    "leader_birth_year",
    "leader_birth_month",
    "leader_birth_day"
  ],
  "additionalProperties": false
}
