{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCathedral of St. Ignatius of Loyola, Vilnius: The Cathedral of St. Ignatius of Loyola (Lithuanian: \"Šv.  Ignoto katedra\" ) also called Church of St. Ignatius (\"Šv.  Ignoto bažnyčia\") It is a religious building of the Catholic Church that serves as the cathedral of the military ordinariate in Lithuania, is located in the capital, Vilnius.\n\nChurch of St. Ignatius Loyola (New York City): The Church of St. Ignatius of Loyola is a Roman Catholic parish church located on the Upper East Side of Manhattan, New York City, administered by the Society of Jesus (Jesuits).  The parish is under the authority of the Archdiocese of New York, and was established in 1851 as St. Lawrence O'Toole's Church.  In 1898, permission to change the patron saint of the parish from St. Lawrence O’Toole to St. Ignatius of Loyola was granted by Rome.  The address is 980 Park Avenue, New York City, New York 10028.  The church on the southwest corner of Park Avenue and 84th Street is part of a Jesuit complex on the block that includes Wallace Hall, the parish hall, beneath the church, the rectory at the midblock location on Park Avenue, the grade school of St. Ignatius's School on the north midblock location of 84th Street behind the church and the high school of Loyola School (also 980 Park Avenue) at the northwest corner of Park Avenue and 83rd Street.  In addition, another Jesuit high school, Regis High School (55 E 84th Street), occupies the midblock location on the north side of 84th Street.  The church was added to the National Register of Historic Places on July 24, 1980.\n\nSt. Ignatius Mission: The St. Ignatius Mission is a landmark Roman Catholic mission founded at its present location, St. Ignatius, Montana, in 1854 by Father Pierre-Jean De Smet and Father Adrian Hoecken.  The current mission church was built between 1891 and 1893, and listed on the U.S. National Register of Historic Places in 1973.\n\nSt. Ignatius School: St. Ignatius School is a Roman Catholic school in Winnipeg, Manitoba.  It was opened on January 12, 1911 by the Parish of St. Ignatius.  The school is located in the neighborhood of Rockwood in the River Heights area.  The school and church share one city block, bounded by Corydon Avenue to the north, Jessie Avenue to the south, Stafford Street to the east and Harrow Street to the west.\n\nSt. Ignatius, Montana: St. Ignatius (Salish: snyél̓mn, Ktunaxa: ʔa·kikqǂaǂaǂuk̓pǂiʔit) is a town in Lake County, Montana, United States.  The population was 842 at the 2010 census.  The town is located on the Flathead Indian Reservation along US 93, and is home to the St. Ignatius Mission which is listed on the National Register of Historic Places.\n\nFlathead Indian Reservation: The Flathead Indian Reservation, located in western Montana on the Flathead River, is home to the Bitterroot Salish, Kootenai, and Pend d'Oreilles Tribes - also known as the\n\nFlathead Valley: The Flathead Valley, located in Northwestern Montana, is a region of the U.S. state of Montana.  It includes Flathead County, and part of Lake County.  Notable towns include Bigfork, Kalispell, Columbia Falls, Polson, and Whitefish.  The geography of the Flathead roughly corresponds to the valley where Flathead Lake is located.  In addition to the lake, the area's proximity to attractions such as Glacier National Park and Whitefish Mountain Resort have made the area a major resort destination.  Many outdoor activities can be pursued there such as hiking, backpacking, rafting, canoeing, skiing, hunting, and some of the best trout fishing in the world.  The Flathead Valley is also home to a portion of the Flathead Indian Reservation.\n\nLoyola School (New York City): Loyola School is an independent Jesuit high school on the Upper East Side of New York City, founded in 1900 by the Society of Jesus.  Originally a Roman Catholic boys school, Loyola became coeducational in 1973, becoming the only Jesuit co-ed college preparatory high school in the Tri-State Region.  With a student enrollment of two hundred, the average class size of fifteen students promotes personal attention and individual participation.  Loyola education fosters lifelong learning and aims to produce graduates who are academically excellent, open to growth, religious, loving, and committed to doing justice in service to others.  The school is located two city blocks east of Central Park and Museum Mile on 83rd Street and Park Avenue in Manhattan.  St. Ignatius Church is in the same complex and is used for various school functions.  The church is listed as a NYC landmark and the complex is listed as a National Historic Place.  St. Ignatius Loyola School is an elementary school that also shares the complex but there is no official link between the schools.\n\nSt. Ignatius College Preparatory: St. Ignatius College Preparatory (SI) is a private, Catholic preparatory school in the Jesuit tradition, serving the San Francisco Bay Area since 1855.  Located in the Roman Catholic Archdiocese of San Francisco, in the Sunset District of San Francisco, St. Ignatius is one of the oldest secondary schools in the U.S. state of California.\n\nNorthwest Montana Wetland Management District: The Northwest Montana Wetland Management District is located in the U.S. state of Montana and is an integral part of the National Bison Range Complex along with four other wildlife refuges and the National Bison Range.  The district comprises numerous small wetland environments set aside primarily to protect areas for waterfowl.  The district comprises 14 separate Waterfowl Production Areas (WPA)'s totalling 8452 acre and one 6300 acre conservation easement along the north shores of Flathead Lake.  Some of the land is located on the Flathead Indian Reservation (known as the Tribal Trust Lands of the Confederated Salish and Kootenai Tribes) and they continue to have claim over the land provided they assist in maintaining the resource.  The Northwest Montana Wetland Management District is administered by the U.S. Fish and Wildlife Service, an agency within the U.S. Department of the Interior.  The individual lands were acquired beginning in 1970 by purchasing plots from willing landowners, and an ongoing effort to continue to increase area.\n\nQuestion: St. Ignatius, located on Flathead Indian Reservation, is listed in what register?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"listed_entity_name\": {\n      \"type\": \"string\",\n      \"description\": \"The specific name of the entity that is listed on the register.\"\n    },\n    \"entity_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of the listed entity (e.g., mission, church, school).\"\n    },\n    \"location_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"town\": {\n          \"type\": \"string\",\n          \"description\": \"The town where the entity is located.\"\n        },\n        \"state\": {\n          \"type\": \"string\",\n          \"description\": \"The state where the entity is located.\"\n        },\n        \"reservation\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the Indian Reservation the entity is located on.\"\n        }\n      },\n      \"required\": [\n        \"town\",\n        \"state\",\n        \"reservation\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"register_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"register_name\": {\n          \"type\": \"string\",\n          \"description\": \"The full name of the historical register.\"\n        },\n        \"listing_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the entity was listed on the register.\"\n        }\n      },\n      \"required\": [\n        \"register_name\",\n        \"listing_year\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"listed_entity_name\",\n    \"entity_type\",\n    \"location_details\",\n    \"register_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "listed_entity_name": {
        "type": "string",
        "description": "The specific name of the entity that is listed on the register."
      },
      "entity_type": {
        "type": "string",
        "description": "The type of the listed entity (e.g., mission, church, school)."
      },
      "location_details": {
        "type": "object",
        "properties": {
          "town": {
            "type": "string",
            "description": "The town where the entity is located."
          },
          "state": {
            "type": "string",
            "description": "The state where the entity is located."
          },
          "reservation": {
            "type": "string",
            "description": "The name of the Indian Reservation the entity is located on."
          }
        },
        "required": [
          "town",
          "state",
          "reservation"
        ],
        "additionalProperties": false
      },
      "register_details": {
        "type": "object",
        "properties": {
          "register_name": {
            "type": "string",
            "description": "The full name of the historical register."
          },
          "listing_year": {
            "type": "integer",
            "description": "The year the entity was listed on the register."
          }
        },
        "required": [
          "register_name",
          "listing_year"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "listed_entity_name",
      "entity_type",
      "location_details",
      "register_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
