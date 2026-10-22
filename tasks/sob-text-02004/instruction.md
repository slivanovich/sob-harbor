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
Baoding People's Stadium: Baoding People's Stadium (Simplified Chinese: 保定市人民体育场) is a multi-use stadium in Baoding, Hebei province, China.  It is currently used mostly for football matches.  The stadium holds 13,000 people.

Wang Chengbin: Wang Chengbin () (August 21, 1874 – February 15, 1936) was an ethnic Manchu Chinese general of the Warlord Era of the Republic of China.  He was the father of Hong Kong cartoonist Alfonso Wong.  Born in Fengtian (modern Liaoning) province, Wang attended the Baoding Military Academy from 1907-09, joining the New Army shortly afterward and being stationed in Changchun, Jilin province.  In October 1911, after the outbreak of the Wuchang Uprising, he was sent to Shanxi Province to suppress supporters of the Xinhai Revolution.  In August 1912 he was made commander of the 11th Regiment, which was part of the 3rd Division, 6th Brigade.  In autumn 1913 he went with the 3rd Division to Yuezhou (modern Yueyang, Hunan province), to suppress the Second Revolution.  In 1915, he went with the 3rd Division to Sichuan province to suppress opposition to the Empire of China.  In July 1917 he acted with Wu Peifu to bring down Zhang Xun's Manchu Restoration.

Baoding: Baoding () is a city in Hebei province, China, approximately 150 km southwest of the national capital, Beijing.  At the 2010 census, Baoding City had 11,194,372 inhabitants out of which 2,176,857 lived in the built-up ("or metro") area made of 3 urban districts and Qingyuan and Mancheng counties largely being conurbated, on 1,840 km2 .  Baoding is among 13 Chinese cities with a population of over 10 million, ranking seventh.

Baoding East Railway Station: The Baoding East Railway Station is a railway station of Jingshi Passenger Railway located in Baoding, Hebei Province, the People's Republic of China.

San Miguel Brewery Hong Kong: San Miguel Brewery Hong Kong Ltd. (香港生力啤酒廠有限公司) (SMBHK) () is a brewery based in Hong Kong and is a majority-owned subsidiary of San Miguel Brewing International Ltd., a wholly owned subsidiary of San Miguel Brewery, Inc..  The company has two subsidiaries located in the Guangdong province of the People’s Republic of China.  An affiliate company, San Miguel Baoding Brewery Company Limited, is based in Baoding, China.

Lengshuijiang, Lengshuijiang: Lengshuijiang Subdistrict () is a Subdistrict in Lengshuijiang, Loudi City, Hunan Province, People's Republic of China.

Lengshuijiang: Lengshuijiang () is a county-level city in Hunan Province, China, it is under the administration of Loudi prefecture-level City.  Located on the central Hunan, the city is bordered to the north and west by Xinhua County, to the south by Xinshao County, to the east by Lianyuan City.  Lengshuijiang City covers 439 km2 .  As of 2015， it has a registered population of 370,300 and a resident population of 342,700.  The city has 4 subdistricts, 5 towns and a township under its jurisdiction, the government seat is Lengshuijiang Subdistrict (冷水江街道).

Dingzhou: Dingzhou (), formerly Dingxian ( postal: Tingsien) is a county-level city with sub-prefecture-level city status, located under the administration of the prefecture-level city of Baoding in the southwest of Hebei Province in northern China, about halfway between Baoding and Shijiazhuang.  As of 2009, Dingzhou had a population of 1.2 million.  Dingzhou has 3 subdistricts, 13 towns, 8 townships, and 1 ethnic township.  Dingzhou is 196 km southwest of Beijing, 68 km northeast of Shijiazhuang.

Gaobeidian: Gaobeidian () is a county-level city in south-central Hebei province, People's Republic of China.  It is under the administration of Baoding Prefecture-level city.  Gaobeidian has 4 subdistricts, 6 towns, and 4 townships, and a total of 442 villages.  It is 82 km south of Beijing and 68 km north of Baoding.

Roman Catholic Diocese of Baoding: The Roman Catholic Diocese of Baoding/Ching-Yüan/Qingyuan (Latin: "Paotimen(sis)" , ) is a diocese located in the city of Baoding in the Ecclesiastical province of Beijing in China.

Question: Are Baoding and Lengshuijiang in the same province in China?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "are_in_same_province": {
      "type": "boolean",
      "description": "Indicates whether the two cities are located in the same province."
    },
    "city_1": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the first city."
        },
        "province": {
          "type": "string",
          "description": "The province where the first city is located."
        }
      },
      "required": [
        "name",
        "province"
      ],
      "additionalProperties": false
    },
    "city_2": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the second city."
        },
        "province": {
          "type": "string",
          "description": "The province where the second city is located."
        }
      },
      "required": [
        "name",
        "province"
      ],
      "additionalProperties": false
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation for why the cities are or are not in the same province."
    }
  },
  "required": [
    "are_in_same_province",
    "city_1",
    "city_2",
    "reasoning"
  ],
  "additionalProperties": false
}
