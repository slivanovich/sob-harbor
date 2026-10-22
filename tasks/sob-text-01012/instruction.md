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
Sebastián Rulli: Sebastián Óscar Rulli (] or ] ; born July 6, 1975 in Buenos Aires, Argentina) is an Argentine actor and model.

El mejor papá del mundo: El mejor papá del mundo ("The Best Dad in the World") is a 1941 black and white Argentine drama.  It explores a son's gradual realization that his father is far from perfect, and also conveys a message hostile to global capitalism.

Papá Corazón se quiere casar: Papá Corazón se quiere casar is a 1974 Argentine film.

Minguito Tinguitela, papá: Minguito Tinguitela, papá is a 1974 Argentine film.

Eloy Álvarez: Eloy Álvarez (1896–1951) was an Argentine actor of the classic period of Argentine cinema.  At the 1944 Argentine Film Critics Association Awards he won the Silver Condor Award for Best Supporting Actor for his performance in the critically acclaimed comedy-drama "Juvenilia".  He later starred in the successful picture "Dark River" ("Las aguas bajan turbias") in 1952.

Lattice model (physics): In physics, a lattice model is a physical model that is defined on a lattice, as opposed to the continuum of space or spacetime.  Lattice models originally occurred in the context of condensed matter physics, where the atoms of a crystal automatically form a lattice.  Currently, lattice models are quite popular in theoretical physics, for many reasons.  Some models are exactly solvable, and thus offer insight into physics beyond what can be learned from perturbation theory.  Lattice models are also ideal for study by the methods of computational physics, as the discretization of any continuum model automatically turns it into a lattice model.  Examples of lattice models in condensed matter physics include the Ising model, the Potts model, the XY model, the Toda lattice.  The exact solution to many of these models (when they are solvable) includes the presence of solitons. Techniques for solving these include the inverse scattering transform and the method of Lax pairs, the Yang-Baxter equation and quantum groups.  The solution of these models has given insights into the nature of phase transitions, magnetization and scaling behaviour, as well as insights into the nature of quantum field theory.  Physical lattice models frequently occur as an approximation to a continuum theory, either to give an ultraviolet cutoff to the theory to prevent divergences or to perform numerical computations.  An example of a continuum theory that is widely studied by lattice models is the QCD lattice model, a discretization of quantum chromodynamics.  However, digital physics considers nature fundamentally discrete at the Planck scale, which imposes , aka Holographic principle.  More generally, lattice gauge theory and lattice field theory are areas of study.  Lattice models are also used to simulate the structure and dynamics of polymers.  Examples include the bond fluctuation model and the 2nd model.

Papá a toda madre: Papá a toda madre is an upcoming Mexican telenovela produced by Eduardo Meza for Televisa.  It is an original story of Pedro Armando Rodríguez in collaboration with Alejandra Romero and Humberto Robles.  The production of the series is scheduled for August 14, 2017.  The trailer for the telenovela was presented by Univision for the 2017-2018 television season.  It stars Sebastián Rulli and Maite Perroni.

Dreams of Childhood: Dreams of Childhood is a spoken word album by American indie folk musician Mark Kozelek and Argentine actor Nicolás Pauls.  Executive produced by Pauls, the album features eleven poems written by Argentine street kids, translated by Pauls, Federico Novik, Pablo Cubarle and Catalina Moran.  Proceeds from the album will be donated to La Casa de la Cultura de la Calla, an Argentine non-profit organization for homeless children.

Toda oscillator: In physics, the Toda oscillator is a special kind of nonlinear oscillator.  It represents a chain of particles with exponential potential interaction between neighbors.  These concepts are named after Morikazu Toda.  The Toda oscillator is used as a simple model to understand the phenomenon of self-pulsation, which is a quasi-periodic pulsation of the output intensity of a solid-state laser in the transient regime.

Los Problemas de papá: Los Problemas de papá is a 1954 Argentine film.

Question: What Argentine actor and model stars in Papá a toda madre?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The full name of the actor."
    },
    "nationality": {
      "type": "string",
      "description": "The nationality of the actor."
    },
    "professions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of professions held by the actor."
    },
    "starred_in_production": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the production the actor starred in."
        },
        "type": {
          "type": "string",
          "description": "The type of the production (e.g., telenovela, film)."
        }
      },
      "required": [
        "title",
        "type"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actor_name",
    "nationality",
    "professions",
    "starred_in_production"
  ],
  "additionalProperties": false
}
