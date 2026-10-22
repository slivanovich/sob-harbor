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
Deadhorse Airport: Deadhorse Airport (IATA: SCC, ICAO: PASC, FAA LID: SCC) is a public airport located in Deadhorse on the North Slope of Alaska.  It can be accessed from Fairbanks via the Elliott and Dalton highways.  It is near Prudhoe Bay and is sometimes also called Prudhoe Airport.

Everts Air Cargo: Everts Air Cargo is an American Part 121 airline based in Fairbanks, Alaska, USA.  It operates D.O.D, scheduled and charter airline cargo within Alaska, Canada, Mexico and continental US Its Maintenance base is Fairbanks International Airport with its major cargo hub at Ted Stevens Anchorage International Airport.

Sagavanirktok River: The Sagavanirktok River or Sag River is a stream in the North Slope Borough of the U.S. state of Alaska.  It is about 180 mi long and originates on the north slope of the Brooks Range, flowing north to the Beaufort Sea near Prudhoe Bay.  The Trans-Alaska Pipeline System and Dalton Highway roughly parallel it from Atigun Pass to Deadhorse.  Also, a glaciation happened approximately at the same time as the Illinoian Stage of central North America at the Sagavanirktok River.

KZZ53: KZZ53 (sometimes referred to as Barrow All Hazards) is a NOAA Weather Radio station that serves the Barrow, Alaska area.  It is programmed from the National Weather Service Forecast Office in Fairbanks.  The station broadcasts weather and hazard information for the North Slope Borough in the North Slope Region in Northern Alaska.  The County Coverage (SAME/FIPS Code) for the borough is: 002185.  It is the northernmost NOAA Weather Radio station transmitter in Alaska, the United States and in North America.

Deadhorse, Alaska: Deadhorse is an unincorporated community in North Slope Borough, Alaska, United States, along the North Slope near the Arctic Ocean.  The town consists mainly of facilities for the workers and companies that operate at the nearby Prudhoe Bay oil fields.  Deadhorse is accessible via the Dalton Highway from Fairbanks, 495 miles south, or Deadhorse Airport.  Limited accommodations are also available for tourists.

Fairbanks International Airport: Fairbanks International Airport (IATA: FAI, ICAO: PAFA, FAA LID: FAI) is a state-owned public-use airport located three miles (5 km) southwest of the central business district of Fairbanks, a city in the Fairbanks North Star Borough of the United States state of Alaska.  Fairbanks is the smallest city in the United States with non-stop service to Europe, as Condor offers weekly flights to Frankfurt during the summer tourist season.  In addition, Air North is another international airline with flights (to Canada) and Antonov Airlines offers cargo flights to South Korea.

Barter Island LRRS Airport: Barter Island LRRS Airport (IATA: BTI, ICAO: PABA, FAA LID: BTI) is a public/military airport located near the city of Kaktovik on Barter Island, in the North Slope Borough, located 312 mi east of Point Barrow, Alaska.  The airport is owned by the North Slope Borough.  It is also known as Barter Island Airport or Kaktovik Airport.  The acronym LRRS stands for "Long Range Radar Site" or "Long Range Radar Station".

Dalton Highway: The James W. Dalton Highway, usually referred to as the Dalton Highway (and signed as Alaska Route 11), is a 414 mi road in Alaska.  It begins at the Elliott Highway, north of Fairbanks, and ends at Deadhorse near the Arctic Ocean and the Prudhoe Bay oil fields.  Once called the North Slope Haul Road (a name by which it is still sometimes known), it was built as a supply road to support the Trans-Alaska Pipeline System in 1974.  It is named after James Dalton, a lifelong Alaskan and an engineer who supervised construction of the Distant Early Warning Line in Alaska and, as an expert in Arctic engineering, served as a consultant in early oil exploration in northern Alaska.  It is also the subject of the second episode of "America's Toughest Jobs" and the first episode of the BBC's "World's Most Dangerous Roads".

Everts Air: Everts Air is an American airline based in Fairbanks, Alaska, USA.  It operates scheduled and charter airline cargo as well as passenger services within Alaska and Canada.  Its main base is Fairbanks International Airport with its major hub at Ted Stevens Anchorage International Airport.

Binky (polar bear): Binky (1975 – July 20, 1995) was a polar bear who lived at the Alaska Zoo in Anchorage.  He was originally orphaned near Cape Beaufort, close to the Chukchi Sea, but was found by a driller in Northwest Alaska named David Bergsrud.  The area where Binky was located is known to those living outside of Alaska as the North Slope.  Alaska Fish and Game was contacted shortly after Binky's discovery, and arrangements were being made to find a zoo in the Lower 48.  Anchorage had a small zoo at the time, with an elephant that a lady had won and a few other animals.  When word got around that a polar bear cub had been found, folks started hunting for ways to stall the effort of sending Binky outside of Alaska.  Time was needed to find a sponsor to fund an enclosure at the Alaska Children's Zoo for Binky.  Alaska Fish and Game employees came up with the idea of flying Binky to a number of the inland North Slope villages.  School was let out in these villages so all the children could come to the airstrips to see Binky.  These received major news coverage.  Finally things fell into place to allow the Anchorage zoo to take Binky.  Binky quickly became one of its most popular attractions.  He became a local hero and received international news coverage after mauling two zoo visitors in separate incidents in 1994.  Binky died in 1995 from sarcocystosis, a parasitic disease.

Question: Are Fairbanks International Airport and Deadhorse Airport both located on the North Slope of Alaska?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_asked": {
      "type": "string",
      "description": "The original question posed."
    },
    "airport_locations": {
      "type": "array",
      "description": "Details about the location of each airport mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "airport_name": {
            "type": "string",
            "description": "The name of the airport."
          },
          "is_on_north_slope": {
            "type": "boolean",
            "description": "True if the airport is located on the North Slope of Alaska, false otherwise."
          },
          "stated_location": {
            "type": "string",
            "description": "The specific location information provided for the airport in the context."
          }
        },
        "required": [
          "airport_name",
          "is_on_north_slope",
          "stated_location"
        ],
        "additionalProperties": false
      }
    },
    "both_on_north_slope": {
      "type": "boolean",
      "description": "The final answer to whether both airports are located on the North Slope of Alaska."
    }
  },
  "required": [
    "question_asked",
    "airport_locations",
    "both_on_north_slope"
  ],
  "additionalProperties": false
}
