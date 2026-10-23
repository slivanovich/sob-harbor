{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJacob Beser: Jacob Beser (May 15, 1921 – June 16, 1992) was a lieutenant in the United States Army Air Forces who served during World War II.  Beser was the radar specialist aboard the \"Enola Gay\" on August 6, 1945, when it dropped the Little Boy atomic bomb on Hiroshima.  Three days later, Beser was a crewmember aboard \"Bockscar\" when the Fat Man bomb was dropped on Nagasaki.  He was the only person to have served as a strike crew member of both of the 1945 atomic bomb missions.\n\nTheodore Van Kirk: Theodore \"Dutch\" Van Kirk (February 27, 1921 – July 28, 2014) was a navigator in the United States Army Air Forces, best known as the navigator of the \"Enola Gay\" when it dropped the first atomic bomb on Hiroshima.  With the death of fellow crewman Morris Jeppson (who died on March 30, 2010), Van Kirk became the last surviving member of the \"Enola Gay\" crew.  He died four years later on July 28, 2014.\n\nLittle Boy: \"Little Boy\" was the codename for the atomic bomb dropped on the Japanese city of Hiroshima on 6 August 1945 during World War II by the Boeing B-29 Superfortress \"Enola Gay\", piloted by Colonel Paul W. Tibbets, Jr., commander of the 509th Composite Group of the United States Army Air Forces.  It was the first atomic bomb to be used in warfare.  The Hiroshima bombing was the second artificial nuclear explosion in history, after the Trinity test, and the first uranium-based detonation.  It exploded with an energy of approximately 15 ktonTNT .  The bomb caused significant destruction to the city of Hiroshima and its occupants.\n\nEnola; or, Her fatal mistake: Enola; or, Her fatal mistake is an 1886 book written by Mary Young Ridenbaugh.  It is notable for being the inspiration, indirectly, for the naming of the Enola Gay, the B-29 bomber airplane which dropped the first atomic bomb on Hiroshima.  Its commanding pilot, Colonel Paul Tibbets, named the aircraft after his mother, Enola Gay Tibbets (1893–1983), who was named after the title character of Ridenbaugh's book.\n\nRobert A. Lewis: Robert Alvin Lewis (October 18, 1917 – June 18, 1983) was a United States Army Air Forces officer serving in the Pacific Theatre during World War II.  He was the co-pilot of the \"Enola Gay\", the B-29 Superfortress bomber which dropped the atomic bomb Little Boy on the Japanese city of Hiroshima on 6 August 1945.\n\nAbove and Beyond (film): Above and Beyond is a 1952 American war film about Lt. Col. Paul W. Tibbets, Jr., the pilot of the aircraft that dropped the atomic bomb on Hiroshima in August 1945.\n\nGeorge Benedict Zabelka: George B. Zabelka, a Catholic chaplain with the U.S. Army Air Force, was stationed on Tinian Island in the South Pacific in 1945, where he was assigned to 509th Composite Group.  This is the unit of the crews of \"Enola Gay\" and \"Bockscar\" (aka Bock’s Car and Bocks Car), that dropped the Atomic Bombs (”Little Boy” and “Fat Man”) on Hiroshima and Nagasaki.  His duties included saying Mass on Sunday and during the week, hearing confessions, talking with the soldiers, and other typical duties of a wartime chaplain.\n\nWilliam Sterling Parsons: Rear Admiral William Sterling \"Deak\" Parsons (26 November 1901 – 5 December 1953) was an American naval officer who worked as an ordnance expert on the Manhattan Project during World War II.  He is best known for being the weaponeer on the \"Enola Gay\", the aircraft which dropped the Little Boy atomic bomb on Hiroshima, Japan in 1945.  To avoid the possibility of a nuclear explosion if the aircraft crashed and burned on takeoff, he decided to arm the bomb in flight.  While the aircraft was \"en route\" to Hiroshima, Parsons climbed into the cramped and dark bomb bay, and inserted the powder charge and detonator.  He was awarded the Silver Star for his part in the mission.\n\nPaul Tibbets: Paul Warfield Tibbets Jr. (23 February 1915 – 1 November 2007) was a brigadier general in the United States Air Force.  He is best known as the pilot who flew the \"Enola Gay\" (named after his mother) when it dropped Little Boy, the first of two atomic bombs used in warfare, on the Japanese city of Hiroshima.\n\nEnola Gay: The Enola Gay ( ) is a Boeing B-29 Superfortress bomber, named for Enola Gay Tibbets, the mother of the pilot, Colonel Paul Tibbets, who selected the aircraft while it was still on the assembly line.  On 6 August 1945, during the final stages of World War II, it became the first aircraft to drop an atomic bomb.  The bomb, code-named \"Little Boy\", was targeted at the city of Hiroshima, Japan, and caused unprecedented destruction.  \"Enola Gay\" participated in the second atomic attack as the weather reconnaissance aircraft for the primary target of Kokura.  Clouds and drifting smoke resulted in a secondary target, Nagasaki, being bombed instead.\n\nQuestion: Above and Beyond is a 1952 American war film about Lt. Col. Paul W. Tibbets, Jr., best known as the pilot who flew the \"Enola Gay\" when it dropped Little Boy, the first of two atomic bombs used in warfare, on the Japanese city of what?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_information\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"release_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"pilot_information\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"rank_at_time_of_film_subject\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"rank_at_time_of_film_subject\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"bombing_event\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"aircraft_name\": {\n          \"type\": \"string\"\n        },\n        \"bomb_codename\": {\n          \"type\": \"string\"\n        },\n        \"bomb_type\": {\n          \"type\": \"string\"\n        },\n        \"target_city\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"aircraft_name\",\n        \"bomb_codename\",\n        \"bomb_type\",\n        \"target_city\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_information\",\n    \"pilot_information\",\n    \"bombing_event\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_information": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string"
          },
          "release_year": {
            "type": "integer"
          }
        },
        "required": [
          "title",
          "release_year"
        ],
        "additionalProperties": false
      },
      "pilot_information": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "rank_at_time_of_film_subject": {
            "type": "string"
          }
        },
        "required": [
          "name",
          "rank_at_time_of_film_subject"
        ],
        "additionalProperties": false
      },
      "bombing_event": {
        "type": "object",
        "properties": {
          "aircraft_name": {
            "type": "string"
          },
          "bomb_codename": {
            "type": "string"
          },
          "bomb_type": {
            "type": "string"
          },
          "target_city": {
            "type": "string"
          }
        },
        "required": [
          "aircraft_name",
          "bomb_codename",
          "bomb_type",
          "target_city"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_information",
      "pilot_information",
      "bombing_event"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
