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
Frederick Lindemann, 1st Viscount Cherwell: Frederick Alexander Lindemann, 1st Viscount Cherwell, (5 April 18863 July 1957), pronounced , was a British physicist and an influential scientific adviser to the British government from the early 1940s to the early 1950s, particularly to Winston Churchill.  He advocated the "area" bombing or "strategic bombing" of German cities and civilian homes during the Second World War by falsely stating data to Winston Churchill from a study on psychological impact of Germany's Birmingham Blitz and Hull Blitz on the local population.  He also doubted the sophistication of Nazi Germany's radar technology and the existence of its "V" weapons programme.

John Beddington: Sir John Rex Beddington, HonFREng, CMG, FRS (born 13 October 1945) is Senior Adviser at the Oxford Martin School, and was previously Professor of Applied Population Biology at Imperial College London, and the UK Government Chief Scientific Adviser from 2008 until 2013.

Yuri Izrael: Yuri Antonovich Izrael (Russian: Юрий Антониевич Израэль ; 15 May 1930, Tashkent – 23 January 2014, Moscow) was a vice-chairman of the Intergovernmental Panel on Climate Change (IPCC) until September 2008, when the new bureau was elected.  He was the "most influential scientific adviser" for Vladimir Putin, the former president of Russia, according to CNN.

G. Satheesh Reddy: G. Satheesh Reddy is an Indian Aerospace Scientist and presently Scientific Adviser to Raksha Mantri (SA to RM) and Director General, Missiles and Strategic Systems.  Earlier, Satheesh served as Director of the Research Centre Imarat ( RCI) a key laboratory of Dr APJ Abdul Kalam Missile Complex, Defence Research and Development Organisation and an advanced centre for design, development and delivery of avionics systems for missiles and other applications.  Reddy pioneered many technological developments for Indian Missiles and has made significant contributions towards successful flight testing of the country's maiden intercontinental ballistic missile (ICBM) Agni-V mission.  In June 2015 he was appointed scientific adviser to the defence minister of India.

Mark T. Maybury: Mark Thomas Maybury, PhD (born December 13, 1964) is an American computer scientist and Chief Scientist of the United States Air Force, Washington, D.C. He serves as chief scientific adviser to the Chief of Staff of the Air Force and Secretary of the U.S. Air Force, and provides assessments on a wide range of scientific and technical issues affecting the Air Force mission.

Vladimir Pletser: Vladimir Pletser (born 28 February 1956) is Visiting Professor – Scientific Adviser at the Technology and Engineering Centre for Space Utilization  (CSU) of the Chinese Academy of Sciences in Beijing, China, since April 2016.  He supports the preparation of scientific experiments in microgravity for the future Chinese Space Station and for aircraft parabolic flights.

Joseph Makoju: Engineer Joseph Oyeyani Makoju (born 13 July 1948) served as Special Adviser (Electric Power) to the President Goodluck Jonathan of Nigeria under two separate administrations.  He is now Honorary Adviser on Electric Power to the current President/Commander-in-Chief, Federal Republic of Nigeria (effect from 20 May 2008).  He is also the Special Adviser to the President/Chief Executive, Dangote Group, from 2009 to date,

John Loughhead: Prof John Neil Loughhead OBE FREng FIMechE FIET (born 24 September 1948) is a British businessman and Chief Scientific Adviser to Department of Energy and Climate Change (DECC).  He is also a Fellow of the Royal Academy of Engineering and was formerly the Executive Director of the UK Energy Research Centre.  He was appointed an OBE for services to Technology in 2011.  In 2014, he was voted as one of the Top 500 Most Influential People in Britain by Debrett's and The Sunday Times.

Vincent Ellis McKelvey: Vincent Ellis McKelvey (April 6, 1916 – January 23, 1987) was an American geologist.  He was married to Genevieve Bowman McKelvey.  They had one son, Gregory McKelvey of Spokane, Washington.  Dr. McKelvey was an earth scientist who spent 46 years with the United States Geological Survey.  Dr. McKelvey was recognized as an international authority on deep-sea mineral deposits.  From 1968 to 1982, he served as scientific adviser and senior deputy to the United States delegation to the Law of the Sea Conference of the United Nations, where fellow delegates often depended on his ability to render complex scientific issues into plain English.

Vladimir Putin: Vladimir Vladimirovich Putin ( ; Russian: Влади́мир Влади́мирович Пу́тин ; ] ; born 7 October 1952) is the current President of Russia, holding the office since 7 May 2012.  He was Prime Minister from 1999 to 2000, President from 2000 to 2008, and again Prime Minister from 2008 to 2012.  During his second term as Prime Minister, he was the Chairman of the ruling United Russia party.

Question: According to whom was Yuri Izrael the  "most influential scientific adviser" to the current President of Russia?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "adviser_name": {
      "type": "string",
      "description": "The name of the scientific adviser."
    },
    "advised_person": {
      "type": "string",
      "description": "The name of the person or leader who was advised."
    },
    "adviser_role_description": {
      "type": "string",
      "description": "The specific description of the adviser's role or influence."
    },
    "source_of_information": {
      "type": "string",
      "description": "The entity that provided the information about the adviser's influence."
    }
  },
  "required": [
    "adviser_name",
    "advised_person",
    "adviser_role_description",
    "source_of_information"
  ],
  "additionalProperties": false
}
