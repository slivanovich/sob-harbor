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
Xinji: Xinji(辛集，Xīnjí) is a county-level city with sub-prefecture-level city status, located under the administration of the prefecture-level city of Shijiazhuang of Hebei Province in northern China.  There are 8 towns (镇，zhèn) and 7 townships (乡，xiāng) under the administration of Xinji.

Shanghai: Shanghai is one of the four direct-controlled municipalities of China and the most populous city proper in the world with a population of more than 24 million as of 2014 .  It is a global financial centre and transport hub, with the world's busiest container port.  Located in the Yangtze River Delta, it sits on the south edge of the estuary of the Yangtze in the middle portion of the East China coast.  The municipality borders the provinces of Jiangsu and Zhejiang to the north, south and west, and is bounded to the east by the East China Sea.

Yangtze River Delta: The Yangtze River Delta or YRD is a triangle-shaped metropolitan region generally comprising Wu-speaking area, Shanghai, southern Jiangsu province and northern Zhejiang province of China.  The area lies in the heart of the Jiangnan region (literally, "south of the River"), where Yangtze River drains into the East China Sea.  The urban build-up in the area has given rise to what may be the largest concentration of adjacent metropolitan areas in the world.  It covers an area of 99,600 km2 and is home to over 115 million people as of 2013, of which an estimated 83 million is urban.  If based on the greater Yangtze River Delta zone, it has over 140 million people in this region.  Having a fertile soil, the Yangtze River Delta abundantly produces grain, cotton, hemp and tea.

Shanghai–Nantong Railway: Shanghai–Nantong Railway, abbreviated as Hutong Railway (, "Hu" and "Tong" being the abbreviations for Shanghai and Nantong, respectively) is a future railway in China's Yangtze River Delta area.  It will connect the region's main city, Shanghai, located south of the Yangtze, with Nantong, north of the river.

Yangtze River Delta Economic Zone: Yangtze River Delta Economic Zone or Yangtze River Delta Economic Region () is an economic region in China that encompasses Shanghai municipality, Jiangsu, Anhui and Zhejiang province.

Tianchang: Tianchang is a Sub-prefecture-level city on the Yangtze River, 290 km northwest of Shanghai, it's a part of Yangtze River Delta Economic Zone.  It is under the administration of Chuzhou, Anhui Province, China.

Geography of Shanghai: The geography of Shanghai is characterised by its location on the Yangtze River Delta on China's east coast and its proximity to the Pacific Ocean via the East China Sea.  The city is centred on the Huangpu River, a tributary of the Yangtze River, and extends outwards in all directions, with the suburbs and satellite towns reaching east to the East China Sea, north and west to Jiangsu province, and south to Zhejiang province over Hangzhou Bay.

Suzhou: Suzhou, formerly romanized as Soochow, is a major city located in southeastern Jiangsu Province of East China, about 100 km northwest of Shanghai.  It is a major economic center and focal point of trade and commerce, and the largest city in the province.  The city is situated on the lower reaches of the Yangtze River and the shores of Lake Tai and belongs to the Yangtze River Delta region.  Administratively, Suzhou is a prefecture-level city with a population of 4.33 million in its city proper, and a total resident population (as of 2013 ) of 10.58 million in its administrative area.  Its urban population grew at an unprecedented rate of 6.5% between 2000 and 2014, which is the highest among cities with more than 5 million people.

Chongming–Qidong Yangtze River Bridge: Chongming-Qidong Yangtze River Bridge or the Chongqi Bridge (), also called Chongqi Crossing Project (), is a bridge across the north fork of the Yangtze River, near the river's mouth between Chongming Island of Shanghai and Qidong in Jiangsu Province.  This bridge, along with the Shanghai Yangtze River Tunnel and Bridge to the south, forms the last crossing of the Yangtze River before the river empties into the East China Sea.  The bridge carries the six-lane G40 Shanghai–Xi'an Expressway, part of the National Expressway Network of the People's Republic of China.

Shanghai Yangtze River Tunnel and Bridge: The Shanghai Yangtze River Tunnel and Bridge is the collective name given to the bridge–tunnel complex across the south fork of the Yangtze River near the river mouth in Shanghai.  The tunnel connects the Pudong District of Shanghai on the south bank of the river with Changxing Island, while the bridge connects Changxing Island with Chongming Island.  In combination with the Chongqi Bridge (opened in December 2011), which connects Chongming Island to the north bank of the Yangtze, the bridge–tunnel complex forms the final crossing of the Yangtze before it empties into the East China Sea.

Question: In between  Xinji and Shanghai which one is located in the Yangtze River Delta?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "city_in_yangtze_river_delta": {
      "type": "string",
      "description": "The name of the city located in the Yangtze River Delta."
    },
    "is_located_in_yangtze_river_delta": {
      "type": "boolean",
      "description": "Indicates whether the identified city is indeed located in the Yangtze River Delta."
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation for why the city is or is not in the Yangtze River Delta, based on the provided context."
    },
    "other_city_information": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the other city mentioned in the question."
        },
        "location_description": {
          "type": "string",
          "description": "A description of the other city's location, indicating it is not in the Yangtze River Delta."
        }
      },
      "required": [
        "name",
        "location_description"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "city_in_yangtze_river_delta",
    "is_located_in_yangtze_river_delta",
    "reasoning",
    "other_city_information"
  ],
  "additionalProperties": false
}
