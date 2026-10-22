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
Red River Army Depot: The Red River Army Depot (RRAD) is an 15835 acre facility located 18 mi west of Texarkana, Texas, in Bowie County.  The facility has over 3000000 sqft of storage capacity.  RRAD was activated in 1941 to create an ammunition storage facility.  The depot was supposed to be deactivated after the findings of the 1995 Base Realignment and Closure Commission.  However, the depot remained open after the commission changed its mind.  The depot was once again slated for closure upon recommendation from the 2005 BRAC commission, but has remained open to provide maintenance support for the army.  The depot's primary mission is the maintenance and repair of all tactical wheeled vehicles, which includes repairing MRAPs and HUMVEEs. Letterkenny Army Depot took over some of RRAD's missile systems.

Letterkenny Munitions Center: Letterkenny Munitions Center, located on Letterkenny Army Depot in Franklin County, Pennsylvania, is a satellite activity under Crane Army Ammunition Activity in Crane, Indiana.  The center maintains, stores, and demilitarizes tactical missiles and conventional ammunition for the Army, Air Force and Navy.  LEMC assembles, disassembles and tests missiles and missile sections and is also responsible for every aspect of conventional ammunition and missiles to include demilitarization, renovation and X-ray.

Pleasant Hall, Pennsylvania: Pleasant Hall is an unincorporated community in Letterkenny Township in Franklin County, Pennsylvania, United States.  Pleasant Hall is located at the intersection of Pennsylvania Route 533 and Pennsylvania Route 997 north of Chambersburg and northeast of the Letterkenny Army Depot.

Camp Navajo: Camp Navajo was originally opened in 1942 in Bellemont, Arizona.  It was originally designated Navajo Ordnance Depot, and its primary use was the storage of ammunition used in the Pacific Theater of World War II.  It was renamed Navajo Army Depot in 1965, changed to Navajo Depot Activity in 1982, and then changed in 1993 to its current name.  In 1993 the Department of Defense transferred all ammunition activities to Hawthorne Army Ammunition Plant in Nevada.  Following the transfer, Camp Navajo was shifted to the Arizona Army National Guard.

Pennsylvania Route 433: Pennsylvania Route 433 (PA 433) is a 9.1 mi state highway located in Franklin County, Pennsylvania.  The southern terminus is at U.S. Route 11 (US 11) near Red Bridge.  The northern terminus is at PA 997 in Lurgan Township.  PA 433 is a two-lane undivided road that passes through farmland in northern Franklin County.  The route passes to the east of the Letterkenny Army Depot before it crosses PA 997.  The route heads northeast and north before curving northwest and crossing PA 533 in Orrstown.  PA 433 continues northwest to its end at PA 997.

Pueblo Depot Activity: Pueblo Depot Activity "(PUDA)", formerly known as the Pueblo Ordnance Depot and the Pueblo Army Depot, was a U.S. Army ammunition storage and supply facility.  Responsibility for the depot fell upon the U.S. Army Ordnance Corps, and the first civilians were hired in 1942 as operations began.  The mission quickly expanded to include general supplies as well.  It is a 24202 acre site located 14 mi east of Pueblo, Colorado.  In 1945 they began to receive mass amounts of equipment returning from the combat theaters of World War II.  Therefore, the mission expanded yet again to include the maintenance and refurbishing of artillery, fire control, and optical material.  In 1951 the depot assumed responsibility to distribute U.S. Air Force ammunition for an eight-state area, as well as storage of strategic and critical materials for the General Services Administration (GSA).  They were also tasked to rebuild and provide on-site maintenance support for guided missiles, ensure calibration and maintenance of electronic test equipment and radio-controlled aerial targets.  They would also provide specialized training for new Army equipment as needed.  In 1952, Rocky Mountain Arsenal in Denver, Colorado transferred chemical agents and chemical munitions to Pueblo Army Depot for secure storage.  In 1974 Pueblo Army Depot was redesignated as Pueblo Depot Activity.

Pennsylvania Route 997: Pennsylvania Route 997 (PA 997) is a 49.0 mi route in Franklin and Cumberland counties in central Pennsylvania.  The route runs from the Maryland state line south of Waynesboro, where it continues into that state as Maryland Route 64 (MD 64), north to PA 233 in the Upper Mifflin Township community of McCrea.  PA 997 heads north from the state line through agricultural areas in the Cumberland Valley and passes through Waynesboro, where it intersects PA 16, and Mont Alto, where it intersects the south end of PA 233, before coming to U.S. Route 30 (US 30) in Greenwood.  From here, the route turns northwest and comes to a junction with Interstate 81 (I-81) and PA 696 near Scotland and US 11 in Green Village.  PA 997 crosses PA 433 in Culbertson and heads north along the eastern border of Letterkenny Army Depot to Pleasant Hall, where it crosses PA 533.  The route continues north through rural areas and intersects PA 433 near Lurgan and PA 641 in Roxbury before heading northeast and reaching an interchange with the Pennsylvania Turnpike (I-76) near Blue Mountain.  PA 997 leaves Franklin County for Cumberland County and intersects the north end of PA 696 before continuing to McCrea.

James Finley House (Chambersburg, Pennsylvania): James Finley House, also known as the Commanding Officer's Residence, is a historic home located at Letterkenny Army Depot in Greene Township in Franklin County, Pennsylvania.  It was built about 1778, and is a 2 ⁄ -story, limestone farmhouse.  It is five bays wide and has a medium pitched gable roof.  The house was obtained for use as the Commanding Officer's Residence in 1942.  It is one of the oldest surviving dwellings in Franklin County.

Letterkenny Army Depot: Letterkenny Army Depot (originally Letterkenny Ordnance Depot), the Center of Industrial and Technical Excellence (CITE) for Air Defense and Tactical Missile Systems, was established in 1942.  The Depot is under the command structure of the U.S. Army Aviation and Missile Command (AMCOM).  The facilities at Letterkenny are used to conduct maintenance, modification, storage, and demilitarization operations on tactical missiles and ammunition.

Pennsylvania Route 533: Pennsylvania Route 533 (PA 533) is a 21.7 mi state highway located in Franklin and Cumberland Counties in Pennsylvania.  The western terminus is at State Route 4004 (SR 4004) at a junction with Mountain Road, Valley Road, and Community Road in the community of Upper Strasburg in Letterkenny Township.  The eastern terminus is at PA 233 in Newville.  PA 533 heads east from Upper Strasburg as a two-lane undivided road through farmland, passing to the north of Letterkenny Army Depot before crossing PA 997 in Pleasant Hall.  The route continues east and crosses PA 433 in Orrstown before reaching Shippensburg, where it reaches U.S. Route 11 (US 11).  Here, PA 533 becomes concurrent with US 11 and intersects PA 696 in the downtown area and PA 174 upon leaving Shippensburg.  PA 533 splits from US 11 and runs northeast through more agricultural areas before reaching Newville.

Question: Letterkenny Munitions Center, located on Letterkenny Army Depot in Franklin County, Pennsylvania, is a satellite activity under Crane Army Ammunition Activity in Crane, Indiana, Letterkenny Army Depot (originally Letterkenny Ordnance Depot), the Center of Industrial and Technical Excellence (CITE) for Air Defense and Tactical Missile Systems, was established in which year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "depot_name": {
      "type": "string",
      "description": "The current name of the army depot."
    },
    "original_name": {
      "type": "string",
      "description": "The original name of the army depot."
    },
    "establishment_year": {
      "type": "integer",
      "description": "The year the army depot was established."
    },
    "location_county": {
      "type": "string",
      "description": "The county where the depot is located."
    },
    "command_structure": {
      "type": "string",
      "description": "The command structure the depot is under."
    },
    "designation": {
      "type": "string",
      "description": "The special designation or center of excellence for the depot."
    }
  },
  "required": [
    "depot_name",
    "original_name",
    "establishment_year",
    "location_county",
    "command_structure",
    "designation"
  ],
  "additionalProperties": false
}
