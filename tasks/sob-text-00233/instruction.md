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
J. Allen Hynek: Dr. Josef Allen Hynek (May 1, 1910 – April 27, 1986) was an American astronomer, professor, and ufologist.  He is perhaps best remembered for his UFO research.  Hynek acted as scientific advisor to UFO studies undertaken by the U.S. Air Force under three consecutive projects: Project Sign (1947–1949), Project Grudge (1949–1952), and Project Blue Book (1952–1969).

Sumit Bhaduri: Sumit Bhaduri (born 1948) is an Indian organometallic chemist and was a senior scientific advisor to Reliance Industries.  He is known for his studies on metal-carbonyl clusters and to the polymer-supported catalysis and is credited with the development of technology for the manufacture of Ziegler-Natta polypropylene catalyst which is in use with Reliance Industries.  He has authored a book, "Homogeneous Catalysis: Mechanisms and Industrial Applications" and is an elected fellow of the Indian National Science Academy and the Indian Academy of Sciences The Council of Scientific and Industrial Research, the apex agency of the Government of India for scientific research, awarded him the Shanti Swarup Bhatnagar Prize for Science and Technology, one of the highest Indian science awards, in 1992, for his contributions to chemical sciences.

Allan Hendry: Allan Hendry (born 1950) is an American astronomer and ufologist.  UFO historian Jerome Clark calls him "one of the most skilled investigators in the history of UFO research."  He was the main investigator for the Center for UFO Studies (CUFOS) in the 1970s.

Jill James: Sandra Jill James is an American biochemist and autism researcher who studies metabolic autism biomarkers.  She works at Arkansas Children's Hospital Research Institute, where she is the director of the Metabolic Genomics Laboratory, as well as the University of Arkansas for Medical Sciences's department of pediatrics, where she has worked since 2002.  She is also a member of the Autism Speaks Treatment Advisory Board, and is also a scientific advisor to the autism foundation N of One.  Her current research focuses on the role of epigenetics in causing autism, as well as the effectiveness of supplements as a treatment for autism and the potential existence of abnormal metabolism in autistic children.  This research is funded by a 5-year grant from the National Institutes of Health entitled "Metabolic biomarkers of autism: predictive potential and genetic susceptibility," as well as by a grant from Autism Speaks.  She is a consulting editor for the "American Journal of Clinical Nutrition".

Ornithology: Ornithology is a branch of zoology that concerns the study of birds.  The word "ornithology" derives from the ancient Greek ὄρνις "ornis" ("bird") and λόγος "logos" ("rationale" or "explanation").  Several aspects of ornithology differ from related disciplines, due partly to the high visibility and the aesthetic appeal of birds.  Most marked among these is the extent of studies undertaken by amateurs working within the parameters of strict scientific methodology.

Robin Boast: Robin Boast (born 2 March 1956) is the Professor of Information Science and Culture at the University of Amsterdam, Department of Media Studies.  Until the end of 2012 he was the Deputy Director and Curator for World Archaeology at the Museum of Archaeology and Anthropology at the University of Cambridge (MAA).  He teaches on Cultural Information Science, Neo-colonial information governance, and the history and sociology of digitally and collecting.  He has been a Visiting Professor at the European University Institute in Florence Italy, a Scientific Advisor for several EU projects, and was the Director of the Virtual Teaching Collection Project.  Dr. Boast has worked in museums in the US and Britain for over 30 years, specializing in museum access, classification and documentation, especially around diverse knowledge communities.  Through a program of historical, theoretical and practical inquiry, his research explores forms of informed, collaborative and critical access to museum spaces and collections.  Dr. Boast is currently working with many indigenous communities around the world that seek to enable and re-centre the many dimensions of local knowledge expertise within the academy – research informed by the critiques of the Sociology of Scientific Knowledge, Post-colonial studies, Indigenous Studies and collaborative developments in e-Science.  Dr. Boast has worked for several years on an international research project which subjects the museum and the academy to the ethnographic gaze of indigenous partners to de-centre the ownership and control of research of indigenous patrimony.  His most recent work has been with source community museums and heritage organizations with Dr. Ramesh Srinivasan and Mr. James Enote, primarily at the A:shiwi A:wan Museum & Heritage Center in Zuni, New Mexico (USA).

Michael D. Swords: Michael D. Swords is a retired professor of Natural Science at Western Michigan University, who writes about general sciences and anomalous phenomena, particularly parapsychology, cryptozoology, and ufology, editing the academic publication "The Journal of UFO Studies".  He is a board member of the J. Allen Hynek Center for UFO Studies.

Center for UFO Studies: The Center for UFO Studies (CUFOS) is a privately funded UFO research group.  The group was founded in 1973 by J. Allen Hynek, who at the time was the Chair of the Department of Astronomy at Northwestern University in Illinois.

UFO Investigators League: The UFO Investigators League (UFOIL) was a UFO group founded by Timothy Green Beckley in the early 1970s.  They were a member of the Coalition of Concerned Ufologists and branched into state chapters.

Gilles Saint-Paul: Gilles Saint-Paul (born 8 February 1963) is a French economist at the Toulouse 1 University Social Sciences.  He also is a scientific advisor to the Economic Studies Directorate at the French Ministry of the Environment.  His main interests include the political economy of unemployment and how information technology affects wage inequality.

Question: The Center for UFO Studies was a group founded by an American astronomer who acted as scientific advisor to UFO studies undertaken by who?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "organization_founded": {
      "type": "string",
      "description": "The name of the organization that was founded."
    },
    "founder": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the founder."
        },
        "profession": {
          "type": "string",
          "description": "The primary profession of the founder relevant to the context."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the founder."
        }
      },
      "required": [
        "name",
        "profession",
        "nationality"
      ],
      "additionalProperties": false
    },
    "advisor_role": {
      "type": "object",
      "properties": {
        "advised_entity": {
          "type": "string",
          "description": "The entity to whom the founder acted as a scientific advisor."
        },
        "area_of_advice": {
          "type": "string",
          "description": "The subject area of the scientific advice."
        },
        "related_projects": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of projects associated with the advisory role."
        }
      },
      "required": [
        "advised_entity",
        "area_of_advice",
        "related_projects"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "organization_founded",
    "founder",
    "advisor_role"
  ],
  "additionalProperties": false
}
