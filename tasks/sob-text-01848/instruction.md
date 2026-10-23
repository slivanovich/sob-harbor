{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMir: Mir (Russian: Мир , ] ; lit.  \"peace\" or \"world\") was a space station that operated in low Earth orbit from 1986 to 2001, operated by the Soviet Union and later by Russia.  \"Mir\" was the first modular space station and was assembled in orbit from 1986 to 1996.  It had a greater mass than any previous spacecraft.  At the time it was the largest artificial satellite in orbit, succeeded by the International Space Station after Mir's orbit decayed.  The station served as a microgravity research laboratory in which crews conducted experiments in biology, human biology, physics, astronomy, meteorology and spacecraft systems with a goal of developing technologies required for permanent occupation of space.\n\nMars cycler: A Mars cycler (or Earth–Mars cycler) is a special kind of spacecraft trajectory that encounters Earth and Mars on a regular basis.  The term Mars cycler may also refer to a spacecraft on a Mars cycler trajectory.  The Aldrin cycler is an example of a Mars cycler.\n\nPluto Kuiper Express: Pluto Kuiper Express was an interplanetary space probe that was proposed by Jet Propulsion Laboratory (JPL) scientists and engineers and under development by NASA.  The spacecraft was intended to be launched to study Pluto and its moon Charon, along with one or more other Kuiper belt objects (KBOs).  The proposal was the third of its kind, after the \"Pluto 350\" and a proposal to send a \"Mariner Mark II\" spacecraft to Pluto.\n\nMagnetometer (Juno): Magnetometer (MAG) is the name of an instrument suite on the \"Juno\" orbiter for planet Jupiter.  The MAG instrument includes both the Fluxgate Magnetometer (FGM) and Advanced Stellar Compass (ASC) instruments.  There two sets of MAG instrument suites, and they are both positioned on the far end of on three solar panel array booms.  Each MAG instrument suite observes the same swath of Jupiter, and by having two sets of instruments, determining what signal is from the planet and what is from spacecraft is supported.  Avoiding signals from the spacecraft is another reason MAG is placed at the end of the solar panel boom, about 10 m (33 feet) and 12 m (39 feet) away from the central body of the Juno spacecraft.  The MAG instrument is designed to detect the magnetic field of Jupiter, which is one of the largest structures in the Solar System.  If one could see Jupiter's magnetic field from Earth, it would appear five times larger than the full moon in the sky despite being nearly 1700 times farther away.  Jupiter's internal magnetic field prevents the solar wind, a stream of ionized particles emitted by the Sun, from interacting directly with its atmosphere, and instead diverts it away from the planet, effectively creating a cavity in the solar wind flow, called a magnetosphere, composed of a plasma different from that of the solar wind.\n\nAstron (spacecraft): Astron was a Soviet spacecraft launched on 23 March 1983 at 12:45:06 UTC, using Proton launcher, which was designed to fulfill an astrophysics mission.  It was based on the 4MV spacecraft design and was operational for six years as the largest ultraviolet space telescope during its lifetime.  The project was headed by Alexandr Boyarchuk.\n\nDOME Microserver / MicroDataCenter: DOME is a Dutch government-funded project between IBM and ASTRON in form of a public-private-partnership to develop technology roadmaps targeting the Square Kilometer Array (SKA), the world's largest planned radio telescope.  It will be built in Australia and South Africa during the late 2010s and early 2020s.  One of the 7 DOME projects is MicroDataCenter (previously called Microservers) that are small, inexpensive and computationally efficient.\n\nAryabhata (satellite): Aryabhata (Hindi: आर्यभट) was India's first satellite, named after an Indian astronomer of the same name.\n\nUSA-202: USA 202, previously NRO Launch 26 or NROL-26, is a classified spacecraft which is operated by the United States National Reconnaissance Office.  It is an Advanced Orion ELINT satellite.  According to Aviation Week it, \"Fundamentally involves America's biggest, most secret and expensive military spacecraft on board the world's largest rocket.\"  The combined cost of the spacecraft and launch vehicle has been estimated to be over US$2 billion.\n\nDOME project: DOME is a Dutch government-funded project between IBM and ASTRON in form of a public-private-partnership focussing on the Square Kilometre Array (SKA), the world's largest planned radio telescope.  SKA will be built in Australia and South Africa.  The DOME project objective is technology roadmap development that applies both to SKA and IBM.  The 5-year project was started in 2012 and is co-funded by the Dutch government and IBM Research in Zürich, Switzerland.\n\nMitsubishi Astron engine: The Mitsubishi Astron or 4G5 engine, is a series of straight-four internal combustion engines first built by Mitsubishi Motors in 1972.  Engine displacement ranged from 1.8 to 2.6 litres, making it one of the largest four-cylinder engines of its time.  It became the first Japanese production engine to combine both electronic fuel injection (EFI) and turbocharging.\n\nQuestion: Which spacecraft was the largest of its kind, Aryabhata or Astron?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"spacecraft_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the spacecraft that was the largest of its kind.\"\n    },\n    \"was_largest_of_kind\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates whether the spacecraft was indeed the largest of its specified kind.\"\n    },\n    \"largest_category\": {\n      \"type\": \"string\",\n      \"description\": \"The specific category or type of spacecraft in which it was considered the largest.\"\n    },\n    \"largest_context\": {\n      \"type\": \"string\",\n      \"description\": \"The context or timeframe during which the spacecraft held the title of 'largest'.\"\n    }\n  },\n  \"required\": [\n    \"spacecraft_name\",\n    \"was_largest_of_kind\",\n    \"largest_category\",\n    \"largest_context\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "spacecraft_name": {
        "type": "string",
        "description": "The name of the spacecraft that was the largest of its kind."
      },
      "was_largest_of_kind": {
        "type": "boolean",
        "description": "Indicates whether the spacecraft was indeed the largest of its specified kind."
      },
      "largest_category": {
        "type": "string",
        "description": "The specific category or type of spacecraft in which it was considered the largest."
      },
      "largest_context": {
        "type": "string",
        "description": "The context or timeframe during which the spacecraft held the title of 'largest'."
      }
    },
    "required": [
      "spacecraft_name",
      "was_largest_of_kind",
      "largest_category",
      "largest_context"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
