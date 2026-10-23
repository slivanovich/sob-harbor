{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nC. Everett Koop: Charles Everett Koop, MD (October 14, 1916 – February 25, 2013) was an American pediatric surgeon and public health administrator.  He was a vice admiral in the Public Health Service Commissioned Corps, and served as the 13th Surgeon General of the United States under President Ronald Reagan from 1982 to 1989.  According to the Associated Press, \"Koop was the only surgeon general to become a household name.\"\n\nCoal Creek War: The Coal Creek War was an early 1890s armed labor uprising in the southeastern United States that took place primarily in Anderson County, Tennessee.  This labor conflict ignited during 1891 when coal mine owners in the Coal Creek watershed began to remove and replace their company-employed, private coal miners then on the payroll with convict laborers leased out by the Tennessee state prison system.\n\nCoal Wars: The Coal Wars, or the Coal Mine Wars, were a series of armed labor conflicts in the United States, roughly between 1890 and 1930.  Although they occurred mainly in the East, particularly in Appalachia, there was a significant amount of violence in Colorado after the turn of the century.\n\nWar Lords: The War Lords were a Black militant youth organization in East St. Louis, Illinois in the 1960's.  Founded in January 1965 as The Royal Serpents, the organization's name changed to Imperial War Lords within its first month of existence.  The organization sponsored teenage dances, and frequented the First United Lutheran Church, whose pastors Sonny Goldenstein and later Keith Davis ministered to them.  The group was led by Charles \"Sweed\" Jeffries, who was active in the East St. Louis school boycotts in the spring of 1968.  He was closely associated with Charles Koen, and often arrested.  The War Lords played an active role in Project IMPACT (innovative Methods of Positive Action for Community Tranquility), a federally funded arts and recreation program in East St. Louis which sponsored summer music concerts.  In 1968, the War Lords were involved in the formation of Youth Organizations United, a national coalition of street gangs, which included the Black Knights from Memphis, the Black Egyptians from East St. Louis, the Vice Lords from Chicago, the Thugs United from New Orleans and many others.  At sometime in 1969, the War Lords joined with the Black Egyptians and possibly Black Culture Inc. as well to form the United Front of East St. Louis.  There are few references to the War Lords after that, although in one late press release, Charles Jeffries stated that membership had been opened to whites.  The War Lord's transition to mixed race membership lead to other endeavors and the formation of Warlords MC(Motorcycle Club), the nation's first interracial 3 piece patch MC.\n\nMoody Sarno: Amerino J. \"Moody\" Sarno (September 21, 1914 – November 9, 1997) was an American football player and coach.  An All-American at Fordham University, he played on the same offensive line as future Pro Football Hall of Famer Vince Lombardi.  On March 30, 1941, he was hired as Boston College's line coach.  He became the Eagles head coach in 1943 after head coach Denny Myers joined the United States Navy.  Sarno himself was the only member of the Boston College coaching staff not to join the United States Armed Forces.  In three seasons as head coach at Boston College, he had an 11–7–1 record, including an unbeaten 1943 season.  He later served as head coach at his former school, Everett High School in Everett, Massachusetts, from 1955 to 1982.  In 28 seasons at Everett, he finished with a 128–116–11 record and won four state championships (1961, 1962, 1964, 1965).\n\nMisr Spinning and Weaving Company: The Misr Spinning and Weaving Company (Arabic: شركة مصر للغزل والنسيج‎ ‎ ), also known as Misr Helwan or the El-Ghazl factory, is a large, publicly owned textile company located in El-Mahalla El-Kubra within the Nile Delta of Egypt, approximately 80 kilometers north of Cairo.  The company's current board chairman is Mohamed Moheb Salah Elden.  Egypt's largest industrial facility, Misr Helwan employs over 25,000 workers, many of whom have played an active role in Egyptian labor struggles.  Large protests and strikes at Misr Helwan since 2006 contributed to the collapse of the Mubarak government, the 2011 Egyptian revolution, and the Arab Spring more generally.\n\nLebanese Armed Revolutionary Factions: The Lebanese Armed Revolutionary Factions – LARF (Arabic: الفصائل المسلحة الثورية اللبنانية | \"Al Fasael al-Musallaha al-Thawriyya al-Lubnaniyya\") or Fractions armées révolutionnaires libanaises (FARL) in French, was a small Marxist-Leninist guerrilla group which played an active role in the Lebanese civil war.\n\nShannon Lively: Shannon James Lively (born May 4, 1992 in Attadale, Western Australia) is an Australian actor.  His first television role was Declan in the second series of \"The Sleepover Club\".  He graduated in the class of 2009 from Corpus Christi College, Bateman and within that time he also finished working on the Australian television series entitled \"Wormwood\".  In 2010, Shannon Lively played Chub Pickles on the Australian miniseries; Cloudstreet, based on the popular novels by Tim Winton and aired in 2011.\n\nCharles Everett Lively: Charles Everett Lively (1887–1962) was a private detective affiliated with the Baldwin-Felts Detective Agency.  He played an active role in the Coal Wars in Appalachia, and is chiefly remembered as one of the assassins of Police Chief Sid Hatfield.\n\nSturla Sighvatsson: Sturla Sighvatsson (1199 – 21 August 1238) was an Icelandic chieftain or \"goði\" of the Sturlungar family clan who played an active role in the armed conflicts in Iceland during the Age of the Sturlungs (Icelandic: \"Sturlungaöld\").\n\nQuestion: Charles Everett Lively played an active role in what series of armed labor conflicts in the United States, roughly between 1890 and 1930?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"conflict_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the armed labor conflict.\"\n    },\n    \"involved_person\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person who played an active role in the conflict.\"\n    },\n    \"conflict_type\": {\n      \"type\": \"string\",\n      \"description\": \"A description of the type of conflict.\"\n    },\n    \"time_period\": {\n      \"type\": \"string\",\n      \"description\": \"The approximate time period during which the conflict occurred.\"\n    },\n    \"primary_location\": {\n      \"type\": \"string\",\n      \"description\": \"The main geographical area where the conflict took place.\"\n    }\n  },\n  \"required\": [\n    \"conflict_name\",\n    \"involved_person\",\n    \"conflict_type\",\n    \"time_period\",\n    \"primary_location\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "conflict_name": {
        "type": "string",
        "description": "The name of the armed labor conflict."
      },
      "involved_person": {
        "type": "string",
        "description": "The name of the person who played an active role in the conflict."
      },
      "conflict_type": {
        "type": "string",
        "description": "A description of the type of conflict."
      },
      "time_period": {
        "type": "string",
        "description": "The approximate time period during which the conflict occurred."
      },
      "primary_location": {
        "type": "string",
        "description": "The main geographical area where the conflict took place."
      }
    },
    "required": [
      "conflict_name",
      "involved_person",
      "conflict_type",
      "time_period",
      "primary_location"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
