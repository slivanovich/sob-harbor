{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCamp Hero State Park: Camp Hero State Park is a 754 acre state park located on Montauk Point, New York.  The park occupies a portion of the former Montauk Air Force Station.\n\nCamp Slayer: Camp Slayer was a US military base in Iraq, an annex of the Victory Base Complex, established early into the 2003 Iraq War.  Located on the southeastern corner of the Baghdad International Airport, it is part of the former Al Radwaniyah Presidential Complex and contains several man-made lakes, a man-made hill (result of the man-made lakes), the Ba'ath Party House, the Victory Over America Palace, Perfume Palace, and dozens of smaller luxury homes for Ba'ath Party notables.\n\nYongsan Family Park: Yongsan Family Park () is a park in Yongsan District, Seoul, South Korea.  It was originally part of the US military base Yongsan Garrison, the headquarters of the US military in South Korea, including the base golf course.  However, the land was returned to civilian use in November 1992 to establish this park.\n\nClark Freeport Zone: Clark Freeport Zone is a redevelopment of the former Clark Air Base, a former United States Air Force base in the Philippines.  It is located on the northwest side of Angeles City and on the west side of Mabalacat City in the province of Pampanga.  It is located northwest of Metro Manila.  The zone is a former US military base and has modern infrastructure facilities, generous fiscal and non-fiscal incentives, professional support services and other amenities.  Today, Clark forms the hub for business, industry, aviation, education, and tourism in the Philippines as well as a leisure, fitness, entertainment and gaming center of Central Luzon.\n\nMike Eden (baseball): Eden has the distinction of being the only major leaguer born in Fort Clayton, a former US military base on the Pacific side of the Panama Canal.  He attended Southern Illinois University, and as member of the SIU Salukis, was selected third baseman to the All-Tournament Team of the 1971 College World Series.\n\nCamp Lemonnier: Camp Lemonnier is a United States Naval Expeditionary Base, situated at Djibouti's Djibouti–Ambouli International Airport and home to the Combined Joint Task Force - Horn of Africa (CJTF-HOA) of the U.S. Africa Command (USAFRICOM).  It is the only permanent US military base in Africa.  The camp is operated by U.S. Navy Region Europe, Africa, Southwest Asia; CJTF-HOA is the most notable tenant command located at the facility as of 2008.  It was established as the primary base in the region for the support of Operation Enduring Freedom - Horn of Africa (OEF-HOA).  After negotiations between March and May 2001, the Djiboutian government allowed for the base's use by the U.S., providing for demining, humanitarian, and counter-terrorism efforts, and it now serves as the location from which U.S. and Coalition forces are operating in the Horn of Africa.  The access agreement made by officials from the U.S. Embassy in Djibouti with the Djiboutian government allows for use of the camp, as well as a nearby airport and port facilities.\n\nCamp Holcomb: Camp Holcomb was a US military base in Chinwangtao (Qinhuangdao) China.  Established in 1912 in response to the Boxer Rebellion, it was garrisoned by the 15th Infantry Regiment, US Army as part of their larger presence in nearby Tientsin (Tianjin).  Chinwangtao is a strategic deep water port near where the Great Wall of China meets the sea.  Called Camp Burrowes by the Army, on February 28, 1938, the base was transferred to the US Marine Corps and renamed Camp Holcomp after the Commandant of the Marine Corps, General Thomas Holcomb The base was surrendered to the Japanese on December 8, 1941.  After World War II, the base was again used by the Marines until 1947, when it was caught up in the Chinese Civil War and evacuated.\n\nMontauk Air Force Station: Montauk Air Force Station was a US military base at Montauk Point on the eastern tip of Long Island, New York.  It was decommissioned in 1981 and is now owned by the New York State Office of Parks, Recreation and Historic Preservation as Camp Hero State Park.\n\nNorth Hero State Park: North Hero State Park is a 399-acre day use state park on Lake Champlain in North Hero, Vermont.  It is a stop on the Lake Champlain Paddlers' Trail.\n\nPalaly Military Base: Palaly Military Base is a military base located in Palaly, Northern Province of Sri Lanka.  The base houses the Security Forces Headquarters - Jaffna and is in close proximity to the naval base; SLNS Uttara at Kankasanturai and air base; SLAF Palaly.  The Sri Lanka Army Medical Corps maintains a base hospital in Palali.Palaly Military Base is the largest military base in Jaffna Peninsula\n\nQuestion: Camp Hero State Park is located on what former US military base?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"park_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the state park.\"\n    },\n    \"park_location\": {\n      \"type\": \"string\",\n      \"description\": \"The location of the state park.\"\n    },\n    \"former_military_base\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the former US military base.\"\n    },\n    \"base_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of the former military base (e.g., Air Force Station).\"\n    },\n    \"base_status\": {\n      \"type\": \"string\",\n      \"description\": \"The status of the former military base (e.g., decommissioned).\"\n    }\n  },\n  \"required\": [\n    \"park_name\",\n    \"park_location\",\n    \"former_military_base\",\n    \"base_type\",\n    \"base_status\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "park_name": {
        "type": "string",
        "description": "The name of the state park."
      },
      "park_location": {
        "type": "string",
        "description": "The location of the state park."
      },
      "former_military_base": {
        "type": "string",
        "description": "The name of the former US military base."
      },
      "base_type": {
        "type": "string",
        "description": "The type of the former military base (e.g., Air Force Station)."
      },
      "base_status": {
        "type": "string",
        "description": "The status of the former military base (e.g., decommissioned)."
      }
    },
    "required": [
      "park_name",
      "park_location",
      "former_military_base",
      "base_type",
      "base_status"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
