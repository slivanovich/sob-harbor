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
François Englert: François Baron Englert (] ; born 6 November 1932) is a Belgian theoretical physicist and 2013 Nobel prize laureate (shared with Peter Higgs).  He is Professor emeritus at the Université libre de Bruxelles (ULB) where he is member of the Service de Physique Théorique.  He is also a Sackler Professor by Special Appointment in the School of Physics and Astronomy at Tel Aviv University and a member of the Institute for Quantum Studies at Chapman University in California.  He was awarded the 2010 J. J. Sakurai Prize for Theoretical Particle Physics (with Gerry Guralnik, C. R. Hagen, Tom Kibble, Peter Higgs, and Robert Brout), the Wolf Prize in Physics in 2004 (with Brout and Higgs) and the High Energy and Particle Prize of the European Physical Society (with Brout and Higgs) in 1997 for the mechanism which unifies short and long range interactions by generating massive gauge vector bosons.  He has made contributions in statistical physics, quantum field theory, cosmology, string theory and supergravity.  He is the recipient of the 2013 Prince of Asturias Award in technical and scientific research, together with Peter Higgs and the CERN.

Palash Baran Pal: Palash Baran Pal (Bengali: পলাশ বরন পাল "Palāś Baran Pāl", born : 1955) is an Indian theoretical physicist, a senior professor at Saha Institute of Nuclear Physics, Kolkata, a writer, a linguist and a poet.  His main area of research is Particle Physics.  His works in the area of neutrino physics and relativistic treatment of particle properties in matter are well recognized in the particle physics community.  Apart from his scientific contributions, he has authored well known text books in physics as well as several popular science literature in Bengali to popularize science.

TRIUMF: TRIUMF is Canada's national laboratory for particle and nuclear physics and accelerator-based science.  TRIUMF is considered Canada's premier physics laboratory, and is consistently regarded as one of the leading subatomic physics research centers on the international level.  Owned and operated by a consortium of universities as a joint venture, TRIUMF is located on the south campus of one of its founding members - the University of British Columbia in Vancouver, British Columbia.  TRIUMF houses the world's largest cyclotron, a source of 520 MeV protons, which was named an IEEE Milestone in 2010.  TRIUMF's accelerator-focused activities involve particle physics, nuclear physics, nuclear medicine, materials science, and detector and accelerator development.

CERN: The European Organization for Nuclear Research (French: "Organisation européenne pour la recherche nucléaire"), known as CERN ( ; ] ; derived from the name "Conseil Européen pour la Recherche Nucléaire"), is a European research organization that operates the largest particle physics laboratory in the world.  CERN is an official United Nations Observer.  Established in 1954, the organization is based in a northwest suburb of Geneva on the Franco–Swiss border, ( ) and has 22 member states.  Israel is the only non-European country granted full membership.

Julius Ashkin: Julius Ashkin (August 23, 1920 – June 4, 1982) was a leader in experimental and theoretical physics known for furthering the evolution of particle physics from nuclear physics.  As a theoretical physicist he made contributions in the fields of statistical mechanics, solid state physics, nuclear physics, and elementary particle physics.  As an experimental physicist his main contributions concerned the passage of certain particles (pi-mesons, or pions) through solid matter and their subsequent decay.  He was recognized for the quality of his research and teaching.

Kyriakos Tamvakis: Kyriakos Tamvakis (Greek: Κυριάκος Ταμβάκης ; born in 1950 ) is a Greek theoretical physicist and professor at the University of Ioannina.  Kyriakos Tamvakis studied at the University of Athens and gained his Ph.D. at Brown University, Providence, Rhode Island, USA in 1978.  His thesis title was "Induced Boson Selfcouplings In Four Fermion And Yukawa Theories".  Since then he has held several positions at CERN’s Theory Division in Geneva, Switzerland.  He has been Professor of Theoretical Physics at the University of Ioannina, Greece, since 1982.  Professor Tamvakis has published more than 100 articles on theoretical high-energy physics in various journals and has written two textbooks in Greek, on quantum mechanics and on classical electrodynamics.

Juansher Chkareuli: Juansher Levan Chkareuli (Georgian: ჯუანშერ ჩქარეული ; born 1940, Tbilisi) is a Georgian theoretical physicist working in particle physics, Professor at Institute of Theoretical Physics of Ilia State University in Tbilisi and Head of Particle Physics Department at Andronikashvili Institute of Physics of Tbilisi State University.

JoAnne L. Hewett: JoAnne L. Hewett (born 1960) is a theoretical particle physicist on the faculty of the SLAC National Accelerator Laboratory, where she is a professor in the Department of Particle Physics and Astrophysics, and Director of the Elementary Particle Physics Division.  Her research interests include physics beyond the Standard Model, string theory, and hidden dimensions.  She is a fellow of the American Physical Society and a fellow of the American Association for the Advancement of Science (AAAS).

KEK: The High Energy Accelerator Research Organization (高エネルギー加速器研究機構 , Kō Enerugī Kasokuki Kenkyū Kikō ) , known as KEK, is a Japanese organization whose purpose is to operate the largest particle physics laboratory in Japan, situated in Tsukuba, Ibaraki prefecture.  It was established in 1997.  The term "KEK" is also used to refer to the laboratory itself, which employs approximately 695 employees.  KEK's main function is to provide the particle accelerators and other infrastructure needed for high-energy physics, material science, structural biology, radiation science, computing science, nuclear transmutation and so on.  Numerous experiments have been constructed at KEK by the internal and international collaborations that have made use of them.  Makoto Kobayashi, emeritus professor at KEK, is known globally for his work on CP-violation, and was awarded the 2008 Nobel Prize in Physics.

Phenomenology (particle physics): Particle physics phenomenology is the part of theoretical particle physics that deals with the application of theoretical physics to high-energy experiments.  Phenomenology forms a bridge between the mathematical models of theoretical physics (such as quantum field theories and theories of the structure of space-time) and experimental particle physics, by making quantitative predictions based upon the theoretical models.  Phenomenology is related to the philosophical notion in that these predictions describe anticipated behaviors for phenomena in reality.

Question: Kyriakos Tamvakis is a Greek theoretical physicist and professor who has held positions at what European research organization that operates the largest particle physics laboratory in the world?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "physicist_name": {
      "type": "string",
      "description": "The name of the theoretical physicist."
    },
    "organization": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the European research organization."
        },
        "type": {
          "type": "string",
          "description": "Description of the organization's primary function or type."
        },
        "key_characteristic": {
          "type": "string",
          "description": "A defining characteristic of the organization, as described in the context."
        }
      },
      "required": [
        "name",
        "type",
        "key_characteristic"
      ],
      "additionalProperties": false
    },
    "physicist_role_at_organization": {
      "type": "string",
      "description": "The specific role or division the physicist held at the organization."
    }
  },
  "required": [
    "physicist_name",
    "organization",
    "physicist_role_at_organization"
  ],
  "additionalProperties": false
}
