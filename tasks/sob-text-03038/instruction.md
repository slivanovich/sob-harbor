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
Jalan Tengku Mizan: Jalan Tengku Mizan, Federal Route 65 (formerly Terengganu State Route T4), is a major highway in Kuala Nerus and Kuala Terengganu, Terengganu, Malaysia.  The highway connects Bulatan, Kuala Nerus in the north to Bukit Besar, Kuala Terengganu in the south.  It was named after Yang di-Pertuan Muda (Crown Prince) of Terengganu at that time, Tengku Mizan Zainal Abidin from 1979 to 1998 (now Sultan Mizan Zainal Abidin of Terengganu).  It has been a toll-free highway since toll collection was abolished on 1999.  The highway has a motorcycle lane.  Landmarks along the highway include Sultan Mahmud Bridge and Terengganu Welcome Sign "(Allah Peliharakanlah Terengganu)".

Johor Bahru East Coast Highway: The Johor Bahru East Coast Highway or Johor Bahru–Pasir Gudang Highway, Federal Route 35, is a major highway in Johor Bahru, Johor, Malaysia.  It is a toll free highway and part of the Iskandar Malaysia project.  This 13.4 km (8.3 mile) highway connects Bakar Batu in city centre to the town of Pasir Gudang, and passes through Bandar Baru Permas Jaya and Taman Rinting.  This highway also passes through Permas Jaya Bridge and is the alternative way to Pasir Gudang besides Pasir Gudang Highway.  Johor Bahru East Coast Highway is the fourth east–west-oriented expressway in the Iskandar Malaysia area after the Pasir Gudang Highway, the Pontian–Johor Bahru Link of the Second Link Expressway and the Senai–Desaru Expressway.

Colonial Park Mall: The Colonial Park Mall is a shopping mall located in Lower Paxton Township, Pennsylvania, about 3 mi NE of Harrisburg.  Located at the NE corner of U.S. Route 22 and Colonial Road in the Colonial Park CDP just east of Interstate 83 and south of Interstate 81, it serves the eastern and northern suburbs of the Harrisburg metropolitan area.  Its current anchor stores are The Bon-Ton, Boscov's, and Sears.

Virginia State Route 156: State Route 156 (SR 156) is a primary state highway in the U.S. state of Virginia.  The state highway runs 57.38 mi from U.S. Route 301 (US 301) and SR 35 in Templeton north to US 360 Business in Mechanicsville.  SR 156 follows a circuitous route through the eastern part of the Richmond–Petersburg metropolitan area.  South of the James River, the state highway connects Templeton in Prince George County with Hopewell, which is directly served by SR 156 Business.  SR 156 crosses the James River on the Benjamin Harrison Memorial Bridge and briefly passes through Charles City County.  For most of its length in Henrico and Hanover, the state highway is a rural road that provides access to several units of Richmond National Battlefield Park.  However, SR 156 provides access to Richmond International Airport, Interstate 64, and I-295 as it passes through the Richmond suburbs of Sandston and Highland Springs as a major highway.

Proton City Highway: Proton City Highway, Federal Route 258, is a major highway in Perak, Malaysia.  The 3.8 km (2.4 mi) federal highway connects Tanjung Malim North Interchange of the Tanjung Malim-Slim River Highway (Federal Route 1) to Proton City in the east.  It is a main route to Proton City.  The Kilometre Zero is located at Tanjung Malim North Interchange.

Maryland Route 175: Maryland Route 175 is a state highway in the U.S. state of Maryland.  The highway runs 17.01 mi from Little Patuxent Parkway in Columbia east to MD 3 in Millersville.  MD 175 is a major highway through the large unincorporated community of Columbia; the highway connects U.S. Route 29 (US 29) next to Columbia Town Center with Interstate 95 (I-95) and an industrial area on the eastern side of Howard County.  MD 175 also connects Fort Meade with Jessup and Odenton in western Anne Arundel County, where it links MD 295 and MD 32 with the eastern part of the U.S. Army base.

Colonial Park, Pennsylvania: Colonial Park is an unincorporated community and census-designated place (CDP) in Lower Paxton Township, Dauphin County, Pennsylvania, United States.  The population was 13,229 at the 2010 census.  It is part of the Harrisburg–Carlisle Metropolitan Statistical Area.  It uses the Harrisburg ZIP code of 17109 and hosts a great deal of the area's retail activity, including the Colonial Park Mall.

Interstate 81: Interstate 81 (I-81) is a north–south (physically northeast–southwest) Interstate Highway in the eastern part of the United States.  Its southern terminus is at I-40 in Dandridge, Tennessee; its northern terminus is on Wellesley Island (near Fishers Landing, New York) at the Canadian border, where the Thousand Islands Bridge connects it to Highway 401, the main Ontario freeway connecting Detroit via Toronto to Montreal.  The major metropolitan areas that I-81 connects to include Harrisburg in Pennsylvania and Syracuse in New York.

Iskandar Coastal Highway: The Iskandar Coastal Highway (ICH) (formerly Johor Bahru West Coast Parkway) (Malay: "Lebuhraya Pesisir Pantai Iskandar (LPPI)") or the stretch of road that includes Lebuhraya Sultan Iskandar, Persiaran Sultan Abu Bakar (formerly Jalan Skudai, Jalan Abu Bakar) and Persiaran Sultan Ismail (formerly Jalan Ibrahim and Persiaran Tun Sri Lanang) (Federal Route 52 (Iskandar Puteri–Danga Bay) and Johor State Route 1 (Danga Bay–City Centre)) is a major highway in Iskandar Malaysia, Johor Bahru, Johor, Malaysia.  The 23 km (14 mi) highway connects Iskandar Puteri in the west to Johor Bahru in the east.  It is a toll free highway and part of the Iskandar Malaysia project.  The Iskandar Coastal Highway is the fifth east–west-oriented expressway in the Iskandar Malaysia area after the Pasir Gudang Highway, the Pontian–Johor Bahru Link of the Second Link Expressway, the Senai–Desaru Expressway and the Johor Bahru East Coast Highway.

U.S. Route 17 in Virginia: U.S. Route 17 (US 17) is a part of the U.S. Highway System that runs from Punta Gorda, Florida to Winchester, Virginia.  In Virginia, the U.S. Highway runs 255.83 mi from the North Carolina state line in Chesapeake north to its northern terminus at US 11, US 50, and US 522 in Winchester.  US 17 is a major highway in the eastern half of Virginia.  The U.S. Highway connects the Albemarle Region of North Carolina with the Hampton Roads metropolitan area.  Within the urban area, US 17 passes through the South Hampton Roads cities of Chesapeake, Portsmouth, and Suffolk and the Virginia Peninsula city of Newport News.  Between Yorktown and Fredericksburg, the U.S. Highway serves as the primary highway of the Middle Peninsula.  At Fredericksburg, US 17 leaves the Atlantic coastal plain; the highway passes through the Piedmont town of Warrenton and crosses the Blue Ridge Mountains on its way to Winchester in the Shenandoah Valley. The route from Tappahannock to Winchester roughly follows the Confederate March during the Civil War to Gettysburg

Question: What major highway connects to Harrisburg in Pennsylvania and Syracuse in New York and north of the Colonial Park Mall?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "highway_name": {
      "type": "string",
      "description": "The name of the major highway."
    },
    "highway_type": {
      "type": "string",
      "description": "The type of the highway (e.g., Interstate Highway, Federal Route)."
    },
    "connected_major_areas": {
      "type": "array",
      "description": "A list of major metropolitan areas connected by the highway.",
      "items": {
        "type": "object",
        "properties": {
          "city": {
            "type": "string",
            "description": "The city connected by the highway."
          },
          "state": {
            "type": "string",
            "description": "The state where the city is located."
          }
        },
        "required": [
          "city",
          "state"
        ],
        "additionalProperties": false
      }
    },
    "location_relative_to_colonial_park_mall": {
      "type": "string",
      "description": "The directional relationship of the highway to Colonial Park Mall."
    }
  },
  "required": [
    "highway_name",
    "highway_type",
    "connected_major_areas",
    "location_relative_to_colonial_park_mall"
  ],
  "additionalProperties": false
}
