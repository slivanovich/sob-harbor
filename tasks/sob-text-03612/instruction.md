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
Lingual tonsils: The lingual tonsils are two small mounds of lymphatic tissue located at the back of the base of the tongue, one on either side.  They are composed of lymphatic tissue that functions to assist the immune system in the production of antibodies in response to invading pathogenic bacteria or viruses.

Pararenal fat: The pararenal fat (or paranephric fat or paranephric body) is collection of adipose tissue located superficial to the renal fascia.  The "perirenal fat", or adipose capsule of kidney, is deep to the renal fascia but superficial to the renal capsule.

Insulitis: Insulitis is an inflammation of the islets of Langerhans, a collection of endocrine tissue located in the pancreas.  The islets containing the pancreatic β-cells, and in some cases, the exocrine tissues, become infiltrated by T and B lymphocytes, macrophages and dendritic cells.  This innate immune cell and lymphocyte infiltration can result in destruction of the insulin producing beta cells of the islets, and clinical diabetes.  Insulitis is often studied in the multiple low dose streptozotocin (MLDS) mouse model or the non-obese diabetic (NOD) mouse model of type 1 diabetes.  The chemokine family of proteins may play a key role in promoting leukocytic infiltration into the pancreas prior to pancreatic beta-cell destruction.

Waldeyer's tonsillar ring: Waldeyer's tonsillar ring (pharyngeal lymphoid ring or Waldeyer's lymphatic ring) is an anatomical term collectively describing the annular arrangement of lymphoid tissue in the pharynx.  Waldeyer's ring circumscribes the naso- and oropharynx, with some of its tonsillar tissue located above and some below the soft palate (and to the back of the oral cavity).

Future Fibre Technologies: Future Fibre Technologies (FFT) is a fiber optic sensing technologies company based in Melbourne, Australia, with its US head office in Mountain View, California, Middle East head office in Dubai, Indian head office in New Delhi and European head office in London.  Founded in 1994, Future Fibre Technologies product line provides optical fiber intrusion detection systems for perimeters, buried oil and gas pipelines and data communication networks.

Sublingual papilla: The sublingual papilla or sublingual fold is a small fold of soft tissue located on each side of the frenulum linguae binding the lips to the gums within the mouth.

Jazz Pakistan: Jazz (Urdu: ‎ ) is the largest mobile network in Pakistan formed by the merger of Mobilink and Warid.  It provides a range of services for prepaid and postpaid customers to individual and corporate clients.  Its Head Office is located in Islamabad, and the current CEO is Aamir Ibrahim.

Vascular cambium: The vascular cambium (also called main cambium, wood cambium, bifacial cambium; plural "cambia") is a plant tissue located between the xylem and the phloem in the stems and roots of vascular plants.  It is a cylinder of unspecialized meristem cells that divide to form secondary vascular tissues.  It is the source of both secondary xylem growth inwards towards the pith, and secondary phloem growth outwards to the bark.  Unlike the xylem and phloem, it does not transport water, minerals or food through the plant.

Rheoencephalography: Rheoencephalography (REG) a technique of continuous registration of cerebral blood flow.  An electronic device called a rheoencephalograph is used in rheoencephalography.  Electrodes are attached to the cranium at specific points on the head and allow the device to continuously measure the electrical conductivity of the tissue located between the electrodes.  A rheoencephalograph is also used for brain blood flow biofeedback.

No issue, lelo tissue: No issue, lelo tissue (Urdu: ‎ ) was a Pakistani television advertisement campaign started by Jazz Pakistan, following the victory of Pakistan's cricket team in the 2017 ICC Champions Trophy Final.  It was directed by Hassan Dawar.  The advertisement has been dubbed as Pakistan's response to India's famous "Mauka Mauka" commercials.

Question: Where is the head office of the company that developed No issue, lelo tissue located?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "company_name": {
      "type": "string",
      "description": "The name of the company that developed the advertisement campaign."
    },
    "advertisement_campaign_name": {
      "type": "string",
      "description": "The name of the advertisement campaign."
    },
    "head_office_location": {
      "type": "string",
      "description": "The city where the company's head office is located."
    },
    "company_country": {
      "type": "string",
      "description": "The country where the company is based."
    }
  },
  "required": [
    "company_name",
    "advertisement_campaign_name",
    "head_office_location",
    "company_country"
  ],
  "additionalProperties": false
}
