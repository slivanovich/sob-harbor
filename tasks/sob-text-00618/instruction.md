{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nFranklin Hotel (Strawberry Point, Iowa): The Franklin Hotel is a historic building located in Strawberry Point, Iowa, United States.  The Franklin Hotel and Land Company was established in 1902 for the purpose of building a modern hotel to serve the community.  They hired the Independence, Iowa architectural firm of Netcott and Donnan to design the building, which was constructed by E.M. Loop of Hopkinton, Iowa.  The hotel opened on February 12, 1903, and the building has served that purpose ever since.  The two-story brick building combines the Neoclassical and Romanesque Revival styles.  It sits on the northeast corner of an intersection and its rounded corner follows the curve of the intersection.  The commercial space adjacent to the north is also a part of this building with hotel rooms on the second floor.  Railroad tracks at one time were located just north of the hotel, which served the passengers from the railroad and later travelers from the highways that run past the hotel.  The building was listed on the National Register of Historic Places in 1999.\n\nDayuse.com: Dayuse.com is a French company and a booking platform for hotel rooms during the day.  Created in 2010, Dayuse.com is a website that offers the booking of daytime hotel rooms online and by telephone.  The company lists over 2000 hotels in 15 countries.\n\nHarrah's New Orleans: Harrah's New Orleans is a casino located in New Orleans, Louisiana, near the foot of Canal Street a block away from the Mississippi River.  It is a 115000 sqft casino with approximately 2,100 slot machines, over 90 table games and a poker room.  There are several places to eat ranging from buffet style to fine dining.  Since its opening in 1999 Harrah's has been renting nearby hotel rooms to accommodate its guests; currently, the newly renovated 202-room Wyndham Riverfront Hotel is providing such accommodations.  In order to avoid leasing rooms, the casino opened its own 27-story hotel tower with 450 rooms across the street from the casino on September 21, 2006, just days ahead of the New Orleans Saints return to the Louisiana Superdome.  It is the only land-based private casino with table games in the state by Louisiana law (there are other casinos in the state with their gambling facilities on floating boats and horse racing racinos with slot machines).  It is referred to in state statute as \"the official gaming establishment\", see Chp.10, Title 4 of Louisiana Revised Statutes.\n\nRedwoods Hotel: The Redwoods Hotel, also known as the Redwood Towers, is an historic six-story hotel building located at 306-310 Northwest 6th Street in Grants Pass, Josephine County, Oregon.  Built in 1926 of reinforced concrete with cast concrete art deco ornamentation on its front facade, it was designed by the architectural firm of Tourtellotte and Hummel, noted for the many buildings it designed in Idaho and Oregon.  Its builder was R.I. (Richard Irwin) Stuart, of Medford, Oregon, who completed it in 6 months.  It was built as an expansion of the adjacent 3-story brick Josephine Hotel and originally contained 45 hotel rooms with retail space on its first floor.  The old Josephine Hotel was completely gutted by fire in 1975 and was razed.  After the fire, the owners of the Redwoods Hotel made the decision to convert its upper floors to office space.\n\nGilmore Building: The Gilmore Building, also known as the Gilmore Hotel, is a historic commercial building at 326 Front Street in Ketchikan, Alaska.  It is a three story masonry building located adjacent to Ketchikan City Hall, and was built in 1926-27 by P. J. Gilmore, Sr. to meet growing demand in the growing community for retail space and hotel rooms.  The build is in the shape of a reversed L, whose base lies along Front Street, and includes three commercial storefronts.  The upper floors are populated with hotel rooms.\n\nBessie the Heifer: \"Bessie The Heifer\" is an American country-western novelty song written by Jimmy Dickens and Boudleaux Bryant.  Performed by Dickens, the song was released by Columbia in 1951 (Columbia 20786).  The song was one of Billboard Magazine's Country And Western Disk Jockey Picks shortly after it was released.  The song has been performed by other musicians such as Wayne Newton and Grant Rogers.  Newton sang the song on a 1965 episode of \"The Lucy Show,\" \"Lucy Discovers Wayne Newton.\"  The song (and a parody of it called Melvin the Mollusk) was performed many times at The Adventurers Club in Downtown Disney at Walt Disney World.\n\nNH Hotel Group: NH Hotel Group (officially NH Hotel Group SA, ) is a Spanish-based hotel chain headquartered in Madrid.  NH offers moderately priced and modernly-furnished hotel rooms and lobbies, located primarily in Europe and Latin America.  NH Hotel Group ranks third in the European ranking for business hotels.  The group has 380 hotels in 29 countries with over 53,000 rooms.  In 2016, China becomes the 30th country that NH Hotel Group enter.  It expects to open two hotels in Haikou and Sanya in the second half of 2016.  It has 54 projects for new hotels under construction, which would add almost 8,000 new rooms.\n\nRemember When (We Made These Memories): \"Remember When (We Made These Memories)\" is a song written by Bert Kaempfert, Charles Singleton, and Eddie Snyder and performed by Wayne Newton.  It reached #15 on the U.S. adult contemporary chart and #69 on the \"Billboard\" Hot 100 in 1965.  It was featured on his 1966 album, \"Wayne Newton...Now!\"\n\nWayne Newton Live in Concert: Wayne Newton Live in Concert was a Pay-Per-View concert special starring Wayne Newton that aired live from the Westgate Las Vegas Resort & Casino (then called the Las Vegas Hilton) on May 23, 1989.  The concert was one of only a handful of times that Newton has starred in a concert special featuring his entire Las Vegas show, and was also a way of promoting his then-new album \"Coming Home.\"  The show was directed by Steve Binder, the same man who directed Elvis Presley's '68 Comeback Special.  Select pieces of the show were put together in a video cassette titled \"Wayne Newton: Live In Concert at the Las Vegas Hilton\" & was released in 1998.\n\nWestgate Las Vegas Resort &amp; Casino: The Westgate Las Vegas Resort & Casino is a hotel and casino in Winchester, Nevada.  It is owned by Westgate Resorts and operated by Navegante Group.  It has 2,956 hotel rooms including 305 suites.  It opened in 1969 as the International Hotel, and was known for many years as the Las Vegas Hilton, then briefly as the LVH – Las Vegas Hotel and Casino.  It was renamed the Westgate Las Vegas on July 1, 2014.\n\nQuestion: How many hotel rooms are in the hotel where Wayne Newton performed his May 23, 1989 Pay-Per-View concert?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"hotel_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"current_name\": {\n          \"type\": \"string\",\n          \"description\": \"The current name of the hotel.\"\n        },\n        \"name_at_event\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the hotel at the time of the event.\"\n        },\n        \"total_rooms\": {\n          \"type\": \"integer\",\n          \"description\": \"The total number of hotel rooms.\"\n        },\n        \"number_of_suites\": {\n          \"type\": \"integer\",\n          \"description\": \"The number of suites within the hotel.\"\n        }\n      },\n      \"required\": [\n        \"current_name\",\n        \"name_at_event\",\n        \"total_rooms\",\n        \"number_of_suites\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"event_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"event_type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of event that took place.\"\n        },\n        \"performer_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the performer at the event.\"\n        },\n        \"event_date\": {\n          \"type\": \"string\",\n          \"format\": \"date\",\n          \"description\": \"The date the event took place.\"\n        }\n      },\n      \"required\": [\n        \"event_type\",\n        \"performer_name\",\n        \"event_date\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"answer\": {\n      \"type\": \"integer\",\n      \"description\": \"The number of hotel rooms in the specified hotel.\"\n    }\n  },\n  \"required\": [\n    \"hotel_details\",\n    \"event_details\",\n    \"answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "hotel_details": {
        "type": "object",
        "properties": {
          "current_name": {
            "type": "string",
            "description": "The current name of the hotel."
          },
          "name_at_event": {
            "type": "string",
            "description": "The name of the hotel at the time of the event."
          },
          "total_rooms": {
            "type": "integer",
            "description": "The total number of hotel rooms."
          },
          "number_of_suites": {
            "type": "integer",
            "description": "The number of suites within the hotel."
          }
        },
        "required": [
          "current_name",
          "name_at_event",
          "total_rooms",
          "number_of_suites"
        ],
        "additionalProperties": false
      },
      "event_details": {
        "type": "object",
        "properties": {
          "event_type": {
            "type": "string",
            "description": "The type of event that took place."
          },
          "performer_name": {
            "type": "string",
            "description": "The name of the performer at the event."
          },
          "event_date": {
            "type": "string",
            "format": "date",
            "description": "The date the event took place."
          }
        },
        "required": [
          "event_type",
          "performer_name",
          "event_date"
        ],
        "additionalProperties": false
      },
      "answer": {
        "type": "integer",
        "description": "The number of hotel rooms in the specified hotel."
      }
    },
    "required": [
      "hotel_details",
      "event_details",
      "answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
