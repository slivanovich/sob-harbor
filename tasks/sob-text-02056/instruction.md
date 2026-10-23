{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nArea code 708: Telephone area code 708 covers western and southern Cook County and eastern and southern Will County in the state of Illinois, USA.  Area code 708 was split off from area code 312 on November 11, 1989, and once covered almost all of the suburbs of Chicago.  In 1996, area code 847 and area code 630 were broken off from 708.  Area code 464 is being reserved as an overlay area code for 708 to provide additional numbering options for this area.\n\nArea code 909: Area code 909 is a California telephone area code that covers far eastern Los Angeles County and southwestern San Bernardino County.  The 909 area code was split from area code 714 on November 14, 1992.  By August 1993 use of the new area code became mandatory.  Western Riverside County was split off from 909 into area code 951 on July 17, 2004.  Originally on that same date, the area retaining the 909 area code was to be overlaid by a new area code 752.  However, this overlay plan was shelved prior to the 909/951 split, and area code 752 was returned to the NANPA numbering pool to be assigned at a later date.  909 still covers small portions of Corona, Riverside, and Moreno Valley, which are in Riverside County.\n\nArea code 772: Area code 772 serves the Treasure Coast of the state of Florida.  It covers Sebastian, Fellsmere, Vero Beach, Fort Pierce, Port St. Lucie, Jensen Beach, Stuart, Hobe Sound, Indiantown, and other areas in east central Florida.  It was created in 2002 as a split from area code 561 when there was a need for more phone numbers (due in part to the increase of cell phone users).\n\nArea code 440: Area code 440 is a North American telephone area code for the state of Ohio, serving parts of the Greater Cleveland area, but not the city of Cleveland or most of its inner suburbs.  This area code was established August 16, 1997.  Area code 440 was formed by a three-way split of Area code 216, one of the original North American Numbering Plan codes.  Area code 330 was created in 1996 from the southern part of 216 and 440 was added the following year to keep up with the increasing number of cellular phones, as well as population factors.\n\nArea code 619: Area code 619 is a California telephone area code that was split from 714 on November 5, 1982.  This area code currently covers the southern half of the city of San Diego and its eastern and southern suburbs.  Area code 619 was the first new area code in the NANP since area code 804 was split off from 703 in 1973, and the second area code added since 1966.\n\nStuart, Florida: Stuart is a city in, and the seat of, Martin County, Florida, United States.  Located on Florida's Treasure Coast, Stuart is the largest of four incorporated municipalities in Martin County.  The population was 15,593 in the 2010 census.  It is part of the Port St. Lucie, Florida Metropolitan Statistical Area.\n\nArea code 928: North American area code 928 is a telephone area code in the state of Arizona that was created in a split from area code 520 on June 23, 2001, due mainly to population gains in Tucson, Yuma and Flagstaff.  928 covers northern, eastern, and western portions of Arizona.  The area code encompasses areas such as the Grand Canyon, Flagstaff, Holbrook, Lake Havasu City, Kingman, Prescott, Wickenburg, Winslow and Yuma, also serving the majority of Greenlee County.  The Arizona portion of the Navajo Nation is served by the 928 area code.  Some areas on the western and northern fringes of the Phoenix metropolitan area such as Lake Pleasant Regional Park in Peoria also fall within this area code.\n\nArea code 941: Area code 941 is an area code in Florida.  Introduced on March 3, 1996, it includes the counties of Manatee, Sarasota, and Charlotte, areas along the Sun Coast of southwestern Florida, USA.  DeSoto County, Hardee County, Polk County, Highlands County, Okeechobee County, Glades County, and Hendry County were part of this area code until 1999, and Lee County and Collier County were part of 941 until March 2003.  Before the 941 area code, the region was originally 305, then area code 813.\n\nArea code 863: 863 is the telephone area code in Florida which covers the Heartland, as well as Polk County in Central Florida.  Some of the larger and more notable cities in the 863 area code include Lakeland, Bartow, Winter Haven, Lake Wales, Sebring, Clewiston, Arcadia, Poinciana and Okeechobee City.  Because the area code has no overlays, it is not required to dial the area code when dialing from one location in the area code to another, unless calling from outside this territory.\n\nOld Martin County Courthouse: The Old Martin County Court House, built in 1937, is an historic Art Deco style courthouse building located at 80 East Ocean Boulevard in Stuart, Martin County, Florida.  In 1989, it was listed in \"A Guide to Florida's Historic Architecture\", published by the University of Florida Press.  On November 7, 1997, it was added to the U.S. National Register of Historic Places.  On March 15, 2007, it was added to the Martin County Historic Register by the Martin County Historic Preservation Board.  It is now known as the Courthouse Cultural Center and is the headquarters of the Arts Council, Inc., the designated local arts agency for Martin County.\n\nQuestion: This Martin County, Florida city with area code 772 is located on what coast?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"city_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the city.\"\n    },\n    \"county_name\": {\n      \"type\": \"string\",\n      \"description\": \"The county where the city is located.\"\n    },\n    \"state_name\": {\n      \"type\": \"string\",\n      \"description\": \"The state where the city is located.\"\n    },\n    \"area_code\": {\n      \"type\": \"integer\",\n      \"description\": \"The telephone area code for the city.\"\n    },\n    \"coast_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the coast where the city is located.\"\n    }\n  },\n  \"required\": [\n    \"city_name\",\n    \"county_name\",\n    \"state_name\",\n    \"area_code\",\n    \"coast_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "city_name": {
        "type": "string",
        "description": "The name of the city."
      },
      "county_name": {
        "type": "string",
        "description": "The county where the city is located."
      },
      "state_name": {
        "type": "string",
        "description": "The state where the city is located."
      },
      "area_code": {
        "type": "integer",
        "description": "The telephone area code for the city."
      },
      "coast_name": {
        "type": "string",
        "description": "The name of the coast where the city is located."
      }
    },
    "required": [
      "city_name",
      "county_name",
      "state_name",
      "area_code",
      "coast_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
