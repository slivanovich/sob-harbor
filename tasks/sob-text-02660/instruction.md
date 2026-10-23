{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSecond Phase Campaign: The Second Phase Campaign of the Korean War was an extended military offensive by the Chinese People's Volunteer Army during the last week of November, 1950, and the first two weeks of December.  The two major engagements were battles near the Ch'ongch'on River in the Chinese-designated Western Sector and Chosin Reservoir in their Eastern Sector.  The Chinese opposed United Nations-authorized forces composed of American military and various allied forces.\n\nBattle of Guam (1944): The Second Battle of Guam (21 July – 10 August 1944) was the American recapture of the Japanese-held island of Guam, a U.S. territory in the Mariana Islands captured by the Japanese from the U.S. in the 1941 First Battle of Guam during the Pacific campaign of World War II.\n\nBattle of the Ch'ongch'on River: The Battle of the Ch'ongch'on River, also known as the Battle of the Ch'ongch'on () or the Second Phase Campaign Western Sector (), was a decisive battle in the Korean War, and it took place from November 25 to December 2, 1950, along the Ch'ongch'on River Valley in the northwestern part of North Korea.  In response to the successful Chinese First Phase Campaign against the United Nations forces, General Douglas MacArthur launched the Home-by-Christmas Offensive to evict the Chinese forces from Korea and to end the war.  Anticipating this reaction, the Chinese People's Volunteer Army Commander Peng Dehuai planned a counteroffensive, dubbed the \"Second Phase Campaign\", against the advancing UN forces.\n\nMYH16 gene: The MYH16 gene encodes a protein called myosin heavy chain 16 which is a muscle protein in mammals.  At least in primates, it is a specialized muscle protein found only in the temporalis and masseter muscles of the jaw.  Myosin heavy chain proteins are important in muscle contraction, and if they are missing, the muscles will be smaller.  In non-human primates, MYH16 is functional and the animals have powerful jaw muscles.  In humans, the MYH16 gene has a mutation which causes the protein not to function.  Although the exact importance of this change in accounting for differences between humans and other apes is not yet clear, such a change may be related to increased brain size and finer control of the jaw which facilitates speech.  It is not clear how the MYH16 mutation relates to other changes to the jaw and skull in early human evolution (for example, whether the MYH16 mutation happened first and led to other changes, or whether the MYH16 mutation happened after other changes made the MYH16 protein no longer necessary).\n\nBattle of Wawon: The Battle of Wawon (Turkish: \"Kunuri Muharebeleri\" ), also known as the Battle of Wayuan (), was a series of delay actions of the Korean War that took place from November 27–29, 1950 near Wawon in present-day North Korea.  After the collapse of the US Eighth Army's right flank during the Battle of the Ch'ongch'on River, the Chinese 38th Corps advanced rapidly towards the critical road junction at Kunu-ri in an effort to cut off United Nations forces' retreat route.  In what was considered to be Turkey's first real combat action since the aftermath of World War I, the Turkish Brigade attempted to delay the Chinese advances at Wawon.  Although during the battle the Turkish Brigade was crippled after being encircled by Chinese forces with superior numbers, they were still be able to breach the Chinese trap and rejoin the US 2nd Infantry Division.\n\nBattle of Guam (1941): The First Battle of Guam was an engagement during the Pacific War in World War II, and took place from 8 December to 10 December 1941 on Guam in the Mariana Islands between Japan and the United States.  The American garrison was defeated by Japanese forces on 10 December, which resulted in an occupation until the Second Battle of Guam in 1944.\n\nTaeryong River: Taeryong River is a river of North Korea.  The river is a tributary of the Ch'ongch'on River.\n\nThird Battle of Seoul: The Third Battle of Seoul, also known as the Chinese New Year's Offensive, the January–Fourth Retreat (Korean: 1•4 후퇴 ) or the Third Phase Campaign Western Sector (), was a battle of the Korean War, which took place from December 31, 1950 to January 7, 1951 around the South Korean capital of Seoul.  In the aftermath of the major Chinese victory at the Battle of the Ch'ongch'on River, the United Nations Command started to contemplate the possibility of evacuation from the Korean Peninsula.  Upon learning of this development, China's Chairman Mao Zedong ordered the Chinese People's Volunteer Army to cross the 38th parallel in an effort to pressure the United Nations forces to withdraw from South Korea.\n\nGeorge McMillin: George Johnson McMillin (November 25, 1889 – August 29, 1983 ) was a United States Navy Rear Admiral who served as the 38th and final Naval Governor of Guam.  He graduated from the United States Naval Academy in 1911 and served as an officer during four separate conflicts: World War I, the occupation of the Dominican Republic, the United States occupation of Veracruz, and World War II.  He served on the staff of both the Naval Academy and the Naval War College as well.  He is most remembered as the commander who surrendered Guamanian forces to a much larger Japanese force during the First Battle of Guam, only the second battle of World War II involving the United States.  He had previously evacuated all but one civilian American citizen from the island and attempted to rebuild defenses after a strong typhoon devastated the island the year before.  On December 8, 1941, Japanese forces invaded Guam and McMillin surrendered two days later.  He spent the rest of the war at various Japanese prisoner of war camps.\n\nEighth Army Ranger Company: The Eighth Army Ranger Company, also known as the 8213th Army Unit, was a Ranger light infantry company of the United States Army that was active during the Korean War.  As a small special forces unit, it specialized in irregular warfare.  Intended to combat the North Korean (NK) commandos who had been effective at infiltration and disruption behind United Nations (UN) lines, the Eighth Army Ranger Company was formed at the height of the Battle of Pusan Perimeter in September 1950 and was the first U.S. Army Ranger unit created since World War II.  The company went into action as a part of the 25th Infantry Division during the UN advance into North Korea in October and November.  It was best known for its defense of Hill 205 against an overwhelming Chinese attack during the Battle of the Ch'ongch'on River which resulted 41 of the 51 Rangers becoming casualties.\n\nQuestion: Which happened first, the Battle of the Ch'ongch'on River or the Battle of Guam?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"event_a\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the first event being compared.\"\n        },\n        \"start_date\": {\n          \"type\": \"string\",\n          \"description\": \"The start date of the first event.\"\n        },\n        \"end_date\": {\n          \"type\": \"string\",\n          \"description\": \"The end date of the first event.\"\n        },\n        \"year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the first event started.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"start_date\",\n        \"end_date\",\n        \"year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"event_b\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the second event being compared.\"\n        },\n        \"start_date\": {\n          \"type\": \"string\",\n          \"description\": \"The start date of the second event.\"\n        },\n        \"end_date\": {\n          \"type\": \"string\",\n          \"description\": \"The end date of the second event.\"\n        },\n        \"year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the second event started.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"start_date\",\n        \"end_date\",\n        \"year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"earlier_event_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the event that occurred first.\"\n    }\n  },\n  \"required\": [\n    \"event_a\",\n    \"event_b\",\n    \"earlier_event_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "event_a": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the first event being compared."
          },
          "start_date": {
            "type": "string",
            "description": "The start date of the first event."
          },
          "end_date": {
            "type": "string",
            "description": "The end date of the first event."
          },
          "year": {
            "type": "integer",
            "description": "The year the first event started."
          }
        },
        "required": [
          "name",
          "start_date",
          "end_date",
          "year"
        ],
        "additionalProperties": false
      },
      "event_b": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the second event being compared."
          },
          "start_date": {
            "type": "string",
            "description": "The start date of the second event."
          },
          "end_date": {
            "type": "string",
            "description": "The end date of the second event."
          },
          "year": {
            "type": "integer",
            "description": "The year the second event started."
          }
        },
        "required": [
          "name",
          "start_date",
          "end_date",
          "year"
        ],
        "additionalProperties": false
      },
      "earlier_event_name": {
        "type": "string",
        "description": "The name of the event that occurred first."
      }
    },
    "required": [
      "event_a",
      "event_b",
      "earlier_event_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
