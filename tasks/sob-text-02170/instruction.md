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
Minor planet: A minor planet is an astronomical object in direct orbit around the Sun that is neither a planet nor exclusively classified as a comet.  Minor planets can be dwarf planets, asteroids, trojans, centaurs, Kuiper belt objects, and other trans-Neptunian objects.  As of 2017, the orbits of 734,274 minor planets were archived at the Minor Planet Center, 496,815 of which had received permanent numbers ).

C/2015 ER61 (PANSTARRS): C/2015 ER (PANSTARRS) is a comet, inner Oort cloud object, Amor near-Earth asteroid, and possibly a damocloid.  When classified as a minor planet, it had the fourth-largest aphelion of any known minor planet in the Solar System, after , , and .  It additionally had the most eccentric orbit of any known minor planet, with its distance from the Sun varying by about 99.9% during the course of its orbit, followed by with an eccentricity of 0.9973.  On January 30, 2016, it was classified as a comet when it was 5.7 AU from the Sun.  It comes close to Jupiter, and a close approach in the past threw it on the distant orbit it is on now.

Distant minor planet: The term distant minor planet is used by the International Astronomical Union's Minor Planet Center to refer collectively to those minor planets found in the outer Solar System that are not commonly thought of as "asteroids".  Included are the populations of centaurs, Neptune trojans, and trans-Neptunian objects. All distant objects have a semi-major axis (average distance from the Sun) greater than 6 AU, which is just beyond the planet Jupiter.

Uncertainty parameter: The uncertainty parameter "U" is a parameter introduced by the Minor Planet Center (MPC) to quantify concisely the uncertainty of a perturbed orbital solution for a minor planet.  The parameter is a logarithmic scale from 0 to 9 that measures the anticipated longitudinal uncertainty in the minor planet's mean anomaly after 10 years.  The uncertainty parameter is also known as condition code in JPL's Small-Body Database Browser.  The "U" value should not be used as a predictor for the uncertainty in the future motion of near-Earth objects.

USS Tabora (AKA-45): USS "Tabora" (AKA-45) was an "Artemis"-class attack cargo ship named after the minor planet "721 Tabora."  The minor planet was itself named after a ship, as after its discovery in 1911 it was named in 1913 at a conference in Hamburg, Germany held aboard the ocean liner "Tabora" of the Deutsche Ost-Afrika Linie.

Transit of minor planets: A transit of a minor planet takes place when a minor planet passes directly between an observer and another heavenly body, obscuring a small part of that body's disc.  From the perspective of observers on Earth, transits of the Sun and Moon by minor planets are very rare, as the minor planets orbiting between the Earth and those bodies are few and very small.  Transits of the Sun would be more visible from the outer planets.

Giovanni de Sanctis: Giovanni de Sanctis (born 1949) is an Italian astronomer and discoverer of minor planets at the Osservatorio Astronomico di Torino (Astronomical Observatory of Turin) in Turin, Italy.  His name is sometimes spelt DeSanctis, particularly in the Minor Planet Circulars.  The Minor Planet Center credits him with the discovery of 42 numbered minor planets, most of which he discovered at ESO's La Silla site in northern Chile in the early 1980s.

Meanings of minor planet names: This is a list of minor planets which have been officially named by the Minor Planet Center (MPC).  The list consists of partial pages, each covering a number range of 1000 bodies citing the source after each minor planet was named for.  An overview of all existing partial pages is given in section .

Timur Eneev: Timur Magomedovich Eneev (born September 23, 1924) is a Russian mathematician specializing in mechanics and control processes.  A minor planet Eneev discovered in 1978 is named after him.  He is currently the editor-in-chief of the journal Cosmic Research.  Balkar by nation.

Cosmic Research: Cosmic Research (Russian: "Kosmicheskie Issledovaniya") is a bimonthly peer-reviewed scientific journal that was established in 1963.  It is published by MAIK Nauka/Interperiodica and published online by Springer Science+Business Media.  The editor-in-chief is Timur M. Eneev (Keldysh Institute of Applied Mathematics).  The journal is a continuation of the Soviet-Russian publication "Artificial Earth Satellites" (ISSN 0571-2041  ), in existence between 1960–1964.

Question: The minor planet Eneev is named after a mathematician that is the editor-in-cheif for a journal established in what year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "mathematician_name": {
      "type": "string",
      "description": "The name of the mathematician after whom the minor planet is named."
    },
    "journal_name": {
      "type": "string",
      "description": "The name of the journal for which the mathematician is the editor-in-chief."
    },
    "journal_establishment_year": {
      "type": "integer",
      "description": "The year the journal was established."
    }
  },
  "required": [
    "mathematician_name",
    "journal_name",
    "journal_establishment_year"
  ],
  "additionalProperties": false
}
