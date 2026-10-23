{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThomas B. Hayward: Admiral Thomas Bibb Hayward (born May 3, 1924) was Chief of Naval Operations (CNO) for the United States Navy from July 1, 1978, until June 30, 1982, after which he retired from military service.  Shortly after the commencement of World War II, he enlisted in the U.S. Navy V-5 aviation program and was called to active duty as a naval aviation cadet in 1943, anticipating that he would shortly be flying combat in the South Pacific.  However, when roughly halfway through the flight training syllabus, he competed for and was accepted to attend the U.S. Naval Academy at Annapolis, Maryland, to position himself for a career in the U.S. Navy at war's end.  He graduated from the Academy in July, 1947 and was assigned to the USS Antietam (CV-36) as an engineering officer.  United States Naval Academy.  USS Antietam (CV-36), In 1949 he returned to flight training at Pensacola, Florida,and received his United States Naval Aviator wings in July 1950.  The Korean War having begun, then as Lieutenant junior grade, he reported to Fighter Squadron Fifty-One (VF-51) and flew from the decks of the USS Essex (CV-9) and USS Valley Forge (CV-45), accumulating 146 combat missions and was awarded the Distinguished Flying Cross, ten Air Medals, and two Navy Commendation Medals with Combat \"V\" for Valor.\n\nAlbert O. Vorse Jr.: Albert Ogden \"Scoop\" Vorse Jr. was an accomplished World War II naval ace who participated in some of the most prominent actions of the Pacific Theater, including the Battle of the Coral Sea and the Guadalcanal Campaign.  Vorse served in early fighter squadrons with legendary figures like Butch O'Hare and Jimmy Thach.  Rising in rank throughout the war, he would act as Executive Officer and Operations Officer in different squadrons before being given command of his own squadron, VF-80, the eponymous \"Vorse's Vipers\".  Vorse ended the war as commander of Air Group 80 and ultimately achieved Rear Admiral status before his retirement from the U.S. Navy in 1959.\n\nKenneth Whiting: Kenneth Whiting (22 July 1881 – 24 April 1943) was a United States Navy officer who was a pioneer in submarines and is best known for his lengthy career as a pioneering naval aviator.  During World War I, he commanded the first American military force to arrive in Europe for combat.  After the war, he was instrumental in development of the aircraft carrier in the United States, where he sometimes is known as the U.S. Navy' s \"father of the aircraft carrier.\"  He was involved in some way in the design or construction of five of the first six U.S. Navy aircraft carriers, and served as acting commanding officer of the first carrier to enter U.S. Navy service and as executive officer of the first two American carriers.  In the earliest days of the U.S. Navy' s development of an aircraft carrier force, he led many shipboard innovations still in use aboard carriers today.\n\nService Squadron: A Service Squadron (ServRon) was a U.S. Navy squadron that supported fleet combat units.  Service Squadrons were used by the United States Navy from their inception in 1943 to as late as the early 1980s.  At the time of their inception during the Second World War they allowed the US Navy to operate across the vast reaches of the Pacific ocean for extended periods of time.  Service Squadrons created temporary forward bases to allow the naval squadrons to spend less time in transit and more time in the area of combat.  Ulithi, a small volcanic atoll in the central Pacific, is one such example.  Service Squadrons essentially created a major naval base near the area of operation.  With the naval base at Ulithi to refit, repair and resupply, many ships were able to deploy and operate in the western Pacific for a year or more without returning to a major port facility.  Among the vessels operating in service squadrons were tankers, oilers, refrigerator ships, ammunition ships, supply ships, floating docks and repair ships.  They provided diesel, ordnance, aviation fuel, food stuffs and all other supplies.  Equally important at places like Ulithi were the portable piers and floating dry docks which allowed many ships damaged by enemy action or Pacific storms to undergo repair without having to travel the thousands of miles back to a major US naval base.  Ulithi was as far forward from the US naval base at San Francisco as the San Francisco base was from London, England.  To have a fully functional major port in the middle of the Pacific was a significant aid to U.S. Navy operations.\n\nRobert L. Rasmussen: Robert L. “Bob” Rasmussen (born May 26, 1930 in Rio Vista, California), is a noted military artist; a retired Captain of the United States Navy; a former career naval aviator, primarily in the F-8 Crusader; a former member of the U.S. Navy Flight Demonstration Squadron, the Blue Angels, and Director of the National Naval Aviation Museum at NAS Pensacola, Florida.  His Vietnam war experiences, including surviving the fire aboard USS \"Oriskany\" , have been documented in several books.  A prolific artist, Rasmussen has created hundreds of Naval Aviation paintings in watercolor, oil and acrylic.  His bronze sculptures include the design of the Spirit of Naval Aviation, displayed at the front entrance of the National Museum of Naval Aviation, Pensacola, Florida, the Alan Shepard memorial heroic figure at the Astronaut Hall of Fame, and the World War II and Korean War memorials in Pensacola, Florida.  His works have been displayed around the country, including the National Air and Space Museum in Washington, D.C., the National Naval Aviation Museum in Pensacola, Florida, and the NASA Museum at Cape Canaveral, Florida.  Rasmussen is the recipient of the R.G. Smith Award for Excellence in Naval Aviation Art, was inducted into the Naval Aviation Hall of Honor in 2008, and was awarded the Navy Superior Civilian Service Award on 24 September 2009.\n\nDonald B. Beary: Donald Bradford Beary (4 December 1888 – 7 March 1966) was a vice admiral of the United States Navy.  His career included service in both World War I and World War II and a tour as President of the Naval War College.  He commanded a wide variety of ships and organizations, and is particularly noted for his leadership during World War II in establishing and directing a large-scale U.S. Navy training program and for his pioneering and highly successful work as a commander of U.S. Navy underway replenishment forces.\n\nAlexander Vraciu: Alexander Vraciu (November 2, 1918 – January 29, 2015) was a U.S. Navy fighter ace, a Navy Cross recipient, and a Medal of Honor nominee during World War II.  At the end of the war, Vraciu ranked fourth among the U.S. Navy's flying aces, with 19 enemy planes downed during flight and 21 destroyed on the ground.  After the war, he served as a test pilot and was instrumental in forming the post-war Naval and Marine Air Reserve program.  From 1956 to 1958 Vraciu led his own fighter squadron, VF-51, for twenty-two months.  He retired from the U.S. Navy with the rank of commander on December 31, 1963.  Vraciu later moved to Danville, California, and worked for Wells Fargo.\n\nRichard John Cork: Richard John \"Dickie\" Cork, (4 April 1917 – 14 April 1944) was a fighter ace in the Fleet Air Arm of the Royal Navy during the Second World War.  Cork served in the Battle of Britain as the wingman for Douglas Bader of No. 242 Squadron RAF.  When he returned to the Fleet Air Arm in 1941, Cork served with 880 Naval Air Squadron in the Arctic, Mediterranean and Indian Ocean.  It was during Operation Pedestal in 1942 that he became the only Royal Navy pilot to shoot down five aircraft in one day, and was the leading naval ace using the Hawker Hurricane.  He was given command of the 15th Naval Fighter Wing aboard HMS \"Victorious\" before being killed in a flying accident over Ceylon in 1944.\n\nFrancis Dawson-Paul: Francis Dawson-Paul (18 February 1916 – 30 July 1940) was a fighter ace in the Fleet Air Arm of the Royal Navy during the Second World War.  He was seconded to the Royal Air Force during the Battle of Britain, serving with No. 64 Squadron RAF.  Between 1 and 25 July he shot down seven and a half German aircraft before being shot down himself over the English Channel.  Taken prisoner by the crew of a German E-boat he died of his wounds five days later.  In those 24 days of combat he became the first naval air ace of the battle and the highest scoring naval ace on the Supermarine Spitfire, a record which still stood by the end of the war.\n\nJohn Thach: John Smith \"Jimmy\" Thach (April 19, 1905 – April 15, 1981) was a World War II naval aviator, air combat tactician, and United States Navy admiral.  Thach developed the Thach Weave, a combat flight formation that could counter enemy fighters of superior performance, and later the big blue blanket, an aerial defense against Kamikaze attacks.\n\nQuestion: What was the name of the accomplished World War II naval ace who commanded squadron VF-80, retired from the U.S. Navy in 1959, and served with another legendary aviator born in 1905?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the individual.\"\n    },\n    \"role\": {\n      \"type\": \"string\",\n      \"description\": \"The primary role or achievement of the individual.\"\n    },\n    \"squadron_commanded\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the squadron commanded by the individual.\"\n    },\n    \"retirement_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the individual retired from the U.S. Navy.\"\n    },\n    \"served_with_legendary_aviator\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the individual served with a legendary aviator.\"\n    },\n    \"legendary_aviator_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the legendary aviator.\"\n        },\n        \"birth_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The birth year of the legendary aviator.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"birth_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"wars_participated_in\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of wars the individual participated in.\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"role\",\n    \"squadron_commanded\",\n    \"retirement_year\",\n    \"served_with_legendary_aviator\",\n    \"legendary_aviator_details\",\n    \"wars_participated_in\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The full name of the individual."
      },
      "role": {
        "type": "string",
        "description": "The primary role or achievement of the individual."
      },
      "squadron_commanded": {
        "type": "string",
        "description": "The name of the squadron commanded by the individual."
      },
      "retirement_year": {
        "type": "integer",
        "description": "The year the individual retired from the U.S. Navy."
      },
      "served_with_legendary_aviator": {
        "type": "boolean",
        "description": "Indicates if the individual served with a legendary aviator."
      },
      "legendary_aviator_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the legendary aviator."
          },
          "birth_year": {
            "type": "integer",
            "description": "The birth year of the legendary aviator."
          }
        },
        "required": [
          "name",
          "birth_year"
        ],
        "additionalProperties": false
      },
      "wars_participated_in": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of wars the individual participated in."
      }
    },
    "required": [
      "person_name",
      "role",
      "squadron_commanded",
      "retirement_year",
      "served_with_legendary_aviator",
      "legendary_aviator_details",
      "wars_participated_in"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
