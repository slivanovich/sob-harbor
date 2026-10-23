{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRoyal Irish Rangers: The Royal Irish Rangers (27th (Inniskilling), 83rd and 87th) was a regular infantry regiment of the British Army with a relatively short existence, formed in 1968 and later merged with the Ulster Defence Regiment in 1992 to form the Royal Irish Regiment.\n\nRoyal Irish Regiment (1992): The Royal Irish Regiment (27th (Inniskilling) 83rd and 87th and Ulster Defence Regiment) (R IRISH) is an infantry regiment of the British Army.  The regiment was founded in 1992 through the amalgamation of the Royal Irish Rangers and the Ulster Defence Regiment.  Their oldest predecessor; the 27th Regiment of Foot; was first raised in June 1689 to fight in the Williamite War in Ireland.  Other notable regiments in their lineage include the Royal Inniskilling Fusiliers, Royal Irish Rifles and the Royal Irish Fusiliers (Princess Victoria's).\n\nKillaloe March: Killaloe is the Regimental Quick March of the British Army regiment, The Royal Irish Regiment (27th (Inniskilling) 83rd and 87th and Ulster Defence Regiment).  It has informal, historical associations with other Irish Regiments and Brigades: as an unofficial march by the Connaught Rangers and Royal Inniskilling Fusiliers and at brigade level in World War II by the 38th (Irish) Infantry Brigade.  It is also the regimental march of the South African Irish Regiment.\n\n4th Battalion, Ulster Defence Regiment: 4th (County Fermanagh) Battalion, Ulster Defence Regiment (4 UDR) was formed in 1970 as part of the 7 original battalions specified in The Ulster Defence Regiment Act 1969, which received Royal Assent on 18 December 1969 and was brought into force on 1 January 1970.  It was amalgamated with the 6th Battalion, Ulster Defence Regiment in 1992 to form the 4th/6th Battalion, Ulster Defence Regiment.\n\n1st Battalion, Ulster Defence Regiment: 1st (County Antrim) Battalion, Ulster Defence Regiment (1 UDR) was formed in 1970 as part of the 7 original battalions specified in The Ulster Defence Regiment Act 1969, which received Royal Assent on 18 December 1969 and was brought into force on 1 January 1970.  It was amalgamated with the 9th Battalion, Ulster Defence Regiment in 1984 to form the 1st/9th Battalion, Ulster Defence Regiment.\n\n7th Battalion, Ulster Defence Regiment: 7th (City of Belfast) Battalion, Ulster Defence Regiment (7 UDR) was formed in 1970 as part of the 7 original battalions specified in The Ulster Defence Regiment Act 1969, which received Royal Assent on 18 December 1969 and was brought into force on 1 January 1970.  It was amalgamated with the 10th Battalion, Ulster Defence Regiment in 1984 to form the 7th/10th (City of Belfast) Battalion, Ulster Defence Regiment.\n\nFaugh A Ballagh: Faugh a Ballagh ( ; also written Faugh an Beallach) is a battle cry of Irish origin, meaning \"clear the way\".  The spelling is an 18th-century anglicization of the Irish language phrase Fág an Bealach ] , also written \"Fág a' Bealach\".  Its first recorded use as a regimental motto was by the 87th (Prince of Wales's Irish) Regiment of Foot (who later became the Royal Irish Fusiliers) in 1798.  It remains the motto of the Royal Irish Regiment today.\n\n28th Regiment Massachusetts Volunteer Infantry: The 28th Massachusetts Infantry regiment was the second primarily Irish American volunteer infantry regiment recruited in Massachusetts for service in the American Civil War.  The regiment's motto (or cry) was \"Faugh a Ballagh (Clear the Way!)\"\n\n11th Battalion, Ulster Defence Regiment: The 11th (Craigavon) Battalion, Ulster Defence Regiment was formed from companies of the 2nd Battalion Ulster Defence Regiment (2 UDR) and the 3rd Battalion Ulster Defence Regiment in 1972.  In 1991 under the reductions planned in Options for Change by the British Army, it again amalgamated with 2 UDR to form the 2nd/11th Battalion Ulster Defence Regiment.\n\n2nd Battalion, Ulster Defence Regiment: 2nd (County Armagh) Battalion, Ulster Defence Regiment (2 UDR) was formed in 1970 as part of the seven original battalions specified in the Ulster Defence Regiment Act 1969, which received Royal Assent on 18 December 1969 and was brought into force on 1 January 1970.  It was, along with the rest of the regiment, amalgamated with the Royal Irish Rangers in 1992 to form the Royal Irish Regiment.  It had previously been amalgamated in 1991 with the 11th Battalion Ulster Defence Regiment to form the 2nd/11th Battalion Ulster Defence Regiment.\n\nQuestion: Faugh a Ballagh, is a battle cry of Irish origin, meaning \"clear the way\", and today it remains the motto of which (27th (Inniskilling) 83rd and 87th and Ulster Defence Regiment) (R IRISH) is an infantry regiment of the British Army?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"regiment_name\": {\n      \"type\": \"string\",\n      \"description\": \"The common name of the regiment.\"\n    },\n    \"regiment_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of regiment.\"\n    },\n    \"army_affiliation\": {\n      \"type\": \"string\",\n      \"description\": \"The army the regiment is affiliated with.\"\n    },\n    \"motto\": {\n      \"type\": \"string\",\n      \"description\": \"The battle cry or motto of the regiment.\"\n    },\n    \"motto_meaning\": {\n      \"type\": \"string\",\n      \"description\": \"The meaning of the motto.\"\n    }\n  },\n  \"required\": [\n    \"regiment_name\",\n    \"regiment_type\",\n    \"army_affiliation\",\n    \"motto\",\n    \"motto_meaning\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "regiment_name": {
        "type": "string",
        "description": "The common name of the regiment."
      },
      "regiment_type": {
        "type": "string",
        "description": "The type of regiment."
      },
      "army_affiliation": {
        "type": "string",
        "description": "The army the regiment is affiliated with."
      },
      "motto": {
        "type": "string",
        "description": "The battle cry or motto of the regiment."
      },
      "motto_meaning": {
        "type": "string",
        "description": "The meaning of the motto."
      }
    },
    "required": [
      "regiment_name",
      "regiment_type",
      "army_affiliation",
      "motto",
      "motto_meaning"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
