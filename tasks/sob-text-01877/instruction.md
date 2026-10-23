{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\n9 Regiment Army Air Corps: 9 Regiment Army Air Corps was a regiment of the Army Air Corps (AAC).  It merged with 1 Regiment Army Air Corps in 2016 and is based at RNAS Yeovilton (HMS Heron).\n\nHelicopter: A helicopter is a type of rotorcraft in which lift and thrust are supplied by rotors.  This allows the helicopter to take off and land vertically, to hover, and to fly forward, backward, and laterally.  These attributes allow helicopters to be used in congested or isolated areas where fixed-wing aircraft and many forms of VTOL (vertical takeoff and landing) aircraft cannot perform.\n\nUnited States Army Air Corps: The United States Army Air Corps (USAAC) was the military aviation arm of the United States of America between 1926 and 1941.  After World War I, as early aviation became an increasingly important part of modern warfare, a philosophical rift developed between more traditional ground-based army personnel and those who felt that aircraft were being underutilized and that air operations were being stifled for political reasons unrelated to their effectiveness.  The USAAC was renamed from the earlier United States Army Air Service on 2 July 1926, and was part of the larger United States Army.  The Air Corps became the United States Army Air Forces (USAAF) on 20 June 1941, giving it greater autonomy from the Army's middle-level command structure.  During World War II, although not an administrative echelon, the Air Corps (AC) remained as one of the combat arms of the Army until 1947, when it was legally abolished by legislation establishing the Department of the Air Force.\n\nClaire Lee Chennault: Claire Lee Chennault (September 6, 1893 – July 27, 1958) was an American military aviator best known for his leadership of the \"Flying Tigers\" and the Republic of China Air Force in World War II.  Chennault was a fierce advocate of \"pursuit\" or fighter-interceptor aircraft during the 1930s when the United States Army Air Corps was focused primarily on high-altitude bombardment.  Chennault retired from the United States Army in 1937, and went to work as an aviation adviser and trainer in China.  Starting in early 1941, Chennault commanded the 1st American Volunteer Group (nicknamed \"Flying Tigers\").  One mission which never came to fruition was the bombing of Japanese cities; the bombers did not arrive before Pearl Harbor.  (B-29's started bombing from China in 1944, but they were not under Chennault's command.)  He headed both the volunteer group and the uniformed U.S. Army Air Forces units that replaced it in 1942.  He feuded constantly with General Joseph Stilwell, the U.S. Army commander in China, and helped China's leader Chiang Kai-shek to convince President Roosevelt to remove Stilwell in 1944.  The China-Burma-India theater was strategically essential in order to fix many vital elements of the Imperial Japanese Army on the Chinese mainland to limit their use against Allied forces advancing towards Japan in the two Pacific campaigns.\n\nNaval Training Center Orlando: Naval Training Center Orlando is a former United States Navy training installation located in Orlando, Florida.  It was originally established in 1940 as Orlando Army Air Base, a World War II advanced flight training base for the United States Army Air Corps, later United States Army Air Forces, that was also used earlier in the war for coastal patrols until the turnover of the coastal patrol mission to maritime patrol aircraft of the United States Navy and United States Coast Guard and civilian aircraft of the Civil Air Patrol.  Prior to 1940, the airport was used as the Orlando Municipal Airport, and served primarily commercial flights from its construction in 1929 to 1940.  When acquired by the Army Air Corps, multiple new landing strips were built to control the demand created by the many aircraft stationed at the base.\n\n2 Regiment Army Air Corps: 2 (Training) Regiment Army Air Corps is a regiment of the British Army's Army Air Corps.  It is responsible for all of the Army Air Corps' groundcrew Phase 2 and 3 training, as well as the Ground Support Commanders Course for officers.  The Regiment is based at Middle Wallop and is made up of two squadrons:\n\nProp and Wings: The Prop and Wings (propeller and wings) is a military insignia used to identify various aviation-related units in the United States military.  The Prop and Wings originated as branch insignia of the United States Army Air Service in 1920, and remained such from 1926 to 1947 for the successor United States Army Air Corps.  Approximately 90% of all officers serving in the United States Army Air Forces were commissioned in the Air Corps and wore the insignia.  Versions of the insignia are still used by the United States Air Force and the United States Army Aviation Branch.\n\nNo. 675 (The Rifles) Squadron AAC: No. 675 (The Rifles) Squadron Army Air Corps (675 Sqn) is a British Army Army Reserve groundcrew aviation support squadron.  It is part of 6 Regiment Army Air Corps (6 Regt AAC).  It is located in the city of Taunton, with a detachment currently at RNAS Yeovilton, in the county of Somerset.\n\nNo. 679 (The Duke of Connaught's) Squadron AAC: No. 679 (The Duke of Connaught's) Squadron AAC is a Helicopter Support squadron made up of the Volunteer Groundcrew of the Army Air Corps.\n\n6 Regiment Army Air Corps: 6 Regiment Army Air Corps is the sole Army Reserve regiment of the Army Air Corps (AAC).  The regiment operates in a groundcrew role, providing support to Army Aviation units of the Joint Helicopter Command.\n\nQuestion: what did Volunteer Groundcrew of the Army Air Corps use in isolated areas.\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"supported_entity_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of aircraft or entity that is supported.\"\n    },\n    \"supported_entity_category\": {\n      \"type\": \"string\",\n      \"description\": \"The broader category or classification of the supported entity.\"\n    },\n    \"support_unit_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the squadron or unit providing support.\"\n    },\n    \"support_unit_personnel\": {\n      \"type\": \"string\",\n      \"description\": \"The specific personnel group within the support unit.\"\n    },\n    \"operational_area_characteristic\": {\n      \"type\": \"string\",\n      \"description\": \"A characteristic of the areas where the supported entity is used.\"\n    }\n  },\n  \"required\": [\n    \"supported_entity_type\",\n    \"supported_entity_category\",\n    \"support_unit_name\",\n    \"support_unit_personnel\",\n    \"operational_area_characteristic\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "supported_entity_type": {
        "type": "string",
        "description": "The type of aircraft or entity that is supported."
      },
      "supported_entity_category": {
        "type": "string",
        "description": "The broader category or classification of the supported entity."
      },
      "support_unit_name": {
        "type": "string",
        "description": "The name of the squadron or unit providing support."
      },
      "support_unit_personnel": {
        "type": "string",
        "description": "The specific personnel group within the support unit."
      },
      "operational_area_characteristic": {
        "type": "string",
        "description": "A characteristic of the areas where the supported entity is used."
      }
    },
    "required": [
      "supported_entity_type",
      "supported_entity_category",
      "support_unit_name",
      "support_unit_personnel",
      "operational_area_characteristic"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
