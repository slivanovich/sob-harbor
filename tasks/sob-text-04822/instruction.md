{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCochran Grange: The Cochran Grange, also known as John P. Cochran House, is a historic home located in Middletown, New Castle County, Delaware.  It was built between 1842 and 1845, and consists of a two-story, five bay, main block with a two-story wing.  The design is influenced by the Greek Revival, Italianate, and Georgian styles.  The house features a two-story porch supported by Doric order columns and a flat roof surmounted by a square cupola.  Cochran Grange was the home of John P. Cochran, 43rd Governor of Delaware (1875–1879).\n\nGary S. Fields: Gary S. Fields is an American economist, the John P. Windmuller Professor of International and Comparative Labor and Professor of Economics at Cornell University.  Fields' has performed extensive research in labor economics and development economics, in particular labor mobility, which was rewarded with the IZA Prize in Labor Economics in 2014.\n\nMontgomery County Sheriff's Office (Pennsylvania): The Montgomery County Sheriff's Office provides police protection for Montgomery County, Pennsylvania in conjunction with local and Pennsylvania State Police.  Pennsylvania law calls for the Sheriff to be elected every four years.  Sheriff John P. Durante died suddenly on February 10, 2010 and Chief Deputy Sheriff Alfred J. Ricci became the Acting Sheriff.  On May 6, 2011, Eileen Whalon Behr, who had been appointed Sheriff by the Governor and confirmed by the Pennsylvania Senate, was sworn in to serve the balance of John P. Durante's term.  Behr had previously served as Chief of Police in Whitemarsh Township.  Behr was subsequently elected to a full four-year term on November 8, 2011.\n\nMapuche uprising of 1881: The Mapuche uprising of 1881 was the last major rebellion of the indigenous Mapuches of Araucanía.  The uprising took place during the last phase of the Occupation of Araucanía (1861–1883) by the Chilean state.  The uprising was planned by Mapuche chiefs in March 1881 to be launched in November of the same year.  Mapuche support for the uprising was not unanimous, some Mapuche factions sided with the Chileans and others declared themselves neutral.  The organizers of the uprising did however succeed in involving Mapuche factions that had not previously been at war with Chile.  The 1881 uprising can be considered the climax of the Chilean-Mapuche hostilities during the Occupation of Araucanía.\n\nJohn P. Buchanan: John Price Buchanan (October 24, 1847May 14, 1930) was an American politician and farmers' advocate.  He served as Governor of Tennessee from 1891 to 1893, and was president of the Tennessee Farmers' Alliance and Laborers' Union in the late 1880s.  Buchanan's lone term as governor was largely marred by the Coal Creek War, an armed uprising by coal miners aimed at ending the state's convict lease system.\n\nBattle of Blair Mountain: The Battle of Blair Mountain was the largest labor uprising in United States history and one of the largest, best-organized, and most well-armed uprisings since the American Civil War.  For five days in late August and early September 1921, in Logan County, West Virginia, some 10,000 armed coal miners confronted 3,000 lawmen and strikebreakers, called the Logan Defenders, who were backed by coal mine operators during an attempt by the miners to unionize the southwestern West Virginia coalfields.  The battle ended after approximately one million rounds were fired, and the United States Army intervened by presidential order.\n\nOxford Fashion Week: Oxford Fashion Week was established in 2009.  The event is now an annual fashion feature and takes place primarily over the course of one week in the year, with satellite events at other times.  In 2009 and 2010, Oxford Fashion Week took place in May.  In 2011, it took place in March.  In 2012, it took place in November.  Since 2013, the Oxford fashion week is taking place biannually displaying summer collections in March and autumn collections in September.\n\n1989 Jonesborough ambush: The Jonesborough ambush took place on 20 March 1989 near the Irish border outside the village of Jonesborough, County Armagh, Northern Ireland.  Two senior Royal Ulster Constabulary (RUC) officers, Chief Superintendent Harry Breen and Superintendent Bob Buchanan, were shot dead in an ambush by the Provisional IRA South Armagh Brigade.  Breen and Buchanan were returning from an informal cross-border security conference in Dundalk with senior Garda officers when Buchanan's car – a red Vauxhall Cavalier — was flagged down and fired upon by six IRA gunmen, who the policemen had taken for British soldiers.  Buchanan was killed outright whilst Breen, suffering gunshot wounds, was deliberately shot in the back of the head after he had left the car waving a white handkerchief.  They were the highest-ranking RUC officers to be killed during the Troubles.\n\nCoal Creek War: The Coal Creek War was an early 1890s armed labor uprising in the southeastern United States that took place primarily in Anderson County, Tennessee.  This labor conflict ignited during 1891 when coal mine owners in the Coal Creek watershed began to remove and replace their company-employed, private coal miners then on the payroll with convict laborers leased out by the Tennessee state prison system.\n\nGreene–Jones War: The Greene–Jones War was an ongoing Appalachian Mountain clan feud in the United States reputed to be second only to that of the Hatfield-McCoy feud in scale, duration, and number of persons killed.  At least sixteen people, including one child, were killed during the course of the feud, and many others were seriously injured.  The feud took place primarily in the border areas of Hawkins County (formerly part of Sullivan County, North Carolina, one of the earliest Tennessee counties and said to have a large Melungeon population), Washington County, Claiborne County, Hancock County, Tennessee (created when Hawkins County, Tennessee was subdivided), and Lee County, Virginia, not far from Cumberland Gap, the narrow Appalachian Mountain pass sometimes called The Wilderness Road leading into Kentucky.\n\nQuestion: John P. Buchanan's lone term as governor was largely marred by a labor uprising that took place primarily in what county in Tennessee?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person whose term was marred.\"\n    },\n    \"person_role\": {\n      \"type\": \"string\",\n      \"description\": \"The political role held by the person.\"\n    },\n    \"marring_event\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the event that marred the person's term.\"\n        },\n        \"type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of the event (e.g., labor uprising).\"\n        },\n        \"primary_location\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"county\": {\n              \"type\": \"string\",\n              \"description\": \"The primary county where the event took place.\"\n            },\n            \"state\": {\n              \"type\": \"string\",\n              \"description\": \"The state where the event took place.\"\n            }\n          },\n          \"required\": [\n            \"county\",\n            \"state\"\n          ],\n          \"additionalProperties\": false\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"type\",\n        \"primary_location\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"person_role\",\n    \"marring_event\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the person whose term was marred."
      },
      "person_role": {
        "type": "string",
        "description": "The political role held by the person."
      },
      "marring_event": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the event that marred the person's term."
          },
          "type": {
            "type": "string",
            "description": "The type of the event (e.g., labor uprising)."
          },
          "primary_location": {
            "type": "object",
            "properties": {
              "county": {
                "type": "string",
                "description": "The primary county where the event took place."
              },
              "state": {
                "type": "string",
                "description": "The state where the event took place."
              }
            },
            "required": [
              "county",
              "state"
            ],
            "additionalProperties": false
          }
        },
        "required": [
          "name",
          "type",
          "primary_location"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "person_name",
      "person_role",
      "marring_event"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
