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
USS Illinois (SSN-786): USS "Illinois" (SSN-786) is a "Virginia"-class submarine built by Electric Boat, a division of General Dynamics.  "Illinois" is the third of the Block III "Virginia"-class subs, which feature a revised bow, including some technology from "Ohio"-class SSGNs.  The submarine was delivered to the United States Navy on 27 August 2016 and was commissioned at Naval Submarine Base New London, Groton, Connecticut, on October 29, 2016.

ORP Orzeł (1962): ORP "Orzeł" a Polish Navy submarine of the "Project 613" (Whiskey-class) .  She was built in the Soviet Union and was commissioned by the Polish Navy in 1962.  She served under the code designation 292 (317 for a brief period) and was decommissioned in 1983.  In 1968, during Warsaw Pact fleet exercise on Barents Sea, together with the other Polish submarine ORP "Kondor", she avoided detection by huge Soviet and East Germany ASW forces, consisting of 300 ships - including nuclear submarines - and about 500 aircraft, and unnoticed entered into the biggest Soviet naval base in Murmansk.  A year later, guided by radio-guidance from Poland, "Orzeł" intercepted in the North Sea the Soviet Sverdlov class cruiser and torpedoed her by dummy torpedoes.  In implementing the Warsaw Pact's Cold War strategy, she also led patrols in the North Atlantic, doing jobs there such as a continuous reconnaissance in close distance to NATO's naval bases, including the most important U.S. strategic submarine base outside United States - Holy Loch in Scotland and also the base of Londonderry in Northern Ireland.  She was also exercising the breaking of western marine communication lines in the North Atlantic, as well as carrying out tasks in the North Atlantic training programs, including "Use of weapons and overcome ASW forces exercise program".

USS Seal (SS-183): USS "Seal" (SS-183), a "Salmon"-class submarine, was the second ship of the United States Navy to be named for the seal, a sea mammal valued for its skin and oil.  Her keel was laid down on 25 May 1936 by the Electric Boat Company in Groton, Connecticut.  She was launched on 25 April 1937 at the Naval Submarine Base, New London, sponsored by Mrs. Rosemary G. Greenslade, wife of Lieutenant (later Rear Admiral) John F. Greenslade and daughter-in-law of Rear Admiral John W. Greenslade.  The boat was commissioned on 30 April 1937, Lieutenant Karl G. Hensel in command.

Georgia State Route 40: State Route 40 (SR 40) is a 30.46 mi state highway in the southeast part of the U.S. state of Georgia.  The highway travels from US 1/US 23/US 301/SR 4/SR 15 in Folkston east to Church Street in St. Marys.  SR 40 is the primary east–west highway of eastern Charlton County and southern Camden County.  The highway connects Folkston and St. Marys with Kingsland, where the route meets Interstate 95 (I-95) and US 17/SR 25.  SR 40 also serves as the majority of the route from I-95 to Naval Submarine Base Kings Bay and Cumberland Island National Seashore.  SR 40 has a pair of auxiliary routes: a connector route in Folkston and a spur route in St. Marys that provides access to the submarine base and Crooked River State Park.

USS Los Angeles (SSN-688): USS "Los Angeles" (SSN-688), lead ship of her class of submarines, was the fourth ship of the United States Navy to be named for Los Angeles, California.  The contract to build her was awarded to Newport News Shipbuilding and Dry Dock Company in Newport News, Virginia on 8 January 1971 and her keel was laid down on 8 January 1972.  She was launched on 6 April 1974 sponsored by Anne Armstrong, and commissioned on 13 November 1976 with Commander John E. Christensen in command.  She hosted President Jimmy Carter and the First Lady on 27 May 1977 for an at-sea demonstration of her capabilities.  In 2007 she was the oldest submarine in active service with the United States Navy.  The Navy decommissioned USS "Los Angeles" on 23 January 2010, in the Port of Los Angeles, Los Angeles, California, her namesake city.  The wardroom of the oldest submarine in the fleet carries Richard O'Kane's personal cribbage board, and upon "Los Angeles"' decommissioning the board was transferred to the next oldest boat, USS "Bremerton" .

Naval Submarine Base Bangor: Naval Submarine Base Bangor is a former submarine base of the United States Navy that was merged with Naval Station Bremerton into Naval Base Kitsap in 2004.

USS Plunger (1897): Plunger (a.k.a. "Holland V") was the first submarine torpedo boat to be built for the United States Navy.  She was entirely experimental and was never commissioned in the U.S. Navy or operationally deployed.  (Some sources refer to her as the USS "Plunger" but the USS title is only applied to commissioned ships in the U.S. Navy.)  She is not to be confused with the later submarine USS "Plunger" (SS-2).

American submarine NR-1: Deep Submergence Vessel "NR-1" was a unique United States Navy (USN) nuclear-powered ocean engineering and research submarine, built by the Electric Boat Division of General Dynamics at Groton, Connecticut.  "NR-1" was launched on 25 January 1969, completed initial sea trials 19 August 1969, and was home-ported at Naval Submarine Base New London.  "NR-1" was the smallest nuclear submarine ever put into operation.  The vessel was casually known as "Nerwin" and was never officially named or commissioned.  The U.S. Navy is allocated a specific number of warships by the U.S. Congress.  Admiral Hyman Rickover avoided using one of those allocations, and he also wanted to avoid the oversight that a warship receives from various bureaus.

Naval Submarine Base New London: Naval Submarine Base New London is the United States Navy's primary East Coast submarine base, also known as the "Home of the Submarine Force".  It is located in Groton, Connecticut.

Naval Submarine Base Kings Bay: Naval Submarine Base Kings Bay is a base of the United States Navy located adjacent to the town of St. Marys in Camden County, Georgia, in southeastern Georgia, and 38 miles (61 km) from Jacksonville, Florida.  The Submarine Base is the U.S. Atlantic Fleet's home port for U.S. Navy Fleet ballistic missile nuclear submarines armed with Trident missile nuclear weapons.  This submarine base covers about 16,000 acres (6,400 hectares) of land, of which 4,000 acres (1,600 hectares) are protected wetlands.

Question: The USS "Illinois" was commissioned at the United States Navy's primary East Coast submarine base, also known as what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "submarine_base_name": {
      "type": "string",
      "description": "The official name of the submarine base."
    },
    "alternative_name": {
      "type": "string",
      "description": "Another name or designation for the submarine base."
    },
    "location": {
      "type": "string",
      "description": "The city and state where the submarine base is located."
    },
    "commissioned_submarine": {
      "type": "string",
      "description": "The name of the submarine commissioned at this base."
    }
  },
  "required": [
    "submarine_base_name",
    "alternative_name",
    "location",
    "commissioned_submarine"
  ],
  "additionalProperties": false
}
