{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLand Rover Tangi: The Land Rover Tangi is a type of armoured vehicle, based on the Land Rover chassis used in policing in Northern Ireland.  They have been used by the Royal Ulster Constabulary and, since its renaming, by the Police Service of Northern Ireland.  The vehicle was designed and built in house by the Royal Ulster Constabulary's own engineers.\n\nRoyal Ulster Constabulary: The Royal Ulster Constabulary was the police force in Northern Ireland from 1922 to 2001.  Following the awarding of the George Cross in 2000, its formal title became the Royal Ulster Constabulary, GC.  It was founded on 1 June 1922 as a successor to the Royal Irish Constabulary (RIC).  At its peak the force had around 8,500 officers with a further 4,500 who were members of the RUC Reserve.  During the Troubles, 319 members of the RUC were killed and almost 9,000 injured in paramilitary assassinations or attacks, mostly by the Provisional IRA, which made, by 1983, the RUC the most dangerous police force in the world in which to serve.  In the same period, the RUC killed 55 people, 28 of whom were civilians.\n\nRoyal Ulster Constabulary Service Medal: The Royal Ulster Constabulary Service Medal was a medal created to honor the service of members of the Royal Ulster Constabulary (RUC) and the RUC Reserve.  Established in 1982 and first awarded in 1985, the medal ceased to be awarded when the RUC was replaced by the Police Service of Northern Ireland.\n\nThe Troubles in Magherafelt: A total of eleven people were killed in violence relating to the Northern Irish Troubles in the town of Magherafelt, County Londonderry.  Nine were killed by the Irish Republican Army (IRA), including three IRA members killed by the premature explosion of their own bomb while travelling through Magherafelt.  One was killed by a non-specific republican group and another by the opposing Ulster Freedom Fighters (UFF).  Of the others killed by the IRA, four were Protestant civilians.  Three of them were killed in two separate car bomb explosions.  The fourth Protestant civilian was shot because his firm was a contractor for the British Army and the Royal Ulster Constabulary (RUC).  The IRA's other two victims were both Protestant members of the security forces, one from the RUC and the other from the Ulster Defence Regiment.  Both were off duty when killed.  The man killed by the UFF was a Sinn Féin councillor who was shot in his workplace.  The man killed by the non-specific republican group was a Catholic civilian.\n\nContinuity Irish Republican Army: The Continuity Irish Republican Army, usually known as the Continuity IRA (CIRA) is an Irish republican paramilitary group that aims to bring about a united Ireland.  It emerged from a split in the Provisional IRA in 1986 but did not become active until the Provisional IRA ceasefire of 1994.  It is an illegal organisation in the Republic of Ireland and is designated a terrorist organisation in the United Kingdom, New Zealand and the United States.  It has links with the political party Republican Sinn Féin (RSF).\n\nLoughgall ambush: The Loughgall ambush took place on 8 May 1987 in the village of Loughgall, Northern Ireland.  An eight-man unit of the Provisional Irish Republican Army (IRA) launched an attack on the Royal Ulster Constabulary (RUC) barracks in the village.  An IRA member drove a digger with a bomb in its bucket through the perimeter fence, while the rest of the unit arrived in a van and fired on the building.  The bomb exploded and destroyed almost half of the base.  Soldiers of the British Army's Special Air Service (SAS) then returned fire from the base and opened fire from hidden ambush positions around it, killing all IRA members.  The security forces were aware of the IRA plan and the 24-man SAS unit had been lying in wait.  Two of the IRA members were unarmed.  A civilian was also killed by the SAS after unwittingly driving into the ambush zone.\n\nDissident Irish Republican campaign: Since the Provisional Irish Republican Army (IRA) called a ceasefire and ended its armed campaign in 1997, breakaway groups opposed to the ceasefire (\"dissident Irish republicans\") have continued a low-level armed campaign against the British security forces in Northern Ireland.  The main paramilitaries involved are the Real IRA, Continuity IRA and Óglaigh na hÉireann.  They have targeted the British Army and Police Service of Northern Ireland (PSNI, successor of the Royal Ulster Constabulary) in gun and bomb attacks, as well as with mortars and rockets.  They have also carried out bombings that are meant to cause disruption.  However, their campaign has not been as intensive as the Provisional IRA's.\n\nDenis Donaldson: Denis Martin Donaldson (1950 – 4 April 2006) was a volunteer in the Provisional Irish Republican Army (IRA) and a member of Sinn Féin who was murdered following his exposure in December 2005 as an informer in the employ of MI5 and the Special Branch of the Police Service of Northern Ireland (formerly the Royal Ulster Constabulary).  It was initially believed that the Provisional IRA were responsible for his killing although the Real IRA claimed responsibility for his murder almost three years later.\n\nKenneth Newman: Sir Kenneth Leslie Newman (15 August 1926 – 4 February 2017) was a senior British police officer.  He was Chief Constable of the Royal Ulster Constabulary from 1976 to 1980, and Commissioner of the Metropolitan Police from 1982 to 1987.  He is best known for initiating a major reform and restructure of the Metropolitan Police during his tenure as Commissioner and for seeing the Royal Ulster Constabulary replace the British Army as the dominant security force in Northern Ireland during his tenure as Chief Constable.\n\nShorland armoured car: The Shorland is an armoured patrol car that was designed specifically for the Royal Ulster Constabulary by Frederick Butler with the first design meeting taking place in November 1961.  The third and final prototype was completed in 1964, the first RUC Shorlands were delivered in 1966.  They were reallocated to the Ulster Defence Regiment in 1970.  The Royal Ulster Constabulary soon replaced the Shorland with an armoured Land Rover with more conventional profiles and no machine gun turret.\n\nQuestion: The group known as the Continuity IRA, along with the Real IRA, targeted what successor of the Royal Ulster Constabulary?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"paramilitary_groups_involved\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"List of paramilitary groups involved in the campaign.\"\n    },\n    \"targeted_organizations\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"Name of the organization targeted.\"\n          },\n          \"is_ruc_successor\": {\n            \"type\": \"boolean\",\n            \"description\": \"True if the organization is the successor of the Royal Ulster Constabulary.\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"is_ruc_successor\"\n        ],\n        \"additionalProperties\": false\n      },\n      \"description\": \"List of organizations targeted by the paramilitary groups, indicating if they are the RUC successor.\"\n    },\n    \"ruc_successor_targeted\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the Royal Ulster Constabulary's successor that was targeted.\"\n    }\n  },\n  \"required\": [\n    \"paramilitary_groups_involved\",\n    \"targeted_organizations\",\n    \"ruc_successor_targeted\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "paramilitary_groups_involved": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "List of paramilitary groups involved in the campaign."
      },
      "targeted_organizations": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "Name of the organization targeted."
            },
            "is_ruc_successor": {
              "type": "boolean",
              "description": "True if the organization is the successor of the Royal Ulster Constabulary."
            }
          },
          "required": [
            "name",
            "is_ruc_successor"
          ],
          "additionalProperties": false
        },
        "description": "List of organizations targeted by the paramilitary groups, indicating if they are the RUC successor."
      },
      "ruc_successor_targeted": {
        "type": "string",
        "description": "The name of the Royal Ulster Constabulary's successor that was targeted."
      }
    },
    "required": [
      "paramilitary_groups_involved",
      "targeted_organizations",
      "ruc_successor_targeted"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
