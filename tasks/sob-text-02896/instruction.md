{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nNorthern Pacific Depot (Aitkin, Minnesota): The Northern Pacific Depot in Aitkin, Minnesota, United States, is a brick passenger depot built on the Northern Pacific Railway mainline in 1916.  The rail line is now part of the BNSF Railway.  The depot symbolizes the importance of the railroad in Aitkin's growth and development.\n\nNorthern Pacific Depot: Northern Pacific Depot, or Northern Pacific Railway Depot, or Northern Pacific Passenger Depot, or Northern Pacific Railroad Depot, or Northern Pacific Railway Passenger Depot may refer to the following stations in the United States:\n\nNorthern Pacific Depot (Villard, Minnesota): The Northern Pacific Depot or Villard Depot is a historic railway station in Villard, Minnesota, United States, built in 1882.  It is listed on the National Register of Historic Places for having local significance in exploration/settlement and transportation.  The depot was constructed upon the completion of a new Northern Pacific Railway line and the platting of a new trackside town named after the railway's president Henry Villard.  The Little Falls and Dakota Branch line, running between Little Falls and Morris, Minnesota, provided a key link between the agricultural region of west-central Minnesota and the Great Lakes port of Duluth.  The depot now marks the eastern terminus of the Villard–Starbuck Trail, a rail trail in development from Villard through Glenwood, Starbuck, and on to Glacial Lakes State Park.\n\nFredericktown Missouri Pacific Railroad Depot: Fredericktown Missouri Pacific Railroad Depot, also known as the Fredericktown Depot, is a historic train station located at Fredericktown, Madison County, Missouri.  It was built in 1917 by the St. Louis, Iron Mountain and Southern Railway, later Missouri Pacific Railroad.  It is a one-story rectangular brick building with a low-pitched red tile hipped roof with Prairie School and Bungalow / American Craftsman style influences.  It measures 22 feet by 128 feet, and features widely overhanging eaves supported by large curvilinear brackets and a projecting dispatcher's bay.  In 1917-1918, the new Fredericktown Missouri Pacific Depot took over passenger service, while freight continued to be handled by the original St. Louis, Iron Mountain and Southern Railroad Depot.  Passenger service to Fredericktown was discontinued in 1972 and the building subsequently used for commercial enterprises.\n\nRobert Reamer: The Old Faithful Inn was commissioned in 1902 by Child, and funded with loans from the Northern Pacific Railroad, using laborers who were experienced railroad trestle builders.  Child introduced Reamer to Charles Sanger Mellen, president of the Northern Pacific.  While he was carrying out design work on the Old Faithful Inn for Child, Reamer was also designing the Gardiner, Montana depot for the Northern Pacific, at the northern entrance to Yellowstone National Park.  The depot and the Inn were complementary projects, and similar in style.  The depot opened first, in 1903, and embodied many design features that Reamer explored on a grander scale at the Old Faithful Inn.\n\nNorthern Pacific Depot (Hinckley, Minnesota): The Northern Pacific Depot in Hinckley, Minnesota, United States, is a wood-framed depot built in 1895, the year after the previous depot was destroyed in the Great Hinckley Fire on September 1, 1894.  The depot was built from the plans of the previous depot.  It was listed on the National Register of Historic Places in 1973.  The building was originally built by the St. Paul and Duluth Railroad, which was acquired by the Northern Pacific Railway in 1900.  The Northern Pacific operated the depot until the mid-1960s.  The building had separate men's and women's waiting rooms, a freight room, a restaurant known as the \"Beanery\", and a stationmaster's living quarters on the second floor.\n\nGreat Hinckley Fire: The Great Hinckley Fire was a conflagration in the pine forests of Minnesota in September 1894, which burned an area of at least 200000 acre (perhaps more than 250000 acre ) including the town of Hinckley.  The official death count was 418; the actual number of fatalities was likely higher.\n\nNiles Depot Museum: The Niles Depot Museum is located in the former Southern Pacific Railroad colonnade-style passenger depot built in 1901, and freight depot, located in the Niles District of Fremont, California.  The museum is operated by the Niles Depot Historical Foundation and features exhibits and artifacts about area railroads, including the early Southern Pacific Railroad and Western Pacific Railroad, as well as the current Union Pacific Railroad and Amtrak.\n\nGreat Northern Depot (Wayzata, Minnesota): The Great Northern Depot in Wayzata, Minnesota is a depot built by the Great Northern Railway in 1906 to a design in the Tudor Revival style by architect Samuel L. Bartlett.  The depot is listed on the National Register of Historic Places.  The depot now houses the offices and museum of the Wayzata Historical Society as well as the Wayzata Area Chamber of Commerce, and is known as the \"Wayzata Depot\".\n\nSS Northern Pacific (1914): SS \"Northern Pacific was built as a passenger ship at Philadelphia by William Cramp & Sons under supervision of the Great Northern Pacific Steam Ship Company for the Spokane, Portland and Seattle Railway Company.  \"Northern Pacific\", along with sister ship \"Great Northern\" , were built to provide a passenger and freight link by sea between the Great Northern Railway Lines and Spokane, Portland and Seattle Railway terminal at Astoria, Oregon and San Francisco beginning in spring of 1915.  The ship was acquired on 17 September 1917 for use as a transport ship for the United States Navy during World War I, commissioned USS \"Northern Pacific and later, after transfer to the United States Army, as the Army transport USAT \"Northern Pacific\".  She was destroyed by fire in 1922.\n\nQuestion: Where was the Northern Pacific Depot built after the previous depot was destroyed in the 200000 acre fire on September 1, 1894?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"depot_location\": {\n      \"type\": \"string\",\n      \"description\": \"The city and state where the Northern Pacific Depot was built.\"\n    },\n    \"depot_construction_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"year_built\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the new depot was constructed.\"\n        },\n        \"original_builder_railway\": {\n          \"type\": \"string\",\n          \"description\": \"The railway company that originally built the depot.\"\n        },\n        \"operated_by_northern_pacific\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the depot was operated by the Northern Pacific Railway.\"\n        }\n      },\n      \"required\": [\n        \"year_built\",\n        \"original_builder_railway\",\n        \"operated_by_northern_pacific\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"fire_event_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"fire_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the fire that destroyed the previous depot.\"\n        },\n        \"fire_date\": {\n          \"type\": \"string\",\n          \"format\": \"date\",\n          \"description\": \"The date the fire occurred.\"\n        },\n        \"area_burned_acres\": {\n          \"type\": \"integer\",\n          \"description\": \"The minimum area burned by the fire in acres.\"\n        }\n      },\n      \"required\": [\n        \"fire_name\",\n        \"fire_date\",\n        \"area_burned_acres\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"depot_location\",\n    \"depot_construction_details\",\n    \"fire_event_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "depot_location": {
        "type": "string",
        "description": "The city and state where the Northern Pacific Depot was built."
      },
      "depot_construction_details": {
        "type": "object",
        "properties": {
          "year_built": {
            "type": "integer",
            "description": "The year the new depot was constructed."
          },
          "original_builder_railway": {
            "type": "string",
            "description": "The railway company that originally built the depot."
          },
          "operated_by_northern_pacific": {
            "type": "boolean",
            "description": "Indicates if the depot was operated by the Northern Pacific Railway."
          }
        },
        "required": [
          "year_built",
          "original_builder_railway",
          "operated_by_northern_pacific"
        ],
        "additionalProperties": false
      },
      "fire_event_details": {
        "type": "object",
        "properties": {
          "fire_name": {
            "type": "string",
            "description": "The name of the fire that destroyed the previous depot."
          },
          "fire_date": {
            "type": "string",
            "format": "date",
            "description": "The date the fire occurred."
          },
          "area_burned_acres": {
            "type": "integer",
            "description": "The minimum area burned by the fire in acres."
          }
        },
        "required": [
          "fire_name",
          "fire_date",
          "area_burned_acres"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "depot_location",
      "depot_construction_details",
      "fire_event_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
