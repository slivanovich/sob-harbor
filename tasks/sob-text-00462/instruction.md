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
Trident laser: The Trident Laser is a high power, sub-petawatt class, solid-state laser facility located at Los Alamos National Laboratory (LANL website), in Los Alamos, New Mexico, originally built in the late 1980s for Inertial confinement fusion (ICF) research by KMS Fusion, founded by Kip Siegel, in Ann Arbor, Michigan, it was later moved to Los Alamos in the early 1990s to be used in ICF and materials research.  The system is now being decommissioned with final laser experiments being completed February 2017.

New Mexico State Road 501: New Mexico Route 501 is a very short state highway in New Mexico, United States of America.  Its total length is only about 7 mi .  New Mexico Route 501's southwestern terminus is at New Mexico State Road 4 west of Los Alamos.  It runs northeast into the town of Los Alamos, where it ends.  It passes through the territory of Los Alamos National Laboratory (LANL), which is closed to the public (the public may drive through on Route 501).  Guard posts are at either end of the LANL section of the highway, and motorists passing into (but not out of) LANL territory must pause at the posts and be waved through.  Under most conditions, no inspections, etc., are performed at the guard posts, but heightened security postures at LANL may lead to more intrusive checks.

ASCI Blue Mountain: ASCI Blue Mountain is a supercomputer installed at the Los Alamos National Laboratory in Los Alamos, New Mexico.  It was designed to run simulations for the United States National Nuclear Security Administration's Advanced Simulation and Computing program.  The computer was a collaboration between Silicon Graphics Corporation and Los Alamos National Laboratory.

Otto Robert Frisch: Otto Robert Frisch FRS (1 October 1904 – 22 September 1979) was an Austrian-British physicist.  With his collaborator Rudolf Peierls he designed the first theoretical mechanism for the detonation of an atomic bomb in 1940.

Michael R. Anastasio: Michael Anastasio (born 1948) led two national science laboratories during a time of transition.  He was the director of the Los Alamos National Laboratory and president of the Los Alamos National Security LLC, the company that operates the laboratory.  He is the former director of Lawrence Livermore National Laboratory (LLNL).  The University of California Board of Regents appointed Michael R. Anastasio the director of LLNL on June 4, 2002.  He started on July 1, 2002.  In 2005 he became the president of the Los Alamos National Security LLC, and became the director of the Los Alamos National Laboratory on June 1, 2006.  During his directorship at Lawrence Livermore, the laboratory won 25 R&D 100 Awards and maintained its world-class leadership position in high-performance computing and its application to global climate modeling.

Los Alamos National Security: Los Alamos National Security, LLC (LANS LLC) is a private limited liability company (LLC) formed by the University of California, Bechtel, BWX Technologies, and URS Energy and Construction (which was purchased by AECOM in 2014).  It currently operates Los Alamos National Laboratory (LANL) for the Department of Energy and the National Nuclear Security Administration.  It took over direct management and operation of the Los Alamos National Laboratory from the University of California on June 1, 2006.  It is based in Los Alamos, New Mexico.

White Rock, New Mexico: White Rock is a town in Los Alamos County, New Mexico, United States.  It is one of two population centers in the county known as census-designated places (CDPs); the other is Los Alamos (the county seat).  The population was 6,045 at the 2000 census.  It is largely a bedroom community for employees of Los Alamos National Laboratory and their families.  Access to White Rock from the town of Los Alamos and other cities and towns in New Mexico is via New Mexico State Road 4, which forms the northwestern boundary of the community.  Administratively, White Rock is a neighborhood of Los Alamos; locals refer to Los Alamos (meaning not White Rock) as "the Townsite," or "the Hill".

Omega West Reactor: The Omega West Reactor (OWR) was an experimental nuclear reactor located at Los Alamos National Laboratory in Los Alamos NM.  OMR was completed in 1956 and primarily used for scientific scale nuclear research until it was fully decommissioned in 1994.  It operated 24 hours a day, five days a week until 1972, when it went to eight hours a day, five days a week operation.  The original purpose of the reactor was to collect nuclear material properties in support of the United States nuclear weapons program.  Other uses included production of useful medical isotopes.  The reactor was capable of producing an external beam of neutrons via beam tubes which extended through the reactor shielding.  These were provided for external neutron beam experiments including: neutron radiography, neutron capture studies, gamma ray studies, neutron cross section measurements and neutron activation studies.

James Doss: James D. Doss (1939, Kentucky, -17 May 2012) was a noted American mystery novel author.  He was the creator of the popular fictional Ute detective/rancher Charlie Moon, of whom he wrote 17 mystery novels.  James "Danny" Doss was born and raised in Kentucky and died in Los Alamos, New Mexico.  He was also an electrical engineer who worked on particle accelerators and biomedical technology for the University of California's Los Alamos National Laboratory, while writing his novels.  After retirement from Los Alamos National Laboratory, he continued to write his popular novels while living in Taos, New Mexico and Los Alamos, New Mexico.

Godiva device: The Lady Godiva device was an unshielded, pulsed nuclear reactor originally situated at the Los Alamos National Laboratory (LANL), New Mexico, U.S.  It was one of a number of criticality devices within Technical Area 18 (TA-18).  Specifically, it was used to produce bursts of neutrons and gamma rays for irradiating test samples, and inspired development of Godiva-like reactors.  Physicist Otto Frisch remembered the Los Alamos team called an earlier unshielded uranium-235 assembly in 1944 "Lady Godiva".

Question: The Lady Godiva device was an unshielded, pulsed nuclear reactor originally situated at the Los Alamos National Laboratory (LANL), New Mexico, physicist Otto Frisch remembered the Los Alamos team called an earlier unshielded uranium-235 assembly in which year, "Lady Godiva"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "device_name": {
      "type": "string",
      "description": "The name given to the nuclear assembly."
    },
    "device_type": {
      "type": "string",
      "description": "The type of nuclear assembly."
    },
    "location": {
      "type": "string",
      "description": "The laboratory where the device was located."
    },
    "year_named": {
      "type": "integer",
      "description": "The year the assembly was named 'Lady Godiva'."
    },
    "named_by_team": {
      "type": "string",
      "description": "The team that named the assembly."
    },
    "physicist_who_remembered": {
      "type": "string",
      "description": "The physicist who remembered the naming of the assembly."
    }
  },
  "required": [
    "device_name",
    "device_type",
    "location",
    "year_named",
    "named_by_team",
    "physicist_who_remembered"
  ],
  "additionalProperties": false
}
