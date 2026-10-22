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
Braeburn Lodge: Braeburn Lodge is a roadhouse on the Klondike Highway in the Yukon Territory of Canada.  It is located east of Braeburn Lake and north of Braeburn Mountain, on the path of the former Dawson Overland Trail, which was built in 1902 between Whitehorse and Dawson City.  The lodge itself is a tourist destination and is famous for its large cinnamon buns.  Nearby Cinnamon Bun Airport is named for the lodge's cinnamon buns.  Every February, Braeburn Lodge hosts a checkpoint of the long-distance Yukon Quest sled dog race.

Alaska Highway: The Alaska Highway (also known as the Alaskan Highway, Alaska-Canadian Highway, or ALCAN Highway) was constructed during World War II for the purpose of connecting the contiguous United States to Alaska across Canada.  It begins at the junction with several Canadian highways in Dawson Creek, British Columbia, and runs to Delta Junction, Alaska, via Whitehorse, Yukon.  Completed in 1942 at a length of approximately 2700 km , as of 2012 it is 2232 km long.  The difference in distance is due to constant reconstruction of the highway, which has rerouted and straightened out numerous sections.  The highway was opened to the public in 1948.  Legendary over many decades for being a rough, challenging drive, the highway is now paved over its entire length.

Canol pipeline: The Canol pipeline was built to carry crude oil from Norman Wells, Northwest Territories, in Canada to Alaska, USA, during World War II.  The routing was to Johnson Crossing and then along the Alaska highway to Whitehorse, Yukon, where a refinery was built.

Kentucky Route 212: Kentucky Route 212 (KY 212) is a short state highway located in Boone County, in the northern region of the U.S. state of Kentucky.  The highway is approximately 1.3 mi long, and partially constructed as a freeway, with the rest being a divided highway.  The roadway links Interstate 275 (I-275) to the Cincinnati/Northern Kentucky International Airport (CVG Airport), and has been designated as a connector route by the Federal Highway Administration (FHWA).  A road first appeared near the location of KY 212 around 1937.  A short road was built in the location of KY 212 when the U.S. Army Air Corps built the predecessor to the CVG Airport.  The road was reconstructed to a divided highway in 1972, and has remained relatively unchanged since.

Ross River, Yukon: Ross River is an unincorporated community in Yukon, Canada.  It lies at the junction of the Ross River and the Pelly River, along the Canol Road, not far from the Campbell Highway.  Primary access to the Campbell Highway is via a nine-mile access road.  Formerly it was accessed along a six-mile Canol Road section that is no longer maintained.  It is serviced by Ross River Airport, used mainly for charter and scheduled flights to and from Whitehorse and Watson Lake.

Saskatchewan Highway 35: Highway 35 is a paved undivided provincial highway in the Canadian province of Saskatchewan.  It runs from the US Border near Port of Oungre (where it meets United States Route 85) to a dead end near the north shore of Tobin Lake.  Saskatchewan Highway 35 is about 540 km long.  The CanAm Highway comprises Saskatchewan Highways 35, SK Hwy 39, SK Hwy 6, SK Hwy 3, SK Hwy 2 and U.S. Route 85.  46.5 mi of SK Hwy 35 contribute to the CanAm Highway between Port of Oungre on the Canada – United States border and Weyburn.  Mudslides, and spring flooding were huge road building and maintenance problems around Nipawin as well as along the southern portion of the route named the "Greater Yellow Grass Marsh".  Over 20 early dams were built until the problem was addressed with the Rafferty-Alameda Project on the Souris River and the construction of the Qu'Appelle River Dam which have helped to eliminate washed out roads and flooded communities.  The highway through the homesteading community followed the Dominion Land Survey on the square until reaching the Saskatchewan River at Nipawin.  The completion of the combined railway and traffic bridge over the Saskatchewan River at Nipawin in the late 1920s retired the ferry and basket crossing for traffic north of Nipawin.  The E.B. Campbell Dam built in 1963 northeast of Nipawin created Tobin Lake, and Codette Lake was formed with the construction of the Francois-Finlay Hydroelectric dam at Nipawin.  The railway/traffic bridge that formed part of Highway 35 was the only crossing utilized at Nipawin until a new traffic bridge was constructed in 1974.  The new bridge then became part of the combined Highway 35 and 55 until the highway parts just east of White Fox.  Highway 35 then continued north along the west side of Tobin Lake.  The railway/traffic bridge continues to be utilized for one lane vehicle traffic controlled by traffic lights, and continues as the "old highway 35" on the west side of the river until it joins with the current Highway 35/55.

RN-5 (Autopista Comalapa): The RN-5 (Autopista Comalapa, Boulevard Los Proceres) serves as one of the main highways in the Metropolitan Area of San Salvador.  The highway connects the metropolitan area with the El Salvador International Airport, located in San Luis Talpa, La Paz, a municipality that borders with the San Salvador Department.  The highway was built to replace the old "Carretera al Aeropuerto", a small road that runs on the side of a mountain range, parallel to the "Autopista Comalapa".  This road has been turned into a scenic road.  It overlooks the new RN-5 and the southern hills of the San Salvador Department.  The total length of the highway is 40.7 km .  It is currently the only highway that connects to the airport coming from the metropolitan area.  Other highways connect with the RN-5 to provide connection to the other departments in the country.  The construction of the first Carretera a Comalapa was made in 1980.  The construction of the highway began in 2001 and it was completed and inaugurated on November 22, 2002.  The part of the highway known as "Boulevard de Los Proceres" runs through the southern side of the city of San Salvador.  The highway is also a vital area in the city.  It connects with various restaurants, business centers, and other dealerships.

Erik Nielsen Whitehorse International Airport: Erik Nielsen Whitehorse International Airport (IATA: YXY, ICAO: CYXY) is located in Whitehorse, Yukon, Canada.  It is part of the National Airports System, and is owned and operated by the Government of Yukon.  The airport was renamed in honour of longtime Yukon Member of Parliament Erik Nielsen on December 15, 2008.  The terminal handled 294,000 passengers in 2012, representing a 94% increase in passenger traffic since 2002.  Air North is based in Whitehorse.

Whitehorse/Cousins Airport: Whitehorse/Cousins Airport (TC LID: CFP8) is an unpaved airstrip located in Whitehorse, Yukon, Canada, 8 NM northwest of the city centre between the Alaska Highway and the Yukon River.  This airport has no services at all, and is used primarily as an emergency landing area and for local pilot training.  Vehicles enter via Cousins Access Road.  The airport was built to support the Alaska Highway construction and the Northwest Staging Route.

Braeburn Airport: Braeburn Airport, also known as the Cinnamon Bun Airstrip, (TC LID: CEK2) in the Yukon, Canada, is adjacent to the Klondike Highway between Whitehorse and Carmacks.  It is next to Braeburn Lodge (famous for its oversized cinnamon buns and sandwiches) and near Braeburn Lake.  It receives no maintenance and pilots are advised to use caution as there are numerous holes in the runway caused by gophers.

Question: How long is the highway Whitehorse/Cousins Airport was built to support as of 2012?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "highway_name": {
      "type": "string",
      "description": "The name of the highway."
    },
    "supported_airport_name": {
      "type": "string",
      "description": "The name of the airport built to support the highway."
    },
    "length_km": {
      "type": "number",
      "description": "The length of the highway in kilometers."
    },
    "length_as_of_year": {
      "type": "integer",
      "description": "The year for which the highway length is specified."
    }
  },
  "required": [
    "highway_name",
    "supported_airport_name",
    "length_km",
    "length_as_of_year"
  ],
  "additionalProperties": false
}
