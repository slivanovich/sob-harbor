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
Taleh: Taleh (Somali: "Taleex" , Arabic: تلأ ح‎ ‎ ) is a historical town in the eastern Sool region of Somaliland.  It served as the headquarters of the pre-independence Dervish State.

Zeila &amp; Lughaya State: Zeila & Lughaya State, or Saylac & Lughaya State, officially the Zeila & Lughaya State of Somalia, (Somali: "Maamul Goboleedka Saylac & Lughaya ee Soomaaliya" ), is a region in northwestern Somalia.  Saylac and Lughaya State was formed in 2011, claiming to be a federal state of Somalia.  "Zeila State" was proclaimed first.  It later united with Lugayhe to form the "State of Sayla and Lugayhe".  The territory has a total area of 8,639 km.  Its main city is Zeila, which is situated on the coast.  Lughaya, Asha Addo, Harirad, Jidhi and Lawyacado are the other principal cities in the region.  Most residents of the region belong to the Somali ethnic group, with the Issa especially well-represented.

President of Somalia: The President of Somalia (Somali: "Madaxaweynaha Soomaaliya" ) is the head of state of Somalia.  The President is also commander-in-chief of the Somali Armed Forces.  The President represents the Federal Republic of Somalia, and the unity of the Somali nation, as well as ensuring the implementation of the Constitution of Somalia and the organized and harmonious functioning of the organs of state.  The office of President of Somalia was established with the proclamation of the Republic of Somalia on 1 July 1960.  The first President of Somalia was Aden Abdullah Osman Daar.  The current office-holder is the 9th President Mohamed Abdullahi Mohamed, since 16 February 2017.

War in Somalia (2006–2009): The War in Somalia was an armed conflict involving largely Ethiopian and Somali Transitional Federal Government (TFG) forces and Somali troops from Puntland versus the Somali Islamist umbrella group, the Islamic Court Union (ICU), and other affiliated militias for control of the country.  There is a clear connection between War in Somalia (2009–) and the War of 2006.  The war officially began shortly before July 20, 2006 when U.S. backed Ethiopian troops invaded Somalia to prop up the TFG in Baidoa.  The TFG in Somalia invited Ethiopians to intervene, which became an "unpopular decision".  Subsequently, the leader of the ICU, Sheik Hassan Dahir Aweys, declared "Somalia is in a state of war, and all Somalis should take part in this struggle against Ethiopia".  On December 24, Ethiopia stated it would actively combat the ICU.

Somaliland: Somaliland (Somali: "Somaliland" ; Arabic: صوماليلاند‎ ‎ "Ṣūmālīlānd ", أرض الصومال "Arḍ aṣ-Ṣūmāl "), officially the Republic of Somaliland (Somali: "Jamhuuriyadda Somaliland" , Arabic: جمهورية صوماليلاند‎ ‎ "Jumhūrīyat Ṣūmālīlānd"), is a self-declared state internationally recognised as an autonomous region of Somalia.

Bashir Yussuf: Sheikh Bashir Yussuf (Somali: "Sheekh Bashiir Yuusuf" , Arabic: الشيخ يوسف بشير‎ ‎ , born c. 1905 in Taleh, northern Somalia) was a Somali religious leader.

Taleh Airport: Taleh Airport is an airport in Taleh, Somalia.

Taleh District: Taleh District is a district in the northern Sool region of Somalia.  Its capital lies at Taleh, the former headquarters of the Somali religious and nationalist leader Mohammed Abdullah Hassan (the "Mad Mullah") and his Dervish State.

Independence Day (Somalia): The Independence Day of Somalia is a national holiday observed annually in Somalia on July 1.  The date celebrates the union of the Trust Territory of Somaliland (the former Italian Somaliland) and the State of Somaliland (the former British Somaliland) on July 1, 1960, which formed the Somali Republic (Somalia).  A government was subsequently formed by Abdullahi Issa and Muhammad Haji Ibrahim Egal and other members of the trusteeship and protectorate governments, with speaker of the SOMALIA ACT OF UNION Haji Bashir Ismail Yusuf as President of the Somali National Assembly, Aden Abdullah Osman Daar as President of the Somali Republic, On 20 July 1961 and through a popular referendum, the people of Somalia ratified a new constitution, which was first drafted in 1960.

Kenneth Menkhaus: Kenneth Menkhaus is a political scientist who is a professor at Davidson College in North Carolina, where he has taught since 1991.  Menkhaus's publications include the book "Somalia: State Collapse and the Threat of Terrorism" (2004) and the article "Governance without Government in Somalia" in the journal "International Security" (2007).  He is a specialist on Somalia and the Horn of Africa.  Menkhaus was a Fulbright Scholar during his PhD research on Somalia.  He subsequently taught for two years at the American University in Cairo, between 1989 and 1991, and between 1993 and 1994 was a special political advisor for the UN Operation in Somalia.  He was visiting civilian professor at the US Army Peacekeeping Institute in 199495, and visiting scholar at the US Army Strategic Studies Institute in 201112.

Question: What state in Somalia does Taleh belong?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "town_name": {
      "type": "string",
      "description": "The name of the town in question."
    },
    "region_name": {
      "type": "string",
      "description": "The region where the town is located."
    },
    "state_name": {
      "type": "string",
      "description": "The name of the state or self-declared state to which the town belongs."
    },
    "state_status": {
      "type": "string",
      "description": "The international recognition status of the state."
    }
  },
  "required": [
    "town_name",
    "region_name",
    "state_name",
    "state_status"
  ],
  "additionalProperties": false
}
