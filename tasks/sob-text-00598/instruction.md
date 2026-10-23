{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nFaughanvale GAC: Saint Mary's Faughanvale GAA (Irish: \"CLG Naomh Muire Nuachongbháil\" ) is a Gaelic Athletic Association club based in Greysteel, County Londonderry, Northern Ireland, in the Catholic parish of Faughanvale, nine miles from Derry City.  The club is a member of the Derry GAA and currently cater for Gaelic football, Ladies' Gaelic football.\n\nGreysteel: Greysteel or Gresteel is a village in County Londonderry, Northern Ireland.  It lies 9 mi to the east of Derry and 7 mi to the west of Limavady on the main A2 coast road between Limavady and Derry, overlooking Lough Foyle.  It is designated as a Large Village and in the 2001 Census it had a population of 1,229 people, an increase of almost 20% compared to 1991.  It is situated within Causeway Coast and Glens district.\n\nRainey Endowed School: Rainey Endowed School,known colloquially as \"The Rainey\", is a voluntary grammar school in Magherafelt, County Londonderry, Northern Ireland.  The school was founded in 1707 and has an enrolment of approximately 700 pupils.  The school borders three counties and draws its students from County Londonderry, County Antrim and County Tyrone.  It offers the Northern Ireland curricula up to the age of 16 and a range of AS and A2 courses at post 16.  It is also a member of a local inter-school program which shares its A-level classes with other schools in the area.\n\nHeygate baronets: The Heygate Baronetcy, of Southend in the County of Essex, is a title in the Baronetage of the United Kingdom.  It was created on 30 September 1831 for William Heygate, Lord Mayor of London from 1822 to 1823 and Member of Parliament for Sudbury from 1818 to 1826.  The second Baronet married Marianne Gage in 1851 and so acquired an estate at Bellarena, County Londonderry.  He represented the constituency of County Londonderry in the House of Commons as a Conservative from 1859 to 1874.  The third Baronet was Parliamentary Under-Secretary to the Lord-Lieutenant of Ireland, the Marquess of Londonderry, from 1887 to 1888.\n\nTorrens Knight: Torrens Knight (born 4 August 1969) is a Northern Ireland loyalist, who belonged to the North Antrim and Londonderry Brigade of the Ulster Defence Association (UDA).  In 1993 he took part in the Greysteel massacre (in which eight civilians were shot dead) and the Castlerock killings (in which three civilians and a Provisional Irish Republican Army (IRA) member were killed).  After being convicted—along with three others—for the killings, he served seven years in the Maze Prison before his release in 2000 under the terms of the Belfast Agreement.\n\nFoyle College: Foyle College is a co-educational non-denominational voluntary grammar school in Derry City, County Londonderry, Northern Ireland.  The school's legal name is Foyle and Londonderry College.  In 1976, two local schools, Foyle College and Londonderry High School, merged under the Foyle and Londonderry College Act 1976 to form Foyle and Londonderry College.  In 2011, the Board of Governors re-branded the school as 'Foyle College' and updated the school's crest.  The school is a member of the Independent Schools Council of the United Kingdom and also the Headmasters' and Headmistresses' Conference (HMC).\n\nGreysteel massacre: The Greysteel massacre was a mass shooting that happened on the evening of 30 October 1993 in Greysteel, County Londonderry, Northern Ireland.  Three members of the Ulster Defence Association (UDA), a loyalist paramilitary group, opened fire in a crowded pub during a Halloween party, killing eight civilians and wounding thirteen.  The pub was in an Irish Catholic and Irish nationalist area.  The group claimed responsibility using their cover name \"Ulster Freedom Fighters\" and said that the attack was revenge for the Shankill Road bombing by the Provisional IRA a week earlier.\n\nDerryloran: Derryloran is a civil parish mainly in County Tyrone, Northern Ireland, with some areas in County Londonderry.  It is situated in the historic baronies of Dungannon Upper in County Tyrone and Loughinsholin in County Londonderry.  It is also a townland (also known as Kirkstown) of 174 acres.\n\nWilliam Boyd (minister): William Boyd (died 1772), was an Irish Presbyterian minister.  He is known as the bearer of a petition to Samuel Shute, the governor of Province of Massachusetts Bay, embodying a proposal for an emigration from County Londonderry to that colony.  Boyd fulfilled his mission in 1718; the intended emigration did not take place.  In the same year (without awaiting the issue of Boyd's negotiation), James McGregor (minister of Aghadowey, County Londonderry, from 1701 to 1718), who had not signed the document, emigrated to New Hampshire with some of his people and founded a town to which was given the name of Londonderry.\n\nKilrea: Kilrea (pronounced , from Irish: \"Cill Ria\" , meaning \"church on the hill\" ) is a village, townland and civil parish in County Londonderry, Northern Ireland.  It gets its name from St. Patrick's Church of Ireland, which sits on Church Street looking over the town.  It is near the River Bann, which marks the boundary between County Londonderry and County Antrim.  In the 2011 Census it had a population of 2,724 people.  It is situated within Causeway Coast and Glens district.\n\nQuestion: The Greysteel massacre was the killing of 8 people in a County Londonderry pub in October of which year?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"event_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the event.\"\n    },\n    \"event_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of event that occurred.\"\n    },\n    \"location_county\": {\n      \"type\": \"string\",\n      \"description\": \"The county where the event took place.\"\n    },\n    \"year_of_event\": {\n      \"type\": \"integer\",\n      \"description\": \"The year in which the event occurred.\"\n    },\n    \"fatalities_count\": {\n      \"type\": \"integer\",\n      \"description\": \"The number of people killed in the event.\"\n    }\n  },\n  \"required\": [\n    \"event_name\",\n    \"event_type\",\n    \"location_county\",\n    \"year_of_event\",\n    \"fatalities_count\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "event_name": {
        "type": "string",
        "description": "The name of the event."
      },
      "event_type": {
        "type": "string",
        "description": "The type of event that occurred."
      },
      "location_county": {
        "type": "string",
        "description": "The county where the event took place."
      },
      "year_of_event": {
        "type": "integer",
        "description": "The year in which the event occurred."
      },
      "fatalities_count": {
        "type": "integer",
        "description": "The number of people killed in the event."
      }
    },
    "required": [
      "event_name",
      "event_type",
      "location_county",
      "year_of_event",
      "fatalities_count"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
