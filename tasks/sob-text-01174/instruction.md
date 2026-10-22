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
Atomic nucleus: The atomic nucleus is the small, dense region consisting of protons and neutrons at the center of an atom, discovered in 1911 by Ernest Rutherford based on the 1909 Geiger–Marsden gold foil experiment.  After the discovery of the neutron in 1932, models for a nucleus composed of protons and neutrons were quickly developed by Dmitri Ivanenko and Werner Heisenberg.  Almost all of the mass of an atom is located in the nucleus, with a very small contribution from the electron cloud.  Protons and neutrons are bound together to form a nucleus by the nuclear force.

Ernest Rutherford: Ernest Rutherford, 1st Baron Rutherford of Nelson, (30 August 1871 – 19 October 1937) was a New Zealand-born British physicist who came to be known as the father of nuclear physics. " Encyclopædia Britannica" considers him to be the greatest experimentalist since Michael Faraday (1791–1867).

Des Wilson: Des Wilson (born 5 March 1941) is a New Zealand born British campaigner, political activist, businessman, sports administrator, author and poker player.  He was one of the founders of the British homelessness charity Shelter and was for a while an activist in, and President of, the British Liberal Party.

Wu experiment: The Wu experiment was a nuclear physics experiment conducted in 1956 by the Chinese American physicist Chien-Shiung Wu in collaboration with the Low Temperature Group of the US National Bureau of Standards.  The experiment's purpose was to establish whether or not conservation of parity ("P"-conservation), which was previously established in the electromagnetic and strong interactions, also applied to weak interactions.  If "P"-conservation were true, a mirrored version of the world (where left is right and right is left) would behave as the mirror image of the current world.  If "P"-conservation were violated, then it would be possible to distinguish between a mirrored version of the world and the mirror image of the current world.

Hélène Langevin-Joliot: Hélène Langevin-Joliot (born 19 September 1927) is a French nuclear physicist.  She was educated at the "IN2P3" (English: Institute of Nuclear Physics and Particles ) at Orsay, a laboratory which was set up by her parents Irène Joliot-Curie and Frédéric Joliot-Curie.  She is a member of the French government's advisory committee.  Currently, she is a professor of nuclear physics at the Institute of Nuclear Physics at the University of Paris and a Director of Research at the CNRS.  She is also known for her work in actively encouraging women to pursue careers in scientific fields.

Discovery of the neutron: The story of the discovery of the neutron and its properties is central to the extraordinary developments in atomic physics that occurred in the first half of the 20th century.  Early in the century, Ernest Rutherford developed a crude model for the atom, based on the gold foil experiment of Hans Geiger and Ernest Marsden.  In this model, atoms had their mass and positive charge concentrated in a very small nucleus.  Throughout the 1920s, the nucleus was viewed as composed of combinations of protons and electrons, the two elementary particles known at the time, but that model presented several experimental and theoretical contradictions.  The essential nature of the atomic nucleus was established with the discovery of the neutron by James Chadwick in 1932 and the determination that it was a new elementary particle, distinct from the proton.  Both the proton and neutron were presumed to be elementary particles until the 1960s when they were determined to be composite particles built from quarks.

Geiger–Marsden experiment: The Geiger–Marsden experiment(s) (also called the Rutherford gold foil experiment) were a landmark series of experiments by which scientists discovered that every atom contains a nucleus where its positive charge and most of its mass are concentrated.  They deduced this by measuring how an alpha particle beam is scattered when it strikes a thin metal foil.  The experiments were performed between 1908 and 1913 by Hans Geiger and Ernest Marsden under the direction of Ernest Rutherford at the Physical Laboratories of the University of Manchester.

Alec Merrison: Sir Alexander Walter Merrison FRS, was a British physicist born in Wood Green, London on 20 March 1924.  He was a professor in Experimental Physics at Liverpool University and the first Director of the new Daresbury Nuclear Physics Laboratory.  He later became Vice-Chancellor of University of Bristol.

Rudolf Peierls: Sir Rudolf Ernst Peierls, ( ; ] ; 5 June 1907 – 19 September 1995) was a German-born British physicist who played a major role in Tube Alloys, Britain's nuclear programme, and the Manhattan Project.  His obituary in "Physics Today" described him as "a major player in the drama of the eruption of nuclear physics into world affairs...".

Chien-Shiung Wu: Chien-Shiung Wu (; May 31, 1912 – February 16, 1997) was a Chinese-American experimental physicist who made significant contributions in the field of nuclear physics.  Wu worked on the Manhattan Project, where she helped develop the process for separating uranium metal into uranium-235 and uranium-238 isotopes by gaseous diffusion.  She is best known for conducting the Wu experiment, which contradicted the hypothetical law of conservation of parity.  This discovery resulted in her colleagues Tsung-Dao Lee and Chen-Ning Yang winning the 1957 Nobel Prize in physics, and also earned Wu the inaugural Wolf Prize in Physics a mere two decades later in 1978.  Her expertise in experimental physics evoked comparisons to Marie Curie.  Her nicknames include "the First Lady of Physics", "the Chinese Madame Curie", and the "Queen of Nuclear Research".

Question: Also called the Rutherford gold foil experiment, this New Zealand born British physicist directed the Geiger-Marsden experiment and later was known as the father of nuclear physics. Who was he?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "physicist_name": {
      "type": "string",
      "description": "The name of the physicist."
    },
    "nationality_or_origin": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The nationalities or places of origin of the physicist."
    },
    "key_roles_or_titles": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Significant roles or titles attributed to the physicist."
    },
    "directed_experiment": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The primary name of the experiment directed."
        },
        "alternative_name": {
          "type": "string",
          "description": "An alternative name for the experiment."
        },
        "performance_period": {
          "type": "string",
          "description": "The period during which the experiment was performed."
        }
      },
      "required": [
        "name",
        "alternative_name",
        "performance_period"
      ],
      "additionalProperties": false,
      "description": "Details about the experiment directed by the physicist."
    }
  },
  "required": [
    "physicist_name",
    "nationality_or_origin",
    "key_roles_or_titles",
    "directed_experiment"
  ],
  "additionalProperties": false
}
