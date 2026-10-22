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
Bylong Valley: The Bylong Valley is a winding but relatively flat valley that crosses the Great Dividing Range between the Goulburn River National Park and Wollemi National Park, west of the upper Hunter Region in New South Wales, Australia.

Lower Goulburn National Park: The Lower Goulburn National Park is a national park located in the Goulburn Valley district of Victoria, Australia.  The 9310 ha linear national park protects the lower Goulburn River from Shepparton to its river mouth near Echuca where it forms confluence with the Murray River.

Wollar: Wollar is a town in New South Wales, Australia.  The town is located 316 km north west of the state capital Sydney and 48 km north east of the regional centre of Mudgee, near the Goulburn River National Park.  At the 2006 census , Wollar and the surrounding region had a population of 304.

Eucalyptus aenea: Eucalyptus aenea is a tree native to eastern Australia, known only from Goulburn River National Park in New South Wales.

Sydney: Sydney ( ) is the state capital of New South Wales and the most populous city in Australia and Oceania.  Located on Australia's east coast, the metropolis surrounds the world's largest natural harbour and sprawls about 70 km on its periphery towards the Blue Mountains to the west, Hawkesbury to the north and Macarthur to the south.  Sydney is made up of 658 suburbs, 40 local government areas and 15 contiguous regions.  Residents of the city are known as "Sydneysiders".  As at June 2016 Sydney's estimated population was 5,029,768.

New South Wales: New South Wales (abbreviated as NSW) is a state on the east coast of :Australia.  It borders Queensland to the north, Victoria to the south, and South Australia to the west.  Its coast borders the Tasman Sea to the east.  The Australian Capital Territory is an enclave within the state.  New South Wales' state capital is Sydney, which is also Australia's most populous city.  In March 2014 , the estimated population of New South Wales was 7.5 million, making it Australia's most populous state.  Just under two-thirds of the state's population, 4.67 million, live in the Greater Sydney area.  Inhabitants of New South Wales are referred to as "New South Welshmen".

Goulburn Valley: The Goulburn Valley is a sub-region, part of the Hume region of the Australian state of Victoria.  The sub-region consists of those areas in the catchment of the Goulburn River and other nearby streams, and is part of the Murray-Darling Basin.  The Goulburn Valley is bordered on the south by the Great Dividing Range and to the north by the Murray River, the state border with New South Wales.  The sub-region is one of Australia's most productive and intensively farmed areas and is predominantly irrigated.

Yarra, New South Wales: Yarra is a locality in the Goulburn Mulwaree Council, New South Wales, Australia.  It is located about 18 km southwest of Goulburn, 84 km northeast of Canberra and 213 km southwest of Sydney.  It lies at the intersection of the Federal Highway and the Hume Highway.  At the 2016 census , it had a population of 173.  Yarra railway station was a station on the Main Southern railway line from 1875 to the 1970s.  A small settlement had grown up around the railway station and the Hume Highway, parts of which were demolished during road widening in the 1970s.

Querétaro City: Querétaro City is the capital and largest city of the state of Querétaro, located in central Mexico.  It is part of the macroregion of Bajío.  It is located 213 km northwest of Mexico City, 63 km southeast of San Miguel de Allende and 200 km south of San Luis Potosí.  The city of Querétaro is divided into seven boroughs: Josefa Vergara y Hernández, Felipe Carrillo Puerto, Centro Histórico, Cayetano Rubio, Santa Rosa Jáuregui, Félix Osores Sotomayor and Epigmenio González.  In 1996, the historic center of Querétaro was declared a World Heritage Site by UNESCO.

Goulburn River National Park: Goulburn River National Park is in New South Wales, Australia, 213 km northwest of Sydney and it is 35 km south-west of Merriwa.  The Goulburn River National Park is located in the Hunter Valley region and covers approximately 90 km of the Goulburn River.  It is near the towns of Sandy Hollow, Denman, Merriwa, and Mudgee.

Question: Goulburn River National Park is located 213 km northwest of what state capital of New South Wales, which is the most populous city in Australia and Oceania?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "city_name": {
      "type": "string",
      "description": "The name of the city that is the state capital of New South Wales."
    },
    "city_details": {
      "type": "object",
      "properties": {
        "is_state_capital_of_new_south_wales": {
          "type": "boolean",
          "description": "Indicates if the city is the state capital of New South Wales."
        },
        "is_most_populous_in_australia_and_oceania": {
          "type": "boolean",
          "description": "Indicates if the city is the most populous in Australia and Oceania."
        },
        "estimated_population": {
          "type": "integer",
          "description": "The estimated population of the city as of June 2016."
        }
      },
      "required": [
        "is_state_capital_of_new_south_wales",
        "is_most_populous_in_australia_and_oceania",
        "estimated_population"
      ],
      "additionalProperties": false
    },
    "location_relative_to_goulburn_river_national_park": {
      "type": "object",
      "properties": {
        "distance_km": {
          "type": "integer",
          "description": "The distance in kilometers from Goulburn River National Park."
        },
        "direction_from_goulburn_river_national_park": {
          "type": "string",
          "description": "The direction of the city from Goulburn River National Park."
        }
      },
      "required": [
        "distance_km",
        "direction_from_goulburn_river_national_park"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "city_name",
    "city_details",
    "location_relative_to_goulburn_river_national_park"
  ],
  "additionalProperties": false
}
