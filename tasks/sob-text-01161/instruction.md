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
Sikorsky S-1: The Sikorsky S-1 was the first fixed wing aircraft design by Igor Sikorsky.  In February 1910 work began on the pusher configured biplane powered by a 15 hp Anzani three-cylinder, air-cooled engine.  The machine was completed in April and Sikorsky began his first attempts at flight.  In early May during a take-off attempt on a windy day the machine briefly became airborne due mostly to the fact it had a favorable headwind.  Further attempts were less successful and Sikorsky disassembled it saving the main wing section to construct the S-2.

Sikorsky S-37: The Sikorsky S-37 was an American twin-engine aircraft built by the Sikorsky Manufacturing Corporation.  Both examples of the series were completed in 1927.  The S-37 was specifically designed to compete for the Orteig Prize and would be the last land based fixed-wing aircraft Sikorsky would produce.

Tiltrotor: A tiltrotor is an aircraft which generates lift and propulsion by way of one or more powered rotors (sometimes called "proprotors") mounted on rotating engine pods or nacelles usually at the ends of a fixed wing or an engine mounted in the fuselage with drive shafts transferring power to rotor assemblies mounted on the wingtips.  It combines the vertical lift capability of a helicopter with the speed and range of a conventional fixed-wing aircraft.  For vertical flight, the rotors are angled so the plane of rotation is horizontal, lifting the way a helicopter rotor does.  As the aircraft gains speed, the rotors are progressively tilted forward, with the plane of rotation eventually becoming vertical.  In this mode the wing provides the lift, and the rotor provides thrust as a propeller.  Since the rotors can be configured to be more efficient for propulsion (e.g. with root-tip twist) and it avoids a helicopter's issues of retreating blade stall, the tiltrotor can achieve higher speeds than helicopters.

Aerial firefighting: Aerial firefighting is the use of aircraft and other aerial resources to combat wildfires.  The types of aircraft used include fixed-wing aircraft and helicopters.  Smokejumpers and rappellers are also classified as aerial firefighters, delivered to the fire by parachute from a variety of fixed-wing aircraft, or rappelling from helicopters. Chemicals used to fight fires may include water, water enhancers such as foams and gels, and specially formulated fire retardants such as Phos-Chek.

Sikorsky S-30: The Sikorsky S-30 was a proposed aircraft design by Igor Sikorsky to be built by the Sikorsky Manufacturing Corporation at Roosevelt, New York in 1925.  The twin engine biplane was to have been used on mail routes or configured as a commercial passenger airliner.  No examples of the S-30 were ever manufactured.

Strafing: Strafing is the military practice of attacking ground targets from low-flying aircraft using aircraft-mounted automatic weapons ranging from machine guns (5mm to 20mm) to autocannons or rotary cannons (typically 20mm to 37mm).  This means that, although ground attack using automatic weapons fire is very often accompanied with bombing or rocket fire, the term "strafing" does not specifically include the last two.  The term "strafing" can cover either fixed guns, or aimable (flexible) guns.  Fixed guns firing directly ahead tend to be more predominant on fixed wing aircraft, while helicopters tend to use aimable weapons which can be fired in many different directions independent of the direction the aircraft is pointing in (in most cases, flexible guns on a fixed wing aircraft are for defense purposes only, although they can sometimes be used to fire on ground targets to limited effect).  Some fixed wing aircraft, like fighter-bombers, are capable of flying either air-combat missions or ground attack missions (P-47 Thunderbolt), while others are dedicated ground-attack types (Il-2 Shturmovik).  In cases where an aircraft is capable of both types of combat, when it is assigned to a ground attack role, and thus expected to be using the guns mostly for strafing, the fixed weapons are often mounted so that the convergence point is lower and at a greater range than would be used for air combat.  This is helpful because it allows the pilot to aim at a target without having to dive towards the ground as steeply, decreasing the risk of collision with the ground and increasing the amount of firing time available before having to pull up, and it also increases the range from the target, helping avoid anti-aircraft fire and potential damage from exploding targets.  Because of the low altitude and relatively low airspeed required for accurate strafing, it is very risky for the pilot, who is exposed not only to the risk of flight-into-terrain and obstacles such as power lines, but also to anti-aircraft weapons, including surface-to-air missiles (both vehicle mounted and hand-held), anti-aircraft artillery and small caliber weapons fire (such as machine guns and small arms).  Planes purposely designed for ground attack may include additional armour around and underneath the cockpit and other vulnerable areas such as engines to protect the pilot and key flight components, while aircraft designed mostly for air combat tend to have most of their armor placed to protect directly ahead or to the rear, where fire from other aircraft is most likely, leaving them more vulnerable to fire from directly below or to the sides, where much ground fire often comes from.

Igor Sikorsky: Igor Ivanovich Sikorsky (Russian: И́горь Ива́нович Сико́рский ; ] , "Ígor' Ivánovič Sikórskij"; , "Ihor Ivanovych Sikorskyi"; May 25, 1889 – October 26, 1972), was a Russian-American aviation pioneer in both helicopters and fixed-wing aircraft.  First success came with the S-2, the second aircraft of his design and construction.  His fifth airplane, the S-5, won him national recognition as well as F.A.I. license Number 64.  His S-6-A received the highest award at the 1912 Moscow Aviation Exhibition.  and in the fall of that year the aircraft won for its young designer, builder and pilot first prize in the military competition at Petrograd.

Helicopter Underwater Escape Training: Helicopter Underwater Egress Training in the United States, and Helicopter Underwater Escape Training in most other countries, (often abbreviated HUET, pronounced "hue-wet", "hue-way" or "you-way") is training provided to helicopter flight crews, offshore oil and gas industry staff law enforcement personnel, and military personnel who are regularly transported by helicopters over water.  As the name implies, the purpose is to prepare them for emergency exit in the case of a crash landing over water.  While the training may be taken by crew and frequent passengers in all small aircraft that could ditch over water, a fixed wing aircraft such as a seaplane or small jet is not as prone to rollover as quickly or sink as rapidly as a helicopter with its main rotor on top of the aircraft.  In addition, due to the slow speed of helicopters versus fixed wing aircraft and the lower height above the water, their cabins have a greater chance of being intact with passengers inside when ditched in the water.

Sikorsky S-2: The Sikorsky S-2 was the second fixed wing aircraft designed by Igor Sikorsky using the main wing section from the S-1 and a 25 hp Anzani three-cylinder engine in a tractor configuration.  During the first flight attempt on June 3, 1910 the biplane reached a height of two to four feet and traveled approximately 200 yards.  After several successful flights the S-2 was completely destroyed on June 30 when Sikorsky inadvertently stalled the underpowered aircraft at an altitude of 70 feet.

Tailplane: A tailplane, also known as a horizontal stabiliser, is a small lifting surface located on the tail (empennage) behind the main lifting surfaces of a fixed-wing aircraft as well as other non-fixed-wing aircraft such as helicopters and gyroplanes. Not all fixed-wing aircraft have tailplanes.  Canards, tailless and flying wing aircraft have no separate tailplane, while in v-tail aircraft the vertical stabilizer, rudder, and the tail-plane and elevator are combined to form two diagonal surfaces in a V layout.

Question: The Sikorsky S-1 was the first fixed wing aircraft design by Igor Ivanovich Sikorsky, a Russian-American aviation pioneer in both helicopters and fixed-wing aircraft, first success came with which aircraft?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "pioneer_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the aviation pioneer."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the pioneer."
        },
        "pioneering_fields": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "The types of aircraft in which the pioneer made contributions."
        }
      },
      "required": [
        "name",
        "nationality",
        "pioneering_fields"
      ],
      "additionalProperties": false
    },
    "first_aircraft_design": {
      "type": "object",
      "properties": {
        "model_name": {
          "type": "string",
          "description": "The model name of the first aircraft designed."
        },
        "design_order": {
          "type": "integer",
          "description": "The sequential order of this design by the pioneer."
        },
        "aircraft_type": {
          "type": "string",
          "description": "The general type of the aircraft (e.g., fixed-wing)."
        }
      },
      "required": [
        "model_name",
        "design_order",
        "aircraft_type"
      ],
      "additionalProperties": false
    },
    "first_successful_aircraft": {
      "type": "object",
      "properties": {
        "model_name": {
          "type": "string",
          "description": "The model name of the aircraft that brought the pioneer their first success."
        },
        "design_order": {
          "type": "integer",
          "description": "The sequential order of this design by the pioneer."
        },
        "aircraft_type": {
          "type": "string",
          "description": "The general type of the aircraft (e.g., fixed-wing)."
        }
      },
      "required": [
        "model_name",
        "design_order",
        "aircraft_type"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "pioneer_details",
    "first_aircraft_design",
    "first_successful_aircraft"
  ],
  "additionalProperties": false
}
