{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nNarendra Modi: Narendra Damodardas Modi (] , born 17 September 1950) is an Indian politician who is the 14th and current Prime Minister of India, in office since May 2014.  He was the Chief Minister of Gujarat from 2001 to 2014, and is the Member of Parliament for Varanasi.  Modi, a member of the Bharatiya Janata Party (BJP), is a Hindu nationalist and member of the right-wing Rashtriya Swayamsevak Sangh (RSS).\n\nAli Babacan: Ali Babacan (] ; born 4 April 1967 in Ankara, Turkey) is a Turkish politician.  He is member of the parliament and former Deputy Prime Minister of Turkey responsible for the Economy.  He fırst served as the Minister of State in charge of economic affairs in the 58th cabinet from the Justice and Development Party (AK Party).  He retained this position throughout the 58th and 59th Governments of the Republic of Turkey.  On August 29, 2007, he was appointed as the Minister of Foreign Affairs of the 60th Government of the Republic of Turkey.  During 2009-2015 he served as the Deputy Prime Minister for Economic and Financial Affairs of Turkey.  He is married with three children.\n\nJawad Anani: Jawad Anani (born 1943) is a Jordanian economist and politician.  After working for the Central Bank of Jordan in the 1960s and 1970s he held high ranking positions in the civil service.  He has held several ministerial posts since 1979, including a four-year stint as Minister of Labour between 1980 and 1984.  During the early 1990s he held positions as Minister of State for Cabinet Affairs and Minister of Information, and was involved in the peace-process between Jordan and Israel.  During the later half of the decade he was Deputy Prime Minister for Development Affairs, Foreign Minister and Chief of the Royal Court.  From June 2016 until January 2017 he was Deputy Prime Minister for Economic Affairs in the cabinets of Hani Al-Mulki.\n\nElyor Ganiyev: Elyor Majidovich G‘aniyev, whose name is also transliterted as Elyar Ganiyev and Elyer Ganiev (born January 7, 1960), has served as the Minister of Foreign Economic Affairs, Investments and Trade in the Government of Uzbekistan since July 2006.  He served as Minister of Foreign Affairs of Uzbekistan and Deputy head of the cabinet from February 4, 2005 to July 12, 2006.  Uzbek President Islam Karimov appointed and removed G‘aniev from that position.  He had previously served as Deputy Prime Minister and head of the Uzbek foreign economic relations agency.\n\nSwedish governmental line of succession: The Swedish constitution of 1974 allows the Prime Minister of Sweden to appoint one of the Ministers in the cabinet as Deputy Prime Minister (\"biträdande statsminister\", also unofficially known as \"vice statsminister\", \"Vice Prime Minister\"), in case the Prime Minister for some reason is prevented from performing his or her duties.  However, if a Deputy Prime Minister has not been appointed, the Minister in the cabinet who has served the longest time (and if there are several with equal experience the one who is oldest) takes over as head of government.  Note that the person acting as Prime Minister does not do so on a permanent basis: if a Prime Minister dies, resigns or loses a vote of confidence in the Riksdag, the Speaker of the Riksdag will then confer with the parties of the Riksdag and propose a new Prime Minister, who must be tolerated by a majority of the Riksdag.  If the Prime Minister has resigned or lost a vote of confidence, he or she will remain the head of a government \"ad interim\" until the new Prime Minister assumes his or her office.  The only case where the governmental line of succession becomes relevant is when the Prime Minister dies (upon which the person next in the line of succession serves as the head of a government \"ad interim\") or when the Prime Minister is on leave or for any other reason incapable of serving, but still remains in office.  This might be compared to the Presidential line of succession in the United States, where the person next in line assumes the Presidency throughout the remainder of the term if the President dies, resigns or is impeached.\n\nAbdou Kolley: Abdou Kolley (born 1 January 1970) is a Gambian economist and politician who was Gambian Minister of Finance and Economic Affairs.  He has held several roles in the Cabinet of the Gambia, having previously served as Minister of Finance and Economic Affairs and Minister of Trade, Industry, Regional Integration and Employment several times, as well as Minister of Fisheries and Water Resources.\n\nCabinet Committee on National Security (Pakistan): The Cabinet Committee on National Security (CCNS or CNS), previously known as the Defence Committee of Cabinet, is the principle federal institution and consultative forum used by the people-elected Prime Minister of Pakistan for concerning matters of state's national security, geopolitical, geostrategic, and foreign policy matters with the Prime minister's chief military advisers, senior government advisers and senior Cabinet ministers.\n\nSecretary of State for Economic Affairs: The Secretary of State for Economic Affairs was briefly an office of Her Majesty's government in the United Kingdom.  It was established by Harold Wilson in October 1964.  Wilson had been impressed by the six-weeks experiment of a Minister for Economic Affairs in 1947, an office occupied by Stafford Cripps before he was appointed Chancellor of the Exchequer.  The office was revived for eight months in 1950 and held by Hugh Gaitskell and, after Conservative victory in 1951 election, Churchill also appointed a Minister of Economic Affairs, Arthur Salter, in the period 1951–52.\n\nPradhan Mantri Krishi Sinchai Yojana: Pradhan Mantri Krishi Sinchai Yojana (PMKSY)(Hindi: प्रधानमंत्री कृषि सिंचाई योजना ) is a national mission to improve farm productivity and ensure better utilization of the resources in the country.  The budget of () in a time span of five years has been allocated to this scheme.  The decision was taken on 1 July 2015 at the meeting of Cabinet Committee on Economic Affairs (CCEA), which in turn was headed by the Prime Minister, Narendra Modi.\n\nAbdulkarim Al-Arhabi: Abdulkarim Ismail Al-Arhabi (Arabic: عبدالكريم اسماعيل الارحبي‎ ‎ ) was the Deputy Prime Minister for Economic Affairs and Minister of Planning and International Cooperation in the Republic of Yemen.  He was also the Managing Director of the Social Fund for Development, which was established in 1997.  Al-Arhabi held the post of Minister of Social Affairs and Labor from 2001 to 2006, when he was appointed Deputy Prime Minister for Economic Affairs and Minister of Planning and International Cooperation.  On April 30, 2010, the World Bank awarded Al-Arhabi the Jit Gill Memorial Award for Outstanding Public Service for being \"a key champion in the battle to reduce poverty, improve governance and broaden economic growth for Yemen.\"  \n\nQuestion: This current prime minister of India was also the head of the meeting of Cabinet Committee on Economic Affairs?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"prime_minister\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the Prime Minister.\"\n        },\n        \"country\": {\n          \"type\": \"string\",\n          \"description\": \"The country the Prime Minister serves.\"\n        },\n        \"is_current\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the person is the current Prime Minister.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"country\",\n        \"is_current\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"committee_headed\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the committee headed by the Prime Minister.\"\n        },\n        \"meeting_date\": {\n          \"type\": \"string\",\n          \"description\": \"The date of the committee meeting.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"meeting_date\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"answer\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the Prime Minister who meets the criteria.\"\n    }\n  },\n  \"required\": [\n    \"prime_minister\",\n    \"committee_headed\",\n    \"answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "prime_minister": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the Prime Minister."
          },
          "country": {
            "type": "string",
            "description": "The country the Prime Minister serves."
          },
          "is_current": {
            "type": "boolean",
            "description": "Indicates if the person is the current Prime Minister."
          }
        },
        "required": [
          "name",
          "country",
          "is_current"
        ],
        "additionalProperties": false
      },
      "committee_headed": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the committee headed by the Prime Minister."
          },
          "meeting_date": {
            "type": "string",
            "description": "The date of the committee meeting."
          }
        },
        "required": [
          "name",
          "meeting_date"
        ],
        "additionalProperties": false
      },
      "answer": {
        "type": "string",
        "description": "The name of the Prime Minister who meets the criteria."
      }
    },
    "required": [
      "prime_minister",
      "committee_headed",
      "answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
