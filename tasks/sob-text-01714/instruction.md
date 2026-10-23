{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nADX Florence: The United States Penitentiary, Administrative Maximum Facility (ADX) is an American federal supermax prison for male inmates located in Fremont County, Colorado.  It is unofficially known as ADX Florence, Florence ADMAX, or the \"Alcatraz of the Rockies.\"  It is part of the Florence Federal Correctional Complex, which is operated by the Federal Bureau of Prisons (BOP), a division of the United States Department of Justice.  It houses the male inmates in the federal prison system who are deemed the most dangerous and in need of the tightest control.  ADX also includes an adjacent minimum-security camp that, as of 2014 , houses more prisoners than the supermax unit.\n\nUnited States Penitentiary, Lompoc: The United States Penitentiary, Lompoc (USP Lompoc) is a medium-security United States federal prison for male inmates in California.  It is part of the Lompoc Federal Correctional Complex (FCC Lompoc) and is operated by the Federal Bureau of Prisons, a division of the United States Department of Justice.  The facility also has a satellite prison camp for minimum-security male inmates.  It was formerly a military disciplinary barracks on Camp Cooke.\n\nPutnamville Correctional Facility: The Putnamville Correctional Facility, located in Warren Township, Putnam County, near Greencastle, Indiana, is a medium-security prison for men located on 4350 acre in Putnam County, Indiana (the west-central part of the state, near U.S. Routes 231 and 40).  It currently houses approximately 2,400 inmates.  Established in 1914, the prison was known for nearly 70 years as the Indiana State Farm.  Inmates, nearly all of whom were serving time for minor offenses, worked in the prison's extensive farm and dairy operations.\n\nFederal Correctional Institution, Danbury: The Federal Correctional Institution, Danbury (FCI Danbury) is a low-security United States federal prison for male inmates in Danbury, Connecticut.  It is operated by the Federal Bureau of Prisons, a division of the United States Department of Justice.  The facility also has an adjacent satellite prison camp that houses minimum-security female offenders.  It was announced in the summer of 2013 that FCI Danbury would transition from housing women to housing men with the female inmates transferring out between August and December 2013 and the male inmates arriving in early 2014.  The satellite camp will continue to house female offenders.\n\nFederal Correctional Institution, Berlin: The Federal Correctional Institution, Berlin (FCI Berlin) is a medium-security United States federal prison for male inmates in New Hampshire.  It is operated by the Federal Bureau of Prisons, a division of the United States Department of Justice.  The facility also has an adjacent satellite prison camp housing minimum-security male inmates.\n\nFederal Medical Center, Devens: The Federal Medical Center, Devens (FMC Devens) is a United States federal prison in Massachusetts for male inmates requiring specialized or long-term medical or mental health care.  It is designated as an administrative facility, which means it has inmates from different security classifications, from white-collar criminals to mobsters and sex offenders.  It is operated by the Federal Bureau of Prisons, a division of the United States Department of Justice.  FMC Devens also has a satellite camp housing minimum-security male inmates.\n\nFederal Correctional Institution, Terre Haute: The Federal Correctional Institution, Terre Haute (FCI Terre Haute) is a medium-security United States federal prison for male inmates in Indiana.  It is part of the Terre Haute Federal Correctional Complex (FCC Terre Haute) and is operated by the Federal Bureau of Prisons, a division of the United States Department of Justice.  The facility also has an adjacent satellite prison camp for minimum-security male offenders.\n\nUnited States Penitentiary, Atlanta: The United States Penitentiary, Atlanta (USP Atlanta) is a medium-security United States federal prison for male inmates in Atlanta, Georgia.  It is operated by the Federal Bureau of Prisons, a division of the United States Department of Justice.  The facility also has a detention center for pretrial and holdover inmates, and a satellite prison camp for minimum-security male inmates.\n\nStewart Nozette: Stewart David Nozette (born May 20, 1957) is an American planetary scientist, technologist, and consultant who worked for the United States Department of Energy, the United States Department of Defense, DARPA, the United States Naval Research Laboratory, and NASA.  He is also a convicted felon for attempted espionage and fraud against the United States.  The FBI arrested him October 19, 2009, charging him with attempted espionage after a sting operation which Nozette's lawyer claims amounted to entrapment.  At trial, Nozette admitted attempting to sell U.S. classified information to someone he believed was an Israeli Mossad operative, but was in reality an undercover Federal Bureau of Investigation employee.  He pleaded guilty to one charge of attempted espionage and was sentenced, under the terms of a plea bargain, to thirteen years in prison and is now serving time at the Federal Correctional Institution, Terre Haute.  The FBI found no evidence that any classified materials were actually released to anyone outside the US Government.\n\nFederal Medical Center, Butner: The Federal Medical Center, Butner (FMC Butner) is a United States federal prison in North Carolina for male inmates of all security levels who have special health needs.  It is part of the Butner Federal Correctional Complex and is operated by the Federal Bureau of Prisons, a division of the United States Department of Justice.  An adjacent satellite prison camp houses minimum-security male inmates.\n\nQuestion: Stewart Nozette is serving time at what prison for male inmates in Indiana?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"prisoner_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the prisoner.\"\n    },\n    \"prison_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"prison_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the prison where the individual is incarcerated.\"\n        },\n        \"location_state\": {\n          \"type\": \"string\",\n          \"description\": \"The state where the prison is located.\"\n        },\n        \"inmate_gender_housed\": {\n          \"type\": \"string\",\n          \"description\": \"The gender of inmates primarily housed at this facility.\"\n        }\n      },\n      \"required\": [\n        \"prison_name\",\n        \"location_state\",\n        \"inmate_gender_housed\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"offense_committed\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"The crimes the prisoner was convicted of.\"\n    }\n  },\n  \"required\": [\n    \"prisoner_name\",\n    \"prison_details\",\n    \"offense_committed\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "prisoner_name": {
        "type": "string",
        "description": "The name of the prisoner."
      },
      "prison_details": {
        "type": "object",
        "properties": {
          "prison_name": {
            "type": "string",
            "description": "The name of the prison where the individual is incarcerated."
          },
          "location_state": {
            "type": "string",
            "description": "The state where the prison is located."
          },
          "inmate_gender_housed": {
            "type": "string",
            "description": "The gender of inmates primarily housed at this facility."
          }
        },
        "required": [
          "prison_name",
          "location_state",
          "inmate_gender_housed"
        ],
        "additionalProperties": false
      },
      "offense_committed": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "The crimes the prisoner was convicted of."
      }
    },
    "required": [
      "prisoner_name",
      "prison_details",
      "offense_committed"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
