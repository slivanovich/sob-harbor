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
China Southern Airlines Flight 3943: China Southern Airlines Flight 3943 was a China Southern Airlines flight from the former Guangzhou Baiyun International Airport, Guangzhou to Guilin Qifengling Airport, Guilin, China on 24 November 1992.  It crashed on descent to Guilin Airport, killing all 141 aboard.

Shaoyang Wugang Airport: Shaoyang Wugang Airport (IATA: WGN, ICAO: ZGSY) is an airport serving the city of Shaoyang in Hunan Province, China.  It is located 9 km north of Wugang, a county-level city under the administration of Shaoyang, and 100 km from the urban center of Shaoyang.  The airport received approval from the State Council of China and the Central Military Commission in July 2013.  It is expected to cost 957 million yuan to build.  The airport was opened on 28 June 2017, with an inaugural China Southern Airlines flight from Changsha Huanghua International Airport.

Si Xianmin: Si Xianmin (; born November 1957) is a former Chinese business executive who served as chairman and general manager of China Southern Airlines, the world's sixth-largest airline measured by passengers carried and Asia's largest airline in fleet size and passengers carried.  Si Xiamin spent more than 20 years in China Southern Airlines.  He was a delegate to the 12th National People's Congress.  In November 2015, he was placed under investigation by the Chinese Communist Party's anti-corruption agency.  He is the first head of civil aviation in China implicated since the beginning of Xi Jinping's anti-corruption drive after he took power in late 2012.

Dalian Zhoushuizi International Airport: Dalian Zhoushuizi International Airport (IATA: DLC, ICAO: ZYTL) is the airport serving the city of Dalian in Liaoning Province, China.  It is located in Ganjingzi District, about 10 km northwest of the city center.  In 2014 the airport handled 17,203,640 passengers, making it the busiest airport in Northeast China and the 16th busiest nationwide.  The airport is the hub for Dalian Airlines and a focus city for China Southern Airlines and Hainan Airlines.  As Zhoushuizi Airport has reached its designed capacity, the new Dalian Jinzhouwan International Airport is being built on reclaimed land to replace it.

1990 Guangzhou Baiyun airport collisions: On 2 October 1990, a hijacked Boeing 737, operating Xiamen Airlines Flight 8301, collided with two other aircraft on the runways of the old Guangzhou Baiyun International Airport, while attempting to land.  The hijacked aircraft struck a parked China Southwest Airlines Boeing 707 first, inflicting only minor damage, but then collided with China Southern Airlines Flight 2812, a Boeing 757 waiting to take off, flipping onto its back.  A total of 128 people were killed, including seven of nine crew members and 75 of 93 passengers on Flight 8301 and 46 of 110 passengers on Flight 2812.

Wuhan Tianhe International Airport: Wuhan Tianhe International Airport (IATA: WUH, ICAO: ZHHH) serves Wuhan, the capital of the Hubei province, People's Republic of China.It was opened on 15 April 1995 substituting the old Hankou Wangjiadun Airport and Nanhu Airport as the major airport of Wuhan.  The airport is located in Wuhan's suburban Huangpi District, around 26 kilometres to the north of Wuhan city center.  It is the busiest airport of central China as it is geographically located in the centre of China's airline route network.  The airport is a focus city for Air China, China Eastern Airlines and China Southern Airlines.  The airport has flights to international destinations such as Bangkok, Moscow, Osaka, Paris, Seoul, and Singapore.

Guizhou Airlines: Guizhou Airlines () was an airline based in Guiyang, Guizhou, China.  It was a small provincial subsidiary of China Southern Airlines operated scheduled domestic passenger and cargo services in southern China.  Its main base was Guiyang Longdongbao Airport, Guizhou.  In 1998, it merged into China Southern Airlines.

Shenzhen Bao'an International Airport: Shenzhen Bao'an International Airport (; formerly Shenzhen Huangtian Airport) (IATA: SZX, ICAO: ZGSZ) is located near Huangtian and Fuyong villages in Bao'an District, Shenzhen, Guangdong, China, 32 km northwest of the city center.  It is a hub for Shenzhen Airlines and Shenzhen Donghai Airlines and for cargo airline SF Airlines, and a focus city for China Southern Airlines and Hainan Airlines.  The airport also serves as an Asian-Pacific cargo hub for UPS Airlines.  The airport is undergoing major expansion with a second runway completed and opened in 2011 and a new terminal which opened in 2013.

Guilin: Guilin, formerly romanized as Kweilin, is a prefecture-level city in the northeast of China's Guangxi Zhuang Autonomous Region.  It is situated on the west bank of the Li River and borders Hunan to the north.  Its name means "Forest of Sweet Osmanthus", owing to the large number of fragrant sweet osmanthus trees located in the city.  The city has long been renowned for its scenery of karst topography and is one of China's most popular tourist destinations.

China Southern Airlines Flight 3456: China Southern Airlines Flight 3456 (CZ3456/CSN3456) was a scheduled domestic passenger flight from Chongqing to Shenzhen Huangtian Airport (now Shenzhen Bao'an International Airport), Guangdong, China.  On May 8, 1997, the Boeing 737 performing this route crashed during the second attempt to land in a thunderstorm.

Question: China Southern Airlines Flight 3943 used to fly to an airport in a city situated on the west bank of which river ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "flight_details": {
      "type": "object",
      "properties": {
        "airline": {
          "type": "string",
          "description": "The airline operating the flight."
        },
        "flight_number": {
          "type": "string",
          "description": "The flight number."
        }
      },
      "required": [
        "airline",
        "flight_number"
      ],
      "additionalProperties": false
    },
    "destination_city": {
      "type": "string",
      "description": "The destination city of the flight."
    },
    "associated_river": {
      "type": "string",
      "description": "The name of the river the destination city is situated on."
    }
  },
  "required": [
    "flight_details",
    "destination_city",
    "associated_river"
  ],
  "additionalProperties": false
}
