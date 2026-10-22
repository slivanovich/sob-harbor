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
Columbus Wardogs: The Columbus Wardogs are a defunct af2 team that played their home games in the Columbus Civic Center in Columbus, Georgia from 2001 - 2004.  The Wardogs became famous in 2001 and received a mention on ESPN as the first professional football team to finish a 16-game season winless.  The inactive club was sold during the summer of 2005 and renamed the Mississippi Headhunters after relocating to Biloxi, Mississippi.  The team was not able to begin play in Biloxi due to damage to the Mississippi Coast Coliseum by Hurricane Katrina.  The owner of the team, Greg Disotell, had planned on building a new 12,000-seat arena, called Jackson Sports Arena, for his team in Pearl, Mississippi (a suburb of Jackson) but he was not able to secure funding.  The franchise continued to be dormant until it ceased to exist along with the rest of the AF2 following the 2009 season.

Biloxi Yacht Club: The Biloxi Yacht Club (BYC) is located in Biloxi, Mississippi on the shores of the Mississippi Sound.  The BYC is a founding member of the Gulf Yachting Association, as well as the Mississippi Coast Yachting Association.  Established in 1849, it is the fourth oldest yacht club in the United States.

Coast Transit Authority: The Coast Transit Authority is the primary provider of mass transportation in the Gulfport–Biloxi metropolitan area.  Service was founded in 1974, after the Mississippi State Legislature passed a bill authorizing the creation of public transit for the region; the area's previous private bus operator, Municipal Transit Lines, had been devastated by Hurricane Camille, and the area was left with no public transportation for a 3-year period after the disaster.  Originally known as the Mississippi Coast Transit Authority, the agency changed its name to Coast Area Transit in 1985, before arriving on its current moniker in 1992.

Mississippi Renewal Forum: The Mississippi Renewal Forum was a design charrette in which over 200 community leaders and design professionals worked together to plan the rebuilding of the Mississippi Coast post-hurricane Katrina.  In the course of a week in October 2005, the charrette’s design teams generated new plans and codes for all eleven municipalities along the Mississippi coast, including Waveland, Bay St. Louis, Pass Christian, Long Beach, Gulfport, Biloxi, D’Iberville, Ocean Springs, Gautier, Pascagoula and Moss Point.

CoastCon: CoastCon is Mississippi's longest running and largest science fiction, fantasy and gaming convention.  It is the main sponsored event of CoastCon, Inc., a non-profit literary organization.  CoastCon, Inc. and its ten-member volunteer board develop events and gatherings to promote reading, education, fellowship, and science fiction, fantasy and gaming in all formats across the Southern United States, for over thirty-five years.  The next CoastCon annual convention, CoastCon 40, will be held March 3-5, 2017, at the Mississippi Coast Coliseum and Convention Center in Biloxi, Mississippi.

Mississippi Coast Yachting Association: The Mississippi Coast Yachting Association was organized to promote the sport of yacht racing on the Mississippi Gulf Coast and nearby areas.

Mississippi Beach Kings: The Mississippi Beach Kings were an indoor soccer team based in Biloxi, Mississippi.  They played their games in the Mississippi Coast Coliseum.  They were members of the Eastern Indoor Soccer League and played only during the 1998 season.  During the 1997 season, the team played in Columbus, Georgia as the Columbus Comets.

Jackson Wildcats: The Jackson Wildcats were a United States Basketball League team located in Jackson, Mississippi.  The Wildcats were originally located in Glens Falls, New York as the Adirondack Wildcats.  The new ownership announced the move to Mississippi on 1 December 2006.  Plans for the team to play at the Mississippi Coast Coliseum were nixed when the team and venue could not agree on a lease; the Wildcats later played some home games at a local community center.  As of May 1, 2007, the Jackson Wildcats were removed from the USBL schedule.

Bay St. Louis, Mississippi: Bay Saint Louis is a city in and the county seat of Hancock County, Mississippi, in the United States.  It is part of the Gulfport–Biloxi Metropolitan Statistical Area.  As of the 2010 census, the city had a total population of 9,260.  The city is recovering population lost in 2005 due to Hurricane Katrina, and the Census Bureau's 2016 population estimate was 12,667.

Mississippi Sea Wolves: The Mississippi Sea Wolves were a professional hockey team based in Biloxi, Mississippi and playing in the Mississippi Coast Coliseum.  The Sea Wolves were members of the ECHL.

Question: What is a county on the Mississippi coast?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "county_name": {
      "type": "string",
      "description": "The name of the county located on the Mississippi coast."
    },
    "associated_city": {
      "type": "string",
      "description": "A city within the county that is explicitly mentioned as being on the Mississippi coast."
    },
    "is_county_seat": {
      "type": "boolean",
      "description": "Indicates if the associated city is the county seat of the identified county."
    },
    "metropolitan_area": {
      "type": "string",
      "description": "The metropolitan statistical area that the county or city is part of."
    }
  },
  "required": [
    "county_name",
    "associated_city",
    "is_county_seat",
    "metropolitan_area"
  ],
  "additionalProperties": false
}
