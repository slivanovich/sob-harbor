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
Fighter aircraft: A fighter aircraft is a military aircraft designed primarily for air-to-air combat against other aircraft, as opposed to bombers and attack aircraft, whose main mission is to attack ground targets.  The hallmarks of a fighter are its speed, maneuverability, and small size relative to other combat aircraft.

Otto Weiß (pilot): Otto Albert Bernhard Weiß (25 September 1907 – 19 August 1955) was a World War II Luftwaffe attack aircraft pilot and recipient of the coveted Knight's Cross of the Iron Cross with Oak Leaves (German: "Ritterkreuz des Eisernen Kreuzes mit Eichenlaub" ).  The Knight's Cross of the Iron Cross and its higher grade Oak Leaves was awarded to recognise extreme battlefield bravery or successful military leadership.  He was the first attack aircraft pilot so honored.  Weiß flew more than 500 combat missions with the Henschel Hs 123 and the Messerschmitt Bf 109.

List of fighter aircraft: This is a list of military aircraft that are primarily designed for air-to-air combat and thus does not include aircraft intended for other roles where they have some secondary air-to-air capability, such as with many ground attack aircraft.  The list includes fighter aircraft which are currently in "operational" service, those that have been "retired", designs that flew but were "abandoned" without having been used operationally, and future "project" aircraft still in development.  The list does not include projects that were cancelled before an aircraft was built or fictional aircraft.  They are listed alphabetically by manufacturer, but the table can be sorted by any column.

McDonnell Douglas F/A-18 Hornet: The McDonnell Douglas F/A-18 Hornet is a twin-engine supersonic, all-weather carrier-capable multirole combat jet, designed as both a fighter and attack aircraft (hence the F/A designation).  Designed by McDonnell Douglas (now Boeing) and Northrop, the F/A-18 was derived from the latter's YF-17 in the 1970s for use by the United States Navy and Marine Corps.  The Hornet is also used by the air forces of several other nations and, since 1986, by the U.S. Navy's Flight Demonstration Squadron, the Blue Angels.

Amy McGrath: Amy McGrath Henderson is a retired combat aviator in the United States Marines who was the first female marine to fly in an F-18 on a combat mission.  She served for 20 years in Marine Corps during which she flew 89 combat missions bombing al Qaeda and the Taliban.In 2016, she was inducted into the Aviation Museum of Kentucky's Hall of Fame and her military story is described in "Band of Sisters: American Women at War in Iraq".  She has announced her intention to run for the United States House of Representatives in 2017.

Airstrike: An airstrike or air strike is an offensive operation carried out by attack aircraft.  Air strikes are commonly delivered from aircraft such as fighters, bombers, ground attack aircraft, and attack helicopters.  The official definition includes all sorts of targets, including enemy air targets, but in popular usage the term is usually narrowed to a tactical (small-scale) attack on a ground or naval objective.  Weapons used in an airstrike can range from aircraft cannon and machine gun bullets, air-launched missiles to various types of bombs and even directed-energy weapons such as lasers.  It is also commonly referred to as an air raid.

Petlyakov Pe-2: The Petlyakov Pe-2 (Russian: Петляков Пе-2 ) was a Soviet light bomber used during World War II.  It was regarded as one of the best ground attack aircraft of the war and it was also successful in the roles of heavy fighter, reconnaissance and night fighter.  It was similar in many respects to the wooden British de Havilland Mosquito.  Pe-2s were manufactured in greater numbers (11,427 built) during the war than any other twin-engined combat aircraft except for the German Junkers Ju 88 and British Vickers Wellington.  The Pe-2 was fast, maneuverable and durable.  Several Communist nations flew the type after the war, when it became known by the NATO reporting name Buck.  Six captured Pe-2s were also transferred from the Germans to the Finnish Air Force during the Continuation War, with the serial code "PE-" and the unofficial nickname "Pekka-Eemeli".

B28 nuclear bomb: The B28, originally Mark 28, was a thermonuclear bomb carried by U.S. tactical fighter bombers, attack aircraft and bomber aircraft.  From 1962 to 1972 under the NATO nuclear weapons sharing program, American B28s also equipped six Europe-based Canadian CF-104 squadrons known as the RCAF Nuclear Strike Force.  It was also supplied for delivery by UK-based Royal Air Force Valiant and Canberra aircraft assigned to NATO under the command of SACEUR.  In addition, certain USN carrier based attack aircraft such as the A3D (later A-3B) Skywarrior, A4D (later A-4) Skyhawk, and A3J (later A-5A) Vigilante were equipped to carry the MK 28.

Light fighter: Light fighters are fighter aircraft towards the low end of the practical range of weight, cost, and complexity over which fighters are fielded.  The term lightweight fighter is more commonly used in the modern literature, and by example tends to imply somewhat more capable aircraft than light fighters at the very low end of the practical weight range, but the terms overlap and are sometimes used interchangeably.  Whatever term is used, the concept is to be on the generally lower half of the practical range, but still with carefully selected competitive features, in order to project highly effective force per unit of budget via an efficient design.  As well designed lightweight fighters have proven able to match or beat heavier aircraft plane for plane for many missions, and to significantly excel them in budgetary efficiency, light/lightweight fighters have proven to be a strategically valuable concept.  Attempting to scale this efficiency to still lower cost, some manufacturers have in recent years adopted the term “light fighter” to also refer to light primarily air-to-ground attack aircraft, some of which are modified trainer designs.

Fighter-bomber: A fighter-bomber is a fighter aircraft that has been modified, or used primarily, as a light bomber or attack aircraft.  It differs from bomber and attack aircraft primarily in its origins, as a fighter that has been adapted into other roles, whereas bombers and attack aircraft are developed specifically for bombing and attack roles.

Question: Who designed the fighter and attack aircraft that Amy McGrath Henderson flew?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "pilot_name": {
      "type": "string",
      "description": "The name of the pilot who flew the aircraft."
    },
    "aircraft_name": {
      "type": "string",
      "description": "The name of the aircraft flown by the pilot."
    },
    "aircraft_roles": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The primary roles of the aircraft (e.g., fighter, attack aircraft)."
    },
    "designers": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The companies or entities that designed the aircraft."
    }
  },
  "required": [
    "pilot_name",
    "aircraft_name",
    "aircraft_roles",
    "designers"
  ],
  "additionalProperties": false
}
