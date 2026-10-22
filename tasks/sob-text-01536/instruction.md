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
Armstrong School District (Pennsylvania): The Armstrong School District is a large, public school district which encompasses approximately 437 sqmi .  The District is one of the 500 public school districts of Pennsylvania.  In Armstrong County, Pennsylvania, Armstrong School District covers the Boroughs of Applewold, Atwood, Dayton, Elderton, Ford City, Ford Cliff, Kittanning, Manorville, Rural Valley, West Kittanning and Worthington and the Townships of Bethel Township, Boggs Township, Burrell Township, Cadogan Township, Cowanshannock Township, East Franklin Township, Kittanning Township, Manor Township, North Buffalo Township, Pine Township, Plumcreek Township, Rayburn Township, South Bend Township, Valley Township, Washington Township, Wayne Township and West Franklin Township.  In Indiana County, Pennsylvania the district includes the Borough of Smicksburg and West Mahoning Township.  According to 2000 federal census data, it served a resident population of 44,970.  By 2010, the District's population declined to 43,301 people.  In 2009, Armstrong School District residents' per capita income was $15,449, while the median family income was $36,907.

The Century for Young People: The Century for Young People is a non-fiction history book written by Peter Jennings and Todd Brewster.  This book is an version of "The Century", adapted by Jennifer Armstrong.  The book contains over 200 pictures to depict the 100 years of history.

Jennifer Armstrong: Jennifer Mary Armstrong (born May 19, 1961) is an American children's writer known for both fiction and non-fiction.  She was born in Waltham, Massachusetts, grew up outside of New York City, and now lives in Saratoga Springs, New York.  She was formerly married to the author James Howard Kunstler.

Demographics of Mexico: With a population of over 123 million in 2017, Mexico ranks as the 10th most populated country in the world.  It is the most populous Spanish-speaking country and the third-most populous in the Americas after United States and Brazil.  Throughout most of the twentieth century Mexico's population was characterized by rapid growth.  Although this tendency has been reversed and average annual population growth over the last five years was less than 1%, the demographic transition is still in progress, and Mexico still has a large cohort of youths.  The most populous city in the country is the capital, Mexico City, with a population of 8.9 million (2016), and its metropolitan area is also the most populated with 20.1 million (2010).  Approximately 50% of the population lives in one of the 55 large metropolitan areas in the country.  In total, about 78.84% of the population of the country lives in urban areas, meaning that only 21.16% live in rural areas.

Spallumcheen: Spallumcheen is a district municipality in the Canadian province of British Columbia.  Located in the Okanagan region between Vernon and Enderby, the township had a population of 5,055 and land area of 255.77 sqkm in the Canada 2011 Census.  The district, whose official name is the Township of Spallumcheen and which is the oldest rural municipality in the British Columbia Interior (incorporated in 1892), consists primarily of agricultural land surrounding the separately incorporated City of Armstrong.  Both Spallumcheen and Armstrong are member municipalities of the Regional District of North Okanagan.

Sara Garden Armstrong: Sara Garden Armstrong is an American artist who lives and works in New York City.  Armstrong creates sculptures, paintings, drawings from miniature to wall size, artist's books, multimedia artworks involving computers sound and light, and constructs permanent installations in atrium spaces.  Armstrong received her Master of Fine Arts from the University of Alabama in Tuscaloosa and her Master of Art Education from the University of Alabama at Birmingham.  Armstrong also studied art at New York University and with the University of Windsor, Windsor, Ontario in Yeovil, England while attending UAB.  An educator for several years at the University of Alabama at Birmingham, she moved to New York City in 1981.

Davenport, Iowa: Davenport is the county seat of Scott County in Iowa and is the largest of the Quad Cities, a metropolitan area with a population estimate of 382,630 and a CSA population of 474,226, making it the 90th largest CSA in the nation.  Davenport was founded on May 14, 1836 by Antoine Le Claire and was named for his friend, George Davenport, a colonel during the Black Hawk War stationed at nearby Fort Armstrong.  According to the 2010 census, the city had a population of 99,685 (making it Iowa's third-largest city).  However, the city is currently appealing this figure, arguing that the Census Bureau missed a section of residents that would place the total population over 100,000, and indeed, even the Census Bureau's own "estimate" for Davenport's 2011 population is 100,802.

Saratoga Springs, New York: Saratoga Springs is a city in Saratoga County, New York, United States.  The population was 26,586 at the 2010 census.  The name reflects the presence of mineral springs in the area, which has made Saratoga a popular resort destination for over 200 years.  The city is just north of Ballston Spa, in the heart of New York's Capital Region.

Armstrong, Iowa: Armstrong is a city in Emmet County, Iowa, United States.  The population was 926 at the 2010 census.  It was originally known as Armstrong Grove.

Jennifer Armstrong (disambiguation): Jennifer Armstrong is an author.

Question: What is the population of the city where Jennifer Armstrong now lives?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "author_name": {
      "type": "string",
      "description": "The name of the author."
    },
    "current_city": {
      "type": "string",
      "description": "The city where the author currently lives."
    },
    "city_population": {
      "type": "integer",
      "description": "The population of the city where the author lives."
    },
    "population_census_year": {
      "type": "integer",
      "description": "The year the population data was recorded."
    }
  },
  "required": [
    "author_name",
    "current_city",
    "city_population",
    "population_census_year"
  ],
  "additionalProperties": false
}
