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
Hasan Gafoor: Hasan Gafoor (11 December 1950 – 12 March 2012) was the Director General of Police of Maharashtra (Anti Corruption bureau).  Previously he was the Director General of Police of Maharashtra and managing director of the Maharashtra Police Housing & Welfare Corporation.  He was the Police Commissioner of Mumbai, but was promoted as an aftermath of the November 2008 Mumbai attacks.  Prior to being the Police Commissioner, he was the Additional Director General, Anti-Corruption Bureau (ACB) between 15 June 2007 and 29 February 2008.  Gafoor is a 1974 batch IPS officer, and was the second Muslim to become the police chief of Mumbai after Syed Majeedullah, who was the Police Commissioner from 1962 to 1965.

Shahid Azmi: Shahid Azmi (1977 – 11 February 2010) was an Indian lawyer, most known for defending innocent people charged with terrorism, including some of accused in the 2008 Mumbai attacks, such as Faheem Ansari, who was later acquitted for lack of evidence.  At age 14, he was arrested during the 1992 Bombay Riots.  He was arrested again under TADA, serving seven years in Delhi's Tihar Jail, on charges of plotting against the state, though he was acquitted later.  He started studies while in jail, and went on to become criminal defence lawyer in Mumbai in 2003, defending cases for those accused of terrorism.  Prevention of Terrorism Act, 2002 (POTA) was later repealed.  He was shot dead by four assailants in his office in Kurla, Mumbai on 11 February 2010 at the age of 32.

Attribution of the 2008 Mumbai attacks: Attribution of the 2008 Mumbai attacks cani made by the Indian authorities who said that the Mumbai attacks cani directed by Lashkar-e-Taiba militants inside Pakistan.  American intelligence agencies also cani with this attribution.  Pakistan initially contested this attribution, but agreed this was the case on 7 January 2009.  To back up its accusations, the Indian government supplied a dossier to Pakistan's high commission in Delhi.  The Pakistan government dismissed the dossier as "not evidence," but also announced that it had detained over a hundred members of Jamaat-ud-Dawa, a charity linked with Lashkar-e-Taiba.  In February 2009, Pakistan's Interior Minister Rehman Malik agreed that "some part of the conspiracy" did take place in Pakistan.

Rahul Bhatt: Rahul "Sunny" Bhatt (born 24 January 1982), is an Indian fitness trainer and an aspiring film actor.  The son of famous film director Mahesh Bhatt and Kiran Bhatt, Rahul gained unwitting notoriety in 2009 following revelations that David Headley, an accused in the 2008 Mumbai attacks, had befriended him.  In an investigative report by PBS, Rahul Bhatt was described as a B-movie actor asking for favors to reveal more details about Headley.  He was a contestant on Bigg Boss 4 in 2010.

Zabiuddin Ansari: Sayed Zabiuddin Ansari a.k.a. Abu Hamza or Abu Jundal is an Indian national, Islamic fundamentalist/terrorist belonging to Indian Mujahideen and Lashkar-e-Taiba.  He is accused of being involved in 2008 Mumbai attacks.  Zabiuddin Ansari (Abu Hamza)'s name was listed in the list of "50 most wanted criminals sheltered in Pakistan" released by India on 21 May 2011.  He had served as the handler of the 10 LeT terrorists during 2008 Mumbai attacks.

Mukesh Bhatt: Mukesh Bhatt (born 5 June 1952 in Mumbai), is an Indian film producer, who has produced several Bollywood films.  He is the younger brother of Mahesh Bhatt, and also the co-owner of the production company Vishesh Films, set up in 1986.  He is the uncle of Pooja Bhatt, Rahul Bhatt, Alia Bhatt, Shaheen Bhatt and Emraan Hashmi.

Erroneous reporting on the 2008 Mumbai attacks: During and immediately after the 2008 Mumbai attacks the news media worldwide broadcast incorrect factual information on a scale often seen in a fog of war.  Erroneous reporting on the 2008 Mumbai attacks included false information concerning the number of attackers, their nationality, their organizational affiliations, origins, and the methods of transport they had used.  Theories and speculations were openly aired by various commentators that were later proved to be wrong.  Many such speculations, such as the involvement in the attacks of the "Deccan Mujahideen", were widely reported by media worldwide.  Various news outlets carried opinion pieces and unattributed theories about the origins of the attackers which were unfounded.

Tukaram Omble: Tukaram Omble AC ( 1954 — 27 November 2008) was an assistant sub-inspector (ASI) of the Mumbai Police, and a retired army man.  He was killed in action while fighting terrorists during the 2008 Mumbai attacks, at Girgaum Chowpatty Mumbai, and was instrumental in apprehending Pakistan national Ajmal Kasab alive.  The lone surviving terrorist Kasab was later convicted and hanged.  The Indian government honoured Omble, on 26 January 2009, with the Ashoka Chakra – the country's highest peace-time gallantry award for extraordinary bravery and valour in the line of duty.

2008 Mumbai attacks: The 2008 Mumbai attacks were a group of terrorist attacks that took place in November 2008, when 10 members of Lashkar-e-Taiba, an Islamic terrorist organisation based in Pakistan, carried out a series of 12 coordinated shooting and bombing attacks lasting four days across Mumbai.  The attacks, which drew widespread global condemnation, began on Wednesday, 26 November and lasted until Saturday, 29 November 2008, killing 164 people and wounding at least 308.

David Headley: David Coleman Headley (born Daood Sayed Gilani; 30 June 1960) is an American terrorist of Pakistani origin, and a spy who conspired with the Lashkar-e-Taiba (LeT) in plotting the 2008 Mumbai attacks.  He is currently in jail in the United States of America.

Question: Where is the friend of Rahul Bhatt, who is accused of the 2008 Mumbai attacks, being held?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the individual whose detention location is being sought."
    },
    "role_in_attacks": {
      "type": "string",
      "description": "The individual's role in the 2008 Mumbai attacks."
    },
    "current_status": {
      "type": "string",
      "description": "The current status of the individual."
    },
    "location_of_detention": {
      "type": "string",
      "description": "The country where the individual is currently detained."
    }
  },
  "required": [
    "person_name",
    "role_in_attacks",
    "current_status",
    "location_of_detention"
  ],
  "additionalProperties": false
}
