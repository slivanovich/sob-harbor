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
50 West Street: 50 West Street is a 64-story, 778 ft tall mixed-use retail and residential condominium tower developed by Time Equities Inc. in Lower Manhattan, New York City.  It contains 191 residential units.

Albany Street (Manhattan): Albany Street is a short street in the Financial District of Lower Manhattan in New York City.  The street runs west-to-east from the Battery Park City Esplanade along the Hudson River to Greenwich Street, passing through South End Avenue and West Street on the way.  The street has a walkway connection to the Rector Street Bridge which crosses West Street.

125 Greenwich Street: 125 Greenwich Street (also known under the name of 22 Thames Street) is a residential supertall skyscraper being built in the Financial District, Manhattan, New York City, designed by architect Rafael Viñoly.  It is across the street from the construction site of 5 World Trade Center, at 130 Liberty Street.

West Village, Dallas: The West Village District is a walkable urban village in the Uptown area of Dallas, Texas.  West Village is located at the northern edge of Uptown along McKinney Avenue and is bordered by Lemmon Avenue, Cole Avenue, Haskell Drive and Central Expressway.  West Village proper has 88 retail, restaurant and entertainment tenants within 244000 sqft and contains approximately 700 residential units.  This has been the catalyst for the West Village District, which contains approximately 3,600 residential units, an emerging office market (including the Richard's Group Corporate Headquarters), and an estimated 500,000 square feet of gross leasable space- all within walking distance.

Dey Street: Dey Street is a short street in Lower Manhattan, in New York City.  It passes the west side of the World Trade Center site and the World Trade Center Transportation Hub.  It runs for one block between Church Street and Broadway.  It originally ran to West Street, but the western reaches were demolished to make way for the World Trade Center in the late 1960s.  It now extends to Greenwich Street.  15 Dey Street is the site of the first transcontinental telephone call.

Unity Buildings: The Unity Buildings in Liverpool, England consist of the 86 m (282 ft) tall Unity Residential and 64 m (210 ft) Unity Commercial.  They are respectively 27 and 16 storeys tall and the city's eighth and thirteenth tallest buildings (although typically speaking, the towers are one entity as they are both connected to one another).  The buildings are located immediately within Liverpool city centre on Chapel Street and were completed in 2007.  As the names suggest, the taller of the two towers consists primarily of flats and residential units, whilst the smaller tower is primarily office space.  The residential tower contains 162 residential units of mainly two and three bedroom duplex apartments, as well as a residents' gym and underground parking.  Prior to the construction of the Unity Buildings, another project was tipped for development on the same site.  The 145 m 40 storey building was to be called 'Capital Exchange', however it was scrapped in favour of the Unity Buildings.

54 Marsh Wall: 54 Marsh Wall is a residential/retail planned skyscraper in the Isle of Dogs, London.  The building was approved by Tower Hamlets on 19 January 2017.  At 140 meters high and containing 216 residential units, the tower will be among a number of similar residential skyscrapers under construction in the Isle of Dogs, including South Quay Plaza and the Landmark Pinnacle.  An earlier proposal, submitted in 2014, envisioned 240 residential units involving two twin towers at 39 and 29 stories.

101 Warren Street: 101 Warren Street (also known as 270 Greenwich Street) is a 35-story, 227 condominium, 163 rental apartment building in the Tribeca area of lower Manhattan, located between Greenwich Street and West Street.  The project was developed by Edward J. Minskoff Equities, designed by Skidmore Owings & Merrill, and completed in 2008.  The project features an "Artrium" on the fifth floor with a pine tree forest consisting of 101 trees.

Bank Street (Manhattan): Bank Street is a primarily residential street in the West Village part of Greenwich Village in the borough of Manhattan in New York City.  It runs for a total length of about 710 m from West Street, crossing Washington Street and Greenwich Street, to Hudson Street and Bleecker Street where it is interrupted by the Bleecker Playground, north of which is Abingdon Square; it then continues to Greenwich Avenue, crossing West 4th Street and Waverly Place.  Vehicular traffic runs west-east along this one-way street.  As with several other east-west streets in the Far West Village, the three blocks west of Hudson Street are paved with setts.

88 Greenwich Street: 88 Greenwich Street, also known as the Greenwich Club Residences, and previously known as 19 Rector Street, is a building which takes up the full block on the south side of Rector Street between Greenwich Street and Washington Street in the Financial District of Manhattan, New York City.  Built in 1929-30, the 37-story building was designed by Lafayette A. Goldstone and Alexander Zamshnick in the Art Deco style.

Question: In between 125 Greenwich Street and 50 West Street ,which contains 191 residential units?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "building_with_specified_units": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the building that matches the specified number of residential units."
        },
        "residential_units_count": {
          "type": "integer",
          "description": "The number of residential units in the identified building."
        }
      },
      "required": [
        "name",
        "residential_units_count"
      ],
      "additionalProperties": false
    },
    "other_building_in_question": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the other building mentioned in the question."
        },
        "residential_units_known_from_context": {
          "type": "boolean",
          "description": "Indicates if the number of residential units for this building is explicitly stated in the context."
        }
      },
      "required": [
        "name",
        "residential_units_known_from_context"
      ],
      "additionalProperties": false
    },
    "question_unit_count": {
      "type": "integer",
      "description": "The specific residential unit count mentioned in the question."
    }
  },
  "required": [
    "building_with_specified_units",
    "other_building_in_question",
    "question_unit_count"
  ],
  "additionalProperties": false
}
