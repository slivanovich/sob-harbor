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
WIFR-LD: WIFR-LD is a low-powered CBS-affiliated television station serving Rockford, Illinois, United States.  It broadcasts its digital signal on UHF channel 41 from a transmitter at its studios on North Meridian Road in Rockford.  Until 2017, WIFR operated as a full-power television station licensed to nearby Freeport; until 2009, it broadcast an analog signal on channel 23, which WIFR-LD continues to use as its virtual digital channel via PSIP.  It is owned by Gray Television.  WIFR is the only television station in the Rockford market to retain the same network affiliation since it first signed on.

WGCL-TV: WGCL-TV, virtual channel 46 (UHF digital channel 19), is a CBS-affiliated television station license to Atlanta, Georgia, United States.  The station is owned by the Meredith Corporation as part of a duopoly with independent station WPCH-TV (channel 17).  The two stations share a studio located on 14th Street in northwestern Atlanta; WGCL-TV's transmitter is located near North Druid Hills.  WGCL-TV is the third-largest CBS-affiliated station by market size (WUSA in Washington, D.C. being the largest and KHOU in Houston being the second largest) that is not owned and operated by the network.

Las Vegas: Las Vegas ( , Spanish for "The Meadows"), officially the City of Las Vegas and often known simply as Vegas, is the 28th-most populated city in the United States, the most populated city in the state of Nevada, and the county seat of Clark County.  The city anchors the Las Vegas Valley metropolitan area and is the largest city within the greater Mojave Desert.  Las Vegas is an internationally renowned major resort city, known primarily for its gambling, shopping, fine dining, entertainment, and nightlife.  The Las Vegas Valley as a whole serves as the leading financial, commercial, and cultural center for Nevada.

WBKB-TV: WBKB-TV is the CBS-affiliated television station for the northeastern Lower Peninsula of Michigan in the United States.  Licensed to Alpena, it broadcasts a high definition digital signal on VHF channel 11 (also the station's virtual channel via PSIP) from a transmitter in unincorporated Alcona County (near M-72) south of Hubbard Lake.  On cable, the station can be seen on Charter channel 10 in Standard definition and digital channel 781 in high definition.  Owned by the Marks Radio Group, WBKB has studios on North Bagley Street in Alpena.  WBKB is the only commercial television station in one of the smallest media markets in the United States.

Wyoming Valley: The Wyoming Valley is an historic, industrialized region of Northeastern Pennsylvania once famous for fueling the industrial revolution in the United States with its many anthracite coal mines.  As a metropolitan area, it is known as the Wilkes-Barre/Scranton area, the 97th-largest metropolitan area in the United States and the 4th largest in Pennsylvania.  It is called the "Wilkes-Barre/Scranton Metropolitan Area" after its principal cities, Scranton and Wilkes-Barre, and makes up its own unique physiographic province, the Anthracite Valley in the geology of Pennsylvania.  Greater Pittston makes up the center of the valley.  Scranton is the most populated city in the metropolitan area with a population of 77,114.  The city of Scranton has grown in population after the 2015 mid term census while Wilkes-Barre has declined in population.  Wilkes-Barre is still the second most populated city in the metropolitan area and Hazleton is third.  The airport(s) for this area are Wilkes-Barre/Scranton International Airport (Avoca) and the Wilkes-Barre Wyoming Valley Airport (Forty Fort).

Belleville, Illinois: Belleville (French: "Belle ville", meaning "Beautiful city") is a city in St. Clair County, Illinois, United States, coterminous with the now defunct Belleville Township.  The population was 42,034 according to the Census Bureau's 2015 estimates.  It is the eighth-most populated city outside the Chicago Metropolitan Area and the most populated city south of Springfield in the state of Illinois.  It is the county seat of St. Clair County, and the seat of the Roman Catholic Diocese of Belleville and the National Shrine of Our Lady of the Snows.  Belleville is the most populated city in the Metro-East region of the St. Louis Metropolitan Area and in Southern Illinois.  Due to its proximity to Scott Air Force Base, the population receives a boost from military and federal civilian personnel, defense contractors, and military retirees.

KWTV-DT: KWTV-DT, virtual channel 9 (UHF digital channel 39), is a CBS-affiliated television station licensed to Oklahoma City, Oklahoma, United States.  It is the flagship television station of locally based Griffin Communications, and is part of a duopoly with MyNetworkTV affiliate KSBI (channel 52).  The two stations share studio facilities located on Kelley Avenue (adjacent to the studios and main offices of the state's PBS member network, the Oklahoma Educational Television Authority [OETA]), and its transmitter facilities are located near the John Kilpatrick Turnpike on the city's northeast side.

KUTV: KUTV, virtual channel 2 (UHF digital channel 34), is a CBS-affiliated television station located in Salt Lake City, Utah, United States.  The station is owned by the Sinclair Broadcast Group, as part of a triopoly with independent station KJZZ-TV (channel 14) and St. George-licensed MyNetworkTV affiliate KMYU (channel 12, formerly solely a satellite station KUTV from its 1999 sign-on to 2008).  KUTV and KMYU share studio facilities located on South Main Street in downtown Salt Lake City, and its transmitter is located at Farnsworth Peak in the Oquirrh Mountains, southwest of Salt Lake City.

KLFY-TV: KLFY-TV, virtual and VHF digital channel 10, is the CBS-affiliated television station in Lafayette, Louisiana, United States.  Its transmitter is located north of Rayne, Louisiana.  Its original 1800 ft tower was located just north of Crowley near the small town of Maxie.  The original tower was shortened to 1100 ft in the late 2000s due to mechanical issues.  The station is owned by the Nexstar Media Group and is the oldest television station in the Lafayette area.

KLAS-TV: KLAS-TV, virtual channel 8 (VHF digital channel 7), is a CBS-affiliated television station located in Las Vegas, Nevada, United States.  The station is owned by Nexstar Media Group.  KLAS-TV's studios are located at 3228 Channel 8 Drive near the northern portion of the Las Vegas Strip in the unincorporated community of Winchester (though with a Las Vegas address) and its transmitter is located on Mount Arden in Henderson.

Question: Which CBS-affiliated television station is located on the 28th-most populated city in the United States, the most populated city in the state of Nevada?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "station_name": {
      "type": "string",
      "description": "The name of the television station."
    },
    "network_affiliation": {
      "type": "string",
      "description": "The network the station is affiliated with."
    },
    "location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the station is located."
        },
        "state": {
          "type": "string",
          "description": "The state where the station is located."
        },
        "city_us_population_rank": {
          "type": "integer",
          "description": "The population rank of the city in the United States."
        },
        "city_state_population_description": {
          "type": "string",
          "description": "Description of the city's population rank within its state."
        }
      },
      "required": [
        "city",
        "state",
        "city_us_population_rank",
        "city_state_population_description"
      ],
      "additionalProperties": false
    },
    "owner": {
      "type": "string",
      "description": "The company that owns the television station."
    },
    "virtual_channel": {
      "type": "integer",
      "description": "The virtual channel number of the station."
    }
  },
  "required": [
    "station_name",
    "network_affiliation",
    "location",
    "owner",
    "virtual_channel"
  ],
  "additionalProperties": false
}
