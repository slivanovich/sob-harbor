{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCorrective Movement (Syria): The Corrective Movement (الحركة التصحيحية), also referred to as the Corrective Revolution, was a political movement in Syria, initiated by a coup d'état, led by General Hafez al-Assad on 13 November 1970.  Al-Assad's program of reform, considered revolutionary in Syria, aimed to sustain and improve the \"nationalist socialist line\" of the state and the Ba'ath party.  Al-Assad would rule Syria until his death in 2000, after which he was succeeded by his son Bashar al-Assad.\n\nCorrective Revolution: Corrective Revolution (Arabic: الثورة التصحيحية‎ ‎ ), or alternately \"Corrective Movement\" (in Syria's case) and the \"Corrective Step\" (in South Yemen's case), may refer to:\n\nBashar al-Assad: Bashar Hafez al-Assad (Arabic: بشار حافظ الأسد‎ ‎ \"Baššār Ḥāfiẓ al-ʾAsad \", ] ;    ; born 11 September 1965) is the 19th and current President of Syria, holding the office since 17 July 2000.  He is also commander-in-chief of the Syrian Armed Forces, General Secretary of the ruling Arab Socialist Ba'ath Party and Regional Secretary of the party's branch in Syria.  He is a son of Hafez al-Assad, who was President of Syria from 1971 to 2000.\n\nHafez al-Assad: Hafez al-Assad (Arabic: حافظ الأسد‎ ‎ \"Ḥāfiẓ al-ʾAsad \", ] ] ; 6 October 1930 – 10 June 2000) was a Syrian statesman, politician, and general who was President of Syria from 1971 to 2000.  He was also Prime Minister from 1970 to 1971, as well as Regional Secretary of the Regional Command of the Syrian Regional Branch of the Arab Socialist Ba'ath Party and Secretary General of the National Command of the Ba'ath Party from 1970 to 2000.\n\nBassel Al-Assad International Airport: Bassel al-Assad International Airport (Arabic: مطار باسل الأسد الدولي‎ ‎ ) (IATA: LTK, ICAO: OSLK) is an airport serving Latakia, the principal port city of Syria.  The airport is named for Bassel al-Assad (1962–1994), son of the late Syrian President Hafez al-Assad and brother of the current President Bashar al-Assad.\n\nBa'ath Party (Syrian-dominated faction): The Arab Socialist Ba'ath Party (also spelled Baath, meaning \"resurrection\" or \"renaissance\"; Arabic: حزب البعث العربي الاشتراكي‎ ‎ \"Hizb Al-Ba'ath Al-'Arabi Al-Ishtiraki\"), also referred to as the pro-Syrian Ba'ath movement, is a neo-Ba'athist political party, with branches across the Arab world.  The party emerged from a split in the Ba'ath Party in February 1966.  The party leads the government in Syria.  From 1970 until 2000, the party was led by the Syrian president Hafez al-Assad.  s of 2000 , leadership has been shared between his son Bashar al-Assad (head of the Syrian regional organization) and Abdullah al-Ahmar (head of the pan-Arab national organization).  The Syrian branch of the party is the largest organisation within the Syrian-led Ba'ath Party.\n\nBushra al-Assad: Bushra al-Assad (Arabic: بشرى الأسد‎ ‎ ) (born 24 October 1960) is the first child and only daughter of Hafez al-Assad, who was the president of Syria from 1971 to 2000.  She is the sister of current Syrian President Bashar al-Assad.  She is the widow of Assef Shawqat, the deputy chief of staff of the Syrian Armed Forces and former head of the Syrian Military Intelligence, who was killed by the rebels on 18 July 2012.\n\nCorrective Revolution (Egypt): The Corrective Revolution (officially launched as the \"Corrective Movement\") was a reform program (officially just a change in policy) launched on 15 May 1971 by President Anwar Sadat.  It involved purging Nasserist members of the government and security forces, often considered pro-Soviet and left-wing, and drumming up popular support by presenting the takeover as a continuation of the Egyptian Revolution of 1952, while at the same time radically changing track on issues of foreign policy, economy, and ideology.  Sadat's Corrective Revolution also included the imprisonment of other political forces in Egypt, including liberals, and Islamists.\n\nBassel al-Assad: Bassel al-Assad (Arabic: باسل الأسد \"Bāssel al Assad\"; 23 March 1962 – 21 January 1994) was a Syrian engineer, colonel, and politician who was the eldest son of President of Syria Hafez al-Assad and the older brother of (later) President Bashar al-Assad.  It was widely expected that he would succeed his father as President of Syria until he died in a car accident in 1994.\n\nAnisa Makhlouf: Anisa (or Aniseh) Makhlouf (1929/1930 – 6 February 2016) was the Syrian matriarch of the Al-Assad family, which has ruled the country since 1971.  The wife of the late President Hafez al-Assad, Makhlouf held the position of First Lady of Syria from 1971 until 2000.  Her five children include Bashar al-Assad, the President of Syria since 2000.\n\nQuestion: The Corrective Movement, also referred to as the Corrective Revolution, was a political movement in Syria, initiated by a coup d'état, led by General Hafez al-Assad, on which date, he was a Syrian statesman, politician, and general who was President of Syria from 1971 to 2000?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"event_name\": {\n      \"type\": \"string\",\n      \"description\": \"The primary name of the political movement.\"\n    },\n    \"alternative_event_name\": {\n      \"type\": \"string\",\n      \"description\": \"An alternative name for the political movement.\"\n    },\n    \"event_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of event that initiated the movement.\"\n    },\n    \"event_country\": {\n      \"type\": \"string\",\n      \"description\": \"The country where the event took place.\"\n    },\n    \"leader\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the leader of the movement.\"\n        },\n        \"title_at_event\": {\n          \"type\": \"string\",\n          \"description\": \"The title or rank of the leader at the time of the event.\"\n        },\n        \"presidency_start_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the leader began his presidency in Syria.\"\n        },\n        \"presidency_end_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the leader's presidency in Syria ended.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"title_at_event\",\n        \"presidency_start_year\",\n        \"presidency_end_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"event_date\": {\n      \"type\": \"string\",\n      \"description\": \"The specific date when the movement was initiated.\"\n    }\n  },\n  \"required\": [\n    \"event_name\",\n    \"alternative_event_name\",\n    \"event_type\",\n    \"event_country\",\n    \"leader\",\n    \"event_date\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "event_name": {
        "type": "string",
        "description": "The primary name of the political movement."
      },
      "alternative_event_name": {
        "type": "string",
        "description": "An alternative name for the political movement."
      },
      "event_type": {
        "type": "string",
        "description": "The type of event that initiated the movement."
      },
      "event_country": {
        "type": "string",
        "description": "The country where the event took place."
      },
      "leader": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the leader of the movement."
          },
          "title_at_event": {
            "type": "string",
            "description": "The title or rank of the leader at the time of the event."
          },
          "presidency_start_year": {
            "type": "integer",
            "description": "The year the leader began his presidency in Syria."
          },
          "presidency_end_year": {
            "type": "integer",
            "description": "The year the leader's presidency in Syria ended."
          }
        },
        "required": [
          "name",
          "title_at_event",
          "presidency_start_year",
          "presidency_end_year"
        ],
        "additionalProperties": false
      },
      "event_date": {
        "type": "string",
        "description": "The specific date when the movement was initiated."
      }
    },
    "required": [
      "event_name",
      "alternative_event_name",
      "event_type",
      "event_country",
      "leader",
      "event_date"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
