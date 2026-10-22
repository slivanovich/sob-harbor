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
Newbill-McElhiney House: Newbill-McElhiney House is a historic home located at St. Charles, St. Charles County, Missouri.  The original three-bay section was built in 1836, and expanded to five bays in the 1850s.  It is a two-story, five bay, Federal style brick dwelling.  It has a side-gable roof and features a three-bay central porch.  Also on the property is a contributing small two-story "L-plan" brick building rumored to have been used as a slave quarters.

Dr. John H. Stumberg House: Dr. John H. Stumberg House is a historic home located at St. Charles, St. Charles County, Missouri.  It was built in 1869-1870, and is a two-story, "T"-plan, red brick dwelling on a stone foundation.  It has a cross-gable roof with dormers and decorated cornice.

Oliver L. and Catherine Link House: Oliver L. and Catherine Link House is a historic home located at St. Charles, St. Charles County, Missouri.  It was built in 1895, and is a 2 1/2-story, Richardsonian Romanesque style yellow brick dwelling on a raised basement.  It has a hipped roof with cross gables and features a round tower with a conical roof and large round arched opening over the entryway.

St. Charles, Missouri: St. Charles is a city in, and the county seat of, St. Charles County, Missouri, United States.  The population was 65,794 at the 2010 census, making St. Charles the ninth-largest city in Missouri.  It lies to the northwest, and is a suburb of St. Louis, Missouri on the Missouri River.

St. Charles County Smartt Airport: St. Charles County Smartt Airport, also known as Smartt Field, is a county owned, public use airport in St. Charles County, Missouri, United States.  It is located nine nautical miles (17 km) northeast of the central business district of the City of St. Charles.  This facility is included in the National Plan of Integrated Airport Systems, which categorized it as a general aviation "reliever airport".

Samuel Stewart Watson House: Samuel Stewart Watson House, also known as Ermeling House, is a historic home located at St. Charles, St. Charles County, Missouri.  It was built in 1859, and is a two-story, Italianate style brick dwelling with a hipped roof.  It features a broad denticulated cornice with heavy brackets, segmentally arched windows, and a classically inspired portico.

Midtown Neighborhood Historic District: Midtown Neighborhood Historic District is a national historic district located at St. Charles, St. Charles County, Missouri.  The district encompasses 527 contributing buildings, 7 contributing sites, and 5 contributing objects in a predominantly residential section of St. Charles.  It developed between about 1838 and 1959, and includes representative examples of Federal, Greek Revival, Gothic Revival, Italianate, Queen Anne, Romanesque Revival, Folk Victorian, Colonial Revival, Classical Revival, Tudor Revival, and Bungalow / American Craftsman style architecture.  Located in the district are the separately listed African Church and Oliver L. and Catherine Link House.  Other notable buildings include the St. Charles County Courthouse, Benton School (1896), St. John’s A.M.E. Church (1872), Immanuel Lutheran Church (1867), Jefferson Street Presbyterian Church, Fourth Street Market Grocery (1926-1927), West End Grocery and Meat Market (c. 1900), Dr. Ludwell Powell House (1838), Rogers-Ehrhard House (1856, 1866), Waye Monument Company and Residence (1889), Meyer House, Kaemmerlen House, and Elsner House.

Frenchtown Historic District: Frenchtown Historic District is a national historic district located at St. Charles, St. Charles County, Missouri.  The district encompasses 205 contributing buildings and 1 contributing structure in the Frenchtown section of St. Charles.  It developed between about 1830 and 1940, and includes representative examples of Greek Revival style, Late Victorian style and Colonial style architecture.  The district includes an industrial complex associated with the St. Charles Car Company, founded in 1873, and later known as the American Car and Foundry Company.

August Sehrt House: The August Sehrt House is a historic home located at Augusta, St. Charles County, Missouri.  It was built about 1860 by German immigrant, August Sehrt.  He came to America in 1848 with several family members, including his brother, Julius Sehrt who went on to become the most extensive land owner in St. Charles, MO.  It is a 1 1/2-story, five bay, brick dwelling on a stone foundation and with a side-gable roof.  The building houses the Augusta History Museum.

Marten-Becker House: Marten-Becker House, also known as Becker House, is a historic home located at St. Charles, St. Charles County, Missouri.  It was built about 1865, and is a two-story, "L"-plan, Italianate style brick dwelling.  It features a richly bracketed cornice, cupola with arched windows of colored glass and ornate cast iron portico.  Also on the property are two contributing brick outbuildings.

Question: Marten-Becker House, also known as Becker House, is a historic home located at St. Charles, a city in, and the county seat of, St. Charles County, Missouri, in which country?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "house_name": {
      "type": "string",
      "description": "The primary name of the historic house."
    },
    "alternate_name": {
      "type": "string",
      "description": "An alternative name for the historic house."
    },
    "location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the house is located."
        },
        "county": {
          "type": "string",
          "description": "The county where the house is located."
        },
        "state": {
          "type": "string",
          "description": "The state where the house is located."
        },
        "country": {
          "type": "string",
          "description": "The country where the house is located."
        }
      },
      "required": [
        "city",
        "county",
        "state",
        "country"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "house_name",
    "alternate_name",
    "location"
  ],
  "additionalProperties": false
}
