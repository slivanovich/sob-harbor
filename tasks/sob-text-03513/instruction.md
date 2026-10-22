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
Hospital for Tropical Diseases: The Hospital for Tropical Diseases (HTD) is a specialist tropical disease hospital located in London, United Kingdom.  It is part of the University College London Hospitals NHS Foundation Trust and is closely associated with University College London and the London School of Hygiene & Tropical Medicine.  It is the only NHS hospital dedicated to the prevention, diagnosis and treatment of tropical diseases and travel-related infections.  In addition to specialists in major tropical diseases such as Malaria, Leprosy and tuberculosis.  It also provides an infectious disease treatment service for UCLH.

Alok Bhattacharya: Alok Bhattacharya (born 1951) is an Indian parasitologist, academic and a professor at the School of Life Sciences of the Jawaharlal Nehru University.  He chairs the "Biotechnology Information System Network" (BITSNET) as well as the Life Sciences Expert Committee of "FIST program" of the Department of Science and Technology (DST).  He is an elected fellow of the Indian Academy of Sciences and the Indian National Science Academy and is known for his studies on Entamoeba histolytica and "species-specific calcium binding protein and its gene".  The Council of Scientific and Industrial Research, the apex agency of the Government of India for scientific research, awarded him the Shanti Swarup Bhatnagar Prize for Science and Technology, one of the highest Indian science awards, in 1994, for his contributions to biological sciences.

Sickle-cell disease: Sickle-cell disease (SCD) is a group of blood disorders typically inherited from a person's parents.  The most common type is known as sickle-cell anaemia (SCA).  It results in an abnormality in the oxygen-carrying protein haemoglobin (hemoglobin S) found in red blood cells.  This leads to a rigid, sickle-like shape under certain circumstances.  Problems in sickle cell disease typically begin around 5 to 6 months of age.  A number of health problems may develop, such as attacks of pain ("sickle-cell crisis"), anemia, swelling in the hands and feet, bacterial infections, and stroke.  Long term pain may develop as people get older.  The average life expectancy in the developed world is 40 to 60 years.

Alimuddin Zumla: Sir Alimuddin Zumla KBE, PhD, FRCP, FRCPath, FRSB (born 15 May 1955) is a British Zambian professor of infectious diseases and international health at University College London Medical School.  He specialises in infectious and tropical diseases, clinical immunology, and internal medicine, with a special interest in HIV/AIDS, respiratory infections, and diseases of poverty.  He is internationally renowned for his extensive outputs and leadership of infectious/tropical diseases research and capacity development activities.

Eli Schwartz: Eliezer (Eli) Schwartz (Hebrew: אליעזר שוורץ, born in Jerusalem, Israel) MD, DTMH is an Israeli physician, known for his speciality in tropical diseases and travel medicine.  He is a founding member of the International Society of Travel Medicine (ISTM) and served as chair of its Professional Education Committee.  Schwartz is currently president of the Asia Pacific Travel Health Society (APTHS) as well as the Israel Society for Parasitology, Protozoology and Tropical Diseases (ISPPTD).  At clinical practice, he is head of the Center for Travel Medicine and Tropical Diseases at the Sheba Medical Center.  He is also a Proffessor at the Sackler Faculty of Medicine, Tel Aviv University.

PLOS Neglected Tropical Diseases: PLOS Neglected Tropical Diseases is a peer-reviewed open access scientific journal devoted to the study of neglected tropical diseases, including helminth, bacterial, viral, protozoan, and fungal infections endemic to tropical regions.  "PLOS Neglected Tropical Diseases" is abstracted and indexed in PubMed and the Web of Science.  It is the seventh and youngest member of the Public Library of Science family of open access journals.

Chukwuedu Nwokolo: Chukwuedu Nathaniel II Nwokolo (19 April 1921 – 18 May 2014) was an internationally distinguished tropical diseases, nutrition, human, medical, biological and life sciences expert; plus research scientist, scholar, pioneer medical doctor, author, humanitarian and acclaimed professor of medicine.  He was Nigerian, and is listed in the "Who's Who in Nigeria" series by Newswatch.  Nwokolo was outstandingly recognised worldwide for discovering and mapping out the area of paragonimiasis lung disease in Eastern Nigeria, with a study of the disease in Africa and clinical research for its control.  Nwokolo founded SICREP: Sickle Cell Research Programme to effectively fight the disease in Nigeria and globally.

Naval Medical Research Unit One: Naval Medical Research Unit One was a research laboratory of the US Navy which was founded as Naval Laboratory Research Unit 1, a Naval Reserve Unit at the University of California Berkeley in the life sciences building in 1934 after a campaign by a Berkeley scientist Albert P. Krueger to the Bureau of Medicine and Surgery to have a laboratory to study and prevent influenza and respiratory infections in naval forces.  It was mobilized as an active duty naval unit in 1941 to study the epidemiological impact of diseases such as influenza, meningitis, and catarrhal fever, as well as tropical diseases such as malaria on the US Navy during World War II.

Eating disorders and development: Eating disorders typically peak at specific periods in development, notably sensitive and transitional periods such as puberty.  Feeding and eating disorders in childhood are often the result of a complex interplay of organic and non-organic factors.  Medical conditions, developmental problems and temperament are all strongly correlated with feeding disorders, but important contextual features of the environment and parental behavior have also been found to influence the development of childhood eating disorders.  Given the complexity of early childhood eating problems, consideration of both biological and behavioral factors is warranted for diagnosis and treatment.

Biofluid dynamics: Bio-Fluid Dynamics, may be considered as the discipline of biological engineering or biomedical engineering in which the fundamental principles of fluid dynamics are used to explain the mechanisms of biological flows and their interrelationships with physiological processes, in health and in diseases/disorder.  It can be considered as the conjuncture of mechanical engineering and biological engineering.  It spans from cells to organs, covering diverse aspects of functionality of systemic physiology, including cardiovascular, respiratory, reproductive, urinary, musculoskeletal and neurological systems etc.  Bio fluid dynamics and its simulations through computational fluid dynamics (CFD) apply to both internal as well as external flows.  Internal flows such as cardiovascular blood flow and respiratory airflow, and external flows such as flying and aquatic locomotion (i.e., swimming).  Biological fluid Dynamics (or Bio fluid Dynamics) involves the study of the motion of biological fluids (e.g. blood flow in arteries, animal flight, fish swimming, etc.).  It can be either circulatory system or respiratory systems.  Understanding the circulatory system is one of the major areas of research .  The respiratory system is very closely linked to the circulatory system and is very complex to study and understand.  The study of Bio fluid Dynamics is also directed towards finding solutions to some of the human body related diseases and disorders.  The usefulness of the subject can also be understood by seeing the use of Bio fluid Dynamics in the areas of physiology in order to explain how living things work and about their motions, in developing an understanding of the origins and development of various diseases related to human body and diagnosing them, in finding the cure for the diseases related to cardiovascular and pulmonary systems.

Question: What internationally distinguished tropical diseases, nutrition, human, medical, biological and life sciences expert found a way to fight a group of blood disorders typically inherited from a person's parents?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "expert_name": {
      "type": "string",
      "description": "The full name of the internationally distinguished expert."
    },
    "expertise_areas": {
      "type": "array",
      "description": "A list of the expert's primary fields of expertise.",
      "items": {
        "type": "string"
      }
    },
    "disease_targeted": {
      "type": "object",
      "description": "Details about the group of blood disorders the expert worked to fight.",
      "properties": {
        "name": {
          "type": "string",
          "description": "The common name of the disease group."
        },
        "category": {
          "type": "string",
          "description": "The general category of the disease (e.g., blood disorder)."
        },
        "inheritance_pattern": {
          "type": "string",
          "description": "How the disease is typically inherited."
        }
      },
      "required": [
        "name",
        "category",
        "inheritance_pattern"
      ],
      "additionalProperties": false
    },
    "program_founded": {
      "type": "object",
      "description": "Information about the program or initiative founded by the expert to combat the disease.",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the program or initiative."
        },
        "purpose": {
          "type": "string",
          "description": "The stated purpose of the program."
        }
      },
      "required": [
        "name",
        "purpose"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "expert_name",
    "expertise_areas",
    "disease_targeted",
    "program_founded"
  ],
  "additionalProperties": false
}
