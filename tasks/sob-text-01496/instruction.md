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
Conejo Valley Airport: Conejo Valley Airport, also known as Janss Airport, was an airport in Thousand Oaks, California.  It had a 2,600 foot runway and was located adjacent to Thousand Oaks Boulevard.  The airport opened in 1926, but was relocated in the early 1960s.  The new airport, known as Rancho Conejo Airport, was established on the south side of State Highway 101.  Various movies were filmed at Conejo Valley Airport, including "The Paleface" (1948), "Riders of the Whistling Pines" (1949), and "Overland Stage Raiders" (1938).  Rancho Conejo Airport appeared in the film "It's a Mad, Mad, Mad, Mad World" (1963).

Chippewa Valley Regional Airport: Chippewa Valley Regional Airport (IATA: KEAU, ICAO: EAU) is a public use airport in Chippewa County, Wisconsin, United States.  The airport is owned by Eau Claire county and is located three nautical miles (6 km) north of the central business district of the city of Eau Claire, Wisconsin.

Orrin Henry Ingram: Orrin Henry Ingram (May 13, 1830 – October 16, 1918) was an American lumber baron and philanthropist from Eau Claire, Wisconsin.  Orphaned at age 11, he established sawmills in Ontario, Canada, and the Chippewa Valley of Wisconsin.  He was responsible for the deforestation of the Chippewa Valley and the establishment of many small towns in the area.  He was a banker and philanthropist in Eau Claire.

Yampa Valley Airport: Yampa Valley Regional Airport (IATA: KHDN, ICAO: HDN) is in Routt County, Colorado, two miles southeast of Hayden and about 25 mi west of Steamboat Springs.  Also known as Yampa Valley Regional Airport, it has the only scheduled passenger flights to northwest Colorado.  It is also used by larger business jets that cannot use the smaller Steamboat Springs Airport (Bob Adams Field).

State Theatre (Eau Claire, Wisconsin): The State Theatre is a nonprofit venue for the performing arts and entertainment, located in downtown Eau Claire, Wisconsin with seating for 1100 people.  It was first opened as a vaudeville theatre in 1926, then several years later converted to a movie house that closed in 1982.  In 1984 the Theatre was donated to a group of arts-minded community members called the Eau Claire Regional Arts Council to create a center for artistic expression.  After a significant renovation it reopened the doors in 1986.  It is now used by a number of local performing arts organizations including: Chippewa Valley Symphony, Chippewa Valley Theatre Guild, Chippewa Valley Youth Choirs, Eau Claire Children's Theatre, Valley Gospel Choir and UW - Eau Claire.

Chippewa Valley High School: Chippewa Valley High School is a public high school located in Clinton Township, Macomb County, Michigan, located in the Detroit Metropolitan Area.  The school is one of three high schools operated by Chippewa Valley Schools.  Starting with the 2008-2009 school year, Chippewa Valley High School opened its Ninth Grade Center.  The ninth grade center's current principal is Diane Zatkoff while the current principal for the main campus is Jerry Davisson.

Chippewa Valley Schools: Chippewa Valley Schools is a school district with its headquarters located in Clinton Township, Macomb County, Michigan.  The Chippewa Valley School district covers 28 square miles serving in the Clinton and Macomb Townships.  It is the eighth largest school district out of 788 public and charter schools in Michigan and the second largest school district in Macomb County.  Chippewa Valley school district teaches 16,300 students each day.  Those students attend school at twelve Elementary, four Middle, two ninth grade centers, three High Schools, one International Academy of Macomb (IAM) High School, and one preschool center.

Greenbrier Valley Airport: Greenbrier Valley Airport (IATA: KLWB, ICAO: LWB) is a public airport three miles (5 km) north of Lewisburg in Greenbrier County, West Virginia, United States.  It has one runway and is owned by the Greenbrier County Airport Authority.  Silver Airways ("United Express") has scheduled airline flights, subsidized by the Essential Air Service program, to Washington-Dulles International Airport, which replaced Cleveland-Hopkins International Airport in summer 2012.  Silver Airways also flies to Atlanta-Hartsfield International Airport as an independent airline, replacing Delta Connection.

Marana Regional Airport: Marana Regional Airport (IATA: AVW, ICAO: KAVQ, FAA LID: AVQ) , also known as Marana Northwest Regional Airport or Avra Valley Airport, is a general aviation airport in Marana, Arizona, about 15 miles (24 km) northwest of Tucson.  In 1999, the airport was purchased from Pima County by the town of Marana.

Peter Truax: Peter Truax (February 24, 1828 – March 18, 1909) was a philanthropist, businessman, farmer, and third-party politician in the Chippewa Valley of Wisconsin.  Truax was a prominent figure in the Chippewa Valley and one of the richest men in the county.  His acquisition of wealth was due to the many business ventures he took part in.  Truax was one of the leaders of the Prohibitionist movement in the state and was nominated for state and federal office by organizations of that party on several occasions.  He owned large stocks in the Bank of Eau Claire and the New Bank of Eau Claire.

Question: What country are the Chippewa Valley Regional Airport and Greenbrier Valley Airport in?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "airports": {
      "type": "array",
      "description": "List of airports and their respective countries.",
      "items": {
        "type": "object",
        "properties": {
          "airport_name": {
            "type": "string",
            "description": "The name of the airport."
          },
          "location_country": {
            "type": "string",
            "description": "The country where the airport is located."
          }
        },
        "required": [
          "airport_name",
          "location_country"
        ],
        "additionalProperties": false
      }
    },
    "common_country": {
      "type": "string",
      "description": "The country that all listed airports are located in."
    },
    "all_airports_in_same_country": {
      "type": "boolean",
      "description": "Indicates if all listed airports are located in the same country."
    }
  },
  "required": [
    "airports",
    "common_country",
    "all_airports_in_same_country"
  ],
  "additionalProperties": false
}
