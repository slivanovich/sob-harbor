{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSplendid China Folk Village: Splendid China Folk Village (Chinese: 锦绣中华民俗村, pinyin: Jǐnxiù Zhōnghuá Mínsú Cūn) is a theme park including two areas (Splendid China Miniature Park & China Folk Culture Village) located in Shenzhen, Guangdong province, People's Republic of China.  The park's theme reflects the history, culture, art, ancient architecture, customs and habits of various nationalities.  It is one of the world's largest scenery parks in the amount of scenarios reproduced.  The park is developed and managed by the major travel and tourist corporation, China Travel Service.\n\nPacific Mall: Pacific Mall is an Asian shopping centre in Markham, Ontario, Canada.  It is located on the northeast side of Steeles Avenue and Kennedy Road, right across the municipal border from the city of Toronto, on the site formerly occupied by Cullen Country Barns.  The two entrance roads of the mall are Redlea Avenue and Clayton Drive.  Pacific Mall is surrounded by an existing shopping plaza, including the Market Village, and together they encompass over 500 stores and are served by both indoor and outdoor parking areas with over 1,500 parking spaces combined.  It has two floors and an underground level that leads to an underground parking lot.  Designed by Wallman Clewes Bergman Architects, their first proposal was modified by the aesthetic expectations of Markham Town Council (now City Council).  Pacific Mall first opened its doors for business in 1997.  Its Cantonese name, \"太古廣場\" (Tai Gu Gwong Cheung), is derived from Pacific Place in Hong Kong.  The mall has a total of 270000 sqft of retail space.\n\nList of largest shopping malls: This is an incomplete list of the world's largest shopping malls based on their gross leasable area.  The Dubai Mall in Dubai, UAE is the largest mall in the world by total area.  It is the nineteenth largest shopping mall in the world by gross leasable area.  New South China Mall in Dongguan, China is the largest shopping mall in the world when measured in terms of gross leasable area, and second in terms of total area to The Dubai Mall.\n\nOverseas Chinese Town Station: OCT Station (), also referred to as Overseas Chinese Town Station in English, and formerly known as Huaqiaocheng Station, is a station on Line 1 of the Shenzhen Metro.  It opened on December 28, 2004.  It is located underground at Shennan Dadao (), near Shenzhen Bay Hotel (), in Nanshan District, Shenzhen, China.  The station is named after Overseas Chinese Town (OCT) ().  It is also located close to Splendid China () and China Folk Culture Village ().\n\nRobinsons Cabanatuan: Robinsons Townville Cabanatuan (referenced as Robinsons Cabanatuan listed on the text-only annual reports for Robinsons Land (known as SEC 17-A)) is a shopping mall located Maharlika Highway, Cabanatuan, Philippines.  The mall is owned by John Gokongwei, founder of JG Summit Holdings and Robinsons Land Co, it is the first Robinsons mall in the province.  The mall was built beside NE Pacific Mall in 2007.  The mall had its soft opening on November 2008 and its grand opening the next year.\n\nSouth China Mall: New South China Mall () in Dongguan, China is the largest shopping mall in the world when measured in terms of gross leasable area, and second in terms of total area to The Dubai Mall (which has extensive non-shopping space including a zoo, a hotel complex and a theme park).  South China Mall opened in 2005 and for more than 10 years it was mostly vacant as few merchants ever signed up, leading it to be dubbed a dead mall.  In 2015 a CNN story reported that the mall had begun to attract tenants after extensive renovations and remodeling, though large portions remained vacant.\n\nChina Folk Culture Village: The China Folk Culture Village (深圳中国民俗文化村) is a part of Splendid China Folk Village in Shenzhen, China.  It is located adjacent to the Splendid China theme park and features displays of the daily life and architecture of China's 56 ethnic groups.  It was opened to the public in October 1991.\n\nSplendid China Mall: Splendid China Mall (Traditional Chinese: 錦繡中華; Simplified Chinese: 锦绣中华) (formerly known as Splendid China Tower) is a 90000 sqft Chinese-themed ethnic shopping centre located at the southeast corner of Redlea Avenue and Steeles Avenue in the Scarborough district of Toronto, Ontario, Canada.  It is located adjacent to Milliken GO Station and across from the Pacific Mall along with the Market Village.  The structure was formerly occupied by Canadian Tire.\n\nSplendid China (Florida): Splendid China was a theme park in Four Corners, Florida near Disney World and Orlando.  It opened in 1993, and closed on December 31, 2003.  It was a sister park to Splendid China in Shenzhen, China which is still open and receives many visitors.  Florida Splendid China cost $100 million to build.\n\nYitian Holiday Plaza: Yitian Holiday Plaza () is a shopping mall in Nanshan, Shenzhen, China.  It is located within the Overseas Chinese Town (OCT) area of Shenzhen, and a walking distance from a number of theme parks such as Window of the World and Splendid China.  The mall features, amongst others, a Westin Hotel, an ice rink and the first Apple retail store in Shenzhen.\n\nQuestion: Splendid China Mall and Pacific Mall are both partially located on which street?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"shared_street_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the street that both entities are partially located on.\"\n    },\n    \"malls_on_street\": {\n      \"type\": \"array\",\n      \"description\": \"Details about the malls located on the shared street.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"mall_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the shopping mall.\"\n          },\n          \"location_description\": {\n            \"type\": \"string\",\n            \"description\": \"A detailed description of the mall's location from the context.\"\n          },\n          \"city\": {\n            \"type\": \"string\",\n            \"description\": \"The city where the mall is located.\"\n          }\n        },\n        \"required\": [\n          \"mall_name\",\n          \"location_description\",\n          \"city\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"common_geographic_area\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"province_state\": {\n          \"type\": \"string\",\n          \"description\": \"The common province or state for both locations.\"\n        },\n        \"country\": {\n          \"type\": \"string\",\n          \"description\": \"The common country for both locations.\"\n        }\n      },\n      \"required\": [\n        \"province_state\",\n        \"country\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"shared_street_name\",\n    \"malls_on_street\",\n    \"common_geographic_area\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "shared_street_name": {
        "type": "string",
        "description": "The name of the street that both entities are partially located on."
      },
      "malls_on_street": {
        "type": "array",
        "description": "Details about the malls located on the shared street.",
        "items": {
          "type": "object",
          "properties": {
            "mall_name": {
              "type": "string",
              "description": "The name of the shopping mall."
            },
            "location_description": {
              "type": "string",
              "description": "A detailed description of the mall's location from the context."
            },
            "city": {
              "type": "string",
              "description": "The city where the mall is located."
            }
          },
          "required": [
            "mall_name",
            "location_description",
            "city"
          ],
          "additionalProperties": false
        }
      },
      "common_geographic_area": {
        "type": "object",
        "properties": {
          "province_state": {
            "type": "string",
            "description": "The common province or state for both locations."
          },
          "country": {
            "type": "string",
            "description": "The common country for both locations."
          }
        },
        "required": [
          "province_state",
          "country"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "shared_street_name",
      "malls_on_street",
      "common_geographic_area"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
