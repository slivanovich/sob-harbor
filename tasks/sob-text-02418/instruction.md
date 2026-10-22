Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Jinhua:    , is a prefecture-level city in central Zhejiang province in eastern China.  It borders the provincial capital of Hangzhou to the northwest, Quzhou to the southwest, Lishui to the south, Taizhou to the east, and Shaoxing to the northeast.  Its population was 5,361,572 at the 2010 census including 1,077,245 in the built-up area made of two urban districts (not including the satellite city of Lanxi, which has become essentially a suburban offshoot of Jinhua's main urban area).

Lanxi, Zhejiang: Lanxi also known as Lanchi () is a county-level city under the administration of the prefecture-level city Jinhua in Zhejiang Province, China.

Huangdian, Zhejiang: Huangdian () is a town under the administration of Lanxi City in western Zhejiang province, China, located 10 km northwest of downtown Lanxi.  , it has 46 villages under its administration.

Glove puppetry: Glove puppetry () is a type of opera using cloth puppets that originated during the 17th century in Quanzhou or Zhangzhou of China's Fujian province, and historically practised in the Min Nan-speaking areas such as Quanzhou, Zhangzhou, the Chaoshan region of Guangdong, and other parts of southern China.  It had since established itself contemporarily as a popular art form in Taiwan.

Longhai City: Longhai is a county-level city within the prefecture-level city of Zhangzhou, in the south of Fujian province, People's Republic of China.  Longhai comprises territory on both banks of the lower Jiulong River, although most of its area is on the right (southern) bank.  The left bank yields to Xiamen before reaching the sea, the right bank becomes the south shore of Xiamen Bay and is home to the Zhangzhou Port tariff-free industrial export zone, in Longhai's Gangwei Town.

Zhejiang Television: Zhejiang Television (ZJTV, ), is a television channel under Zhejiang Radio and Television Group serving the Hangzhou city and Zhejiang province area.  Zhejiang TV, Zhejiang radio and Television Group satellite channel, Taiwan and Taiwan nickname blueberry blue whale, is Zhejiang radio and television group integrated satellite television channel, launched in October 1, 1960, January 1, 1994 for the national broadcast.

Zhangzhou dialect: Zhangzhou dialect (), also known as Changchew dialect or Changchow dialect, is a dialect of Hokkien originating from southern Fujian province (in southeast China), centered on the city of Zhangzhou.  The Zhangzhou dialect has an intelligibility of over 90% with other dialects of Hokkien such as Amoy and Quanzhou.  The Zhangzhou dialect is often simply called Hokkien or Minnan.  It is the source of some former place names in English, including Amoy (/ɛ˨˩ mui˩˧/ ) and Quemoy (/kim˨˨ mui˩˧/ ).

Zhangzhou: Zhangzhou, formerly romanized as Changchow, is a prefecture-level city in Fujian Province, China.  The prefecture around the city proper comprises the southeast corner of the province, facing the Taiwan Strait and surrounding the prefecture of Xiamen.  During the 2010 census, the entire area of Zhangzhou was home to 4,809,983 inhabitants.  Along with the 1.9m people of central Xiamen, its urban districts of Longwen and Xiangcheng, together with Longhai, form a single metropolitan area of about 5 million people .

Zhangzhou Railway Station: Zhangzhou Railway Station is the main train station of the Zhangzhou metropolitan area in China's Fujian Province.  The station is located in Hongtang Village (洪塘村) of Longhai City, about 10 km south of downtown Zhangzhou.  It is located on the common section of the Longxia Railway (Longyan-Xiamen; opened in mid-2012) and the Xiashen Railway (Xiamen-Shenzhen Railway; opened at the end of 2013).

Zhejiang University of Finance and Economics: Zhejiang University of Finance and Economics located in the city of Hangzhou, the capital of Zhejiang Province, Zhejiang University of Finance and Economics (hereinafter referred to as ZUFE) is a prestigious institution of higher education with economy-related disciplines as the key disciplines, ensuring a coordinated development of various disciplines, namely， Economics, Management, Humanities, Law, Science, Engineering and Arts.  ZUFE, founded in 1974, was formerly known as Zhejiang Academy of Public Finance and Banking, and in 1987 she was renamed as Zhejiang Institute of Finance and Economics with the approval of the former State Education Commission.  Then In 1991, the university was authorized as a bachelor's degree granting institution, in 2003 an institution granting master's degree, and in 2006, ZUFE got “Excellence” in the Undergraduate Teaching Quality Assessment initiated by Ministry of Education.  In 2012, ZUFE became an institution qualified to grant doctoral degree in “National Special Needs Services Personnel Training Project”.  In 2013, approved by the Ministry of Education, the university finally adopted the name Zhejiang University of Finance and Economics.

Question: Lanxi, Zhejiang and Zhangzhou are both what type of city?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "cities_in_question": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the city"
          },
          "administrative_type": {
            "type": "string",
            "description": "The administrative classification of the city as described in the context"
          }
        },
        "required": [
          "name",
          "administrative_type"
        ],
        "additionalProperties": false
      },
      "description": "A list of cities mentioned in the question and their administrative types"
    },
    "question_analysis": {
      "type": "object",
      "properties": {
        "question_text": {
          "type": "string",
          "description": "The original question asked"
        },
        "common_type_exists": {
          "type": "boolean",
          "description": "Indicates whether a single administrative type applies to both cities based on the context"
        },
        "reasoning": {
          "type": "string",
          "description": "Explanation for whether a common type was found or not"
        }
      },
      "required": [
        "question_text",
        "common_type_exists",
        "reasoning"
      ],
      "additionalProperties": false
    },
    "final_answer": {
      "type": "string",
      "description": "The final answer to the question, if a common type is identified"
    }
  },
  "required": [
    "cities_in_question",
    "question_analysis"
  ],
  "additionalProperties": false
}
