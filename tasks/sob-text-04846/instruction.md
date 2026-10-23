{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBab-i-Pakistan: Bab-i-Pakistan is Pakistan's busiest border gate and crossing terminal with Afghanistan.  Pakistan has completed the construction of the border gate, crossing terminal and other associated infrastructure on its side of Torkham border by July 2016.  The border gate has been named as Bab-i-Pakistan and the crossing terminal has been named \"Shaheed Major Ali Jawad Changezi terminal\" after the officer lost his life in skirmishes against the Afghan security forces at the same border and in the clashes that resulted from the construction of this very gate.  The flag hosting ceremony has also started just like the one at Wagah border crossing with India.  Now no one will be allowed to cross border without proper documentations to check the infiltration of terrorists from Afghanistan into Pakistan.  Work on the construction of the gate and associated facilities began in 2014 but kept getting delayed because of Afghan reservations and abrupt clashes.  Pakistan plans to have similar border control measures at all six major crossing points between the two countries on the 2,600 km-long porous border.\n\nPembina, North Dakota: Pembina is a city in Pembina County, North Dakota, United States.  The population was 592 at the 2010 census.  Pembina is located 2 mi south of the Canada–US border.  Interstate 29 passes on the west side of Pembina, leading north to the Canada–US border at Emerson, Manitoba and south to the cities of Grand Forks and Fargo.  The Pembina-Emerson Border Crossing is the busiest between Blaine, Washington and Detroit, Michigan and the fifth busiest along the Canada-United States border.  It is one of three 24-hour ports of entry in North Dakota, the others being Portal and Dunseith.  The Emerson-Noyes border crossing, located 2 mi to the east on the Minnesota side of the Red River, also processed cross border traffic until its closure in 2006.\n\nThe Centre for Cross Border Studies: The Centre for Cross Border Studies (CCBS) is a think tank based in Ireland.\n\nCounty Louth: County Louth (Irish: \"Contae Lú\" ) is a county in Ireland.  It is in the province of Leinster and is part of the Border Region.  It is named after the village of Louth.  Louth County Council is the local authority for the county.  The population of the county is 122,897 according to the 2016 census.\n\nCross Border Trio: Cross Border Trio is an international collaborate jazz group featuring American saxophonist Jason Robinson (musician), bassist Rob Thorsen, and Mexican percussionist Paquito Villa.  Formed in 2003, the group has released an album, \"New Directions\" (2007/Circumvention), and toured extensively throughout Mexico and occasionally appeared in the United States.  Since 2008, the group has featured a rotating cast of guest members and used the names of Cross Border Trio and X Border.\n\nCross Border Orchestra of Ireland: The Cross Border Orchestra of Ireland (CBOI) is one of Ireland's primary youth orchestras.  Based at the Dundalk Institute of Technology in County Louth, the CBOI maintains a membership of 160 young musicians between the ages of 12 and 24 years from both sides of the border.\n\nCross border attacks in Sabah: The Cross border attacks in Sabah are a series of cross border terrorism perpetrated by the Moro pirates from Mindanao on Sabah that began even before the British colonial period.  Many civilians have died or suffered during these incidents, causing an increase in anti-Filipino sentiment among the native peoples of Sabah, especially after major attacks in 1985, 2000 and 2013.  The attacks were more intense during the presidential terms of Diosdado Macapagal and Ferdinand Marcos who supported irredentist claims to include eastern Sabah as part of the Philippines territory.  In addition with the recent infiltration and attacks by militants as well the uncontrolled human migration from Mindanao to Sabah that has led to more unease sentiments among the local residents of Sabah, with around 78% prison inmates that were caught in the state due to involvement in criminal activities and lawlessness issues are mainly originated from the southern Philippines.\n\nThe North/South Language Body: The North/South Language Body (Irish: \"An Foras Teanga Thuaidh/Theas\" ; Ulster-Scots: Tha Noarth/Sooth Boord o Leid or The Langage Curn) is an implementation body, provided for by the Belfast Agreement, that exists to implement policies agreed by Ministers in the North/South Ministerial Council (NSMC) in Republic of Ireland and Northern Ireland with regard to the Irish and Ulster-Scots (or \"Ullans\") languages on a cross border all Island basis.\n\nGerry MacLochlainn: Gerard \"Gerry\" MacLochlainn (born 1954) is a Sinn Féin politician from Derry, Northern Ireland, where he was a councillor.  He chaired several of the council's major committees including regional and cross border committees.  His writings were widely circulated in his now deceased wife (Valerie June \"Val\" Cardwell)'s native Wales and several of his prison letters are held in the National Library of Wales.\n\nČadca railway station: Čadca railway station (Slovak: \"Železničná stanica Čadca\" ) is the main station serving the municipality and district town of Čadca, in the Žilina Region, northern Slovakia.  Opened in 1871, the station forms part of the cross border Žilina–Čadca–Svrčinovec zastávka–Mosty u Jablunkova railway, and is also a junction station for two other lines, one of them also cross border.\n\nQuestion: Cross Border Orchestra of Ireland is based at an institute in what province?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"orchestra_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the orchestra.\"\n    },\n    \"institute_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the institute where the orchestra is based.\"\n    },\n    \"county_name\": {\n      \"type\": \"string\",\n      \"description\": \"The county where the institute is located.\"\n    },\n    \"province_name\": {\n      \"type\": \"string\",\n      \"description\": \"The province where the county is located.\"\n    }\n  },\n  \"required\": [\n    \"orchestra_name\",\n    \"institute_name\",\n    \"county_name\",\n    \"province_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "orchestra_name": {
        "type": "string",
        "description": "The name of the orchestra."
      },
      "institute_name": {
        "type": "string",
        "description": "The name of the institute where the orchestra is based."
      },
      "county_name": {
        "type": "string",
        "description": "The county where the institute is located."
      },
      "province_name": {
        "type": "string",
        "description": "The province where the county is located."
      }
    },
    "required": [
      "orchestra_name",
      "institute_name",
      "county_name",
      "province_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
