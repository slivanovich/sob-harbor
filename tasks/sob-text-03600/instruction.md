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
Guoshan Stele: Guoshan Stele () is a stele located at the west foot of Guoshan Mountain in Zhangzhu Town, Yixing City, Jiangsu Province in China.  The stele was listed in the fifth batch of Major Site Protected for Its Historical and Cultural Value at the National Level in 2001.

Yixing ware: Yixing clay () is a type of clay from the region near the city of Yixing in Jiangsu Province, China, used in Chinese pottery since the Song dynasty (960–1279) when Yixing clay was first mined around China's Lake Tai.  From the 17th century on, Yixing wares were commonly exported to Europe.  The finished stoneware, which is used for teaware and other small items, is usually red or brown in color.  Also known as zisha () ware, they are typically left unglazed and use clays that are very cohesive and can form coils, slabs and most commonly slip casts.  These clays can also be formed by throwing.  The best known wares made from Yixing clay are Yixing clay teapots, tea pets, and other teaware.

Liaocheng: Liaocheng (), also known as the Water City, is a prefecture-level city in western Shandong province, China.  It borders the provincial capital of Jinan to the southeast, Dezhou to the northeast, Tai'an to the south, and the provinces of Hebei and Henan to the west.  The Grand Canal flows through the city center.  Its population was 5,789,863 at the 2010 census whom 1,229,768 lived in the built-up area made up of Donchangfu district, even though large parts remain rural.

Huaiyin District, Jinan: Huaiyin District () is one of six districts of Jinan, the capital of Shandong province, People's Republic of China, forming part of the city's urban core.  It borders the districts of Tianqiao to the northeast, Shizhong to the southeast, and Changqing to the southwest, as well as the prefecture-level city of Dezhou to the northwest.

Dezhou: Dezhou () is a prefecture-level city in northwestern Shandong province, People's Republic of China.  It borders the provincial capital of Jinan to the southeast, Liaocheng to the southwest, Binzhou to the northeast, and the province of Hebei to the north.

Yucheng, Shandong: Yucheng (禹城; pinyin: "Yǔchéng") is a county-level city of the Chinese province of Shandong.  It is administered by the prefecture-level city of Dezhou.

Qianhuang: Qianhuang is a Chinese city located south of Changzhou city, in southern Jiangsu province of the China.  It is 8 kilometers away from Wujin District.  To the east of Qianhuang is Wuxi, a national tourist resort, and it is 15 kilometers away from Yixing, a famous pottery city.

Dezhou braised chicken: Dezhou braised chicken () is a famous Chinese dish from the city of Dezhou in Shandong Province, China.

Yixing: Yixing () is a county-level city with a population of 1.24 million administrated under the prefecture-level city of Wuxi in southern Jiangsu province, People's Republic of China, and is part of the Yangtze River Delta.  The city is known for its traditional Yixing clay ware.

Yixing Pumped Storage Power Station: The Yixing Pumped Storage Power Station is a pumped-storage hydroelectric power station located Yixing city of Jiangsu Province, China.  Construction on the power station began in 2003 and the first unit was commissioned in 2007, the last in 2008.  The entire project cost US$490 million, of which US$145 million was provided by the World Bank.  The power station operates by shifting water between an upper and lower reservoir to generate electricity.  The lower reservoir was formed with the existing Huiwu Dam at the foot of Mount Tongguan.  The Yixing Upper Reservoir is located atop Mount Tongguan which peaks at 530 m above sea level.  During periods of low energy demand, such as at night, water is pumped from Huiwu Lower Reservoir up to the upper reservoir.  When energy demand is high, the water is released back down to the lower reservoir but the pump turbines that pumped the water up now reverse mode and serve as generators to produce electricity.  Water from the nearby Huangtong River can also be pumped into the lower reservoir to augment storage.  The process is repeated as necessary and the plant serves as a peaking power plant.  The power station is operated by East China Yixing Pumped Storage Co Ltd.

Question: Are Yixing and Dezhou the same level of city?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "city_1_name": {
      "type": "string",
      "description": "The name of the first city being compared."
    },
    "city_1_administrative_level": {
      "type": "string",
      "description": "The administrative level of the first city."
    },
    "city_2_name": {
      "type": "string",
      "description": "The name of the second city being compared."
    },
    "city_2_administrative_level": {
      "type": "string",
      "description": "The administrative level of the second city."
    },
    "are_same_level": {
      "type": "boolean",
      "description": "Indicates whether the two cities are at the same administrative level."
    },
    "comparison_summary": {
      "type": "string",
      "description": "A summary of the comparison regarding their administrative levels."
    }
  },
  "required": [
    "city_1_name",
    "city_1_administrative_level",
    "city_2_name",
    "city_2_administrative_level",
    "are_same_level",
    "comparison_summary"
  ],
  "additionalProperties": false
}
