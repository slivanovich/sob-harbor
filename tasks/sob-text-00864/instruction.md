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
Saunders-Roe Duchess: The Saunders-Roe Duchess also known as the model P.131 was a British design for a large jet-powered flying boat from Saunders-Roe, based in Cowes on the Isle of Wight.  The Duchess was designed to follow the propeller-driven Princess.  The Duchess would have been a high-wing cantiliver monoplane with a conventional tail and a full-length planing bottom.  It also had retractable stabiliser floats at each wingtip.  It was to have had a pressurised and air-conditioned cabin for 74 passengers in two compartments with a freight hold in the centre.  The six de Havilland Ghost turbojets were to have been mounted inside the wing roots.  The company displayed a model of the aircraft at the 1950 Farnborough Air Show.  Tasman Empire Airways considered ordering the aircraft for journeys between Australia and New Zealand but the aircraft was cancelled.

Horten brothers: Walter Horten (born 13 November 1913; died 9 December 1998 in Baden-Baden, Germany) and Reimar Horten (born 12 March 1915; died 14 March 1994 in Villa General Belgrano, Argentina), sometimes credited as the Horten Brothers, were German aircraft pilots and enthusiasts.  Although they had little, if any, formal training in aeronautics or related fields, the Hortens designed some of the most revolutionary aircraft of the 1940s, including the world's first jet-powered flying wing, the Horten Ho 229.

Northrop JB-1 Bat: The Northrop JB-1 "Bat" was a United States surface-to-surface cruise missile that was a prototype jet-powered flying wing.  The United States Army Air Forces MX-543 program was initiated in September 1942 to use US versions of Frank Whittle's jet engine (US-named General Electric J31).  The Northrop Corporation was contracted in late 1943, and only 10 JB-1 airframes were built.  A manned version was towed for the 1st flight on "August 27, 1943", ["sic"] from Rogers Dry Lake; and a glider version was launched from a rocket-propelled sled and crashed in December 1944.  An unmanned JB-1 powered by an improvised General Electric B-1 turbojet with a wing span of 28 ft made its 1st flight from Eglin Field's Santa Rosa Island, Florida, on December 7, 1944, and crashed 400 yards from the rail launcher.

Horten H.XVIII: The Horten H.XVIII was a proposed German World War II intercontinental bomber, designed by the Horten brothers with pioneering features such as a flying wing configuration, turbojet engines and stealth characteristics.  The unbuilt H.XVIII represented, in many respects, a scaled-up version of the Horten Ho 229, a prototype jet fighter.  The H.XVIII was one of many proposed designs for an "Amerika Bomber", and would have carried sufficient fuel for transatlantic flights.

Horten H.VI: The Horten H.VI was a flying wing aircraft designed by the Horten brothers during World War II.

Horten H.IV: The Horten H.IV was a German tailless flying wing glider in which the pilot lay in a prone position to reduce the frontal area, and hence drag.  It was designed by Reimar and Walter Horten in Göttingen.  Four were built between 1941 and 1943.  They were flown in a number of unofficial competitions in Germany during World War II.  After the war the flying examples were transported to the United Kingdom and the United States where several contest successes were achieved.

Horten Ho 229: The Horten H.IX, RLM designation Ho 229 (or Gotha Go 229 for extensive re-design work done by Gotha to prepare the aircraft for mass production) was a German prototype fighter/bomber initially designed by Reimar and Walter Horten to be built by Gothaer Waggonfabrik late in World War II.  It was the first flying wing to be powered by jet engines.

Hawker Hunter: The Hawker Hunter is a transonic British jet-powered fighter aircraft that was developed by Hawker Aircraft for the Royal Air Force (RAF) during the late 1940s and early 1950s.  It was designed to take advantage of the newly developed Rolls-Royce Avon turbojet engine and the swept wing, and was the first jet-powered aircraft produced by Hawker to be procured by the RAF.  On 7 September 1953, the modified first prototype broke the world air speed record for aircraft, achieving a speed of 727.63 mph .

Horten H.II: The Horten H.II Habicht (Hawk) was a German flying wing glider built in Germany in 1935.  Four, including one flown mostly as a motorglider, were built.  One of the gliders was used to test the aerodynamics of a prototype World War II Horten jet fighter-bomber.

Horten H.III: The Horten H.III was a flying wing sailplane built by Walter and Reimar Horten in Germany from 1937 to 1944.

Question: The designers of the Horten H.XVIII also designed the world's first jet-powered flying wing known by what name?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "aircraft_model_name": {
      "type": "string",
      "description": "The name of the aircraft that is the world's first jet-powered flying wing."
    },
    "aircraft_key_feature": {
      "type": "string",
      "description": "A key distinguishing feature of the aircraft."
    },
    "designers": {
      "type": "array",
      "description": "A list of the individuals who designed the aircraft.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the designer."
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      }
    },
    "related_aircraft_model": {
      "type": "string",
      "description": "The model name of the aircraft mentioned in the question for comparison."
    },
    "designers_are_same": {
      "type": "boolean",
      "description": "Indicates whether the designers of the identified aircraft and the related aircraft are the same."
    }
  },
  "required": [
    "aircraft_model_name",
    "aircraft_key_feature",
    "designers",
    "related_aircraft_model",
    "designers_are_same"
  ],
  "additionalProperties": false
}
