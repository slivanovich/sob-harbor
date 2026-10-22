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
Ranger Bridge: The Ranger Bridge (officially Veterans Memorial Bridge) between Wells River, Vermont and Woodsville, New Hampshire, is a three-hinged steel arch truss bridge over the Connecticut River.  It was built in 1923 to replace a 1917 bridge.  This is the oldest steel arch bridge over the Connecticut River. .

Red Cliff Bridge: Red Cliff Bridge is a cantilevered steel arch bridge located about 0.5 mi southwest of the town of Red Cliff, Colorado.  The bridge carries U.S. Highway 24 over the Eagle River, as well as a county road, and the former Union Pacific Railroad track that heads south toward Tennessee Pass and the city of Leadville.  One of only two steel arch bridges within Colorado, Red Cliff Bridge has been listed on the National Register of Historic Places since 1985 and is the state's only "cantilevered" steel arch bridge.

Lupu Bridge: The Lupu Bridge () is a through arch bridge over the Huangpu River in Shanghai, China, connecting the city's Huangpu and Pudong districts.  It is the world's second longest steel arch bridge, after the Chaotianmen Bridge in Chongqing.  The bridge has a total length including approach spans of 3900 m and opened on June 28, 2003.  The main bridge structure is 750m long including the two side spans of 100m each, and the main span of 550 m over the Huangpu River is 32 m longer than the previous record holder for the longest arch bridge, the New River Gorge Bridge in Fayetteville, West Virginia.  It cost 2.5 billion yuan (US$302 million), including US$78.04 for the main steel structure alone.  It is located adjacent to the former Expo 2010 site and served as the centrepiece of the world exposition in Shanghai.

Bayonne Bridge: The Bayonne Bridge is an arch bridge spanning the Kill Van Kull connecting Bayonne, New Jersey with Staten Island, New York City.  It carries NY 440 and NJ 440.  The Bayonne Bridge is the fifth-longest steel arch bridge in the world, and was the longest in the world at the time of its completion.  The bridge is also one of four connecting New Jersey with Staten Island; the other two roadway bridges are the Goethals Bridge in Elizabeth and Outerbridge Crossing in Perth Amboy, and the rail-only Arthur Kill Vertical Lift Bridge, all of which traverse the Arthur Kill.

Glen Canyon Dam Bridge: The Glen Canyon Bridge or Glen Canyon Dam Bridge is a steel arch bridge in Coconino County, Arizona, carrying U.S. Route 89 across the Colorado River.  The bridge was originally built by the United States Bureau of Reclamation to facilitate transportation of materials for the Glen Canyon Dam, which lies adjacent to the bridge just 865 ft upstream.  The two-lane bridge has an overall length of 1271 ft with a deck 700 ft above the river, making it the one of the highest bridges in the United States.  The bridge was the highest arch bridge in the world when completed in 1959.

Port Mann Bridge: The Port Mann Bridge is a 10-lane cable-stayed bridge that opened to traffic in 2012.  It is currently the second longest cable-stayed bridge in North America and was the widest bridge in the world until the opening of the new Bay Bridge in California.  The new bridge replaced a steel arch bridge that spanned the Fraser River, connecting Coquitlam to Surrey in British Columbia near Vancouver.  The old bridge consisted of three spans with an orthotropic deck carrying five lanes of Trans-Canada Highway traffic, with approach spans of three steel plate girders and concrete deck.  The total length of the previous Port Mann was 2093 m , including approach spans.  The main span was 366 m , plus the two 110 m spans on either side.  Volume on the old bridge was 127,000 trips per day.  Approximately 8 percent of the traffic on the Port Mann bridge was truck traffic.  The previous bridge was the longest arch bridge in Canada and third-longest in the world at the time of its inauguration.

Whirlpool Rapids Bridge: The Whirlpool Rapids Bridge, commonly called the Whirlpool Bridge, and until 1937, known as the Lower Steel Arch Bridge, is a spandrel braced, riveted, two-hinged arch bridge.  It crosses the international border between Canada and the United States, connecting the commercial downtown districts of Niagara Falls, Ontario and Niagara Falls, New York.  This bridge is located approximately 1.5 km north of the Rainbow Bridge and about 2 km from the Falls.  This bridge was acquired by the Niagara Falls Bridge Commission in January 1959.

Zhaoqing Bridge: The Xijiang Railway Bridge (), is located on the Guangzhou to Nanning highspeed railway with a 450-meter main span that is the world's longest railway-only arch bridge and the second largest steel box arch after the Lupu Bridge in Shanghai.  The basket handle arch carries 2 railway lines over a deep reservoir on the Xi River.

Samson Occom Bridge: Bridge No. 1860, also known as the Samson Occom Bridge, is a fieldstone arch bridge in Montville, Connecticut, United States.  Constructed by the Connecticut State Highway Department in 1936 as a Works Progress Administration project, it is located on Mohegan tribal land in an area that was once a part of Fort Shantok State Park.  The bridge carries traffic from Massapeag Side Road (Special Service Road 433) over the Shantok Brook, a tributary of the Thames River.  Spanning 12 ft across the brook, the bridge's arch rises about 6 ft above the water.  According to a 2011 Connecticut Department of Transportation report, it carries 1,100 vehicles per day.  Samson Occom Bridge was listed on the National Register of Historic Places in 1993.

New River Gorge Bridge: The New River Gorge Bridge is a steel arch bridge 3030 ft long over the New River Gorge near Fayetteville, West Virginia, in the Appalachian Mountains of the eastern United States.  With an arch 1700 ft long, the New River Gorge Bridge was for many years the world's longest single-span arch bridge; it is now the fourth longest.  Part of U.S. Route 19, its construction marked the completion of Corridor L of the Appalachian Development Highway System.  The bridge is crossed by an average of 16,200 motor vehicles per day.

Question: Lupu Bridge is longer than which steel arch bridge in the Appalachian Mountains of the eastern United States that is crossed by an average of 16,200 motor vehicles per day?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "bridge_name": {
      "type": "string",
      "description": "The official name of the identified steel arch bridge."
    },
    "bridge_type": {
      "type": "string",
      "description": "The structural type of the bridge."
    },
    "location": {
      "type": "object",
      "properties": {
        "region": {
          "type": "string",
          "description": "The geographical region where the bridge is located."
        },
        "state": {
          "type": "string",
          "description": "The U.S. state where the bridge is located."
        }
      },
      "required": [
        "region",
        "state"
      ],
      "additionalProperties": false
    },
    "daily_vehicle_traffic": {
      "type": "integer",
      "description": "The average number of motor vehicles crossing the bridge per day."
    },
    "length_comparison_to_lupu_bridge": {
      "type": "string",
      "description": "Describes the length relationship between the identified bridge and the Lupu Bridge."
    }
  },
  "required": [
    "bridge_name",
    "bridge_type",
    "location",
    "daily_vehicle_traffic",
    "length_comparison_to_lupu_bridge"
  ],
  "additionalProperties": false
}
