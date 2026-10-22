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
Dengsheng: Dengsheng () is an area in Wolong National Nature Reserve, Wenchuan County, Sichuan, China.  It is located in the southwestern part of the Wolong National Nature Reserve, approximately 77 miles WNW of Chengdu, the capital of Sichuan province), approximately 62 miles southwest of Wenchuan county seat, Weizhou, approximately 47 miles WSW of Dujiangyan City, approximately 122 miles southwest of Beichuan County and approximately 128 miles WSW of Mianyang.

Kuiguang Pagoda: The Kuiguang Pagoda (Chinese: 奎光塔; pinyin: Kúi Gūang Tǎ ) of Dujiangyan City, Sichuan province, China, is a pagoda built in 1831 during the Qing dynasty.

Dujiangyan: The Dujiangyan () is an ancient irrigation system in Dujiangyan City, Sichuan, China.  Originally constructed around 256 BC by the State of Qin as an irrigation and flood control project, it is still in use today.  The system's infrastructure is on the Min River (Minjiang), the longest tributary of the Yangtze.  The area is in the west part of the Chengdu Plain, at the confluence between the Sichuan basin and the Tibetan plateau.  Originally the Min rushed down from the Min Mountains, but slowed abruptly after reaching the Chengdu Plain, filling the watercourse with silt, which made the nearby areas extremely prone to floods.  Li Bing, then governor of Shu for the state of Qin, and his son headed the construction of the Dujiangyan, which harnessed the river using a new method of channeling and dividing the water rather than simply following the old way of dam building.  It is still in use today to irrigate over 5,300 km2 of land in the region.  The Dujiangyan, the Zhengguo Canal in Shaanxi and the Lingqu Canal in Guangxi are collectively known as the "three great hydraulic engineering projects of the Qin."

Juyuan High School: Dujiangyan August 1 Juyuan High School (Chinese Simplified: 都江堰市八一聚源高级中学, Traditional: 都江堰市八一聚源高級中學, Pinyin: Dūjiāngyànshì Bāyī Jùyuán Gāojízhōngxué, BYJYGZ) is a secondary school located in Dujiangyan City, Chengdu, Sichuan.

List of dams and reservoirs in China: Dams and reservoirs in China are numerous and have had a profound effect on the country's development and people.  According to the World Commission on Dams in 2000, there were 22,104 dams over the height of 15 m operating in China.  Of the world's total large dams, China accounts for the most – 20 percent of them; 45 percent of which are used for irrigation.  Accordingly, the oldest in China still in use belongs to the Dujiangyan Irrigation System which dates back to 256 BC.  In 2005, there were over 80,000 reservoirs in the country and over 4,800 dams completed or under construction that stands at or exceed 30 m in height.  As of 2007, China is also the world's leader in the construction of large dams; followed by Turkey, and Japan in third.  The tallest dam in China is the Jinping-I Dam at 305 m , an arch dam, which is also the tallest dam in the world.  The largest reservoir is created by the Three Gorges Dam, which stores 39.3 billion m (31,900,000 acre feet) of water and has a surface area of 1045 km2 .  Three Gorges is also the world's largest power station.

Dujiangyan City: Dujiangyan () is a county-level city, a subdivision of Chengdu, the capital of Sichuan Province, People's Republic of China.  Its north-west region forms a border with sourthern Ngawa Tibetan and Qiang Autonomous Prefecture.  It has an area of 1208 km2 and had a population of 600,000 in 2003.

Yingxiu: Yingxiu () is a town of southern Wenchuan County, northwestern Sichuan province of Southwest China.  It is located at the southern end of the Ngawa Tibetan and Qiang Autonomous Prefecture, and lies on the road to Jiuzhaigou Valley, Wolong and the Siguniang Mountains.  It is located 47 km south of the county urban centre, and just 14 km west of the city of Dujiangyan.  The town has an area of 115 km2 , and as of 2007, a population of 6,906.

Sichuan Leaders F.C.: Sichuan Leaders Football Club () are a China League Two club.  They are an association football club from Dujiangyan City.  The Sichuan Leaders were a new entry in the 2014 China League Two.  The Dujiangyan Sports Centre Stadium is their home venue.

Fuqing:    (; Foochow Romanized: Hók-chiăng; also romanized as Hokchia) is a county-level city of Fuzhou Prefecture in Fujian Province, People's Republic of China.

G0511 Deyang-Dujiangyan Expressway: G0511 Deyang–Dujiangyan Expressway(Chinese:德都高速公路, 德都高速) is a part of Chengdu Economic Zone Ring Expressway, starting from Deyang City in Sichuan Province, the way Shifang, Pengzhou, only in Dujiangyan City, Sichuan Province.

Question: In between Fuqing and Dujiangyan City which has an area of 1208 km2?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "city_with_specified_area": {
      "type": "string",
      "description": "The name of the city that has the specified area."
    },
    "area_km2": {
      "type": "integer",
      "description": "The area in square kilometers."
    },
    "compared_cities": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of cities that were compared."
    },
    "area_information_available_for_all_compared_cities": {
      "type": "boolean",
      "description": "Indicates if area information was available for all cities in the comparison."
    }
  },
  "required": [
    "city_with_specified_area",
    "area_km2",
    "compared_cities",
    "area_information_available_for_all_compared_cities"
  ],
  "additionalProperties": false
}
