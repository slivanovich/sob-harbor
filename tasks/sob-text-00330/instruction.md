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
In the Hour of Chaos: In the Hour of Chaos is a 2016 American documentary film directed by Bayer Mack.  It details the life and various trials of the Reverend Martin Luther King Sr. ("Daddy King"), including his violent, poverty-stricken upbringing in rural Georgia, the assassination of his oldest son (civil rights leader Martin Luther King Jr.), the drowning of his younger son Alfred Daniel Williams King and the shooting death of his wife, Alberta Williams King.

King (miniseries): King is a 1978 American television miniseries based on the life of Martin Luther King Jr., the American civil rights leader and 1964 Nobel laureate.  It aired for three consecutive nights on NBC from February 12 through 14, 1978.  The miniseries earned nine Emmy Award nominations, including nominations for actors Paul Winfield, Cicely Tyson and Ossie Davis.  Several real-life figures from the Civil Rights Movement had minor roles in the production, including then-Atlanta mayor Maynard Jackson, King's sister Christine King Farris, his niece Alveda King, and his four children: Yolanda, Martin III, Dexter and Bernice.  Donzaleigh Abernathy, Tony Bennett, Julian Bond and Ramsey Clark each portrayed themselves.

Clayborne Carson: Clayborne Carson (born June 15, 1944) is an African-American professor of history at Stanford University, and director of the Martin Luther King, Jr., Research and Education Institute.  Since 1985 he has directed the Martin Luther King Papers Project, a long-term project to edit and publish the papers of Martin Luther King, Jr.

Martin Luther King Jr. Outpatient Center: The Martin Luther King Jr.  Outpatient Center (MLK OC), formerly known as Martin Luther King Jr.  Multi-Service Ambulatory Care Center (MLK-MACC), Martin Luther King Jr./Drew Medical Center (King/Drew) and later Martin Luther King Jr.–Harbor Hospital (MLK-Harbor or King–Harbor), is a public urgent care center and outpatient clinic in Willowbrook, an unincorporated section of Los Angeles County, California, north of the city of Compton and south of the Watts neighborhood of Los Angeles.  Founded as a major public hospital, it was shut down in August 2007 because of its poor record of patient care.  The urgent care center and outpatient clinic, however, remain operating on the site.  There are plans to reopen the facility in 2013 as a smaller hospital under a partnership between Los Angeles County and the University of California as a nonprofit organization governed by a seven-member board of directors.

Bearing the Cross: Bearing the Cross: Martin Luther King, Jr., and the Southern Christian Leadership Conference is a 1986 book by David J. Garrow about Martin Luther King Jr., the Southern Christian Leadership Conference, and the American Civil Rights Movement.  The book won the 1987 Pulitzer Prize for Biography.

Alberta Williams King: Alberta Christine Williams King (September 13, 1904 – June 30, 1974) was Martin Luther King, Jr.'s mother and the wife of Martin Luther King, Sr. She played a significant role in the affairs of the Ebenezer Baptist Church.  She was shot and killed in the church six years after the assassination of Martin Luther King, Jr.

Jerry Wurf: Jerome "Jerry" Wurf (May 18, 1919 – December 10, 1981) was a U.S. labor leader and president of the American Federation of State, County and Municipal Employees (AFSCME) from 1964 to 1981.  Wurf was a friend of Martin Luther King Jr., and was arrested multiple times for his activism, notably during the Memphis Sanitation Strike and was released just in time to hear Martin Luther King Jr's 'I've Been to the Mountaintop' oratory at the strike, assassination the next day, and attend his funeral.

Alveda King: Alveda Celeste King (born January 22, 1951) is an American activist, author and former state representative for the 28th District in the Georgia House of Representatives.

Alpha Man: The Brotherhood of MLK: Alpha Man: The Brotherhood of MLK is a television documentary film that reveals the story of Martin Luther King Jr.’s fraternity days as a member of Alpha Phi Alpha fraternity.  Produced by Rainforest Films, the half-hour special originally aired August 28, 2011 on Black Entertainment Television (BET).  The documentary special was scheduled to debut on the same day as the much-anticipated official dedication of the Martin Luther King, Jr.  Memorial statue on the National Mall in Washington, D.C..  The statue's dedication, which was to coincide with the 48th anniversary of the March on Washington and King’s "Dream" speech, was postponed until October 16, 2011 due to Hurricane Irene.

Martin Luther King Jr. National Historic Site: The Martin Luther King Jr.  National Historic Site consists of several buildings including Martin Luther King Jr.'s boyhood home and the original Ebenezer Baptist Church, the church where King was baptized and both his father Martin Luther King Sr. and he were pastors.  These places, critical to the interpretation of the life of Martin Luther King Jr. and his legacy as a leader of the American Civil Rights Movement, were included in the National Historic Site when it was established on October 10, 1980.

Question: King is a 1978 American television miniseries about Martin Luther King Jr., that included his niece, who is an american activist, and representative for what district in the Georgia House of Representatives?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "miniseries_name": {
      "type": "string",
      "description": "The name of the television miniseries."
    },
    "person_name": {
      "type": "string",
      "description": "The name of the individual mentioned in the question."
    },
    "person_relationship_to_mlk_jr": {
      "type": "string",
      "description": "The relationship of the person to Martin Luther King Jr."
    },
    "person_professions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of professions or roles held by the person."
    },
    "representative_district": {
      "type": "string",
      "description": "The district the person represented in the Georgia House of Representatives."
    }
  },
  "required": [
    "miniseries_name",
    "person_name",
    "person_relationship_to_mlk_jr",
    "person_professions",
    "representative_district"
  ],
  "additionalProperties": false
}
