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
Alvarado, Minnesota: Alvarado is a city situated along the Snake River in Marshall County in the State of Minnesota.  The population was 363 at the 2010 census.

Lansing, Kansas: Lansing is a city situated along the Missouri River in the eastern part of Leavenworth County, located in northeast Kansas, in the Central United States.  As of the 2010 census, the city population was 11,265.  It is the second most populous city of Leavenworth County and is a part of the Kansas City metropolitan area.

Pazardzhik: Pazardzhik (Bulgarian: Пазарджик ) is a city situated along the banks of the Maritsa river, Southern Bulgaria.  It is the capital of Pazardzhik Province and centre for the homonymous Pazardzhik Municipality.

Villasis, Pangasinan: Villasis is a farming town situated along the Agno River.  On its borders are the towns of Malasiqui (on the west), Urdaneta City (on the north), Asingan (on the east), and Rosales and Sto.  Tomas (on the south).  Hemmed between two bustling areas, Urdaneta City and Rosales, Villasis is one of the fastest developing towns in the province.  It also thrives on its rice, corn and tobacco plantations.  Its hilly barangays situated along the Malasiqui boundary is an ideal place for resort developers and agri-businessmen.

Emprise Bank: Emprise Bank is a Kansas-based, family owned, community bank headquartered in Wichita, Kansas with more than $1 billion in assets.  Emprise has 37 locations across the state of Kansas, including branches in Wichita, Andover, Augusta, Chanute, Clearwater, Council Grove, Derby, El Dorado, Eureka, Goddard, Hays, Haysville, Hillsboro, Humboldt, Iola, Lawrence, McPherson, Moran, Mulvane, Park City, Potwin, Rose Hill, and Valley Center.

Iola, Kansas: Iola (pronounced ) is a city situated along the Neosho River in the northwestern part of Allen County, located in Southeast Kansas, in the Central United States.  As of the 2010 census, the city population was 5,704.  Iola is the county seat of Allen County.  It is named in honor of Iola Colborn.

Humboldt, Kansas: Humboldt is a city in Allen County, Kansas, United States.  It is situated along the Neosho River.  As of the 2010 census, the city population was 1,953.

La Cygne, Kansas: La Cygne (pronounced "luh SEEN") is a city situated along the Marais des Cygnes River in the northeast part of Linn County, located in East Central Kansas, in the Central United States.  As of the 2010 census, the city population was 1,149.  The city is named after the Marais des Cygnes River which is a French translation of an Osage appellation meaning "marsh of the swans".

Wasaga Beach: Wasaga Beach (variant: Wasaga) is a town in Simcoe County, Ontario, Canada.  Situated along the longest (14 km) freshwater beach in the world, it is a popular summer tourist destination, located along the southern end of Georgian Bay, approximately two hours north of Toronto, and neighbours, to the west, Collingwood and The Blue Mountains which attract visitors much of the year.  The town is situated along a very long sandy beach on Nottawasaga Bay in Georgian Bay and the winding Nottawasaga River.  The beaches are part of the Ontario Parks's Wasaga Beach Provincial Park; the park area totals 168 hectares (415 acres).

Bassett, Kansas: Bassett is a city situated along the Neosho River in the west-central part of Allen County, located in southeast Kansas, in the central United States of America.  As of the 2010 census, the city population was 14.

Question: Emprise Bank has branches in a city situated along what river?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "bank_name": {
      "type": "string",
      "description": "The name of the bank in question."
    },
    "cities_with_branches_on_river": {
      "type": "array",
      "description": "A list of cities where the bank has branches and which are situated along a specific river.",
      "items": {
        "type": "object",
        "properties": {
          "city_name": {
            "type": "string",
            "description": "The name of the city."
          },
          "river_name": {
            "type": "string",
            "description": "The name of the river the city is situated along."
          },
          "county": {
            "type": "string",
            "description": "The county where the city is located."
          },
          "state": {
            "type": "string",
            "description": "The state where the city is located."
          },
          "population_2010": {
            "type": "integer",
            "description": "The population of the city as of the 2010 census."
          }
        },
        "required": [
          "city_name",
          "river_name",
          "county",
          "state",
          "population_2010"
        ],
        "additionalProperties": false
      }
    },
    "identified_river": {
      "type": "string",
      "description": "The name of the river that a city with an Emprise Bank branch is situated along."
    }
  },
  "required": [
    "bank_name",
    "cities_with_branches_on_river",
    "identified_river"
  ],
  "additionalProperties": false
}
