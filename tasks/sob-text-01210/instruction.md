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
American Dream Meadowlands: American Dream Meadowlands (ADM) is a retail and entertainment complex under construction in the Meadowlands Sports Complex in East Rutherford, New Jersey that will contain over 500 stores.  It was first proposed in 2003 by the Mills Corporation as the "Meadowlands Xanadu".  After the bankruptcy of that company in 2007, the project was taken over by Colony Capital.  In May 2009, construction stalled due to the bankruptcy of Lehman Brothers.  The Triple Five Group announced intent to take over the mall in May 2011, and on July 31, 2013, officially gained control of the mall and the surrounding site.

Bergen Ballpark: The Bergen Ballpark was a proposed 8,000-seat baseball-only stadium in East Rutherford, New Jersey, intended to be the home of the Bergen Cliff Hawks.  The stadium was to be part of the larger Meadowlands Xanadu project that is currently under construction.  Bergen Ballpark was in the planning stages since 2001, but local politics and a lease agreement between the Mills Corporation, the company who built the Xanadu and would own the ballpark, halted plans in 2005.

Meadowlands Sports Complex: The Meadowlands Sports Complex is a sports and entertainment complex located in East Rutherford, Bergen County, New Jersey, United States, owned and operated by the New Jersey Sports and Exposition Authority (NJSEA).

Meadowlands State Fair: The State Fair Meadowlands (formerly the Meadowlands Fair) is a carnival held every summer at the Meadowlands Sports Complex in East Rutherford, New Jersey.  It derives its name from State Fair Stores, which run the carnival.  It should also not be confused with the New Jersey State Fair, Sussex County Farm and Horse Show in Augusta, New Jersey.  The fair is held in the parking lot that surrounds the MetLife Stadium and runs for two weeks in late June and early July.  It attracts over 300,000 visitors per year.Michael Moore has been spotted at this fair while wearing his Rutgers hat.

New Jersey Route 3: Route 3 is a state highway in the northern part of New Jersey in the United States.  The route runs 10.84 mi from U.S. Route 46 in Clifton, Passaic County to U.S. Route 1/9 in North Bergen, Hudson County.  Route 3 is sometimes called the Secaucus Bypass within Secaucus.  The route is a divided highway for its entire length, with most of the highway considered a freeway, except the westernmost part, which contains direct access to a few businesses.  Route 3 intersects many major roads, including the Garden State Parkway and Route 21 in Clifton, the western spur of the New Jersey Turnpike (Interstate 95) in East Rutherford, the eastern spur of the New Jersey Turnpike in Secaucus, and Route 495 in North Bergen.  A commuting route for northern New Jersey to the Lincoln Tunnel into New York City by way of Route 495, Route 3 also provides access to the Meadowlands Sports Complex in East Rutherford.  The road inspired a story in "The New Yorker" in 2004 by Ian Frazier.

New Jersey Devils: The New Jersey Devils are a professional ice hockey team based in Newark, New Jersey.  They are members of the Metropolitan Division of the Eastern Conference of the National Hockey League (NHL).  The club was founded as the Kansas City Scouts in Kansas City, Missouri, in 1974.  The Scouts moved to Denver, Colorado in 1976 and became the Colorado Rockies.  In 1982, they moved to East Rutherford, New Jersey and took their current name.  For their first 25 seasons in New Jersey, the Devils were based at the Meadowlands Sports Complex in East Rutherford and played their home games at Brendan Byrne Arena (later renamed to Continental Airlines Arena).  Beginning with the 2007–08 season, the Devils relocated to Newark and now play their home games at the Prudential Center.

New Jersey Route 120: Route 120 is a state highway located in Bergen County, New Jersey, United States.  It extends 2.65 mi from an interchange with Route 3 in East Rutherford to another interchange with Route 17 in Carlstadt, where it continues to the west as County Route 120.  NJ 120 serves the Meadowlands Sports Complex, which consists of MetLife Stadium, Meadowlands Racetrack, and the Izod Center.  It heads north from Route 3 as a six-lane freeway through the sports complex to an interchange with the southern terminus of County Route 503.  From here, Route 120 heads northwest along the northern edge of the sports complex as a four-lane divided at-grade Paterson Plank Road, passing through industrial and commercial areas.

Meadowlands station: Meadowlands Sports Complex, or Meadowlands, is a New Jersey Transit train station that is the western teminus for the Meadowlands Rail Line located at the Meadowlands Sports Complex in East Rutherford, New Jersey.

Meadowlands Arena: Meadowlands Arena (formerly Brendan Byrne Arena, Continental Airlines Arena, and IZOD Center) is an indoor venue located in the Meadowlands Sports Complex in East Rutherford, New Jersey, United States.  The arena is located on New Jersey Route 120 and is across the highway from MetLife Stadium and the Meadowlands Racetrack.  A covered footbridge connects one of MetLife Stadium's parking lots with the Meadowlands Arena's lot.

MetLife Stadium: MetLife Stadium is an American sports stadium located in East Rutherford, New Jersey.  It is part of the Meadowlands Sports Complex and serves as the home stadium for two National Football League (NFL) franchises: the New York Giants and the New York Jets.  The stadium is owned by the MetLife Stadium Company, a joint venture of the Giants and Jets, who jointly built the stadium using private funds on land owned by the New Jersey Sports and Exposition Authority.  The stadium opened as New Meadowlands Stadium in 2010.  In 2011, MetLife, an insurance company based in New York City, acquired the naming rights to the stadium.  At a construction cost of approximately $1.6 billion, it is the most expensive stadium ever built and is the second-largest stadium in the NFL in terms of seating capacity.

Question: The Bergen Ballpark was a proposed 8,000-seat baseball-only stadium in East Rutherford, New Jersey, intended to be the home of the Bergen Cliff Hawks, the stadium was to be part of which retail and entertainment complex under construction in the Meadowlands Sports Complex in East Rutherford, New Jersey that will contain over 500 stores?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "complex_name": {
      "type": "string",
      "description": "The current name of the retail and entertainment complex."
    },
    "original_project_name": {
      "type": "string",
      "description": "The initial proposed name of the project."
    },
    "location": {
      "type": "string",
      "description": "The city and state where the complex is located."
    },
    "number_of_stores": {
      "type": "integer",
      "description": "The number of stores the complex will contain."
    },
    "parent_complex": {
      "type": "string",
      "description": "The larger sports complex where this retail and entertainment complex is located."
    }
  },
  "required": [
    "complex_name",
    "original_project_name",
    "location",
    "number_of_stores",
    "parent_complex"
  ],
  "additionalProperties": false
}
