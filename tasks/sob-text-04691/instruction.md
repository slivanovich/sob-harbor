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
Genii (Stargate): In the fictional universe of the science fiction television series "Stargate Atlantis", the Genii are a human culture living in the Pegasus galaxy ("see also: Human civilizations in Stargate Atlantis").  Although they appear to be simple Amish-like farmers, the Genii are an advanced, militaristic society.  In the series, they have been both enemies and allies to the Atlantis Expedition.  Nevertheless, Teyla Emmagan believes that outside of Atlantis, they represent the galaxy's best hope of defeating the Wraith.

Eric Lux: Éric Lux is a Luxembourg entrepreneur and businessman.  Alongside Gerard Lopez, he is a founding partner of The Genii Group.  Lux is also the CEO and Director of Genii Capital, an investment management and financial member of The Genii Group and owner of the Lotus F1 Team.  He is also CEO of the real estate investment group Ikodomos Holding and real estate developer company Ikogest.

Cryptocarya foetida: Cryptocarya foetida is a rainforest tree growing at the eastern coastal parts of Australia.  The common name is due to the allegedly offensive odour given by the flowers.  The stinking cryptocarya or stinking laurel is considered vulnerable to extinction with a ROTAP rating of 3VC.

Acinos: Acinos is a genus of ten species of annual and short-lived evergreen perennial woody plants native to southern Europe and western Asia.  Its name comes from the Greek word "akinos", the name of a small aromatic plant.  They are small, tufted, bushy or spreading plants growing to 10-45 cm tall.  The 2-lipped, tubular flowers are in whorls borne on erect spike-like inflorescence produced in mid-summer.

Cryptocarya triplinervis: Cryptocarya triplinervis is a rainforest tree growing in eastern Australia.  Common names include the three veined laurel, three veined cryptocarya and the brown laurel.

Genii Capital: Genii Capital is an international financial advisory and investment firm, which specialises in brand management, promising technologies, motorsport and a wide spectrum of venture capitalism activities.  It was created in 2008, by two Luxembourger investors, Gerard Lopez and Eric Lux and has a particular focus on emerging markets, including the BRIC (Brazil, Russia, India and China) nations.  Genii Capital focuses on a wide range of investment vehicles and also provides advisory services on topics ranging from the preparation of an IPO, the joint development of businesses, mergers and acquisitions and capital markets.  As a result of a global restructuring initiative in 2011, Genii Capital is now located in the Finance division of The Genii Group, a global enterprise overseeing the business activities of Lux and Lopez.

Optics Software for Layout and Optimization: Optics Software for Layout and Optimization (OSLO) is an optical design program originally developed at the University of Rochester in the 1970s.  The first commercial version was produced in 1976 by Sinclair Optics.  Since then, OSLO has been rewritten several times as computer technology has advanced.  In 1993, Sinclair Optics acquired the GENII program for optical design, and many of the features of GENII are now included in OSLO.  Lambda Research Corporation (Littleton MA) purchased the program from Sinclair Optics in 2001.

Cryptocarya: Cryptocarya is a genus of evergreen trees belonging to the laurel family, Lauraceae.  The genus includes more than 350 species, distributed through the Neotropic, Afrotropic, Indomalaya, and Australasia ecozones.

Acinos arvensis: Acinos arvensis, known commonly as basil thyme and spring savory, is a species of plant of the genus "Acinos".

Cryptocarya chinensis: Cryptocarya chinensis, commonly known as the Chinese cryptocarya, is a medium-sized evergreen tree native to the subtropical forests of Taiwan, southern China (Fujian, Guangdong, Guangxi, Hainan, Sichuan), and Japan.

Question: Are Acinos and Cryptocarya both evergreen genii?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "overall_answer": {
      "type": "boolean",
      "description": "The final answer to the question: Are Acinos and Cryptocarya both evergreen genera?"
    },
    "acinos_classification": {
      "type": "object",
      "properties": {
        "is_genus": {
          "type": "boolean",
          "description": "Indicates if Acinos is classified as a genus."
        },
        "has_evergreen_species": {
          "type": "boolean",
          "description": "Indicates if the Acinos genus includes evergreen species."
        }
      },
      "required": [
        "is_genus",
        "has_evergreen_species"
      ],
      "additionalProperties": false
    },
    "cryptocarya_classification": {
      "type": "object",
      "properties": {
        "is_genus": {
          "type": "boolean",
          "description": "Indicates if Cryptocarya is classified as a genus."
        },
        "is_evergreen_genus": {
          "type": "boolean",
          "description": "Indicates if Cryptocarya is a genus of evergreen plants."
        }
      },
      "required": [
        "is_genus",
        "is_evergreen_genus"
      ],
      "additionalProperties": false
    },
    "genii_term_interpretation": {
      "type": "string",
      "description": "Explanation of how the term 'genii' in the question is interpreted based on the context."
    }
  },
  "required": [
    "overall_answer",
    "acinos_classification",
    "cryptocarya_classification",
    "genii_term_interpretation"
  ],
  "additionalProperties": false
}
