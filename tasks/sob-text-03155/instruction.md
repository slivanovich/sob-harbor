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
John Alite: John Edward Alite also known as Johnny Alletto (born September 30, 1962), is a mobster and hitman of Albanian origin.  An associate of the Gambino crime family and John A. Gotti in the 1980s, 1990s and early 2000s, he fled in 2003 after learning he had been targeted for murder.  He traveled to twenty countries in Europe and South America.  While living in Brazil, he was served with an Interpol arrest warrant.  He spent two years in Brazilian prisons and was extradited to the US in 2006.  He was convicted on several counts of murder conspiracy and racketeering and was sentenced in 2011 to 10 years in prison.  He was a prosecution witness against former associates, Gotti and Charles Carneglia.

Kosovo War crimes witness intimidation and deaths: War crimes witnesses to the Kosovo War (1998–99) have been victims to threats, violence, and murder.  Those who spoke out about the abuses of their side in the conflict were seen as traitors to their community, and therefore, only a few became witnesses in war crime trials.  The international institutions ICTY, UNMIK and EULEX, and national courts in Serbia and Kosovo, have all had problems in ensuring safety for testifying protected witnesses.  According to observers, one of the main reasons that the Kosovo Relocated Specialist Judicial Institution will partly operate outside Kosovo is the past failures of the international institutions to protect witnesses.  According to Carla Del Ponte, the former ICTY prosecutor, "the investigation of the Kosovo Liberation Army fighters appeared to be the most frustrating of all the investigations done by the ICTY", and stated "witnesses were so afraid and intimidated that they even feared to talk about the KLA presence in some areas, not to mention actual crimes".  She further stated that "I am convinced that UNMIK and even KFOR officers were afraid for their lives and the lives of their missions’ members.  I think some of the ICTY judges were afraid that they would become a target for the Albanians" and believes that witness intimidation seriously affected the acquitting verdicts against KLA officials Fatmir Limaj and Ramush Haradinaj.  Numerous witnesses did change their testimonies during trials, while others were killed or mysteriously disappeared.  Avni Zogiani, leader of an anti-corruption nongovernmental organization in Kosovo, said "Intimidation and even killings of witnesses are nothing new or shocking in Kosovo".  EULEX prosecutor Charles Hardaway said that "Witness intimidation, not only in war crimes but in other cases too, is happening from people with high competencies in government who are powerful".  According to Belgian author Jelle Janssens, it was reported that judges and prosecutors became terrified at the mention of high-ranking KLA officers or politicians in case files.  Del Ponte asserts that there were serious abuses of witnesses in Kosovo local criminal proceedings, and also alleged that UNMIK leaked sensitive information about witnesses to defendants, which UNMIK denied but later admitted that it had stopped some investigations into high-level perpetrators due to political reasons.  The Humanitarian Law Center concluded that a large number of acquittances were due to witnesses changing their stories, suspecting intimidation.

Michael Capuzzo: Michael Capuzzo (born on May 1, 1957) is an American journalist and author best known for his "New York Times"-bestselling nonfiction books "The Murder Room" and "Close to Shore".  "The Murder Room," the true story of a private dining club of famous detectives who solve cold murders, and "Close to Shore", an historic thriller and recreation of the first American shark attack in World War I-era New Jersey, both enjoyed wide acclaim from critics and authors such as Gay Talese, Mark Bowden, John Sanford, and Michael Connelly.  Capuzzo signed a contract for a new book with Simon & Schuster in 2011.

Charles Bowden (disambiguation): Charles Bowden (born 1945) is an American non-fiction author, journalist, and essayist.

Charles Bowden (criminal): Charles Bowden is a convicted Irish criminal, who after turning state's witness in the murder of journalist Veronica Guerin, was the first person to enter Irelands's Witness Security Programme.

Bowden Glacier: Bowden Glacier ( ) is a glacier lying on the southeast flank of Salient Ridge that flows northeast to Blue Glacier, Victoria Land.  It was named by the New Zealand Geographic Board in 1994 for Charles Bowden, first chairman of the Ross Dependency Committee during Sir Edmund Hillary's South Pole Expedition, part of the Commonwealth Trans-Antarctic Expedition in 1957.  Bowden also served as a member of the Parliament of New Zealand until 1955.

El Sicario, Room 164: El Sicario, Room 164 is a 2010 documentary film directed by Gianfranco Rosi and based on an article by Charles Bowden.

Charles Bowden (cricketer): Charles Bowden (6 November 1860 – 3 September 1909) was a New Zealand cricketer.  He played one first-class match for Auckland in 1883/84.

Veronica Guerin: Veronica Guerin (5 July 1958 – 26 June 1996) was an Irish crime reporter who was murdered by drug lords. Born in Dublin, she was an athlete in school, and later played on the Irish national teams for both football and basketball.  After studying accountancy she ran a public-relations firm for seven years, before working for Fianna Fáil and as an election agent for Seán Haughey.  She became a reporter in 1990, writing for the "Sunday Business Post" and "Sunday Tribune".  In 1994 she began writing about crime for the "Sunday Independent".  In 1996 she was fatally shot while stopped at a traffic light.  The shooting caused national outrage in Ireland.  Investigation into her death led to a number of arrests and convictions.

Border Regional Library Association: The Border Regional Library Association (B.R.L.A.) promotes libraries and librarianship in the tri-border region of West Texas, Southern New Mexico and Northern Chihuahua, Mexico.  The non-profit organization was founded in 1966 and, as of 2009, has over 100 members including libraries, librarians, trustees, and library paraprofessionals.  B.R.L.A. events and awards include an annual continuing education workshop and banquet, Librarian and Staff Member of the Year awards and annual scholarship awards.  The organization is best known for its annual Southwest Book Awards for noteworthy books about the Southwest published in any genre and geared toward any audience.  Past winners include James Carlos Blake, Charles Bowden, Dennis DeConcini, Tomie dePaola, Arturo Islas, Neil Miller, Pat Mora, Benjamin Alire Sáenz, Rubén Salazar, Sergio Troncoso, and Luis Alberto Urrea.

Question: Where was the person who Charles Bowden was a witness in their murder born?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "witness_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person who was a witness."
        },
        "role": {
          "type": "string",
          "description": "The role of the person in the murder case, e.g., state's witness."
        }
      },
      "required": [
        "name",
        "role"
      ],
      "additionalProperties": false
    },
    "victim_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person who was murdered."
        },
        "profession": {
          "type": "string",
          "description": "The profession of the victim."
        },
        "birth_location": {
          "type": "string",
          "description": "The city where the victim was born."
        }
      },
      "required": [
        "name",
        "profession",
        "birth_location"
      ],
      "additionalProperties": false
    },
    "crime_type": {
      "type": "string",
      "description": "The type of crime committed against the victim."
    }
  },
  "required": [
    "witness_details",
    "victim_details",
    "crime_type"
  ],
  "additionalProperties": false
}
