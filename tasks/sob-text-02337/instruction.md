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
Walcha Shire: Walcha Shire is a local government area located in the New England region of New South Wales, Australia.  The Shire is situated adjacent to the junction of the Oxley Highway and Thunderbolts Way and is 20 km east of the Main North railway line passing through Walcha Road.

Thunderbolts Way: The Thunderbolts Way is a 290 km country road located in the Northern Tablelands region of New South Wales, Australia.  The road links Gloucester to Walcha (where it crosses the Oxley Highway), Uralla, where it very briefly joins the New England Highway and, to Copes Creek, 16 km south of the Gwydir Highway intersection at Inverell.  The road is fully sealed and passes through thickly forested mountain areas with many nearby national parks and nature reserves.

Barrington, New South Wales: Barrington is a small village on the Barrington River, 5 km north-west of Gloucester, New South Wales, Australia on Thunderbolts Way.

Gilgai, New South Wales: Gilgai is a village in the Northern Tablelands region of New South Wales, Australia The village is situated 10 km south of Inverell, New South Wales on Thunderbolts Way and is in Inverell Shire.  At the 2006 census, Gilgai had a population of 289 people.  The name Gilgai is an Aboriginal word meaning 'waterhole'.

Bretti Nature Reserve: The Bretti Nature Reserve is a protected nature reserve located near the Barrington Tops in the Hunter Region of New South Wales, Australia.  The 2902 ha reserve is situated approximately 30 km north of Gloucester.  Flora includes wet sclerophyll eucalyptus forest and rainforest.  It is most often viewed on a drive along the Thunderbolts Way.  The locally rare wompoo fruit dove may be heard in rainforest areas.

New England Highway: The New England Highway is an 878 km long highway in Australia running from Hexham at Newcastle, New South Wales at its southern end to Yarraman near Toowoomba, Queensland at its northern end.

Nowendoc, New South Wales: Nowendoc is a parish and village on the Northern Tablelands, New South Wales, Australia.  It is 360 km north of the state capital, Sydney, 66 km south of Walcha in the Walcha Shire local government area.  A sealed road, Thunderbolts Way, is about three hundred metres to the south of Nowendoc and provides links to the south and north.

Uralla, New South Wales: Uralla is a town on the Northern Tablelands, New South Wales, Australia.  The town is located at the intersection of the New England Highway and Thunderbolts Way, 465 km north of Sydney and about 23 km south west of the city of Armidale.  At the 2011 census , the township of Uralla had a population of 2,388 people, while the larger gazetted locality of 193.5 km had a population of 2,754 people.

Bundarra, New South Wales: Bundarra is a small town on the Northern Tablelands of New South Wales, Australia.  The town is located on Thunderbolts Way and on the banks of the Gwydir River, in the Uralla Shire local government area, 563 kilometres (350 mi) kilometres from the state capital, Sydney.  At the 2011 census , Bundarra had a population of 404 and the surrounding area had 805 persons.

Kentucky, New South Wales: Kentucky is a village in the New England region of New South Wales, Australia.  The village is situated about 17 km to the south of Uralla and 35 km to the north west of Walcha and approximately 7 km off the New England Highway.  Kentucky is located 540 km by rail from Sydney in Sandon County on the Northern Tablelands.  The village is at an altitude of about 1066 m and is within Uralla Shire.  At the 2006 census, Kentucky and the surrounding area had a population of 311.

Question: Uralla, New South Wales is located at the intersection of Thunderbolts Way and the highway that is of what length?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "town_name": {
      "type": "string",
      "description": "The name of the town."
    },
    "intersecting_roads": {
      "type": "array",
      "description": "A list of roads that intersect at the specified town.",
      "items": {
        "type": "string"
      }
    },
    "highway_of_interest": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the highway whose length is being queried."
        },
        "length_km": {
          "type": "integer",
          "description": "The length of the highway in kilometers."
        }
      },
      "required": [
        "name",
        "length_km"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "town_name",
    "intersecting_roads",
    "highway_of_interest"
  ],
  "additionalProperties": false
}
