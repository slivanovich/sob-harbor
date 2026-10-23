{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nStar Sports Network: Star Sports Network (previously known as ESPN STAR Sports or ESS) is a leading sports broadcasting network in India,owned by 21st Century Fox through its subsidiaries STAR TV and Fox Networks Group.  It was formed as ESPN STAR Sports, a joint venture between ESPN Inc. (jointly owned by The Walt Disney Company and Hearst Corporation, and through ESPN International, which it directly owns,) and News Corporation in 1994.  News Corporation acquired Disney's stake in the company in 2012 and Manu Sawhney was replaced by Peter Hutton as the CEO.\n\nWIYY: WIYY (97.9 FM, \"98 Rock\") is a commercial FM radio station licensed to serve Baltimore, Maryland.  The station is owned by the Hearst Corporation and broadcasts a mainstream rock format.  WIYY shares a studio/office facility with sister stations WBAL (1090 AM) and WBAL-TV (channel 11) on Television Hill in the Woodberry section of Baltimore, near the transmission tower it shares with WBAL-TV.  WIYY and WBAL are the only two radio stations owned by the Hearst Corporation.\n\nFashion One: Fashion One is a global television network founded by Michael Gleissner and owned by the New York-based entertainment company, Bigfoot Entertainment.  Launched on April 8, 2010, the TV network broadcasts programming related to fashion, entertainment and lifestyle internationally across multiple platforms, including direct-to-home satellite television, cable television, internet television and IPTV.\n\nPhoebe Hearst Cooke: Phoebe Millicent Hearst Cooke (July 13, 1927 – November 18, 2012) was an American businesswoman and philanthropist.  She served on the board of directors of the Hearst Corporation from 1962 to 1998.  She was a granddaughter of William Randolph Hearst.  Her twin brother was former Hearst Corporation chairman George Randolph Hearst, Jr., who died in June 2012.\n\nAsian Television Content Corporation: Asian Television Content Corporation (ATC) is a Filipino TV broadcast programming content provider and the major blocktimer of the Intercontinental Broadcasting Corporation, a government-sequestred TV network founded in 1960.  Its offices located at the # 85 Dona Justina St. Cor.  Dalton St. Filinvest II, Brgy.  Batasan Hills, Quezon City.\n\nVision TV Network: Vision TV Network is a TV network owned by Vision247 in the United Kingdom that allows access to a network of foreign TV channels from within the UK.  Viewers have to subscribe online in order to watch the pay TV channels on Vision TV Network, which are delivered to Roku, Samsung, IOS and Android Apps.  As an IPTV service, Vision TV Network also allows two-way interactivity to enable functionality such as voting, commerce and targeted advertising.  The service initially broadcast French, Greek, Polish and Turkish channels.\n\nRaymond E. Joslin: Raymond E. Joslin (c. 1936 – August 2, 2013) was an American businessman and cable executive.  Joslin served as Group Head of Hearst Entertainment & Syndication of The Hearst Corporation since 1989 and served as its President.  He served as Senior Vice President of The Hearst Corporation.  He was the CEO of CAD Sciences LLC.  Joslin attended Trinity College and is a member of the cable hall of fame.\n\nWMOR-TV: WMOR-TV, virtual channel 32 (UHF digital channel 19), is an independent television station serving Tampa and St. Petersburg, Florida, United States that is licensed to Lakeland.  Owned by the Hearst Television subsidiary of the Hearst Corporation, WMOR maintains studio facilities located on Hillsborough Avenue in east Tampa, with its transmitter located in Riverview.  Master control and some internal operations are based at the studios of Orlando NBC affiliate WESH on North Wymore Road in Winter Park.  WMOR is the only television station owned by Hearst that is not affiliated with any major broadcast network, as well as the only Hearst station that does not maintain a news department.\n\nAlpha Repertory Television Service: The Alpha Repertory Television Service (ARTS) is a defunct American cable television network that was owned by Hearst/ABC Video Services, a joint venture between the Hearst Corporation and the American Broadcasting Company (ABC).  The network, which operated nightly on the channel space of Nickelodeon, focused mainly on fine arts programming.  It merged with The Entertainment Channel in 1984 to become the Arts and Entertainment Network (A&E).\n\nA&amp;E (TV channel): A&E (previously Arts & Entertainment Network) is an American digital cable and satellite television network that serves as the flagship television property of A&E Networks, a joint venture between the Hearst Corporation and Disney–ABC Television Group subsidiary of the Walt Disney Company (both of which maintain a 50% ownership interest).\n\nQuestion: What TV network founded in 1984 is co owned by the Hearst Corporation and Disney?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"network_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the television network.\"\n    },\n    \"founding_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the network was founded or established in its current form.\"\n    },\n    \"ownership_structure\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of ownership arrangement (e.g., joint venture).\"\n        },\n        \"owners\": {\n          \"type\": \"array\",\n          \"description\": \"A list of entities that co-own the network.\",\n          \"items\": {\n            \"type\": \"object\",\n            \"properties\": {\n              \"name\": {\n                \"type\": \"string\",\n                \"description\": \"The name of the owning entity.\"\n              },\n              \"stake_percentage\": {\n                \"type\": \"string\",\n                \"description\": \"The percentage of ownership stake held by the entity.\"\n              }\n            },\n            \"required\": [\n              \"name\",\n              \"stake_percentage\"\n            ],\n            \"additionalProperties\": false\n          }\n        }\n      },\n      \"required\": [\n        \"type\",\n        \"owners\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"network_name\",\n    \"founding_year\",\n    \"ownership_structure\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "network_name": {
        "type": "string",
        "description": "The name of the television network."
      },
      "founding_year": {
        "type": "integer",
        "description": "The year the network was founded or established in its current form."
      },
      "ownership_structure": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "description": "The type of ownership arrangement (e.g., joint venture)."
          },
          "owners": {
            "type": "array",
            "description": "A list of entities that co-own the network.",
            "items": {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string",
                  "description": "The name of the owning entity."
                },
                "stake_percentage": {
                  "type": "string",
                  "description": "The percentage of ownership stake held by the entity."
                }
              },
              "required": [
                "name",
                "stake_percentage"
              ],
              "additionalProperties": false
            }
          }
        },
        "required": [
          "type",
          "owners"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "network_name",
      "founding_year",
      "ownership_structure"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
