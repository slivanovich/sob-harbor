{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nFairchild K-20: The K-20 is an aerial photography camera used during World War II, e.g., from the Enola Gay's tail gunner position of the mushroom cloud over Hiroshima.  Designed by Fairchild Camera and Instrument, approximately 15,000 were manufactured under licence for military contract by Folmer Graflex Corporation in Rochester, NY between 1941 and 1945.  The K-20 uses a 5.25\"x20 to 5.25\"x200 foot Roll Film, with an image size of 4x5 inches.  Lenses were 6 3/8\" f/4.5 with an adjustable diaphragm and were non interchangeable, these were made by Kodak, Ilex, or Bausch & Lomb, as available at the time of order.  The camera featured the use of a vacuum to keep the film flat.\n\nPaul Tibbets: Paul Warfield Tibbets Jr. (23 February 1915 – 1 November 2007) was a brigadier general in the United States Air Force.  He is best known as the pilot who flew the \"Enola Gay\" (named after his mother) when it dropped Little Boy, the first of two atomic bombs used in warfare, on the Japanese city of Hiroshima.\n\nEnola; or, Her fatal mistake: Enola; or, Her fatal mistake is an 1886 book written by Mary Young Ridenbaugh.  It is notable for being the inspiration, indirectly, for the naming of the Enola Gay, the B-29 bomber airplane which dropped the first atomic bomb on Hiroshima.  Its commanding pilot, Colonel Paul Tibbets, named the aircraft after his mother, Enola Gay Tibbets (1893–1983), who was named after the title character of Ridenbaugh's book.\n\nMorris R. Jeppson: Morris Richard Jeppson (June 23, 1922 – March 30, 2010) was a Second Lieutenant in the United States Army Air Forces during World War II.  He served as assistant weaponeer on the \"Enola Gay\", which dropped the first atomic bomb on the city of Hiroshima, Japan on August 6, 1945.\n\nJacob Beser: Jacob Beser (May 15, 1921 – June 16, 1992) was a lieutenant in the United States Army Air Forces who served during World War II.  Beser was the radar specialist aboard the \"Enola Gay\" on August 6, 1945, when it dropped the Little Boy atomic bomb on Hiroshima.  Three days later, Beser was a crewmember aboard \"Bockscar\" when the Fat Man bomb was dropped on Nagasaki.  He was the only person to have served as a strike crew member of both of the 1945 atomic bomb missions.\n\nWilliam Sterling Parsons: Rear Admiral William Sterling \"Deak\" Parsons (26 November 1901 – 5 December 1953) was an American naval officer who worked as an ordnance expert on the Manhattan Project during World War II.  He is best known for being the weaponeer on the \"Enola Gay\", the aircraft which dropped the Little Boy atomic bomb on Hiroshima, Japan in 1945.  To avoid the possibility of a nuclear explosion if the aircraft crashed and burned on takeoff, he decided to arm the bomb in flight.  While the aircraft was \"en route\" to Hiroshima, Parsons climbed into the cramped and dark bomb bay, and inserted the powder charge and detonator.  He was awarded the Silver Star for his part in the mission.\n\nSteven F. Udvar-Hazy Center: The Steven F. Udvar-Hazy Center, also called the Udvar-Hazy Center, is the Smithsonian National Air and Space Museum (NASM)'s annex at Washington Dulles International Airport in the Chantilly area of Fairfax County, Virginia, United States.  It holds numerous exhibits, including the Space Shuttle \"Discovery\" and the \"Enola Gay\".\n\nEnola Gay: The Enola Gay ( ) is a Boeing B-29 Superfortress bomber, named for Enola Gay Tibbets, the mother of the pilot, Colonel Paul Tibbets, who selected the aircraft while it was still on the assembly line.  On 6 August 1945, during the final stages of World War II, it became the first aircraft to drop an atomic bomb.  The bomb, code-named \"Little Boy\", was targeted at the city of Hiroshima, Japan, and caused unprecedented destruction.  \"Enola Gay\" participated in the second atomic attack as the weather reconnaissance aircraft for the primary target of Kokura.  Clouds and drifting smoke resulted in a secondary target, Nagasaki, being bombed instead.\n\nEnola Gay (song): \"Enola Gay\" is an anti-war song by the British synthpop group Orchestral Manoeuvres in the Dark (OMD), and the only single from the band's 1980 album, \"Organisation\".  The track addresses the atomic bombing of Hiroshima on 6 August 1945, during the final stages of World War II.\n\nAbove and Beyond (film): Above and Beyond is a 1952 American war film about Lt. Col. Paul W. Tibbets, Jr., the pilot of the aircraft that dropped the atomic bomb on Hiroshima in August 1945.\n\nQuestion: What \"Enola Gay\" pilot has a war film based on him called Above and Beyond?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"pilot_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the pilot.\"\n    },\n    \"aircraft_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the aircraft piloted.\"\n    },\n    \"film_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the film based on the pilot.\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the film.\"\n        },\n        \"genre\": {\n          \"type\": \"string\",\n          \"description\": \"The genre of the film.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"release_year\",\n        \"genre\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"pilot_name\",\n    \"aircraft_name\",\n    \"film_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "pilot_name": {
        "type": "string",
        "description": "The full name of the pilot."
      },
      "aircraft_name": {
        "type": "string",
        "description": "The name of the aircraft piloted."
      },
      "film_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the film based on the pilot."
          },
          "release_year": {
            "type": "integer",
            "description": "The release year of the film."
          },
          "genre": {
            "type": "string",
            "description": "The genre of the film."
          }
        },
        "required": [
          "title",
          "release_year",
          "genre"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "pilot_name",
      "aircraft_name",
      "film_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
