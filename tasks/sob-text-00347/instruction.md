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
De Sitter double star experiment: The de Sitter effect was described by Willem de Sitter in 1913 (as well as by Daniel Frost Comstock in 1910) and used to support the special theory of relativity against a competing 1908 emission theory by Walther Ritz that postulated a variable speed of light.  De Sitter showed that Ritz's theory predicted that the orbits of binary stars would appear more eccentric than consistent with experiment and with the laws of mechanics, however, the experimental result was negative.  This was confirmed by Brecher in 1977 by observing the x-rays spectrum.  For other experiments related to special relativity, see tests of special relativity.

Moving magnet and conductor problem: The moving magnet and conductor problem is a famous thought experiment, originating in the 19th century, concerning the intersection of classical electromagnetism and special relativity.  In it, the current in a conductor moving with constant velocity, "v", with respect to a magnet is calculated in the frame of reference of the magnet and in the frame of reference of the conductor.  The observable quantity in the experiment, the current, is the same in either case, in accordance with the basic "principle of relativity", which states: "Only "relative" motion is observable; there is no absolute standard of rest".  However, according to Maxwell's equations, the charges in the conductor experience a magnetic force in the frame of the magnet and an electric force in the frame of the conductor.  The same phenomenon would seem to have two different descriptions depending on the frame of reference of the observer.

Time for the Stars: Time for the Stars is a juvenile science fiction novel by American writer Robert A. Heinlein, published by Scribner's in 1956 as one of the Heinlein juveniles.  The basic plot line is derived from a 1911 thought experiment in special relativity, commonly called the twin paradox, proposed by French physicist Paul Langevin.

Doubly special relativity: Doubly special relativity (DSR) – also called deformed special relativity or, by some, extra-special relativity – is a modified theory of special relativity in which there is not only an observer-independent maximum velocity (the speed of light), but an observer-independent maximum energy scale and minimum length scale (the Planck energy and Planck length).

Twin paradox: In physics, the twin paradox is a thought experiment in special relativity involving identical twins, one of whom makes a journey into space in a high-speed rocket and returns home to find that the twin who remained on Earth has aged more.  This result appears puzzling because each twin sees the other twin as moving, and so, according to an incorrect and naive application of time dilation and the principle of relativity, each should paradoxically find the other to have aged less.  However, this scenario can be resolved within the standard framework of special relativity: the travelling twin's trajectory involves two different inertial frames, one for the outbound journey and one for the inbound journey, and so there is no symmetry between the spacetime paths of the twins.  Therefore, the twin paradox is not a paradox in the sense of a logical contradiction.

Bell's spaceship paradox: Bell's spaceship paradox is a thought experiment in special relativity.  It was first designed by E. Dewan and M. Beran in 1959 and became more widely known when J. S. Bell included a modified version.  A delicate string or thread hangs between two spaceships.  Both spaceships now start accelerating simultaneously and equally as measured in the inertial frame S, thus having the same velocity at all times in S. Therefore, they are all subject to the same Lorentz contraction, so the entire assembly seems to be equally contracted in the S frame with respect to the length at the start.  Therefore, at first sight, it might appear that the thread will not break during acceleration.

Michelson–Gale–Pearson experiment: The Michelson–Gale–Pearson experiment (1925) is a modified version of the Michelson–Morley experiment and the Sagnac-Interferometer.  It measured the Sagnac effect due to Earth's rotation, and thus tests the theories of special relativity and luminiferous ether along the rotating frame of Earth.

Schrödinger's cat: Schrödinger's cat is a thought experiment, sometimes described as a paradox, devised by Austrian physicist Erwin Schrödinger in 1935.  It illustrates what he saw as the problem of the Copenhagen interpretation of quantum mechanics applied to everyday objects.  The scenario presents a cat that may be simultaneously both alive and dead, a state known as a quantum superposition, as a result of being linked to a random subatomic event that may or may not occur.  The thought experiment is also often featured in theoretical discussions of the interpretations of quantum mechanics.  Schrödinger coined the term "Verschränkung" (entanglement) in the course of developing the thought experiment.

Ladder paradox: The ladder paradox (or barn-pole paradox) is a thought experiment in special relativity.  It involves a ladder, parallel to the ground, travelling horizontally and therefore undergoing a Lorentz length contraction.  As a result, the ladder fits inside a garage which would normally be too small to contain it.  On the other hand, from the point of view of an observer moving with the ladder, it is the garage that is moving, so it is the garage which will be contracted to an even smaller size, thus being unable to contain the ladder.  This apparent paradox results from the mistaken assumption of absolute simultaneity.  The ladder fits into the garage only if both of its ends are simultaneously inside the garage.  In relativity, simultaneity is relative to each observer, and so the question of whether the ladder fits inside the garage is relative to each observer, and the paradox is resolved.

John Stewart Bell: John Stewart Bell FRS (28 June 1928 – 1 October 1990) was a Northern Irish physicist, and the originator of Bell's theorem, an important theorem in quantum physics regarding hidden variable theories.

Question: The thought experiment in special relativity became more widely known when a Northern Irish physicist, the originator of what  included a modified version?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "physicist_name": {
      "type": "string",
      "description": "The name of the physicist who made the thought experiment more widely known."
    },
    "physicist_nationality": {
      "type": "string",
      "description": "The nationality of the physicist."
    },
    "thought_experiment_name": {
      "type": "string",
      "description": "The name of the thought experiment in special relativity."
    },
    "concept_originated_by_physicist": {
      "type": "string",
      "description": "The name of the concept or theorem originated by the physicist."
    },
    "concept_field": {
      "type": "string",
      "description": "The field of physics to which the originated concept belongs."
    }
  },
  "required": [
    "physicist_name",
    "physicist_nationality",
    "thought_experiment_name",
    "concept_originated_by_physicist",
    "concept_field"
  ],
  "additionalProperties": false
}
