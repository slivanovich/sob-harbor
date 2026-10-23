{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDon Dillard: Dillard's pro career lasted 13 seasons, beginning in 1955 in the Cleveland farm system.  He made the Indians' 1959 roster coming out of spring training, but had only six at bats as a pinch hitter during the season's early weeks before returning to the minor leagues, where he batted .283 in the Pacific Coast League.  He added four more pinch hitting appearances that September, and ended his first big-league campaign as a .400 batter, with four singles and an RBI in ten at bats.  The 1960 season was much the same; he had eight plate appearances and seven at bats with the Indians, and played the bulk of the year for the Triple-A Toronto Maple Leafs, batting .294.\n\nSecond Messenian War: The Second Messenian War was a war between the Ancient Greek states of Messenia and Sparta.  It started around 40 years after the end of the First Messenian War with the uprising of a slave rebellion.  This war lasted from 685 to 668 BC.  Other scholars, however, assign later dates, claiming, for example, that 668 is the date of the war's start, pointing at Sparta's defeat at the First Battle of Hysiae as a possible catalyst for the uprising.\n\nKazuhiro Yamakura: Kazuhiro Yamakura (山倉 和博, born September 2, 1955) is a former Japanese professional baseball player.  He played as a catcher.  His career lasted 13 seasons, from 1978 to 1990.\n\nIndo-Pakistani War of 1971: The Indo-Pakistani War of 1971 was a military confrontation between India and Pakistan that occurred during the liberation war in East Pakistan, from 3 December 1971 to the fall of Dacca (Dhaka) on 16 December 1971.  The war began with preemptive aerial strikes on 11 Indian air stations that led to the commencement of hostilities with Pakistan and Indian entry into the war of independence in East Pakistan on the side of Bengali nationalist forces.  Lasting just 13 days, it is one of the shortest wars in history.\n\nThompson Station Bank: Thompson Station Bank is a property in Thompsons Station, Tennessee, United States, with historical significance during period 1913-1927.  The bank opened in 1913 but only lasted 13 years, and closed in 1927.\n\nBattle of Hilli: The Battle of Hilli or the Battle of Bogra was a major battle fought in the Indo-Pakistani War of 1971 and Bangladesh Liberation War.  It is generally regarded as the most pitched battle that took place in East Pakistan, now Bangladesh.  The battle of Hilli took place between 23 November 1971 and 11 December 1971, although the final surrender took place on 18 December 1971.\n\nNemontemi: In the Aztec culture, the Nahuatl word nemontemi refers to a period of five intercalary days inserted between years of the Aztec calendar.  Each of the 18 Aztec \"months\" had 20 days, for a total of 360 days.  The nemontemi accounted for the remaining 5 days of the approximate tropical year.  According to the research by R. C. Tunnicliffe, the Aztecs dealt with the remaining fractional-day discrepancy with the true tropical year length by adding a \"trecena\" (13 days) after each bundle of 52 years; these 13 days were not considered unlucky, but they were not characterized by the features (numbers and symbols) of the Aztec calendar.\n\nRakesh Saxena: Rakesh Saxena (born 13 July 1952, at Indore, Madhya Pradesh, India) is an Indian financier and trader in the derivatives market.  On 29 October 2009, he was deported to Thailand after fighting the longest extradition battle in Canadian history, which lasted 13 years.  He is accused of embezzlement in 1994-1995.  He is widely reputed to have been engaged in dozens of high risk ventures and deals throughout the world over the previous three decades.  In June 2012 Saxena was jailed for 10 years by Bangkok South Criminal Court, and ordered to pay US$41 million in fines and compensation, after being convicted five counts of securities fraud between 1992 and 1995.\n\nTecumseh's War: Tecumseh's War or Tecumseh's Rebellion was a conflict between the United States Army and an American Indian confederacy led by the Shawnee leader Tecumseh in the Indiana Territory.  Although the war is often considered to have climaxed with William Henry Harrison's victory at the Battle of Tippecanoe in 1811, Tecumseh's War essentially continued into the War of 1812, and is frequently considered a part of that larger struggle.  The war lasted for two more years, until the fall of 1813, when Tecumseh, as well as second-in-command Roundhead died fighting Harrison's Army of the Northwest at the Battle of the Thames in Upper Canada, near present-day Chatham, Ontario, and his confederacy disintegrated.  Tecumseh's War is viewed by some academic historians as being the final conflict of a longer term military struggle for control of the Great Lakes region of North America, encompassing a number of wars over several generations, referred to as the Sixty Years' War.\n\nAnglo-Powhatan Wars: The Anglo-Powhatan Wars were three wars fought between English settlers of the Virginia Colony, and Indians of the Powhatan Confederacy in the early seventeenth century.  The First War started in 1610, and ended in a peace settlement in 1614.  Another war between the two powers lasted from 1622 to 1626.  The third war lasted from 1644 until 1646, and ended when Opechancanough was captured and killed.  That war resulted in a boundary being defined between the Indians and English lands that could only be crossed for official business with a special pass.  This situation would last until 1677 and the Treaty of Middle Plantation, which established Indian reservations following Bacon's Rebellion.\n\nQuestion: Which war lasted 13 days and contained the Battle of Hilli?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"war_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the war.\"\n    },\n    \"duration_days\": {\n      \"type\": \"integer\",\n      \"description\": \"The total duration of the war in days.\"\n    },\n    \"start_date\": {\n      \"type\": \"string\",\n      \"description\": \"The start date of the war.\"\n    },\n    \"end_date\": {\n      \"type\": \"string\",\n      \"description\": \"The end date of the war.\"\n    },\n    \"involved_parties\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"The main entities or countries involved in the war.\"\n    },\n    \"contained_battles\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of significant battles that occurred during this war.\"\n    }\n  },\n  \"required\": [\n    \"war_name\",\n    \"duration_days\",\n    \"start_date\",\n    \"end_date\",\n    \"involved_parties\",\n    \"contained_battles\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "war_name": {
        "type": "string",
        "description": "The name of the war."
      },
      "duration_days": {
        "type": "integer",
        "description": "The total duration of the war in days."
      },
      "start_date": {
        "type": "string",
        "description": "The start date of the war."
      },
      "end_date": {
        "type": "string",
        "description": "The end date of the war."
      },
      "involved_parties": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "The main entities or countries involved in the war."
      },
      "contained_battles": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of significant battles that occurred during this war."
      }
    },
    "required": [
      "war_name",
      "duration_days",
      "start_date",
      "end_date",
      "involved_parties",
      "contained_battles"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
