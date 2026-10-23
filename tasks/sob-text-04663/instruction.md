{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAichi E3A: The Heinkel HD 56 was a reconnaissance seaplane developed in Germany in 1929 to operate from warships of the Imperial Japanese Navy, which designated it the Type 90-1 Reconnaissance Seaplane or E3A.  It was a conventional single-bay biplane with staggered wings braced by N-type interplane struts.  The pilot and gunner sat in tandem, open cockpits. Heinkel designed the aircraft at the request of Aichi, in order to submit it as their entry in an IJN competition to select such an aircraft.  Heinkel built a single HD 56 prototype that was evaluated against the Nakajima Type 90-2 Reconnaissance Seaplane and the Kawanishi Type 90-3 Reconnaissance Seaplane.  The Heinkel design announced the winner in 1931, on the condition that Aichi would address some shortcomings, particularly a lack of range.  Refined versions of the \"losing\" Nakajima and Kawanishi designs would eventually see production and - in the case of the Nakajima design - in far greater numbers.\n\nNakajima A4N: The Nakajima A4N was a carrier-based fighter used by the Imperial Japanese Navy, and the last biplane designed by Nakajima.  The first prototype was completed in 1934, but due to engine trouble the aircraft did not see service until 1936.  Given the Nakajima internal designation Nakajima YM, the Japanese Navy designation was Type 95 Carrier-based Fighter.  A total of 221 were built.\n\nCAC Boomerang: The CAC Boomerang was a fighter aircraft designed and manufactured in Australia by the Commonwealth Aircraft Corporation between 1942 and 1945.  Approved for production shortly following the Empire of Japan's entry into the Second World War, the Boomerang was rapidly designed as to meet the urgent demands for fighter aircraft to equip the Royal Australian Air Force (RAAF).  The type holds the distinction of being the first combat aircraft to be both designed and constructed in Australia.\n\nSukhoi Su-57: The Sukhoi Su-57 (Russian: Сухой Су-57 ) is the designation intended for a stealth, single-seat, twin-engine jet multirole fighter aircraft designed for air superiority and attack operations.  The aircraft is the product of the PAK FA (Russian: ПАК ФА , Russian: Перспективный авиационный комплекс фронтовой авиации , \"Perspektivny Aviatsionny Kompleks Frontovoy Aviatsii\", literally \"Prospective Airborne Complex of Frontline Aviation\"), a fifth-generation fighter programme of the Russian Air Force.  Sukhoi's internal name for the aircraft is T-50.  The Su-57 will be the first aircraft in Russian military service to use stealth technology.  The fighter is planned to have supercruise, stealth, supermaneuverability and advanced avionics to overcome the prior generation fighter aircraft as well as ground and maritime defences.\n\nKawasaki Ki-28: The Kawasaki Ki-28 (キ28 , Ki-Nijuhachi ) , World War II Allied reporting name \"Bob\", was an experimental fighter aircraft designed for the Imperial Japanese Army and meant as a replacement for the Kawasaki Ki-10.  It flew in 1936, but was never produced for actual use as the Army choose the Nakajima Ki-27.\n\nFighter aircraft: A fighter aircraft is a military aircraft designed primarily for air-to-air combat against other aircraft, as opposed to bombers and attack aircraft, whose main mission is to attack ground targets.  The hallmarks of a fighter are its speed, maneuverability, and small size relative to other combat aircraft.\n\nNakajima Ki-87: The Nakajima Ki-87 was a Japanese high-altitude fighter-interceptor of World War II.  It was a single seat, exhaust-driven turbo-supercharged engined, low-wing monoplane with a conventional undercarriage.\n\nInterceptor aircraft: An interceptor aircraft, or simply interceptor, is a type of fighter aircraft designed specifically to attack enemy aircraft, particularly bombers and reconnaissance aircraft, as they approach.  There are two general classes of interceptor: relatively lightweight aircraft built for high performance, and heavier aircraft designed to fly at night or in adverse weather and operate over longer ranges.\n\nNakajima Ha219: The Nakajima Ha219, (also known as the Ha-44under the unified designation system, BH by the company and NK11A by the Imperial Japanese Navy Air Service (IJNAS)), was a late war Imperial Japanese Army Air Force (IJAAF) 2461 hp 18-cylinder air-cooled radial engine, used on the Tachikawa Ki-94-2, Nakajima Ki-84-N and Nakajima Ki-87.\n\nNakajima Ki-84: The Nakajima Ki-84 \"Hayate\" (キ84 疾風\"Gale\" ) was a single-seat fighter flown by the Imperial Japanese Army Air Service in the last three years of World War II.  The Allied reporting name was \"Frank\"; the Japanese Army designation was Army Type 4 Fighter (四式戦闘機 , yon-shiki-sentō-ki ) .  The Ki-84 is generally considered the best Japanese fighter to see large-scale operation during the conflict.  The aircraft boasted high speeds and excellent maneuverability with an armament (up to two 30 mm and two 20 mm cannon) that gave it formidable firepower.  The Ki-84's performance matched that of any single-engine Allied fighter it faced, while its operational ceiling enabled it to intercept high-flying B-29 Superfortress bombers.  Pilots and crews in the field learned to take care with the plane's high-maintenance Nakajima Homare engine and landing gear prone to buckling.  The difficulties of Japan's situation late in the war took a toll on the aircraft's overall field performance as manufacturing defects multiplied, quality fuel proved difficult to procure, and experienced pilots grew scarce.  Even then, the pilot of a well-maintained Ki-84 took to the skies in knowing possession of Japan's fastest fighter.  A total of 3,514 aircraft were built.\n\nQuestion: The Nakajima Ki-87 was a type of fighter aircraft designed specifically to attack what?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"aircraft_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the aircraft.\"\n    },\n    \"aircraft_type\": {\n      \"type\": \"string\",\n      \"description\": \"The general classification of the aircraft.\"\n    },\n    \"designed_purpose\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"primary_target\": {\n          \"type\": \"string\",\n          \"description\": \"The main category of aircraft the interceptor was designed to attack.\"\n        },\n        \"specific_targets\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"Specific types of enemy aircraft the interceptor was designed to attack.\"\n        }\n      },\n      \"required\": [\n        \"primary_target\",\n        \"specific_targets\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"aircraft_name\",\n    \"aircraft_type\",\n    \"designed_purpose\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "aircraft_name": {
        "type": "string",
        "description": "The name of the aircraft."
      },
      "aircraft_type": {
        "type": "string",
        "description": "The general classification of the aircraft."
      },
      "designed_purpose": {
        "type": "object",
        "properties": {
          "primary_target": {
            "type": "string",
            "description": "The main category of aircraft the interceptor was designed to attack."
          },
          "specific_targets": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Specific types of enemy aircraft the interceptor was designed to attack."
          }
        },
        "required": [
          "primary_target",
          "specific_targets"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "aircraft_name",
      "aircraft_type",
      "designed_purpose"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
