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
Midewin National Tallgrass Prairie: The Midewin National Tallgrass Prairie (MNTP) is a tallgrass prairie reserve and United States National Grassland operated by the United States Forest Service.  The first national tallgrass prairie ever designated in the U.S. and the largest conservation site in the Chicago Wilderness region, it is located on the site of the former Joliet Army Ammunition Plant between the towns of Elwood, Manhattan and Wilmington in northeastern Illinois.

Joliet Army Ammunition Plant: Joliet Army Ammunition Plant (JOAAP, formerly known as the Joliet Arsenal) was a United States Army arsenal located in Will County, Illinois, near Elwood, Illinois, south of Joliet, Illinois.  Opened in 1940 during World War II, the facility consisted of the Elwood Ordnance Plant (EOP) and the Kankakee Ordnance Works (KNK).  In 1945, the two were deactivated and combined forming the Joliet Arsenal.  The plant was reactivated for the Korean War and renamed Joliet Army Ammunition Plant during the Vietnam War.  Production of TNT ended in 1976, and the major plant operations closed shortly after in the late 1970s.  The facility briefly revived an automated load-assemble-pack (LAP) artillery shell operation that was managed by the Honeywell Corporation during the Reagan administration in the 1980s before it was finally closed.

Big Stone National Wildlife Refuge: Straddling the headwaters of the Minnesota River in extreme west-central Minnesota, Big Stone National Wildlife Refuge is within the heart of the tallgrass prairie's historic range.  Today, less than one-percent of tallgrass prairie remains.

Tallgrass Prairie Preserve: The Tallgrass Prairie Preserve, located in Osage County, Oklahoma near Foraker, Oklahoma, is owned and managed by The Nature Conservancy.  It is protected as the largest tract of remaining tallgrass prairie in the world.  The preserve contains 39000 acre owned by the Conservancy and another 6000 acre leased in what was the original tallgrass region of the Great Plains that stretched from Texas to Manitoba.

Nine Mile Prairie: Nine Mile Prairie (named for its location 5 mi west and 4 mi north of downtown Lincoln) is a 230 acre tract of conserved tallgrass prairie in Lancaster County, Nebraska, United States.  Except for one small portion of it that was farmed as recently as the 1950s, Nine-Mile Prairie has never been plowed (some of the land has at times been grazed as recently as the 1960s).  As such, it is one of the largest areas of virgin tallgrass prairie in the state of Nebraska.  It has been listed on the National Register of Historic Places since 1986.

Tallgrass Aspen Parkland: The Tallgrass Aspen Parkland is a Conservation area located in southeastern Manitoba and northwestern Minnesota.  The area is characterized by a mosaic of habitat types, including tallgrass prairie, aspen woodland, sedge meadow wetlands, riparian woodland, and oak savannah.  A number of endangered and threatened species occur in the area, including the Western Prairie Fringed Orchid and Dakota Skipper.  One of Minnesota's only wild elk herds utilizes the area as well.

Manitoba Tall Grass Prairie Preserve: The Manitoba Tall Grass Prairie Preserve is located in southeastern Manitoba near Gardenton and Vita, this is about 50 km south of Steinbach, Manitoba.  It is one of the last remaining stands of tallgrass prairie in Manitoba and is part of the Tallgrass Aspen Parkland conservation area in Manitoba and Minnesota.  Several groups and organizations help in land preservation in the Manitoba Tall Grass Prairie such as the Nature Conservancy of Canada, Nature Manitoba, Environment Canada, Manitoba Conservation and the Manitoba Habitat Heritage Corporation.

Tallgrass Prairie bison herd: The Tallgrass Prairie bison herd is a population of genetically pure American bison ("Bison bison") inhabiting the Tallgrass Prairie National Preserve in central Kansas.

Tallgrass Prairie National Preserve: Tallgrass Prairie National Preserve is a United States National Preserve located in the Flint Hills region of Kansas, north of Strong City.  The preserve protects a nationally significant example of the once vast tallgrass prairie ecosystem.  Of the 400,000 square miles (1,000,000 km) of tallgrass prairie that once covered the North American continent, less than 4% remains, primarily in the Flint Hills.  Since 2009, the preserve has been home to the growing Tallgrass Prairie bison herd.

Harrell Prairie Botanical Area: Harrell Prairie Botanical Area or Harrell Prairie Hill is a 160 acre tallgrass prairie nature preserve located within Bienville National Forest near Forest, Mississippi.  It is a rare remaining example of the Jackson Prairie Belt in Mississippi.  It was declared a National Natural Landmark in May 1976 and a Botanical Area by the Forest Service in 1980.

Question: When did the Army arsenal formerly located on the site now occupied by the Midewin National Tallgrass Prairie open?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "former_facility": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the former facility."
        },
        "type": {
          "type": "string",
          "description": "The type of the former facility (e.g., arsenal, plant)."
        },
        "opening_year": {
          "type": "integer",
          "description": "The year the facility opened."
        },
        "associated_conflict": {
          "type": "string",
          "description": "A historical conflict associated with the facility's opening."
        }
      },
      "required": [
        "name",
        "type",
        "opening_year"
      ],
      "additionalProperties": false
    },
    "current_site": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the current site occupying the former facility's location."
        },
        "type": {
          "type": "string",
          "description": "The type of the current site (e.g., national tallgrass prairie)."
        }
      },
      "required": [
        "name",
        "type"
      ],
      "additionalProperties": false
    },
    "question_answer": {
      "type": "integer",
      "description": "The direct answer to the question, which is the opening year."
    }
  },
  "required": [
    "former_facility",
    "current_site",
    "question_answer"
  ],
  "additionalProperties": false
}
