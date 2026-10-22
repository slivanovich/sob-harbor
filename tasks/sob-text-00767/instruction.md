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
Berwind-White Coal Mining Co. v. Chicago &amp; Erie Railroad Co.: Berwind-White Coal Mining Co. v. Chicago &amp; Erie Railroad Co.

Rochester &amp; Genesee Valley Railroad Museum: The Rochester and Genesee Valley Railroad Museum (RGVRRM) is an operating railroad museum located in Industry, New York.  The museum started in 1971 with the purchase of a former Erie Railroad Depot from the Erie Lackawanna Railroad.  Since then the museum has grown to include a one-mile demonstration railroad, making it one of the only operating railroad museums in New York State.  The museum was formerly an operation of the Rochester Chapter National Railway Historical Society until 2011.  The organization rosters more than 40 pieces of historic railroad equipment, including diesel and steam locomotives, electric trolley and multiple-unit cars, freight cars, cabooses, passenger cars, and work equipment.  The museum campus includes a number of preserved railroad structures, including the 1909 Industry Depot built by the Erie Railroad, a waiting shelter from the Rochester, Lockport & Buffalo Railroad, and a crossing watchman's shanty from the New York Central.  Train rides are operated and the museum is open to the public on select weekends from June through October, and is staffed entirely by volunteers.

Additur: An additur (Latin: "it is added to") is a legal term referring to the practice of a trial judge adding damages additional to the original amount awarded by the jury.  It is not allowed in U.S. federal courts, as held by "Dimick vs. Schiedt", 293 U.S. 474 (1935).  However, "Dimick" was decided before "Erie Railroad Co. v. Tompkins" (1938), which given the rarity of additur makes it unclear whether federal courts are bound by this rule when applying state law in diversity cases.

Erie Railroad: The Erie Railroad (reporting mark ERIE) was a railroad that operated in the northeastern United States, originally connecting New York City — more specifically Jersey City, New Jersey, where Erie's former terminal, long demolished, used to stand — with Lake Erie.  It expanded west to Chicago with its 1941 merger with the former Atlantic and Great Western Railroad, also known as the New York, Pennsylvania and Ohio Railroad (NYPANO RR).  Its mainline route proved influential in the development and economic growth of the Southern Tier, including cities such as Binghamton, Elmira, and Hornell.  The Erie Railroad repair shops were located in Hornell, and were Hornell's largest employer.  Hornell was also where Erie's main line split into two routes, one north to Buffalo and the other west to Cleveland.

Erie Railroad Depot (Rochester, New York): Erie Railroad Depot, Erie Railroad Station or Erie Depot was the terminal station for the Erie Railroad in Rochester, New York, designed by George E. Archer, the railroad's architect.  The station opened in 1887 between the Genesee River and Exchange Street on the south side of Court St. The station was one of the Erie's few electrified railroad stations, and was one of the first stations to provide electric commuter services in 1907.  In 1905 the Lehigh Valley Railroad Station opened directly across the Genesee River from the Erie Depot.

Erie War: The Erie War was a 19th-century conflict between American financiers for control of the "Erie Railway Company", which owned and operated the Erie Railroad.  Built with public funds raised by taxation and on land donated by public officials and private developers, by the middle of the 1850s the railroad was mismanaged and heavily in debt.  A cattle drover turned Wall Street banker and broker Daniel Drew at first loaned $2 million to the railroad, and then acquired control over it.  He amassed fortune by skilfully manipulating the Erie railroad shares on the New York Stock Exchange.  Cornelius Vanderbilt, who set his mind on building a railroad empire, saw multiple business and financial opportunities in railways and decided in 1866 to "corner the market on Erie" by silently scooping the Erie railroad stock.  After succeeding, Vanderbilt permitted Drew to stay on the board of directors in his former capacity as a treasurer.

Guaranty Trust Co. v. York: Guaranty Trust Co. v. York, 326 U.S. 99 (1945), was a United States Supreme Court case that described how federal courts were to follow state law.  Justice Frankfurter delivered the majority opinion further refining the doctrine set forth in "Erie Railroad Co. v. Tompkins".

Brown v. Board of Education: Brown v. Board of Education of Topeka, 347 U.S. 483 (1954) , was a landmark United States Supreme Court case in which the Court declared state laws establishing separate public schools for black and white students to be unconstitutional.  The decision overturned the "Plessy v. Ferguson" decision of 1896, which allowed state-sponsored segregation, insofar as it applied to public education.  Handed down on May 17, 1954, the Warren Court's unanimous (9–0) decision stated that "separate educational facilities are inherently unequal."  As a result, "de jure" racial segregation was ruled a violation of the Equal Protection Clause of the Fourteenth Amendment of the United States Constitution.  This ruling paved the way for integration and was a major victory of the Civil Rights Movement, and a model for many future impact litigation cases.  However, the decision's fourteen pages did not spell out any sort of method for ending racial segregation in schools, and the Court's second decision in "Brown II", 349 U.S. 294 (1955) only ordered states to desegregate "with all deliberate speed".

Erie Railroad Co. v. Tompkins: Erie Railroad Co. v. Tompkins, 304 U.S. 64 (1938) , is a landmark decision by the Supreme Court of the United States in which the Court held that federal courts did not have the judicial power to create general federal common law when hearing state law claims under diversity jurisdiction.  In reaching this holding, the Court overturned almost a century of federal civil procedure case law, and established the foundation of what remains the modern law of diversity jurisdiction as it applies to United States federal courts.

Cliffs Erie Railroad: The Cliffs Erie Railroad (reporting mark LTVX) was a railroad that operated from Hoyt Lakes to Taconite Harbor, Minnesota.  The railroad opened in 1956 by Erie Mining Company to transport taconite from Hoyt Lakes to Taconite Harbor.  In 1989, LTV Steel purchased Erie Mining and the railroad was renamed LTV Mining Railroad.  The railroad closed in early 2001 when the LTV company ended the operations of the harbor.  In 2002 Cleveland Cliffs bought the plant, and again renamed the railroad The Cliffs Erie Railroad (combining the names Erie Mining and Cleveland Cliffs).  In 2004 Cliffs Erie hired a contractor to claim leftover chips and pellets from the mine due to the high iron prices.  They used the only unsold locomotives, EMD F9s (borrowing one from Lake Superior Railroad Museum).  The cleanup trains ran until 2008 when the last train ran.  In 2014, the F9s were sold off.  The railroad is now sitting, unlikely to ever see activity again.

Question: Did Brown v. Board of Education or Erie Railroad Co. v. Tompkins deal with racism?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "case_name": {
      "type": "string",
      "description": "The name of the Supreme Court case that dealt with racism."
    },
    "dealt_with_racism": {
      "type": "boolean",
      "description": "Indicates whether the identified case dealt with racism."
    },
    "topic_of_case": {
      "type": "string",
      "description": "A brief description of the main topic of the case that dealt with racism."
    },
    "other_case_mentioned": {
      "type": "string",
      "description": "The name of the other Supreme Court case mentioned in the question."
    },
    "other_case_topic": {
      "type": "string",
      "description": "A brief description of the main topic of the other case mentioned."
    }
  },
  "required": [
    "case_name",
    "dealt_with_racism",
    "topic_of_case",
    "other_case_mentioned",
    "other_case_topic"
  ],
  "additionalProperties": false
}
