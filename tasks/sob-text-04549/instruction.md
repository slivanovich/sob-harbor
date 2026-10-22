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
Austin Young: Austin Young (born April 12, 1966) is an American photographer, film maker and new media artist currently based in Los Angeles.  His work has created an encyclopedic documentation of sub and trans culture in New York, Los Angeles and San Francisco.  Young's photographs have been featured in major publications such as Interview magazine, OK, and Flaunt and have been shown in solo exhibitions and projects at LACMA (Los Angeles, CA), Machine Project (Los Angeles, CA), Hammer Museum (Los Angeles, CA), Berkeley Art Museum (Berkeley, California); and as well as groups shows at Los Angeles Contemporary Exhibitions (Los Angeles, CA) and Stephen Cohen Gallery (Los Angeles, CA).  In addition to photography and film making, Young is co-founder of Fallen Fruit, an art collective who use fruit as a common denominator for public engagement and collaboration.

Cars (franchise): Cars is a CGI-animated film series and Disney media franchise set in a world populated by anthropomorphic vehicles created by John Lasseter.  The franchise began with the 2006 film, ""Cars", produced by Pixar and released by Walt Disney Pictures.  The film was followed by a sequel in 2011.  A third film was released in 2017.  DisneyToon Studios produced the spin-off films "Planes" (2013) and "" (2014).

S-Series of ILS specifications: The S-Series of ILS specifications is a common denominator for a set of specifications associated to different integrated logistics support aspects.  Originally developed by AECMA (French acronym for the Association Européenne des Constructeurs de Matériel Aeronautique, later ASD), the S-Series suite of ILS specifications is managed currently jointly by multinational teams from the Aerospace and Defence Industries Association of Europe (ASD) and Aerospace Industries Association (AIA) reporting to the AIA/ASD ILS Council.  The ILS Council established the term S-Series (of) ILS specifications as the common denominator for all its specifications, and this term was consolidated with the publication of SX000i.

Thomas Forrest (colonist): Thomas Forrest, Esq, also known as Thomas Forrest, Gentleman, in the Jamestown Colonists historic lists (May 1572 in Morborne, Huntingdonshire, England – 1641 in St. Mary's City, Maryland), was a gentleman financier in the Virginia Company.  At that time, "gentleman" denoted a man of the lowest rank of the English gentry, standing below an esquire and above a yeoman.  By definition, this category included the younger sons of the younger sons of peers, knights, and esquires in perpetual succession; thus the term captures the common denominator of gentility (and often armigerousness) shared by both constituents of the English aristocracy: the peerage and the gentry.

Lowest common denominator: In mathematics, the lowest common denominator or least common denominator (abbreviated LCD) is the least common multiple of the denominators of a set of fractions.  It simplifies adding, subtracting, and comparing fractions.

Shaharit (NPO): Shaharit – Creating Common Cause is an Israeli think tank and nonprofit organization, which was founded as a "think- and do- tank" in 2012 to forge a new social partnership between all segments of Israeli society and create a new common denominator by transcending the hackneyed dichotomies between Right and Left, Jewish and Arabs, religious and secular, Mizrahim and Ashkenazim, etc.  Shaharit's overarching goal is to "forge common ground between all the groups in Israeli society thereby creating a sustainable future that allows everyone to thrive."  The organization is active on several fronts in parallel—local civic groups, an intellectual think tank, and building working groups within and between the various communities that make up Israeli society.

G4 nations: The G4 nations comprising Brazil, Germany, India, and Japan are four countries which support each other’s bids for permanent seats on the United Nations Security Council.  Unlike the G7, where the common denominator is the economy and long-term political motives, the G4's primary aim is the permanent member seats on the Security Council.  Each of these four countries have figured among the elected non-permanent members of the council since the UN's establishment.  Their economic and political influence has grown significantly in the last decades, reaching a scope comparable to the permanent members (P5).  However, the G4's bids are often opposed by the Uniting for Consensus movement, and particularly their economic competitors or political rivals.

Integrated stress response: Integrated Stress Response (ISR) is a cellular stress response common to all eukaryotes. ISR is a common denominator of different types of cellular stresses resulting in activation of at least one of the eIF-2 alpha (EIF2S1).

Joint decision trap: The joint decision trap was identified by the political scientist, Fritz W. Scharpf in a 1988 scholarly article, It is understood to be a situation in which there is a tendency for government decisions to be taken at the lowest common denominator in situations where the decision-makers have the ability to veto the proposals.  It is a common challenge for federal governments such as Germany and the European Union.

Planes (film): Planes is a 2013 American 3D computer-animated sports comedy film produced by DisneyToon Studios and released by Walt Disney Pictures.  It is a spin-off of Pixar's "Cars" franchise and the first film in a planned "Planes" trilogy.  Despite not being produced by Pixar, the film was co-written and executive produced by Pixar and Walt Disney Animation Studios' chief creative officer John Lasseter, who directed the first two "Cars" films.  The film stars the voices of Dane Cook, Stacy Keach, Priyanka Chopra, Brad Garrett, Teri Hatcher, Danny Mann, Julia Louis-Dreyfus, Roger Craig Smith, John Cleese, Carlos Alazraqui, Val Kilmer, and Anthony Edwards.

Question: What writer is the common denominator for both Disney films, cars and planes?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_franchise_name": {
      "type": "string",
      "description": "The name of the main film franchise."
    },
    "spin_off_film_name": {
      "type": "string",
      "description": "The name of the spin-off film."
    },
    "common_denominator_person": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person who is the common denominator."
        },
        "roles_in_cars": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Roles of the person in the Cars franchise."
        },
        "roles_in_planes": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Roles of the person in the Planes film."
        }
      },
      "required": [
        "name",
        "roles_in_cars",
        "roles_in_planes"
      ],
      "additionalProperties": false
    },
    "relationship_description": {
      "type": "string",
      "description": "A description of the relationship between the person and the films."
    }
  },
  "required": [
    "film_franchise_name",
    "spin_off_film_name",
    "common_denominator_person",
    "relationship_description"
  ],
  "additionalProperties": false
}
