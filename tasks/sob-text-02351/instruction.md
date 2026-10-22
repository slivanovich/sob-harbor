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
William Douglas Crowder: Vice Admiral William Douglas Crowder retired from the United States Navy in November 2009 after serving as the Deputy Chief of Naval Operations for Operations, Plans and Strategy (N3/N5).  Vice Admiral Crowder was the 45th commander of the United States 7th Fleet.

Scott R. Van Buskirk: Vice Admiral Scott Ray Van Buskirk, is a retired United States Navy officer who was the 56th Chief of Naval Personnel.  He served as the CNP from October 2011 to August 2013.  He was succeeded by Vice Admiral William F. Moran and retired after 34 years of service.

USS Bainbridge (CGN-25): USS "Bainbridge" (DLGN-25/CGN-25) was a nuclear-powered guided missile cruiser in the United States Navy, the only ship of her class.  Named in honor of Commodore William Bainbridge, she was the fourth US Navy ship to bear the name.  With her original hull classification symbol of DLGN (nuclear-powered guided missile destroyer leader, called a "frigate" at the time), she was the first nuclear-powered destroyer-type ship in the US Navy, and shared her name with the lead ship of the first US Navy destroyer class, the "Bainbridge"-class destroyer s.

USS Porter (DDG-78): USS "Porter" (DDG-78) is an "Arleigh Burke"-class destroyer in the United States Navy.  "Porter" is the fifth US Navy ship to be named after US Navy officers Commodore David Porter, and his son, Admiral David Dixon Porter.  This ship is the 28th destroyer of her class.  "Porter" was the 12th ship of this class to be built at Ingalls Shipbuilding in Pascagoula, Mississippi.  She was laid down on 2 December 1996, launched and christened on 12 November 1997, and commissioned 20 March 1999, in Port Canaveral, Florida.

Rear Admiral William S. Parsons Award: The Rear Admiral William S. Parsons Award for Scientific and Technical Progress is awarded each year by the Navy League of the United States to a Navy or Marine Corps officer, enlisted person or civilian, who has made an outstanding contribution in any field of science that has furthered the development and progress of the US Navy or Marine Corps.  The award is named for Admiral William Sterling Parsons.  The award is presented with a certificate and a watch along with other Professional Excellence Awards (Sea Service Awards) at the National Convention of the Navy League of the United States.

USS Intrepid (CV-11): USS "Intrepid" (CV/CVA/CVS-11), also known as The Fighting "I", is one of 24 "Essex"-class aircraft carrier s built during World War II for the United States Navy.  She is the fourth US Navy ship to bear the name.  Commissioned in August 1943, "Intrepid" participated in several campaigns in the Pacific Theater of Operations, most notably the Battle of Leyte Gulf.  Decommissioned shortly after the end of the war, she was modernized and recommissioned in the early 1950s as an attack carrier (CVA), and then eventually became an antisubmarine carrier (CVS).  In her second career, she served mainly in the Atlantic, but also participated in the Vietnam War.  Her notable achievements include being the recovery ship for a Mercury and a Gemini space mission.  Because of her prominent role in battle, she was nicknamed "the Fighting I", while her frequent bad luck and time spent in dry dock for repairs—she was torpedoed once and hit by four separate Japanese kamikaze aircraft—earned her the nicknames "Decrepit" and "the Dry I".  Decommissioned in 1974, in 1982 "Intrepid" became the foundation of the "Intrepid" Sea, Air & Space Museum in New York City.

Marshalls–Gilberts raids: The Marshalls–Gilberts raids were tactical airstrikes and naval artillery attacks by United States Navy aircraft carrier and other warship forces against Imperial Japanese Navy (IJN) garrisons in the Marshall and Gilbert Islands on 1 February 1942.  The Japanese garrisons were under the overall command of Vice Admiral Shigeyoshi Inoue, commander of the 4th Fleet.  Japanese aircraft in the islands belonged to the IJN's 24th Air Flotilla under Rear Admiral Eiji Gotō.  The U.S. warship forces were under the overall command of Vice Admiral William Halsey, Jr.

Richard R. McNulty: Richard Robert McNulty, Rear admiral United States Navy, Vice admiral USMS, was born in Gloucester, Massachusetts on April 20, 1899 and died in Boston, Massachusetts on November 1, 1980.  The United States Merchant Marine Academy community considers Vice Admiral McNulty, a World War II veteran, who had long advocated for the Academy's creation, its "Father".  The Academy's McNulty Campus is named for the Vice Admiral.  He served as the Academy's 3rd superintendent.  Vice Admiral McNulty was, too, a professor emeritus at Georgetown University.

Albert T. Church: Vice Admiral Albert Thomas Church III (born 1947) is a retired Vice Admiral in the United States Navy.  Church served as on active duty for 36 years, retiring as a Vice Admiral in 2005.  During his service he commanded two warships, the Navy’s largest shore installation at Naval Station Norfolk, Virginia and was the longest serving Budget Director of the Navy (1998-2002).  Vice Admiral Church also served as the Naval Inspector General, during which time he completed a comprehensive review of interrogation techniques used by the Department of Defense in Iraq, Afghanistan, and at Guantanamo Bay, Cuba.  He is currently President of Prescient Edge Corporation, a US-based National Security Services and Technology Firm.

William Edward Ellis: Vice admiral William Edward Ellis (November 7, 1908 – September 26, 1982) served over 40 years in the U.S. Navy.  He ended his career as Chief of Staff to the Supreme Allied Commander Atlantic (SACLANT).  Ellis first distinguished himself as a naval aviator during World War II, during which time he earned commendations for service in the North African Campaign and, later, valor awards for his leadership as Commander Air Group 18 aboard USS "Intrepid".

Question: What year was the decommissioning of the US Navy ship that Vice admiral William Edward Ellis received valor awards for his leadership on?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "officer_name": {
      "type": "string",
      "description": "The name of the Vice Admiral associated with the ship."
    },
    "ship_name": {
      "type": "string",
      "description": "The name of the US Navy ship."
    },
    "decommissioning_year": {
      "type": "integer",
      "description": "The year the ship was decommissioned."
    }
  },
  "required": [
    "officer_name",
    "ship_name",
    "decommissioning_year"
  ],
  "additionalProperties": false
}
