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
Zhang Boxing: Zhang Boxing (; born August 1930) is a retired Chinese politician.  He was born in Bazhou City, Hebei.  He received his university education in Xi'an.  He was governor (1986–1987), Communist Party of China Committee Secretary (1987–1994) and People's Congress Chairman (1993–1998) of Shaanxi.  He was a delegate to the 8th National People's Congress.

Bà Prefecture: Bazhou or Ba Prefecture (霸州) was a "zhou" (prefecture) in imperial China in modern Bazhou City, Hebei, China.  It existed (intermittently) from 959 to 1913.

Bazhou City: Bazhou () is a county-level city in Hebei province, China.  It is under the jurisdiction of Langfang prefecture-level city.  As of 2002, it had a population of over 132,000.

Chengbei Subdistrict, Linxia City: Chengbei Subdistrict () is a subdistrict in the heart of Linxia City, Gansu, People's Republic of China.  , it has six residential communities (居委会) under its administration.

Tao River: Tao River () is a right tributary of China's Yellow River.  It starts in Xiqing Mountains (西倾山) near the Gansu–Qinghai border, flows eastward across Gannan Tibetan Autonomous Prefecture, and then northward more or less along the border between Dingxi Prefecture-level City in the east and Gannan and Linxia Prefectures in the west.  It flows into the Yellow River (actually, the Liujiaxia Reservoir) near Liujiaxia Town (the county seat of Yongjing County), just upstream of Liujiaxia Dam.

Sanhe, Hezheng County: Sanhe () is a town of Hezheng County in south-central Gansu province, China, located immediately north of the county seat and 20 km southeast of Linxia City.  , it has seven villages under its administration.

Yongjing County: Yongjing (, Xiao'erjing: ﻳْﻮ دٍ ﺷِﯿًﺎْ ) is a county in Linxia Hui Autonomous Prefecture in China's Gansu Province.  The county seat, the town ("zhen") of Liujiaxia (), is located about 80 km south-west from the provincial capital city, Lanzhou.  As is the case with most Chinese county seats, Liujiaxia Town is labeled on most less-detailed maps simply as "Yongjing" or "Yongjing County".

Linxia City: Linxia City (), once known as Hezhou (), is a county-level city in the province of Gansu of the People's Republic of China, and the capital of the multi-ethnic Linxia Hui Autonomous Prefecture.  It is located in the valley of the Daxia River (a right tributary of the Yellow River), 150 km (by road) southwest of the provincial capital Lanzhou.

Laohua Mosque: The Laohua Mosque () is a mosque in Linxia City, Linxia Hui Autonomous Prefecture, Gansu Province, China.

Huasi Mosque: The Huasi Mosque () is a mosque in China built during the reign of the Chenghua Emperor (r. 1465–1487) in the Ming dynasty.  Buddhist temples and imperial palaces were the architecture on which the construction for the mosque was based.  It was constructed by Muslims living in West Phoenix Wood Town, now the Bafang areas of Linxia City, Gansu.  Ma Zhongying's 1928 revolt in the Muslim conflict in Gansu (1927–30) led to a blaze that destroyed the building.  It was capable of holding 2,000 people being 5 mu in area after reconstruction of the Mosque in 1941.

Question: Are Linxia City and Bazhou City bouth country-level cities?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "is_both_county_level_cities": {
      "type": "boolean",
      "description": "True if both cities are county-level cities, false otherwise."
    },
    "cities_information": {
      "type": "array",
      "description": "Details about each city mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "city_name": {
            "type": "string",
            "description": "The name of the city."
          },
          "is_county_level": {
            "type": "boolean",
            "description": "Indicates if the city is a county-level city."
          },
          "administrative_level_description": {
            "type": "string",
            "description": "The specific administrative level description from the context."
          },
          "province": {
            "type": "string",
            "description": "The province the city is located in."
          }
        },
        "required": [
          "city_name",
          "is_county_level",
          "administrative_level_description",
          "province"
        ],
        "additionalProperties": false
      }
    },
    "conclusion_reasoning": {
      "type": "string",
      "description": "Explanation for the conclusion regarding the administrative level of both cities."
    }
  },
  "required": [
    "is_both_county_level_cities",
    "cities_information",
    "conclusion_reasoning"
  ],
  "additionalProperties": false
}
