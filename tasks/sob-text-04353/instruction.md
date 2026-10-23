{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJoan Miller: Joan W. Miller is a Canadian-American ophthalmologist and scientist who has made notable contributions to the treatment and understanding of eye disorders (particularly diseases of the retina).  She is credited for developing photodynamic therapy (PDT) with verteporfin (Visudyne®), the first pharmacologic therapy for retinal disease.  She also co-discovered the role of vascular endothelial growth factor (VEGF) in eye disease and demonstrated the therapeutic potential of VEGF inhibitors, forming the scientific basis of anti-VEGF therapy for age-related macular degeneration (AMD), diabetic retinopathy, and related conditions.\n\nNapoleone Ferrara: Napoleone Ferrara, M.D. (born 26 July 1956, Catania), is an Italian-American molecular biologist who joined University of California, San Diego Moores Cancer Center in 2013 after a storied career in Northern California at the biotechnology giant Genentech, where he pioneered the development of new treatments for angiogenic diseases such as cancer, age-related macular degeneration (AMD), and diabetic retinopathy.  At Genetech, he discovered VEGF—and made the first anti-VEGF antibody—which suppresses growth of a variety of tumors.  These findings helped lead to development of the first clinically available angiogenesis inhibitor, bevacizumab (Avastin), which prevents the growth of new blood vessels into a solid tumor and which has become part of standard treatment for a variety of cancers.  Ferrara’s work led also to the development of ranibizumab (Lucentis), a drug that is highly effective at preventing vision loss in intraocular neovascular disorders.\n\nEmixustat hydrochloride: Emixustat hydrochloride is a small molecule notable for its establishment of a new class of compounds known as Visual Cycle Modulators (VCM).  It is also the first synthetic medicinal compound shown to affect retinal disease processes when taken by mouth.  Emixustat was invented by the British-American chemist, Ian L. Scott, and is currently in Phase 3 trials for dry, age-related macular degeneration (AMD).  The compound is also being investigated as a potential therapy for proliferative diabetic retinopathy, diabetic macular edema and Stargardt disease.  In 2008, Acucela Inc. partnered with Otsuka Pharmaceutical Company for the development of emixustat (ACU-4429) in an agreement totaling $263 million in cash and milestone payments.\n\nPredictive genomics: Predictive genomics is at the intersection of multiple disciplines: predictive medicine, personal genomics and translational bioinformatics.  Specifically, predictive genomics deals with the future phenotypic outcomes via prediction in areas such as complex multifactorial diseases in humans.  To date, the success of predictive genomics has been dependent on the genetic framework underlying these applications, typically explored in genome-wide association (GWA) studies.  The identification of associated single-nucleotide polymorphisms (variation of a DNA sequence in a population) underpin GWA studies in complex diseases that have ranged from Type 2 Diabetes (T2D), Age-related macular degeneration (AMD) and Crohn’s Disease.\n\nGeographic atrophy: Geographic Atrophy (GA), also known as atrophic age-related macular degeneration (AMD) or advanced dry AMD, is an advanced form of age-related macular degeneration that can result in the progressive and irreversible loss of retina (photoreceptors, retinal pigment epithelium, choriocappillaris) which can lead to a loss of visual function over time.  It is estimated that GA affects >5 million people worldwide and approximately 1 million patients in the US, which is similar to the prevalence of neovascular (wet) AMD, the other advanced form of the disease.\n\nRanibizumab: Ranibizumab (trade name Lucentis among others) is a monoclonal antibody fragment (Fab) created from the same parent mouse antibody as bevacizumab.  It is an anti-angiogenic that has been approved to treat the \"wet\" type of age-related macular degeneration (AMD, also ARMD), a common form of age-related vision loss.\n\nRinucumab: Rinucumab is a monoclonal antibody designed for the treatment of neovascular age-related macular degeneration.\n\nOSI Pharmaceuticals: OSI Pharmaceuticals, Inc. is an American pharmaceutical company based in Long Island, New York with facilities in Colorado, New Jersey and the United Kingdom.  OSI specializes in the discovery and development of molecular targeted therapies.  Though oncology is the top priority for OSI, research and development targeting type 2 diabetes and obesity is conducted through their U.K. subsidiary Prosidion Limited.  OSI has also made a foray into the ophthalmology market through a marketing agreement with Pfizer over Macugen (Pegaptanib) for Age-related macular degeneration; however, acquisition of the firm Eyetech, meant to provide control over this product and diversify the company, has been unsuccessful, ending in divestiture.\n\nAMD Alliance International: AMD Alliance International is a non-profit coalition of the world’s leading vision, seniors and research organizations working to raise awareness of age-related macular degeneration, understanding of available options for prevention, early detection, treatment, rehabilitation and support services.  It is the only international organization in the world that concentrates exclusively on age related macular degeneration, the leading cause of vision loss in the developed world.\n\nPegaptanib: Pegaptanib sodium injection (brand name Macugen) is an anti-angiogenic medicine for the treatment of neovascular (wet) age-related macular degeneration (AMD).  It was discovered by NeXstar Pharmaceuticals and licensed in 2000 to EyeTech Pharmaceuticals, now OSI Pharmaceuticals, for late stage development and marketing in the United States.  Outside the US pegaptanib is marketed by Pfizer.  Approval was granted by the U.S. Food and Drug Administration (FDA) in December 2004.\n\nQuestion: Pegaptanib sodium injection (brand name Macugen) is an anti-angiogenic medicine for the treatment of neovascular (wet) age-related macular degeneration (AMD), it was licensed in 2000 to EyeTech Pharmaceuticals, now called what, an American pharmaceutical company based in Long Island, New York with facilities in Colorado, New Jersey and the United Kingdom?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"company_name\": {\n      \"type\": \"string\",\n      \"description\": \"The current name of the pharmaceutical company.\"\n    },\n    \"company_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of company, e.g., pharmaceutical.\"\n    },\n    \"headquarters_location\": {\n      \"type\": \"string\",\n      \"description\": \"The primary location of the company's headquarters.\"\n    },\n    \"other_facilities_locations\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Other locations where the company has facilities.\"\n    },\n    \"product_licensed\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the product that was licensed to the company.\"\n    },\n    \"licensing_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the product was licensed.\"\n    }\n  },\n  \"required\": [\n    \"company_name\",\n    \"company_type\",\n    \"headquarters_location\",\n    \"other_facilities_locations\",\n    \"product_licensed\",\n    \"licensing_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "company_name": {
        "type": "string",
        "description": "The current name of the pharmaceutical company."
      },
      "company_type": {
        "type": "string",
        "description": "The type of company, e.g., pharmaceutical."
      },
      "headquarters_location": {
        "type": "string",
        "description": "The primary location of the company's headquarters."
      },
      "other_facilities_locations": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Other locations where the company has facilities."
      },
      "product_licensed": {
        "type": "string",
        "description": "The name of the product that was licensed to the company."
      },
      "licensing_year": {
        "type": "integer",
        "description": "The year the product was licensed."
      }
    },
    "required": [
      "company_name",
      "company_type",
      "headquarters_location",
      "other_facilities_locations",
      "product_licensed",
      "licensing_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
