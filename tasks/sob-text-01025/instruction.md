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
Midea Group: Midea Group () is a Chinese electrical appliance manufacturer, headquartered in Beijiao, Shunde, Foshan, Guangdong.  As of 2013, the firm employs approximately 100,000 people in China and overseas across 21 manufacturing plants and 260 logistics centers across 200 countries.  Midea Group is listed on Shenzhen Stock Exchange since 2013.  It has been listed on the Fortune Global 500 since July 2016.  Midea produces wide ranges of lighting, water appliances, floor care, small kitchen appliances, laundry, large cooking appliances, and refrigeration appliances.  It also has a long history in producing home and commercial solutions in air conditioning and heating (HVAC).  In the summer of 2016, Midea made a highly publicized move to acquire German robotics company KUKA.

Waller High School: Waller High School ( ) is a public high school in unincorporated Harris County, Texas, north of Waller, and classified as a 5A school by the UIL.  It is part of the Waller Independent School District and serves students from Waller, Pine Island, Prairie View, unincorporated sections of Waller County (including Fields Store), and unincorporated sections of Harris County (including Hockley).  In 2013, the school was rated "Met Standard" by the Texas Education Agency.

KILT (AM): KILT (610 AM, "SportsRadio 610") is a Sports/Talk formatted radio station in the Houston, Texas, metropolitan area.  The station is currently owned by CBS Radio.  KILT shares its call letters with its sister station 100.3 FM, which airs a country music format.  Its studios are located in the Greenway Plaza district, and its transmitter is located on West Road, between Ella Boulevard and the Interstate 45 North Freeway, near Greenspoint in unincorporated Harris County.

Schlumberger: Schlumberger Limited (] ) is the world's largest oilfield services company.  Schlumberger employs approximately 100,000 people

Lithia Motors: Lithia Motors, Inc. is an American nationwide automotive retailer headquartered in Medford, Oregon.  It is the fourth largest automotive retailer in the United States.  In 2015, Lithia Motors broke into the Fortune 500 list at #482, making it one of only three Oregon-based companies in the Fortune 500.  This followed a year that saw the acquisition of the DCH Auto Group, one of the 10 largest dealer groups in the country, with 27 dealerships, before being purchased by Lithia Motors.  In 2016, Lithia climbed to #346 and that same year made the Fortune 500 List of Top Ten Companies with the biggest Jump in rank on the Fortune 500.  Today, Lithia is ranked #318 on the Fortune 500.  Lithia employs more than 11,100 people in stores across the nation including Alaska and Hawaii.  Lithia operates 160 stores in 18 states.

Smith International: Smith International was a Fortune 500 company headquartered in the Greenspoint district and in unincorporated Harris County, Texas.  Smith International ceased to exist as an independent company following the merger with Schlumberger.  This company supplies products to gas and oil production and exploration companies.  The company used to be easily identified by its red Sii logo.  The company had recently changed its logo to consist of the word "SMITH" in black capital letters with a green globe.

KBME (AM): KBME (branded as Sportstalk 790) AM is a sports-talk radio station in the Houston, Texas metropolitan area.  It is currently owned by iHeartMedia, Inc..  The station airs local sports-talk and carries nationally syndicated Fox Sports Radio programming.  KBME is also the flagship radio station for the Houston Rockets, Houston Astros and Texas Longhorns.  The station's studios are located along the West Loop Freeway in the city's Uptown district.  The transmitter site is located at what is now the southwest corner of Fallbrook Drive and T.C. Jester Boulevard, near Greenspoint in unincorporated Harris County.

Aldine Independent School District: The Aldine Independent School District is a public school district based in unincorporated Harris County, Texas, United States.  It serves portions of Houston and unincorporated Harris County.  Aldine ISD serves the communities of Aldine, most of Greenspoint, most of East Aldine, and portions of Airline, Acres Homes, Kinwood, Bordersville, and Inwood Forest.  The district is part of the taxation base for the Lone Star College System.  As of August 2014, Dr. Wanda Bamberg serves as superintendent of schools.

List of highways in Harris County, Texas: The state highways in Harris County, Texas consists of approximately 1213 mi of routes in the Texas state highway system that are located within Harris County.  These highways are maintained by the Texas Department of Transportation (TxDOT).  These highways are made up of Interstate Highways, U.S. Highways, State Highways, State Loop and Spur Highways, Farm to Market Roads, Park Highways, and Alternate and Business Routes.  In addition to these highways, three independent Toll Roads and a section of Interstate 10 that is toll managed are also located in Harris County.  These roads are maintained by the Harris County Toll Road Authority, and add approximately 120 mi of highways to the overall Harris County highway system.

Nimitz High School (Harris County, Texas): Chester W. Nimitz Senior High School is a public secondary school made up of two campuses located in unincorporated Harris County, Texas, United States.  The campuses have Houston addresses.  The school is located directly across the street from Lone Star College–North Harris and west of Bush Intercontinental Airport The school serves portions of Houston, the Aldine Independent School District portion of Humble, and unincorporated areas of Harris County.  Nimitz is one of five high schools in Aldine ISD.  The main campus serves grades 10 through 12, while Nimitz Ninth Grade Center serves grade 9.

Question: The company that  employs approximately 100,000 people and had a merger with a Fortune 500 company headquartered in the Greenspoint district and in unincorporated Harris County, Texas, is the worlds largest what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "company_name": {
      "type": "string",
      "description": "The name of the company that fits the description."
    },
    "employee_count": {
      "type": "integer",
      "description": "The approximate number of people employed by the company."
    },
    "merged_company_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the company it merged with."
        },
        "is_fortune_500": {
          "type": "boolean",
          "description": "Indicates if the merged company was a Fortune 500 company."
        },
        "headquarters_location": {
          "type": "string",
          "description": "The headquarters location of the merged company."
        }
      },
      "required": [
        "name",
        "is_fortune_500",
        "headquarters_location"
      ],
      "additionalProperties": false
    },
    "company_classification": {
      "type": "string",
      "description": "The classification of the company (e.g., 'world's largest oilfield services company')."
    }
  },
  "required": [
    "company_name",
    "employee_count",
    "merged_company_details",
    "company_classification"
  ],
  "additionalProperties": false
}
