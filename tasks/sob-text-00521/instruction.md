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
Air Nunavut: Air Nunavut is an airline based in Iqaluit, Nunavut, Canada.  It is the only local and Inuit-owned air carrier in the eastern Arctic, operating MEDEVAC and charter services throughout Canada's Arctic, northern Quebec and Greenland.  Its main base is Iqaluit Airport.

Iqaluit Airport: Iqaluit Airport (IATA: YFB, ICAO: CYFB) serves Iqaluit, Nunavut, Canada and is located adjacent to the town.  It is operated by the government of Nunavut.  It hosts scheduled passenger service from Ottawa, Montreal, Rankin Inlet and Kuujjuaq on carriers such as First Air and Canadian North, and from smaller communities throughout eastern Nunavut.  It is also used as a forward operating base by the CF-18 Hornet.  In 2011, the terminal handled more than 120,000 passengers.

Canadian North: Canadian North Inc. is an airline headquartered in Calgary, Alberta, Canada.  It operates scheduled passenger services to communities in the Northwest Territories and Nunavut.  Southern gateways include Edmonton and Ottawa.  Its main base is Edmonton Airport.

Alberta Citylink: Alberta Citylink was an airline based in Medicine Hat, Alberta, Canada.  It operated domestic passenger service for Air Canada as an Air Canada Connector air carrier via a code sharing agreement.  Its main base was Medicine Hat Airport, with a hub at Calgary International Airport

Lethbridge Airport: The Lethbridge Airport (IATA: YQL, ICAO: CYQL) , previously the Lethbridge County Airport, is located 4 NM south southeast of Lethbridge, Alberta, Canada.  It is 10–15 driving minutes from downtown and has scheduled service to the Alberta cities of Calgary and Edmonton.  The airport is classified as an airport of entry by Nav Canada and is staffed by the Canada Border Services Agency (CBSA).  CBSA officers at this airport can handle general aviation aircraft only, with no more than 15 passengers.  The airport hosts the biennial Lethbridge International Airshow.

Alta Flights: Alta Flights was a charter airline based in Edmonton, Alberta, Canada.  It operated regional passenger and cargo charters throughout Canada and the United States.  Its main base was Edmonton International Airport, with hubs at Edmonton City Centre Airport and at Calgary International Airport.

Edmonton City Centre (Blatchford Field) Airport: Edmonton City Centre (Blatchford Field) Airport (ECCA), (IATA: YXD, ICAO: CYXD) , was located within the city of Edmonton, Alberta, Canada.  It was bordered by Yellowhead Trail to the north, Kingsway to the south, 121 Street to the west, and the Northern Alberta Institute of Technology (NAIT) and Jefferson armouries to the east.  It encompassed approximately 144 acre of land just north of the Edmonton city centre.  The airport was originally named for former mayor Kenneth Alexander Blatchford, then was known as the Edmonton Municipal Airport, then as Edmonton Industrial Airport and then as Edmonton City Centre Airport, finally ending as Blatchford Field at Edmonton City Centre Airport.  In all cases, the three letter "YXD" code continued to be used for the airport by all of the airlines serving the airfield over the years.

First Air: Bradley Air Services Limited, operating as First Air, is an airline headquartered in Kanata, a suburb of Ottawa, Ontario, Canada.  It operates services to 34 communities in Nunavut, Nunavik, and the Northwest Territories.  The majority of its fleet is available for charters worldwide.  First Air has assisted in various humanitarian missions such as the 2010 Haiti earthquake, airlifting relief supplies and equipment.  Its main base, which includes a large hangar, cargo and maintenance facility, is located at Ottawa Macdonald–Cartier International Airport, with hubs at Iqaluit Airport, Rankin Inlet Airport and Yellowknife Airport.

Alberta Highway 2: Alberta Provincial Highway No. 2, commonly referred to as Highway 2 or the Queen Elizabeth II Highway, is a major highway in Alberta, Canada that stretches from the Canada–United States border through Calgary and Edmonton to Grande Prairie.  Running primarily north to south for approximately 1273 km , it is the longest and busiest highway in the province carrying nearly 170,000 vehicles per day in central Calgary.  Between Edmonton and Fort Macleod, the highway forms a portion of Alberta's Export Highway and the CANAMEX Corridor.  More than half of Alberta's 4 million residents live in the Calgary–Edmonton Corridor created by Highway 2.

Frobisher Bay Air Base: Frobisher Bay Air Base is a former United States Air Force facility adjacent to the then town of Frobisher Bay, Northwest Territories (now Iqaluit, Nunavut); 1299 mi north of Ottawa, Ontario.  It was closed in 1963 and became a civilian airport Frobisher Bay Airport (Iqaluit Airport since 1987).

Question:  Iqaluit Airport hosts which airline that is headquartered in Calgary, Alberta, Canada and whose main base is Edmonton Airport?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "airline_name": {
      "type": "string",
      "description": "The name of the airline."
    },
    "headquarters": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the airline is headquartered."
        },
        "province_territory": {
          "type": "string",
          "description": "The province or territory where the airline is headquartered."
        },
        "country": {
          "type": "string",
          "description": "The country where the airline is headquartered."
        }
      },
      "required": [
        "city",
        "province_territory",
        "country"
      ],
      "additionalProperties": false
    },
    "main_base_airport": {
      "type": "string",
      "description": "The name of the airline's main base airport."
    },
    "serves_iqaluit_airport": {
      "type": "boolean",
      "description": "Indicates if the airline hosts services at Iqaluit Airport."
    }
  },
  "required": [
    "airline_name",
    "headquarters",
    "main_base_airport",
    "serves_iqaluit_airport"
  ],
  "additionalProperties": false
}
