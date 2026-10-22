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
Spies for Peace: Spies for Peace was a British group of anti-war activists associated with the Committee of 100 who publicized government preparations for rule after a nuclear war.  In 1963 they broke into a secret government bunker, Regional Seat of Government Number 6 (RSG-6) at Warren Row, near Reading, where they photographed and copied documents.  The RSGs were to include representatives of all the central government departments, to maintain law and order, communicate with the surviving population and control remaining resources.  The public were virtually unaware what the government was planning for the aftermath of a nuclear war until it was revealed by Spies for Peace.

Stanislav Petrov: Stanislav Yevgrafovich Petrov (Russian: Станисла́в Евгра́фович Петро́в ; 7 September 1939 – 19 May 2017) was a lieutenant colonel of the Soviet Air Defence Forces who became known as "the man who single-handedly saved the world from nuclear war" for his role in the 1983 Soviet nuclear false alarm incident.

Second Variety: "Second Variety" is a science fiction short story by American writer Philip K. Dick, first published in "Space Science Fiction" magazine, in May 1953.  A nuclear war between the Soviet Union and the West has reduced much of the world to a barren wasteland.  The war continues, however, among the scattered remains of humanity.  The Western forces have developed "claws", which are autonomous self-replicating robots to fight on their side.  It is one of Dick's many stories in which nuclear war has rendered the Earth's surface uninhabitable.  The story was adapted into the movie" Screamers "in 1995.

Vasili Arkhipov: Vasili Alexandrovich Arkhipov (Russian: Василий Александрович Архипов ) IPA: [vɐˈsʲilʲɪj ɐlʲɪkˈsandrəvʲɪtɕ arˈxipɔːf] (30 January 1926 – 19 August 1998) was a Soviet Navy officer credited with casting the single vote that prevented a Soviet nuclear strike (and, presumably, all-out nuclear war) during the Cuban Missile Crisis.  Such an attack likely would have caused a major global thermonuclear response which could have destroyed much of the world.  As flotilla commander and second-in-command of the diesel powered submarine "B-59" , only Arkhipov refused to authorize the captain's use of nuclear torpedoes against the United States Navy, a decision requiring the agreement of all three senior officers aboard.  In 2002 Thomas Blanton, who was then director of the US National Security Archive, said that "Vasili Arkhipov saved the world".

Emergency Action Message: In the U.S. military's strategic nuclear weapon nuclear command and control (NC2) system, an Emergency Action Message (EAM) is a preformatted message that directs nuclear-capable forces to execute specific Major Attack Options (MAOs) or Limited Attack Options (LAOs) in a nuclear war.  Individual countries or specific regions may be included or withheld in the EAM, as specified in the Single Integrated Operational Plan (SIOP).  The SIOP was updated annually until February 2003, when it was replaced by Operations Plan (OPLAN) 8044.  Since July 2012, the US nuclear war plan has been OPLAN 8010-12, "Strategic Deterrence and Force Employment".

WarGames: WarGames is a 1983 American Cold War science fiction film written by Lawrence Lasker and Walter F. Parkes and directed by John Badham.  The film stars Matthew Broderick, Dabney Coleman, John Wood, and Ally Sheedy.  The film follows David Lightman (Broderick), a young hacker who unwittingly accesses WOPR (War Operation Plan Response), a United States military supercomputer originally programmed to predict possible outcomes of nuclear war.  Lightman gets WOPR to run a nuclear war simulation, originally believing it to be a computer game.  The computer, now tied into the nuclear weapons control system and unable to tell the difference between simulation and reality, attempts to start World War III.

Proud Prophet: Proud Prophet was a simulated war game played by the United States in 1983.  With an ongoing arms buildup against the Soviet Union, President Ronald Reagan and his Administration had a great deal of concern for the U.S. nuclear war plan and what may occur if we did not take action.  After being briefed on the strike plan in place, President Reagan was unsatisfied and took measures to simulate a response to the onset of a nuclear war.  The simulation consisted of 200 Military Personnel and Politicians with only twelve days of actual play.  Stretching the twelve days of gameplay over several week periods, Personnel involved in the simulation were forced to make critical strategic and diplomatic decisions to test the effectiveness of the United States strike plan.  Due to heightened tensions with the ongoing Cold War made this simulation the most realistic in United States Military history.  For the first time ever, the Secretary of Defense and the Chairman of the Joint Chiefs of Staff took part in the game, although their participation was concealed.  One of the main purposes of the simulation was to test the response of the National Command Authority's (NCA) decision making when dealing with many different situations at once.  Although Proud Prophet was intended to help senior officials test their nuclear strategies, it was apparent that many of the concepts in place were incompatible with current Military capabilities.  Many important parts of this simulation saw limited use of de-escalation tactics.  If a risk of a war did occur, many Military advisors saw the use of nuclear missiles as the deterring factor when dealing with the Soviet Union.  The idea behind this concept was that Soviet forces would seek ceasefire if the West moved to use nuclear weapons.  The final outcome of the Proud Prophet war game would show the need to resolve global issues in times of war or potential war.  The outcome of an all-out nuclear war is the total destruction of both sides involved, and a death toll nearly reaching half a billion with the remaining dying from starvation or lethal doses of radiation.  The government file for Proud Prophet was not declassified until December 20th, 2012, and was only declassified in part.  While there is no known reason why it was unclassified under the Obama administration.

Agreement on the Prevention of Nuclear War: The Prevention of Nuclear War Agreement was created to reduce the danger of nuclear war between the United States and the Union of Soviet Socialist Republics.  The agreement was signed in Washington, D.C., on June 22, 1973, during a relative period of détente.  The United States and the U.S.S.R. agreed to reduce the threat of a nuclear war and establish a policy to restrain hostility.

Threads: Threads is a 1984 British television drama jointly produced by the BBC, Nine Network and Western-World Television Inc.  Written by Barry Hines and directed by Mick Jackson, it is a docudrama account of nuclear war and its effects on the city of Sheffield in Northern England.  The plot centres on two families as a confrontation between the United States and the Soviet Union erupts.  As the nuclear exchange between NATO and the Warsaw Pact begins, the film depicts the medical, economic, social and environmental consequences of nuclear war.

Yury Votintsev: Colonel General Yuriy Vsyevolodich Votintsev (Russ.  Юрий Всеволодович Вотинцев) was a retired commander of the Soviet Air Defense's Missile Defense Units.  He is best known for the revelation in his memoirs in 1998 of the 1983 incident involving Stanislav Petrov in which the latter probably prevented an inadvertent nuclear war between the United States and the former Soviet Union.

Question: Who was revealed as "the man who single-handedly saved the world from nuclear war" in memoirs by Yury Votintsev?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The full name of the person identified."
    },
    "role_description": {
      "type": "string",
      "description": "The description of the person's action or significance."
    },
    "incident_year": {
      "type": "integer",
      "description": "The year the incident associated with the person occurred."
    },
    "revealed_by_memoirs": {
      "type": "string",
      "description": "The name of the person whose memoirs revealed this information."
    }
  },
  "required": [
    "person_name",
    "role_description",
    "incident_year",
    "revealed_by_memoirs"
  ],
  "additionalProperties": false
}
