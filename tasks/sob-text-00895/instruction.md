{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGaya River: The Gaya River () is a tributary of the Tumen River in east Jilin province of China.  The source of river is located in Wangqing County and flows generally from north to south and joins Tumen River at Tumen City. The river has a length of 205.2 km and drains an area of 13,565 square km.\n\nLongtanshan Railway Station: Longtanshan Railway Station is a railway station of Changchun–Tumen Railway, Jilin–Shulan Railway and Longtanshan–Fengman Railway.  The station located in the Longtan District of Jilin, Jilin province, China.\n\nTumen River Bridge: The Tumen River Bridge () is a bridge over the Tumen River, connecting Hunchun City, Jilin Province, China, with Undok County, North Hamgyong Province, North Korea.  It was built in 1938 by the Japanese Empire and is 535.2 m long and 6.6 m wide.  It is located at Quanhe where the Quan River meets the Tumen River.\n\nDonggang, Liaoning: Donggang () is a city in the southeast of Liaoning Province in Northeast China.  Situated on the coast of the Yellow Sea at the mouth of the Yalu River, it is located near the maritime border with North Korea.  Administratively, it is a county-level city of Dandong, which lies 35 km to the northeast.\n\nJiangbei Railway Station: Jiangbei Railway Station is a railway station of Changchun–Tumen Railway and Jilin–Shulan Railway.  The station located in the Longtan District of Jilin, Jilin province, China.\n\nZ117/118 Beijing-Jilin Through Train: The Z117/118 Beijing-Jilin Through Train (Chinese:Z117/118次北京到吉林直达特快列车) is Chinese railway running between the capital Beijing to Jilin City express passenger trains by the Shenyang Railway Bureau, Jilin passenger segment responsible for passenger transport task, JIlin originating on the Beijing train.  25T Type Passenger trains running along the Jingha Railway and Changtu Railway across Jilin, Liaoning, Hebei, Tianjin, Beijing and other provinces and cities, the entire 1131 km.  Beijing Railway Station to Jilin Railway Station running 14 hours and 9 minutes, use trips for Z117; Jilin Railway Station to Beijing Railway Station to run 12 hours and 17 minutes, use trips for Z118.\n\nTumen Border Bridge: The Tumen Border Bridge () is a bridge over the Tumen River, connecting Tumen City, Jilin Province, China, with Onsong County (Namyang), North Hamgyong Province, North Korea.  It was built in 1941 by the Japanese and is 515 metres long, 6 metres high, 6 metres wide.  Tumen Border Post is located there.  A little upstream from the bridge is Tumen Border Railway Bridge.\n\nTumen, Jilin: Tumen is a county-level city in Yanbian Korean Autonomous Prefecture, eastern Jilin province, Northeast China.  Of its 136,000 inhabitants, approximately 78,000 (or 57%) are of Korean descent.  The two official languages are Chinese and Korean.  Tumen is separated from Namyang of North Hamgyong province of North Korea by the Tumen River.  Due to this proximity, many North Koreans escaping their country pass through Tumen.  Tumen is also the location of a large detention center for captured North Koreans awaiting deportation.  Tumen has two major food markets, the South Market and the North Market, where most of the residents purchase their food.  Packaged foods and meats are usually sold inside the building, and vegetables are sold outside.  There are six elementary schools, with three Korean schools, and three Chinese schools.\n\nD73/74 Beijing-Jilin Through Train: The D73/74 Beijing-Jilin Through Train (Chinese:D73/74次北京到吉林动车组列车) is a railway running between Beijing and Jilin City.  It carries express passenger trains for the Shenyang Railway Bureau.  The Jilin passenger segment is responsible for passenger transport.  CRH5 Type Passenger trains run along the Jingha Railway, Harbin–Dalian High-Speed Railway and Changchun–Jilin Intercity Railway across Jilin, Liaoning, Hebei, Tianjin, Beijing and other areas.  The route spans 1248 km.  Beijing Railway Station to Jilin Railway Station requires 7 hours and 5 minutes.  Jilin Railway Station to Beijing Railway Station runs 7 hours and 21 minutes.\n\nLongwangmiao, Liaoning: Longwangmiao () is a town of Donggang City in southeastern Liaoning province, China, located 39 km northwest of downtown Donggang and 20 km inland of Korea Bay.  , it has one residential community (社区) and 7 villages under its administration.\n\nQuestion: What do Donggang, Liaoning and Tumen, Jilin have in common?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"entity_1_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the first entity being compared.\"\n    },\n    \"entity_2_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the second entity being compared.\"\n    },\n    \"common_attribute\": {\n      \"type\": \"string\",\n      \"description\": \"The attribute that both entities share.\"\n    },\n    \"attribute_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of the common attribute (e.g., 'geographic_region').\"\n    }\n  },\n  \"required\": [\n    \"entity_1_name\",\n    \"entity_2_name\",\n    \"common_attribute\",\n    \"attribute_type\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "entity_1_name": {
        "type": "string",
        "description": "The name of the first entity being compared."
      },
      "entity_2_name": {
        "type": "string",
        "description": "The name of the second entity being compared."
      },
      "common_attribute": {
        "type": "string",
        "description": "The attribute that both entities share."
      },
      "attribute_type": {
        "type": "string",
        "description": "The type of the common attribute (e.g., 'geographic_region')."
      }
    },
    "required": [
      "entity_1_name",
      "entity_2_name",
      "common_attribute",
      "attribute_type"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
