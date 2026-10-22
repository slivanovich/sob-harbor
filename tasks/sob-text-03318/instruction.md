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
Cervia Air Base: Cervia Air Base (ICAO: LIPC) is an air base of the Italian Air Force (Aeronautica Militare).  It is located in northern Italy, approximately 6 km southwest of Cervia, in the province of Ravenna (Emilia-Romagna).  It was the home of the 5th Fighter Wing, which flew leased US Air Force Lockheed Martin F-16 Falcon.  It is also a NATO air base and is visited by other NATO air forces on a routine basis.  After Italy returned the leased F-16 to the US Air Force the 5th Fighter Wing was disbanded and in its place the 1st Special Air Brigade moved to Cervia.  Along with the 1st Special Air Brigade arrived the 15th CSAR Wing - the Italian air force's Combat Search and Rescue wing.

Ralph Royce: Ralph Royce (28 June 1890 – 7 August 1965) was a United States Army Air Forces general during World War II.  A West Point graduate who learned to fly in 1915–16, he served with the 1st Aero Squadron in the Pancho Villa Expedition and later led it on the Western Front.  During World War II as a brigadier general, he led the Royce special mission to Mindanao, in which a small force of bombers flew from Australia to attack Japanese targets in the Philippines.  Later he was Deputy Commander of the Ninth Air Force and commanded the 1st Provisional Tactical Air Force.

Billy Mitchell: William Lendrum "Billy" Mitchell (December 29, 1879 – February 19, 1936) was a United States Army general who is regarded as the father of the United States Air Force.

Marine Aviation Training Support Group 33: Marine Aviation and Training Support Group 33 (MATSG-33) is a United States Marine Corps aviation training group that was originally established during World War II as Marine Aircraft Group 33 (MAG-33).  Fighter squadrons from MAG-33 fought most notably during the Battle of Okinawa and also as the first Marine aviation units to support the Korean War when they arrived as part of the 1st Provisional Marine Brigade.  They helped stabilize the United Nations positions during the Battle of Pusan Perimeter and fought in Korea for the remainder of the war.  At some point in the 1960s, the group was deactivated and was not reactivated until 2000, when Marine Aviation Training Support Group at Naval Air Station Oceana, Virginia was renamed MATSG-33.

1st Reconnaissance Squadron (disambiguation): The 1st Reconnaissance Squadron is an active United States Air Force unit, originally organized as the 1st Provisional Aero Squadron in 1913.  It has held this designation since September 1991.

11th Mechanized Corps (Soviet Union): The 11th Mechanized Corps was formed from March to September 1932 from the 11th Rifle Division in Leningrad, one of the first two Red Army mechanized corps.  The corps was commanded by division commander Komkor Kasyan Chaykovsky and its chief of staff was Mikhail Bakshi.  The 31st Mechanized Brigade was formed from the 32nd Rifle Regiment named for Volodarsky, the 32nd Mechanized Brigade from the 33rd Rifle Regiment named for Voskov, the 33rd Rifle and Machine Gun Brigade from the 31st Rifle Regiment named for Uritsky.  The 31st Brigade was equipped with the T-26 and the 32nd Brigade was equipped with the BT-2.  The corps at the time had a total of 220 tanks.  On 1 January 1933 the 83rd Aviation Group was attached the corps, and was later reformed into the Motor-Mechanized Squadron.  By March of that year the brigades were based in Tsarskoye Selo, Slutsk, and Stary Peterhof, while the corps headquarters and rear units were still in Leningrad.  In December, the 32nd Brigade's 1st Tank Battalion was transferred to the 6th Mechanized Brigade in the Special Red Banner Far Eastern Army.  On 16 January 1934 the corps received the honorific "Leningrad", the 31st Brigade received the honorific "named for Uritsky", the 32nd Brigade the honorific "named for Volodarsky", and the 33rd Brigade the honorific "named for Voskov".

1st Provisional Marine Brigade: The 1st Provisional Marine Brigade was a Marine infantry brigade of the United States Marine Corps (USMC) that existed periodically from 1912 to 1950.  It was an ad hoc unit formed for specific operations and not considered a "permanent" USMC unit.

157th Maneuver Enhancement Brigade: The 157th Maneuver Enhancement Brigade, also known as the Iron Brigade, is based out of Milwaukee, Wisconsin.  It was formerly known as the 57th Field Artillery Brigade, at which time its subordinate organizations included the 1st Battalion, 126th Field Artillery Regiment and the 1st Battalion, 121st Field Artillery Regiment from the Wisconsin Army National Guard, plus the 1st Battalion, 182nd Field Artillery Regiment of the Michigan Army National Guard.  Not to be confused with the famous "Iron Brigade" of the Civil War, the 57th Field Artillery Brigade is also known as the "Iron Brigade," a nickname traditionally given to crack artillery units in the Civil War.  It was during World War I that the 57th Field Artillery Brigade earned its nickname as it spent many hours at the front and fired more artillery rounds than any brigade in the American Army.

1st Provisional Air Brigade: The 1st Provisional Air Brigade was a temporary unit of the United States Army Air Service, commanded by Col. Billy Mitchell, operating out of Langley Field, Virginia, that was used in to demonstrate the vulnerability of ships to aerial attack when, in July 1921, the "unsinkable" German dreadnought SMS "Ostfriesland" was sent to the bottom of the Atlantic Ocean by bombardment.  Other targets included the German destroyer SMS G-102, the SMS "Frankfurt", and the USS "Iowa".

Edward A. Craig: Edward Arthur Craig (November 22, 1896 — December 11, 1994) was a commissioned officer in the United States Marine Corps, and a decorated combat veteran of World War II and the Korean War who eventually attained the rank of Lieutenant General.  Craig is best known as the general who commanded the 1st Provisional Marine Brigade during its actions in the Korean War.

Question: The gentleman who commanded the 1st Provisional Air Brigade was regarded as what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "commander_name": {
      "type": "string",
      "description": "The name of the individual who commanded the unit."
    },
    "commander_rank": {
      "type": "string",
      "description": "The rank of the commander at the time of commanding the unit."
    },
    "unit_commanded": {
      "type": "string",
      "description": "The name of the unit that was commanded."
    },
    "regarded_as_title": {
      "type": "string",
      "description": "The title or recognition the commander was regarded as."
    }
  },
  "required": [
    "commander_name",
    "commander_rank",
    "unit_commanded",
    "regarded_as_title"
  ],
  "additionalProperties": false
}
