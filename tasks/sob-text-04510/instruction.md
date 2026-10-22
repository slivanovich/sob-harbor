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
Motorenfabrik Oberursel: Motorenfabrik Oberursel A.G. was a German manufacturer of automobile, locomotive and aircraft engines situated in Oberursel (Taunus), near Frankfurt (Main), Germany.  During World War I it supplied a major 100 hp-class rotary engine that was used in a number of early-war fighter aircraft designs.  In 1921 the company merged with Deutz AG, and then again in 1930 with Humboldt-Deutz Motoren, and finally in 1938 with Klöcknerwerke AG.  From this point on they were known as the Klöckner-Humboldt-Deutz Oberursel factory, known primarily for their locomotive engines.  Today they are part of Rolls-Royce Deutschland, and produce one family of their jet engines.

Rolls-Royce Holdings: Rolls-Royce Holdings plc is a British multinational public limited company incorporated in February 2011 that owns Rolls-Royce, a business established in 1904 and today designs, manufactures and distributes power systems for aviation and other industries.  Rolls-Royce is the world’s second-largest maker of aircraft engines and has major businesses in the marine propulsion and energy sectors.  All of its shares are tradeable on the London Stock Exchange and other markets.

Engineering apprentice: An engineering apprenticeship in the United Kingdom is an apprenticeship in mechanical engineering or electrical engineering or aeronautical engineering to train craftsmen, technicians, senior technicians, Incorporated Engineers and Chartered Engineer for vocational oriented work and professional practice.  Chartered Engineers are usually formed through a university degree programme at the Masters Engineering level and may undertake a short form of post graduate apprenticeship.  A typical example is the apprenticeships formerly available at the BTH and EEC at Rugby in England.  Subjects covered included mathematics, engineering sciences, limits and fits, metallurgy, foundry technology, engineering drawing, design, materials science for engineering materials, metalworking by hand, operating machine tools, and basic features of engineering design.  Also refer to apprenticeship and the UK and German section.  Elite technical apprenticeships (4-6 years long) have been a decades long tradition at UK companies such as BAE Systems, Rolls-Royce Holdings, Bombardier Aerospace (Short Brothers), and Babcock International.

Gloup: "Note: "Gloup" is common in Scottish placenames referring to a sea jet."

Rolls-Royce Power Systems: Rolls-Royce Power Systems AG is the name of a German industrial concern, which holds interests in a number of engine manufacturing brands and facilities, owned by Rolls-Royce Holdings.  The company previously traded, from 2006 to 2014, as Tognum AG.  Prior to 2006, the core company - MTU Friedrichshafen GmbH was a constituent of DaimlerChrysler Powersystems Off-Highway.

Warren East: (David) Warren Arthur East {'1': ", '2': ", '3': ", '4': "} (born 27 October 1961) is the chief executive officer (CEO) of Rolls-Royce Holdings, a leading UK-based engine manufacturer.  He previously held senior positions at ARM Holdings and Texas Instruments.

De Havilland Sea Vixen: The de Havilland DH.110 Sea Vixen is a twin boom, twin-engined 1950s–60s British two-seat jet fighter operated by the Fleet Air Arm.  It was designed by de Havilland during the late 1940s at its facility in Hatfield, Hertfordshire.  Developed from an earlier first generation jet fighter, the Sea Vixen was a carrier-based fleet defence fighter that served into the 1970s.  Initially produced by de Havilland, it was later known as the Hawker Siddeley Sea Vixen after de Havilland became a part of the Hawker Siddeley group in 1960.

Alvis plc: Alvis Ltd. was created when United Scientific Holdings plc acquired the Alvis division of the nationalised vehicle manufacturer British Leyland in 1981.  United Scientific maintained its own name until 1992 when the group was renamed Alvis plc.  Alvis acquired Swedish armoured vehicle manufacturer Hagglunds AB in 1997 and the armoured vehicle business of GKN in 1998.  Finally, it acquired Vickers Defence Systems from Rolls-Royce in October 2002.  Alvis was acquired by BAE Systems in 2004 and became BAE Systems Land Systems (Weapons & Vehicles), now part of the BAE Systems Land & Armaments operating group.

Rolls-Royce India Private Limited: Rolls-Royce India Private Limited is a subsidiary of Rolls-Royce Holdings.  The subsidiary looks after the regional client base as well as the supply chain for its aeronautics and industrial businesses.

Sea Jet: Sea Jet, or Advanced Electric Ship Demonstrator (AESD), is a naval testbed funded by the U.S. Navy's Office of Naval Research.  The 133 ft vessel is operated out of the Carderock Division's Acoustic Research Detachment in Bayview, Idaho.  "Sea Jet" was operated on Lake Pend Oreille, where she was used for test and demonstration of various technologies.  Among the first technologies tested was an underwater discharge water jet from Rolls-Royce Naval Marine, Inc., called AWJ-21, a propulsion concept with the goals of providing increased propulsive efficiency, reduced acoustic signature, and improved maneuverability over previous Destroyer Class combatants.

Question: What part did Rolls-Royce Holdings make for Sea Jet?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "part_description": {
      "type": "string",
      "description": "A description of the part manufactured."
    },
    "part_model_name": {
      "type": "string",
      "description": "The specific model name or designation of the part."
    },
    "manufacturer_group": {
      "type": "string",
      "description": "The name of the overarching manufacturing group."
    },
    "manufacturer_subsidiary": {
      "type": "string",
      "description": "The specific subsidiary of the manufacturer that produced the part."
    },
    "vessel_name": {
      "type": "string",
      "description": "The name of the vessel for which the part was made."
    },
    "part_function_goals": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of the intended goals or benefits of the part's design."
    }
  },
  "required": [
    "part_description",
    "part_model_name",
    "manufacturer_group",
    "manufacturer_subsidiary",
    "vessel_name",
    "part_function_goals"
  ],
  "additionalProperties": false
}
