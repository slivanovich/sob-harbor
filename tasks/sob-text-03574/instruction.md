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
Queens: Queens is the easternmost and largest in area of the five boroughs of New York City.  It is geographically adjacent to the borough of Brooklyn at the southwestern end of Long Island, and to Nassau County farther east on Long Island; in addition, Queens shares water borders with the boroughs of Manhattan and the Bronx.  Coterminous with Queens County since 1899, the borough of Queens is the second-largest in population (after Brooklyn), with a census-estimated 2,333,054 residents in 2016, approximately 48% of them foreign-born.  Queens County also is the second-most populous county in the U.S. state of New York, behind the neighboring borough of Brooklyn, which is coterminous with Kings County.  Queens is the fourth-most densely populated county among New York City's boroughs, as well as in the United States.  If each of New York City's boroughs were an independent city, Queens also would be the nation's fourth most populous, after Los Angeles, Chicago, and Brooklyn.  Queens is the most ethnically diverse urban area in the world.

Los Angeles: Los Angeles ( ; Spanish for "The Angels"; ] ), officially the City of Los Angeles and often known by its initials L.A., is the cultural, financial, and commercial center of Southern California.  With a U.S. Census-estimated 2016 population of 3,976,322, it is the second most populous city in the United States (after New York City) and the most populous city in the state of California.  Located in a large coastal basin surrounded on three sides by mountains reaching up to and over 10000 ft , Los Angeles covers an area of about 469 sqmi .  The city is also the seat of Los Angeles County, the most populated county in the country.  Los Angeles is the center of the Los Angeles metropolitan area, with 13,131,431 residents, and is part of the larger designated Los Angeles-Long Beach combined statistical area (CSA), the second most populous in the nation with a 2015 estimated population of 18.7 million.

Staten Island: Staten Island is one of the five boroughs of New York City in the U.S. state of New York.  In the southwest of the city, Staten Island is the southernmost part of both the city and state of New York, with Conference House Park at the southern tip of the island and the state.  The borough is separated from New Jersey by the Arthur Kill and the Kill Van Kull, and from the rest of New York by New York Bay.  With a 2016 Census-estimated population of 476,015, Staten Island is the least populated of the boroughs but is the third-largest in area at 58 sqmi .  Staten Island is the only borough of New York with a non-Hispanic White majority.

David Graham (photographer): David Graham (born 1952, Abington, Pennsylvania) is an American artist photographer and professor at the University of the Arts in Philadelphia.  He currently lives and works in Newtown, Pennsylvania.  Embracing popular forms of American photography (the snapshot, family portrait, and vacation photo), David Graham explores contemporary culture through the idiosyncratic nature of the American landscape.  His work is in many collections, including the Museum of Modern Art, New York City; the San Francisco Museum of Modern Art; the Art Institute of Chicago; the Philadelphia Museum of Art; the George Eastman House, Rochester, New York; the International Center of Photography, New York City; and the Brooklyn Museum, New York.  He is represented by the Laurence Miller Gallery in New York City and the PDNB Gallery in Dallas, Texas.

List of artists from Brooklyn: Brooklyn is the most populous borough of New York City.  Many artists have originated from Brooklyn or relocated there.

Brooklyn: Brooklyn ( ) is the most populous borough of New York City, with a Census-estimated 2,629,150 residents in 2016.  It borders the borough of Queens at the southwestern end of Long Island, and has several bridge connections to the nearby boroughs of Staten Island and Manhattan.  Since 1896, Brooklyn has had the same boundaries as Kings County, the most populous county in the U.S. state of New York and the second-most densely populated county in the United States, after the county of New York (which is coextensive with the borough of Manhattan).

Islanders–Rangers rivalry: The Islanders–Rangers rivalry, also unofficially known as the "Battle of New York", is a rivalry between the New York Islanders and New York Rangers of the National Hockey League.  Both teams play in New York City, with the Rangers in the borough of Manhattan, and the Islanders in the borough of Brooklyn.  They are two of the three teams that play in the New York metropolitan area, the other being the New Jersey Devils who play in Newark, New Jersey.  The rivalry is an intra-city rivalry similar to the Mets–Yankees rivalry in Major League Baseball and join the recent Knicks–Nets rivalry and yesteryear's Dodgers–Giants rivalry as professional sports rivalries between teams based in New York City's most populous borough, Brooklyn, and the location of most of New York's corporate headquarters and shopping districts, Manhattan.

Anchorage, Alaska: Anchorage (officially called the Municipality of Anchorage) (Dena'ina Athabascan: "Dgheyaytnu") is a unified home rule municipality in the U.S. state of Alaska.  With an estimated 298,192 residents in 2016, it is Alaska's most populous city and contains more than 40 percent of the state's total population; among the 50 states, only New York has a higher percentage of residents who live in its most populous city.  All together, the Anchorage metropolitan area, which combines Anchorage with the neighboring Matanuska-Susitna Borough, had a population of 401,635 in 2016.

Demographics of Queens: The demographics of Queens, the second-most populous borough in New York City, are highly diverse.  No racial or ethnic group holds a 50% majority in the borough.

Roberto Gari: Roberto Gari (February 13, 1920 – January 22, 2008) was an American artist and actor.  He was born in Brooklyn and appeared in vaudeville under the name of Jackie Hayes from the age of 4.

Question: Roberto Gari was an American artist and actor born in the most populous borough of New York City, with how many Census-estimated residents in 2016?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person."
    },
    "birth_place": {
      "type": "string",
      "description": "The borough where the person was born."
    },
    "birth_place_details": {
      "type": "object",
      "properties": {
        "is_most_populous_borough": {
          "type": "boolean",
          "description": "Indicates if the birth place is the most populous borough of New York City."
        },
        "population_year": {
          "type": "integer",
          "description": "The year for which the population estimate is given."
        },
        "estimated_population": {
          "type": "integer",
          "description": "The Census-estimated population of the borough for the specified year."
        }
      },
      "required": [
        "is_most_populous_borough",
        "population_year",
        "estimated_population"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_name",
    "birth_place",
    "birth_place_details"
  ],
  "additionalProperties": false
}
