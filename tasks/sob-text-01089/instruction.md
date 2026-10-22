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
9th Indian Infantry Brigade: The 9th Indian Infantry Brigade was an infantry brigade formation of the Indian Army during World War II.  Before the war the 9th (Jhansi) Infantry Brigade was a peacetime formation in Meerut district.  This brigade was redesignated the 5th Indian Infantry Brigade and a new 9th Brigade was then formed all in September 1939.  The new brigade was assigned to the 5th Indian Infantry Division in June 1940 to January 1944.  It then spent February attached to the 7th Indian Infantry Division before returning to the 5th Division.  The brigade spent two other short periods away from the 5th Division it was attached to the 17th Indian Infantry Division between March and April 1945 and was with the 19th Indian Infantry Division in April 1945, and returned to the 5th for the rest of the war.

Geoffrey Serle: Alan Geoffrey Serle (10 March 1922 – 27 April 1998), known as Geoff, was an Australian historian, who is best known for his books on the colony of Victoria; "The Golden Age" (1963) and "The Rush to be Rich" (1971) and his biographies of John Monash, John Curtin and Robin Boyd.

128th Infantry Brigade (United Kingdom): The 128th Infantry Brigade was an infantry brigade of the British Army.  The brigade, known as the Hampshire Brigade, served in British India during World War I but not as a complete formation.  During World War II the 128th Infantry Brigade fought in the final stages of the North African Campaign in late in Tunisia and the Italian Campaign, and later in the Greek Civil War.  Throughout its existence the brigade was composed almost entirely of battalions of the Hampshire Regiment (later Royal Hampshire Regiment).

John Monash: General Sir John Monash, ( ; 27 June 1865 – 8 October 1931) was a civil engineer and an Australian military commander of the First World War.  He commanded the 13th Infantry Brigade before the war and then, shortly after its outbreak, became commander of the 4th Brigade in Egypt, with whom he took part in the Gallipoli campaign.  In July 1916 he took charge of the newly raised 3rd Division in northwestern France and in May 1918 became commander of the Australian Corps, at the time the largest corps on the Western Front.  The successful Allied attack at the Battle of Amiens on 8 August 1918, which expedited the end of the war, was planned by Monash and spearheaded by British forces including the Australian and Canadian Corps under Monash and Arthur Currie.  Monash is considered one of the best Allied generals of the First World War and the most famous commander in Australian history.

48th Indian Infantry Brigade: The 48th Infantry Brigade, was raised as the 48 Indian Infantry Brigade, in October 1941, at Secunderabad, India.  After an initial tenure with 19th Indian Infantry Division, it was transferred to the 17th Indian Infantry Division.  In World War II it participated in the Burma campaign and in April 1942 was attached to 1st Burma Division.  After the war the brigade returned to India as an independent brigade, and was located at Dhond in August 1947.  After India gained Independence in 1947, 48 Indian Infantry Brigade was re-designated as 48 Infantry Brigade.  Since then 48 infantry brigade has seen action Goa in 1961, as part of 17 Infantry Division; in the 1962 War in Kameng Frontier Division, Arunachal Pradesh, as part of 4th Infantry Division; and in the 1971 war, as part of 7th Infantry Division.  Since the 1970s, 48 Infantry Brigade has been located in Ferozpur, Punjab, as part of 7 Infantry Division.

87th Battalion (Canadian Grenadier Guards), CEF: The 87th (Canadian Grenadier Guards) Battalion, CEF was a unit in the Canadian Expeditionary Force during the First World War.  Based in Montreal, Quebec, the unit began recruiting in September 1915 in Montreal, the surrounding districts, and also in mining districts elsewhere in the province.  After sailing to England in April 1916, the battalion was stationed there as part of the 12th Infantry Brigade (until June) and then 11th Infantry Brigade of the 4th Canadian Infantry Division until August of the same year.  On August 11/12, the battalion crossed over to France and served the duration of the war as part of the 11th Infantry Brigade, 4th Canadian Infantry Division.  The battalion returned to Canada in June 1919.

191st Infantry Brigade (United States): The 191st Infantry Brigade was constituted on 24 June 1921 in the Organized Reserves as Headquarters and Headquarters Company, 191st Infantry Brigade, and assigned to the 96th Division.  It was organized in December 1921 at Portland, Oregon, and redesignated on 23 March 1925 as Headquarters and Headquarters Company, 191st Brigade, then redesignated on 24 August 1936 as Headquarters and Headquarters Company, 191st Infantry Brigade.  It was converted and redesignated on 6 April 1942 as the 96th Reconnaissance Troop (less 3d Platoon), 96th Division (Headquarters and Headquarters Company, 192d Infantry Brigade, concurrently converted and redesignated as the 3d Platoon, 96th Reconnaissance Troop, 96th Division).  The Troop was ordered into active military service on 15 August 1942 and reorganized at Camp Adair, Oregon, as the 96th Cavalry Reconnaissance Troop, an element of the 96th Infantry Division.  It was reorganized and redesignated on 16 August 1943 as the 96th Reconnaissance Troop, Mechanized, and then again reorganized and redesignated on 20 November 1945 as the 96th Mechanized Cavalry Reconnaissance Troop.  Following World War II service with the 96th Infantry Division in the Pacific, it was inactivated on 3 February 1946 at Camp Anza, California.

15th Infantry Brigade (United Kingdom): The 15th Infantry Brigade, later 15 (North East) Brigade, was an infantry brigade of the British Army.  It was part of the regular 5th Infantry Division during the First World War and Second World War, and was subsequently part of the 2nd Infantry Division in the north of the United Kingdom, with specific responsibility for the areas of North East England and Yorkshire and the Humber.

69th Infantry Brigade (United Kingdom): The 69th Infantry Brigade was an infantry brigade formation of the British Army in World War II.  It was a 2nd Line Territorial Army unit and during the Battle of France served with the 23rd (Northumbrian) Division a division which suffered such heavy losses that it was disbanded.  The brigade was included in the "order of battle" of the 50th (Northumbrian) Infantry Division, together with the 150th Infantry Brigade and the 151st Infantry Brigade and became part of XII Corps, British home forces.

199th (Manchester) Brigade: The 199th (2/1st Manchester) Brigade was an infantry brigade formation of the British Army that saw active service during the Great War as part of 66th (2nd East Lancashire) Division and was reformed as 199th Infantry Brigade in World War II, serving with 55th (West Lancashire) Infantry Division until August 1944 when it was redesignated 166th Infantry Brigade.

Question: What was the birth date of the Australian historian who wrote a biography of the commander of the 13th infantry brigade before the First World War?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "historian_name": {
      "type": "string",
      "description": "The name of the Australian historian."
    },
    "historian_birth_date": {
      "type": "string",
      "description": "The birth date of the historian."
    },
    "biographed_person": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person whose biography was written."
        },
        "role": {
          "type": "string",
          "description": "The role or title of the biographed person."
        },
        "military_unit_commanded": {
          "type": "string",
          "description": "The military unit commanded by the biographed person."
        },
        "command_period": {
          "type": "string",
          "description": "The period during which the military unit was commanded."
        }
      },
      "required": [
        "name",
        "role",
        "military_unit_commanded",
        "command_period"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "historian_name",
    "historian_birth_date",
    "biographed_person"
  ],
  "additionalProperties": false
}
