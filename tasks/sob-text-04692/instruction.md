{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nHackney London Borough Council: Hackney London Borough Council is the local government authority for the London Borough of Hackney, London, England, one of 32 London borough councils.  The council is unusual in the United Kingdom local government system in that its executive function is controlled by a directly elected mayor of Hackney, currently Philip Glanville of the Labour Party.  Hackney comprises 19 wards, each electing three Councillors. Following the May 2014 election, Hackney London Borough Council consists of 50 Labour Party councillors, four Conservative Party councillors and three Liberal Democrat councillors.  The council was created by the London Government Act 1963 whereby it replaced three local authorities: Hackney Metropolitan Borough Council, Shoreditch Metropolitan Borough Council and Stoke Newington Metropolitan Borough Council.\n\nStoke Newington: Stoke Newington is an area occupying the north-west part of the London Borough of Hackney in north-east London.  It is 5 miles north-east of Charing Cross.  Stoke Newington Church Street was the site of the original hamlet of Stoke Newington, which in turn gave its name to Stoke Newington the ancient parish.\n\nDiane Abbott: Diane Julie Abbott (born 27 September 1953) is a British Labour Party politician who was appointed Shadow Home Secretary in October 2016.  She was first elected as the Member of Parliament (MP) for Hackney North and Stoke Newington at the 1987 general election, when she became the first black woman to hold a seat in the House of Commons.\n\nStoke Newington Central (ward): Stoke Newington Central is a ward in the London Borough of Hackney.  It corresponds roughly to Stoke Newington in London, UK and forms part of the Hackney North and Stoke Newington constituency of Diane Abbott MP.\n\nLeabridge (ward): Leabridge is a ward in the London Borough of Hackney and roughly corresponds to the Lea Bridge district of London, and is distinct from the Lea Bridge ward in the neighbouring London Borough of Waltham Forest.  It is part of Hackney North and Stoke Newington constituency.  The ward has existed since the creation of the borough on 1 April 1965 and was first used in the 1964 elections.\n\nStoke Newington Common: Stoke Newington Common is an open space in Stoke Newington in the London Borough of Hackney.  It is east of Stoke Newington High Street, with Northwold Road to the north, and it straddles the busy Rectory Road.  The Common is 2.15 ha in area.\n\nDeath of Colin Roach: Colin Roach was a 21-year-old black British man who died from a gunshot wound inside the entrance of Stoke Newington police station, in the London Borough of Hackney, on 12 January 1983.  Amid allegations of a police cover-up, the case became a cause célèbre for civil rights campaigners and black community groups in the United Kingdom.  Prior to Roach's death, Hackney Black People's Association had been calling for a public inquiry into policing in the area, alleging that there existed a culture of police brutality, wrongful detention of black people, racial harassment, and racially motivated \"stopping and searching.\"  Ernie Roberts, the MP for Hackney North and Stoke Newington, said that there had been \"a complete breakdown of faith and credibility in the police\" in the area and the Commission for Racial Equality called for a full inquiry into both the death of Roach and the policing in Hackney generally.  In June 1983 a coroner's jury returned a majority verdict of suicide.  INQUEST, the United Kingdom pressure group founded following the death of Blair Peach at the hands of a police officer in April 1979, was highly critical of the coroner's directions to the jury, and said that he had wrongly pointed them towards a verdict of suicide.\n\nHackney Downs (ward): Hackney Downs is a ward in the London Borough of Hackney, corresponding roughly to the Hackney Downs area of London, UK and forms part of the Hackney North and Stoke Newington constituency.\n\nBrownswood (ward): Brownswood is a ward in the London Borough of Hackney and forms part of the Hackney North and Stoke Newington constituency.  The ward has existed since the creation of the borough on 1 April 1965 and was first used in the 1964 elections.  The population of the ward in 2011 was 11,091.  The boundaries of the ward from May 2014 are revised.\n\nClissold Park: Clissold Park is a designated community park in Stoke Newington, within the London Borough of Hackney.  It is bounded by Greenway Close (to the north), Stoke Newington Church Street (to the south) and Green Lanes (west) and Queen Elizabeth's Walk (east).  The park derives its name from Metropolitan Borough of Stoke Newington the local authority when it was established.  The park is (22.57 hectares (55.8 acres)) in extent.\n\nQuestion: Stoke Newington Central is a ward in the London Borough of Hackney, it corresponds roughly to Stoke Newington in London, UK and forms part of the Hackney North and Stoke Newington constituency of which British Labour Party politician, who was appointed Shadow Home Secretary, in October 2016?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"politician_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the politician.\"\n    },\n    \"political_party\": {\n      \"type\": \"string\",\n      \"description\": \"The political party the politician belongs to.\"\n    },\n    \"role\": {\n      \"type\": \"string\",\n      \"description\": \"The political role held by the politician.\"\n    },\n    \"appointment_date\": {\n      \"type\": \"string\",\n      \"description\": \"The date of appointment to the specified role.\"\n    },\n    \"constituency\": {\n      \"type\": \"string\",\n      \"description\": \"The parliamentary constituency represented by the politician.\"\n    },\n    \"associated_ward\": {\n      \"type\": \"string\",\n      \"description\": \"A ward that forms part of the politician's constituency.\"\n    }\n  },\n  \"required\": [\n    \"politician_name\",\n    \"political_party\",\n    \"role\",\n    \"appointment_date\",\n    \"constituency\",\n    \"associated_ward\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "politician_name": {
        "type": "string",
        "description": "The full name of the politician."
      },
      "political_party": {
        "type": "string",
        "description": "The political party the politician belongs to."
      },
      "role": {
        "type": "string",
        "description": "The political role held by the politician."
      },
      "appointment_date": {
        "type": "string",
        "description": "The date of appointment to the specified role."
      },
      "constituency": {
        "type": "string",
        "description": "The parliamentary constituency represented by the politician."
      },
      "associated_ward": {
        "type": "string",
        "description": "A ward that forms part of the politician's constituency."
      }
    },
    "required": [
      "politician_name",
      "political_party",
      "role",
      "appointment_date",
      "constituency",
      "associated_ward"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
