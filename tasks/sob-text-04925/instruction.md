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
Port of Detroit: The Port of Detroit is located along the west side of the Detroit River, and is the largest seaport in the state of Michigan.  The port is overseen by the Detroit/Wayne County Port Authority, a five-member board of directors appointed by the State of Michigan, Wayne County, and the City of Detroit.  The authority coordinates river commerce on the waters and shoreline of Wayne County.  The port consists of multiple marine terminals handling general, liquid, and bulk cargo as well as passengers.  The Port of Detroit's single most valuable commodity is steel, and the largest commodity handled by tonnage is ore.  Other important commodities handled at the port include stone, coal and cement.

List of islands in the Detroit River: The following is a description of islands in the Detroit River.  The Detroit River is a river in the Great Lakes system, about 32 miles (51 km) long and 0.5–2.5 miles (0.8–4.0 km) wide.  The river serves as a major shipping channel, jointly controlled by the United States and Canada, and is a major component of the Canada–United States border.  Ownership and control of the islands varies by their geographic location along the river.  The majority of islands are on the American side of the river, which are all under the jurisdiction of Wayne County in Michigan.  The Canadian islands are part of Essex County in Ontario.  There are no islands in the Detroit River that are divided by the international border.

Jenson Tunnel: Jenson Railroad Tunnel is the first and only railroad tunnel in the present state of Oklahoma.  It was constructed through Backbone Mountain during 1885-6, by the Fort Smith & Southern Railway (FSSR).  and has remained in service until the present.  At the time it was built, this area belonged to the Choctaw Nation in Indian Territory.  Since Oklahoma became a state in 1907, the tunnel site has been part of Le Flore County, Oklahoma.  It is now primarily used by the Kansas City Southern Railroad (KCS), and is sometimes referred to as the KCS - Jenson Tunnel.

Detroit: Detroit ( ) is the most populous city in the U.S. state of Michigan, the largest city on the United States–Canada border, and the seat of Wayne County.  The municipality of Detroit had a 2015 estimated population of 677,116, making it the 21st-most populous city in the United States.  The metropolitan area, known as Metro Detroit, is home to 4.3 million people, making it the second-largest in the Midwest after Chicago.

Niagara Cantilever Bridge: The Niagara Cantilever Bridge or Michigan Central Railway Cantilever Bridge was a cantilever bridge across the Niagara Gorge.  An international railway-only bridge between Canada and the United States, it connected Niagara Falls, New York, and Niagara Falls, Ontario, located just south of the Whirlpool Bridge, and opened to traffic in 1883, it was replaced by the Michigan Central Railway Steel Arch Bridge in 1925.

Blue Ridge Tunnel: The Blue Ridge Tunnel (also known as the Crozet Tunnel) is a historic railroad tunnel built during the construction of the Blue Ridge Railroad in the 1850s.  The tunnel was the westernmost and longest of four tunnels engineered by Claudius Crozet to cross the Blue Ridge Mountains at Rockfish Gap in central Virginia.  At 4237 ft in length, the tunnel was the longest tunnel in the United States at the time of its completion in 1858.  The tunnel was used by the Virginia Central Railroad from its opening to 1868, when the line was reorganized as the Chesapeake and Ohio Railroad (renamed Chesapeake and Ohio Railway in 1878).  The Chesapeake and Ohio routed trains through the tunnel until it was abandoned and replaced by a new tunnel in 1944.  The new tunnel was named the "Blue Ridge Tunnel" as well, although the original tunnel still remains abandoned nearby.  The old Blue Ridge Tunnel has since been named a Historic Civil Engineering Landmark.

Alaska Central Railroad Tunnel No. 1: Alaska Central Railroad Tunnel No. 1, also known as the Loop District Tunnel No. 1 is a historic railroad tunnel located about 40 mile north of Seward, Alaska, in the Placer River Valley, Kenai Peninsula.  The tunnel was dug in 1906 and served the Alaska Central Railroad and later the Alaska Railroad until the route in the area, known as the "Loop District" was rerouted in 1951.

Cobble Hill Tunnel: The Cobble Hill Tunnel (popularly the Atlantic Avenue Tunnel) of the Long Island Rail Road (LIRR) is an abandoned railroad tunnel beneath Atlantic Avenue in downtown Brooklyn, New York City.  When open, it ran for about 2517 ft between Columbia Street and Boerum Place.  It is the oldest railway tunnel beneath a city street in North America that was fully devoted to rail.

Detroit River: The Detroit River flows for 24 nmi from Lake St. Clair to Lake Erie as a strait in the Great Lakes system and forms part of the border between Canada and the United States.  The river divides the metropolitan areas of Detroit, Michigan and Windsor, Ontario - an area referred to as Detroit–Windsor.  The two cities are connected by the Ambassador Bridge, the Detroit–Windsor Tunnel and the Michigan Central Railway Tunnel.

Michigan Central Railway Tunnel: The Michigan Central Railway Tunnel is a railroad tunnel under the Detroit River connecting Detroit, Michigan, in the United States with Windsor, Ontario, in Canada.  The US entrance is south of Porter and Vermont streets near Rosa Parks Boulevard.  The Canadian entrance is south of Wyandotte Street West between Cameron and Wellington Avenues.  It was built by the Detroit River Tunnel Company for the Canada Southern Railway, leased by the Michigan Central Railroad and owned by the New York Central Railroad.  The tunnel opened in 1910 and is still in use today by the Canadian Pacific Railway.  On the Detroit side, the area around the tunnel is off limits to the general public and is routinely patrolled by officers and agents of the US Department of Homeland Security, Canadian Pacific Police Service, CN Police, Detroit Police Department, and the security elements of the bridge company.

Question: Which state of Canada is connected to the most populous city in the US state of Michigan and the seat of Wayne County, by means of the Michigan Central Railway Tunnel, a railroad tunnel under the Detroit River?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "connected_us_city": {
      "type": "string",
      "description": "The US city connected by the tunnel."
    },
    "us_state": {
      "type": "string",
      "description": "The US state where the connected US city is located."
    },
    "us_county_seat": {
      "type": "boolean",
      "description": "Indicates if the US city is the seat of its county."
    },
    "us_most_populous_city_in_state": {
      "type": "boolean",
      "description": "Indicates if the US city is the most populous in its state."
    },
    "connected_canadian_city": {
      "type": "string",
      "description": "The Canadian city connected by the tunnel."
    },
    "canadian_province": {
      "type": "string",
      "description": "The Canadian province where the connected Canadian city is located."
    },
    "connecting_tunnel_name": {
      "type": "string",
      "description": "The name of the railway tunnel connecting the two cities."
    }
  },
  "required": [
    "connected_us_city",
    "us_state",
    "us_county_seat",
    "us_most_populous_city_in_state",
    "connected_canadian_city",
    "canadian_province",
    "connecting_tunnel_name"
  ],
  "additionalProperties": false
}
