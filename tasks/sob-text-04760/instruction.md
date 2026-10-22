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
Pakistan Armed Forces Eastern Command: The Eastern Military High Command of the Pakistan Armed Forces was a field-level military command headed by an appointed senior 3-star officer, who was designated the Unified Commander of the Eastern Military High Command.  After the partition of India by Great Britain, the Islamic Republic of Pakistan was divided into two territories separated by 1000 mi (prior to the independence of Bangladesh in 1971).  Most of the assets of the Pakistan armed forces were stationed in West Pakistan; the role of the Pakistan armed forces in East Pakistan was to hold out until Pakistan was defeated by India in the west (in case of war).  The Pakistan armed forces created the Eastern Military High Command, with one unified commander of the Pakistan armed forces responsible for the command.  The armed forces (particularly the Pakistan Army), had drawn up a plan to defend Dhaka by concentrating all their forces along the Dhaka Bowl (the area surrounded by the rivers Jamuna, Padma and Meghna).

OB West: The German Army Command in the West ("Oberbefehlshaber West" (German: initials OB West) was the overall command of the Westheer, the German Armed Forces on the Western Front during World War II.  It was directly subordinate to German Armed Forces High Command.  The area under the command of the OB West varied as the war progressed.  At its farthest extent it reached the French Atlantic coast.  By the end of World War II in Europe it was reduced to commanding troops in Bavaria.

Ioannis Davos: Ioannis Davos (Greek: Ιωάννης Ντάβος , 1918 – 15 January 2008) was a Greek Army officer who rose to the rank of full General, and held the posts of Chief of the Hellenic Army General Staff and of the Armed Forces High Command.

Supreme Command (Kingdom of Yugoslavia): The Supreme Command or High Command () was the highest headquarters of the armed forces of the Kingdom of Yugoslavia during wartime.  According to regulations, upon activation the general staff became the staff of the Supreme Command and the Chief of the General Staff became Chief of Staff of the Supreme Command ("Načelnik štaba Vrhovne komande").  While the king was at all times commander-in-chief of the armed forces, during wartime the Chief of Staff of the Supreme Command was the "de facto" supreme commander.

Wilhelm Keitel: Wilhelm Keitel (22 September 1882 – 16 October 1946) was a German field marshal who served as Chief of the Armed Forces High Command ("Oberkommando der Wehrmacht" or OKW) in Nazi Germany during World War II.  According to David Stahel, Keitel was "well known and [...] reviled as Hitler's dependable mouthpiece and habitual yes-man" among his military colleagues.

Telmo Vargas: General Telmo Oswaldo Vargas Benalcázar (9 October 1912 – 9 August 2013) was Chief of Staff of the Armed Forces of Ecuador, who overthrew the military junta of Ramón Castro Jijón on 29 March 1966.  After Castro Jijón turned over power to army high command, the high command appointed Clemente Yerovi as president of the civilian junta.  As the leader of the army high command, Vargas is considered by some to have briefly served as head of state of Ecuador.  He died on 9 August 2013 at the age of 100.

Alfred Jodl: Alfred Josef Ferdinand Jodl (   ; 10 May 1890 – 16 October 1946) was a German general and war criminal during World War II, who served as the Chief of the Operations Staff of the Armed Forces High Command (Oberkommando der Wehrmacht).

Oberkommando des Heeres: The Oberkommando des Heeres (OKH) was the Supreme High Command of the German Army.  It was founded in 1935 as a part of Adolf Hitler's re-militarisation of the Third Reich.  Its commander held the title "Oberbefehlshaber des Heeres", Supreme High Commander of the Army.  From 1938 OKH was together with OKL "Oberkommando der Luftwaffe", Supreme High Command of the Air Force and OKM "Oberkommando der Marine", Supreme High Command of the Navy, formally subordinated to the OKW "Oberkommando der Wehrmacht", Supreme High Command of all Armed Forces (with exception of the Waffen-SS).  During the war OKH had the responsibility of strategic planning of Armies and Army Groups, while the General Staff of the OKH managed operational matters.  Each German Army also had an "Armeeoberkommando", Army Command, or AOK.  Until the German defeat at Moscow in December 1941, OKH and its staff was "de facto" the most important unit within the German war planning.  OKW ("Oberkommando der Wehrmacht", Supreme High Command of the Armed Forces) then took over this function for theaters other than the Russian front.

Ernst John von Freyend: Ernst John von Freyend (25 March 1909– 24 March 1980) was a German Oberkommando der Wehrmacht officer who served during World War II as the adjutant to Field Marshal Wilhelm Keitel.  He is notable for unwittingly helping to place the 20 July plot bomb that was intended to kill Adolf Hitler.

Royal Gendarmerie of Cambodia: The Royal Gendarmerie of Cambodia (Khmer: កងរាជអាវុធហត្ថ ), or "Military Police", is a branch of the Royal Cambodian Armed Forces and it is responsible for the maintenance of public order and internal security in Cambodia.  The paramilitary unit has a strength of 10,000 soldiers deployed in all provinces.  Its headquarters is located in Phnom Penh, with the unit's chain of command through the Royal Cambodian Armed Forces High Command.  The Gendarmerie is under the direct supervision of a commander with an equivalent rank to Lieutenant-General.  The High Command is responsible for monitoring all Gendarmerie units as well as general training. The current commander of Gendarmerie is lieutenant-General Sao Sokha, a former bodyguard and personal advisor to Cambodian Prime minister Hun Sen.

Question: Ernst John von Freyend was adjutant to which Chief of the Armed Forces High Command during WWII?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "adjutant_name": {
      "type": "string",
      "description": "The name of the adjutant."
    },
    "superior_officer_name": {
      "type": "string",
      "description": "The name of the superior officer."
    },
    "superior_officer_title": {
      "type": "string",
      "description": "The title held by the superior officer."
    },
    "military_organization": {
      "type": "string",
      "description": "The military organization the officers belonged to."
    },
    "conflict": {
      "type": "string",
      "description": "The historical conflict during which the service took place."
    }
  },
  "required": [
    "adjutant_name",
    "superior_officer_name",
    "superior_officer_title",
    "military_organization",
    "conflict"
  ],
  "additionalProperties": false
}
