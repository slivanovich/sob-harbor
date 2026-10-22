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
Insulin detemir: Insulin detemir is a long-acting human insulin analogue for maintaining the basal level of insulin.  Novo Nordisk markets it under the trade name Levemir.  It is an insulin analogue in which a fatty acid (myristic acid) is bound to the lysine amino acid at position B29.  It is quickly absorbed after which it binds to albumin in the blood through its fatty acid at position B29.  It then slowly dissociates from this complex.

Insulin pen: An insulin pen is used to inject insulin for the treatment of diabetes.  Insulin is a hormone produced by the pancreas.  It is composed of an insulin cartridge (integrated or bought separately) and a dial to measure the dose, and is used with disposable pen needles to deliver the dose.  It was introduced and marketed as NovoPen by the Danish company Novo Nordisk in 1985.

Insulin aspart: Insulin aspart is a fast-acting insulin analog marketed by Novo Nordisk as NovoLog/NovoRapid.  It is a manufactured form of human insulin; where a single amino acid has been exchanged.  This change helps the fast-acting insulin analog be absorbed quickly into the bloodstream.  As a result, it starts working in minutes, which allows one to take insulin and eat right away.  Fast-acting insulin analogs are considered to act similarly to the way insulin is released in people without diabetes mellitus.

Novo Nordisk: Novo Nordisk is a Danish multinational pharmaceutical company headquartered in Bagsværd, Denmark, with production facilities in eight countries, and affiliates or offices in 75 countries.  Novo Nordisk is controlled by majority shareholder Novo Holdings A/S which holds approximately 25% of its shares and a supermajority (75%) of its voting shares.

Insulin glulisine: Insulin glulisine is a rapid-acting insulin analogue that differs from human insulin in that the amino acid asparagine at position B3 is replaced by lysine and the lysine in position B29 is replaced by glutamic acid.  It was developed by Sanofi-Aventis and is sold under the trade name Apidra.  When injected subcutaneously, it appears in the blood earlier than human insulin.  When used as a meal time insulin, the dose is to be administered within 15 minutes before or 20 minutes after starting a meal.  Intravenous injections may also be used for extreme hyperglycemia, but must be performed under the supervision of a medical professional.

Insulin glargine: Insulin glargine, marketed under the names Lantus, among others, is a long-acting basal insulin analogue, given once daily to help control the blood sugar level of those with diabetes.  It consists of microcrystals that slowly release insulin, giving a long duration of action of 18 to 26 hours, with a "peakless" profile (according to the insulin glargine package insert).  Pharmacokinetically, it resembles basal insulin secretion of non-diabetic pancreatic beta cells.  Sometimes, in type 2 diabetes and in combination with a short acting sulfonylurea (drugs which stimulate the pancreas to make more insulin), it can offer moderate control of serum glucose levels.  In the absence of endogenous insulin—type 1 diabetes, depleted type 2 (in some cases) or latent autoimmune diabetes of adults in late stage—insulin glargine needs the support of fast acting insulin taken with food to reduce the effect of prandially derived glucose.

Biotechnology in pharmaceutical manufacturing: Amongst the earliest uses of biotechnology in pharmaceutical manufacturing is the use of recombinant DNA technology to modify "Escherichia coli" bacteria to produce human insulin, which was performed at Genentech in 1978.  Prior to the development of this technique, insulin was extracted from the pancreas glands of cattle, pigs, and other farm animals.  While generally efficacious in the treatment of diabetes, animal-derived insulin is not indistinguishable from human insulin, and may therefore produce allergic reactions.  Genentech researchers produced artificial genes for each of the two protein chains that comprise the insulin molecule.  The artificial genes were "then inserted... into plasmids... among a group of genes that" are activated by lactose.  Thus, the insulin-producing genes were also activated by lactose.  The recombinant plasmids were inserted into "Escherichia coli" bacteria, which were "induced to produce 100,000 molecules of either chain A or chain B human insulin."  The two protein chains were then combined to produce insulin molecules.

Liraglutide: Liraglutide (NN2211) is a derivative of human incretin (metabolic hormone) glucagon-like peptide-1 (GLP-1) that is used as a long-acting glucagon-like peptide-1 receptor agonist, binding to the same receptors as does the endogenous metabolic hormone GLP-1 that stimulates insulin secretion.  Marketed under the brand name Victoza, it is an injectable drug developed by Novo Nordisk for the treatment of type 2 diabetes.  In 2015, Novo Nordisk began marketing a separate strength in the U.S. and E.U. under the brand name Saxenda as a treatment for adults who are obese or overweight with at least one weight-related comorbid condition.

Insulin degludec: Insulin degludec (INN/USAN) is an ultralong-acting basal insulin analogue that was developed by Novo Nordisk under the brand name Tresiba.  It is administered via subcutaneous injection once daily to help control the blood sugar level of those with diabetes.  It has a duration of action that lasts up to 42 hours (compared to 18 to 26 hours provided by other marketed long-acting insulins such as insulin glargine and insulin detemir), making it a once-daily basal insulin, that is one that provides a base insulin level, as opposed to the fast and short acting bolus insulins.

Insulin oscillation: The insulin concentration in blood increases after meals and gradually returns to basal levels during the next 1–2 hours.  However, the basal insulin level is not stable.  It oscillates with a regular period of 3-6 min.  After a meal the amplitude of these oscillations increases but the periodicity remains constant.  The oscillations are believed to be important for insulin sensitivity by preventing downregulation of insulin receptors in target cells.  Such downregulation underlies insulin resistance, which is common in type 2 diabetes.  It would therefore be advantageous to administer insulin to diabetic patients in a manner mimicking the natural oscillations.  The insulin oscillations are generated by pulsatile release of the hormone from the pancreas.  Insulin originates from beta cells located in the islets of Langerhans.  Since each islet contains up to 2000 beta cells and there are one million islets in the pancreas it is apparent that pulsatile secretion requires sophisticated synchronization both within and among the islets of Langerhans.

Question: Insulin detemir is a long-acting human insulin analogue for maintaining the basal level of insulin, Novo Nordisk markets it under which trade name?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "insulin_analogue_name": {
      "type": "string",
      "description": "The name of the insulin analogue."
    },
    "insulin_type": {
      "type": "string",
      "description": "The classification of the insulin analogue based on its action duration."
    },
    "manufacturer": {
      "type": "string",
      "description": "The company that markets the insulin analogue."
    },
    "trade_name": {
      "type": "string",
      "description": "The commercial trade name under which the insulin analogue is marketed."
    },
    "purpose": {
      "type": "string",
      "description": "The primary medical purpose of the insulin analogue."
    }
  },
  "required": [
    "insulin_analogue_name",
    "insulin_type",
    "manufacturer",
    "trade_name",
    "purpose"
  ],
  "additionalProperties": false
}
