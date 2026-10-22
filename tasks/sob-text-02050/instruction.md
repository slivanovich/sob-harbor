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
Leavenworth, Kansas: Leavenworth is the largest city in and the county seat of Leavenworth County, Kansas, United States.  As of the 2010 census, the city population was 35,251.  Located on the west bank of the Missouri River 25 mi northwest of Kansas City, Missouri, it is part of the Kansas City metropolitan area.

Boyer Chute National Wildlife Refuge: Boyer Chute National Wildlife Refuge, created in 1992, is a National Wildlife Refuge (NWR) located along the banks of the Missouri River in the U.S. state of Nebraska.  The 4040 acre refuge preserves an area that had been cultivated and neglected before the early 1990s.  Channelization projects along the Missouri River to improve flood control and navigation resulted in the closing off a side branch of the river, known since the early 19th century as Boyer Chute.  Between 1820 and 1937 the Missouri River had migrated 3 mi eastward and the area of the chute had originally been on the east bank of the river; today, the chute is west of the main channel of the Missouri.  In 1937, the Army Corps of Engineers began to rechannel portions of the Missouri River, cutting off the chute to flowing water.  Overgrowth and cultivation took over the lands now preserved in the refuge.  Restoration of the area commenced in 1993; this included planting 9,100 native plants and trees and restoring the inflow to the chute from the main channel of the Missouri River.

Missouri Route 9: Route 9 is a highway in the Kansas City, Missouri area.  Its northern terminus is at Interstate 29/U.S. Route 71 in Kansas City North; its southern terminus is at Interstate 35/Interstate 70/U.S. Route 24/U.S. Route 40 in downtown Kansas City.  Even though both termini are in Kansas City, it passes through other towns and cities.  It is carried across the Missouri River by the Heart of America Bridge between downtown Kansas City, Missouri and North Kansas City, MO.  In North Kansas City, the highway serves as a main thoroughfare, Burlington Street.

Cow Creek (Montana): Cow Creek is a tributary of the Missouri River, approximately 35 mi long, in north central Montana in the United States.  Cow Creek rises in the southern foothills of the Bear Paw Mountains in western Blaine County and flows east and then south, joining the Missouri approximately 25 mi northeast of Winifred, Montana—or 22 mi upstream from the Fred Robinson Bridge.  Cow Creek flows down to the Missouri in a canyon that passes through the Missouri Breaks, which are severely eroded badlands that extend out on either side from the Missouri River.  The floor of Cow Creek canyon provided a pathway of travel from the Montana plains north of the river, down to the Missouri – at the mouth of Cow Creek, Cow Island made fording the Missouri easier – a steep but short trail on the south bank of the Missouri opposite Cow Creek completed this route which led from the northern Montana plains to the central and southern Montana plains.  This pathway was used by migrating buffalo/bison and nomadic American Natives for centuries.  During the steamboat era on the Missouri River, when low water prevented riverboats getting up to Fort Benton, the mouth of Cow Creek became a river landing and freighting depot, and it was the start of the Cow Island Trail by which freight was moved on to Fort Benton by going north up Cow Creek and then west.  In 1877 the Nez Perce Indian Tribe, fleeing to Canada, had several skirmishes along Cow Creek including the "Battle of Cow Island", and several days later at a camp on Cow Creek the Nez Perce, thinking themselves now beyond the reach of the U.S. Army, made the fateful decision to slow down, rather than push on for the Canada–US border.  Today, modern highways have by passed Cow Creek, and the buffalo and the nomadic Indian are gone.  Cow Creek is dormant, in one of the most remote spots of the isolated regions of the vast area known as the Montana Missouri Breaks.

Kansas City, Missouri: Kansas City is the largest city in Missouri, United States, and the sixth largest city in the Midwest.  According to the U.S. Census Bureau, the city had an estimated population of 481,420 in 2016, making it the 37th largest city by population in the United States.  It is the anchor city of the Kansas City metropolitan area, which straddles the Kansas–Missouri border.  Kansas City was founded in the 1830s as a Missouri River port at its confluence with the Kansas River coming in from the west.  On June 1, 1850 the town of Kansas was incorporated; shortly after came the establishment of the Kansas Territory.  Confusion between the two ensued and the name Kansas City was assigned to distinguish them soon thereafter.

Jack Killilay: John William Killilay (May 24, 1887 – October 21, 1968) was a pitcher in Major League Baseball who played for the Boston Red Sox during the season.  Listed at 5 ft , 165 lb., Killilay batted and threw right-handed.  He was born in Leavenworth, Kansas.

Downtown Kansas City: Downtown Kansas City is the central business district (CBD) of Kansas City, Missouri and the Kansas City metropolitan area.  It is between the Missouri River in the north, to 31st Street in the south; and from the Kansas–Missouri state line east to Bruce R. Watkins Drive as defined by the Downtown Council of Kansas City; the 2010 Greater Downtown Area Plan formulated by the City of Kansas City defines the Greater Downtown Area to be the city limits of North Kansas City and Missouri to the north, the Kansas–Missouri state line to the west, 31st Street to the south and Woodland Avenue to the east.  However, the definition used by the Downtown Council is the most commonly accepted.

North Kansas City, Missouri: North Kansas City is a city in Clay County, Missouri, United States that despite the similarity in name to its larger counterpart, Kansas City, is an independent municipality part of the Kansas City metropolitan area.  The population was 4,208 at the 2010 census.  Originally a northern suburb across the Missouri River from Kansas City, Missouri, it is now almost completely surrounded by Kansas City, which has annexed far to the north of North Kansas City's northern city limits.  North Kansas City also adjoins the small municipality of Avondale.

2011 Missouri River Flood: The 2011 Missouri River floods was a flooding event on the Missouri River in the United States.  The flooding was triggered by record snowfall in the Rocky Mountains of Montana and Wyoming along with near-record spring rainfall in central and eastern Montana.  All six major dams along the Missouri River released record amounts of water to prevent overflow which led to flooding threatening several towns and cities along the river from Montana to Missouri; in particular Bismarck, North Dakota; Pierre, South Dakota; Dakota Dunes, South Dakota; South Sioux City, Nebraska, Sioux City, Iowa; Omaha, Nebraska; Council Bluffs, Iowa; Kansas City, Missouri; Jefferson City, Missouri, as well as putting many smaller towns at risk.  According to the National Weather Service, in the second half of the month of May 2011, almost a year's worth of rain fell over the upper Missouri River basin.  Extremely heavy rainfall in conjunction with an estimated 212 percent of normal snowpack in the Rocky Mountains contributed to this flooding event.

Blue River (Missouri River): The Blue River (also known as the Big Blue River) is a 39.8 mi stream that flows through Johnson County, Kansas and Jackson County, Missouri in the Kansas City Metropolitan Area.  The river rises in Johnson County near the border of the states of Kansas and Missouri.  Crossing the city of Kansas City, Missouri, it empties into the Missouri River near the border between Kansas City and Independence, Missouri.

Question: What is the name of the place that is on the west bank of the Missouri River 25 mi northwest of Kansas City, Missouri where Jack Killilay was born?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "place_name": {
      "type": "string",
      "description": "The name of the city."
    },
    "county_seat_of": {
      "type": "string",
      "description": "The county for which the city is the county seat."
    },
    "location_details": {
      "type": "object",
      "properties": {
        "distance_from_kansas_city_miles": {
          "type": "integer",
          "description": "Distance from Kansas City, Missouri in miles."
        },
        "direction_from_kansas_city": {
          "type": "string",
          "description": "Direction from Kansas City, Missouri."
        },
        "river_bank": {
          "type": "string",
          "description": "The bank of the Missouri River the city is located on."
        }
      },
      "required": [
        "distance_from_kansas_city_miles",
        "direction_from_kansas_city",
        "river_bank"
      ],
      "additionalProperties": false
    },
    "notable_person_born_there": {
      "type": "string",
      "description": "The name of a notable person born in this city."
    }
  },
  "required": [
    "place_name",
    "county_seat_of",
    "location_details",
    "notable_person_born_there"
  ],
  "additionalProperties": false
}
