{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\n1997 Thredbo landslide: The Thredbo landslide was a catastrophic landslide that occurred at the village and ski resort of Thredbo, New South Wales, Australia, on 30 July 1997.  Two ski lodges were destroyed and a total of 18 died.\n\nMarie Ficarra: Marie Ann Ficarra (born 25 March 1954) is an Australian politician who was a Liberal Party of Australia member of the New South Wales Legislative Council from 2007 to 2015.  She was previously a member of the New South Wales Legislative Assembly for Georges River, but was defeated during the landslide election of 1999.  She was the Shadow Minister for the Environment for the New South Wales Opposition.\n\nCharles Winning: Charles Samuel Winning (17 July 1889 – 20 April 1967) was an Australian cricketer active from 1914 to 1920 who played for New South Wales and the Australian Imperial Force Touring XI.  He was born in Paddington, New South Wales and died in Newport, New South Wales.  He appeared in 28 first-class matches as a right-handed batsman who bowled right arm medium pace.  He scored 253 runs with a highest score of 30 and took 67 wickets with a best performance of six for 30.  Although he played for New South Wales at junior level before the First World War, he never took part in the Sheffield Shield and all his first-class appearances were for the Australian Imperial Force (AIF) Touring XI.  He retired after the AIF team disbanded.\n\nColony of New South Wales: The colony of New South Wales was a colony of the British Empire from 1788 to 1901, when it became a State in the federal Commonwealth of Australia on 1 January 1901.  At its greatest extent, the colony of New South Wales included the present-day Australian states of New South Wales, Queensland, Victoria, Tasmania, and South Australia, as well as New Zealand.  The first \"responsible\" self-government of New South Wales was formed on 6 June 1856 with Sir Stuart Alexander Donaldson appointed by Governor Sir William Denison as its first Colonial Secretary which in those days accounted also as the Premier.\n\nSoccer in New South Wales: Soccer in New South Wales describes the sport of soccer being played and watched by people in the state of New South Wales, Australia.  Soccer in New South Wales is organised and managed on a state level by two separate governing bodies; Football NSW and Northern New South Wales Football which are affiliated at a national level to Football Federation Australia.\n\nRoy Smith (Australian politician): Roy Anthony Smith (1953/54 – 30 July 2010) was an Australian politician, and a former manager of the New South Wales Sporting Shooters Association of Australia.  He was a member of the Shooters Party, and at the 2007 state election was elected to the New South Wales Legislative Council.  Prior to entering politics, he worked as an electrical fitter.\n\nMartin Faull: Martin Peter Faull (born 10 May 1968) is a former Australian cricketer, who regularly played for South Australia during the 1990s.  Born in Darwin, Northern Territory, Faull played cricket for South Australia at both under-16 and under-19 level, as well as for the state's Colts and Second XI sides.  Faull made his first-class debut for South Australia in February 1991 during the 1990–91 Sheffield Shield, in a match against New South Wales at the Adelaide Oval.  His first first-class half-century was made the following month, a score of 89 runs in the return match against New South Wales, batting at number three.  Faull played regularly at both Sheffield Shield and domestic one-day level throughout the rest of the decade, at first as a middle-order batsman, but later as an opening batsman, often opening alongside Greg Blewett or David Fitzgerald.  He was more successful at first-class level, with the 1996–97 season his best, where he scored 459 runs from eight matches (including six half-centuries).  Faull's only first-class century came during the 1997–98 season, a score of 103 runs in the second innings of a match against New South Wales, which followed a first innings score of 58 runs.  Overall, he played 30 first-class and nine List A matches over his career, with his final matches at both levels coming in the 1998–99 season.  In the SACA District competition, Faull played for the Tea Tree Gully District Cricket Club.\n\nStuart Diver: Stuart Diver (born 14 January 1970 in New South Wales, Australia) is a ski instructor and was the sole survivor of the 1997 Thredbo landslide.\n\nBeatrice Kerr: Beatrice Maude Williams (née Kerr; 30 November 1887 – 3 August 1971), known professionally as Beatrice Kerr, was an Australian swimmer, diver, and aquatic performer.  Born in Melbourne, Kerr learnt to swim at Albert Park Lake, and won medals at both the Victorian and Australasian championships in 1905, at the age of 17.  Early the following year, she toured South Australia and Western Australia, winning every race she entered.  From there, Kerr went to England, giving swimming exhibitions in Bradford, Liverpool, London, and Manchester, being billed as \"Australia's Champion Lady Swimmer and Diver\".  She returned to Australia in October 1911, living the rest of her life in Sydney, New South Wales.  Although often compared to Annette Kellerman, another Australian swimmer, Kerr's repeated challenges to Kellerman to race went unanswered.\n\nNew South Wales Police Force: The New South Wales Police Force (NSW Police Force; previously the New South Wales Police Service and New South Wales Police) is the primary law enforcement agency of the state of New South Wales, Australia.  It is a servant of the Crown, independent of Government, although a minister of the Crown has administration.  Divided into seventy six local area commands (LAC), the NSW Police Force consists of more than 500 local police stations and covers an area of 801,600 square kilometres in a state of some seven million people.\n\nQuestion: Which landslide killed 18 people in New South Wales, Australia, on 30 July 1997 with only Stuart Diver surviving?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"landslide_event\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the landslide event.\"\n        },\n        \"date\": {\n          \"type\": \"string\",\n          \"description\": \"The date the landslide occurred.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"date\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"location_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"village\": {\n          \"type\": \"string\",\n          \"description\": \"The village where the landslide occurred.\"\n        },\n        \"state\": {\n          \"type\": \"string\",\n          \"description\": \"The state where the landslide occurred.\"\n        },\n        \"country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the landslide occurred.\"\n        }\n      },\n      \"required\": [\n        \"village\",\n        \"state\",\n        \"country\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"impact_summary\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"fatalities_count\": {\n          \"type\": \"integer\",\n          \"description\": \"The total number of people who died in the landslide.\"\n        },\n        \"sole_survivor\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"name\": {\n              \"type\": \"string\",\n              \"description\": \"The name of the sole survivor.\"\n            }\n          },\n          \"required\": [\n            \"name\"\n          ],\n          \"additionalProperties\": false\n        }\n      },\n      \"required\": [\n        \"fatalities_count\",\n        \"sole_survivor\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"landslide_event\",\n    \"location_details\",\n    \"impact_summary\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "landslide_event": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the landslide event."
          },
          "date": {
            "type": "string",
            "description": "The date the landslide occurred."
          }
        },
        "required": [
          "name",
          "date"
        ],
        "additionalProperties": false
      },
      "location_details": {
        "type": "object",
        "properties": {
          "village": {
            "type": "string",
            "description": "The village where the landslide occurred."
          },
          "state": {
            "type": "string",
            "description": "The state where the landslide occurred."
          },
          "country": {
            "type": "string",
            "description": "The country where the landslide occurred."
          }
        },
        "required": [
          "village",
          "state",
          "country"
        ],
        "additionalProperties": false
      },
      "impact_summary": {
        "type": "object",
        "properties": {
          "fatalities_count": {
            "type": "integer",
            "description": "The total number of people who died in the landslide."
          },
          "sole_survivor": {
            "type": "object",
            "properties": {
              "name": {
                "type": "string",
                "description": "The name of the sole survivor."
              }
            },
            "required": [
              "name"
            ],
            "additionalProperties": false
          }
        },
        "required": [
          "fatalities_count",
          "sole_survivor"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "landslide_event",
      "location_details",
      "impact_summary"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
