{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAir Tahoma Flight 185: Air Tahoma Flight 185 was a scheduled cargo flight from Memphis to the Cincinnati/Northern Kentucky International Airport conducted by Air Tahoma as part of a contract to freight parcels for courier firm DHL.  On August 13, 2004, the flight crashed during approach to landing just one mile short of the runway.  The Convair 580, which is a twin engine turboprop, was destroyed upon impact.  The first officer was killed and the captain received minor injuries.\n\nČSA Flight 001: Czechoslovak Airlines Flight 001 was an Ilyushin Il-18B four engine turboprop airliner, registered OK-NAB, which was operating as a scheduled domestic passenger flight from Prague's Ruzyně airport to Bratislava-Ivanka Airport, both in Czechoslovakia, which crashed into the Zlaté Piesky (Golden Sands) Lake while attempting to land in Bratislava on July 28, 1976.  All 6 crew members and 70 out of 73 passengers died.\n\nATR 72: The ATR 72 is a twin-engine turboprop, short-haul regional airliner developed and produced in France and Italy by aircraft manufacturer ATR (Aerei da Trasporto Regionale or Avions de transport régional), a joint venture formed by French aerospace company Aérospatiale (now Airbus) and Italian aviation conglomerate Aeritalia (now Leonardo S.p.A.).  The number \"72\" in its name is derived from the aircraft's standard seating configuration in a passenger-carrying configuration, which could seat 72-78 passengers in a single-class arrangement.\n\nTempuling Airport: Tempuling Airport is a domestic airport located at Tembilahan, the capital of Indragiri Hilir Regency, Riau province.  It serves Tembilahan and surrounding areas.  It has some facilities like other airports.  Currently, this airport only serves flights to and from Pekanbaru.  This airport is able to serve aircraft equivalent to ATR 72.\n\nAerocaribe Flight 7831: Aerocaribe Flight 7831 was a Jetstream 32, registration N912FJ, with 17 passengers and 2 crew on a short haul flight from Terán Airport in Tuxtla Gutiérrez, Chiapas, to Carlos Rovirosa Pérez International Airport in Villahermosa, Tabasco both cities in Mexico.  On 8 July 2000, as Flight 7831 leave the airport, severe weather in their flight path prompted the captain to ask air traffic control at Tuxtla Gutiérrez for permission to circumvent the severe weather.  Air traffic control granted the request and the flight turned to the right, but at 19:50 Flight 7831 struck the ground in a mountainous area while descending.  The aircraft burst into flames on impact.  Flight 7831 crashed near Chulum Juarez (Chiapas) and all passengers and crew on board died in the site of the accident.\n\nAlitalia CityLiner: Alitalia CityLiner S.p.A. is the regional subsidiary of Alitalia.  It operates short haul point to point flights with low passenger load factors, using regional airliners, and carries passengers from minor airports to Alitalia's hub at Leonardo da Vinci–Fiumicino Airport.\n\n2016 Indian Air Force An-32 disappearance: On 22 July 2016, an Antonov An-32 twin engine turboprop transport aircraft of the Indian Air Force disappeared while flying over the Bay of Bengal.  The aircraft was en route from Tambaram Air Force Station in the city of Chennai on the western coastline of the Bay of Bengal to Port Blair in the Andaman and Nicobar Islands.  There were 29 people on board.  Radar contact with the aircraft was lost at 9:12am, 280 km east of Chennai.  The search and rescue operation became India's largest search operation for a missing plane on the sea in history.\n\nFlyMontserrat Flight 107: FlyMontserrat Flight 107 was a short haul flight from V. C. Bird International Airport, Antigua to John A. Osborne Airport, Montserrat on 7 October 2012.  The flight was being undertaken by a Britten-Norman Islander, registration VP-MON with one crew and three passengers on board.  The flight crashed shortly after take off near the end of the runway.  Three of the four passengers and crew died in the crash.\n\nCessna Denali: The Cessna Denali, previously known as the Textron Single Engine TurboProp (SETP), is a single engine turboprop aircraft under development by Cessna, announced at EAA AirVenture Oshkosh 2015.  The aircraft is a completely new design, not derived from any existing aircraft.  It should compete with the Pilatus PC-12 and Daher-Socata TBM, as well as other new projects such as the One Aviation Kestrel K-350 and the CAIGA Primus 150.\n\nDiamond DA42: The Diamond DA42 Twin Star is a four seat, twin engine, propeller-driven airplane developed manufactured by Austrian company Diamond Aircraft Industries.  It was Diamond's first twin engine design, as well as the first new European twin-engine aircraft in its category to be developed in over 25 years.  During 2004, the DA42 became the first diesel-powered fixed-wing aircraft to perform a non-stop crossing of the North Atlantic.\n\nQuestion: The twin engine turboprop, short haul regional airliner, which can be serviced by the Tempuling Airport, can hold how many passengers?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"aircraft_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the aircraft.\"\n    },\n    \"aircraft_type\": {\n      \"type\": \"string\",\n      \"description\": \"Description of the aircraft's engine and propulsion type.\"\n    },\n    \"aircraft_role\": {\n      \"type\": \"string\",\n      \"description\": \"The operational role of the aircraft.\"\n    },\n    \"airport_compatibility\": {\n      \"type\": \"string\",\n      \"description\": \"The airport that can service this type of aircraft.\"\n    },\n    \"passenger_capacity\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"min\": {\n          \"type\": \"integer\",\n          \"description\": \"Minimum passenger capacity.\"\n        },\n        \"max\": {\n          \"type\": \"integer\",\n          \"description\": \"Maximum passenger capacity.\"\n        }\n      },\n      \"required\": [\n        \"min\",\n        \"max\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"aircraft_name\",\n    \"aircraft_type\",\n    \"aircraft_role\",\n    \"airport_compatibility\",\n    \"passenger_capacity\"\n  ],\n  \"additionalProperties\": false\n}"
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
        "description": "Description of the aircraft's engine and propulsion type."
      },
      "aircraft_role": {
        "type": "string",
        "description": "The operational role of the aircraft."
      },
      "airport_compatibility": {
        "type": "string",
        "description": "The airport that can service this type of aircraft."
      },
      "passenger_capacity": {
        "type": "object",
        "properties": {
          "min": {
            "type": "integer",
            "description": "Minimum passenger capacity."
          },
          "max": {
            "type": "integer",
            "description": "Maximum passenger capacity."
          }
        },
        "required": [
          "min",
          "max"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "aircraft_name",
      "aircraft_type",
      "aircraft_role",
      "airport_compatibility",
      "passenger_capacity"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
