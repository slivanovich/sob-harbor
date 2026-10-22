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
Bryan Willson: Bryan Willson is a Professor of Mechanical Engineering at Colorado State University (CSU), United States, and is the director and founder of the Engines and Energy Conversion Laboratory (EECL) at CSU.  His main area of research interest involves the development of sustainable energy solutions.

Electrochemical energy conversion: Electrochemical energy conversion is a field of energy technology concerned with electrochemical methods of energy conversion including fuel cells and photoelectrochemical.  This field of technology also includes electrical storage devices like batteries and supercapacitors.  It is increasingly important in context of automotive propulsion systems.  There has been the creation of more powerful, longer running batteries allowing longer run times for electric vehicles.  These systems would include the energy conversion fuel cells and photoelectrochemical mentioned above.

Energy conversion efficiency: Energy conversion efficiency (η) is the ratio between the useful output of an energy conversion machine and the input, in energy terms.  The input, as well as the useful output may be chemical, electric power, mechanical work, light (radiation), or heat.

ETH Zurich: ETH Zurich (Swiss Federal Institute of Technology in Zurich; German: "Eidgenössische Technische Hochschule Zürich" ) is a science, technology, engineering and mathematics university in the city of Zürich, Switzerland.  Like its sister institution EPFL, it is an integral part of the Swiss Federal Institutes of Technology Domain (ETH Domain) that is directly subordinate to Switzerland's Federal Department of Economic Affairs, Education and Research.  The school was founded by the Swiss Federal Government in 1854 with the stated mission to educate engineers and scientists, serve as a national center of excellence in science and technology and provide a hub for interaction between the scientific community and industry.

Photosynthetic reaction centre: A photosynthetic reaction centre is a complex of several proteins, pigments and other co-factors that together execute the primary energy conversion reactions of photosynthesis.  Molecular excitations, either originating directly from sunlight or transferred as excitation energy via light-harvesting antenna systems, give rise to electron transfer reactions along the path of a series of protein-bound co-factors.  These co-factors are light-absorbing molecules (also named chromophores or pigments) such as chlorophyll and phaeophytin, as well as quinones.  The energy of the photon is used to excite an electron of a pigment.  The free energy created is then used to reduce a chain of nearby electron acceptors, which have subsequently higher redox-potentials.  These electron transfer steps are the initial phase of a series of energy conversion reactions, ultimately resulting in the conversion of the energy of photons to the storage of that energy by the production of chemical bonds.

John Newman (scientist): John Scott Newman (b. 17 Nov 1938) is a retired professor of the University of California and renowned battery researcher.  The university's Department of Chemical Engineering's Newman Research Group was founded by Newman and "interests of this research group include the investigation of efficient and economical methods for electrochemical energy conversion and storage, development of mathematical models to predict the behavior of electrochemical systems and to identify important process parameters, and experimental verification of the completeness and accuracy of the models".  Newman also worked for the Electrochemical Technologies Group at Lawrence Berkeley National Laboratory where he was a Faculty Senior Scientist.  He served as director of the Department of Energy’s Batteries for Advanced Transportation Technologies Program.  He was elected to the National Academy of Engineering in 1999 and was an Onsager Professor at the Norwegian University of Science and Technology in 2002.  Venkat Srinivasan has called Newman "the father of electrochemical engineering."

Thermal engineering: Thermal Engineering is a study of energy transport particularly in nanoscale structure to obtain knowledge and understanding of the scientific effects on physical world that can engineering discoveries in industrial energy applications.  The thermal engineering is heat transfer, thermodynamics, energy conversion, and HVAC applications.

Chlorophyll fluorescence: Chlorophyll fluorescence is light re-emitted by chlorophyll molecules during return from excited to non-excited states and used as indicator of photosynthetic energy conversion in higher plants, algae and bacteria.  Excited chlorophyll dissipates the absorbed light energy by driving photosynthesis (photochemical energy conversion), as heat in non-photochemical quenching or by emission as fluorescence radiation.  As these processes are complementary processes analysis of chlorophyll fluorescence is an important tool in plant research with a wide spectra of applications.

Argonne–Northwestern Solar Energy Research Center: The Argonne–Northwestern Solar Energy Research Center (ANSER Center) is a joint research program between the Argonne National Laboratory and Northwestern University.  Michael R. Wasielewski, Professor of Chemistry at Northwestern founded the ANSER center in 2007 and is its current director.  The center's goal is to develop the fundamental understanding, materials, and methods necessary to create efficient and economically viable technologies for solar fuels and electricity production.  The union of synthesis, measurement, theory, and engineering allows ANSER to create exceptional new energy conversion systems.  As part of its $777 million effort to establish Energy Frontier Research Centers, Grants provided by the US Department of Energy will enable the ANSER "to analyse photosynthesis for ways to create more efficient photovoltaic cells and create hybrid solar cells that have both organic and inorganic components."

Laboratory for Energy Conversion: The Laboratory for Energy Conversion (LEC) formerly known as Turbomachinery Laboratory (LSM) was founded in 1892 by Aurel Boleslav Stodola.  As part of the Federal Institute of Technology Zurich (ETH).  The laboratory has been headed by some of the most prominent mechanical engineers in the history of turbomachinery.

Question: The Laboratory for Energy Conversion  is part of the engineering and math university in what country?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "laboratory_info": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the laboratory."
        },
        "founding_year": {
          "type": "integer",
          "description": "The year the laboratory was founded."
        },
        "founder": {
          "type": "string",
          "description": "The founder of the laboratory."
        }
      },
      "required": [
        "name",
        "founding_year",
        "founder"
      ],
      "additionalProperties": false
    },
    "affiliated_university_info": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the university the laboratory is part of."
        },
        "city": {
          "type": "string",
          "description": "The city where the university is located."
        }
      },
      "required": [
        "name",
        "city"
      ],
      "additionalProperties": false
    },
    "country_of_university": {
      "type": "string",
      "description": "The country where the university is located."
    }
  },
  "required": [
    "laboratory_info",
    "affiliated_university_info",
    "country_of_university"
  ],
  "additionalProperties": false
}
