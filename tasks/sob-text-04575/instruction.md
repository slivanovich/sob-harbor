{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nIndian Airlines Flight 427: Indian Airlines Flight IC427 was involved in an aircraft hijacking that took place in India between April 24 and April 25, 1993.  Commandos from the National Security Guard (NSG) rescued all 141 hostages of the Indian Airlines Boeing 737, on the ground at Amritsar airport.  The lone hijacker, Mohammed Yousuf Shah, was killed within 5 minutes of commandos entering the plane, before he could react and harm any of the hostages.  The rescue was code-named Operation Ashwamedh.\n\nIndian Airlines Flight 605: Indian Airlines Flight 605 was a scheduled domestic passenger flight, flying from Chhatrapati Shivaji International Airport in India's largest city of Bombay (present day Mumbai) to Hindustan Airport in Bangalore, the capital of Indian state of Karnataka.  On 14 February 1990, the aircraft involved in the crash, an Airbus A320-231 registered in India as VT-EPN, crashed onto a golf course while on a landing attempt on Bangalore International Airport, killing 92 people.\n\nCapital Airlines Flight 67: Capital Airlines Flight 67 was domestic scheduled passenger flight operated by Capital Airlines that crashed on final approach to Freeland, Michigan, USA, during a severe snowstorm on April 6, 1958.  The flight was en route from Flint-Bishop Airport to the Freeland-Tri City Airport (now MBS International Airport) when it crashed.  Flight 67 was the first of four fatal crashes in the space of two years involving Capital Airlines Vickers Viscounts; the others were Capital Airlines Flight 300 (May 1958), Capital Airlines Flight 75 (May 1959) and Capital Airlines Flight 20 (January 1960).\n\nIndian Airlines: Indian Airlines, later Indian (Indian Airlines Limited from 1993 and Indian Airlines Corporation from 1953 to 1993), was a major Indian airline based in Delhi and focused primarily on domestic routes, along with several international services to neighbouring countries in Asia.  It was state-owned, after merger of eight pre-Independence domestic airlines and was administered by the Ministry of Civil Aviation.  Indian was formerly one of the two flag carriers of India, the other being Air India.\n\nAirline Allied Services: Airline Allied Services Limited (AASL) is Public Sector Undertaking (PSU) of the Government of India and is a subsidiary of Indian Airlines.  Established in 1983, the company provides support services to Indian Airlines such as air transport services and manage airplane purchase, lease and sale transactions.  As a subsidiary of Indian Airlines, AASL also provides air transport services under the name \"Alliance Air\".  AASL is headquartered in New Delhi.\n\nIndian Airlines flight 814 hijacking: Indian Airlines Flight 814 commonly known as IC 814 was an Indian Airlines Airbus A300 en route from Tribhuvan International Airport in Kathmandu, Nepal to Indira Gandhi International Airport in Delhi, India on Friday, 24 December 1999, when it was hijacked.  Harkat-ul-Mujahideen was accused of the hijacking.\n\nUnited Airlines Flight 608: United Airlines Flight 608 was a Douglas DC-6 airliner, registration NC37510, on a scheduled passenger flight from Los Angeles to Chicago when it crashed at 12:29 pm on October 24, 1947 about 1.5 miles southeast of Bryce Canyon Airport, Utah.  There were no survivors among the 5 crew members and 47 passengers on board.  It was the first crash of a DC-6, and at the time it was the second deadliest air crash in the United States, surpassed by Eastern Air Lines Flight 605 by only one fatality.\n\nCapital Airlines Flight 75: Capital Airlines Flight 75 was a domestic scheduled Capital Airlines flight operating between La Guardia Airport and Atlanta Airport.  A Vickers Viscount flying the route crashed in Chase, Maryland, on May 12, 1959, with the loss of all on board.  The crash was the second of three involving a Capital Airlines Vickers Viscount in as many years; the other two were Capital Airlines Flight 20 and Capital Airlines Flight 67.\n\nChhatrapati Shivaji International Airport: Chhatrapati Shivaji International Airport (IATA: BOM, ICAO: VABB) , formerly known as Sahar International Airport, is the primary international airport serving the Mumbai Metropolitan Area, India.\n\nChina Airlines Flight 605: China Airlines Flight 605 (callsign \"Dynasty 605\") was a daily non-stop flight departing from Taipei at 6:30 a.m. and arriving at Kai Tak Airport in Hong Kong at 7:00 a.m. local time.  On November 4, 1993, the plane crashed after overrunning the runway on landing during a storm.  It was the first major loss of a Boeing 747-400.\n\nQuestion: Indian Airlines Flight 605 was flying from an airport formerly known by what name?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"flight_number\": {\n      \"type\": \"string\",\n      \"description\": \"The flight number of the aircraft.\"\n    },\n    \"airline_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the airline operating the flight.\"\n    },\n    \"departure_airport\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"current_name\": {\n          \"type\": \"string\",\n          \"description\": \"The current name of the departure airport.\"\n        },\n        \"former_name\": {\n          \"type\": \"string\",\n          \"description\": \"The former name of the departure airport.\"\n        }\n      },\n      \"required\": [\n        \"current_name\",\n        \"former_name\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"flight_number\",\n    \"airline_name\",\n    \"departure_airport\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "flight_number": {
        "type": "string",
        "description": "The flight number of the aircraft."
      },
      "airline_name": {
        "type": "string",
        "description": "The name of the airline operating the flight."
      },
      "departure_airport": {
        "type": "object",
        "properties": {
          "current_name": {
            "type": "string",
            "description": "The current name of the departure airport."
          },
          "former_name": {
            "type": "string",
            "description": "The former name of the departure airport."
          }
        },
        "required": [
          "current_name",
          "former_name"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "flight_number",
      "airline_name",
      "departure_airport"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
