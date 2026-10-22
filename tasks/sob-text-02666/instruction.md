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
Silver Bow Basin: The Silver Bow Basin is a valley located 2.4 miles northeast of Juneau, Alaska, USA.  It is situated on Gold Creek in an area north of Icy Gulch, and approximately 1.5 miles north of Gastineau Peak.  A trail from Juneau leads directly to the mountainside.  The basin was the site of the earliest gold discovery in the Juneau area, leading to the establishment of the town called Juneau.

Pikru: Pikru is a village in Tarvastu Parish, Viljandi County, Estonia located 24 km (15 miles) southeast of the village of Viljandi, 3.9 km (2.4 miles) south of the small borough of Mustla, near the western shore of Lake Võrtsjärv.  Neighboring villages include Jakobimõisa, Ämmuste, Unametsa and Soe.  As of 2011, the population of Pikru was 42, a decrease from 61 in the 2000 census.

Mount Baldy (Nevada): Mount Baldy is located in Washoe County, Nevada in the Mount Rose Wilderness.  The summit is 3.1 mi north-northwest of Kings Beach, California and 2.4 mi northwest of Incline Village, Nevada, both of which are on the north shore of Lake Tahoe.

Camp McKinney, British Columbia: Camp McKinney is a ghost town in the Boundary Country region of British Columbia, Canada.  It is located southeast of Mount Baldy, northeast of Osoyoos.

Panchkula: Panchkula is a planned city in the Panchkula district, Haryana, India.  It forms a part of a continuous area with the union territory of Chandigarh and the city of Mohali.  It is approximately 4 km (2.4 miles) southeast of Chandigarh, 105 km (65 miles) southwest of Shimla and 259 km (162 miles) northeast of New Delhi, the national capital.  It is a part of the Chandigarh capital region or Greater Chandigarh.  The Chandigarh-Mohali-Panchkula metropolitan region collectively forms a Chandigarh Tricity, with a combined population of over 2 million.

Incline Village, Nevada: Incline Village is a census-designated place (CDP) in Washoe County, Nevada on the north shore of Lake Tahoe.  The population was 8,777 at the 2010 census.  It is part of the Reno−Sparks Metropolitan Statistical Area.  Until the 2010 census, the CDP Crystal Bay, Nevada was counted jointly with Incline Village.

Baldy Mountain (Colfax County, New Mexico): Baldy Mountain (official name), Baldy Peak, Mount Baldy, or Old Baldy is the highest peak in the Cimarron Range, a subrange of the Sangre de Cristo Mountains of New Mexico.  It is located in Colfax County, about 6 mi northeast of Eagle Nest.  It rises abruptly, with 3,640 ft of vertical relief (in 3 miles/4.8 km), from the Moreno Valley to the west and has a total elevation of 12441 ft .

Crystal Lake Recreation Area: Crystal Lake Recreation Area is part of the San Gabriel River (formerly Mount Baldy) District of the Angeles National Forest in Southern California.  It consists of a lake, a public campground, and Deer Flats, a group campground.  It is located approximately 26 miles (42 km) north on Hwy.  39 heading out of Azusa, California at the headwaters of the north fork of the San Gabriel River at an elevation approximately 5,830 feet (1585 m) above sea level.  Crystal Lake is the only naturally occurring lake in the San Gabriel Mountains.

Gastineau Peak: Gastineau Peak is a mountain in the city and borough of Juneau, Alaska, United States.  It is a part of the Boundary Ranges of the Coast Mountains in western North America.  It is located 1.6 miles west of Sheep Mountain and 2.4 miles southeast of the city of Juneau.

Kuressaare, Viljandi County: Kuressaare is a village in Tarvastu Parish, Viljandi County located 23 km (14) southeast of the town of Viljandi, 3.8 km (2.4 miles) southwest of the small borough of Mustla.  Neighboring villages include Pikru, Ämmuste and Jakobimõisa.  Kuressaare had a population of 67 as of 2011, a decrease from 85 in the 2000 census.

Question: What is the population of the census-designated place which is located 2.4 miles southeast of Mount Baldy?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "cdp_name": {
      "type": "string",
      "description": "The name of the Census-Designated Place."
    },
    "population": {
      "type": "integer",
      "description": "The population of the CDP."
    },
    "census_year": {
      "type": "integer",
      "description": "The year the population census was conducted."
    },
    "location_details": {
      "type": "object",
      "properties": {
        "relative_to_entity": {
          "type": "string",
          "description": "The name of the entity it is located relative to."
        },
        "distance_miles": {
          "type": "number",
          "description": "The distance in miles from the relative entity."
        },
        "direction": {
          "type": "string",
          "description": "The cardinal direction from the relative entity."
        }
      },
      "required": [
        "relative_to_entity",
        "distance_miles",
        "direction"
      ],
      "additionalProperties": false
    },
    "county": {
      "type": "string",
      "description": "The county where the CDP is located."
    },
    "state": {
      "type": "string",
      "description": "The state where the CDP is located."
    }
  },
  "required": [
    "cdp_name",
    "population",
    "census_year",
    "location_details",
    "county",
    "state"
  ],
  "additionalProperties": false
}
