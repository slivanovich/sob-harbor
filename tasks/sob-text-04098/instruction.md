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
William &quot;Bull&quot; Nelson: William "Bull" Nelson (September 27, 1824 – September 29, 1862) was a United States naval officer who became a Union general in the Civil War.

Fairfax Moresby: Admiral of the Fleet Sir Fairfax Moresby GCB (1786 – 21 January 1877) was a Royal Navy officer.  As a junior officer he took part in the unsuccessful expedition to capture Ferrol in Spain during the French Revolutionary Wars.  He later saw action during the blockade of Brest during the Napoleonic Wars before becoming commanding officer of a sloop which was sent to the Aegean Sea to defend the population of Malta from pirates; the grateful people presented him with a sword.  He then sailed to the Adriatic Sea where he led a naval brigade providing artillery support to the Austrian forces during the siege of Trieste.  He went on to be senior naval officer at the Cape of Good Hope and then senior officer at Mauritius, with orders to suppress the slave trade: he concluded the Moresby Treaty with Seyyid Said, the imam of Muscat restricting the scope of local slave trading and conferring on English warships the right of searching and seizing local vessels.

George Rooke: Admiral of the Fleet Sir George Rooke (1650 – 24 January 1709) was an English naval officer.  As a junior officer he saw action at the Battle of Solebay and again at the Battle of Schooneveld during the Third Anglo-Dutch War.  As a captain, he conveyed Prince William of Orange to England and took part in the Battle of Bantry Bay during the Williamite War in Ireland.

Richard Howe, 1st Earl Howe: Admiral of the Fleet Richard Howe, 1st Earl Howe, {'1': ", '2': ", '3': ", '4': "} (8 March 1726 – 5 August 1799) was a British naval officer.  After serving throughout the War of the Austrian Succession, he gained a reputation for his role in amphibious operations against the French coast as part of Britain's policy of naval descents during the Seven Years' War.  He also took part, as a naval captain, in the decisive British naval victory at the Battle of Quiberon Bay in November 1759.

Blue Grass Chemical Agent-Destruction Pilot Plant: The Blue Grass Chemical Agent-Destruction Pilot Plant (BGCAPP) is a chemical weapons destruction facility undergoing systemization, or testing.  The plant will destroy the chemical weapons stockpile at the Blue Grass Army Depot (BGAD), near Richmond, Kentucky.  The plant is dedicated to the destruction of 523 ST of nerve agents sarin (GB) and VX, and mustard agent, which constitute about two percent of the United States chemical weapons stockpile.

Battle of Richmond: The Battle of Richmond, Kentucky, fought August 29–30, 1862, was a stunning Confederate victory by Major General Edmund Kirby Smith against Union major general, William "Bull" Nelson's forces, defending the town.  It was the first major battle in the Kentucky Campaign.  The battle took place on and around what is now the grounds of the Blue Grass Army Depot, outside Richmond, Kentucky.

Blue Grass Army Depot: Blue Grass Army Depot (BGAD) is a U.S. Army storage facility for conventional munitions and chemical weapons.  The facility is located in east central Kentucky, southeast of the cities of Lexington and Richmond, Kentucky.  The 14494 acre site, composed mainly of open fields and wooded areas, is used for munitions storage, repair of general supplies, and the disposal of munitions.  The installation is used for the storage of conventional explosive munitions as well as assembled chemical weapons.  The depot primarily is involved in industrial and related activities associated with the storage and maintenance of conventional and chemical munitions.

Savanna Army Depot: Savanna Army Depot was a 13062 acre installation, located on the eastern bank of the Mississippi River, in Carroll and Jo Daviess counties, around 7 mi north of Savanna, Illinois.  It was opened in 1917 as a proving and testing facility for weapons developed at Rock Island Arsenal.  In 1921 it became a weapons depot.  The U.S. Environmental Protection Agency (EPA) listed the depot as a Superfund site in 1989.  The depot was selected for closure through the Base Realignment and Closure process in July 1995 and was officially closed on March 18, 2000.  The Jo-Carroll Local Redevelopment Authority (LRA) was established to redevelop a portion of the property for commercial and business usage referred to as the Savanna Depot Park.  On September 26, 2003, the United States Department of Defense agreed to transfer 9404 acre of land to become the Lost Mound Unit of the Upper Mississippi River National Wildlife and Fish Refuge.  3022 acre were initially transferred with the rest to be transferred following environmental cleanup.  The portion near Lock and Dam No. 12 was transferred to the United States Army Corps of Engineers and a small part to the Illinois Department of Natural Resources.

Lexington Army Depot: Lexington Army Depot is a former United States Army facility located in Avon, Kentucky.  In 1964, it was paired with Blue Grass Army Depot to form Lexington-Blue Grass Army Depot.  In 1999, the facility was closed after the recommendation of the 1988 Base Realignment and Closure Commission.

Red River Army Depot: The Red River Army Depot (RRAD) is an 15835 acre facility located 18 mi west of Texarkana, Texas, in Bowie County.  The facility has over 3000000 sqft of storage capacity.  RRAD was activated in 1941 to create an ammunition storage facility.  The depot was supposed to be deactivated after the findings of the 1995 Base Realignment and Closure Commission.  However, the depot remained open after the commission changed its mind.  The depot was once again slated for closure upon recommendation from the 2005 BRAC commission, but has remained open to provide maintenance support for the army.  The depot's primary mission is the maintenance and repair of all tactical wheeled vehicles, which includes repairing MRAPs and HUMVEEs. Letterkenny Army Depot took over some of RRAD's missile systems.

Question: What naval officer took part in the battle, on what is now the grounds of the Blue Grass Army Depot?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "naval_officer_name": {
      "type": "string",
      "description": "The name of the naval officer."
    },
    "officer_role_in_battle": {
      "type": "string",
      "description": "The rank or role of the officer during the specified battle."
    },
    "battle_details": {
      "type": "object",
      "properties": {
        "battle_name": {
          "type": "string",
          "description": "The name of the battle."
        },
        "battle_date": {
          "type": "string",
          "description": "The date range of the battle."
        },
        "location_description": {
          "type": "string",
          "description": "Description of the battle location in relation to the army depot."
        }
      },
      "required": [
        "battle_name",
        "battle_date",
        "location_description"
      ],
      "additionalProperties": false
    },
    "depot_name": {
      "type": "string",
      "description": "The name of the army depot related to the battle location."
    }
  },
  "required": [
    "naval_officer_name",
    "officer_role_in_battle",
    "battle_details",
    "depot_name"
  ],
  "additionalProperties": false
}
