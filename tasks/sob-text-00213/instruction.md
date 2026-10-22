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
Water Forest (Xinghua): The Water Forest (Chinese name:兴化李中水上森林) is a park in the north-west part of the city of Xinghua, in Jiangsu Province, eastern China.

Hou Yifan: Hou Yifan ( ) (born 27 February 1994, Xinghua, Jiangsu, China) is a Chinese chess grandmaster and former chess prodigy.  She has been the Women's World Chess Champion three times, the youngest ever to win the title, as well as the youngest female player ever to qualify for the title of Grandmaster.

Xinduo: Xinduo (Chinese:新垛) is a township-level division in Xinghua, Jiangsu, China.

Dashiqiao: Dashiqiao () is a city in south-central Liaoning province of Northeast China.  It is under the administration of Yingkou City, which is 23 km to the west.

Xinghua, Jiangsu: Xinghua () is a county-level city under the administration of Taizhou, Jiangsu province, China.  It is located in the central part of Jiangsu Province.  It borders the prefecture-level cities of Yancheng to the north and east and Yangzhou to the west.

Xinghua High School: Xinghua High School (兴化中学) was founded in 1926 and its original name was “Xinghua County Junior High School (兴化县立初级中学)".  The school is located in the original site of Wenzheng College (文正学院).  The school had employed well-trained teachers to teach student, which made it become well known as the Kuan Xing Wui (群英会).  After the Anti-Japanese War, the school moved to a temple in Xinghua city.  After the New China was founded in 1952, the Jiangsu Civil Administration decided to name the school Jiangsu Xinghua School (苏北兴化中学).  In 1953, it was renamed Xinghua High School, Jiangsu Province and became one of the provincial first-class high schools.  In 1980, the provincial government claimed the school as a member of the province's first government run schools.  In 1994, it was accepted as one of the provincial key high schools.  In 2004, Jiangsu Province, it received the first four-star high school acceptance in Jiangsu province.

Chushui Experimental School: Chushui Experimental School (楚水实验学校）is located in xinghua, Jiangsu province.  It is an education modernization project demonstration and a four star high and junior school.  It's surrounded by the ancient zhaoyang city and the CangLang River with an area of more than 250 acres (more than 170,000 square meters).  The school was established in 2000 with the development idea "high school building, high grade school, high efficiency management, high quality education".  With 100 classes and 340 full-time teachers the school has 7,000 students on roll.

Niu Jingyi: Niu Jingyi (钮经义, 1920–1995) was a Chinese biochemist.  He was born on December 26, 1920 in Xinghua, Jiangsu.  In 1942, he graduated from the chemistry department of the National Southwestern Associated University.  He served as an instructor of Tsinghua University from 1946 to 1948.  In 1948, he went to United States to study biochemistry at the University of Texas, five years later commenced doctor degree.  In 1956, he came back to China.

Dainan: Dainan () is a town under the administration of Xinghua City in east-central Jiangsu province, China.  It has 4 residential communities (居委会) and 33 villages under its administration.  The town is located in the southeast of Xinghua City, bordering Dongtai to the east and Jiangyan to the south, and has a population of 93,000 living in an area of 108 km2 .  Part of that area is known as the "cradle of stainless steel" (中国不锈钢之乡) production, and this economic activity gives rise to the nickname "No. 1 Town of Central Jiangsu" (苏中第一镇).

Hechen: Hechen () is a town located in the east of Xinghua City in east-central Jiangsu province.  The area has approximately 60,000 inhabitants spread over 16,200 households.  The town is an old revolutionary base, and was the location of many well-known battles.  The flat terrain, fertile soil, spaced water network, superior ecological environment and rich natural resources have made the town relatively prosperous.

Question: Are the cities of Dashiqiao and Xinghua, Jiangsu in the same country?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "city_1_name": {
      "type": "string",
      "description": "The name of the first city mentioned in the question."
    },
    "city_1_country": {
      "type": "string",
      "description": "The country where the first city is located."
    },
    "city_2_name": {
      "type": "string",
      "description": "The name of the second city mentioned in the question."
    },
    "city_2_country": {
      "type": "string",
      "description": "The country where the second city is located."
    },
    "are_in_same_country": {
      "type": "boolean",
      "description": "True if both cities are in the same country, false otherwise."
    }
  },
  "required": [
    "city_1_name",
    "city_1_country",
    "city_2_name",
    "city_2_country",
    "are_in_same_country"
  ],
  "additionalProperties": false
}
