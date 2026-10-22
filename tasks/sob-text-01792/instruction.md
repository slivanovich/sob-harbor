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
Fred Bell: Thomas Frederick Bell, Jr. (born ca. 1880) was an American millionaire heir, the son of banker Thomas Bell and his wife Teresa.

Federal Republic of Central America: The Federal Republic of Central America (Spanish: "República Federal de Centroamérica" ), also called the United Provinces of Central America (Spanish: "Provincias Unidas del Centro de América" ) in its first year of creation, was a sovereign state in Central America consisting of the territories of the former Captaincy General of Guatemala of New Spain.  It existed from September 1821 to 1841, and was a republican democracy.  It is also sometimes incorrectly referred to in English as the United States of Central America.

Thomas Bell Poole: Thomas Bell Poole (1818–1865) was under-sheriff of Monterey County, and member of the Knights of the Golden Circle serving as a crewman of the Confederate privateer J. M. Chapman.  He was later a leader of Captain Ingram's Partisan Rangers and was captured and tried for killing a Deputy Sheriff following the Bullion Bend Robbery.  He was found guilty of murder and was hanged at Placerville, California on September 29, 1865.

Knights of the Golden Circle: The Knights of the Golden Circle (KGC) was a secret society in the mid-nineteenth-century United States.  The original objective of the KGC was to annex a "golden circle" of territories in Mexico, Central America, Confederate States of America, and the Caribbean as slave states, to be led by Maximilian I of Mexico.

Thomas Miller Bell: Thomas Miller Bell (January 11, 1923 in Saint John, New Brunswick, Canada – November 12, 1996) was a Canadian politician, lawyer and barrister.  He was elected to the Canadian House of Commons as a Member of the Progressive Conservative Party to represent the riding of St. John—Albert in 1953.  He became Parliamentary Assistant to the Minister of Trade and Commerce in 1957.  This position was succeeded by Parliamentary Secretary to the Minister of Justice and Attorney General of Canada for which he served three terms.  He became the Chief Opposition Whip in 1968 until 1973 followed by Opposition House Leader of the Progressive Conservatives.  He was also a member of the Standing Joint Committee on the Parliamentary Restaurant for two terms.  He was defeated in 1974, after serving two terms for Saint John—Lancaster.  Prior to his federal political experience, he served in the Merchant Navy during World War II.  His grandfather, Thomas Bell, also was a Member of Parliament.

Lawrence Bell (footballer): Stanley Lawrence Thomas Bell (May 1873 – 7 April 1945), sometimes known as Laurie Bell or Lawrie Bell, was a Scottish professional football centre forward and outside right.

Losh, Wilson and Bell: Losh, Wilson and Bell, later Bells, Goodman, then Bells, Lightfoot and finally Bell Brothers, was a leading Northeast England manufacturing company, founded in 1809 by the partners William Losh, Thomas Wilson, and Thomas Bell.

Thomas B. Bell: Thomas Bell was one of Stephen F. Austin's colonists, having moved to Texas in 1824 although one record has him entering the colony as early as 1822.  He was a soldier during the Texas Revolution and received bounty land for participating in the Siege of Bexar.  He and his brother James Bell later donated the land upon which the town of Bellville, Texas was built.  His will was probated in Austin County, Texas.  He formally adopted a grown man who was living in Hamilton County Florida in 1855.  This man John G. Slade turned out to be his illegitimate son by a Nancy Slade.  Most of Thomas Bell's estate was left to this son who was already married to Penelope Green and had children when he came to Texas to receive his inheritance.

Military career of Bhoja: The 11th century Paramara king Bhoja ruled from his capital at Dhara (Dhar in present-day Madhya Pradesh, India).  The period of his reign is dated approximately 1010 CE to 1055 CE, although some historians believe that he ascended the throne before 1010 CE.  Bhoja inherited a kingdom centered around the Malwa region, and made several attempts to expand it varying results.  He managed to annex territories as far as northern parts of Konkan, but these territorial gains were short-lived.  He fought wars against several of his neighbours, including the Chaulukyas of Gujarat, the Chalukyas of Lata, the Chalukyas of Kalyani (Western Chalukyas), the Chandelas of Jejakabhukti, the Kachchhapaghatas of Gwalior, the Chahamanas of Shakambhari, the Chahamanas of Naddula, and the Kalachuris of Tripuri.

Cristos Negros of Central America and Mexico: Cristo Negros or Black Christs of Central America and Mexico trace their origins to the veneration of an image of Christ on a cross located in the Guatemalan town of Esquipulas, near the Honduran and El Salvadoran border.  This image was sculpted in 1595 in wood and over time it blackened and gained a reputation for being miraculous.  Little is known of how veneration of the image was spread by clergy, although there are records of its introduction in various locations, especially in Central America, southern Mexico, central Mexico (especially in areas near Mexico City) and even as far north as New Mexico.  However, a number of these images, such as the ones in Chalma, State of Mexico and Mérida, Yucatán have origin stories that do not connect the local image with that of Esquipulas.  The Cristo Negro of Esquipulas remains an important symbol for Central America, with its sanctuary the most visited site in the region.  There are hundreds of other such images with at least local importance with Christ of Chalma attracting millions of visitors, second only to that of the Virgin of Guadalupe in Mexico.  The popularity of the image continues to spread, with Central American and Mexican migrants bringing the image to the United States and Canada, founding new sanctuaries.

Question: Thomas Bell Polla lead what group that wanted to annex territories in Mexico and Central America?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person mentioned in the question."
    },
    "group_name": {
      "type": "string",
      "description": "The name of the group the person was associated with that had the specified objective."
    },
    "group_objective": {
      "type": "string",
      "description": "The primary objective of the identified group."
    },
    "person_role_in_group": {
      "type": "string",
      "description": "The role of the person within the identified group."
    },
    "annexation_targets": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of territories the group aimed to annex."
    }
  },
  "required": [
    "person_name",
    "group_name",
    "group_objective",
    "person_role_in_group",
    "annexation_targets"
  ],
  "additionalProperties": false
}
