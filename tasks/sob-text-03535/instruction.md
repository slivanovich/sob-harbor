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
F.C. Copenhagen: Football Club Copenhagen (Danish: "Football Club København" , ] ), commonly known as FC København, FC Copenhagen, Copenhagen or simply FCK, is a professional Danish football club in Copenhagen, Denmark.  FCK was founded in 1992 through the merger of Kjøbenhavns Boldklub and Boldklubben 1903.

Da Vinci Surgical System: The da Vinci Surgical System is a robotic surgical system made by the American company Intuitive Surgical.  Approved by the Food and Drug Administration (FDA) in 2000, it is designed to facilitate complex surgery using a minimally invasive approach, and is controlled by a surgeon from a console.  The system is commonly used for prostatectomies, and increasingly for cardiac valve repair and gynecologic surgical procedures.  According to the manufacturer, the da Vinci System is called "da Vinci" in part because Leonardo da Vinci's "study of human anatomy eventually led to the design of the first known robot in history."

Xavier Huillard: Xavier Huillard (born 27 June 1954) is a French business executive and the current CEO of Vinci SA.  He has held the position since 2006, he also served as chairman of the board since 2010.  He has been employed with Vinci since March 1998, as Deputy General Manager, Chairman of Vinci Construction, and Chairman of Vinci Energies.  Prior to joining Vinci, he was chairman and CEO of Sogea.  He has been the chairman of the Institut de l’Entreprise since 2011.  He graduated from École Polytechnique and École des ponts ParisTech.

Vinci (board game): Vinci is a board game designed by Philippe Keyaerts.  It resembles a diceless variant of "Risk" with variable special abilities and an original decline mechanic, and is also similar in some ways to "History of the World".  The game's name, pronounced "Vinchi", means "to be conquered" in Latin.  In 2009, the game's mechanics were re-implemented with several changes and a fantasy-oriented theme as "Small World", also credited to Keyaerts, and published by Days of Wonder.

Via Vinci Academy: The Via Vinci University, short for “the International University for Creative Leadership and Entrepreneurship”, was intended as an international, Netherlands based private university.  The name was used in 2000, it now operates under the name of Via Vinci Academy after scrutiny from the Dutch government.  It starting using the name in 2007 when the parent institutes IMAGO Group and the International University of Entrepreneurship merged.  The name “Via Vinci” refers to "the way" of Leonardo da Vinci, the icon of universal, innovative and creative strength.

Ajax København: Ajax København is a handball club based in northern Copenhagen, Denmark, consisting of both a women's and a men's team.  As of the 2017-18 season, the women's team compete in Primo Tours Ligaen, the highest women's league in Denmark, whereas the men's team compete in the 1st Division.  Ajax København play their home matches in Bavnehøj-Hallen.

København (board game): København is a board game by the company We Are Sailing.

Iørn Uldbjerg: Iørn Peter Uldbjerg (born February 1, 1968) is a retired Danish football (soccer) player, who most prominently won the 1993 Danish football championship with FC København.  He began his senior career at Tårnby Boldklub and played six games for the Denmark national under-21 football team in 1988, before signing a professional contract with B 1903.  He started playing for FC København when the club was founded in 1992, and after leaving the club in 1998, he ended his career at Herfølge BK and Farum BK.

Mediehuset København: Mediehuset København (Mediahouse Copenhagen) is a media production company located in Copenhagen, Denmark.  The company's core business is production of content for all digital media platforms such as television, corporate websites, DVD / Blu-ray and social media: Facebook, YouTube, Google +, LinkedIn and Twitter.  Mediehuset Copenhagen has also worked as a broadcast company for many television stations in Denmark - including Kanal København and Kanal Hovedstaden.

Lucan portrait of Leonardo da Vinci: The Lucan portrait of Leonardo da Vinci is a late 15th or early 16th century portrait of a man that was recently discovered in a cupboard of a private house in Italy.  It strongly resembles a portrait of Leonardo da Vinci held by the Uffizi Gallery and regarded by experts as a forgery.  The painting was previously thought by its owners to represent Galileo but on its discovery in 2008 a claim was made that it is a self-portrait by Leonardo da Vinci.  Alessandro Vezzosi, director of the Museo Ideale Leonardo da Vinci at Vinci said in 2011 that he had excluded the possibility that it was a self-portrait, but that the painting "remains intriguing because it adds a new element to the Leonardo puzzle".

Question: København and Vinci are both what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "common_category": {
      "type": "string",
      "description": "The common category that both entities belong to."
    },
    "entities": {
      "type": "array",
      "description": "List of entities mentioned in the question.",
      "items": {
        "type": "string"
      }
    },
    "entity_details": {
      "type": "array",
      "description": "Details for each entity, including its name and type.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the entity."
          },
          "type": {
            "type": "string",
            "description": "The type or category of the entity."
          }
        },
        "required": [
          "name",
          "type"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "common_category",
    "entities",
    "entity_details"
  ],
  "additionalProperties": false
}
