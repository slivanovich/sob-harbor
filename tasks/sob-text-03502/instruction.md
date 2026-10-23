{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAvro Canada C102 Jetliner: The Avro C102 Jetliner was a Canadian prototype medium-range turbojet-powered jet airliner built by Avro Canada in 1949.  It was beaten to the air by only 13 days by the de Havilland Comet, thereby becoming the second jet airliner in the world.  The name \"Jetliner\" was chosen as a shortening of the term \"jet airliner\", a term which is still in popular usage in Canada and the United States.  The aircraft was considered suitable for busy routes along the US eastern seaboard and garnered intense interest, notably from Howard Hughes who even offered to start production under license.  However continued delays in Avro's all-weather interceptor project, the Avro CF-100, led to an order to stop working on the project in 1951, with the prototype Jetliner later cut up for scrap.\n\nConcorde: Aérospatiale/BAC Concorde ( ) is a British-French turbojet-powered supersonic passenger jet airliner that was operated until 2003.  It had a maximum speed over twice the speed of sound at Mach 2.04 (1354 mph at cruise altitude), with seating for 92 to 128 passengers.  First flown in 1969, Concorde entered service in 1976 and continued flying for the next 27 years.  It is one of only two supersonic transports to have been operated commercially; the other is the Soviet-built Tupolev Tu-144, which was operated for a much shorter period.\n\nL'Auberge du Pont de Collonges: L'Auberge du Pont de Collonges also known as Paul Bocuse or Bocuse, is a restaurant in Collonges-au-Mont-d'Or near Lyon, France.  The chef is Paul Bocuse.\n\nAlexei Tupolev: Alexei Andreyevich Tupolev (Russian: Алексе́й Андре́евич Ту́полев ; May 20, 1925 – May 12, 2001) was a Soviet aircraft designer who led the development of the first supersonic passenger jet, the Tupolev Tu-144.  He also helped design the Buran space shuttle and the long-range heavy bomber Tu-2000, both of which were suspended for lack of funding.\n\nPaul Bocuse: Paul Bocuse (] ) (born 11 February 1926) is a French chef based in Lyon who is famous for the high quality of his restaurants and his innovative approaches to cuisine.  A student of Eugénie Brazier, he is one of the most prominent chefs associated with the \"nouvelle cuisine\", which is less opulent and calorific than the traditional \"cuisine classique\", and stresses the importance of fresh ingredients of the highest quality.  Paul Bocuse claimed that Henri Gault first used the term, \"nouvelle cuisine\", to describe food prepared by Bocuse and other top chefs for the maiden flight of the Concorde airliner in 1969.\n\nTupolev Tu-104: The Tupolev Tu-104 (NATO reporting name: Camel) was a twin-engined medium-range narrow-body turbojet-powered Soviet airliner and the world's first successful jet airliner.  Although it was the sixth jet airliner to fly (following, in order, the British Vickers Type 618 Nene-Viking, de Havilland Comet, Canadian Avro Canada C102 Jetliner, US Boeing 367-80 and French Sud Caravelle), the Tu-104 was the second to enter regular service (with Aeroflot) and the first to provide a sustained and successful service (the Comet which had entered service in 1952, was withdrawn from 1954-1958 following a series of crashes due to structural failure).  The Tu-104 was the sole jetliner operating in the world between 1956 and 1958.\n\nBocuse d'Or USA: The Bocuse d'Or USA is a biennial chef championship, where the winner is selected to represent the U.S. in the international Bocuse d'Or competition.  Following 20 years of American representation in the competition, in 2008 Paul Bocuse asked Daniel Boulud to establish a structure for the selection of Team USA, who along with Thomas Keller and Jérôme Bocuse form the Board of Directors of the Bocuse d'Or USA Foundation.  The first Bocuse d'Or USA competition was held in September 2008.\n\nIlyushin Il-62: The Ilyushin Il-62 (Russian: Илью́шин Ил-62 ; NATO reporting name: Classic) is a Soviet long-range narrow-body jet airliner conceived in 1960 by Ilyushin.  As successor to the popular turbo-prop Il-18 and with capacity for almost 200 passengers and crew, the Il-62 was the world's largest jet airliner when first flown in 1963.  Being one of four pioneering long-range designs (the others being Boeing 707, DC-8, and VC10), it was the first such type to be operated by the Soviet Union and a number of allied nations.  The Il-62 entered Aeroflot civilian service on 15 September 1967 with an inaugural passenger flight from Moscow to Montreal, and remained the standard long-range airliner for the Soviet Union (and later, Russia) for several decades.  It was the first Russian pressurised aircraft with non-circular cross-section fuselage and ergonomic passenger doors, and the first Russian jet with six-abreast seating (the turbo-prop Tu-114 shared this arrangement) and international-standard position lights.\n\nZero Emission Hyper Sonic Transport: The Zero Emission Hyper Sonic Transport or ZEHST is a planned supersonic passenger jet airliner project by EADS and Japan.  It can be seen as a descendant of the Concorde airliner capable of flying at more than Mach 4 (four times the speed of sound).  The aircraft is projected to carry 50 to 100 people 32 km above the ground.  Zehst would be able to fly from Paris to Tokyo in 2.5 hours, or from New York to London in an hour.\n\nJet airliner: A jet airliner (or jetliner) is an airliner powered by jet engines (passenger jet aircraft).  Airliners usually have two or four jet engines; three-engined designs were popular in the 1970s but are less common today.\n\nQuestion: Paul Bocuse prepared food for which British-French turbojet-powered supersonic passenger jet airliner?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"aircraft_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the aircraft for which food was prepared.\"\n    },\n    \"aircraft_type\": {\n      \"type\": \"string\",\n      \"description\": \"The general type of the aircraft.\"\n    },\n    \"aircraft_nationalities\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"The countries associated with the aircraft's origin.\"\n    },\n    \"power_source\": {\n      \"type\": \"string\",\n      \"description\": \"The type of engine powering the aircraft.\"\n    },\n    \"chef_who_prepared_food\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the chef who prepared food for the aircraft's event.\"\n    },\n    \"event_context\": {\n      \"type\": \"string\",\n      \"description\": \"The specific event for which the food was prepared.\"\n    },\n    \"event_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the event took place.\"\n    }\n  },\n  \"required\": [\n    \"aircraft_name\",\n    \"aircraft_type\",\n    \"aircraft_nationalities\",\n    \"power_source\",\n    \"chef_who_prepared_food\",\n    \"event_context\",\n    \"event_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "aircraft_name": {
        "type": "string",
        "description": "The name of the aircraft for which food was prepared."
      },
      "aircraft_type": {
        "type": "string",
        "description": "The general type of the aircraft."
      },
      "aircraft_nationalities": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "The countries associated with the aircraft's origin."
      },
      "power_source": {
        "type": "string",
        "description": "The type of engine powering the aircraft."
      },
      "chef_who_prepared_food": {
        "type": "string",
        "description": "The name of the chef who prepared food for the aircraft's event."
      },
      "event_context": {
        "type": "string",
        "description": "The specific event for which the food was prepared."
      },
      "event_year": {
        "type": "integer",
        "description": "The year the event took place."
      }
    },
    "required": [
      "aircraft_name",
      "aircraft_type",
      "aircraft_nationalities",
      "power_source",
      "chef_who_prepared_food",
      "event_context",
      "event_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
