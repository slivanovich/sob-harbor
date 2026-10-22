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
Lyndon B. Johnson National Historical Park: Lyndon B. Johnson National Historical Park is a United States National Historical Park in central Texas about 50 miles west of Austin in the Texas Hill Country.  The park protects the birthplace, home, ranch, and final resting place of Lyndon B. Johnson, 36th President of the United States.  During Johnson's administration, the LBJ Ranch was known as the "Texas White House" because the President spent approximately 20% of his time in office there.

Joseph P. Remington: Joseph P. Remington (March 26, 1847 – January 1, 1918) was an eminent community pharmacist, manufacturer, and educator.  The Remington Medal awarded by the American Pharmacists Association, considered the most prestigious award given in the profession of pharmacy in the United States, is named after him.  He was an active participant and a supporter of the International Pharmaceutical Congress.

George Bush Intercontinental Airport: George Bush Intercontinental Airport (IATA: IAH, ICAO: KIAH, FAA LID: IAH) is an international airport in Houston, Texas, United States, under class B airspace, serving the Greater Houston metropolitan area, the fifth-largest metropolitan area in the United States.  Located about 23 mi north of Downtown Houston, between Interstate 45 and Interstate 69/U.S. Highway 59 with direct access to the Hardy Toll Road expressway, George Bush Intercontinental Airport has scheduled flights to a large number of domestic and international destinations.  The airport is named after George H. W. Bush, the 41st President of the United States.

Allen Ranch: The Allen Ranch, or Sam Allen Ranch, was one of the first and longest running ranches in the history of the state of Texas in the United States.  The ranch was started a few years after the Texas Revolution in what is now southeast Houston and Pasadena.  The ranch itself extended from Clear Lake to Harrisburg (in modern east Houston).  The cattle range covered much of southeast Harris County and Galveston County covering many of the modern communities around Galveston Bay.

Elvira, Illinois: Elvira is an unincorporated community in Johnson County, Illinois, United States.  The closest city to Elvira is Buncombe, which is about 3 mi to the southeast.  No numbered highways pass through Elvira; the closest state highway is Illinois Route 37, to the east.

West Texas Boys Ranch: West Texas Boys Ranch (WTBR) is a Christian private residential community for boys located in Tankersley, unincorporated Tom Green County, Texas, near San Angelo.  The 963 acre facility is a 501(c)3 nonprofit organization, and it is open to any qualified boy, regardless of his or his family's ability to pay the tuition.  The ranch uses donations to fund its services.  The ranch can accommodate up to 40 boys, who come from across the United States.  The ranch does not take custody of its boys, and it is not a boot camp, detention center, drug rehabilitation center, or a "last resort" for hardcore juvenile offenders.

Santa Gertrudis cattle: Santa Gertrudis cattle are a tropical beef breed of cattle developed in southern Texas on the King Ranch.  They were named for the Spanish land grant where Captain Richard King originally established the King Ranch.  This breed was officially recognized by the United States Department of Agriculture in 1940, becoming the first beef breed formed in the United States.  The origin given by King Ranch is that it was formed by mating Brahman bulls with Beef Shorthorn cows, with the final composition being about three-eighths Brahman and five-eighths Shorthorn.  In 1918, the King Ranch purchased 52 bulls of three-quarters to seven-eighths "Bos indicus" breeding to mate with 2500 pure-bred Shorthorn cows on the ranch.  At this time, the American Brahman breed as such did not exist, nor were purebred "Bos indicus" cattle available in the United States.

Rancho Viejo, Texas: Rancho Viejo is a town in Cameron County, Texas, United States.  The population was 2,437 at the 2010 census.  The town is named from a ranch in that area named "Rancho Viejo" (Old Ranch).  This ranch was owned by Blas María de la Garza Falcón, whose name was given to a nearby dam, Falcon Dam.

Waggoner Ranch: The Waggoner Ranch is an historic north Texas ranch located 13 miles south of Vernon, Texas.  The land was used primarily to raise crops, beef cattle and horses as well as for oil production.  It was notable for being the largest ranch under one fence in the United States.  It was originally established in 1852 near Vernon, Texas by Daniel Waggoner under the name of Dan Waggoner & Son; his son being William Thomas Waggoner.  It was acquired by Stan Kroenke, who is married to Ann Walton (niece of Sam Walton), in February 2016.  At the time of acquisition, the ranch comprised 520,527 acres , or 800 mi2 but additional acreage was included in the sale making the total closer to 535,000 acres .

Remington Ranch, Texas: Remington Ranch is a master planned community located in unincorporated Harris County, Texas.  The development, with 2,100 single-family houses, is located between Interstate 45 and the Hardy Toll Road.  It is north of Greenspoint Mall and in proximity to George Bush Intercontinental Airport.

Question: The airport closest to Remington Ranch, Texas was named after what numbered President of the United States?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "airport_name": {
      "type": "string",
      "description": "The name of the airport closest to Remington Ranch."
    },
    "named_after_president": {
      "type": "string",
      "description": "The name of the President after whom the airport was named."
    },
    "president_number": {
      "type": "integer",
      "description": "The ordinal number of the President."
    },
    "location_proximity": {
      "type": "string",
      "description": "Description of the proximity between the ranch and the airport."
    }
  },
  "required": [
    "airport_name",
    "named_after_president",
    "president_number",
    "location_proximity"
  ],
  "additionalProperties": false
}
