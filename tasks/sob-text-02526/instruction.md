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
Falls City Brewing Company: Falls City Brewing Company was based in Louisville, Kentucky, USA.  The company operated from 1905 until 1978.  After the company closed the Falls City brand was purchased by a group of investors who sold it in the late 1990s to the Pittsburgh Brewing Company who produced the brand until around 2007.  The brand name "Falls City Beer" was revived in 2010, and a beer is contract brewed at Sand Creek Brewing Company for a Louisville computer software entrepreneur.

Scottish &amp; Newcastle: Scottish & Newcastle plc was a brewing company headquartered in Edinburgh, Scotland which expanded significantly from its home base to become an international business with beer volumes growing almost tenfold.

Gunther Brewing Company: Gunther Brewing Company is a historic brewery building located at Baltimore, Maryland, United States.  The site comprises 15 masonry buildings.  The main structure is a five-story brick "L"-shaped Romanesque Revival-style brew house with a two-story brick ice plant built about 1910 and one- and two-story boiler room.  Additional brew houses built in 1936 and 1950 are also on the property.  The Tulkoff Factory and Warehouse was built about 1964.  It was home to the George Gunther, Jr.  Brewing Company, founded in 1900.  By 1959 it was the second largest brewery in Baltimore, when it produced 800,000 barrels per year and employed approximately 600 people.  Hamm's Brewing Company bought the Gunther Brewing Company in 1960.  Later acquired by the F. & M. Schaefer Brewing Company in 1963, the plant was closed in 1978.  The Tulkoff company briefly used the factory for their sauce products at the conclusion of all brewing operations.

Live at Bell's: Live At Bell's is the third release from the winners of the 2006 Telluride Bluegrass Festival Band Competition, Greensky Bluegrass.  Recorded in the summer of 2007 at their home base of Bell's Brewery, this album is the first

Tivoli Brewery Company (building): The Tivoli Brewery(now Tivoli Student Union) is a historic building originally home to the Tivoli Brewing Company.  It was designed by prominent Denver architect Frederick C. Eberley.  The building is located in the Auraria Neighborhood of Denver, Colorado.  Today the building is home to the Tivoli Student Union of the Auraria Campus, serving as a student center for the Metropolitan State University of Denver, Community College of Denver, and the University of Colorado Denver.  In August 2015 the revived Tivoli Brewing Company began brewing in a new facility inside the building, in the original brewing area.

Florida Brewing Company building: The Florida Brewing Company building is a historic brewery building that once housed Ybor City Brewing Company, which became Florida Brewing Company.  It has been restored and converted into a law office.  It is the tallest building in Tampa's Ybor City Historic District.

Christian Moerlein Brewing Co.: Christian Moerlein Brewing Co. is a private beer company that began production in 1853 in Cincinnati, Ohio by German immigrant Christian Moerlein.  Before closing its doors in 1919 as result of prohibition, Christian Moerlein was among the ten largest American breweries by volume.  In 1981, the brand was revived by the Hudepohl Brewing Company as a "better beer" a precursor to the current craft beer category and is considered a pioneer craft beer of today's craft beer movement.  In 1999, Hudepohl-Schoenling Brewing Co. sold out to a group of out-of-town owners, a sale that included the famed Christian Moerlein craft beer brand.  In 2004, Greg Hardman a Cincinnati resident purchased Christian Moerlein, as well as 65 other historic Cincinnati brands, returning local ownership to Cincinnati in a move that included a plan to return Cincinnati's grand brewing traditions.  The four phase plan was, 1) return the local ownership of Cincinnati's great beer brands to Cincinnati; 2) build their base of sales to; 3) open local brewing operations in the heart of Cincinnati's historic Brewery District and; 4) open a World-class Moerlein Lager House on the banks of the Ohio River to act as a signal that beer is back in Cincinnati.

Port City Brewing Company: Port City Brewing Company is a craft brewery in Alexandria, VA.  It is the first production brewery to operate in Alexandria since Prohibition, when the Robert Portner Brewing Company closed its doors.  Port City was named the 2015 Small Brewing Company of the Year at the Great American Beer Festival.

Bell's Brewery: Bell's Brewery, Inc. is a brewing company based in Kalamazoo, Michigan, with a second brewery in Comstock, Michigan.  Bell's Brewery produces the Bell's brand of beers.  Bell's also has a brewpub called the Eccentric Cafe.

Billy Beer: Billy Beer was a beer first made in the United States in July 1977, by the Falls City Brewing Company.  It was promoted by Billy Carter, whose older brother Jimmy was the incumbent President of the United States.  In October 1978, Falls City announced that it was closing its doors after less than a year of Carter's promotion.  The beer was produced by Cold Spring Brewing, West End Brewing, and Pearl Brewing Company.

Question: Live at Bell's was an album the band that has a home base at the brewing company in what city?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "album_name": {
      "type": "string",
      "description": "The name of the album mentioned in the context."
    },
    "band_name": {
      "type": "string",
      "description": "The name of the band that released the album."
    },
    "brewery_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the brewing company that is the band's home base."
        },
        "location_city": {
          "type": "string",
          "description": "The city where the brewing company is based."
        },
        "location_state": {
          "type": "string",
          "description": "The state where the brewing company is based."
        }
      },
      "required": [
        "name",
        "location_city",
        "location_state"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "album_name",
    "band_name",
    "brewery_details"
  ],
  "additionalProperties": false
}
