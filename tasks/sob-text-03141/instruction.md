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
Paul Avenue station: Paul Avenue Station was a lightly used Caltrain station located in Bayview, San Francisco, California.  Before its closure in 2005, the station was served by only two trains Monday through Friday (one morning northbound Local and one afternoon southbound Local), and had no service on weekends.  The station was located between 22nd Street Station and Bayshore Station, two blocks west of Gilman/Paul Station on the T Third Street Muni line.

Bayshore, Ottawa: Bayshore (also known as Accora Village) is a neighbourhood in Bay Ward in the west end of Ottawa, Ontario, Canada.  Prior to amalgamation in 2001, the neighbourhood was in the City of Nepean.  It is bounded east by row houses off Bayshore Drive, to the north Carling Avenue, to the west Holly Acres Drive and the Lakeview neighbourhood, and to the south Ontario Highway 417.  The main street in Bayshore is Woodridge Crescent, while the Bayshore Station is the major bus transit station.

Bedok Mall: Bedok Mall (Chinese: 勿落广场) is a large suburban shopping mall in Bedok, Singapore and part of a mixed development compromising of retail and residential development that is integrated with a bus interchange.  Located at the heart of Bedok, the integrated retail and residential development comprises a 3-storey lifestyle and family shopping mall and eight 15-storey residential towers called Bedok Residences.  It was the first major shopping mall to open in Bedok and was built on the site of the former Bedok bus interchange.

Bayshore station: Bayshore is a station on Ottawa, Ontario, Canada's transitway served by OC Transpo buses.  It is located in the western transitway section at the Bayshore Shopping Centre in the neighbourhood of Bayshore.  It is the western terminus for rapid transit route 97 and route 101 , as well as other crosstown routes such as route 11 and route 85 .

Bayshore Mall: The Bayshore Mall is an indoor shopping mall located in Eureka, California owned and managed by Rouse Properties, a former division of General Growth Properties, one of the largest mall owners in the United States.  It is named for its close proximity to Humboldt Bay.  The large shopping facility is the only major mall located on the coast north of the San Francisco Bay Area, securing Eureka as the trading center for the entire far North Coast.

Bayshore Town Center: Bayshore Town Center (formerly called Bayshore Mall) is a shopping mall/mixed use complex including retail, restaurants, entertainment, office and residential in Glendale, Wisconsin.  It is anchored by Barnes & Noble, Boston Store, and Kohl's.  Originally an outdoor strip mall built in 1954, it was converted into an enclosed mall in 1974.  By 1989, it held the last remaining location of local department store T. A. Chapman Co.

Bayshore Shopping Centre: Bayshore Shopping Centre is a major shopping mall located in Ottawa, Ontario, Canada.  The mall is one of the busiest in the National Capital Region as it attracts about 7 million visitors per year from across the city and the surrounding region.

Ansal Plaza: Ansal Plaza is also shopping mall located at Andrews Ganj on Khel Gaon Marg, in South Delhi.  Opened on 1 November 1999, it is the first major shopping mall of Delhi.  The mall was established by Ansal Properties & Infrastructure Ltd.  The mall has an amphitheatre enclaved within the circular shaped plaza.  It has parking facilities for 1000 cars.

OC Transpo Route 97: OC Transpo Route 97 is the City of Ottawa bus (transitway) between downtown and the airport.  It starts at Bayshore Station at Bayshore Shopping Centre and ends at either South Keys Station or the Airport.  Several trips each day start or end at Tunney's Pasture Station.  Some trips also serve Bells Corners after serving Bayshore Station.

Pinecrest Station: Pinecrest is a Transitway station in Ottawa, Ontario, that began service on September 6, 2009.  The name is due to the station's proximity to Pinecrest Road.  On June 9, 2006, Then-Ottawa Mayor Bob Chiarelli announced an extension of the West Transitway that include a 1.8 kilometre stretch of transitway from Bayshore station to Pinecrest Road including the new station and located near the road previously served as a regular stop for westbound buses such as route 101.

Question: Where is the major shopping mall which Bayshore station is located at located 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "shopping_mall": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the shopping mall."
        },
        "is_major_mall": {
          "type": "boolean",
          "description": "Indicates if the shopping mall is described as a major mall."
        }
      },
      "required": [
        "name",
        "is_major_mall"
      ],
      "additionalProperties": false
    },
    "transit_station": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the transit station."
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the shopping mall is located."
        },
        "province_state": {
          "type": "string",
          "description": "The province or state where the shopping mall is located."
        },
        "country": {
          "type": "string",
          "description": "The country where the shopping mall is located."
        }
      },
      "required": [
        "city",
        "province_state",
        "country"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "shopping_mall",
    "transit_station",
    "location"
  ],
  "additionalProperties": false
}
