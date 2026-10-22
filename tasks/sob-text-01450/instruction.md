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
United States Armed Forces: The United States Armed Forces are the military forces of the United States of America.  It consists of the Army, Marine Corps, Navy, Air Force, and Coast Guard.  The President of the United States is the U.S. Armed Forces's overall head, and helps form military policy with the U.S. Department of Defense (DoD) and U.S. Department of Homeland Security (DHS), both federal executive departments, acting as the principal organs by which military policy is carried out.  All five armed services are among the seven uniformed services of the United States.

Achievement Medal: The Achievement Medal is a military decoration of the United States Armed Forces.  The Achievement Medal was first proposed as a means to recognize the contributions of junior officers and enlisted personnel who were not eligible to receive the higher Commendation Medal or the Meritorious Service Medal.

Meritorious Civilian Service Award: The Meritorious Civilian Service Award is commonly the second highest award and medal provided to civilian employees within agencies of the federal government of the United States.  However, the various agencies' awards are not directly comparable.  For example, the US Army Meritorious Civilian Service Award is equivalent to the US military Legion of Merit, while the US Air Force Meritorious Civilian Service Award is equivalent to the lower US military Meritorious Service Medal.

Medal for Defence Service Abroad: The Medal for Defence Service Abroad (Norwegian: "Forsvarets Innsatsmedalje" ) is a military medal of Norway.  Established 1 January 1993, the medal was originally a participant medal awarded for service during military operations that took place in the 1990s.  The subsequent establishment of the Medal for Defence Operations Abroad rendered this medal obsolete.  However, in 2009 the medal was reintroduced as an achievement medal .  The medal was awarded for distinguished bravery and courage, beyond what is normally required during combat operations.  The medal's color was changed from bronze to gold, and the ribbons of the medal would vary, depending on the area of operations.  During this period of award the medal was always awarded with a rosette.  Finally, in 2012 the medal was further changed to a single ribbon design for all awards.  The medal may be awarded with rosette for particularly meritorious distinction.

National Intelligence Superior Service Medal: The National Intelligence Superior Service Medal is an award of the National Intelligence Awards Program that recognizes an individual's superior service or a lasting contribution over a long period of time to the United States Intelligence Community and the United States as a whole.  The medal ranks below the National Intelligence Distinguished Service Medal, but above the National Intelligence Exceptional Achievement Medal.

National Intelligence Reform Medal: The National Intelligence Reform Medal is an award of the United States Intelligence Community's National Intelligence Awards Program that recognizes extraordinary service in implementing the Intelligence Reform and Terrorism Prevention Act.  The medal ranks below the National Intelligence Superior Service Medal, but above the National Intelligence Exceptional Achievement Medal.  Established 23 May 2007 with the creation of the National Intelligence Awards Program, it was retired in November 2010.

National Intelligence Medal of Achievement: The National Intelligence Medal of Achievement is an award that was presented to members of the United States Intelligence Community, both civilian and military, to recognize significant acts of service to the community as a whole.  The National Intelligence Medal of Achievement was replaced with the equivalent National Intelligence Exceptional Achievement Medal, during the restructuring of the National Intelligence Community Awards (NICA) Program, with the revision of Intelligence Community Directive 655 (National Intelligence Awards Program) in 2012.

Jack James (rocket engineer): Jack N. James (November 22, 1920 – August 7, 2001) was a US rocket engineer who worked for over 35 years at the Jet Propulsion Laboratory, Pasadena, California, USA.  His work as a Project Manager for NASA's Mariner program in the 1960s included the first planetary flyby (of Venus) and first photographs by a space probe of Mars.  He received commendations for his work from several US Presidents, and his awards include the NASA Exceptional Scientific Achievement Medal (1965) and the Stuart Ballantine Medal (1967).

NASA Exceptional Achievement Medal: The NASA Exceptional Achievement Medal is an award of the National Aeronautics and Space Administration established in 1991.  The medal is awarded to both civilian members of NASA and military astronauts.

Kevin A. Ford: Kevin Anthony Ford (born July 7, 1960) is a retired United States Air Force Colonel and a NASA astronaut.  Ford has received a number of special honors and awards, some of which are the Air Force Meritorious Service Medal, Air Force Commendation Medal, Aerial Achievement Medal and the Armed Forces Expeditionary Medal.  Ford has also logged more than 5,000 flying hours and also holds FAA commercial certificates for airplanes, helicopters and gliders.  Ford has served in many roles at NASA since his selection in July 2000.  The roles include as a Capsule Communicator or CAPCOM.  He was also the Director Of Operations at the Gagarin Cosmonaut Training Center in Star City, Russia from January 2004 to January 2005.  He was pilot of STS-128 and Flight Engineer 2 of Soyuz TMA-06M from October 23, 2012 to March 16, 2013.

Question: Which position in the us military must you be in to be eligible for the achievement medal?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "medal_name": {
      "type": "string",
      "description": "The name of the military decoration."
    },
    "eligible_personnel_types": {
      "type": "array",
      "description": "A list of personnel types eligible for the medal.",
      "items": {
        "type": "string"
      }
    },
    "purpose": {
      "type": "string",
      "description": "The reason for the establishment or award of the medal."
    },
    "higher_medals_not_eligible_for": {
      "type": "array",
      "description": "A list of higher-ranking medals that personnel eligible for this medal are typically not eligible for.",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "medal_name",
    "eligible_personnel_types",
    "purpose",
    "higher_medals_not_eligible_for"
  ],
  "additionalProperties": false
}
