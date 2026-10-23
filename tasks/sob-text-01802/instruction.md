{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCarvedilol: Carvedilol, sold under the brand name Coreg among others, is a beta blocker used for treating mild to severe congestive heart failure (CHF), left ventricular dysfunction (LVD) following heart attack in people who are otherwise stable, and for treating high blood pressure.\n\nCardiac asthma: Cardiac asthma is a medical diagnosis of wheezing, coughing or shortness of breath due to congestive heart failure.  It is known as cardiac asthma because the symptoms mimic ordinary asthma (bronchial asthma).  One study found that patients with cardiac asthma represented one third of congestive heart failure in elderly patients.\n\nHeart failure with preserved ejection fraction: Heart failure with preserved ejection fraction (HFpEF) is a form of congestive heart failure wherein the amount of blood pumped from the heart's left ventricle with each beat (ejection fraction) is greater than 50%.  Approximately half of people with heart failure have HFpEF, while the remainder display a reduction in ejection fraction, or heart failure with reduced ejection fraction (HFrEF).\n\nTerry's nails: Terry's nails is a physical condition in which a person's fingernails or toenails appear white with a characteristic \"ground glass\" appearance without any lunula.  The condition is thought to be due to a decrease in vascularity and an increase in connective tissue within the nail bed.  It frequently occurs in the setting of liver failure, cirrhosis, diabetes mellitus, congestive heart failure, hyperthyroidism, or malnutrition.  Eighty percent of patients with severe liver disease have Terry's nails, but they are also found in patients with kidney failure, in patients with congestive heart failure and are described as a brown arc near the ends of the nails.  The recognition of characteristic nail patterns, such as Terry’s nails, may be a helpful herald for early diagnosis of systemic diseases.\n\nCongestive hepatopathy: Congestive hepatopathy, also known as nutmeg liver and chronic passive congestion of the liver, is liver dysfunction due to venous congestion, usually due to congestive heart failure.  The gross pathological appearance of a liver affected by chronic passive congestion is \"speckled\" like a grated nutmeg kernel; the dark spots represent the dilated and congested hepatic venules and small hepatic veins.  The paler areas are unaffected surrounding liver tissue.  When severe and longstanding, hepatic congestion can lead to fibrosis; if congestion is due to right heart failure, it is called cardiac cirrhosis.\n\nBeta-3 adrenergic antagonist: A Beta-3 adrenergic antagonist (β-adrenoceptor antagonist) is an adrenergic antagonist which blocks the Beta-3 adrenergic receptors of cells, with either high specificity (an antagonist which is selective for β adrenoceptors) like L-748,328, L-748,337 and SR 59,230A or non-specifically (an antagonist for β and for β or β adrenoceptors) like the non-selective betablocker Carvedilol.\n\nHeart failure: Heart failure (HF), often referred to as congestive heart failure (CHF), occurs when the heart is unable to pump sufficiently to maintain blood flow to meet the body's needs.  Signs and symptoms commonly include shortness of breath, excessive tiredness, and leg swelling.  The shortness of breath is usually worse with exercise, while lying down, and may wake the person at night.  A limited ability to exercise is also a common feature.  Chest pain, including angina, does not typically occur due to heart failure.\n\nMetolazone: Metolazone is a thiazide-like diuretic marketed under the brand names Zytanix from Zydus Cadila, Zaroxolyn, and Mykrox.  It is primarily used to treat congestive heart failure and high blood pressure.  Metolazone indirectly decreases the amount of water reabsorbed into the bloodstream by the kidney, so that blood volume decreases and urine volume increases.  This lowers blood pressure and prevents excess fluid accumulation in heart failure.  Metolazone is sometimes used together with loop diuretics such as furosemide or bumetanide, but these highly effective combinations can lead to dehydration and electrolyte abnormalities.\n\nRobert R. Ruffolo, Jr: Robert R. Ruffolo (born April, 1950, in Yonkers, N.Y.) was president of research and development for Wyeth Pharmaceuticals, and corporate Senior Vice President of Wyeth from 2001 to 2008.  During his career in the pharmaceutical industry, Ruffolo played a significant role in the discovery and/or development of a number of marketed products, including dobutamine (Dobutrex) for the acute management of congestive heart failure, and eprosartan (Teveten) for hypertension.  He holds the patent for the discovery of use of carvedilol (Coreg) for the treatment of congestive heart failure, and he led the research team that discovered ropinerole (Requip) for Parkinson's Disease.\n\nDeoxyepinephrine: Deoxyepinephrine, also known by the common names N-methyldopamine and epinine, is an organic compound and natural product that is structurally related to the important neurotransmitters dopamine and epinephrine.  All three of these compounds also belong to the catecholamine family.  The pharmacology of epinine largely resembles that of its \"parent\", dopamine.  Epinine has been found in plants, insects and animals.  It is also of significance as the active metabolic breakdown product of the prodrug ibopamine, which has been used to treat congestive heart failure.\n\nQuestion: What generic medication is a non-selective betablocker used to treat congestive heart failure?  \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"medication_name\": {\n      \"type\": \"string\",\n      \"description\": \"The generic name of the medication.\"\n    },\n    \"medication_class\": {\n      \"type\": \"string\",\n      \"description\": \"The pharmacological class of the medication.\"\n    },\n    \"selectivity_type\": {\n      \"type\": \"string\",\n      \"description\": \"Describes the selectivity of the beta-blocker (e.g., non-selective).\"\n    },\n    \"conditions_treated\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of medical conditions the medication is used to treat.\"\n    },\n    \"brand_names\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of brand names under which the medication is sold.\"\n    }\n  },\n  \"required\": [\n    \"medication_name\",\n    \"medication_class\",\n    \"selectivity_type\",\n    \"conditions_treated\",\n    \"brand_names\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "medication_name": {
        "type": "string",
        "description": "The generic name of the medication."
      },
      "medication_class": {
        "type": "string",
        "description": "The pharmacological class of the medication."
      },
      "selectivity_type": {
        "type": "string",
        "description": "Describes the selectivity of the beta-blocker (e.g., non-selective)."
      },
      "conditions_treated": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of medical conditions the medication is used to treat."
      },
      "brand_names": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of brand names under which the medication is sold."
      }
    },
    "required": [
      "medication_name",
      "medication_class",
      "selectivity_type",
      "conditions_treated",
      "brand_names"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
