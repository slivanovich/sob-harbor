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
Great Lakes Airport: Great Lakes Airport also known as Kepper Field (ICAO: YGRL) is a private airport located approximately 6 km north of the town of Lakes Entrance in eastern Victoria, Australia.  The airport was officially opened on 2 November 2003 and is capable of operating 24 hours.  The airport facilities are designed to handle transport category aircraft, although there is no regular passenger service.

Fukue Airport: Fukue Airport (福江空港 , Fukue Kūkō ) (IATA: FUJ, ICAO: RJFE) , is a third class airport located 1.7 NM southwest of Gotō, Nagasaki Prefecture, off the western coast of Kyūshū, Japan.  The airport also serves the city of Fukue.  It is also known as Gotō-Fukue Airport (五島福江空港 , Gotō Fukue Kūkō ) .

San Angelo Regional Airport: San Angelo Regional Airport (IATA: SJT, ICAO: KSJT, FAA LID: SJT) , also known as Mathis Field, is a public airport serving the city of San Angelo, in Tom Green County, Texas, USA.  The airport covers 1503 acre and has three runways.  The airport also offers free parking.

Sam Mbakwe Airport: Sam Mbakwe International Cargo Airport (IATA: QOW, ICAO: DNIM) , also known as Imo State Airport, serves Owerri, the capital city of Imo State in southeastern Nigeria.  Owerri is one of the fastest growing, developing cities after Lagos and Abuja in Nigeria.  Other cities served by the airport are, the commercial city of Onitsha, automobile and manufacturing city of Nnewi in Anambra State, the industrial hub of Aba, Umuahia and Arochukwu in Abia State.  Others are Okigwe, Oguta, and Orlu business districts in Imo State.  The airport also serves some parts of Akwa Ibom and Cross River States in the South South part of Nigeria.

Mineola Airport: Mineola–Wisener Field Airport (FAA LID: 3F9) , a privately-owned public use airport also known as the Mineola Airport and Wisener Field, was established in 1917.  It has been under continuous operation by the same family since 1926.  It is considered the oldest privately operated public use airport in the state of Texas.  The field has been designated by the Texas Historical Commission as a Texas Treasure Business.

Minneapolis–St. Paul Airport Trams: The Minneapolis–St. Paul Airport Trams consist of a pair of cable-drawn automated people movers that serve travelers of the Minneapolis–Saint Paul International Airport.  Both were constructed by the Poma-Otis Transit Company of Farmington, Connecticut and are operated under the direction of the Metropolitan Airports Commission.

Bahir Dar Airport: Bahir Dar Airport (IATA: BJR, ICAO: HABD) , also known as Ginbot Haya Airport, is an airport serving Bahir Dar, the capital city of the Amhara Region in Ethiopia.  The name of the city and airport may also be transliterated as Bahar Dar.  The airport is located 8 km west of Bahir Dar, near Lake Tana. The airport also serves the Ethiopian Air Force.

Minneapolis–Saint Paul International Airport: Minneapolis–Saint Paul International Airport (IATA: MSP, ICAO: KMSP, FAA LID: MSP) , also known as Wold–Chamberlain Field, is a joint civil-military public use international airport.  Located in a portion of Hennepin County, Minnesota, United States, outside of any city or school district, within 10 miles (16 km) of both downtown Minneapolis and downtown Saint Paul, it is the largest and busiest airport in the six-state Upper Midwest region of Minnesota, Iowa, Nebraska, North Dakota, South Dakota, and Wisconsin.

Jewel Changi Airport: Jewel Changi Airport also known as Project Jewel is a mixed-use airport terminal complex currently under construction in Singapore Changi Airport, at an estimated cost of S$1.7 billion.  It is located at the heart of the airport, around Changi Airport Terminals 1 to 3.  The site was previously an open-air car park for Terminal 1.  It will feature leisure attractions, retail offerings, hotel and airport operations.

Kalibo International Airport: Kalibo International Airport (Aklanon: "Pangkalibutan nga Paeoparan it Kalibo", Hiligaynon: "Pangkalibutan nga Hulugpaan sang Kalibo" , Filipino: "Paliparang Pandaigdig ng Kalibo" ) (IATA: KLO, ICAO: RPVK) is an airport that serves the general area of Kalibo, the capital of the province of Aklan in the Philippines, and is one of two airports serving Boracay, the other being Godofredo P. Ramos Airport also known as  Caticlan Airport in the town of Malay.  It is the fastest growing airport in the Philippines in terms of passenger traffic with more than 50% growth in 2010, and 2nd fastest for seats offered for June 2014 over the corresponding month of the previous year (20%).  The airport is classified as an international airport by the Civil Aviation Authority of the Philippines, a body of the Department of Transportation and Communications responsible for the operations of all airports in the Philippines except major international airports.

Question: The Minneapolis-St. Paul Airport Trams and the airport also known as World Chamberlain Field were both constructed by whom?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "first_entity": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "constructor": {
          "type": "string"
        }
      },
      "required": [
        "name",
        "constructor"
      ],
      "additionalProperties": false
    },
    "second_entity": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "other_names": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "constructor": {
          "type": "string"
        }
      },
      "required": [
        "name",
        "other_names"
      ],
      "additionalProperties": false
    },
    "common_constructor_identified": {
      "type": "boolean"
    },
    "identified_constructor": {
      "type": "string"
    }
  },
  "required": [
    "first_entity",
    "second_entity",
    "common_constructor_identified"
  ],
  "additionalProperties": false
}
