{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe War at Home (1979 film): The War at Home is a documentary film about the anti-war movement in the Madison, Wisconsin area during the time of the Vietnam War.  It combines archival footage and interviews with participants that explore the events of the period on the University of Wisconsin–Madison campus.  The film was nominated for an Academy Award for Best Documentary Feature.\n\nItalian Armed Forces: The Italian Armed Forces (italian: \"Forze armate italiane\") encompass the Italian Army, the Italian Navy and the Italian Air Force.  A fourth branch of the armed forces, known as the Carabinieri, take on the role as the nation's military police and are also involved in missions and operations abroad as a combat force.  Despite not being a branch of the armed forces, the Guardia di Finanza is part of the military and operates a large fleet of ships, aircraft and helicopters, enabling it to patrol Italy's waters and to eventually participate in warfare scenarios.  These five forces have military status and are all organized along military lines, comprising a total of 350,000 men and women with the official status of active military personnel.  The President of the Italian Republic heads the armed forces as the President of the High Council of Defence established by article 87 of the Constitution of Italy.  According to article 78, the Parliament has the authority to declare a state of war and vest the necessary powers in the Government.\n\nYou Got to Move: You Got to Move is a documentary by Lucie Massie Phenix and Veronica Selver that follows people from communities in the Southern United States in their various processes of becoming involved in social change.  The film’s centerpiece is the Highlander Folk School (now known as Highlander Research and Education Center), a 75-year-old center for education and social action that was somehow involved in each of the lives chronicled in the documentary.\n\nCharles Scott (governor): Charles Scott (April 1739 – October 22, 1813) was an 18th-century American soldier who was elected the fourth governor of Kentucky in 1808.  Orphaned at an early age, Scott enlisted in the Virginia Regiment in October 1755 and served as a scout and escort during the French and Indian War.  He quickly rose through the ranks to become a captain.  After the war, he married and engaged in agricultural pursuits on land left to him by his father, but he returned to active military service in 1775 as the American Revolution began to grow in intensity.  In August 1776, he was promoted to colonel and given command of the 5th Virginia Regiment.  The 5th Virginia joined George Washington in New Jersey later that year, serving with him for the duration of the Philadelphia campaign.  Scott commanded Washington's light infantry, and by late 1778 was also serving as his chief of intelligence.  Furloughed at the end of the Philadelphia campaign, Scott returned to active service in March 1779 and was ordered to South Carolina to assist General Benjamin Lincoln in the southern theater.  He arrived in Charleston, South Carolina, just as Henry Clinton had begun his siege of the city.  Scott was taken as a prisoner of war when Charleston surrendered.  Paroled in March 1781 and exchanged for Lord Rawdon in July 1782, Scott managed to complete a few recruiting assignments before the war ended.\n\nLoot (2008 film): Loot is a 2008 documentary film.  It follows amateur treasure hunter Lance Larson in search of buried treasure from World War II, with the help of the two US war veterans—Darrel Ross and Andrew Seventy—responsible for burying them.  A major theme of the film involves the emotional risks of digging up one's past.\n\nVillisca National Guard Armory: The Villisca National Guard Armory is a historic building located in Villisca, Iowa, United States.  Villisca had active military units as far back as 1877.  Local citizens raised the funds to build the armory, which was completed in 1913.  Company F participated in the following military actions: Mexican Expedition, World War I, World War II, the Korean War, the Vietnam War, and the Gulf War.  The building was used for a variety of community events in addition to activities for the Iowa National Guard.  It was used as the gymnasium for the local high school until 1959.  Ownership of the building was transferred from the Villisca Armory Corporation to the State of Iowa in 1973, and in 2000 it was transferred to the Villisca Community School District.  During the 2000-2001 school year it was used for classroom space when the present high school building was under construction.  Subsequently, the building has been used for storage and various athletic functions.  It was listed on the National Register of Historic Places in 2015.\n\nOperation Daisy: Operation Daisy was a military operation conducted from November 1–20, 1981 by the South African Defence Force and South West African Territorial Force (SWATF) in Angola during the South African Border War and Angolan Civil War.  This conflict was sparked when the South African Defence Force decided to try to halt the regroup of the active military branch of SWAPO, also known as the People's Liberation Army of Namibia.\n\nDonald Nichols (spy): Donald Nichols (18 February 1923 – 2 June 1992) was a United States Air Force officer who worked in military intelligence.  He founded and commanded the U.S. Air Force's first active military intelligence unit, the 6004th Air Intelligence Service Squadron (6004th AISS), which he founded in 1950 during the Korean War.  Although he began his military career in the motor pool, he eventually sparked the infiltration of espionage teams behind communist lines, as well as personally gathering the first data on the communist MiG-15 fighter.  A trusted and reliable intelligence officer who had predicted the start date of the Korean War, he enjoyed 24-hour access to South Korean President Syngman Rhee and his own commanding officer, U.S. Air Force General Earle Partridge.  Under his leadership, the 6004th AISS served as the principal source of intelligence for Far East Air Force during the fighting.\n\n20/20: In an Instant: 20/20: In An Instant is an American documentary series on ABC.  The show premiered on Friday, March 6, 2015, before moving to its regular timeslot on Saturday, March 7, 2015, at 9:00 pm.  The show follows people who have gone through life changing events as they come to terms and relive the moments.\n\nThe Undateables: The Undateables is a British reality documentary show that has aired on Channel 4 since 3 April 2012 and is narrated by Sally Phillips.  The series follows people who have disabilities or learning difficulties on dates.\n\nQuestion: Which film, The War at Home or Loot follows people who were actually active military during a war?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film that follows people who were active military during a war.\"\n    },\n    \"reasoning\": {\n      \"type\": \"string\",\n      \"description\": \"Explanation of why the selected film fits the criteria, referencing details from the context.\"\n    },\n    \"military_personnel_featured\": {\n      \"type\": \"array\",\n      \"description\": \"Details about the military personnel featured in the film.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the military person.\"\n          },\n          \"role\": {\n            \"type\": \"string\",\n            \"description\": \"Their role or status (e.g., veteran, active military).\"\n          },\n          \"conflict_involved_in\": {\n            \"type\": \"string\",\n            \"description\": \"The war or conflict they were involved in.\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"role\",\n          \"conflict_involved_in\"\n        ],\n        \"additionalProperties\": false\n      }\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"reasoning\",\n    \"military_personnel_featured\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film that follows people who were active military during a war."
      },
      "reasoning": {
        "type": "string",
        "description": "Explanation of why the selected film fits the criteria, referencing details from the context."
      },
      "military_personnel_featured": {
        "type": "array",
        "description": "Details about the military personnel featured in the film.",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the military person."
            },
            "role": {
              "type": "string",
              "description": "Their role or status (e.g., veteran, active military)."
            },
            "conflict_involved_in": {
              "type": "string",
              "description": "The war or conflict they were involved in."
            }
          },
          "required": [
            "name",
            "role",
            "conflict_involved_in"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": [
      "film_title",
      "reasoning",
      "military_personnel_featured"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
