{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLomax African Methodist Episcopal Zion Church: Lomax African Methodist Episcopal Zion Church is a historic African Methodist Episcopal Zion church located at 2704 24th Rd.  South in Arlington, Virginia.  It was built in 1922, and is a one story, three bay by six bay, brick church building on a parged concrete foundation.  It features two unequal-sized crenellated towers and brick buttresses along the facade and side elevations in the Late Gothic Revival style.  Also on the property are two contributing resources, including a cemetery dating from circa 1894, and a parsonage built in 1951.  The cemetery contains approximately 107 interments.\n\nConnexionalism: Connexionalism, or connectionalism, is the theological understanding and foundation of Methodist church governance (\"ecclesiastical polity\"), as practised in the Methodist Church of Great Britain, the Methodist Church in Ireland, the American United Methodist Church, African Methodist Episcopal Church, African Methodist Episcopal Zion Church, Christian Methodist Episcopal Church and many of the countries where Methodism was established by missionaries sent out from these Churches.  In the American church, where bishops provide church leadership, connexionalism is a variety of episcopal polity; however, in some countries the title of bishop may be used without any change in the Connexional polity.  In world Methodism, a given Connexion is usually autonomous.\n\nMother African Methodist Episcopal Zion Church: The Mother African Methodist Episcopal Zion Church, also known as \"Mother Zion\", located at 140–148 West 137th Street between Adam Clayton Powell Jr.  Boulevard and Lenox Avenue in the Harlem neighborhood of Manhattan, New York City, is the oldest African-American church in New York City, and the \"mother church\" of the African Methodist Episcopal Zion conference.\n\nGoler Metropolitan AME Zion Church: Goler Metropolitan AME Zion Church, originally known as East Fourth Street Baptist Church, is a historic African Methodist Episcopal Zion church located at 1435 E. Fourth Street in Winston-Salem, Forsyth County, North Carolina.  It was built in 1924, and is a front-gabled brick church with two prominent domed towers and flanking one-story hipped-roof wings in the Classical Revival style.  The front facade features a prominent pedimented porch supported by stuccoed Doric order columns and Ionic order pilasters.  The interior is based on the Akron Plan.  The building was acquired by an African-American congregation split from the Goler Memorial African Methodist Episcopal Zion Church in 1942.  The congregation changed their name to Goler Metropolitan A.M.E. Zion Church in 1953.\n\nAmerican Missionary Association: The American Missionary Association (AMA) was a Protestant-based abolitionist group founded on September 3, 1846 in Albany, New York.  The main purpose of this organization was to abolish slavery, to educate African Americans, to promote racial equality, and to promote Christian values.  Its members and leaders were of both races; The Association was chiefly sponsored by the Congregationalist churches in New England.  Starting in 1861, it opened camps in the South for freed slaves.  It played a major role during the Reconstruction Era in promoting education for blacks in the South.\n\nThomas James (minister): Thomas James (1804–1891) was a former slave who became an African Methodist Episcopal Zion minister, abolitionist, administrator and author.  He was active in New York and Massachusetts with abolitionists, and served with the American Missionary Association and the Union Army during the American Civil War to supervise the contraband camp in Louisville, Kentucky.  After the war, he held national offices in the AME Church and was a missionary to black churches in Ohio.  While in Massachusetts, he challenged the railroad's custom of forcing blacks into second-class carriages and won a reversal of the rule in the State Supreme Court.  He wrote a short memoir published in 1886.\n\nOld Ship African Methodist Episcopal Zion Church: Old Ship African Methodist Episcopal Zion Church is a historic African Methodist Episcopal Zion Church in Montgomery, Alabama.  It is the oldest African American church congregation in the city, established in 1852.  The current Classical Revival-style building was designed by Jim Alexander and was completed in 1918.  It is the fourth building the congregation has erected at this location.  Scenes from the 1982 television movie, \"Sister, Sister\", were shot at the church.  It was placed on the Alabama Register of Landmarks and Heritage on March 3, 1976 and the National Register of Historic Places on January 24, 1991.\n\nList of African Methodist Episcopal churches: This is a list of African Methodist Episcopal Churches, covering local churches of the African Methodist Episcopal Church and also local churches of the African Methodist Episcopal Zion Church, which is related.\n\nHood A.M.E. Zion Church: Hood African Methodist Episcopal Zion Church founded in 1848 is an historic African Methodist Episcopal Zion church located in Oyster Bay, New York.  It is the oldest continuous congregation holding services in its original church structure in Oyster Bay.  A small wood frame building was constructed on this site in 1856.  Later the church was renamed to honor an early bishop, the Right Reverend James Walker Hood.  In 1937, the wooden church was covered with the brick exterior you see today.  From 1937 to 1963 the pastor was Reverend Moses T. Smith.  Today the congregation is led by Reverend Kenneth Nelson, who came to the Hood AME Zion Church in 1981.  Reverend Kenneth Nelson retired in June, 2013 and the Reverend Linda B. Vanager was appointed to the Pastoral charge.\n\nPeople's African Methodist Episcopal Zion Church: People's African Methodist Episcopal Zion Church is a historic African Methodist Episcopal Zion church located in Downtown Syracuse, Onondaga County, New York.  It was designed by noted architect Charles Erastus Colton and Wallace Rayfield and built in 1911.  It is a small Gothic Revival style stuccoed brick building.  It sits on a cut limestone foundation and measures approximately 25 feet wide and 50 feet deep.  It has a two-story projecting front gable and features a three-story bell tower topped by a pyramidal roof.  The congregation was incorporated in 1837 and remained at this location until 1976.\n\nQuestion: Thomas James (1804–1891) was a former slave who became an African Methodist Episcopal Zion minister, abolitionist, administrator and author, and served with which Protestant-based abolitionist group founded on September 3, 1846 in Albany, New York?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person in question.\"\n    },\n    \"organization_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the organization.\"\n    },\n    \"organization_acronym\": {\n      \"type\": \"string\",\n      \"description\": \"The acronym of the organization, if available.\"\n    },\n    \"organization_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"founding_date\": {\n          \"type\": \"string\",\n          \"description\": \"The date the organization was founded.\"\n        },\n        \"founding_location\": {\n          \"type\": \"string\",\n          \"description\": \"The location where the organization was founded.\"\n        },\n        \"type\": {\n          \"type\": \"string\",\n          \"description\": \"A description of the organization's type or primary characteristic.\"\n        }\n      },\n      \"required\": [\n        \"founding_date\",\n        \"founding_location\",\n        \"type\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"person_role_in_organization\": {\n      \"type\": \"string\",\n      \"description\": \"The role or relationship of the person with the organization.\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"organization_name\",\n    \"organization_acronym\",\n    \"organization_details\",\n    \"person_role_in_organization\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the person in question."
      },
      "organization_name": {
        "type": "string",
        "description": "The full name of the organization."
      },
      "organization_acronym": {
        "type": "string",
        "description": "The acronym of the organization, if available."
      },
      "organization_details": {
        "type": "object",
        "properties": {
          "founding_date": {
            "type": "string",
            "description": "The date the organization was founded."
          },
          "founding_location": {
            "type": "string",
            "description": "The location where the organization was founded."
          },
          "type": {
            "type": "string",
            "description": "A description of the organization's type or primary characteristic."
          }
        },
        "required": [
          "founding_date",
          "founding_location",
          "type"
        ],
        "additionalProperties": false
      },
      "person_role_in_organization": {
        "type": "string",
        "description": "The role or relationship of the person with the organization."
      }
    },
    "required": [
      "person_name",
      "organization_name",
      "organization_acronym",
      "organization_details",
      "person_role_in_organization"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
