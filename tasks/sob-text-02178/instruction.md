{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nVMA-322: Marine Attack Squadron 322 (VMA-322) was an attack squadron in the United States Marine Corps.  The squadron, also known as the “Fighting Gamecocks”, fought in World War II and later became a part of the Marine Forces Reserve based out of Naval Air Station South Weymouth, Massachusetts.\n\nNaval Air Station Joint Reserve Base New Orleans: Naval Air Station Joint Reserve Base New Orleans is a base of the United States military located in Belle Chasse, unincorporated Plaquemines Parish, Louisiana, United States.  NAS JRB New Orleans is home to a Navy Reserve strike fighter squadron and a fleet logistics support squadron, the 159th Fighter Wing (159 FW) of the Louisiana Air National Guard, Coast Guard Air Station New Orleans, a detachment of a Marine Corps Reserve light helicopter attack squadron, as well as other US Navy & US Army activities.  The base has a 24/7 operating schedule to support both the 159 FW's NORAD air sovereignty/homeland defense requirements and for Coast Guard Air Station New Orleans search and rescue/maritime law enforcement/port security missions.  It contains a military airport known as Alvin Callender Field (IATA: NBG, ICAO: KNBG, FAA LID: NBG) which is located three nautical miles (6 km) south of the central business district of New Orleans.  The base's predecessor, NAS New Orleans, occupied the current location of the University of New Orleans's principal campus until 1957.\n\nSecond VA-85 (U.S. Navy): Attack Squadron 85 or VA-85 was a long-lived Attack Squadron of the U.S. Navy.  It was called to active duty as U.S. Navy Reserve squadron VA-859 on 1 February 1951 and redesignated VA-85 on 4 February 1953.  It was disestablished on 30 September 1994, over 40 years later.  The squadron's nickname from 1958-1994 was the \"Black Falcons\".  It was the second squadron to be designated VA-85, the first VA-85 was disestablished on 29 November 1949.\n\nSecond VA-155 (U.S. Navy): Attack Squadron 155 or VA-155 was an 'Attack Squadron of the U.S. Navy.  It was established as Reserve Attack Squadron VA-71E in 1946, redesignated as VA-58A on 1 October 1948, and redesignated Reserve Composite Squadron VC-722 on 1 November 1949.  The squadron was redesignated as VA-728 on 1 April 1950, and called to active duty on 1 February 1951.  It was ultimately redesignated VA-155 on 4 February 1953, and disestablished on 30 September 1977.  Its nickname was Silver Fox from the early 1960s onward.  It was the second squadron to be named VA-155, the first VA-155 was disestablished on 30 November 1949, while a third VA-155 was established on 1 September 1987 and disestablished on 30 April 1993.\n\nVAW-77: Carrier Airborne Early Warning Squadron 77 (VAW-77) \"Nightwolves\" was an aviation unit of the United States Navy Reserve based at Naval Air Station Joint Reserve Base New Orleans from 1995 to 2013.  It comprised the U.S. Navy's only fully dedicated counter-narcotics squadron.\n\nVA-873 (U.S. Navy): VA-873 was an attack squadron of the U.S. Navy Reserve, based at Naval Air Station Alameda, California.  Its insignia was approved by CNO on 16 March 1964.  Colors for the insignia were: a white and blue background outlined in black; the blue background section had five white stars and the white section had a gold outline of San Francisco Golden Gate with two blue rows of waves beneath the bridge; separating the two sections was a stylized aircraft in black with a red flame coming from the tail; the scroll was white outlined in black with black lettering.\n\nNaval Air Station Alameda: Naval Air Station Alameda (NAS Alameda) was a United States Navy Naval Air Station in Alameda, California, on San Francisco Bay.\n\nVAQ-209: Electronic Attack Squadron 209 (VAQ-209) is a United States Navy Reserve electronic attack squadron.  Known as the \"Star Warriors\", the squadron flies the EA-18G Growler carrier-based electronic warfare jet aircraft.  Based at Naval Air Station Whidbey Island, WA, it is assigned to the Tactical Support Wing.\n\nSecond VA-75 (U.S. Navy): Attack Squadron 75 (VA-75) or ATKRON 75 was an attack squadron of the United States Navy that was active from World War II through the 1990s.  Nicknamed the \"Sunday Punchers,\" they were based out of Naval Air Station Oceana, Virginia.  Originally established as Bombing Squadron EIGHTEEN (VB-18) on July 20, 1943, it was redesignated Attack Squadron VA-7A on 15 November 1946, redesignated Attack Squadron VA-74 on 27 July 1948, redesignated Attack Squadron VA-75 on 15 February 1950 and disestablished on February 28, 1997.  They were the second squadron to be designated VA-75, the first VA-75 was disestablished on 30 November 1949.  They were the first fleet squadron to operate the A-6 Intruder and the last unit to fly it in operational service.\n\nVA-52 (U.S. Navy): VA-52 was an Attack Squadron of the U.S. Navy.  It was established as U.S. Navy Reserve Fighter Squadron VF-884 on 1 November 1949, and called to active duty on 20 July 1950.  It was redesignated VF-144 on 4 February 1953, and VA-52 on 23 February 1959.  The squadron was nicknamed the \"Bitter Birds\" from about 1951–1953, and the \"Knightriders\" from about 1960 onward.  Its insignia evolved through several versions from 1951–1960.  VA-52 was decommissioned on 31 March 1995.\n\nQuestion: VA-873 was an attack squadron of the U.S. Navy Reserve based at a station located on what bay?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"squadron_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the attack squadron.\"\n    },\n    \"squadron_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of the squadron (e.g., U.S. Navy Reserve attack squadron).\"\n    },\n    \"base_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the naval air station where the squadron was based.\"\n    },\n    \"base_location_city_state\": {\n      \"type\": \"string\",\n      \"description\": \"The city and state where the naval air station was located.\"\n    },\n    \"bay_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the bay on which the naval air station was located.\"\n    }\n  },\n  \"required\": [\n    \"squadron_name\",\n    \"squadron_type\",\n    \"base_name\",\n    \"base_location_city_state\",\n    \"bay_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "squadron_name": {
        "type": "string",
        "description": "The name of the attack squadron."
      },
      "squadron_type": {
        "type": "string",
        "description": "The type of the squadron (e.g., U.S. Navy Reserve attack squadron)."
      },
      "base_name": {
        "type": "string",
        "description": "The name of the naval air station where the squadron was based."
      },
      "base_location_city_state": {
        "type": "string",
        "description": "The city and state where the naval air station was located."
      },
      "bay_name": {
        "type": "string",
        "description": "The name of the bay on which the naval air station was located."
      }
    },
    "required": [
      "squadron_name",
      "squadron_type",
      "base_name",
      "base_location_city_state",
      "bay_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
