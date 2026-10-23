{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nList of organisms named after famous people: In biological nomenclature, organisms often receive scientific names that honor a person.  A taxon (e.g. species or genus; plural: taxa) named in honor of another entity is an eponymous taxon, and names specifically honoring a person or persons are known as patronyms.  Scientific names are generally formally published in peer-reviewed journal articles or larger monographs along with descriptions of the named taxa and ways to distinguish them from other taxa.  Following rules of Latin grammar, species or subspecies names derived from a man's name often end in \"-i\" or \"-ii\" if named for an individual, and \"-orum\" if named for a group of men or mixed-sex group, such as a family.  Similarly, those named for a woman often end in \"-ae\", or \"-arum\" for two or more women.\n\nUSS Neuendorf (DE-200): USS \"Neuendorf\" (DE-200), a \"Buckley\"-class destroyer escort of the United States Navy, was named in honor of Seaman First Class William Frederick Neuendorf (1916–1941), who was killed in action aboard the USS Nevada, as gun captain of No. 6 A.A. gun, gave an example of leadership, skill, and bravery that is remarked upon by all who observed it during the Japanese attack on Pearl Harbor on 7 December 1941.  He was commended posthumously \"for distinguished devotion to duty and extraordinary courage and disregard for his own safety[,]\" and was the most junior sailor mentioned specifically for distinguished conduct in the after action report of the USS Nevada regarding the attack on Pearl Harbor.\n\nRobert M. Brown: Robert M. Brown was the Chief Engineer for Union Pacific Railroad in the 1960s and 1970s.  For his work with the railroad, Modern Railways magazine selected Brown to receive the magazine's Man of the Year award in 1978; the award has since been continued by Railway Age magazine as the Railroader of the Year.  He was the first railway Chief Engineer to receive this honor that was previously awarded only to top-level executives.  Brown was also involved in the hiring process at Union Pacific for Bill Wimmer, the 2007 recipient of the Railroader of the Year award, and coincidentally, only the second Chief Engineer to be chosen for the honor.\n\nUSS Douglas H. Fox: USS \"Douglas H. Fox\" (DD-779) an \"Allen M. Sumner\"-class destroyer , was named in honor of Lieutenant Commander Douglas H. Fox, the commanding officer of the destroyer USS \"Barton\" , who went down with his ship when she was torpedoed and sunk in the naval battle of Guadalcanal on 13 November 1942.  Fox was posthumously awarded the Navy Cross for his contribution to the defeat of a superior enemy force in this battle, and was later awarded a Gold Star in lieu of a second Navy Cross for earlier actions on 26 and 30 October and 3 November, when he rescued survivors of the aircraft carrier USS \"Hornet\" under hazardous conditions.\n\nGolden Globe Cecil B. DeMille Award: The Cecil B. DeMille Award is an honorary Golden Globe Award bestowed by the Hollywood Foreign Press Association for \"outstanding contributions to the world of entertainment\".  It was first presented on February 21, 1952 at the 9th Annual Golden Globe Awards ceremony and is named in honor of its first recipient, director Cecil B. DeMille.  Honorees are selected by the HFPA board of directors and are presented annually (except for 1976 and 2008).  The first woman to receive the honor was Judy Garland in 1962 who, at 39 years of age, was also the youngest honoree ever to receive the award, while Samuel Goldwyn, at the age of 93, in 1973, was the oldest.  The first African-American to receive the honor was Sidney Poitier in 1982.\n\nUSS Marvin Shields (FF-1066): USS \"Marvin Shields\" (FF-1066) was a \"Knox\"-class frigate of the US Navy.  The ship was named after the only Seabee to receive the Medal of Honor.  CM3 Marvin Glenn Shields was awarded the Medal of Honor during the Vietnam War.\n\nUSS Canberra: USS \"Canberra\" (CA-70/CAG-2) was a \"Baltimore\"-class cruiser and later a \"Boston\"-class guided missile cruiser of the United States Navy.  Originally to be named USS \"Pittsburgh\", the ship was renamed before launch to honor the loss of the Australian cruiser HMAS \"Canberra\" during the Battle of Savo Island.  USS \"Canberra\" is the only USN warship named for a foreign warship or a foreign capital city.\n\nUSS John Basilone: USS \"John Basilone\" (DDG-122) is a planned United States Navy \"Arleigh Burke\"-class Flight IIA guided missile destroyer, the 72nd overall for the class.  The ship will be named for United States Marine Corps Gunnery sergeant John Basilone, who received the nation's highest military award for valor, the Medal of Honor, for heroism during the Guadalcanal Campaign in World War II.  Basilone was the only enlisted Marine to receive both the Medal of Honor and the Navy Cross in World War II.\n\nJames L. Kauffman: James Laurence Kauffman (18 April 188721 October 1963) was a United States Navy Vice Admiral and recipient of the Navy Cross.  He and his son Rear Admiral Draper Laurence Kauffman were the namesakes of  .\n\nUSS Kauffman (FFG-59): USS \"Kauffman\" (FFG-59), an \"Oliver Hazard Perry\"-class guided missile frigate, was a ship of the United States Navy named for Vice Admiral James L. Kauffman (1887–1963) and his son, Rear Admiral Draper L. Kauffman (1911–1979), both experts in sub-surface naval missions.\n\nQuestion: What honor did the man for whom the USS \"Kauffman\" was named after receive?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"ship_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the ship.\"\n    },\n    \"namesakes\": {\n      \"type\": \"array\",\n      \"description\": \"A list of individuals after whom the ship was named.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"person_name\": {\n            \"type\": \"string\",\n            \"description\": \"The full name of the person.\"\n          },\n          \"rank\": {\n            \"type\": \"string\",\n            \"description\": \"The military rank of the person.\"\n          },\n          \"honor_received\": {\n            \"type\": \"string\",\n            \"description\": \"The specific honor or award received by this person.\"\n          }\n        },\n        \"required\": [\n          \"person_name\",\n          \"rank\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"primary_honor_for_question\": {\n      \"type\": \"string\",\n      \"description\": \"The specific honor that answers the question about 'the man' for whom the ship was named.\"\n    }\n  },\n  \"required\": [\n    \"ship_name\",\n    \"namesakes\",\n    \"primary_honor_for_question\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "ship_name": {
        "type": "string",
        "description": "The name of the ship."
      },
      "namesakes": {
        "type": "array",
        "description": "A list of individuals after whom the ship was named.",
        "items": {
          "type": "object",
          "properties": {
            "person_name": {
              "type": "string",
              "description": "The full name of the person."
            },
            "rank": {
              "type": "string",
              "description": "The military rank of the person."
            },
            "honor_received": {
              "type": "string",
              "description": "The specific honor or award received by this person."
            }
          },
          "required": [
            "person_name",
            "rank"
          ],
          "additionalProperties": false
        }
      },
      "primary_honor_for_question": {
        "type": "string",
        "description": "The specific honor that answers the question about 'the man' for whom the ship was named."
      }
    },
    "required": [
      "ship_name",
      "namesakes",
      "primary_honor_for_question"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
