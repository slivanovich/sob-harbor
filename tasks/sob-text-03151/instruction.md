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
Idi Amin: Idi Amin Dada ( ;  1923 2816 August 2003) was a Ugandan political leader and military officer who was the President of Uganda from 1971 to 1979.

Cao Chun: Cao Chun (died 210), courtesy name Zihe, was a military officer serving under the warlord Cao Cao in the late Eastern Han dynasty.  He was a younger second cousin of Cao Cao, and is best known for leading the "Tiger and Leopard Cavalry" (虎豹騎), an elite mounted unit, in several battles against Cao Cao's rivals, including Yuan Tan, Tadun and Liu Bei.  His elder brother, Cao Ren, also served as a military officer under Cao Cao.

Siyavosh Beg (qollar-aghasi): Siyavosh Beg, also known by his nisba of Bāshīāchūghī (died ca.  1650/51 or 1655), was a Safavid military commander, official, and "gholam" of Georgian origin.  Early on in his career, he rose to become a military officer ("yuzbashi").  From 1632 to 1635, he served as the governor ("hakem") of Derbent.  Starting from 1632, he also served for a lengthy period as commander of the élite "gholam" corps ("qollar-aghasi"), having succeeded Khosrow Mirza (later Rostam Khan of Kartli) to this post.  In 1645-1649, he served as the governor ("hakem" and "beglarbeg") of Kuhgiluyeh.  When in 1645 the re-appointed grand vizier Khalifeh Sultan urged for repressive laws against Isfahan's large Armenian community, the latter turned to Siyavosh Beg, himself a former Christian.  Alike his then incumbent king Abbas II (1642-1666), Siyavosh Beg was an avid drinker.  Siyavosh Beg's nisba is derived from "Bash-Achuk", a Persian appellation of the Kingdom of Imereti, in western Georgia, where he hailed from.

George Rogers Clark: George Rogers Clark (November 19, 1752 – February 13, 1818) was a surveyor, soldier, and militia officer from Virginia who became the highest ranking American military officer on the northwestern frontier during the American Revolutionary War.  He served as leader of the militia in Kentucky (then part of Virginia) throughout much of the war.  Clark is best known for his celebrated captures of Kaskaskia (1778) and Vincennes (1779) during the Illinois Campaign, which greatly weakened British influence in the Northwest Territory.  Because the British ceded the entire Northwest Territory to the United States in the 1783 Treaty of Paris, Clark has often been hailed as the "Conqueror of the Old Northwest".

Karol Rómmel: Karol Rómmel (Russian: Карл Альфонсович Руммель , German: "Karol von Rummel" ; 1888–1967) was a Polish and Russian military officer, sportsman and horse rider.  He competed in the 1912 Summer Olympics (in the Russian team), the 1924 Summer Olympics, and in the 1928 Summer Olympics (for Poland).  As a military officer he served with distinction in World War I and the Polish-Bolshevist War.

Angus McDonald (United States Army major): Angus McDonald (December 30, 1769 – October 14, 1814) was an American military officer, landowner, and planter in the U.S. state of Virginia.  McDonald served as a military officer during the War of 1812 following his appointment by United States President James Madison.  McDonald was the son of Virginia military officer and frontiersman Colonel Angus McDonald and the father of Colonel Angus William McDonald, a commander in the Confederate States Army during the American Civil War.

Isaac Parsons (American military officer): Isaac Parsons (January 7, 1814 – April 24, 1862) was an American planter, politician, and military officer in the U.S. state of Virginia (now West Virginia).  Parsons served as a justice of the peace of Hampshire County's District 3 from 1852 to 1853.  He later served as a member of the Virginia House of Delegates representing Hampshire County from 1854 until 1857.  Parsons was the grandson of Virginia House Delegate Isaac Parsons (1752–1796), the great-grandson of Colonial Virginia military officer William Foreman (died 1777), and the grandfather of First Lady of West Virginia, Edna Brady Cornwell (1868–1958).

Gudmund Schnitler: Gudmund Schnitler (10 June 1868 – 4 November 1925) was a Norwegian military officer and war historian.  He was born in Oslo as the son of military officer and historian Didrik Thomas Johannes Schnitler.  Among his publications is a continuation of his father's series "Almindelig krigshistorie" (volume 5, published in 1905, covering the period from 1650 to 1792).  His book on World War I, "Verdenskrigen 1914–18" from 1924, has been translated into several languages.

Angus William McDonald: Angus William McDonald (February 14, 1799 – December 1, 1864) was a 19th-century American military officer and lawyer in the U.S. state of Virginia.  He also served as a colonel in command of the Confederate States Army's 7th Virginia Cavalry during the American Civil War.  McDonald was appointed to serve in a number of prominent political positions including a superintendent overseeing the construction of the Northwestern Turnpike and a commissioner representing Virginia in its boundary dispute with Maryland.  McDonald was the grandson of Virginia military officer and frontiersman, Angus McDonald (1727–1778) and the father of United States Fish Commissioner Marshall McDonald (1835–1895).

Koboko: Koboko is a town in Northern Region of Uganda.  It is the main municipal, administrative and commercial centre of Koboko District.  Koboko is also the hometown of former dictator Idi Amin who ruled Uganda between 1971 and 1979.

Question: Which military officer hailed from Koboko?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "officer_name": {
      "type": "string",
      "description": "The name of the military officer."
    },
    "hometown": {
      "type": "string",
      "description": "The town the officer hailed from."
    },
    "roles": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of roles or positions held by the officer."
    },
    "presidency_period": {
      "type": "object",
      "properties": {
        "start_year": {
          "type": "integer",
          "description": "The start year of the officer's presidency."
        },
        "end_year": {
          "type": "integer",
          "description": "The end year of the officer's presidency."
        }
      },
      "required": [
        "start_year",
        "end_year"
      ],
      "additionalProperties": false,
      "description": "The period during which the officer served as president."
    }
  },
  "required": [
    "officer_name",
    "hometown",
    "roles",
    "presidency_period"
  ],
  "additionalProperties": false
}
