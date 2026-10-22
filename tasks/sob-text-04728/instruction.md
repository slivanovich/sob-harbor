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
Herbert Lumsden: Lieutenant-General Herbert Lumsden & Bar, MC (8 April 1897 – 6 January 1945) was a senior British Army officer who fought in both World War I and World War II.  He was the most senior British Army combat casualty of the Second World War.

Polish contribution to World War II: The European theatre of World War II opened with the German invasion of Poland on Friday September 1, 1939 and the Soviet invasion of Poland on September 17, 1939.  The Polish Army was defeated after more than a month of fierce fighting.  After Poland had been overrun, a government-in-exile (headquartered in Britain), armed forces, and an intelligence service were established outside of Poland.  These organizations contributed to the Allied effort throughout the war.  The Polish Army was recreated in the West, as well as in the East (after the German invasion of the Soviet Union).

Tony Hibbert (British Army officer): Tony Hibbert, MBE MC (6 December 1917 – 12 October 2014), was a British Army officer who fought in the Second World War.  During a military career that began in 1935 and ended in 1947, Hibbert saw action in the Battle of France, the North African Campaign, the Italian Campaign and Operation Market Garden.  After these battles, he led a T-Force unit in Operation Eclipse, a campaign carried out by the Allies shortly before V-E Day.

Colin Muir Barber: Lieutenant General Sir Colin Muir Barber & Bar (27 June 1897 – 5 May 1964) was a senior British Army officer who fought in both World War I and World War II where he commanded the 15th (Scottish) Infantry Division during their actions across Northwest Europe, from August 1944 until Victory in Europe Day in May 1945.  Barber was reputed to be the tallest officer in the British Army (at 6 ft ), and thus earned the ironic nickname "Tiny".

Günther Blumentritt: Günther Blumentritt (10 February 1892 – 12 October 1967) was an officer in World War I, who became a Staff Officer under the Weimar Republic and went on to serve as a general for Nazi Germany during World War II.  He served throughout the war, mostly on the Western Front, and mostly as a Staff Officer, though he was eventually given his own Corps and made a "General der Infanterie".  Blumentritt was instrumental in planning the 1939 German invasion of Poland and the 1940 invasion of France, he participated in Operation "Barbarossa", and afterward bore a large part of the responsibility for planning the defense of the Atlantic Wall and Normandy.  After the war, Blumentritt gave an affidavit at the Nuremberg Trials, though he never testified in person, and then later helped in the rearmament of Germany during the Cold War and the development of the modern German army.

The Darkest Hour: The Darkest Hour is a phrase coined by British prime minister Winston Churchill to describe the period of World War II between the fall of France in 1940 and the Nazi invasion of the Soviet Union in 1941, when the British Empire stood alone against Nazi Germany and the Axis Powers in Europe.  The length of time between the fall of France in June 1940 and the German invasion of the Soviet Union in June 1941 measured 363 days, or 11 months and 28 days.  It is particularly used for the time when the United Kingdom was under direct threat of invasion; following the evacuation of the British Army from Dunkirk and prior to victory in the Battle of Britain.  The darkest moment is usually considered to have been 10 May 1941, when over 1,500 civilians died in Luftwaffe bombing raids on London alone.

Ronald Forbes Adam: General Sir Ronald Forbes Adam, 2nd Baronet (30 October 1885 – 26 December 1982) was a senior British Army officer whose career spanned World War I and World War II.  He had an important influence on the conduct of the British Army in World War II as a result of his long tenure as Adjutant General, responsible for the army's organisation and administration, as well as through being a close confidant of Field Marshal Sir Alan Brooke, the Chief of the Imperial General Staff (CIGS), the professional head of the British Army, from December 1941 until the end of the war.

Pyotr Berestov: Pyotr Filippovich Berestov (Russian: Пётр Филиппович Берестов ; December 21 [O.S. December 8] 1896 , Berestovo – November 26, 1961, Zaporozhye) was a Red Army major general during the Second World War.  Drafted into the Imperial Russian Army in 1917, Berestov participated in the Russian Revolution.  He was drafted into the Red Army, fighting in the Russian Civil War and the Polish–Soviet War.  He became a Red Army officer and served in several positions during the interwar period.  Berestov was arrested and released during the Great Purge.  He fought in the Winter War as a regimental commander.  In the early days after the German invasion of the Soviet Union, he was given command of a People's Militia regiment, which was converted into a regular regiment.  Berestov led the regiment in the early period of the Battle of Moscow and transferred to lead a regiment of the 82nd Motor Rifle Division.  Berestov became the division's commander and in the spring of 1942 briefly led the 50th Rifle Division.  In April, he took command of the 331st Rifle Division, which he led during the rest of the war.  For his leadership, Berestov was awarded the title Hero of the Soviet Union in late June 1945.  Postwar he commanded the 72nd Guards Rifle Division, which was downsized into a brigade, and the 43rd Guards Rifle Brigade, which became the 113th Guards Rifle Division.  Berestov retired in 1955 and lived in Zaporozhye until his death in 1961.

Battle of France: The Battle of France, also known as the Fall of France, was the German invasion of France and the Low Countries during the Second World War.  In six weeks from 10 May 1940, German forces defeated Allied forces by mobile operations and conquered France, Belgium, Luxembourg and the Netherlands, bringing land operations on the Western Front to an end until 6 June 1944.  Italy entered the war on 10 June 1940 and attempted an invasion of France.

Ivan Maslennikov: Ivan Ivanovich Maslennikov (Russian: Иван Иванович Масленников ; September 16, 1900 – April 16, 1954), General of the Army, was a Soviet military and NKVD commander of Army and Front level during World War II.  A career Red Army officer, Maslennikov was transferred to NKVD system in 1928, and remained there until the German invasion of 1941, progressing from a counter-guerrilla squadron commander to the chief of NKVD troops.  After a mixed career in field troops of World War II and three post-war years, Maslennikov returned to NKVD in 1948 and stayed there, despite political changes, until his suicide in 1954.

Question: Tony Hibbert, a British Army officer during World War II, fought in what German invasion of France?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "officer_name": {
      "type": "string",
      "description": "The name of the British Army officer."
    },
    "officer_nationality": {
      "type": "string",
      "description": "The nationality of the officer."
    },
    "conflict": {
      "type": "string",
      "description": "The major conflict the officer participated in."
    },
    "invasion_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the German invasion of France."
        },
        "also_known_as": {
          "type": "string",
          "description": "Another common name for the invasion."
        },
        "start_date": {
          "type": "string",
          "description": "The start date of the invasion."
        },
        "duration_weeks": {
          "type": "integer",
          "description": "The duration of the invasion in weeks."
        },
        "countries_invaded": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of countries invaded during this operation."
        }
      },
      "required": [
        "name",
        "also_known_as",
        "start_date",
        "duration_weeks",
        "countries_invaded"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "officer_name",
    "officer_nationality",
    "conflict",
    "invasion_details"
  ],
  "additionalProperties": false
}
