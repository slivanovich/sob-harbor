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
Michael Pollock: Admiral of the Fleet Sir Michael Patrick Pollock, {'1': ", '2': ", '3': ", '4': "} (19 October 1916 – 27 September 2006) was a senior officer in the Royal Navy who rose to become First Sea Lord and Chief of the Naval Staff in the early 1970s.  In the Second World War, he was an officer on ships tasked with protecting convoys in the Atlantic and the Mediterranean, and was gunnery officer on the cruiser HMS "Norfolk" when she fought the German battleship "Scharnhorst" during the Battle of North Cape.  He later commanded the aircraft carrier HMS "Ark Royal" , and hosted Ian Smith on HMS "Tiger" .  In retirement, he held the position of King of Arms of the Order of the Bath and Gloucester King of Arms, with responsibility for heraldry in Wales.

SMS Oldenburg (1884): SMS "Oldenburg"  was an armored warship of the German Imperial Navy.  Laid down at the AG Vulcan shipyard in Stettin in 1883, the ship was launched in December 1884 and commissioned into the Navy in April 1886.  "Oldenburg" was intended to have been a fifth member of the "Sachsen" class of sortie corvettes, but budgetary limitations and dissatisfaction with the "Sachsen" class prompted a redesign that bore little resemblance to the earlier vessels.  "Oldenburg" mounted her main battery of eight 24 cm guns amidships, six in a central casemate on the main deck and two directly above them on the broadside.  She was the first German capital ship constructed entirely from German-made steel.

Varyl Begg: Admiral of the Fleet Sir Varyl Cargill Begg {'1': ", '2': ", '3': ", '4': "} (1 October 1908 – 13 July 1995) was a Royal Navy officer.  He fought in the Second World War as gunnery officer in a cruiser taking part in the North Atlantic convoys, the Norwegian campaign and the occupation of Iceland and then as gunnery officer in a battleship operating in the Mediterranean Fleet during the Battle of Cape Matapan.  After that he commanded a destroyer during the Korean War and was Commander-in-Chief of Far East Command during the Indonesia–Malaysia confrontation.  He was First Sea Lord and Chief of the Naval Staff in the late 1960s.  In that role he vehemently opposed plans to introduce large new aircraft carriers and instead managed to persuade the British Government to develop the design for three small "through-deck cruisers".

HMS Resistance (1861): HMS "Resistance" was the second of two "Defence"-class ironclad s built for the Royal Navy in the 1860s.  She was the first capital ship in the Royal Navy to be fitted with a ram and was given the nickname of "Old Rammo".  "Resistance" was initially assigned to the Channel Fleet upon commissioning, but was transferred to the Mediterranean Fleet in 1864, the first ironclad to be assigned to that fleet.  She was rearmed in 1867 and became a guardship when recommissioned in 1869.  The ship was reassigned to the Channel Fleet in 1873 before reverting to her former duties in 1877.  "Resistance" was decommissioned in 1880 and was used for gunnery and torpedo trials beginning in 1885.  The ship was sold for scrap in 1898 and foundered in 1899 en route to the breaker's yard.  She was salvaged and later scrapped.

USS YMS-418: The YMS-418 was a YMS-1 class minesweeper which saw service in World War II.  The hull was laid down 16 September 1943 by Henry C. Grebe and Co., Chicago, IL.  It was launched 22 February 1944 It was struck from the Navy Register 7 February 1947 and sold 17 December 1947.  According to deck logs stored at the National Archives in College Park Maryland, the ship's commanding officer was Lt. Victor A. Lang, executive officer Ensign Toivo John Hamalainen, gunnery officer Ensign J. J. Dennehy, Jr., engineering officer Ensign Bruce F. Kingsbury.  Its fate is unknown.

Arthur Power: Admiral of the Fleet Sir Arthur John Power (12 April 1889 – 28 January 1960) was a Royal Navy officer.  He took part in the First World War as a gunnery officer and saw action in the Dardanelles Campaign.  During the inter-war years he commanded the gunnery school at HMS "Excellent" and then the aircraft carrier HMS "Ark Royal" .  During the Second World War he played a leading role in the planning for the Allied invasion of Sicily and for the Allied invasion of Italy and then commanded the naval forces for the actual landing of V Corps at Taranto in Italy in September 1943.  He went on to be Commander-in-Chief of the East Indies Fleet in the closing stages of the war and conducted naval strikes on the Imperial Japanese Army in Borneo and Malaya.  After the War he became Second Sea Lord and Chief of Naval Personnel, Commander-in-Chief, Mediterranean Fleet and then Commander-in-Chief, Portsmouth.

Peter Hill-Norton: Admiral of the Fleet Peter John Hill-Norton, Baron Hill-Norton, {'1': ", '2': ", '3': ", '4': "} (8 February 1915 – 16 May 2004) was a senior Royal Navy officer.  He fought in the Second World War as gunnery officer in a cruiser operating on the Western Approaches and in the North Sea taking part in the Norwegian Campaign, then in a cruiser taking part in the Arctic convoys and finally in a battleship operating in the Eastern Fleet.  After the War he commanded a destroyer and then an aircraft carrier.  He served as First Sea Lord and Chief of the Naval Staff and then Chief of the Defence Staff in early 1970s.  In the latter role he gave the final commitment to Project Chevaline, the Polaris missile improvement programme.  He went on to be Chairman of the NATO Military Committee.

German battleship Scharnhorst: Scharnhorst was a German capital ship, alternatively described as a battleship and battlecruiser, of Nazi Germany's "Kriegsmarine".  She was the lead ship of her class, which included one other ship, "Gneisenau" .  The ship was built at the "Kriegsmarinewerft" dockyard in Wilhelmshaven; she was laid down on 15 June 1935 and launched a year and four months later on 3 October 1936.  Completed in January 1939, the ship was armed with a main battery of nine 28 cm (11 in) C/34 guns in three triple turrets.  Plans to replace these weapons with six 38 cm (15 in) SK C/34 guns in twin turrets were never carried out.

German battleship Gneisenau: Gneisenau was a German capital ship, alternatively described as a battleship and battlecruiser, of Nazi Germany's "Kriegsmarine".  She was the second vessel of her class, which included one other ship, "Scharnhorst" .  The ship was built at the "Deutsche Werke" dockyard in Kiel; she was laid down on 6 May 1935 and launched on 8 December 1936.  Completed in May 1938, the ship was armed with a main battery of nine 28 cm (11 in) C/34 guns in three triple turrets, though there were plans to replace these weapons with six 38 cm (15 in) SK C/34 guns in twin turrets.

Michael Le Fanu: Admiral of the Fleet Sir Michael Le Fanu (2 August 1913 – 28 November 1970) was a Royal Navy officer.  He fought in the Second World War as gunnery officer in a cruiser operating in the Home Fleet during the Norwegian Campaign and the Battle of the Mediterranean and then as gunnery officer in a battleship operating in the Eastern Fleet before becoming liaison officer between the British Pacific Fleet and the United States Third Fleet.  After the War he commanded a frigate, a training establishment and an aircraft carrier.  He served as First Sea Lord and Chief of the Naval Staff in the late 1960s.  In that role, in the face of economic difficulties, he worked hard to reshape the Navy as an anti-submarine force operating primarily in the Atlantic Ocean.

Question: Michael Pollock was a gunnery officer on the Norfolk when it fought which German capital ship?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "officer_name": {
      "type": "string",
      "description": "The name of the officer."
    },
    "officer_role": {
      "type": "string",
      "description": "The role of the officer during the engagement."
    },
    "allied_ship": {
      "type": "string",
      "description": "The name of the allied ship the officer was on."
    },
    "enemy_capital_ship": {
      "type": "string",
      "description": "The name of the German capital ship fought."
    },
    "battle_name": {
      "type": "string",
      "description": "The name of the battle where the engagement took place."
    }
  },
  "required": [
    "officer_name",
    "officer_role",
    "allied_ship",
    "enemy_capital_ship",
    "battle_name"
  ],
  "additionalProperties": false
}
