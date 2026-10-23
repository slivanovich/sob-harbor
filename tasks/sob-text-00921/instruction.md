{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nChico Basin Ranch: The Chico Basin Ranch is a working cattle ranch thirty minutes southeast of Colorado Springs, Colorado.  The Chico Basin is owned by the Colorado State Land Board, and managed by Ranchlands, Duke and Janet Phillips' family based ranch management company.  The cattle raised on the ranch are grass fed and no hormones added.  Working cowboys tend to the cattle primarily using quarter horses born and trained on the ranch.  The Chico Basin now has a horse sanctuary for old or injured horses.  Not only is the Chico Basin a working cattle ranch, it is also a wildlife preserve.  The Chico Basin works with the Rocky Mountain Bird Observatory to band migratory birds.  This activity is also open to schools and universities to come and learn about birds.  Free programs are offered to all ages of children and adults to learn about wildlife and ranch life.\n\nAdena Springs Ranch: Adena Springs Ranch is the former name of a 30,000-acre cattle ranch in Florida's Marion County now known as Sleepy Creek Ranch Lands.  Adena Ranches is a related cattle ranch property in Levy County.  Both are owned by Canadian billionaire Frank Stronach.\n\nJohn Palmer Parker (rancher): John Palmer Parker (May 1, 1790 – August 20, 1868) was the founder of the Parker Ranch on the island of Hawaiʻ i in Hawaii.\n\nMiller Brothers 101 Ranch: The Miller Brothers 101 Ranch was a 110000 acre cattle ranch in the Indian Territory of Oklahoma before statehood.  Located near modern-day Ponca City, it was founded by Colonel George Washington Miller, a veteran of the Confederate Army, in 1893.  The 101 Ranch was the birthplace of the 101 Ranch Wild West Show and one of the early focal points of the oil rush in northeastern Oklahoma.  It was the largest diversified farm and ranch in America at the time.  Bill Pickett's grave and the White Eagle Monument are located on the ranch grounds.  The location of the former working cattle ranch was subdivided and all of its buildings destroyed.  An 82 acre area of the ranch is a National Historic Landmark.\n\nObudu Mountain Resort: Obudu Mountain Resort (formerly known as the Obudu Cattle Ranch) is a ranch and resort on the Obudu Plateau in Cross River State, Nigeria.  It was developed in 1951 by M. McCaughley, a Scot who first explored the mountain ranges in 1949.  He camped on the mountaintop of the Oshie Ridge on the Sankwala Mountains for a month before returning with Mr. Hugh Jones a fellow rancher in 1951.  Together with Dr Crawfeild, they developed the Obudu Cattle Ranch.  Although the ranch has been through troubles since, it has been rehabilitated to its former glory.\n\nWhitehorse Ranch: The Whitehorse Ranch is a historic cattle ranch in Harney and Malheur counties in the southeastern corner of Oregon, United States.  The ranch was started in 1869 by John S. Devine, a well-known 19th-century cattle baron.  It was originally the headquarters for the \"Todhunter and Devine Cattle Company\".  The ranch has been in the cattle business continuously since it was founded.  Today, the Whitehorse Ranch includes 63222 acre of deeded property and grazing rights on an additional 287205 acre of public range land administered by the Bureau of Land Management.\n\nStowers Ranch: Stowers Ranch is a cattle ranch in Kerr County, Texas, in the Texas Hill Country.  Founded by G.A. Stowers in 1904 as a cattle ranch, game management area and hunting preserve, it is now owned and operated by Stowers' grandchildren and great-grandchildren.  The ranch provides outdoor recreation opportunities throughout the year, including hunting for whitetail deer, exotic bucks and wild turkey, as well as birdwatching, game viewing, nature photography, and hiking.  The 11250 acre ranch is located at the headwaters of the north fork of the Guadalupe River, approximately 13 mi west of Hunt, Texas.  On its north side it is adjacent to the Kerr Wildlife Management Area.\n\nCross S Ranch Headquarters: The Cross S Ranch Headquarters is a historic building located in farmland 5 mi south of Olustee, Oklahoma.  The two-story stone building served as the headquarters of the Cross S Ranch, a cattle ranch founded in 1891.  As a major cattle trail passed through the area, the ranch took advantage of the open land to raise free-range cattle.  By 1902, the ranch had decreased in size due to homesteaders and raised horses rather than cattle.  The ranch eventually became a wheat farm, reflecting a broader shift in Jackson County agricultural production.  A larger wheat farm purchased the ranch in the 1970s, and the headquarters building is all that remains of the original property.\n\nJohn Parker (English cricketer): John Palmer Parker (29 November 1902 – 9 August 1984) was an English cricketer.  Parker was a right-handed batsman.\n\nParker Ranch: Parker Ranch is a working cattle ranch on the Island of Hawaii in the U.S. state of Hawaii, now run by a charitable trust.\n\nQuestion: John Palmer Parker was the founder of this cattle ranch that is now run by who?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"ranch_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the cattle ranch.\"\n    },\n    \"founder_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the founder of the ranch.\"\n    },\n    \"current_management_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of entity currently managing the ranch.\"\n    },\n    \"location\": {\n      \"type\": \"string\",\n      \"description\": \"The island and state where the ranch is located.\"\n    }\n  },\n  \"required\": [\n    \"ranch_name\",\n    \"founder_name\",\n    \"current_management_type\",\n    \"location\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "ranch_name": {
        "type": "string",
        "description": "The name of the cattle ranch."
      },
      "founder_name": {
        "type": "string",
        "description": "The name of the founder of the ranch."
      },
      "current_management_type": {
        "type": "string",
        "description": "The type of entity currently managing the ranch."
      },
      "location": {
        "type": "string",
        "description": "The island and state where the ranch is located."
      }
    },
    "required": [
      "ranch_name",
      "founder_name",
      "current_management_type",
      "location"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
