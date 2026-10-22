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
Isaac C. Kidd: Isaac Campbell Kidd (March 26, 1884 – December 7, 1941) was an American Rear Admiral in the United States Navy.  Kidd was killed on the bridge of USS "Arizona" during the Japanese attack on Pearl Harbor.  He was the father of Admiral Isaac C. Kidd, Jr. He was a posthumous recipient of his nation's highest military honor—the Medal of Honor.  The highest ranking casualty at Pearl Harbor, he became the first U.S. Navy flag officer killed in action in World War II as well as the first killed in action against any foreign enemy.  A "Fletcher"-class destroyer , "Kidd" (DD-661) , was commissioned in his honor on April 23, 1943.  The second ship named after him, "Kidd" (DDG-993) , lead ship of four "Kidd"-class destroyer s, was commissioned on March 27, 1981.  An "Arleigh Burke"-class guided missile destroyer, "Kidd" (DDG-100) , was the third ship named after him and was commissioned on June 9, 2007.

USS Cole (DDG-67): USS "Cole" (DDG-67) is an "Arleigh Burke"-class Aegis-equipped guided missile destroyer homeported in Naval Station Norfolk, Virginia.  "Cole" is named in honor of Marine Sergeant Darrell S. Cole, a machine-gunner killed in action on Iwo Jima on 19 February 1945, during World War II.  "Cole" is one of 62 authorized "Arleigh Burke"-class guided missile destroyers, and one of 21 members of the Flight I-class that utilized the 5 in /54 caliber gun mounts found on the earliest of the "Arleigh Burke"-class destroyers.  The ship was built by Ingalls Shipbuilding and was delivered to the Navy on 11 March 1996.

USS Hopper: USS "Hopper" (DDG-70) is an "Arleigh Burke"-class guided missile destroyer of the United States Navy, named for the pioneering computer scientist Rear Admiral "Amazing" Grace Hopper.

Grace Hopper: Grace Brewster Murray Hopper (; December 9, 1906 – January 1, 1992) was an American computer scientist and United States Navy rear admiral.  One of the first programmers of the Harvard Mark I computer, she was a pioneer of computer programming who invented one of the first compiler related tools.  She popularized the idea of machine-independent programming languages, which led to the development of COBOL, an early high-level programming language still in use today.

HMS Hampshire (D06): HMS "Hampshire" was a County-class destroyer of the Royal Navy.  Laid down, in March 1959 a couple of weeks behind the class leader "Devonshire" , she was classified as a guided missile destroyer, as the Sea Lords regarded the concept of the cruiser and big gun ship as discredited by the perceived failure of the "Tiger" class and the obsolescence of the heavy gun.  The description of guided missile destroyer seemed more likely to win approval from the Treasury and Government for an adequate number of warships the size of small cruisers, which could play many traditional cruiser flagship and command functions, but had no armour around its gun and missile magazine.

USS Dahlgren (DDG-43): USS "Dahlgren" (DLG-12/DDG-43) was the 7th ship in the "Farragut"-class guided missile destroyer in the United States Navy.  She was launched on 16 March 1960 by Philadelphia Naval Shipyard and sponsored by Mrs. Katharine D. Cromwell, granddaughter of Rear Admiral John Adolphus Dahlgren.  She was commissioned on 8 April 1961, Commander C. E. Landis in command.  It was the third ship in the Navy to bear the name.  Commissioned as DLG-12, "Dahlgren" was reclassified a guided missile destroyer on July 1, 1975 and given the new hull number DDG-43.  The ship saw service until 1992, when she was placed in reserve.  She was sold for scrapping three times, the first time in 1994, but was repossessed twice as the ship breaking companies failed.  The ship was finally dismantled in 2006.

USS Mahan (DDG-42): USS "Mahan" (DDG-42), was a "Farragut"-class guided missile destroyer in the United States Navy.  She was named for Rear Admiral Alfred Thayer Mahan USN (1840–1914).  The ship was Laid down as DLG-11 by the San Francisco Naval Shipyard on 31 July 1957 and launched on 7 October 1959.  "Mahan" was sponsored by Mrs. H. P. Smith, wife of Vice Adm. Harold Page Smith, and commissioned on 25 December 1960.  "Mahan" was reclassified as a guided missile destroyer on 30 June 1975 and designated DDG-42.  USS "Mahan" was decommissioned on 15 June 1993 and stricken from the Naval Vessel Register on the same day.

Holly Graf: Holly Ann Graf is a retired Captain in the United States Navy.  Until January 2010 she was commanding officer of the "Ticonderoga"-class guided missile cruiser USS "Cowpens" (CG-63), a major surface combatant vessel of the fleet.  She was the first woman to command a cruiser in the history of the U.S. Navy.  Earlier, she had been the first woman in the U.S. Navy to command a destroyer when she served as skipper of the guided missile destroyer USS "Winston S. Churchill" (DDG-81).  Her personal decorations include the Legion of Merit and the Bronze Star, among others.  Graf was relieved of command for abusive behavior unbecoming of an officer and was featured in Time magazine that characterized her as a modern-day female "Captain Bligh."  The US Navy forced Graf into early retirement in 2012, but allowed her to do so at her current rank of Captain and under "honorable circumstances."

USS Bainbridge (CGN-25): USS "Bainbridge" (DLGN-25/CGN-25) was a nuclear-powered guided missile cruiser in the United States Navy, the only ship of her class.  Named in honor of Commodore William Bainbridge, she was the fourth US Navy ship to bear the name.  With her original hull classification symbol of DLGN (nuclear-powered guided missile destroyer leader, called a "frigate" at the time), she was the first nuclear-powered destroyer-type ship in the US Navy, and shared her name with the lead ship of the first US Navy destroyer class, the "Bainbridge"-class destroyer s.

Forrest Sherman-class destroyer: The 18 "Forrest Sherman"-class destroyers were the first US post-war destroyers (DD-927 to DD-930 were completed as destroyer leader configurations).  Commissioned beginning in 1955, these ships served until the late 1980s.  Their weaponry underwent considerable modification during their years of service.  Four were converted to guided missile destroyers.  This class also served as the basis for the "Charles F. Adams"-class guided missile destroyer.

Question: What is the name of the class guided missile destroyer named for the female who was a pioneer of computer programming responsible for inventing one of the first compiler related tools?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_named_after": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the person the ship is named after."
        },
        "occupation": {
          "type": "string",
          "description": "The primary occupation or role of the person."
        },
        "notable_achievement": {
          "type": "string",
          "description": "A key achievement or contribution of the person."
        }
      },
      "required": [
        "name",
        "occupation",
        "notable_achievement"
      ],
      "additionalProperties": false
    },
    "ship_details": {
      "type": "object",
      "properties": {
        "ship_name": {
          "type": "string",
          "description": "The name of the ship."
        },
        "ship_hull_number": {
          "type": "string",
          "description": "The hull number of the ship."
        }
      },
      "required": [
        "ship_name",
        "ship_hull_number"
      ],
      "additionalProperties": false
    },
    "destroyer_class_name": {
      "type": "string",
      "description": "The name of the destroyer class."
    },
    "destroyer_type": {
      "type": "string",
      "description": "The type of destroyer, e.g., 'guided missile destroyer'."
    }
  },
  "required": [
    "person_named_after",
    "ship_details",
    "destroyer_class_name",
    "destroyer_type"
  ],
  "additionalProperties": false
}
