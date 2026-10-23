{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRAF Valley: Royal Air Force Valley or more simply RAF Valley (Welsh: \"RAF y Fali\" ) (IATA: VLY, ICAO: EGOV) is a Royal Air Force station on the island of Anglesey, Wales, and which is also used as Anglesey Airport.  It provides fast-jet training using the BAE Systems Hawk and provides training for aircrew working with search and rescue.\n\nMuniz M-9: The Muniz M-9 was a two-seat training biplane with tandem open cockpit and powered by a 200 hp (149 kW) 130 hp (197 kW) de Havilland Gipsy Six engine.  Designed by Lieutenant-Colonel Antonio Muniz, a serving officer in the Brazilian Air Force, as an advanced trainer and was very similar to his earlier M-7 primary trainer.  It was first flown in 1937 and a small production run was built for the air force by Cia Nacional de Navegacao Costiera.\n\nBAE Systems Hawk: The BAE Systems Hawk is a British single-engine, jet-powered advanced trainer aircraft.  It was first flown at Dunsfold, Surrey, in 1974 as the Hawker Siddeley Hawk, and subsequently produced by its successor companies, British Aerospace and BAE Systems, respectively.  It has been used in a training capacity and as a low-cost combat aircraft.\n\nRoyal Air Force Music Services: Royal Air Force Music Services is the organization which provides military musical support to the Royal Air Force.  Based at RAF Northolt (previously at RAF Uxbridge) and RAF Cranwell, it forms the central administration of one hundred and seventy musicians divided between the Central Band of the Royal Air Force, The Band of the Royal Air Force College, The Band of the Royal Air Force Regiment and Headquarters Music Services.  These main military bands contain within their ranks the Royal Air Force Squadronnaires, Royal Air Force Swing Wing, Royal Air Force Shades of Blue, and The Salon Orchestra of the Central Band of the Royal Air Force.\n\nBeechcraft T-6 Texan II: The Beechcraft T-6 Texan II is a single-engine turboprop aircraft built by the Raytheon Aircraft Company (which became Hawker Beechcraft and later Beechcraft Defense Company, and was bought by Textron Aviation in 2014).  A trainer aircraft based on the Pilatus PC-9, the T-6 has replaced the Air Force's Cessna T-37B Tweet and the Navy's T-34C Turbo Mentor.  The T-6A is used by the United States Air Force for basic pilot training and Combat Systems Officer (CSO) training and by the United States Navy and United States Marine Corps for primary Naval Aviator training as well as primary and intermediate Naval Flight Officer (NFO) training.  The T-6A is also used as a basic trainer by the Royal Canadian Air Force (CT-156 Harvard II), the Greek Air Force, the Israeli Air Force (\"Efroni\"), and the Iraqi Air Force.  The T-6B is the primary trainer for U.S. student naval aviators.  The T-6C is used for training by the Mexican Air Force, Royal Air Force, Royal Moroccan Air Force, and the Royal New Zealand Air Force.\n\nYakovlev Yak-130: The Yakovlev Yak-130 (NATO reporting name: Mitten) is a subsonic two-seat advanced trainer aircraft originally developed by Yakovlev and Aermacchi.  It has also been marketed as a potential light attack aircraft.  Development of the plane began in 1991 and the maiden flight was conducted on 25 April 1996.  In 2002, it won a Russian government tender for training aircraft and in 2009 the aircraft entered service with the Russian Air Force.  As an advanced training aircraft, the Yak-130 is able to replicate the characteristics of several 4+ generation fighters as well as the fifth-generation Sukhoi Su-57.  It can also perform light-attack and reconnaissance duties, carrying a combat load of 3,000 kg.\n\nBoulton Paul Balliol: The Boulton Paul Balliol and Sea Balliol were monoplane military advanced trainer aircraft built for the Royal Air Force (RAF) and the Royal Navy Fleet Air Arm (FAA) by Boulton Paul Aircraft.  Developed in the late 1940s the Balliol was designed to replace the North American Harvard trainer and used the Rolls-Royce Merlin engine, with the Sea Balliol a naval version for deck landing training.\n\nPartenavia Mosquito: The Partenavia P.86 Mosquito was a two-seat civil trainer aircraft first flown in Italy on 27 April 1986.  It was a high-wing monoplane of pod-and-boom construction with tricycle undercarriage and a twin tail, that accommodated the student and instructor side-by-side.\n\nMiles Magister: The Miles M.14 Magister is a British two-seat monoplane basic trainer aircraft built by the Miles Aircraft for the Royal Air Force and Fleet Air Arm.  Affectionately known as the Maggie, the Magister was based on Miles' civilian Hawk Major and Hawk Trainer and was the first monoplane designed specifically as a trainer for the RAF.  As a low-wing monoplane, it was an ideal introduction to the Spitfire and Hurricane for new pilots.  Its sister design, the Miles Master was an advanced trainer also built by Phillips & Powis at Woodley.\n\nNorth American T-6 Texan: The North American Aviation T-6 Texan is an American single-engined advanced trainer aircraft used to train pilots of the United States Army Air Forces (USAAF), United States Navy, Royal Air Force, and other air forces of the British Commonwealth during World War II and into the 1970s.  Designed by North American Aviation, the T-6 is known by a variety of designations depending on the model and operating air force.  The United States Army Air Corps (USAAC) and USAAF designated it as the AT-6, the United States Navy the SNJ, and British Commonwealth air forces the Harvard, the name by which it is best known outside of the US.  Starting in 1948, the new United States Air Force (USAF) designated it the T-6, with the USN following in 1962.  It remains a popular warbird aircraft used for airshow demonstrations and static displays.  It has also been used many times to simulate various Japanese aircraft, including the Mitsubishi A6M Zero in movies depicting World War II in the Pacific.\n\nQuestion:  Royal Air Force Valley provides fast-jet training using an advanced trainer aircraft first flown in what year?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"training_location\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the Royal Air Force station providing training.\"\n    },\n    \"training_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of training provided at the location.\"\n    },\n    \"aircraft_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"aircraft_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the aircraft used for training.\"\n        },\n        \"aircraft_role\": {\n          \"type\": \"string\",\n          \"description\": \"The primary role of the aircraft.\"\n        },\n        \"first_flight_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the aircraft was first flown.\"\n        }\n      },\n      \"required\": [\n        \"aircraft_name\",\n        \"aircraft_role\",\n        \"first_flight_year\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"training_location\",\n    \"training_type\",\n    \"aircraft_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "training_location": {
        "type": "string",
        "description": "The name of the Royal Air Force station providing training."
      },
      "training_type": {
        "type": "string",
        "description": "The type of training provided at the location."
      },
      "aircraft_details": {
        "type": "object",
        "properties": {
          "aircraft_name": {
            "type": "string",
            "description": "The name of the aircraft used for training."
          },
          "aircraft_role": {
            "type": "string",
            "description": "The primary role of the aircraft."
          },
          "first_flight_year": {
            "type": "integer",
            "description": "The year the aircraft was first flown."
          }
        },
        "required": [
          "aircraft_name",
          "aircraft_role",
          "first_flight_year"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "training_location",
      "training_type",
      "aircraft_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
