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
Joseph Black: Joseph Black FRSE FRCPE FPSG (16 April 1728 – 6 December 1799) was a Scottish physician and chemist, known for his discoveries of magnesium, latent heat, specific heat, and carbon dioxide.  He was Professor of Anatomy and Chemistry at the University of Glasgow for 10 years from 1756, and then Professor of Medicine and Chemistry at the University of Edinburgh from 1766, teaching and lecturing there for more than 30 years.

Dolphus E. Milligan: Dolphus Edward Milligan (June 17, 1928, Brighton, Alabama – October 18, 1973) was an American chemist.  He received his bachelor's degree in chemistry from Morehouse College in Atlanta in 1949.  He earned a Master of Science (M.S) from Atlanta University in 1951.  He then accepted a position as a chemistry instructor in Fort Valley State College in Georgia.  He joined the faculty at the University of California at Berkeley while pursuing his doctorate studies.  In 1996, When Robert F. Curl accepted the Nobel Prize in chemistry he expressed his appreciation for Milligan’s help on his earlier more volatile experiments.  Milligan obtained his Ph.D in chemistry in 1958, his research focused on spectroscopic study of reaction intermediates at extremely low temperature.  After completing this doctorate he joined the Melton Institute of industrial research in Pittsburg where he conducted basic research.  In 1963, he joined the National Bureau of Standards as a physical chemist.  In 1970, he became an adjunct professor at Howard University while retaining his position at Mellon.  In 1971, he became the chief of the photochemistry section of the National Bureau of Standards (NIST).

METRIC: METRIC (Mapping EvapoTranspiration at high Resolution with Internalized Calibration) is a computer model developed by the University of Idaho, that uses Landsat satellite data to compute and map evapotranspiration (ET).  METRIC calculates ET as a residual of the surface energy balance, where ET is estimated by keeping account of total net short wave and long wave radiation at the vegetation or soil surface, the amount of heat conducted into soil, and the amount of heat convected into the air above the surface.  The difference in these three terms represents the amount of energy absorbed during the conversion of liquid water to vapor, which is ET.  METRIC expresses near-surface temperature gradients used in heat convection as indexed functions of radiometric surface temperature, thereby eliminating the need for absolutely accurate surface temperature and the need for air-temperature measurements.

Combined cycle: In electric power generation a combined cycle is an assembly of heat engines that work in tandem from the same source of heat, converting it into mechanical energy, which in turn usually drives electrical generators.  The principle is that after completing its cycle (in the first engine), the temperature of the working fluid engine is still high enough that a second subsequent heat engine may extract energy from the waste heat that the first engine produced.  By combining these multiple streams of work upon a single mechanical shaft turning an electric generator, the overall net efficiency of the system may be increased by 50–60%.  That is, from an overall efficiency of say 34% (in a single cycle) to possibly an overall efficiency of 51% (in a mechanical combination of two cycles) in net Carnot thermodynamic efficiency.  This can be done because heat engines are only able to use a portion of the energy their fuel generates (usually less than 50%).  In an ordinary (non combined cycle) heat engine the remaining heat (e.g., hot exhaust fumes) from combustion is generally wasted.

Phase-change memory: Phase-change memory (also known as PCM, PCME, PRAM, PCRAM, OUN (ovonic unified memory) and C-RAM or CRAM (chalcogenide RAM)) is a type of non-volatile random-access memory.  PRAMs exploit the unique behaviour of chalcogenide glass.  In the older generation of PCM, heat produced by the passage of an electric current through a heating element generally made of TiN was used to either quickly heat and quench the glass, making it amorphous, or to hold it in its crystallization temperature range for some time, thereby switching it to a crystalline state.  PCM also has the ability to achieve a number of distinct intermediary states, thereby having the ability to hold multiple bits in a single cell, but the difficulties in programming cells in this way has prevented these capabilities from being implemented in other technologies (most notably flash memory) with the same capability.  Newer PCM technology has been trending in two different directions.  One group has been directing a lot of research towards attempting to find viable material alternatives to GeSbTe (GST), with mixed success.  Another group has developed the use of a GeTe - SbTe superlattice to achieve non-thermal phase changes by simply changing the co-ordination state of the Germanium atoms with a laser pulse.  This new Interfacial Phase-Change Memory (IPCM) has had many successes and continues to be the site of much active research.

Fin (extended surface): In the study of heat transfer, fins are surfaces that extend from an object to increase the rate of heat transfer to or from the environment by increasing convection.  The amount of conduction, convection, or radiation of an object determines the amount of heat it transfers.  Increasing the temperature gradient between the object and the environment, increasing the convection heat transfer coefficient, or increasing the surface area of the object increases the heat transfer.  Sometimes it is not feasible or economical to change the first two options.  Thus, adding a fin to an object, increases the surface area and can sometimes be an economical solution to heat transfer problems.

Adair Crawford: Adair Crawford FRS FRSE (174829 July 1795), a chemist and physician, was a pioneer in the development of calorimetric methods for measuring the specific heat capacity of substances and the heat of chemical reactions.  In his influential 1779 book ""Experiments and Observations on Animal Heat"", Crawford presented new experiments proving that respiratory gas exchange in animals is a combustion (two years after Antoine Lavoisier's influential ""On combustion in general"").  Crawford also was involved in the discovery of the element strontium.

Flory–Fox equation: In polymer chemistry, the Flory–Fox equation is a simple empirical formula that relates molecular weight to the glass transition temperature of a polymer system.  The equation was first proposed in 1950 by Paul J. Flory and Thomas G. Fox while at Cornell University.  Their work on the subject overturned the previously held theory that the glass transition temperature was the temperature at which viscosity reached a maximum.  Instead, they demonstrated that the glass transition temperature is the temperature at which the free space available for molecular motions achieved a minimum value.  While its accuracy is usually limited to samples of narrow range molecular weight distributions, it serves as a good starting point for more complex structure-property relationships.

Arthur Smithells: Arthur Smithells, CMG FRS (24 May 1860 – 24 February 1939) was a British chemist.  Born in Bury, Lancashire, on 24 May 1860.  His father James Smithells, was a railway manager.  He was educated at University of Glasgow, then spent time under Roscoe and Schorlemmer at Owens College, Manchester.  He gained his B.Sc.  from the University of London, then took supplemental courses at Munich and, with Robert Bunsen, at Heidelberg University.  In 1883 he was appointed assistant lecturer at Owens College, and two years later succeeded Professor Sir Edward Thorpe as Professor of Chemistry in Yorkshire College, Leeds, which was subsequently incorporated as the University of Leeds.  Smithells went on to hold the position of Pro-Vice-Chancellor at Leeds, which he held until he retired from the Chair then becoming Emeritus Professor in 1923.

Calorimetry: Calorimetry is the science or act of measuring changes in state variables of a body for the purpose of deriving the heat transfer associated with changes of its state due, for example, to chemical reactions, physical changes, or phase transitions under specified constraints.  Calorimetry is performed with a calorimeter.  The word "calorimetry" is derived from the Latin word "calor", meaning heat and the Greek word "μέτρον" (metron), meaning measure.  Scottish physician and scientist Joseph Black, who was the first to recognize the distinction between heat and temperature, is said to be the founder of the science of calorimetry.

Question: What position did the physician and chemist, who was the first to recognize the distinction between heat and temperature, hold at the University of Glasgow?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the physician and chemist."
    },
    "university_name": {
      "type": "string",
      "description": "The name of the university where the position was held."
    },
    "position_held": {
      "type": "string",
      "description": "The specific position held by the person at the university."
    },
    "reason_for_identification": {
      "type": "string",
      "description": "The key characteristic used to identify the person."
    }
  },
  "required": [
    "person_name",
    "university_name",
    "position_held",
    "reason_for_identification"
  ],
  "additionalProperties": false
}
