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
Pacific Northwest: The Pacific Northwest (in the United States, commonly abbreviated as PNW), sometimes referred to as Cascadia, is a geographic region in western North America bounded by the Pacific Ocean to the west and (loosely) by the Cascade Mountain Range on the east.  Though no agreed boundary exists, a common conception includes the U.S. states of Oregon and Washington and the Canadian province of British Columbia.  Broader conceptions reach north into Alaska and Yukon, south into northern California and east to the Continental Divide, thus including Idaho, Western Montana, and western Wyoming.  Idaho, Wyoming, and Montana are more accurately termed the Inland Northwest (INW), as the climate, folia, fauna, and politics are different than in the Pacific Northwest, as well as a different time zone in all but North Idaho.  Narrower conceptions may be limited to the northwestern US or to the coastal areas west of the Cascade and Coast mountains.  The variety of definitions can be attributed to partially overlapping commonalities of the region's history, geography, society, and other factors.

Fort Ridgely and South Pass Wagon Road: The Fort Ridgely and South Pass Wagon Road (also known as Nobles Trail) was a wagon trail that was intended to connect Fort Ridgely in Minnesota Territory (now Minnesota) with South Pass in the Rocky Mountains of Nebraska Territory (now Wyoming).  It was designed to link St. Paul with California via the Oregon Trail, however only a portion of the route was completed.  The trail was promoted and supervised by William H. Nobles.  Appropriations for the trail were authorized by the U.S. Congress on July 22, 1856.  It was the first road built in Dakota Territory.

Mullan: Places named after John Mullan (1830–1909), an American soldier, explorer and road builder

Cooke's Wagon Road: Cooke's Wagon Road or Cooke's Road was the first wagon road between the Rio Grande and the Colorado River to San Diego, through the Mexican provinces of Nuevo México, Chihuahua, Sonora and Alta California, established by Philip St. George Cooke and the Mormon Battalion, from October 19, 1846 to January 29, 1847 during the Mexican American War.  It became the first of the wagon routes between New Mexico and California that with subsequent modifications before and during the California Gold Rush eventually became known as the Southern Trail or Southern Emigrant Trail.

Clark Fork River: The Clark Fork, or the Clark Fork of the Columbia River, is a river in the U.S. states of Montana and Idaho, approximately 310 mi long.  The largest river by volume in Montana, it drains an extensive region of the Rocky Mountains in western Montana and northern Idaho in the watershed of the Columbia River.  The river flows northwest through a long valley at the base of the Cabinet Mountains and empties into Lake Pend Oreille in the Idaho Panhandle.  The Pend Oreille River in Idaho, Washington, and British Columbia, Canada which drains the lake to the Columbia in Washington, is sometimes included as part of the Clark Fork, giving it a total length of 479 mi , with a drainage area of 25820 sqmi .  In its upper 20 mi in Montana near Butte, it is known as Silver Bow Creek.  Interstate 90 follows much of the upper course of the river from Butte to northwest of Missoula.  The highest point within the river's watershed is Mount Evans at 10641 ft in Deer Lodge County, Montana along the Continental Divide.

John Mullan (road builder): John Mullan, Jr. (July 31, 1830 – December 28, 1909) was an American soldier, explorer, civil servant, and road builder.  After graduating from the United States Military Academy in 1852, he joined the Northern Pacific Railroad Survey, led by Isaac Stevens.  He extensively explored western Montana and portions of southeastern Idaho, discovered Mullan Pass, participated in the Coeur d'Alene War, and led the construction crew which built the Mullan Road in Montana, Idaho, and Washington state between the spring of 1859 and summer of 1860.

Joseph Sherar: Joseph Sherar (November 16, 1833 – February 11, 1908) was a 19th-century wagon road builder who, with his wife, Jane, owned and operated a Deschutes River toll bridge and a nearby stagecoach station and hotel in Wasco County in the U.S. state of Oregon.  The bridge and buildings were slightly downstream of the river's lowermost waterfall, a traditional fishing spot for the native inhabitants of the region.

Whitman massacre: The Whitman massacre (also known as the Walla Walla massacre and the Whitman Incident) was the murder of Oregon missionaries Marcus Whitman and his wife Narcissa, along with eleven others, on November 29, 1847.  They were killed by a party of Cayuse Native Americans who accused him of having poisoned 200 Cayuse in his medical care.  The incident began the Cayuse War.  It took place in present-day southeastern Washington state, near the town of Walla Walla, and was one of the most notorious episodes in the U.S. settlement of the Pacific Northwest.  The event was the climax of several years of complex interaction between Whitman, who had helped lead the first wagon train to cross Oregon's Blue Mountains and reach the Columbia River via the Oregon Trail, his wife and fellow missionary Narcissa, and the local Native Americans.  The story of the massacre shocked the United States Congress into action concerning the future territorial status of the Oregon Country.  The Oregon Territory was established on August 14, 1848.

Mullan Road: Mullan Road was the first wagon road to cross the Rocky Mountains to the Inland of the Pacific Northwest.  It was built by U.S. Army troops under the command of Lt. John Mullan, between the spring of 1859 and summer 1860.  It led from Fort Benton, which at the time was in the Dakota Territory, then Idaho Territory from July 1863, and Montana Territory beginning in May 1864, and the navigational head of the Missouri River (and once farthest inland port in the world).  The road connected to Fort Walla Walla, Washington Territory, near the Columbia River.  The road previewed the route approximately followed of modern-day Interstate 15 and Interstate 90 through present-day Montana, Idaho, and Washington.

Henry H. Spalding: Henry Harmon Spalding (1803–1874), and his wife Eliza Hart Spalding (1807–1851) were prominent Presbyterian missionaries and educators working primarily with the Nez Perce in the U.S. Pacific Northwest.  The Spaldings and their fellow missionaries were among the earliest Americans to travel across the western plains, through the Rocky Mountains and into the lands of the Pacific Northwest to their religious missions in what would become the states of Idaho and Washington.  Their missionary party of five, including Marcus Whitman and his wife Narcissa and William H. Gray, joined with a group of fur traders to create the first wagon train along the Oregon Trail.

Question: John Mullan, Jr. (July 31, 1830 – December 28, 1909) was an American soldier, explorer, civil servant, and road builder, heled the construction crew which built which road, was the first wagon road to cross the Rocky Mountains to the Inland of the Pacific Northwest, in Montana, Idaho, and Washington state, between the spring of 1859 and summer 1860?  

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "road_name": {
      "type": "string",
      "description": "The name of the wagon road."
    },
    "builder_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person who led the construction."
        },
        "role": {
          "type": "string",
          "description": "The role of the person in the road's construction."
        }
      },
      "required": [
        "name",
        "role"
      ],
      "additionalProperties": false
    },
    "historical_significance": {
      "type": "string",
      "description": "A description of the road's historical importance."
    },
    "geographical_scope": {
      "type": "object",
      "properties": {
        "region": {
          "type": "string",
          "description": "The broader geographic region the road traversed."
        },
        "states_territories": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "The U.S. states or territories the road traversed."
        }
      },
      "required": [
        "region",
        "states_territories"
      ],
      "additionalProperties": false
    },
    "construction_timeline": {
      "type": "object",
      "properties": {
        "start_period": {
          "type": "string",
          "description": "The starting period of the road's construction."
        },
        "end_period": {
          "type": "string",
          "description": "The ending period of the road's construction."
        }
      },
      "required": [
        "start_period",
        "end_period"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "road_name",
    "builder_details",
    "historical_significance",
    "geographical_scope",
    "construction_timeline"
  ],
  "additionalProperties": false
}
