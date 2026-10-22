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
Yokohama: Yokohama (Japanese: 横浜市 , Hepburn: Yokohama-shi ) is the second largest city in Japan by population, after Tokyo, and the most populous municipality of Japan.  It is the capital city of Kanagawa Prefecture.  It lies on Tokyo Bay, south of Tokyo, in the Kantō region of the main island of Honshu.  It is a major commercial hub of the Greater Tokyo Area.

Japan Airlines: Japan Airlines Co., Ltd. (JAL) (日本航空株式会社 , Nihon Kōkū Kabushiki-gaisha , , OTC Pink: JAPSY) , is the flag carrier airline of Japan and the second largest in the country behind All Nippon Airways.  It is headquartered in Shinagawa, Tokyo, Japan; and its main hubs are Tokyo's Narita International Airport and Tokyo International Airport (Haneda Airport), as well as Osaka's Kansai International Airport and Osaka International Airport.  JAL group companies include Japan Airlines, J-Air, JAL Express, Japan Air Commuter, Japan Transocean Air and Ryukyu Air Commuter for domestic feeder services; and JAL Cargo for cargo and mail services.

Haneda Airport: Tokyo International Airport (東京国際空港 , Tōkyō Kokusai Kūkō ) , commonly known as Haneda Airport (羽田空港 , Haneda Kūkō ) or Tokyo Haneda Airport (IATA: HND, ICAO: RJTT) , is one of the two primary airports that serve the Greater Tokyo Area, and is the primary base of Japan's two major domestic airlines, Japan Airlines (Terminal 1) and All Nippon Airways (Terminal 2), as well as Air Do, Skymark Airlines, Solaseed Air, and StarFlyer.  It is located in Ōta, Tokyo, 14 km south of Tokyo Station.

Tokyo Institute of Technology: Tokyo Institute of Technology (東京工業大学 , Tōkyō Kōgyō Daigaku , informally Tokyo Tech, Tokodai or TITech) is a national research university located in Greater Tokyo Area, Japan.  Tokyo Tech is the largest institution for higher education in Japan dedicated to science and technology, and is generally considered to be one of the most prestigious universities in Japan.

Tokyo Area Control Center: Tokyo Area Control Center (東京航空交通管制部 , "Tōkyō Kōkūkōtsūkanseibu" , "Tokyo Air Traffic Control Center") is an air traffic control center located in the Namiki area of Tokorozawa, Saitama Prefecture, Japan in the Greater Tokyo Area.  The center is north of the special wards of Tokyo.

All Nippon Airways Flight 58: All Nippon Airways (ANA) Flight 58 was a Japanese domestic flight from Sapporo to Tokyo, operated by All Nippon Airways (ANA).  On 30 July 1971, at 2:04 local time, a Japan Air Self-Defense Force (JASDF) jet fighter collided with the Boeing 727 airliner operating the flight, causing both aircraft to crash.  All 162 occupants of the flight were killed, while the Sabre pilot, a trainee with the JASDF, ejected before the collision and survived.  This incident led to the resignation of the head Japan's Defense Agency and the JASDF chief of staff.

All Nippon Airways Flight 533: All Nippon Airways Flight 533, registration JA8658, was a NAMC YS-11 en route from Osaka, Japan, to Matsuyama on the island of Shikoku.  It was the fifth crash in Japan in 1966 and the second one experienced by All Nippon Airways that year, the first being the loss of Flight 60 on February 4.  It was also, at the time, the deadliest crash of an NAMC YS-11, and remains the second-deadliest after Toa Domestic Airlines Flight 63, which crashed in 1971 with 68 deaths.

All Nippon Airways: All Nippon Airways Co., Ltd. (全日本空輸株式会社 , Zen Nippon Kūyu Kabushiki gaisha ) , also known as Zennikkū (全日空 ) or ANA, is the largest airline in Japan.  Its headquarters are located at Shiodome City Center in the Shiodome area of Minato, Tokyo, Japan.  It operates services to both domestic and international destinations and had more than 20,000 employees as of March 2016.  In May 2010, ANA's total passenger traffic was up year-on-year by 7.8%, and its international services grew by 22% to 2.07 million passengers in the first five months of 2010.  ANA's main international hubs are at Narita International Airport outside Tokyo and Kansai International Airport outside Osaka.  Its main domestic hubs are at Tokyo International Airport (Haneda), Osaka International Airport (Itami), Chūbu Centrair International Airport (near Nagoya), and New Chitose Airport (near Sapporo).

Transport in Greater Tokyo: The transport network in Greater Tokyo includes public and private rail and highway networks; airports for international, domestic, and general aviation; buses; motorcycle delivery services, walking, bicycling, and commercial shipping.  While the nexus is in the central part of Tokyo, every part of the Greater Tokyo Area has rail or road transport services.  The sea and air transport is available from a limited number of ports for the general public.

Tokyo: Tokyo (] , ), officially Tokyo Metropolis, is the capital of Japan and one of its 47 prefectures.  The Greater Tokyo Area is the most populous metropolitan area in the world.  It is the seat of the Emperor of Japan and the Japanese government.  Tokyo is in the Kantō region on the southeastern side of the main island Honshu and includes the Izu Islands and Ogasawara Islands.  Formerly known as Edo, it has been the de facto seat of government since 1603 when Shogun Tokugawa Ieyasu made the city his headquarters.  It officially became the capital after Emperor Meiji moved his seat to the city from the old capital of Kyoto in 1868; at that time Edo was renamed Tokyo.  Tokyo Metropolis was formed in 1943 from the merger of the former and the .

Question: All Nippon Airways has a main domestic hubb at what aiport that is one of the two primary airports that serve the Greater Tokyo Area?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "airport_name": {
      "type": "string",
      "description": "The common name of the airport."
    },
    "served_area": {
      "type": "string",
      "description": "The metropolitan area that the airport primarily serves."
    },
    "airline_hub_for": {
      "type": "string",
      "description": "The airline for which this airport is a main domestic hub."
    },
    "is_one_of_primary_airports": {
      "type": "boolean",
      "description": "Indicates if the airport is one of the primary airports serving the specified area."
    },
    "total_primary_airports_in_area": {
      "type": "integer",
      "description": "The total number of primary airports serving the specified area."
    }
  },
  "required": [
    "airport_name",
    "served_area",
    "airline_hub_for",
    "is_one_of_primary_airports",
    "total_primary_airports_in_area"
  ],
  "additionalProperties": false
}
