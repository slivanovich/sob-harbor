{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRTCG: Radio and Television of Montenegro (Montenegrin: \"Radio i televizija Crne Gore\", Радио и телевизија Црне Горе - or RTCG, РТЦГ) is the public service broadcaster of Montenegro.  A state-owned company with its headquarters in Podgorica, it is made up of Radio Montenegro (RCG - \"Radio Crne Gore\") and Montenegro Television (TVCG - \"Televizija Crne Gore\").  In July 2001, RTCG became a joint member of the European Broadcasting Union (EBU), and became a full member of the EBU upon the declaration of Montenegrin independence in 2006.\n\nBBC: The British Broadcasting Corporation (BBC) is a British public service broadcaster with its headquarters at Broadcasting House in London.  The BBC is the world's oldest national broadcasting organisation and the largest broadcaster in the world by number of employees.  It employs over 20,950 staff in total, 16,672 of whom are in public sector broadcasting.  The total number of staff is 35,402 when part-time, flexible, and fixed contract staff are included.\n\nRobert Banks Stewart: Robert Banks Stewart (16 July 1931 – 14 January 2016) was a Scottish screenwriter, television producer and former journalist.  He was sometimes credited as Robert Stewart early in his career.  Banks Stewart contributed extensively to drama for the BBC and ITV for several decades.\n\nThomas Nilsen: Thomas Nilsen (29 August 1968) is a Norwegian journalist who has extensively covered oil drilling in the Arctic region.  He was editor of the \"BarentsObserver,\" a Norwegian Arctic online newspaper based in Kirkenes, for six years before he was sacked in 2015.  Norway’s public service broadcaster, NRK, claim Nilsen was sacked at the behest of the Russian intelligence service, the FSB.\n\nThe Daily Service: The Daily Service is a short Christian church service, often from Emmanuel Church in Didsbury, Manchester, England, broadcast every weekday morning between 9.45 and 10.00 on BBC Radio 4 (long wave and DAB).  Originally aired from Broadcasting House, the service was moved on the outbreak of war in 1939, first to Bristol and later to the Trinity Chapel of St Paul's Church, Bedford, under the musical direction of Dr George Thalben-Ball.  In 1945 the service returned to a studio in Broadcasting House.\n\nRai 1: Rai 1 (until May 2010 known as Rai Uno) is the flagship television channel of Rai, Italy's national public service broadcaster, and the most watched television channel in the country.  It is a general interest channel, mainly focused on shows, movies and public service; its direct competitor is Mediaset's Canale 5.\n\nMedia of the United Kingdom: There are several different types of media in the United Kingdom: television, radio, newspapers, magazines and websites.  The country also has a strong music industry.  The United Kingdom has a diverse range of providers, the most prominent being the publicly-owned public service broadcaster, the British Broadcasting Corporation (BBC).  The BBC's largest competitors are ITV plc, which operates 13 of the 15 regional television broadcasters that make up the ITV Network, and 21st Century Fox, which holds a large stake in the satellite broadcaster Sky plc.  Regional media is covered by local radio, television and print newspapers.  Trinity Mirror operates 240 local and regional newspapers, as well as national newspapers such as the \"Daily Mirror\" and the \"Sunday Mirror\".\n\nScottish Digital Network: The Scottish Digital Network (SDN) is a planned new public service broadcaster and online services provider in Scotland.  It was the principal proposal of the Scottish Broadcasting Commission.  The Scottish Broadcasting Commission published its final report in September 2008, with this as a its primary recommendation.  On September 13, 2010, the Minister for Culture and External Affairs, Fiona Hyslop, requested Blair Jenkins, who had been the chair of the Scottish Broadcasting Commission to actively explore proposed options and business models for the establishment of a Scottish digital network to compete in public service broadcasting with the BBC Network in Scotland.  On March 21, 2013, three bidders were announced as the finalists for the Scottish Wide Area Network (SWAN).  They were British Telecom, a partnership of Cable & Wireless Worldwide with Virgin Media Business and Capita with Updata Infrastructure.\n\nRaidió Teilifís Éireann: Raidió Teilifís Éireann (] ; \"Radio [and] Television of Ireland\"; abbreviated as RTÉ) is a semi-state company and the national public service broadcaster of the Republic of Ireland.  It both produces programmes and broadcasts them on television, radio and the Internet.  The radio service began on 1 January 1926, while regular television broadcasts began on 31 December 1961, making it one of the oldest continuously operating public service broadcasters in the world.  RTÉ also publishes a weekly lifestyle magazine called the \"RTÉ Guide\".\n\nCall Me Mister (TV series): Call Me Mister is a British television drama series, created by Robert Banks Stewart who had previously developed \"Shoestring\" and \"Bergerac\" for the BBC.  One series of ten episodes was broadcast between September and November 1986.\n\nQuestion: Scottish screenwriter, television producer and former journalist, Robert Banks Stewart, contributed extensively to drama for what British public service broadcaster with its headquarters at Broadcasting House in London?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"broadcaster\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the public service broadcaster.\"\n        },\n        \"type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of organization, e.g., 'public service broadcaster'.\"\n        },\n        \"headquarters\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"building\": {\n              \"type\": \"string\",\n              \"description\": \"The name of the headquarters building.\"\n            },\n            \"city\": {\n              \"type\": \"string\",\n              \"description\": \"The city where the headquarters is located.\"\n            },\n            \"country\": {\n              \"type\": \"string\",\n              \"description\": \"The country where the headquarters is located.\"\n            }\n          },\n          \"required\": [\n            \"building\",\n            \"city\",\n            \"country\"\n          ],\n          \"additionalProperties\": false\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"type\",\n        \"headquarters\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"contributor\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the individual who contributed.\"\n        },\n        \"nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the contributor.\"\n        },\n        \"professions\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"A list of professions held by the contributor.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"nationality\",\n        \"professions\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"contribution_area\": {\n      \"type\": \"string\",\n      \"description\": \"The area to which the individual contributed, e.g., 'drama'.\"\n    }\n  },\n  \"required\": [\n    \"broadcaster\",\n    \"contributor\",\n    \"contribution_area\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "broadcaster": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the public service broadcaster."
          },
          "type": {
            "type": "string",
            "description": "The type of organization, e.g., 'public service broadcaster'."
          },
          "headquarters": {
            "type": "object",
            "properties": {
              "building": {
                "type": "string",
                "description": "The name of the headquarters building."
              },
              "city": {
                "type": "string",
                "description": "The city where the headquarters is located."
              },
              "country": {
                "type": "string",
                "description": "The country where the headquarters is located."
              }
            },
            "required": [
              "building",
              "city",
              "country"
            ],
            "additionalProperties": false
          }
        },
        "required": [
          "name",
          "type",
          "headquarters"
        ],
        "additionalProperties": false
      },
      "contributor": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the individual who contributed."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the contributor."
          },
          "professions": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of professions held by the contributor."
          }
        },
        "required": [
          "name",
          "nationality",
          "professions"
        ],
        "additionalProperties": false
      },
      "contribution_area": {
        "type": "string",
        "description": "The area to which the individual contributed, e.g., 'drama'."
      }
    },
    "required": [
      "broadcaster",
      "contributor",
      "contribution_area"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
