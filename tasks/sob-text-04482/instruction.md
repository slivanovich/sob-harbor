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
Lincoln-Way Community High School District 210: Lincoln-Way Community High School District 210 is a school district in the southwest suburbs of Chicago.  Created in 1951, the district serves the communities of New Lenox, Frankfort, Mokena, Manhattan, and small portions of Tinley Park and Orland Park.  Four high schools comprise Lincoln-Way Community High School District 210: Lincoln-Way Central, Lincoln-Way East, Lincoln-Way North and Lincoln-Way West.  Lincoln-Way Central and Lincoln-Way West are located in New Lenox; Lincoln-Way East and Lincoln-Way North are located in Frankfort.  District 210 offices are located at Lincoln-Way Central.Effective for the 2016-2017 school year, due to financial troubles, Lincoln-Way Community High School District 210 will consolidate to a three school district.  The three schools to comprise the district are Lincoln-Way Central, Lincoln-Way East, and Lincoln-Way West.

Ridge Community High School: Ridge Community High School or RCHS is a public high school located on the Davenport, Florida and Haines City, Florida Line.  RCHS was established in 2005 in Polk County.  It currently serves 2,600 students and has 106 teachers on campus.  Ridge Community High School is one of many schools with a separate 9th Grade campus with its own front office.  The main campus holds students in 10th, 11th, and 12th grade with some exceptions.  Ridge Community High School sits on 76 acre of land.  Ridge Community High School is zoned for Davenport and Haines City.  Ridge Community High School's rivals include Haines City High School, Lake Wales High School and others in Polk County.  The principal of RCHS is currently Russell Donnelly who replaced Sherry Wells, the acting principal between the school's opening in 2005 and 2015 and has a few assistant principals.  Ridge Community High School is part of the Polk County School Board.  RCHS's mascot is the Bolt, and the school motto is Once a Bolt, always a Bolt.

East Peoria Community High School: East Peoria Community High School is a four-year public high school located in East Peoria, Illinois, and is the only school of East Peoria Community High School District 309.  It has approximately 1,200 students.  East Peoria Community High School has several feeder schools: Central Junior High School (East Peoria School District 86), Parkview Middle School (Creve Coeur School District 76), and Robein Elementary School (District 85).

Evergreen Park Elementary School District 124: Evergreen Park Elementary School District 124 is a school district headquartered in Evergreen Park, Illinois, in the Chicago metropolitan area.  It serves grades K-8.  Students move on to the Evergreen Park Community High School District 231, which operates Evergreen Park High School.

Franklin Community High School: Franklin Community High School is a community high school based in Franklin, Indiana.  It is a part of Franklin Community Schools.

Community High School District 117: Community High School District 117 is a 9-12 high school district based in Lake Villa, Lake County, Illinois that serves both the city where it is based and the village of Antioch, Illinois, alongside Old Mill Creek and Lindenhurst. District 117 is composed of two high schools: Antioch Community High School, which is located in the city of its namesake; and Lakes Community High School, which is, in turn, located in Lake Villa.  The district superintendent is Jim McKay,

Lakes Community High School: Lakes Community High School, or LCHS, is a public four-year high school located in Lake Villa, Illinois, a northern suburb of Chicago, Illinois, in the United States.  It is part of Community High School District 117, which also includes Antioch Community High School.

Franklin Community Schools: Franklin Community Schools is a school district headquartered in Franklin, Indiana.

Jasper County Community Unit School District 1: Jasper County Community Unit School District 1 is a unified school district based in Jasper County's county seat of Newton, Illinois; it is the only school district in the county and is, consequently, the main educational body in all of Jasper County, although it serves portions of Effingham County and Cumberland County as well.  This school district is composed of six schools in total; four elementary schools, one junior high school, and one high school.  There is also a prekindergarten program run at the high school of the district should parents wish to enroll their children early.  Willow Hill Elementary School, which is located in the village of its namesake, serves only kindergarteners; its proximity to the county seat and central position in the county allows its students to dawn from all parts of the county and still have easy access to the elementary school they will attend.  The principal of Willow Hill is Dave Parker.  Grove Elementary School is located in Island Grove, Illinois, the highest point of elevation in the county.  Grove Elementary School educates students from kindergarten to grade six, and it runs a prekindergarten program as well.  Craig Carr is the principal of this school.  Ste. Marie Elementary School is located in the southern Jasper County village of Ste. Marie, and serves students in grades one through six.  The principal of Ste. Marie is David Parker, the principal of Willow Hill Elementary School.  Newton Elementary School is located in the county seat of Newton, and serves most of west Jasper County's first through sixth graders under principal Travis Wyatt.  The latter three elementary schools feed into Jasper County Junior High School and are taught in the facility during seventh and eighth grade while being supervised by Newton Elementary School principal Travis Wyatt before graduating into Newton Community High School.  Students in grades nine through twelve spend their last leg of precollegiate education at this school; their principal is Ruth Kerner.  The district superintendent is Ron Alburtus, and the district's mascot is the eagle.

Antioch Community High School: Antioch Community High School, Antioch, or ACHS, is a public four-year high school located in Antioch, Illinois, a far north suburb of Chicago, Illinois, in the United States.  It is part of Community High School District 117, which also includes Lakes Community High School.

Question: Franklin Community High School is part of a school district headquartered where?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "high_school_name": {
      "type": "string",
      "description": "The name of the high school in question."
    },
    "school_district_name": {
      "type": "string",
      "description": "The name of the school district that the high school is a part of."
    },
    "district_headquarters": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the school district is headquartered."
        },
        "state": {
          "type": "string",
          "description": "The state where the school district is headquartered."
        }
      },
      "required": [
        "city",
        "state"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "high_school_name",
    "school_district_name",
    "district_headquarters"
  ],
  "additionalProperties": false
}
