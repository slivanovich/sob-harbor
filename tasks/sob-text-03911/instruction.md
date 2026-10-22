Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Robert C. Pittman: Robert C. Pittman (April 25, 1922 – October 27, 1996) was a US Army Air Forces pilot, electrical engineer, and entrepreneur.  He was awarded the Distinguished Flying Cross for his heroic actions during World War II, flying more than 250 combat missions over the Pacific Ocean.

Guadalcanal Campaign: The Guadalcanal Campaign, also known as the Battle of Guadalcanal and codenamed Operation Watchtower was a military campaign fought between 7 August 1942 and 9 February 1943 on and around the island of Guadalcanal in the Pacific theater of World War II.  It was the first major offensive by Allied forces against the Empire of Japan.

USS Dale W. Peterson (DE-337): USS "Dale W. Peterson" (DE–337) was an "Edsall" class destroyer escort, the first United States Navy ship so named.  This ship was named for Ensign Dale William Peterson (18 November 1919 – 8 May 1942), who was awarded the Navy Cross for distinguished service in intercepting enemy bombers attacking his carrier 20 February 1942, and was posthumously awarded the Distinguished Flying Cross for his actions during the Battle of the Coral Sea.

Henry Williams Hise: Henry Williams Hise (July 7, 1920 – October 15, 2010) was a United States Marine Corps Brigadier General.  Hise served in World War II, Korea and Vietnam as a Marine Corps aviator, completing five combat tours.  He was awarded the Distinguished Flying Cross for his actions during the Guadalcanal Campaign in World War II.

Robert Boyd Brazier: Robert Boyd Brazier (June 13, 1916 – June 4, 1942) was an Aviation Radioman in the United States Navy.  He was posthumously awarded the Distinguished Flying Cross for his actions in the Battle of Midway, in which he was mortally wounded.

Distinguished Flying Cross National Memorial Act: The Distinguished Flying Cross National Memorial Act ( ; Pub.L.  113–132 ) is a U.S. public law that designates a memorial located at March Field Air Museum in Riverside, California, as the Distinguished Flying Cross National Memorial, in honor of current and former members of the Armed Forces who have been awarded the Distinguished Flying Cross.  The bill was introduced into the United States House of Representatives during the 113th United States Congress.

Joseph C. McConnell: Joseph Christopher McConnell, Jr. (30 January 1922 – 25 August 1954) was a United States Air Force fighter pilot who was the top American flying ace during the Korean War.  A native of Dover, New Hampshire, Captain McConnell was credited with shooting down 16 MiG-15s while flying North American F-86 Sabres.  He was awarded the Distinguished Service Cross, Silver Star, and the Distinguished Flying Cross for his actions in aerial combat.  McConnell was the first American triple jet-on-jet fighter ace and is still the top-scoring American jet ace.

Don T. Griswold: Ensign Don T. Griswold, Jr., (8 July 1917 – 6 June 1942) was a United States Naval Aviator, who was posthumously awarded the Distinguished Flying Cross for his actions during the Battle of Midway.

Robert Rosenthal (USAAF officer): Lieutenant Colonel Robert "Rosie" Rosenthal (June 11, 1917 – April 20, 2007) was a highly decorated pilot in the Eighth Air Force of the United States Army Air Forces in World War II, receiving sixteen awards including the Distinguished Service Cross for "extraordinary heroism in connection with military operations against the enemy," the Silver Star (with cluster) for "gallantry in action," the Distinguished Flying Cross (with cluster) for "heroism or extraordinary achievement during aerial flight," the Air Medal (with seven clusters) and the Purple Heart (with cluster), as well as the Distinguished Flying Cross from Great Britain and the Croix de Guerre from France.  Intelligence Officer Marvin Bowman is quoted describing Rosenthal as "one of the great figures of the Air Force; a shy, modest, and patriotic gentleman of truly amazing courage and achievement."

Peter Isaacson: Peter Stuart Isaacson, AM, DFC, AFC, DFM (31 July 1920 – 7 April 2017) was an Australian publisher and decorated military pilot.  He was the owner of Peter Isaacson Publications, publisher of various trade journals and suburban newspapers including the "Southern Cross" and the "Sunday Observer" in Melbourne.  During World War II, he served in the Royal Australian Air Force (RAAF) as a pilot with RAF Bomber Command and was awarded the Distinguished Flying Cross, the Air Force Cross and the Distinguished Flying Medal.

Question: What was the codename of the battle in which Henry Williams Hise won a Distinguished Flying Cross for his actions?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person who received the award."
    },
    "award_name": {
      "type": "string",
      "description": "The name of the award received."
    },
    "campaign_details": {
      "type": "object",
      "properties": {
        "campaign_name": {
          "type": "string",
          "description": "The name of the military campaign or battle."
        },
        "campaign_codename": {
          "type": "string",
          "description": "The codename associated with the military campaign."
        }
      },
      "required": [
        "campaign_name",
        "campaign_codename"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_name",
    "award_name",
    "campaign_details"
  ],
  "additionalProperties": false
}
