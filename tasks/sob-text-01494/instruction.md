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
Nanjing (disambiguation): Nanjing means 'southern capital' and is the name of the current capital of Jiangsu Province and a former capital of China.  It was formerly romanized as Nanking or Nankin.

Klang (city): Klang or Kelang, officially Royal Town of Klang (Malay: "Bandar Diraja Klang" ), is a royal town and former capital of the state of Selangor, Malaysia.  It is located within the Klang District.  It was the civil capital of Selangor in an earlier era prior to the emergence of Kuala Lumpur and the current capital, Shah Alam.  Port Klang, which is located in the Klang District, is the 13th busiest transshipment port and the 16th busiest container port in the world.

Milledgeville, Georgia: Milledgeville is a city in and the county seat of Baldwin County in the U.S. state of Georgia.  It is northeast of Macon and bordered on the east by the Oconee River.  The rapid current of the river here made this an attractive location to build a city.  It was the capital of Georgia from 1804 to 1868, notably during the American Civil War.  Milledgeville was preceded as the capital city by Louisville and was succeeded by Atlanta, the current capital.  Today U.S. Highway 441 connects Milledgeville to Madison, Athens, and Dublin.

La Trinitaria (Dominican Republic): La Trinitaria (] , "The Trinity") was a secret society founded in Juan Pablo Duarte's home situated in what today is known as Arzobispo Nouel Street, across from the "Del Carmen's Church" in the then occupied Santo Domingo, the current capital of the Dominican Republic.  The founder, Juan Pablo Duarte and a group of likeminded young people, led the struggle to establish the Dominican Republic as a free, sovereign, and independent nation in the 19th century.  They helped bring about the end of the Haitian occupation of the island from 1822 to 1844.

South Sudan: South Sudan ( ), officially the Republic of South Sudan, is a landlocked country in northeastern Africa that gained its independence from Sudan in 2011.  Its current capital, Juba is also the largest city.  Before the outbreak of a civil war in 2013, it was planned that the capital city would be moved to the more centrally located Ramciel in the future.

Rhône-et-Loire: Rhône-et-Loire was a "département" of France whose "préfecture" (capital) was Lyon.  Created on 4 March 1790 like the other French "départements", Rhône-et-Loire was abolished on 12 August 1793 when it was split into two "départements": Rhône ("préfecture": Lyon) and Loire ("préfecture": Feurs, then Montbrison, and then Saint-Étienne, the current capital).  The division of Rhône-et-Loire was a response to counter-Revolutionary activities in Lyon which, by population, was the country's second largest city.  By splitting Rhône-et-Loire, which was the natural economic and, potentially, military hinterland of Lyon, the government sought to protect the French Revolution from the potential power and influence of the counter revolutionary revolt in the Lyon region.

Toyota Central R&amp;D Labs., Inc.: Toyota Central R&D Labs., Inc. (TCRDL) (in Japanese: 豊田中央研究所, Toyota Chuou Kenkyuusho) is the arch institute of the Toyota Group.  It cooperates with Toyota Group and Toyota Technological Institute (TTI).  The facility is located in Nagakute, near Nagoya in Aichi, Japan.  The facility was established in November 1960 with a capital of 500 million Yen.  Currently, there are about 1000 employees conducting both fundamental and applied research in a large variety of topics for the Toyota group and other partners.  The current president is Ishikawa, and the current capital is 3 billion yen.

Thuri people: The Thuri are a Luo people of South Sudan.  They speak Thuri, a Luo language.  They possibly number several tens of thousands.

Yeheidie'erding: Yeheidie'erding (也黑迭兒丁, "Yěhēidié'érdīng", ?  - 1312), also known as Amir al-Din (Arabic: أمير الدين‎ ‎ , "Amīr al-Dīn"), was a Muslim architect who helped design and led the construction of the capital of the Yuan Dynasty, Khanbaliq, located in present-day Beijing, the current capital of the People's Republic of China.

Buenos Aires Province: Buenos Aires (] , "Provincia de Buenos Aires"; English: "good airs") is the largest and most populous Argentinian province.  It takes the name from the city of Buenos Aires, which used to be part of the province and the provincial capital until it was federalized in 1880.  Since then, in spite of bearing the same name, the province does not include the national capital city proper, though it does include all other localities of the Greater Buenos Aires metropolitan area surrounding it.  The current capital of the province is the city of La Plata, founded in 1882.

Question: What is the current capital of the country that is home to the Thuri people?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "people_group_name": {
      "type": "string",
      "description": "The name of the people group mentioned in the question."
    },
    "country_name": {
      "type": "string",
      "description": "The country where the people group resides."
    },
    "capital_city_name": {
      "type": "string",
      "description": "The current capital city of the identified country."
    },
    "capital_designation": {
      "type": "string",
      "description": "Describes the status of the capital city (e.g., 'current capital')."
    }
  },
  "required": [
    "people_group_name",
    "country_name",
    "capital_city_name",
    "capital_designation"
  ],
  "additionalProperties": false
}
