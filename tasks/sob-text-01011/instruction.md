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
One Body Too Many: One Body Too Many is a 1944 American comedy-mystery film directed by Frank McDonald, starring Bela Lugosi and Jack Haley.

Heat: Heat is the amount of energy flowing from one body of matter to another spontaneously due to their temperature difference, or by any means other than through work or the transfer of matter.  The transfer can be by contact between the source and the destination body, as in conduction; or by radiation between remote bodies; or by way of an intermediate fluid body, as in convective circulation; or by a combination of these.  In thermodynamics, heat is often contrasted with work: heat applies to individual particles (such as atoms or molecules), work applies to objects (or a system as a whole).  Heat involves stochastic (or random) motion equally distributed among all degrees of freedom, while work is directional, confined to one or more specific degrees of freedom.

Dorset and Wilts Rugby Football Union: Dorset and Wilts Rugby Football Union (Dorset & Wilts RFU) is the governing body for rugby union in the counties of Dorset and Wiltshire, England.  Dorset & Wilts RFU is a Constituent Body of the Rugby Football Union (RFU) and is responsible for the management and administration of the game within the counties of Dorset and Wiltshire of all forms and at all levels.  Originally Dorset and Wiltshire had their own county teams but would start to merge into one body towards the end of the 1930's, having already played a combined match against Hampshire in 1935-36 which Dorset & Wilts won 9-6.  By 1939 Dorset & Wilts agreed to become a unified rugby football union to take part in the 1940-41 County Championships but this was postponed by the outbreak of World War 2.  After the war Dorset & Wilts played its first official county match in 1947 and attained full county status from the RFU in 1949.

Retrograde and prograde motion: Retrograde motion is motion in the direction opposite to the movement of something else and the contrary of direct or prograde motion.  This "motion" can be the orbit of one body about another body or about some other point, or the rotation of a single body about its axis, or other phenomena such as precession or nutation of the axis.  In reference to celestial "systems", retrograde motion "usually" means motion that is contrary to the rotation of the primary, that is, the object that forms the system's hub.

Body kit: A body kit or bodykit is a set of modified body parts or additional components that install on a stock car.  Typically composed of front and rear bumpers, side skirts, spoilers, paint jobs, and sometimes front and rear side guards and roof scoops.  There are many companies that offer alternatives to the original factory appearance of the vehicle.  Body kits components are designed to complement each other and work together as a complete design.  Despite this, the 'mix and match' approach is often seen on cars, where the front of one body kit will be matched with the rear of another, for example.

Cornel Wilde: Cornel Wilde (October 13, 1912 – October 16, 1989) was a Hungarian-American actor and film director.

Lake Hart (Winter Haven, Florida): Lake Hart is actually two separate bodies of water that are joined as one body in very rainy years.  The smaller body is circular and is northeast of the main body.  The main body is in the shape of a figure eight with an oval body connected by a wide channel of water.  Lake Hart is a natural freshwater lake with an 67.85 acre surface area.  It is bordered on the west by residences in a gated community.  On the south and east are residences in the Lake Ashton gated community.  To the northeast and north are low-lying areas with no residential development on them.  This lake is on the south fringe of Winter Haven, Florida.

Bela Lugosi: Béla Ferenc Dezső Blaskó (] ; 20 October 1882 – 16 August 1956), better known as Bela Lugosi ( ; ] ), was a Hungarian-American actor, famous for portraying Count Dracula in the 1931 film and for his roles in various other horror films.

Mickey Hargitay: Miklós "Mickey" Hargitay ( ; Hungarian: "Hargitay Miklós" ] ; January 6, 1926 – September 14, 2006) was a Hungarian-American actor and the 1955 Mr. Universe.  Born in Budapest, Hargitay moved to the United States in 1947, where he eventually became a citizen.  He was married to Jayne Mansfield, and is the father of actress Mariska Hargitay.  During their marriage, Hargitay and Mansfield made four movies together: "Will Success Spoil Rock Hunter? " (1957), "The Loves of Hercules" (1960), "Promises!  Promises! " (1963), and "L'Amore Primitivo" (1964).

Organ transplantation: Organ transplantation is a medical procedure in which an organ is removed from one body and placed in the body of a recipient, to replace a damaged or missing organ.  The donor and recipient may be at the same location, or organs may be transported from a donor site to another location.  Organs and/or tissues that are transplanted within the same person's body are called autografts. Transplants that are recently performed between two subjects of the same species are called allografts.  Allografts can either be from a living or cadaveric source.

Question: Which Hungarian-American actor starred in One Body Too Many?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "actor_name": {
      "type": "string",
      "description": "The name of the actor who starred in the film."
    },
    "actor_nationality": {
      "type": "string",
      "description": "The nationality of the actor."
    },
    "actor_profession": {
      "type": "string",
      "description": "The profession of the actor."
    }
  },
  "required": [
    "film_title",
    "actor_name",
    "actor_nationality",
    "actor_profession"
  ],
  "additionalProperties": false
}
