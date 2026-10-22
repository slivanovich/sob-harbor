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
Autocannon: An autocannon or automatic cannon is a large, fully automatic, rapid-fire projectile weapon that fires armour-piercing or explosive shells, as opposed to the bullet fired by a machine gun.  Autocannon often have a larger calibre than a machine gun (e.g., 20 mm or greater), but are usually smaller than a field gun or other artillery.  When used on its own, the word "autocannon" indicates a single-barrel weapon.  When multiple rotating barrels are involved, the word "rotary" is added, and such a weapon is referred to as a "rotary autocannon."  Modern autocannon are typically not single soldier-portable or stand-alone units, rather they are usually vehicle-mounted, aircraft-mounted, or boat-mounted, or even remote-operated as in some naval applications.  As such, ammunition is typically fed from a belt to reduce reloading or for a faster rate of fire, but a magazine remains an option.  They can use a variety of ammunition: common shells include high-explosive dual-purpose types (HEDP), any variety of armour-piercing (AP) types, such as composite rigid (APCR) or discarding sabot types (APDS).

85 mm air defense gun M1939 (52-K): The 85 mm air defense gun M1939 (52-K) (Russian: 85-мм зенитная пушка обр.  1939 г.  (52-К) ) was an 85-mm Soviet air defense gun, developed under guidance of leading Soviet designers M. N. Loginov and G. D. Dorokhin.  This gun was successfully used throughout the German-Soviet War against level bombers and other high- and medium-altitude targets.  In emergencies they were utilized as powerful anti-tank weapons.  The barrel of the 52-K was the basis for the family of 85-mm Soviet tank guns.  Crews of 85-mm AD guns have claimed to have shot down 4,047 Axis aircraft (likely over-reported by factor of 3 to 10).  The claimed quantity of 85-mm ammunition required to shoot down one enemy plane was 598 rounds, although actual number may be in range 2000-7000 rounds per kill.  After the war some 52-Ks were refitted for peaceful purposes as anti-avalanche guns in mountainous terrain.

Vehicle registration plates of Khorasan: At the time of the creation of the new license plate format, the former Khorasan Province was given codes 12 for Mashhad, 32, 42 and 52 as reserve.  However, soon after the province was divided up into three: Razavi Khorasan, North Khorasan, and South Khorasan.  Therefore all codes dedicated to North Khorasan and South Khorasan were withdrawn and stored for future use in Razavi Khorasan.  The reserve code 52 was assigned to South Khorasan.  Qom Province's assigned reserve code 26 was assigned to North Khorasan, and Qom's reserve code 36 was assigned as a replacement for code 52 as Razavi Khorasan's reserve.  The reason for this was the much slower than expected use of Qom Province's initially assigned code 16.  In Razavi Khorasan, after codes 12, 32, and 42 were fully used, some time in August 2016, code 36 was also exhausted.  Therefore it was decided to assign the province code 74, from Yazd Province's reserve code.

Obukhovskii 12&quot;/52 Pattern 1907 gun: The Obukhovskii 12"/52 Pattern 1907 gun was a 12 in 52 caliber naval gun.  It was the most powerful gun to be mounted aboard battleships of the Imperial Russian Navy and later the Soviet Navy during both world wars.  It was later modified by the Soviets and employed as coastal artillery and as a railway gun during World War II.

5&quot;/54 caliber Mark 42 gun: The Mark 42 5"/54 caliber gun (127mm) is a naval gun (naval artillery) mount used by the United States Navy and other countries.  It consisted of the Mark 18 gun and Mark 42 gun mount.  United States naval gun terminology indicates the gun fires a projectile 5 in in diameter, and the barrel is 54 calibers long (barrel length is 5" × 54 = 270" or 6.9 meters.)  In the 1950s a gun with more range and a faster rate of fire than the 5"/38 caliber gun used in World War II was needed, therefore, the gun was created concurrently with the 3"/70 Mark 26 gun for different usages.  The 5"/54 Mk 42 is an automatic, dual-purpose (air / surface target) gun mount.  It is usually controlled remotely from the Mk 68 Gun Fire Control System, or locally from the mount at the One Man Control (OMC) station.

FG 42: The FG 42 (German: "Fallschirmjägergewehr" 42, "paratrooper rifle 42") is a selective-fire automatic rifle produced in Nazi Germany during World War II.  The weapon was developed specifically for the use of the Fallschirmjäger airborne infantry in 1942 and was used in very limited numbers until the end of the war.

Grossfuss Sturmgewehr: Grossfuss Sturmgewehr was a prototype assault rifle designed during World War II by Kurt Horn at the Grossfuss company () better known for their contribution to the German arsenal made with the MG 42.

7.62×45mm: The 7.62×45mm (designated as the 7,62 × 45 by the C.I.P.) is a rimless bottlenecked intermediate rifle cartridge developed in Czechoslovakia.  It is fired by the Czech vz.  52 rifle, Vz.  52 machine gun and ZB-530 light machine gun.  The round was later dropped from use when the Czech converted to the standard Warsaw Pact round, the 7.62×39mm (fired by vz.  52/57 rifle and vz.  52/57 light machine gun).  Its muzzle velocity and muzzle energy are slightly higher than that of the 7.62×39mm cartridge.

Sturmgewehr 52: The Sturmgewehr 52 (STG-52) was a battle rifle manufactured by the government-owned W+F Bern of Switzerland.  It was chambered in the 7.5mm Kurzpatrone cartridge and later the 7.5mm Swiss service round as the Sturmgewehr 54, which was fed from the right-hand side.  The Sturmgewehr 52 was heavily patterned after the German FG 42 as it was fed from the side from a 30- or 40-round magazine and was also fitted with a muzzle attachment capable of launching rifle grenades.

7.5 cm KwK 42: The 7.5 cm KwK 42 L/70 (from "7.5 cm Kampfwagenkanone 42 L/70") was a 7.5 cm calibre German tank gun developed and built by Rheinmetall-Borsig AG in Unterlüß during the Second World War.  The gun was used to equip the SdKfz.171 Panzerkampfwagen V Panther medium tank and the SdKfz.162/1 Jagdpanzer IV/70(A)/(V) tank destroyer.  When mounted on a tank destroyer it was designated as the 7.5 cm Pak 42 ("7.5 cm Panzerabwehrkanone 42") anti-tank gun.

Question: The Sturmgewehr 52 and the FG 42 are both types of which kind of gun?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "gun_type": {
      "type": "string",
      "description": "The common type of gun for both weapons."
    },
    "weapons": {
      "type": "array",
      "description": "Details about each weapon mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the weapon."
          },
          "classification": {
            "type": "string",
            "description": "The specific classification of the weapon as found in the text."
          }
        },
        "required": [
          "name",
          "classification"
        ],
        "additionalProperties": false
      }
    },
    "common_characteristic": {
      "type": "string",
      "description": "A brief explanation of why they are classified under the same type."
    }
  },
  "required": [
    "gun_type",
    "weapons",
    "common_characteristic"
  ],
  "additionalProperties": false
}
