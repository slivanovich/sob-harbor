{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nShaw Air Force Base: Shaw Air Force Base (Shaw AFB) (IATA: SSC, ICAO: KSSC, FAA LID: SSC) is a United States Air Force base located approximately 8.4 mi west-northwest of downtown Sumter, South Carolina.  It is under the jurisdiction of the United States Air Force Air Combat Command (ACC).  The United States Air Force 20th Fighter Wing (20th FW) is the host unit.\n\n924th Fighter Group: The 924th Fighter Group is a group of the United States Air Force Reserve.  It assigned to Tenth Air Force and stationed at Davis-Monthan Air Force Base, Arizona as a Geographically Separated Unit (GSU) of the Air Force Reserve Command's 442d Fighter Wing at Whiteman Air Force Base, Missouri.  On 1 October 2012, the 924 FG was reassigned to the 944th Fighter Wing at Luke Air Force Base, Arizona.  The 924th flies the A-10 Thunderbolt II aircraft and is gained by Air Combat Command when mobilized.\n\nJimmy DeHart: James DeHart (August 25, 1893 – March 4, 1935) was an American football player and coach.  He served as the head coach at Duke University from 1926 to 1930 and Washington & Lee University from 1922 to 1925 and again from 1931 to 1932, compiling a career college football record of 51–50–6.  DeHart also served as an assistant on the coaching staff at the University of Georgia.  In 1935, he signed a contract to become the head coach at Southwestern University in Memphis, Tennessee, but fell ill and died while relocating.  He attended the University of Pittsburgh, where he played football for the Panthers from 1914 to 1916 and in 1918, where he was hailed as a \"star\".  DeHart played quarterback under head coach Glenn \"Pop\" Warner and led the 1916 team to an undefeated season.  He also earned letters in basketball, baseball, and track at Pittsburgh.  DeHart put his college education on hiatus to serve in the United States Army during World War I.  As a lieutenant in the Aviation Section, he coached a service team at Mather Field.  He returned to Pittsburgh after his time in the Army.  After graduation, he coached the backfield at the University of Georgia from 1920 to 1921.\n\nJohn J. Closner III: John James Closner III (born March 27, 1940) was a major general in the United States Air Force who served as Commander of the United States Air Force Reserve Command, Headquarters U.S. Air Force, Washington D.C., and commander, Headquarters Air Force Reserve, a separate operating agency located at Robins Air Force Base, Georgia.  As chief of Air Force Reserve, he served as the principal adviser on Reserve matters to the Air Force Chief of Staff.  As commander of AFRES, he had full responsibility for the supervision of U.S. Air Force Reserve units around the world.\n\nMather Air Force Base: Mather Air Force Base (Mather AFB) was a United States Air Force Base, which was closed in 1993.  It was located 12 mi east of Sacramento, on the south side of U.S. Route 50 in Sacramento County, California.  Mather Field was one of 32 Air Service training camps established after the United States entry into World War I in April 1917.\n\nDouble cantilever hangar: A Double cantilever hangar is a type of hangar that was constructed by the United States Air Force during the Cold War.  Large hangers were constructed at Castle Air Force Base, Loring Air Force Base, Carswell Air Force Base, and Travis Air Force Base, while smaller hangars were constructed at March Air Force Base, Edwards Air Force Base, Hanscom Air Force Base, and Homestead Air Force Base.\n\n5th Bomb Wing: The 5th Bomb Wing (5 BW) is a United States Air Force unit assigned to Air Force Global Strike Command's Eighth Air Force.  It is stationed at Minot Air Force Base, North Dakota.  The wing is also the host unit at Minot.  The 5 BW is one of only two Boeing B-52H Stratofortress wings in the United States Air Force, the other being the 2d Bomb Wing at Barksdale Air Force Base, Louisiana.\n\nMichelle D. Johnson: Michelle D. Johnson is a Lieutenant General in the United States Air Force and was the 19th Superintendent of the United States Air Force Academy.  She is the first woman to lead a United States Department of Defense Service Academy.  Her previous position was the Deputy Chief of Staff, Operations and Intelligence, Supreme Headquarters Allied Powers Europe in Casteau, Belgium.  She was formerly the Director, Strategy, Policy, Programs and Logistics, U.S. Transportation Command at Scott Air Force Base.  She also served as the deputy director for information and cyberspace policy, Strategic Plans and Policy Directorate at the Pentagon.  As an Air Force cadet, she was the first woman to serve as Cadet Wing Commander (the senior ranking cadet) at the United States Air Force Academy.  Johnson played basketball for the Air Force Falcons women's basketball team.  She was twice named an Academic All-American and was inducted into the Academic All-American Hall of Fame in 2007, making her the first woman from the Academy and one of only six graduates with that distinction.  Also, she was selected as the Academy's first woman Rhodes Scholar in her First Class (Senior) Year.  Johnson was recognized as an Honorary Fellow of Brasenose College in 2013.  She received the 2014 American Legion Auxiliary Woman of the Year Award.  Lt. General Johnson was awarded a star (#42) on The Flag for Hope on June 18, 2016 in recognition of her outstanding military service.\n\nJames E. Sherrard III: James Edward Sherrard III (born January 1, 1943) was a lieutenant general in the United States Air Force who served as Commander of the United States Air Force Reserve Command, Headquarters U.S. Air Force, Washington D.C., and commander, Headquarters Air Force Reserve, a separate operating agency located at Robins Air Force Base, Georgia.  As chief of Air Force Reserve, he served as the principal adviser on Reserve matters to the Air Force Chief of Staff.  As commander of AFRES, he had full responsibility for the supervision of U.S. Air Force Reserve units around the world.  He served in this position from November 1994 to June 1998.\n\nTwenty-Fifth Air Force: Twenty-Fifth Air Force (25 AF), also known as Air Force Intelligence is a numbered air force (NAF) within the United States Air Force (USAF), and serves as the Air Force's premier military intelligence organization.  25 AF was established on 29 September 2014 by redesignating the Air Force Intelligence, Surveillance and Reconnaissance Agency (a field operating agency) under Headquarters, United States Air Force, to a numbered air force aligned under Air Combat Command.  USAF also realigned the 9th Reconnaissance Wing and the 55th Wing under the new NAF.  It is headquartered at Lackland Air Force Base, Texas.\n\nQuestion: James DeHart coached a service team at which United States Air Force Base, which was closed in 1993?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person who coached the service team.\"\n    },\n    \"activity\": {\n      \"type\": \"string\",\n      \"description\": \"The activity performed by the person at the base.\"\n    },\n    \"base_information\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"base_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the Air Force Base.\"\n        },\n        \"base_type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of military installation.\"\n        },\n        \"closure_status\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the base was closed.\"\n        },\n        \"closure_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the base was closed.\"\n        }\n      },\n      \"required\": [\n        \"base_name\",\n        \"base_type\",\n        \"closure_status\",\n        \"closure_year\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"activity\",\n    \"base_information\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the person who coached the service team."
      },
      "activity": {
        "type": "string",
        "description": "The activity performed by the person at the base."
      },
      "base_information": {
        "type": "object",
        "properties": {
          "base_name": {
            "type": "string",
            "description": "The name of the Air Force Base."
          },
          "base_type": {
            "type": "string",
            "description": "The type of military installation."
          },
          "closure_status": {
            "type": "boolean",
            "description": "Indicates if the base was closed."
          },
          "closure_year": {
            "type": "integer",
            "description": "The year the base was closed."
          }
        },
        "required": [
          "base_name",
          "base_type",
          "closure_status",
          "closure_year"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "person_name",
      "activity",
      "base_information"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
