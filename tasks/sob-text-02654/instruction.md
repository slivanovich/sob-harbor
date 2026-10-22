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
Beirut Air Base: Beirut Air Base (Arabic: قاعدة بيروت الجوية‎ ‎ "Kaidat Bayrut al-jawiya") is a military base owned by the Lebanese Armed Forces and operated by the Lebanese Air Force.  It is located 9 km (5.6 mi) from the city center in the southern suburbs of Beirut, Lebanon.

Bourj el-Barajneh: Bourj el-Barajneh (Arabic: برج البراجنة‎ ‎ , ""Tower of Towers"") is a municipality located in the southern suburbs of Beirut, in Lebanon.  The municipality lies between Beirut–Rafic Hariri International Airport and the town of Haret Hreik.

Al-Mabarrah: Al-Mabarrah (Arabic: المبرة‎ ‎ ) is a Lebanese football club from Beirut which competes in the Lebanese Premier League.  It was founded in 1980, and played in friendly tournaments.  In 1987 Al-Mabarra joined the Lebanese Football Federation, putting a strong team.  They took top positions in Divisions four, three and two and qualified for the Premier league, winning the Lebanese FA Cup in 2007–08 for the first time in the club's history.  The club has its own stadium called Mebarra Stadium on the Airport Road in the Southern suburbs of Beirut.  Al Mabarra enjoys great popularity and supported by many institutions and charity organizations, which constitute the core of the club.  Its membership and fans reach many parts of Lebanon most notably the southern suburbs near Beirut, the Bekaa Valley and North Lebanon.  The club is sponsored by Jammal Trust Bank.

Rabah Bitat Airport: Rabah Bitat Airport (IATA: AAE, ICAO: DABB) , formerly known as Les Salines Airport, and popularly as El Mellah Airport is an international airport located 9 km south of Annaba, a city in Algeria.  It is named after Rabah Bitat, a president of Algeria (1978-1979).

Ramlet al-Baida: Ramlet al-Baida is a public beach in Beirut, Lebanon.  The beach is situated along the southern end of the Corniche Beirut promenade where Avenue General de Gaulle meets Avenue Rafic Hariri and ends at Rue Venezuela.  Despite the beach's location in the upscale district of Ras Beirut, the beach is popular with a predominately male clientele from Beirut's low-income southern suburbs.  The beach is also a popular gay, cruising area.

Nîmes–Alès–Camargue–Cévennes Airport: Nîmes Airport or Nîmes–Alès–Camargue–Cévennes Airport (French: "Aéroport de Nîmes-Alès-Camargue-Cévennes" ) (IATA: FNI, ICAO: LFTW) is an airport located 9 km south-southeast of the city of Nîmes, in the village of Saint-Gilles near Garons.  It is also known as Garons Airport or Nîmes Garons Airport.  The airport serves the Provence region, including the communes of Nîmes and Alès in the Gard department, the Camargue area and the Cévennes.

Wings of Lebanon: Wings of Lebanon is a privately held Lebanese airline, owned by the Nakhal group, which in July 2016 expanded its business model from pure charter operations to include largely seasonal scheduled international passenger services from its main base at Beirut Rafic Hariri International Airport.  The carrier has historically operated one Boeing 737-300, but has expanded its operations using a variety of wet-leased Boeing 737 aircraft as well as Airbus 319 and 321.

Beirut–Rafic Hariri International Airport: Beirut–Rafic Hariri International Airport (Arabic: مطار بيروت رفيق الحريري الدولي‎ ‎ , "Maṭār Bayrūt Rafīq al-Ḥarīrī ad-Dwaliyy") (French: "Aéroport international de Beyrouth" ) (IATA: BEY, ICAO: OLBA ), formerly Beirut International Airport, is located 9 km from the city center in the southern suburbs of Beirut, Lebanon, and is the only operational commercial airport in the country.  It is the hub for Lebanon's national carrier, Middle East Airlines (more commonly known as "MEA").  It is also the hub for the Lebanese cargo carrier Trans Mediterranean Airways (more commonly known as "TMA Cargo"), as well as the charter carriers Med Airways and Wings of Lebanon.

Shaoyang Wugang Airport: Shaoyang Wugang Airport (IATA: WGN, ICAO: ZGSY) is an airport serving the city of Shaoyang in Hunan Province, China.  It is located 9 km north of Wugang, a county-level city under the administration of Shaoyang, and 100 km from the urban center of Shaoyang.  The airport received approval from the State Council of China and the Central Military Commission in July 2013.  It is expected to cost 957 million yuan to build.  The airport was opened on 28 June 2017, with an inaugural China Southern Airlines flight from Changsha Huanghua International Airport.

Mianyang Nanjiao Airport: Mianyang Nanjiao Airport () (IATA: MIG, ICAO: ZUMY) is an airport serving the city of Mianyang in Sichuan Province, China.  It is located in the southern suburbs of Mianyang (Nanjiao means "southern suburbs" in Chinese), 10 kilometers from the city center.

Question: Which Nakhal group owned airline is based at an airport located located 9 km from the city center in the southern suburbs of Beirut, Lebanon?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "airline_name": {
      "type": "string",
      "description": "The name of the airline."
    },
    "owner_group": {
      "type": "string",
      "description": "The group that owns the airline."
    },
    "airport_details": {
      "type": "object",
      "properties": {
        "airport_name": {
          "type": "string",
          "description": "The name of the airport where the airline is based."
        },
        "location_description": {
          "type": "string",
          "description": "A description of the airport's location relative to the city center."
        },
        "distance_from_city_center_km": {
          "type": "integer",
          "description": "The distance of the airport from the city center in kilometers."
        },
        "city": {
          "type": "string",
          "description": "The city where the airport is located."
        },
        "country": {
          "type": "string",
          "description": "The country where the airport is located."
        },
        "is_commercial_airport": {
          "type": "boolean",
          "description": "Indicates if the airport is a commercial airport."
        }
      },
      "required": [
        "airport_name",
        "location_description",
        "distance_from_city_center_km",
        "city",
        "country",
        "is_commercial_airport"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "airline_name",
    "owner_group",
    "airport_details"
  ],
  "additionalProperties": false
}
