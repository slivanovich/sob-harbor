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
Hailar District: Hailar District (Mongolian: ᠬᠠᠶᠢᠯᠠᠷ ᠲᠣᠭᠣᠷᠢᠭ "Qayilar toɣoriɣ" Хайлаар тойрог, Cyrillic: Хайлаар дүүрэг, "Khailaar düüreg"; ) is an urban district that serves as the seat of the prefecture-level city Hulunbuir in northeastern Inner Mongolia, China.  Hulunbuir, due to its massive size, is a city in administrative terms only, being mainly grassland and rural.  Hailar, therefore, is a "de facto" city.  Hailar can also refer to the urban area around the Hailar district, with Hulunbuir being the wider geographical region that contains the urban area.

Oroqen Autonomous Banner: Oroqen Autonomous Banner (Mongolian: ᠣᠷᠴᠣᠨ ᠤ ᠥᠪᠡᠷᠲᠡᠭᠡᠨ ᠵᠠᠰᠠᠬᠤ ᠬᠣᠰᠢᠭᠤ "Orčon-u öbertegen jasaqu qosiɣu"; simplified Chinese: 鄂伦春自治旗; pinyin: "Èlúnchūn Zìzhìqí") is an autonomous banner that lies directly south of the urban district of Hailar in the prefecture-level city of Hulunbuir.  It covers an area of 60,378 km2 .  As of the 2010 census , there were 223,752 inhabitants with a population density of 4.84 inhabitants per km².  Its capital is the town of Alihe (阿里河镇).  It includes Ganhe (甘河), Dayangshu (大杨树), Jiwen (吉文) but excludes the Jiagedaqi and Songling Districts.

Hulunbuir: Hulunbuir or Hulun Buir (Mongolian: ; , "Hūlúnbèi'ěr") is a region that is governed as a prefecture-level city in northeastern Inner Mongolia, in China.  Its administrative center is located at Hailar District, its largest urban area.  Major scenic features are the high steppes of the Hulun Buir grasslands, the Hulun and Buir lakes (the latter partially in Mongolia), and the Khingan range.  Hulun Buir borders Russia to the north and west, Mongolia to the south and west, Heilongjiang province to the east and Hinggan League to the direct south.  Hulunbuir is a linguistically diverse area: next to Mandarin Chinese, Mongolian dialects such as Khorchin and Buryat, the Mongolic language Dagur and some Tungusic languages are spoken there.

Batetsky (rural locality): Batetsky (Russian: Батецкий ) is a rural locality (a settlement of rural type) and the administrative center of Batetsky District, Novgorod Oblast, Russia, located in the northwest of the oblast, on the banks of the Udrayka River (a right tributary of the Luga).  It also serves as the administrative center of Batetskoye Settlement, one of the three settlements into which the district is administratively divided.  Municipally, it is the administrative center of Batetskoye Rural Settlement in Batetsky Municipal District.  Population:  (2010 Census) ;  (2002 Census) ;  (1989 Census)

Evenk Autonomous Banner: Evenk Autonomous Banner (Evenki: ; Ewengki Aimanni Mvvngkeng Isihēr Gosa ; Mongolian: ᠡᠸᠡᠩᠬᠢ ᠥᠪᠡᠷᠲᠡᠭᠡᠨ ᠵᠠᠰᠠᠬᠤ ᠬᠣᠰᠢᠭᠤ "Eveŋki öbertegen jasaqu qosiɣu"; ) is an autonomous banner that lies directly south of the urban district of Hailar in the prefecture-level city of Hulunbuir, People's Republic of China.  It has an area of 19,111 km ².  By 2013, there are 143,415 inhabitants with a population density of 7.5 inhabitants per km². Its capital is the town of Bayan Tohoi (巴彥托海鎮).  Dayan Town(大雁镇),which used to be Dayan Mining Area(大雁矿区) as an administrative division and is now the main part of an industrial district also named Dayan Mining Area(大雁矿区),has the largest population of about 73,000 in Evenk Autonomous Banner.

Krasnoborsk, Arkhangelsk Oblast: Krasnoborsk (Russian: Краснобо́рск ) is a rural locality (a "selo") and the administrative center of Krasnoborsky District, Arkhangelsk Oblast, Russia, located on the left bank of the Northern Dvina River.  It also serves as the administrative center of Alexeyevsky Selsoviet, one of the ten selsoviets into which the district is administratively divided.  Municipally, it is the administrative center of Alexeyevskoye Rural Settlement in Krasnoborsky Municipal District.  Population:  (2010 Census) ;  (2002 Census) ;  (1989 Census)

Khmelnytskyi Raion: Khmelnytskyi Raion (Ukrainian: Хмельницький район , "Khmel'nyts'kyi raion" ) is one of the 20 administrative raions (a "district") of the Khmelnytskyi Oblast in western Ukraine.  Its administrative center is located in the city of Khmelnytskyi.  Even though the city of Khmelnytskyi is separate from the raion's government, it still serves as its administrative center in addition to its role as that of the Khmelnytskyi Oblast's administrative center.  Its population was 53,686 in the 2001 Ukrainian Census and 52,906 as of 2012 .

Qingyang: Qingyang () is a prefecture-level city in eastern Gansu province, China.

Old Barag Banner: Old Barag Banner (Mongolian: ᠬᠠᠭᠤᠴᠢᠨ ᠪᠠᠷᠭᠤ ᠬᠣᠰᠢᠭᠤ Қаучин Бару қосиу "Qaɣučin Barɣu qosiɣu"; ) is a banner of northeastern Inner Mongolia, People's Republic of China.  It is located 28 km from Hailar District, the administrative centre of Hulunbuir City, which administers this banner.

Hulunbuir Hailar Airport: Hulunbuir Hailar Airport (IATA: HLD, ICAO: ZBLA) is an international airport airport serving Hailar District of Hulunbuir, a prefecture-level city of Inner Mongolia, China.  The airport was formerly called Hailar Dongshan Airport (海拉尔东山机场) until it was renamed on 1 January 2011.

Question: What prefecture-level city has its administrative center located at Hailar District, Qingyang or Hulunbuir?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "prefecture_level_city_name": {
      "type": "string",
      "description": "The name of the prefecture-level city that has Hailar District as its administrative center."
    },
    "administrative_center_district": {
      "type": "string",
      "description": "The name of the district serving as the administrative center."
    },
    "is_administrative_center_of_hulunbuir": {
      "type": "boolean",
      "description": "Indicates if Hailar District is the administrative center of Hulunbuir."
    },
    "is_administrative_center_of_qingyang": {
      "type": "boolean",
      "description": "Indicates if Hailar District is the administrative center of Qingyang."
    },
    "answer": {
      "type": "string",
      "description": "The final answer to the question."
    }
  },
  "required": [
    "prefecture_level_city_name",
    "administrative_center_district",
    "is_administrative_center_of_hulunbuir",
    "is_administrative_center_of_qingyang",
    "answer"
  ],
  "additionalProperties": false
}
