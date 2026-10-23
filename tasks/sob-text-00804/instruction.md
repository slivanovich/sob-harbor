{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nG. I. Taylor: Sir Geoffrey Ingram Taylor OM (7 March 1886 – 27 June 1975) was a British physicist and mathematician, and a major figure in fluid dynamics and wave theory.  His biographer and one-time student, George Batchelor, described him as \"one of the most notable scientists of this (the 20th) century\".\n\nPreferential concentration: Preferential concentration is the tendency of dense particles in a turbulent fluid to cluster in regions of high strain (low vorticity) due to their inertia.  The extent by which particles cluster is determined by the Stokes number, defined as formula_1, where formula_2 and formula_3 are the timescales for the particle and fluid respectively; note that formula_4 and formula_5 are the mass densities of the fluid and the particle, respectively, formula_6 is the kinematic viscosity of the fluid, and formula_7 is the kinetic energy dissipation rate of the turbulence.  Maximum preferential concentration occurs at formula_8.  Particles with formula_9 follow fluid streamlines and particles with formula_10 do not respond significantly to the fluid within the times the fluid motions are coherent.\n\nOpen information extraction: In natural language processing, open information extraction (OIE) is the task of generating a structured, machine-readable representation of the information in text, usually in the form of triples or n-ary propositions.  A proposition can be understood as truth-bearer, a textual expression of a potential fact (e.g., \"Dante wrote the Divine Comedy\"), represented in an amenable structure for computers [e.g., (\"Dante\", \"wrote\", \"Divine Comedy\")].  An OIE extraction normally consists of a relation and a set of arguments.  For instance, (\"Dante\", \"passed away in\" \"Ravenna\") is a proposition formed by the relation \"passed away in\" and the arguments \"Dante\" and \"Ravenna\".  The first argument is usually referred as the subject while the second is considered to be the object.\n\nSurface wave: In physics, a surface wave is a mechanical wave that propagates along the interface between differing media.  A common example is gravity waves along the surface of liquids, such as ocean waves.  Gravity waves can also occur within liquids, at the interface between two fluids with different densities.  Elastic surface waves can travel along the surface of solids, such as \"Rayleigh\" or \"Love\" waves.  Electromagnetic waves can also propagate as \"surface waves\" in that they can be guided along a refractive index gradient or along an interface between two media having different dielectric constants.  In radio transmission, a \"ground wave\" is a guided wave that propagates close to the surface of the Earth.\n\nCapillary length: In fluid mechanics, capillary length is a characteristic length scale for an interface between two fluids which is subject both to gravitational acceleration and to a surface force due to surface tension in the interface.\n\nViscous fingering: Viscous fingering is the formation of patterns in a morphologically unstable interface between two fluids in a porous medium or in a Hele-Shaw cell.  It occurs when a less viscous fluid is injected displacing a more viscous one (in the inverse situation, with the more viscous displacing the other, the interface is stable and no patterns form).  It can also occur driven by gravity (without injection) if the interface is horizontal separating two fluids of different densities, being the heavier one above the other.  In the rectangular configuration the system evolves until a single finger (the Saffman–Taylor finger) forms.  In the radial configuration the pattern grows forming fingers by successive tip-splitting.\n\nCharcoal lighter fluid: Charcoal lighter fluid is a volatile fluid used to accelerate the ignition of charcoal in a barbecue grill.  It can either be petroleum based (e.g., mineral spirits) or alcohol based (usually methanol or ethanol).  It can be used both with lump charcoal and briquettes.  Lighter-fluid infused briquettes, that eliminate the need for separate application of lighter fluid, are available.  The use of lighter fluid is somewhat controversial as the substance is combustible, harmful or fatal if swallowed, and may impart an unpleasant flavor to food cooked upon fires lit with it.  A traditional alternative to using lighter fluid is a chimney starter.\n\nKelvin–Helmholtz instability: The Kelvin–Helmholtz instability (after Lord Kelvin and Hermann von Helmholtz) can occur when there is velocity shear in a single continuous fluid, or where there is a velocity difference across the interface between two fluids.  An example is wind blowing over water: The instability manifests in waves on the water surface.  More generally, clouds, the ocean, Saturn's bands, Jupiter's Red Spot, and the sun's corona show this instability.\n\nRayleigh–Taylor instability: The Rayleigh–Taylor instability, or RT instability (after Lord Rayleigh and G. I. Taylor), is an instability of an interface between two fluids of different densities which occurs when the lighter fluid is pushing the heavier fluid.  Examples include the behavior of water suspended above oil in the gravity of Earth, mushroom clouds like those from volcanic eruptions and atmospheric nuclear explosions, supernova explosions in which expanding core gas is accelerated into denser shell gas, instabilities in plasma fusion reactors and inertial confinement fusion.\n\nRichtmyer–Meshkov instability: The Richtmyer–Meshkov instability (RMI) occurs when two fluids of different density are impulsively accelerated.  Normally this is by the passage of a shock wave.  The development of the instability begins with small amplitude perturbations which initially grow linearly with time.  This is followed by a nonlinear regime with bubbles appearing in the case of a light fluid penetrating a heavy fluid, and with spikes appearing in the case of a heavy fluid penetrating a light fluid.  A chaotic regime eventually is reached and the two fluids mix.  This instability can be considered the impulsive-acceleration limit of the Rayleigh–Taylor instability .\n\nQuestion: The relation that describes an instability of an interface between two fluids of different densities which occurs when the lighter fluid is pushing the heavier fluid is named after which British physicist who passed away in 1975?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"instability_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the fluid instability described.\"\n    },\n    \"physicist_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the physicist.\"\n        },\n        \"nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the physicist.\"\n        },\n        \"death_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the physicist passed away.\"\n        },\n        \"field_of_study\": {\n          \"type\": \"string\",\n          \"description\": \"The primary field of study of the physicist.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"nationality\",\n        \"death_year\",\n        \"field_of_study\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"instability_description\": {\n      \"type\": \"string\",\n      \"description\": \"A description of the instability from the context.\"\n    }\n  },\n  \"required\": [\n    \"instability_name\",\n    \"physicist_details\",\n    \"instability_description\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "instability_name": {
        "type": "string",
        "description": "The name of the fluid instability described."
      },
      "physicist_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the physicist."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the physicist."
          },
          "death_year": {
            "type": "integer",
            "description": "The year the physicist passed away."
          },
          "field_of_study": {
            "type": "string",
            "description": "The primary field of study of the physicist."
          }
        },
        "required": [
          "name",
          "nationality",
          "death_year",
          "field_of_study"
        ],
        "additionalProperties": false
      },
      "instability_description": {
        "type": "string",
        "description": "A description of the instability from the context."
      }
    },
    "required": [
      "instability_name",
      "physicist_details",
      "instability_description"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
