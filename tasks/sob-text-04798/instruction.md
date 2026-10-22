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
Laminar Flow (album): Laminar Flow is the twenty-first album by Roy Orbison recorded at Wishbone Recording Studio in Muscle Shoals, Alabama and released in 1979 on the Asylum Records label.  It was the last album of new material Orbison would release in his lifetime - his next studio effort, "", featured re-recordings of old Orbison hits whilst "Mystery Girl" and "King Of Hearts", his final collections of all-new material, were released posthumously.

Al-Salam Hospital: Al Salam Hospital or Hopital de la paix (Arabic: مستشفى السلام طرابلس‎ ‎ ) founded in 1996, is a private hospital located in Tripoli, Lebanon and has a trauma center, an angiology unit with interventional radiology available, a stroke unit, a cardiovascular and abdominal vascular unit, a dermatology unit, a plastic surgery unit, a large burn center with laminar flow, a polysomnography unit and a new intensive care unit with laminar flow.

Segré–Silberberg effect: The Segré–Silberberg effect is a fluid dynamic separation effect where a dilute suspension of neutrally buoyant particles flowing (in laminar flow) in a tube equilibrates at a distance of 0.6R from the tube's centre.  This effect was first observed by Segré and Silberberg.  The solid particles are subjected to both viscous drag forces and inertial lift forces.  The drag forces are responsible for driving particles along the ﬂow streamlines, whereas the inertial forces are responsible for the lateral migration of particles across the ﬂow streamlines.  The parabolic nature of the laminar velocity proﬁle in Poiseuille ﬂow produces a shear-induced inertial lift force that drives particles towards the channel walls.  As particles migrate closer to the channel walls, the flow around the particle induces a pressure increase between the particle and the wall which prevents particles of moving closer.  The opposing lift forces are dependent on the particle diameter to channel diameter

HKS-1: The HKS-1 was a German 19 19 m span high performance two seat sailplane, designed around 1950 to use recent advances in laminar flow airfoils. To avoid premature transition from laminar flow caused by surface interruptions, the HKS-1 dispensed with hinged ailerons, flaps and spoilers and replaced them with a flexible trailing edge.  Two were built, setting several records.

Mystery Girl: Mystery Girl is the twenty-second album by Roy Orbison, the last album recorded whle he was alive and posthumously released on the Virgin label in 1989.  The album became a hit worldwide, reaching #5 on the US "Billboard" 200, and #2 on the UK Albums Chart.

Laminar flow reactor: A laminar flow reactor (LFR) is a type of chemical reactor that uses laminar flow to control reaction rate, and/or reaction distribution.  LFR is generally a long tube with constant diameter that is kept at constant temperature.  Reactants are injected at one end and products are collected and monitored at the other.  Laminar flow reactors are often used to study an isolated elementary reaction or multi-step reaction mechanism.

Laminar flow: In fluid dynamics, laminar flow (or streamline flow) occurs when a fluid flows in parallel layers, with no disruption between the layers.  At low velocities, the fluid tends to flow without lateral mixing, and adjacent layers slide past one another like playing cards.  There are no cross-currents perpendicular to the direction of flow, nor eddies or swirls of fluids.  In laminar flow, the motion of the particles of the fluid is very orderly with particles close to a solid surface moving in straight lines parallel to that surface.

Oscillatory baffled reactor: A Continuous Oscillatory Baffled Reactor (COBR) is a specially designed reactor to achieve plug flow under laminar flow conditions.  Achieving plug flow has previously been limited to either a large number of continuous stir tank reactors (CSTR) in series or conditions with high turbulent flow.  The technology incorporates annular baffles to a tubular reactor framework to create eddies when liquid is pushed up through the tube.  Likewise, when liquid is on a downstroke through the tube, eddies are created on the other side of the baffles.  Eddy generation on both sides of the baffles creates very effective mixing while still maintaining plug flow.  By using COBR, potentially higher yields of product can be made with greater control and reduced waste.

Kozeny–Carman equation: The Kozeny–Carman equation (or Carman–Kozeny equation) is a relation used in the field of fluid dynamics to calculate the pressure drop of a fluid flowing through a packed bed of solids.  It is named after Josef Kozeny and Philip C. Carman.  The equation is only valid for laminar flow.  The equation was derived by Kozeny and Carman (see ) from a starting point of (a) modelling fluid flow in a packed bed as laminar fluid flow in a collection of curving passages/tubes crossing the packed bed and (b) Poiseuille's law describing laminar fluid flow in straight, circular section pipes.

Laminar flow cabinet: A laminar flow cabinet or laminar flow closet or tissue culture hood is a carefully enclosed bench designed to prevent contamination of semiconductor wafers, biological samples, or any particle sensitive materials.  Air is drawn through a HEPA filter and blown in a very smooth, laminar flow towards the user.  The cabinet is usually made of stainless steel with no gaps or joints where spores might collect.

Question: Who is the artist that created the albums Laminar Flow and Mystery Girl?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "artist_name": {
      "type": "string",
      "description": "The name of the artist who created the albums."
    },
    "albums_created": {
      "type": "array",
      "description": "A list of albums created by the artist mentioned in the context.",
      "items": {
        "type": "object",
        "properties": {
          "album_title": {
            "type": "string",
            "description": "The title of the album."
          },
          "album_sequence_number": {
            "type": "integer",
            "description": "The sequence number of the album in the artist's discography."
          }
        },
        "required": [
          "album_title",
          "album_sequence_number"
        ],
        "additionalProperties": false
      }
    },
    "number_of_albums_found": {
      "type": "integer",
      "description": "The total count of albums by the artist found in the context that match the query."
    }
  },
  "required": [
    "artist_name",
    "albums_created",
    "number_of_albums_found"
  ],
  "additionalProperties": false
}
