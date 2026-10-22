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
Todd J. Leach: Todd J. Leach, PhD is an American administrator and the Chancellor of the University System of New Hampshire, which consists of University of New Hampshire, Plymouth State University, Keene State College, and Granite State College.

Granite State Communications: Granite State Communications is a telecommunications company based in Weare, New Hampshire providing telephone, internet, fiber, and television services to seven towns across the southern part of the state.

Stephen Reno: Stephen J. Reno was Chancellor of the University System of New Hampshire from 2000 to 2009.  The university system comprises four institutions, the University of New Hampshire, Keene State College, Plymouth State University, and Granite State College.  Is currently the Executive Director of Leadership New Hampshire, a leadership development program created to “increase civic engagement and strengthen communities through connecting and educating a diverse pool of engaged or emerging leaders about the state of New Hampshire.”

Granite State College: Granite State College is an institution of the University System of New Hampshire whose mission is to expand access to public higher education to students of all ages in the US state of New Hampshire.

Granite State Credit Union: Granite State Credit Union (GSCU) is a state-chartered credit union based in Manchester, New Hampshire, with branches throughout the state.

Granite State: Granite State is the nickname of the U.S. state of New Hampshire.

Granite State Electric Company: Granite State Electric Company is a regulated company that provides electricity in parts of the American state of New Hampshire.  Since 2012, it has been owned by Liberty Utilities.  The company is headquartered in Salem, New Hampshire.

University System of New Hampshire: The University System of New Hampshire (USNH), established in 1963, is responsible for overseeing the University of New Hampshire, Plymouth State University, Keene State College, and Granite State College.  The University System is the largest provider of post-secondary education in New Hampshire.  The university system is governed by a single Board of Trustees (BOT) which is responsible for ensuring that each institution has a unique character and educational mission.

Weare, New Hampshire: Weare is a town in Hillsborough County, New Hampshire, United States.  The population was 8,785 at the 2010 census.  It is close to two important New Hampshire cities, Manchester and Concord.

State Security Department of Lithuania: The State Security Department or VSD (Lithuanian: "Valstybės saugumo departamentas" ) is a Lithuanian national security agency which collects information on threats to Lithuania's sovereignty and works to eliminate those threats.  The VSD also conducts counterintelligence, protects state secrets and classified information, and vets applicants for residence in or entry to Lithuania.  The department was established on 26 March 1990, two weeks after Lithuania declared independence from the Soviet Union.  At the time, the department was also responsible for certain aspects of law enforcement, provide protection to state officials and strategic objects, ensure integrity of state communications network, investigate political corruption.  Other agencies took over these extra duties and, during 2010, the mission of VSD was clarified to mainly focus on intelligence and counterintelligence.

Question: Granite State Communications is based in what county?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "company_name": {
      "type": "string",
      "description": "The name of the company."
    },
    "company_type": {
      "type": "string",
      "description": "The type of company or industry it belongs to."
    },
    "base_location": {
      "type": "object",
      "properties": {
        "town": {
          "type": "string",
          "description": "The town where the company is based."
        },
        "county": {
          "type": "string",
          "description": "The county where the company is based."
        },
        "state": {
          "type": "string",
          "description": "The state where the company is based."
        }
      },
      "required": [
        "town",
        "county",
        "state"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "company_name",
    "company_type",
    "base_location"
  ],
  "additionalProperties": false
}
