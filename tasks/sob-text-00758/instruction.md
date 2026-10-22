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
Saint Joseph's College of Maine: Saint Joseph's College of Maine is a private Catholic liberal arts college in Standish, Maine, that grants bachelor's degrees in a traditional on-campus setting, as well as bachelor's and master's degrees via online education.  The college’s 430 acre campus in southern Maine is located on the shore of Sebago Lake, just 18 mi from Portland, Maine’s largest city.  It is the only Catholic college in Maine.

Don Ashley Turlington: Don Ashley Turlington is an author and musician born in 1972 in Silver Spring, Maryland.  He graduated from Saint Joseph's College of Maine in Standish, Maine, in 2000 and received his master's degree from Western New Mexico University.  Later Saint Joseph's would name him as one of their most notable alumni.  He currently resides in Saint Augustine, Florida with his wife Laura and their two adopted daughters, Kasenia and Meliza.

Commanda Lake: Commanda Lake (or Lake Commanda) is a lake in central Ontario, Canada.  Located on the border between Patterson Township and Pringle Township, in the Almaguin Highlands region of the District of Parry Sound, it is fed by Gee Creek, Commanda Creek and Beaudry Creek and is drained by the Restoule River.  The Lake is shaped like the number "3", its middle spur is called Deep Bay.  The lake is home to one permanent island, located off a point in its east.  This is a mud bottom lake and its water is "tea coloured."  On the north shore of the lake is the community of Restoule, but cottages line many of the shore lines.  Lots of crown land also surrounds the lake shore making it a very peaceful lake for people of all ages to enjoy.  This lake has one public boat launch towards the southern end of the lake accessible on Commanda Lake Road.  The lake is located at an altitude of 222 m (729 ft) above sea level.  The lake is home to the Northern pike, Walleye, Smallmouth bass and Largemouth bass species of fish.  Ice gets thick in the winter making this lake an all year round fishing lake.

Lake Tohopekaliga: Lake Tohopekaliga Tohopeka ([from tohopke /(i)to-hó:pk-i/ fence, fort]); Tohopekaliga [from tohopke /(i)to-hó:pk-i/ fence, fort + likv /léyk-a/ site], also referred to as Lake Toho, West Lake, or simply Toho, native name meaning "we will gather together here", is the largest lake located in Osceola County, Florida, United States.  It is the primary inflow of Shingle Creek, which rises in Orlando.  It covers 22700 acre , and spans 42 mi in circumference.  It is linked to East Lake Tohopekaliga by Canal 31 (St. Cloud Canal).  The canal is 3 mi long and runs through western St. Cloud.  South Port canal is located at the southern tip of the lake and links it to Cypress Lake.  It is 4 mi long.  Lake Toho is bordered on the northern shore by Kissimmee, on the eastern shore by Kissimmee Park, and South Port on the southern shore.  Lake Tohopekaliga is known for its bass fishing and birdwatching.  Lakefront Park is located at the north end of the lake and borders Lakeshore Blvd.  Lakefront Park has a scenic walking path with benches where visitors may view the area's wide array of waterfowl, alligators, turtles and others.  Lakefront park also has a miniature lighthouse, a children's playground area, and is bordered on its west end by Big Toho Marina.

Lake Forest College: Lake Forest College is a four-year coeducational private liberal arts college in Lake Forest, Illinois, on Chicago's North Shore.  Founded in 1857 as Lind University by Presbyterian ministers, the college has been coeducational since 1876 and an undergraduate-focused liberal arts institution since 1903.  Lake Forest enrolls approximately 1,600 students representing 47 states and 81 countries.  Lake Forest offers 30 undergraduate major and minor programs in the humanities, social sciences, and natural sciences, and features programs of study in pre-law, pre-medicine, communication, business, finance, and computer science.  The majority of students live on the college's wooded 107-acre campus, which is located a half-mile from the Lake Michigan shore.

Wells College: Wells College is a private coeducational liberal arts college located in Aurora, Cayuga County, New York, on the eastern shore of Cayuga Lake.  The college has cross-enrollment with Cornell University and Ithaca College, and is considered Cornell University's sister school.  It is strengthening its off-campus study programs (most notably in Florence) and has created centers in sustainability, business and entrepreneurship, and book arts.  Undergraduate students are required to participate in at least two off-campus internships during their time at Wells.

Lake Shore High School: Lake Shore High School is a high school located in the lakefront community of St. Clair Shores, Michigan.  The school, a part of Lake Shore Public Schools, serves grades 9–12.  The mascot for Lake Shore is the Shorian.  Lake Shore High School offers training in CAD, dental careers, web design and video production along with college advance placement classes and dual enrollment.  Lake Shore High School, along with all of the other district schools have been remodeled, equipped and technologically upgraded to serve students in an environment suited for the 21st century.  Janelle Bross is the current principal with John Hartley and Todd Stevens as the current assistant principals.

Lake Forest, Illinois: Lake Forest is a city located in Lake County, Illinois, United States.  As of the 2010 census it had a population of 19,375.  The city is along the shore of Lake Michigan, and is a part of the Chicago metropolitan area and the North Shore.  Lake Forest was founded around Lake Forest College and was laid out as a town in 1857 as a stop for travelers making their way south to Chicago.  The Lake Forest City Hall, designed by Charles Sumner Frost, was completed in 1898 and originally housed the fire department, the Lake Forest Library, and city offices.  Lake Forest is among the wealthiest cities in the United States.

Magnetawan Lake: Magnetawan Lake "(French: lac Magnetawan)" is a lake in Nipissing District, Ontario, Canada.  Magnetawan Lake is located just within the boundaries of Algonquin Provincial Park.  Being located in the park the lake and its surroundings are protected.  Magnetawan Lake also serves as an access point into Algonquin Park with a parking lot located on the shore acting as an entrance point for many canoeists.  Algonquin Park Canoe routes pass through the lake and four campsites can be found on the shore as well as two portages.  The two portages 340 m and 125 m found on Magnetawan Lake connect this lake with "Little Eagle Lake" and "Hambone Lake" respectively.

Lake Tahoe Community College: Lake Tahoe Community College (LTCC) is a community college located in South Lake Tahoe, California.  At an altitude of 6229 ft , it is at the highest elevation of any college in the state.  The college opened in 1975 without a campus; students attended classes at a closed-down local motel facility located on Lake Tahoe Boulevard.  Most classes in 1975-76 had ten students or fewer, the class catalog totaling a few typewritten pages.  The college now services approximately 2,900 students every quarter.

Question: Don Ashley Turlington graduated from a college located on the shore of what lake?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "alumnus_name": {
      "type": "string",
      "description": "The name of the alumnus."
    },
    "graduated_college": {
      "type": "string",
      "description": "The name of the college the alumnus graduated from."
    },
    "college_location_details": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the college is located."
        },
        "state": {
          "type": "string",
          "description": "The state where the college is located."
        },
        "located_on_lake_shore": {
          "type": "boolean",
          "description": "Indicates if the college campus is located on a lake shore."
        },
        "lake_name": {
          "type": "string",
          "description": "The name of the lake the college is located on the shore of."
        }
      },
      "required": [
        "city",
        "state",
        "located_on_lake_shore",
        "lake_name"
      ],
      "additionalProperties": false
    },
    "graduation_year": {
      "type": "integer",
      "description": "The year the alumnus graduated from the college."
    }
  },
  "required": [
    "alumnus_name",
    "graduated_college",
    "college_location_details",
    "graduation_year"
  ],
  "additionalProperties": false
}
