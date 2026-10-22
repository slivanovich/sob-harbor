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
Guangdong: Guangdong () is a province in South China, located on the South China Sea coast.  Traditionally romanised as Canton or Kwangtung, Guangdong surpassed Henan and Sichuan to become the most populous province in China in January 2005, registering 79.1 million permanent residents and 31 million migrants who lived in the province for at least six months of the year; the total population was 104,303,132 in the 2010 census, accounting for 7.79 percent of Mainland China's population.  The provincial capital Guangzhou and economic hub Shenzhen are among the most populous and important cities in China.  The population increase since the census has been modest, the province at 2015 had 108,500,000 people.

Wugang, Henan: Wugang (Chinese: 舞钢; Pinyin: Wǔgāng) is a city in Henan province, China.  It has a population of approximately 320,000.  It is home to one of China's biggest iron and steel companies: Wuyang Iron and Steel Company Limited, Hangang Group.  Longquan Lake (Shimantan Reservoir) is located at the foot of the city with beautiful mountains surrounding it.  This place has now become a hot tourist destination to neighbouring cities and provinces.  The city region comprises three geological areas including Sipo, Yakou and Zhulan.

Henan: Henan () is a province of the People's Republic of China, located in the central part of the country.  Henan is often referred to as Zhongyuan or Zhongzhou () which literally means "central plain land" or "midland", although the name is also applied to the entirety of China proper.  Henan is the birthplace of Chinese civilization with over 3,000 years of recorded history, and remained China's cultural, economical, and political center until approximately 1,000 years ago.

Karamay: Karamay or Kelamayi is a prefecture-level city in the north of the Xinjiang Uygur Autonomous Region, People's Republic of China.  The name of the city comes from the Uyghur language, and means "black oil", referring to the oil fields near the city.

G30 Lianyungang–Khorgas Expressway: The Lianyungang–Khorgas Expressway (), commonly referred to as the "Lianhuo Expressway" (), is 4243 km in the People's Republic of China that connects the cities of Lianyungang, in the province of Jiangsu, and Khorgas, in the autonomous region of Xinjiang, on the border with Kazakhstan.  At Khorgas, there is a border crossing into Kazakhstan.  The expressway is the longest contiguous expressway in China with a single numeric designation, stretching across the country from the Yellow Sea on the east coast to the Kazakhstan border in the west.  It passes through the provinces of Jiangsu, Anhui, Henan, Shaanxi, Gansu, and Xinjiang.

Shaanxi: Shaanxi () is a province of the People's Republic of China.  Officially part of the Northwest China region, it lies in central China, bordering the provinces of Shanxi (NE, E), Henan (E), Hubei (SE), Chongqing (S), Sichuan (SW), Gansu (W), Ningxia (NW), and Inner Mongolia (N).  It covers an area of over 205,000 sqkm with about 37 million people.  Xi'an—which includes the sites of the former Chinese capitals Fenghao and Chang'an—is the provincial capital.  Xianyang, which served as the Qin capital, is located nearby.  The other prefecture-level cities into which the province is divided are Ankang, Baoji, Hanzhong, Shangluo, Tongchuan, Weinan, Yan'an and Yulin.

Dengzhou: Dengzhou (), formerly Deng County (邓县), is a city in Nanyang, Henan, China.  It has an area of 2,294 km² and a population of 1,500,000.  The urban area is 35 km², and the urban population is 300,000.  The city is located in the southwest of Henan province, adjacent to the borders between Henan, Hubei and Shaanxi.  It geometrically lies in the center of the triangle of Zhengzhou, Wuhan and Xi'an, with equal distance to any of these three cities.

Hongqingsi Grottoes: Hongqing Temple Grotto () is located in Yima, Henan.  It consists of five caves, with a total of 46 shrines.  More than 120 statues were chiseled during the Northern Wei Dynasty.  In 1963, it was registered as a place of cultural importance in Henan, and was listed in the fifth edition of Chinese national cultural relics in 2001.

Huilong Township, Henan: Huilong Township () is a township of Tongbai County in southern Henan province, China, located near the trisection of the prefecture-level cities of Nanyang, Zhumadian, and Xinyang.  It is situated 119 km southeast of Nanyang, 48 km southwest of Zhumadian and 62 km northwest of Xinyang.  , it has 10 villages under its administration.

Yima, Henan: Yima () is a county-level city of Henan, China.  It is under the administration of the Sanmenxia city.  Yima City is located in the western part of Henan province.  It is located inside Xiaoshan Old Way, with Yangshao Peak to the north and Balcony Loewe to the south.  Since ancient times, it was a key road between Luoyang and Changan.  It is of great strategic importance, often a battlefield or a place for merchants to trade.  Yima City was founded two years before the Qin Dynasty called "The New County".  After reforms were made, Yima City reache county-level status in Henan Province (it took 81 years to build the city).  It was originally under the administration of Luoyang.  However, since 1986, it is under the administration of Sanmenxia City.  Currently, it is one of forty-eight counties in Henan Province trying to expand its powers.  It is also one of China's top hundred counties, as well as being the smallest city in China (112 square kilometers with a population of about 160,000).  Yima City has the advantage of being self-sustaining, allowing for massive redevelopment of its industry and increased economic growth.  In 2010, the city's per capita GDP was over seventy thousand RMB, which is about ten thousand US dollars.  It ranks alongside moderately developed countries.  In 2010, it was ranked first economically in Henan Province (perennial top five).  The city is also known as a "The Village of Martial Arts".

Question: Both cities of Karamay and Yima, Henan are located in which country?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "country_name": {
      "type": "string",
      "description": "The name of the country where the cities are located."
    },
    "cities_located": {
      "type": "array",
      "description": "A list of cities located in the specified country.",
      "items": {
        "type": "string"
      }
    },
    "number_of_cities": {
      "type": "integer",
      "description": "The total number of cities found in the specified country."
    }
  },
  "required": [
    "country_name",
    "cities_located",
    "number_of_cities"
  ],
  "additionalProperties": false
}
