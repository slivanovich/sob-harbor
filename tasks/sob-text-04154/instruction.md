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
First Church of Christ, Scientist (Seattle): First Church of Christ, Scientist Building is an historic Christian Science church located at 1519 East Denny Way / 1841 16th Avenue on the corner of East Denny Way and 16th Avenue in the Capitol Hill neighborhood of Seattle, Washington.  Designed in the Classical Revival style, it was built of Bedford limestone between 1906 and 1909.  Established in August 1896, First Church first held services in various rented buildings or halls until building its first church building on the corner of 6th Avenue and Marion Street.  This was completed in time for its first service on Easter Sunday, April 7, 1901.  This was soon outgrown and in November 1906 a contract was signed to purchase the Denny Way property.  In August 1908, services began in a temporary wooden structure that was built on the completed foundation of the new church.  On January 17, 1977 the building was declared a City of Seattle historic landmark.  In 2006 the congregation made the decision to move to the South Lake Union neighborhood to be in a more active urban location.  The building on East Denny Way was sold to a developer who has since converted it into townhouse project called The Sanctuary.  First Church of Christ, Scientist, Seattle, now holds services at 900 Thomas Street and is still an active branch of the Christian Science Mother Church.

750 7th Avenue: 750 Seventh Avenue is a 615 ft (187m) tall Class-A office skyscraper in New York City.  It was completed in 1989 in the postmodern style and has 36 floors.  Kevin Roche John Dinkeloo & Associates designed the building, and it is owned by Hines, a Texas based real estate investment company.  The building's continuous helix design, culminating in a chimney-like extension, was caused by the New York City Building Code, which requires setbacks.  The 84 exterior column transfers exist because of the owner's requirement for a column-free space.  It is tied with the New York Life Building for the 74th tallest building in New York City.  It is also LEED certified.

South Phoenix: South Phoenix is a region of Phoenix, Arizona, with the boundaries of the Gila River Indian Community to the south and west, 48th Street or Interstate-10 (Phoenix/Tempe and Phoenix/Chandler borders) to the east, and the Salt River to the north.  This area includes Phoenix's following Urban Villages: South Mountain Village (aka South Mountain District) along with Laveen Village and Ahwatukee Village.  The area is sometimes simply referred to as "the Southside" by its residents.  Major arterial east-west streets include Broadway Road, Southern Avenue, Baseline Road, Dobbins Road, Elliott Road, Warner Road, Chandler Boulevard, and Pecos Road, most of which connect South Phoenix with the suburbs of Tempe and Chandler.  Major arterial south-north streets include 24th Street, 16th Street, 7th Street, Central Avenue, 7th Avenue, and 19th Avenue connecting South Mountain Village to Central and North Phoenix; 27th Avenue, 35th Avenue, 43rd Avenue, 51st Avenue, 59th Avenue, 67th Avenue, and 75th Avenue connecting Laveen to west Phoenix; and 32nd Street, 40th Street, and 48th Street connecting South Mountain Village to east Phoenix and Tempe.

Moline Downtown Commercial Historic District: Moline Downtown Commercial Historic District is a historic district located in Moline, Illinois, United States.  Centered on 5th Avenue, it is roughly bounded by 12th Street to 18th Street, 4th Avenue to 7th Avenue.  The distinct covers 33 acres and includes 114 buildings.  One hundred of the buildings contribute to the significance of the district because they retain their historic and architectural integrity and reflect the character of the historic downtown.

Hounsfield Heights/Briar Hill, Calgary: Hounsfield Heights/Briar Hill is an inner suburban neighbourhood in northwest Calgary, Alberta, Canada.  Located north of the Hillhurst and West Hillhurst communities, the boundaries of the district are 16th Avenue N (Trans-Canada Highway)to the north; 14th Street W to the east; Lane north of 7th Avenue N to 19th Street W and 8th Avenue N to the south; and Crowchild Trail, 12th Avenue N, Juniper Road, and 22nd Street W to the west.  Lions Park C-Train station is located within the community.  The community is built on an escarpment and is popular for its views of downtown to the south and the Rocky Mountains to the west.

Greenwich Avenue: Greenwich Avenue, formerly Greenwich Lane, is a southeast-northwest avenue located in the Greenwich Village neighborhood of Manhattan, New York City.  It extends from the intersection of 6th Avenue and 8th Street at its southeast end to its northwestern end at 8th Avenue between 14th Street and 13th Street.  It is sometimes confused with Greenwich Street.  Construction of West Village Park, bounded by Greenwich Avenue, 7th Avenue, and 12th Street, began in 2016.

5th Avenue Theatre: The 5th Avenue Theatre (often referred to as 5th Avenue or the 5th) is a landmark theatre building located in Seattle, Washington.  It has hosted a variety of theatre productions and motion pictures since it opened in 1926.  The building and land is owned by the University of Washington and was once part of the original campus.  It is operated as a venue for nationally touring Broadway and original shows by the non-profit 5th Avenue Theatre Association.  The theatre, located at 1308 Fifth Avenue in the historic Skinner Building, has been listed on the U.S. National Register of Historic Places since 1978.

Virginia Dare Dresses, Incorporated: Virginia Dare Dresses, Incorporated operated a chain of retail stores in New York City.  Based at 462 7th Avenue (Manhattan), the company became a casualty of the Great Depression.  In March 1933 it went into receivership, with a court-appointed receiver being named.  In October 1934 the business emerged from financial difficulty and leased 10000 sqft of space in the Penn Terminal Building at 370 7th Avenue.  Philip Wise, another women's wear chain, and Wheelan Studios, rented property in the same building.  The re-emergent organization was known as Virginia Dare Stores, Inc.  It is important for having survived in a turbulent economic time in United States history.

High Springs Historic District: The High Springs Historic District is a U.S. historic district (designated as such on October 31, 1991) located in High Springs, Florida.  It encompasses approximately 750 acre , bounded by Northwest 14th Street, Northwest 6th Avenue, Southeast 7th Street and Southwest 5th Avenue.  It contains 218 historic buildings.

W. R. Grace Building: The W. R. Grace Building is a skyscraper in Manhattan, New York City.  The building was designed principally by Gordon Bunshaft, and completed in 1974.  The building was commissioned by the W.R. Grace Company, and was also used by the Deloitte & Touche, LLP.

Question: What do 750 7th Avenue and W. R. Grace Building have in common?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "entity_1_name": {
      "type": "string",
      "description": "The name of the first entity."
    },
    "entity_2_name": {
      "type": "string",
      "description": "The name of the second entity."
    },
    "common_attributes": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of attributes common to both entities."
    },
    "shared_location": {
      "type": "string",
      "description": "The shared geographical location of both entities."
    },
    "shared_building_type": {
      "type": "string",
      "description": "The shared type of building for both entities."
    }
  },
  "required": [
    "entity_1_name",
    "entity_2_name",
    "common_attributes",
    "shared_location",
    "shared_building_type"
  ],
  "additionalProperties": false
}
