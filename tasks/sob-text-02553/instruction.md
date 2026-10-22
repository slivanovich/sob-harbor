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
Huade County: Huade (Mongolian: ᠬᠤᠸᠠᠳᠧ ᠰᠢᠶᠠᠨ "Quvadė siyan"; ) is a county of central Inner Mongolia, People's Republic of China, bordering Hebei province to the southeast, Xilin Gol League to the northeast, and Shangdu County to the west.  It is under the administration of Ulaan Chab city.

Xilinhot: Xilinhot (Mongolian: Шилийн хот, , "Sili-yin hota" ; ) is a county-level city which serves as the seat of government for the Xilin Gol league in Inner Mongolia, People's Republic of China.  It has a jurisdiction area of 14,785 km2 , and a population of 245,886, with 149,000 being in the Xilinhot urban area.

Chahar Right Rear Banner: Chahar Right Rear Banner (Mongolian: ᠴᠠᠬᠠᠷ ᠪᠠᠷᠠᠭᠤᠨ ᠭᠠᠷᠤᠨ ᠬᠣᠶᠢᠲᠤ ᠬᠣᠰᠢᠭᠤ ; Цахар баруун гарын хойд хошуу; "Čaqar Baraɣun Ɣarun Qoyitu qosiɣu"; ) is a banner of Inner Mongolia, People's Republic of China, bordering Shangdu County to the northeast, Xinghe County to the southeast, Chahar Right Front Banner to the south, Zhuozi County to the southwest, Chahar Right Rear Banner to the west, Siziwang Banner to the northwest, and Xilin Gol to the north.  It is under the administration of Ulaan Chab City, which lies to the south along the G55 Erenhot–Guangzhou Expressway.  The most important settlement in the banner is Baiyinchagan.

Erenhot: Erenhot (Mongolian: "Эрээн хот" ; , commonly shortened to Ereen or Erlian) is a county-level city of the Xilin Gol League, in Inner Mongolia Autonomous Region, located in the Gobi Desert along the Sino-Mongolian border, across from the Mongolian town of Zamyn-Üüd.  There are 74,197 inhabitants (2010 census) and the elevation is 966 m .

Chifeng: Chifeng (), also known as Ulankhad (Mongolian: (Улаанхад хот) "Ulaɣanqada qota" ] , "red cliff"), is a prefecture-level city in southeastern Inner Mongolia, People's Republic of China.  It borders Xilin Gol League to the north and west, Tongliao to the northeast, Chaoyang (Liaoning) to the southeast, and Chengde (Hebei) to the south.  The city has a total administrative area of 90,275 km² and has a population of 4,341,245 inhabitants.  As of the 2010 census, 1,094,970 of those residents reside within in the urban districts of Hongshan, Yuanbaoshan and Songshan.  However, a large part of Songshan is still rural and Yuanbaoshan is a de facto separate town 27 kilometers away from the core district of Chifeng.  The city was the administrative center of the defunct Ju Ud League (; ).

Honggor Sumu, Sonid Left Banner: Honggor Sumu (Mongolian: ""soft"" or ""sweetheart"" ; ) is a sumu in the Sonid Left Banner of Xilin Gol League, Inner Mongolia, China.  In 2000, it had 1621 inhabitants.  It is located in high desert only 38 km from the border with Mongolia.

Artux: Artux, Atush or Atushi (, Xiao'erjing: اَتُشِ; ; Kyrgyz: ارتىش, Артыш , "Artış") is a county-level city in Xinjiang.  The area is 15,509 km² and the total population is 200,000 (2002).  Artux is the seat of Kizilsu Kirghiz Autonomous Prefecture.

Üzemchin Mongols: The Üzemchin (Mongolian: Үзэмчин), also written Ujumchin, Ujumucin or Ujimqin, are a subgroup of Mongols in eastern Mongolia and Inner Mongolia.  They settle mainly in Sergelen, Bayantu'men, Choibalsan city of the Dornod Province and in Xilin Gol League of the Inner Mongolia.  In Mongolia, Some Üzemchins migrated there from Xilin Gol immediately after China was freed from the Japanese in 1945.

Dolon Nor: Dolon Nor (; Mongolian: Долоон нуур , Doloon nuur, "seven lakes"; also: To-lun, Dolonnur), is a town and the county seat of Duolun County, Xilin Gol League in the Inner Mongolia Autonomous region, China.  It is of historical importance because the remnants of Shangdu, the summer capital of Kublai Khan and the following Mongol emperors of the Yuan dynasty (13th and 14th century), are located some 28 kilometers (17 miles) northwest of the modern town.  Beginning in the 17th century, the Manchu emperors of the Qing dynasty developed the city as a religious center.

Zhenglan Banner: Zhenglan (Xulun Hoh) Banner, also known as Plain Blue Banner or Shuluun Huh Banner, (Mongolian: ᠰᠢᠯᠤᠭᠤᠨ ᠬᠥᠬᠡ ᠬᠣᠰᠢᠭᠤ Силуун Көкэ қосиу "Siluɣun Köke qosiɣu"; ) is a banner of Inner Mongolia, China.  It is under the administration of Xilin Gol League.  Xanadu was located here.

Question: Between Artux and Erenhot, which city is a county-level city of the Xilin Gol League?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "query_cities": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The cities mentioned in the question for comparison."
    },
    "identified_city": {
      "type": "string",
      "description": "The city that matches the criteria."
    },
    "city_type": {
      "type": "string",
      "description": "The administrative type of the identified city."
    },
    "administrative_affiliation": {
      "type": "string",
      "description": "The administrative division the identified city belongs to."
    },
    "is_part_of_xilin_gol_league": {
      "type": "boolean",
      "description": "True if the identified city is a county-level city of Xilin Gol League, false otherwise."
    }
  },
  "required": [
    "query_cities",
    "identified_city",
    "city_type",
    "administrative_affiliation",
    "is_part_of_xilin_gol_league"
  ],
  "additionalProperties": false
}
