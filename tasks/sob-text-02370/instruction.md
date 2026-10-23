{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nIron Beam: Iron Beam (Hebrew: קֶרֶן בַּרְזֶל‎ , \"keren barzel \") is an air defense system which as of 2016 is in post-production development and upgrades by Israeli defense contractor Rafael Advanced Defense Systems.  Unveiled at the 2014 Singapore Air Show on February 11 and expected to enter service with the Israel Defense Forces in 2015, the system is designed to destroy short-range rockets, artillery, and mortars with a range of up to 7 km , too small for the Iron Dome system to intercept effectively.  In addition, the system could also intercept unmanned aerial vehicles. Iron Beam will use a \"directed high energy laser beam\" to destroy hostile targets with ranges of up to 7 km .  Iron Beam will constitute the fifth element of Israel's integrated air defense system, in addition to Arrow 2, Arrow 3, David's Sling, and Iron Dome.  However, Iron Beam is also a stand-alone system.\n\nEG&amp;G: EG&G, formally known as Edgerton, Germeshausen, and Grier, Inc., was a United States national defense contractor and provider of management and technical services.  The company was involved in contracting services to the United States government during World War II and conducted weapons research and development during the Cold war era (since 1948 onwards.)  Its close involvement with some of the government's most sensitive technologies has led to its being cited in conspiracy theories related to Department of Defense black projects.\n\nGeneral Dynamics: General Dynamics Corporation is an American aerospace and defense multinational corporation.  Formed by mergers and divestitures, it is the world's fifth-largest defense contractor based on 2012 revenues.  General Dynamics is headquartered in West Falls Church, Fairfax County, Virginia.\n\nVPX: VPX was originally defined by American Logic Machines Inc (ALM) as a scalable backplane technology.  The VPX3264, VPX3232 bridge chips and the scalable backplane were based on VPX.  VPX technology was presented at bus&board (VITA) in 2004.  ALM continues to build custom chipsets for clients including VME-to-PCIX, VME-to-Futurebus+ and other custom scalable backplane technologies.  VPX, formerly known as VITA 46, is an ANSI standard (ANSI/VITA 46.0-2007) that provides VMEbus-based systems with support for switched fabrics over a new high speed connector.  Defined by the VITA (VME International Trade Association) working group (composed of companies such as ADLINK, Aitech, Boeing, Curtiss-Wright, Elma Electronic, Extreme Engineering (X-ES), GE Intelligent Platforms, Kontron, Mercury Computer Systems, Pentek, Cornet Technology, Inc., and Northrop Grumman), it has been designed specifically with defense applications in mind, with an enhanced module standard that enables applications and platforms with superior performance.  VPX retains VME's existing 6U and 3U Eurocard form factors, supporting existing PCI Mezzanine Card (PMC) and XMC mezzanines (PMC with high-speed serial fabric interconnect), and maintaining the maximum possible compatibility with VMEbus.\n\nCSS Working Group: The CSS Working Group (Cascading Style Sheets Working Group) is a working group created by the World Wide Web Consortium (W3C) in 1997 to tackle issues that had not been addressed with CSS level 1.  The number of members reaches 125 in April 2017.\n\nOpenVPX: OpenVPX is an Industry Working Group of 28 defense contractors.  OpenVPX was founded by Mercury Systems in January 2009.  The OpenVPX Industry Working Group has provided new standards which will replace VME and VXS standards in future defense designs.\n\nHRB Systems: HRB Systems Inc., now part of Raytheon Intelligence and Information Systems, is a defense contractor located in State College, Pennsylvania.  The company was started by three scientists: Haller, Raymond, and Brown.  Initially, the firm provided imagery support, then transitioned to signal analysis and processing.  The company was acquired by Singer, and became known as HRB-Singer, one of the firms in the Singer Defense Systems Group, dealing with infrared reconnaissance techniques and equipments.  It was physically located in east e Science Park, in State College.  The company had a strong internal R&D effort which was quite successful.  HRB-Singer provided signal processing equipment and expertise to the US Department of Defense and to international clients in Europe and Asia.  In 1988, Singer sold off the Defense unit to corporate raider Paul Bilzerian, who sold each of the companies separately.  HRB division was sold to Hadson Corporation for $137 million in cash and 2 million shares of Hadson common stock.  HRB was subsequently acquired by E-Systems, and was downsized to a considerable degree.  The company was later acquired by Raytheon.\n\nNorthrop Grumman: Northrop Grumman Corporation () is an American global aerospace and defense technology company formed by Northrop's 1994 purchase of Grumman.  The company was named as the fifth-largest defense contractor in the world in 2015.  Northrop Grumman employs over 68,000 people worldwide.  It reported revenues of $23.526 billion in 2015.  Northrop Grumman ranks No. 124 on the 2015 Fortune 500 list of America's largest corporations and ranks in the top ten military-friendly employers.  It is headquartered in West Falls Church, Virginia.\n\nWorking Group on Internet Governance: The Working Group on Internet Governance (WGIG) was a United Nations multistakeholder Working group initiated after the 2003 World Summit on the Information Society (WSIS) first phase Summit in Geneva failed to agree on the future of Internet governance.  The first phase of World Summit on the Information Society (WSIS) agreed to continue the dialogue on Internet Governance in the Declaration of Principles and Action Plan adopted on 12 December 2003, to prepare for a decision at the second phase of the WSIS in Tunis during November 2005.  In this regard, the first phase of the Summit requested the United Nations Secretary-General to establish a Working Group on Internet Governance (WGIG).\n\nUnited Defense: United Defense Industries was a United States defense contractor which is now part of BAE Systems Land and Armaments.  This company produced combat vehicles, artillery, naval guns, missile launchers and precision munitions.\n\nQuestion: What company was the fifth-largest defense contractor in the world in 2015 and is part of the VITA working group?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"company_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the defense contractor.\"\n    },\n    \"ranking_information\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year for which the ranking was determined.\"\n        },\n        \"position\": {\n          \"type\": \"integer\",\n          \"description\": \"The company's rank among defense contractors globally.\"\n        },\n        \"category\": {\n          \"type\": \"string\",\n          \"description\": \"The category of the ranking, e.g., 'defense contractor'.\"\n        },\n        \"scope\": {\n          \"type\": \"string\",\n          \"description\": \"The geographical scope of the ranking, e.g., 'world'.\"\n        }\n      },\n      \"required\": [\n        \"year\",\n        \"position\",\n        \"category\",\n        \"scope\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"working_group_memberships\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"group_name\": {\n            \"type\": \"string\",\n            \"description\": \"The acronym or common name of the working group.\"\n          },\n          \"group_full_name\": {\n            \"type\": \"string\",\n            \"description\": \"The full name of the working group.\"\n          },\n          \"group_type\": {\n            \"type\": \"string\",\n            \"description\": \"The type of the working group, e.g., 'Trade Association'.\"\n          }\n        },\n        \"required\": [\n          \"group_name\",\n          \"group_full_name\",\n          \"group_type\"\n        ],\n        \"additionalProperties\": false\n      },\n      \"description\": \"A list of working groups the company is a member of.\"\n    }\n  },\n  \"required\": [\n    \"company_name\",\n    \"ranking_information\",\n    \"working_group_memberships\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "company_name": {
        "type": "string",
        "description": "The name of the defense contractor."
      },
      "ranking_information": {
        "type": "object",
        "properties": {
          "year": {
            "type": "integer",
            "description": "The year for which the ranking was determined."
          },
          "position": {
            "type": "integer",
            "description": "The company's rank among defense contractors globally."
          },
          "category": {
            "type": "string",
            "description": "The category of the ranking, e.g., 'defense contractor'."
          },
          "scope": {
            "type": "string",
            "description": "The geographical scope of the ranking, e.g., 'world'."
          }
        },
        "required": [
          "year",
          "position",
          "category",
          "scope"
        ],
        "additionalProperties": false
      },
      "working_group_memberships": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "group_name": {
              "type": "string",
              "description": "The acronym or common name of the working group."
            },
            "group_full_name": {
              "type": "string",
              "description": "The full name of the working group."
            },
            "group_type": {
              "type": "string",
              "description": "The type of the working group, e.g., 'Trade Association'."
            }
          },
          "required": [
            "group_name",
            "group_full_name",
            "group_type"
          ],
          "additionalProperties": false
        },
        "description": "A list of working groups the company is a member of."
      }
    },
    "required": [
      "company_name",
      "ranking_information",
      "working_group_memberships"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
