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
Rainy Lake Falls: Rainy Lake Falls is a waterfall on the inlet stream of namesake "Rainy Lake" in Chelan County, Washington.  The stream heads in a pair of small lakes and the remaining portions of the Lyall Glacier, and flows down a cascade that is said to be approximately 850 ft high.

Fort Saint Pierre: Fort Saint Pierre on Rainy Lake was the first French fort built west of Lake Superior.  It was the first of eight forts built during the elder Vérendrye's expansion of trade and exploration westward from the Great Lakes.  He reached Grand Portage in late August 1731.  Here most of the men refused to continue because of the late season, difficult portage and largely unknown country.  Vérendrye wintered with most of the men at Fort Kaministiquia, but was able to send a few willing men westward under Christopher Dufrost de La Jemeraye.  La Jemeraye reached Rainy Lake before the freezeup and built a fort at its outlet.  Next May he sent a small load of furs back eastward, Vérendrye arrived in July, and pushed west to Lake of the Woods where he built Fort Saint Charles which quickly overshadowed Fort St. Pierre.  Coureurs des bois spread out and drew trade away from the English, but we only know of them from rumors picked up by the English on Hudson Bay.  The area produced fish and wild rice.  The local people were Monsonis, with Cree further west.  Both were at war with the Sioux to the south.  The post remained in operation until 1758.  Fort Lac la Pluie was built nearby by the North West Company sometime between 1775 and 1787.  There is a modern reconstruction of the fort.  The site was on the north bank of the Rainy River just past a series of rapids near its outflow from the lake at the modern town of Fort Frances.

Rainy Lake 17A: Rainy Lake 17A is a First Nations reserve on Rainy Lake in northwestern Ontario.  It is one of the reserves of the Naicatchewenin First Nation.

Rainy Lake 26C: Rainy Lake 26C is a First Nations reserve in Rainy River District, Ontario.  It is one of the reserves of the Nigigoonsiminikaaning First Nation.

Rainy Lake 18C: Rainy Lake 18C is a First Nations reserve on Rainy Lake in Rainy River District, Ontario.  It is the main reserve of the Mitaanjigamiing First Nation.

Indian reserve: In Canada, an Indian reserve (French: "réserve autochtone" ) is specified by the Indian Act as a "tract of land, the legal title to which is vested in Her Majesty, that has been set apart by Her Majesty for the use and benefit of a band."

Rainy Lake and River Bands of Saulteaux: Rainy Lake and River Bands of Saulteaux (Ojibwe language: Gojijiwininiwag) were a historical Saulteaux (Ojibwe) group located in Northwestern Ontario and northern Minnesota, along and about the Rainy Lake and the Rainy River, known in Ojibwe as "Gojijiing".

Rainy Lake: Rainy Lake (French: "lac à la Pluie"; Ojibwe: "gojiji-zaaga'igan") is a relatively large freshwater lake (360 sqmi ) straddling the border between the United States and Canada.  The Rainy River issues from the west side of the lake and is harnessed to make hydroelectricity for US and Canadian locations.  The sister cities of International Falls, Minnesota, and Fort Frances, Ontario, are situated on either side of the outflow of the river from the lake.  Rainy Lake and Rainy River establish part of the boundary between the U.S. state of Minnesota and the Canadian province of Ontario.

Rainy Lake 26B: Rainy Lake 26B is a First Nations reserve in Rainy River District, Ontario.  It is one of the reserves of the Nigigoonsiminikaaning First Nation.

Rainy Lake 26A: Rainy Lake 26A is a First Nations reserve on Rainy Lake in Rainy River District, Ontario.  It is the main reserve of the Nigigoonsiminikaaning First Nation.

Question: Rainy Lake 26A was set apart by who?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "reserve_name": {
      "type": "string",
      "description": "The name of the First Nations reserve."
    },
    "reserve_designation_type": {
      "type": "string",
      "description": "The type of land designation, e.g., 'First Nations reserve' or 'Indian reserve'."
    },
    "entity_responsible_for_setting_apart": {
      "type": "string",
      "description": "The entity or authority that set apart the land for the reserve."
    },
    "location_details": {
      "type": "object",
      "properties": {
        "district": {
          "type": "string",
          "description": "The district where the reserve is located."
        },
        "province": {
          "type": "string",
          "description": "The province where the reserve is located."
        },
        "country": {
          "type": "string",
          "description": "The country where the reserve is located."
        }
      },
      "required": [
        "district",
        "province",
        "country"
      ],
      "additionalProperties": false
    },
    "associated_first_nation": {
      "type": "string",
      "description": "The First Nation associated with this reserve."
    }
  },
  "required": [
    "reserve_name",
    "reserve_designation_type",
    "entity_responsible_for_setting_apart",
    "location_details",
    "associated_first_nation"
  ],
  "additionalProperties": false
}
