{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe 9th Company: The 9th Company (Russian: 9 Рота ) is a 2005 Russian war film directed by Fedor Bondarchuk and set during the Soviet War in Afghanistan.  The film is loosely based on a real-life battle that took place at Elevation 3234 in early 1988, during the last large-scale Soviet military operation (Magistral) in Afghanistan.\n\nJalaluddin Haqqani: Mawlawi Jalaluddin Haqqani (Pashto: جلال الدين حقاني‎ ) (born 1939) is the leader of the Haqqani network, an insurgent group fighting in guerilla warfare initially against US-led NATO forces, and the present government of Afghanistan they support.  He distinguished himself as an internationally sponsored insurgent fighter in the 1980s during the Soviet war in Afghanistan, including Operation Magistral.  By 2004, he was directing pro-Taliban militants to launch a holy war in Afghanistan.  Within Pakistan, Jalaluddin had a cordial relation with Pakistan but he did not act against the TTP, earning controversy though Pakistan saw him as a strategic asset who could mediate between the various factions.  Jalaluddin retains considerable local popularity on the Afghanistan-Pakistan border, and he is the most experienced Islamist leader in the region.  Steve Coll, author of \"Ghost Wars\", claims that Haqqani introduced suicide bombing in the Afghanistan-Pakistan region.\n\nInvasion of the Kuril Islands: The Invasion of the Kuril Islands (Russian: Курильская десантная операция \"Kuril Islands Landing Operation\") was the World War II Soviet military operation to capture the Kuril Islands from Japan in 1945.  The invasion was part of the Manchurian Strategic Offensive Operation, and was decided on when plans to land on Hokkaido were abandoned.  The successful military operations of the Red Army at Mudanjiang and during the Invasion of South Sakhalin created the necessary prerequisites for invasion of the Kuril Islands.\n\nOperation Magistral: Operation Magistral was a Soviet Army military operation during the Soviet war in Afghanistan that began in late November 1987 and ended in early January 1988.\n\nSoviet–Lithuanian Mutual Assistance Treaty: The Soviet–Lithuanian Mutual Assistance Treaty (Lithuanian: \"Lietuvos-Sovietų Sąjungos savitarpio pagalbos sutartis\" ) was a bilateral treaty signed between the Soviet Union and Lithuania on October 10, 1939.  According to provisions outlined in the treaty, Lithuania would acquire about one fifth of the Vilnius Region, including Lithuania's historical capital, Vilnius, and in exchange would allow five Soviet military bases with 20,000 troops to be established across Lithuania.  In essence the treaty with Lithuania was very similar to the treaties that the Soviet Union signed with Estonia on September 28, and with Latvia on October 5.  According to official Soviet sources, the Soviet military was strengthening the defenses of a weak nation against possible attacks by Nazi Germany.  The treaty provided that Lithuania's sovereignty would not be affected.  However, in reality the treaty opened the door for the first Soviet occupation of Lithuania and was described by \"The New York Times\" as \"virtual sacrifice of independence.\"\n\nOperation River Falcon: Operation River Falcon was a military operation in the Iraq War.  From 25–27 July 2006, elements of the United States Army 2nd Brigade Combat Team, 4th Infantry Division (including elements of the 2nd Battalion, 8th Infantry Regiment, and the 1st Battalion, 10th Cavalry Regiment) conducted Operation River Falcon in and around the town of Sayifiyeh in Iraq.  The operation was aimed at denying terrorists the use of the town as a safe haven, disrupting insurgent attacks on Coalition and Iraqi Security Forces, and on collecting and destroying insurgent munitions.\n\nOperation Iskra: Operation Iskra (Russian: операция «Искра» , \"operatsiya Iskra\"; English: Operation Spark ) was a Soviet military operation during World War II, designed to break the German Wehrmacht's Siege of Leningrad.  Planning for the operation began shortly after the failure of the Sinyavino Offensive.  The German defeat in the Battle of Stalingrad in late 1942 had weakened the German front.  By January 1943, Soviet forces were planning or conducting offensive operations across the entire German-Soviet front, especially in southern Russia, Iskra being the northern part of the wider Soviet 1942–1943 winter counter offensive.\n\nExport variants of Soviet military equipment: Export variants of Soviet military equipment were versions of Soviet military equipment (armored vehicles, airplanes, missiles) of significantly inferior capability to the original designs and intended only for export.  Monkey model was the unofficial designation given by the Soviet Military to such variants.  The monkey model was exported with the same or a similar designation as the original Soviet design but in fact it lacked many of the advanced or expensive features of the original.\n\nSoviet invasion of Poland: The Soviet invasion of Poland was a Soviet military operation that started without a formal declaration of war on 17 September 1939.  On that morning, 16 days after Germany invaded Poland from the west, the Soviet Union invaded Poland from the east.  The invasion and the battle lasted for the following 20 days and ended on 6 October 1939 with the two-way division and annexation of the entire territory of the Second Polish Republic by both Germany and the Soviet Union.  The joint German-Soviet invasion of Poland was secretly agreed to in the Molotov-Ribbentrop Pact, signed on 23 August 1939.\n\nOperation Whalers: Operation Whalers was a United States Marine Corps military operation that took place in Afghanistan's Kunar Province, in August 2005, just weeks after Operation Red Wings.  Like Operation Red Wings, the objective of Operation Whalers was the disruption of Anti-Coalition Militia (ACM) activity in the region in support of further stabilizing the region for unencumbered voter turnout for the September 18, 2005 Afghan National Parliamentary Elections.  Operation Whalers was planned and executed by the 2nd Battalion of the 3rd Marine Regiment (2/3).  The emphasis of the operation was an Anti-Coalition Militia cell led by Ahmad Shah, which was one of 22 identified ACM groups operating in the region at that time, and was the most active.  Ahmad Shah's cell was responsible for the Navy SEAL ambush and subsequent MH-47 shootdown that killed, in total, 19 U.S. special operations personnel during Operation Red Wings.  Operation Whalers, named after the Hartford / New England Whalers professional hockey team, was the \"sequel\" to Operation Red Wings in that it was aimed at furthering stabilization of the security situation in the restive Kunar Province of Eastern Afghanistan, a long-term goal of American and coalition forces operating in the area at that time.  Operation Whalers, conducted by a number of Marine infantry companies of 2/3 with attached Afghan National Army soldiers and supported by conventional Army aviation, intelligence, and combat arms forces units and U.S. Air Force aviation assets, proved a success.  Anti-Coalition Militia activity dropped substantially and subsequent human intelligence and signals intelligence revealed that Ahmad Shah had been seriously wounded.  Shah, who sought to disrupt the September 18, 2005 Afghan National Parliamentary Elections, was not able to undertake any significant Anti-Coalition operations subsequent to Operation Whalers in Kunar or neighboring provinces.\n\nQuestion: The Soviet military operation in Afghanistan beginning in 1987 featured what distinguished insurgent born in 1939?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"insurgent_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the distinguished insurgent.\"\n    },\n    \"birth_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth year of the insurgent.\"\n    },\n    \"military_operation\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the Soviet military operation.\"\n        },\n        \"start_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the operation began.\"\n        },\n        \"end_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the operation ended.\"\n        },\n        \"conflict\": {\n          \"type\": \"string\",\n          \"description\": \"The larger conflict the operation was part of.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"start_year\",\n        \"end_year\",\n        \"conflict\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"insurgent_role\": {\n      \"type\": \"string\",\n      \"description\": \"Description of the insurgent's role in the conflict/operation.\"\n    }\n  },\n  \"required\": [\n    \"insurgent_name\",\n    \"birth_year\",\n    \"military_operation\",\n    \"insurgent_role\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "insurgent_name": {
        "type": "string",
        "description": "The name of the distinguished insurgent."
      },
      "birth_year": {
        "type": "integer",
        "description": "The birth year of the insurgent."
      },
      "military_operation": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the Soviet military operation."
          },
          "start_year": {
            "type": "integer",
            "description": "The year the operation began."
          },
          "end_year": {
            "type": "integer",
            "description": "The year the operation ended."
          },
          "conflict": {
            "type": "string",
            "description": "The larger conflict the operation was part of."
          }
        },
        "required": [
          "name",
          "start_year",
          "end_year",
          "conflict"
        ],
        "additionalProperties": false
      },
      "insurgent_role": {
        "type": "string",
        "description": "Description of the insurgent's role in the conflict/operation."
      }
    },
    "required": [
      "insurgent_name",
      "birth_year",
      "military_operation",
      "insurgent_role"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
