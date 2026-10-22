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
McKesson &amp; Robbins scandal (1938): The McKesson & Robbins, Inc. scandal of 1938 was one of the major financial scandals of the 20th century.  The company McKesson & Robbins, Inc. (now McKesson Corporation) had been taken over in 1925 by Phillip Musica, who had previously used Adelphia Pharmaceutical Manufacturing Company as a front for bootlegging operations.  Musica, a twice-convicted felon, used assumed names to conceal his true identity in taking control of the two companies: Frank D. Costa at Adelphia Pharmaceutical and F. Donald Coster at McKesson & Robbins.  Although he was successful in expanding the company’s legitimate business operations, Musica recruited three of his brothers, also working under assumed names, one outside the company and two inside it, to generate bogus sales documentation and to pay commissions to a shell distribution company under their control.  Eventually, McKesson & Robbins treasurer Julian Thompson discovered the distribution company was bogus.  It was eventually determined that about $20 million of the $87 million in assets on the company’s balance sheet were phony.

Takeda Pharmaceutical Company: Takeda Pharmaceutical Company Ltd (武田薬品工業株式会社 , Takeda Yakuhin Kōgyō Kabushiki-gaisha ) is the largest pharmaceutical company in Japan and Asia and a top 15 pharmaceutical company in the world.  The company has over 30,000 employees worldwide and achieved 16.2 billion USD in revenue during the 2012 fiscal year.  The company is focused on metabolic disorders, gastroenterology, neurology, inflammation, as well as oncology through its independent subsidiary, Millennium: The Takeda Oncology Company.  Its headquarters is located in Chuo-ku, Osaka, and it has an office in Nihonbashi, Chuo, Tokyo.

McKesson Corporation: McKesson Corporation is an American company distributing pharmaceuticals at a retail sale level and providing health information technology, medical supplies, and care management tools.  The company had sales of $122 billion in 2012.

Opsonin Pharma Limited: Opsonin Pharma Limited is a pharmaceutical company in Bangladesh which was established in 1956.  As per the IMS Health (Intercontinental Marketing Services, Health) report, Opsonin Pharma Limited is the 4th largest pharmaceutical company in Bangladesh in-terms of sales.  As per the data of 4P Marketing Consultancy, Bangladesh Opsonin Pharma Limited holds the second position among all the pharmaceutical companies in Bangladesh in terms of prescription.

Lupin Limited: Lupin Limited is a transnational pharmaceutical company based in Mumbai.  It is the seventh-largest company by market capitalization; and the 10th-largest generic pharmaceutical company by revenue globally.  Lupin is the fifth-largest generic pharmaceutical company in the US by prescription-led market share and 3rd largest Indian pharmaceutical company by revenue.  It has the distinction of being the fastest growing generic pharmaceutical player in the US and Japan;, and is the 4th largest and the fastest growing generic pharmaceutical player in South Africa.

Glenmark Pharmaceuticals: Glenmark Pharmaceuticals is a pharmaceutical company headquartered in Mumbai, India that was founded in 1977 by Gracias Saldanha as a generic drug and active pharmaceutical ingredient manufacturer; he named the company after his two sons.  The company initially sold its products in India, Russia, and Africa.  The company went public in India in 1999, and used some of the proceeds to build its first research facility.  Saldanha's son Glenn took over as CEO in 2001, having returned to India after working at PriceWaterhouseCoopers.  By 2008 Glenmark was the fifth biggest pharmaceutical company in India.

Istaroxime: Istaroxime is an investigational drug originally patented and developed by the Italian pharmaceutical company Sigma-Tau.  Istaroxime is now under development for treatment of acute decompensated heart failure by CVie Therapeutics, a Taiwanese pharmaceutical company owned by Lee's Pharmaceutical Holdings Limited that in July 2012 has acquired from Sigma-Tau the patents and rights on Istaroxime and related compounds.  It is still in early-stage development, having been evaluated in phase two clinical trials.  Istaroxime is an innovative medication as it is an effective treatment for both systolic and diastolic heart failure.  Systolic heart failure is characterized by impaired ventricular emptying, caused by reduced contractility, and diastolic dysfunction is defined by defective ventricular filling, caused by the heart’s inability to properly relax between beats.  Intracellular calcium fluxes regulate both contraction and relaxation.  Cardiac muscle cells from patients with heart failure show smaller amounts of peak calcium in their cytoplasm during contraction, and slower removal., The mishandling of intracellular calcium is often due to problems in the cells’ ability to mediate calcium influx, and sequestration of calcium back in the sarcoplasmic reticulum. ,

Laboratoires Servier: Servier Laboratories (French: Laboratoires Servier, often abbreviated to Servier) is a privately owned French pharmaceutical company that specialises in medication for cardiological and rheumatological conditions, as well as for diabetes and clinical depression.  The consolidated turnover for the 2015 financial year was €3.9 billion.  Servier is the leading French independent pharmaceutical company, and the second largest French pharmaceutical company worldwide.  It has branches in 140 countries, achieving 82% of its sales outside France.  The annual sales of its ACE inhibitor, Coversyl (perindopril), in 2006 and 2007 exceeded 1 billion US dollars, making it Servier's highest-selling product.

McKesson Plaza: McKesson Plaza is a 38-story, 161 m office skyscraper located at 1 Post Street and Market Street in the Financial District of San Francisco, California.  The building serves as headquarters for the McKesson Corporation.

Pliva: Pliva d.o.o. is a Croatian pharmaceutical company, based in Zagreb, Croatia.  They are one of the world's largest producers of generic Adderall, and have seen drastic increases in revenue with an increasing number of patients being diagnosed with Attention Deficit Disorder (ADD).  It is the largest pharmaceutical company in Southern Europe, and Croatia's third largest exporter.  Pliva has recently recast itself as a generic pharmaceutical company leaving its proprietary business behind.

Question: Which pharmaceutical company has its headquarters in McKesson Plaza?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "company_name": {
      "type": "string",
      "description": "The name of the pharmaceutical company."
    },
    "headquarters_location": {
      "type": "string",
      "description": "The specific location identified as the company's headquarters."
    },
    "is_pharmaceutical_company": {
      "type": "boolean",
      "description": "Indicates whether the identified company is a pharmaceutical company."
    }
  },
  "required": [
    "company_name",
    "headquarters_location",
    "is_pharmaceutical_company"
  ],
  "additionalProperties": false
}
