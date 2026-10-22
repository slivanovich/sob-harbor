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
Eugene Airport: Eugene Airport (IATA: EUG, ICAO: KEUG, FAA LID: EUG) , also known as Mahlon Sweet Field, is a public airport 7 miles (11 km) northwest of Eugene, in Lane County, Oregon.  Owned and operated by the City of Eugene, it is the fifth-largest airport in the Pacific Northwest.  The terminal building has "A" gates on the upper level and "B" gates, ticketing, and baggage claim on the lower level.  The airport has an expanded air cargo facility and three fixed-base operators (FBOs) to handle general aviation.  In 2015, the Eugene Airport handled 909,121 passengers and 59,961 aircraft movements.

Teslin River, Yukon: Teslin River is an unincorporated area in the Yukon Territory, Canada, located on the west bank of the Teslin River at a crossing of that river on the Alaska Highway, about 40 km northwest of the Village of Teslin (Teslin Post), which is on the east shore of Teslin Lake as is the neighbouring community of Teslin Lake.  The settlement of Johnsons Crossing is on the east bank at that point, while the lake and community of Little Teslin Lake is located farther along the highway about 10 km west.

Sydney Airport: Sydney (Kingsford Smith) Airport (colloquially Mascot Airport, Kingsford Smith Airport, or Sydney Airport; IATA: SYD, ICAO: YSSY ; ) is an international airport in Sydney, Australia located 8 km (5 mi) south of Sydney city centre, in the suburb of Mascot.  It is the primary airport serving Sydney, and is a primary hub for Qantas, as well as a secondary hub for Virgin Australia and Jetstar Airways.  Situated next to Botany Bay, the airport has three runways, colloquially known as the east–west, north–south and third runways.

Rambleridge Park: Rambleridge Park was developed in the late 1970s at 11424 Fort Street in Omaha, Nebraska.  The park includes a lagoon, walking trails, soccer fields and a large green space for miscellaneous activities.  A small playground is located farther in the neighborhood and can be reached after a short walk.  The park and green spaces throughout the neighborhood are maintained by the City of Omaha and the residents of the neighborhood.

Merle K. (Mudhole) Smith Airport: Merle K. (Mudhole) Smith Airport (IATA: CDV, ICAO: PACV, FAA LID: CDV) is a state owned, public use airport located 11 nautical miles (13 mi, 20 km) southeast of the central business district of Cordova, a city in the Valdez-Cordova Census Area of the U.S. state of Alaska which has no road access to the outside world.  Airline service is subsidized by the Essential Air Service program.

Serra Springs (California): Serra Springs are a pair of springs located on the campus of University High School in Los Angeles, California, USA.  They are designated by California Historical Landmark #522.  The springs, called Kuruvungna by the native Gabrieleno Tongva people, were used as a source of natural fresh water by the Tongva people since at least the 5th century BC and continue to produce 22,000-25,000 gallons of water a day.  The springs are also sometimes referred to as the Gabrieleno Tongva Springs, the Tongva Holy Springs, and the Sacred Springs.  The springs are found at two separate locations on the high school campus.  The larger is now closed off from the rest of the campus and is under the care of the Gabrielino/Tongva Springs Foundation.  The other spring is located on the northeastern edge of the so-called Girls' Field.  A third spring was located farther north, near Texas Avenue, but it ceased to flow during the 1940s when a local water company began drawing from the aquifer.

Akkanapuram: Akkanapuram is a village located in Watrap Block, Srivilliputhur Taluk,Virudhunagar district, Tamil Nadu State, India.  The village is identified by two names Akkanapuram Villaku and the Akkanapuram itself.  The village naming difference arrised only because of the bus stop junction , because most of the bus does not transport passengers into the village , they just drop them at the 3 way junction akkanpuram villaku (SH - 182).  the west side road of the village reaches to the town Watrap and east side road of the village reaches to Alagapuri , at that junction it crosses at (NH -208 ) and again continues till virudhunagar.  the northside road of the village goes to Periayur.The closest city is Madurai, and nearest towns are Watrap (12 kilometres),Srivilliputhur (21 kilometres), Pallapatti (27 kilometres), Virudhunagar (28 kilometres) and Sivakasi (29 kilometres).  Also, the closest airport is Madurai Airport which is 50 kilometres away.  Most of the people that live in the village are Paraiyar and are farmers.

Konoplev (crater): Konoplev is a small lunar crater that is located on the Moon's far side.  It lies less than a crater diameter to the west of the satellite crater Ellerman Q. Ellerman itself is located farther to the northeast.  To the north-northeast of Konoplev is the larger crater Gerasimovich.

Flight Patterns: Flight Patterns, also known informally as Flying People, is a seven-panel photographic sculpture installation by David Joyce, designed to be installed in 1989 in Concourse A at the Eugene Airport in the U.S. state of Oregon.  During airport construction in 2015–2016, it was moved to Lane Community College.  The airport renovations were completed by early January 2017, but the airport management is studying how public art will be displayed, and has not decided yet whether Flight Patterns will be reinstalled.

Velika Kladuša: Velika Kladuša (] ) is a town and municipality in the far northwest of Bosnia and Herzegovina, located near the border with Croatia.  The closest city is Cazin, and a bit farther, the cities of Bihać and Bosanski Novi.  Across the border, it is not far from Cetingrad.  Administratively, it is part of the Una-Sana Canton of the Federation of Bosnia and Herzegovina.

Question: Which of both airports; Eugene Airport and Merle K. Smith Airport, is located farther from its closest city? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "comparison_successful": {
      "type": "boolean",
      "description": "Indicates if a comparison between the two airports' distances to their closest cities was possible."
    },
    "airport_farther": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the airport that is farther from its closest city."
        },
        "iata_code": {
          "type": "string",
          "description": "The IATA code of the airport."
        },
        "closest_city": {
          "type": "string",
          "description": "The closest city to this airport."
        },
        "distance_to_city_miles": {
          "type": "integer",
          "description": "The distance from the airport to its closest city in miles."
        },
        "distance_to_city_km": {
          "type": "integer",
          "description": "The distance from the airport to its closest city in kilometers."
        }
      },
      "required": [
        "name",
        "iata_code",
        "closest_city",
        "distance_to_city_miles",
        "distance_to_city_km"
      ],
      "additionalProperties": false
    },
    "airport_closer": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the airport that is closer to its closest city."
        },
        "iata_code": {
          "type": "string",
          "description": "The IATA code of the airport."
        },
        "closest_city": {
          "type": "string",
          "description": "The closest city to this airport."
        },
        "distance_to_city_miles": {
          "type": "integer",
          "description": "The distance from the airport to its closest city in miles."
        },
        "distance_to_city_km": {
          "type": "integer",
          "description": "The distance from the airport to its closest city in kilometers."
        }
      },
      "required": [
        "name",
        "iata_code",
        "closest_city",
        "distance_to_city_miles",
        "distance_to_city_km"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "comparison_successful",
    "airport_farther",
    "airport_closer"
  ],
  "additionalProperties": false
}
