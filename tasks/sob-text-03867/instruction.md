{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nFort McAllister: Fort McAllister was a Confederate earthen-work fort used to defend Savannah, Georgia during the American Civil War.  It was the southernmost of the forts defending Savannah and was involved in the most battles.  It was located on the Ogeechee River in Bryan County.  It is listed on the National Register of Historic Places (#70000197).  Fort McAllister was one of three forts protecting Savannah, the others being Fort Pulaski and Fort James Jackson standing in Confederate defiance of the Union naval blockade.  The southeast coast of the United States was the place where both combatants tested the latest in naval artillery and coastal defenses.  Fort McAllister was the key to unlocking the defenses around Savannah, one of the most important Confederate ports on the Atlantic Ocean.\n\nAlbert Creswell Garlington: Albert Cresswell Garlington (June 9, 1822  – March 27, 1885) was a brigadier general in the South Carolina Militia, who served along with the Confederate States Army in South Carolina at various times during the American Civil War (Civil War).  He was initially responsible for coastal defenses and militia in South Carolina, and then for training state troops.  He briefly served as a major of the Holcombe Legion, a South Carolina unit guarding the coast in South Carolina for the Confederate States Army.  After he resigned his commission on May 21, 1862, he served as state adjutant general and inspector general.  Garlington again served as a brigadier general of militia in the Carolinas Campaign of late 1864 and early 1865.\n\nFort Hancock, New Jersey: Fort Hancock is a former United States Army fort at Sandy Hook in Middletown Township New Jersey.  The coastal artillery base defended the Atlantic coast and the entrance to New York Harbor, with its first gun batteries operational in 1896.  Between 1874 and 1919, the adjacent US Army Sandy Hook Proving Ground was operated in conjunction with Fort Hancock.  It is now part of Fort Hancock Memorial Park.  It was preceded by the Fort at Sandy Hook, built 1857–1867 and demolished beginning in 1885.\n\nFort Williams (Maine): Fort Williams is a former United States Army fort in Cape Elizabeth, Maine which operated from 1872 to 1964.  It was part of the Coast Defenses of Portland, later renamed the Harbor Defenses of Portland, a command which protected Portland's port and naval anchorage 1904-1950.  After its closure, it was redeveloped into Fort Williams Park.\n\nFort Williams (disambiguation): Fort Williams Park is a 90-acre park in Cape Elizabeth, Maine.\n\nFort McKinley (Maine): Fort McKinley is a former United States Army coastal defense fort on Great Diamond Island, Maine in Casco Bay, which operated from 1873 to 1947.  It was named for President William McKinley.  It included a sub-post, Fort Lyon, on Cow Island, just north of Great Diamond Island.  Fort Lyon was named for Nathaniel Lyon.  Both forts were part of the Coast Defenses of Portland, renamed the Harbor Defenses of Portland in 1925, a command which protected Portland's port and naval anchorage 1895-1950.  In 1946 Fort Lyon was closed and turned over to the City of Portland.  After Fort McKinley's closure it was transferred to the United States Navy, which sold the site (via the General Services Administration) to private interests in 1961.  The Fort McKinley Historic District was listed on the National Register of Historic Places in 1985.\n\nFort Williams Park: Fort Williams Park is a 90-acre park in Cape Elizabeth, Maine, encompassing numerous historical sites.  Perhaps most famous for having Portland Head Light on its grounds, the park also encompasses the decommissioned and largely demolished United States Army post Fort Williams, which was operational during World War I and World War II.\n\nRebecca Millett: Rebecca J. Millett (born October 5, 1962) is an American politician from Maine.  Millett is a Democrat State Senator from Maine's 29th District, representing South Portland, Cape Elizabeth and part of Scarborough.  From 2004-2010, Millett served on the Cape Elizabeth School Board.  She won a primary for Senate 29 over South Portland Representative Bryan Kaenrath in June 2012 and was first elected to the Maine State Senate the following November after defeating Republican Mike Wallace.  The seat was held by Larry Bliss until his mid-term resignation in 2011.  He was replaced by Cape Elizabeth resident and State Representative Cynthia Dill, who in turn decided not to seek a full term and instead to pursue the open seat in the United States Senate.\n\nBeavertail State Park: Beavertail State Park is a Rhode Island state park encompassing 153 acre at the southern end of Conanicut Island in Narragansett Bay.  Its main attraction is the active Beavertail Lighthouse, the current tower of which dates from 1856.  During World War II, the park area was part of Fort Burnside, one of several coastal fortifications designed to protect Narragansett Bay.  The park's scenic shoreline offers hiking, picnicking, and saltwater fishing.\n\nFort Wetherill State Park: Fort Wetherill State Park is a Rhode Island state park on Conanicut Island in the town of Jamestown, Rhode Island.  The park sits on the East Passage of Narragansett Bay opposite Fort Adams State Park.  From 1901 through World War II, Fort Wetherill and Fort Adams were part of a string of coastal defenses designed to protect the bay's entrance points.  The Fort Wetherill battery and training camp were acquired by the State of Rhode Island from the United States in 1972.  The park is used for sightseeing, scuba diving, picnicking, boating, fishing, and hiking.\n\nQuestion: A former United States Army fort in Cape Elizabeth, Maine which was part of the coastal defenses and redeveloped into an 90-acre park encompassing historical sites is most famous for what?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"park_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the park.\"\n    },\n    \"original_fort_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the former United States Army fort.\"\n    },\n    \"location\": {\n      \"type\": \"string\",\n      \"description\": \"The city and state where the park is located.\"\n    },\n    \"acreage\": {\n      \"type\": \"integer\",\n      \"description\": \"The size of the park in acres.\"\n    },\n    \"original_purpose\": {\n      \"type\": \"string\",\n      \"description\": \"The primary military purpose of the fort.\"\n    },\n    \"most_famous_feature\": {\n      \"type\": \"string\",\n      \"description\": \"The feature for which the park is most famous.\"\n    }\n  },\n  \"required\": [\n    \"park_name\",\n    \"original_fort_name\",\n    \"location\",\n    \"acreage\",\n    \"original_purpose\",\n    \"most_famous_feature\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "park_name": {
        "type": "string",
        "description": "The name of the park."
      },
      "original_fort_name": {
        "type": "string",
        "description": "The name of the former United States Army fort."
      },
      "location": {
        "type": "string",
        "description": "The city and state where the park is located."
      },
      "acreage": {
        "type": "integer",
        "description": "The size of the park in acres."
      },
      "original_purpose": {
        "type": "string",
        "description": "The primary military purpose of the fort."
      },
      "most_famous_feature": {
        "type": "string",
        "description": "The feature for which the park is most famous."
      }
    },
    "required": [
      "park_name",
      "original_fort_name",
      "location",
      "acreage",
      "original_purpose",
      "most_famous_feature"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
