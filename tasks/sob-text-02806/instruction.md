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
Madison Square Garden: Madison Square Garden, often called "MSG" or simply "The Garden", is a multi-purpose indoor arena in the New York City borough of Manhattan.  Located in Midtown Manhattan between 7th and 8th Avenues from 31st to 33rd Streets, it is situated atop Pennsylvania Station.  It is the fourth venue to bear the name "Madison Square Garden", the first two (1879 and 1890) of which were located on Madison Square, on East 26th Street and Madison Avenue, with the third Madison Square Garden further uptown at Eighth Avenue and 50th Street.  The Garden is used for professional basketball and ice hockey, as well as boxing, concerts, ice shows, circuses, professional wrestling and other forms of sports and entertainment.  It is close to other midtown Manhattan landmarks, including the Empire State Building, Koreatown, and Macy's at Herald Square.  It is home to the New York Rangers of the National Hockey League (NHL), the New York Knicks of the National Basketball Association (NBA), and since 1997, the New York Liberty (WNBA).

Herbert H. Lehman High School: Herbert H. Lehman High School is a public high school at 3000 East Tremont Avenue, in the Westchester Square section of the Bronx, New York City, U.S.A.  The school is named after former New York State Governor Herbert Henry Lehman (1878 – 1963).  The school is not affiliated with Lehman College in the Bronx but does hold its annual graduation ceremony there each June.

The Bronx: The Bronx ( ) is the northernmost of the five boroughs of New York City, within the U.S. state of New York.  It is geographically south of Westchester County; north and east of the island and borough of Manhattan to the south and west across the Harlem River; and north of the borough of Queens, across the East River.  Of the five boroughs, the Bronx is the only one that has the majority of its area on the U.S. mainland and, with a land area of 42 sqmi and a population of 1,455,720 in 2016, has the fourth-largest land area, the fourth-highest population, and the third-highest population density.  Since 1914, the Bronx has had the same boundaries as Bronx County, a county of New York and the third most densely populated county in the United States.

Huntington Free Library and Reading Room: The Huntington Free Library is a privately endowed library near Westchester Square in the Bronx borough of New York City which is open to the public.  It has a non-circulating book collection.

Northern Westchester: Northern Westchester refers to the upper portion of Westchester County, New York, a suburban area north of New York City.  Lying north of Interstate 287/Cross Westchester Expressway, these communities are distinguished by distance from New York City and their more rural character from those of Southern Westchester.  The area is notable for its general affluence and high degree of watershed for New York City, being home to two major collection reservoirs supplying drinking water to it, the New Croton Reservoir and the Kensico Reservoir.

Bronx Community Board 10: Bronx Community Board 10 is a local government unit of the New York City borough of the Bronx, encompassing the neighborhoods of City Island, Co-op City, Pelham Bay, Throggs Neck and Westchester Square.  It is delimited by the Hutchinson River and Pelham Bay Park to the east, New England Thruway, Hutchinson River Parkway, and Westchester Creek to the west, the Bronx/Westchester County Line to the north and the East River to the south.

Annabel Palma: Annabel Palma is the Council member for the 18th District of the New York City Council.  She is a Democrat.  The district includes Castle Hill, Clason Point, Hunts Point, Parkchester, Soundview, West Farms and Westchester Square in The Bronx.

IRT Pelham Line: The IRT Pelham Line, also called the Southern Boulevard–Pelham Bay Park Line, is a rapid transit line on the New York City Subway, operated as part of the A Division and served by the 6 and <6> trains.  It was built as part of the Dual Contracts expansion and opened between 1918 and 1920.  It is both elevated and underground with Whitlock Avenue being the southernmost elevated station.  It has three tracks from the beginning to just south of the Pelham Bay Park terminal.  The Pelham Line also has a connection to Westchester Yard, where 6 trains are stored, just north of Westchester Square–East Tremont Avenue.  As of 2013, it has a daily ridership of 205,590.

Westchester Square, Bronx: Westchester Square is a residential neighborhood geographically located in the eastern section of the borough of The Bronx in New York City.  The neighborhood is part of Bronx Community District 10.  Its boundaries, starting from the north and moving clockwise are: East Tremont Avenue and Silver Street, Blondell Avenue and Westchester Creek to the east, Waterbury Avenue to the south and Castle Hill Avenue to the west.  The main roadways into and out of Westchester Square are East Tremont Avenue, Westchester Avenue and Williamsbridge Road.  ZIP codes include 10461 and 10462.  The area is patrolled by the 45th Precinct located at 2877 Barkley Avenue Bronx, New York 10465.

East Bronx: The East Bronx is that part of the New York City borough of the Bronx which lies east of the Bronx River; this roughly corresponds to the eastern half of the borough.  Neighborhoods include: Harding Park, Soundview, Castle Hill, Parkchester, Westchester Square, Edgewater Park, Van Nest, Pelham Parkway, Morris Park, Throggs Neck, Country Club, City Island, Pelham Bay, Williamsbridge, Eastchester, Baychester, Edenwald, Wakefield, Bronx, and Co-op City.

Question: What is the land area of the New York City borough that is home to Westchester Square? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "borough_name": {
      "type": "string",
      "description": "The name of the New York City borough."
    },
    "neighborhood_name": {
      "type": "string",
      "description": "The name of the neighborhood in question."
    },
    "land_area_sqmi": {
      "type": "integer",
      "description": "The land area of the borough in square miles."
    }
  },
  "required": [
    "borough_name",
    "neighborhood_name",
    "land_area_sqmi"
  ],
  "additionalProperties": false
}
