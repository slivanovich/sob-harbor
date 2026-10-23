{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJoseph Orbeli: Joseph Orbeli (Armenian: Հովսեփ Աբգարի Օրբելի , Hovsep Abgari Orbeli; Russian: Иосиф Абгарович Орбели , Iosif Abgarovich Orbeli; 20 March (O.S. 8 March) 1887 – 2 February 1961) was a Soviet-Armenian orientalist and academician, who specialized in medieval history of Southern Caucasus and administered the State Hermitage Museum in Leningrad from 1934 to 1951.  Of Armenian descent, he was the founder and first president of the Armenian Academy of Sciences (1943–47).\n\nGrand Central Art Galleries: The Grand Central Art Galleries were the exhibition and administrative space of the nonprofit Painters and Sculptors Gallery Association, an artists' cooperative established in 1922 by Walter Leighton Clark together with John Singer Sargent, Edmund Greacen, and others.  Artists closely associated with the Grand Central Art Galleries included Hovsep Pushman, George de Forest Brush, and especially Sargent, whose posthumous show took place there in 1928.\n\nHovsep Pushman: Hovsep Pushman (Armenian: Յովսէփ Փուշման ; May 9, 1877 – February 13, 1966) was an American artist of Armenian background.  He was known for his contemplative still lifes and sensitive portraits of women, often in exotic dress.  He was most closely associated during his lifetime with the Grand Central Art Galleries, which represented him from its opening in 1922 until his death in 1966.\n\nFredholm integral equation: In mathematics, the Fredholm integral equation is an integral equation whose solution gives rise to Fredholm theory, the study of Fredholm kernels and Fredholm operators.  The integral equation was studied by Ivar Fredholm.  A useful method to solve such equations, the Adomian decomposition method, is due to George Adomian.\n\nEvolutionary taxonomy: Evolutionary taxonomy, evolutionary systematics or Darwinian classification is a branch of biological classification that seeks to classify organisms using a combination of phylogenetic relationship (shared descent), progenitor-descendant relationship (serial descent), and degree of evolutionary change.  This type of taxonomy may consider whole taxa rather than single species, so that groups of species can be inferred as giving rise to new groups.  The concept found its most well-known form in the modern evolutionary synthesis of the early 1940s.\n\nJames Adomian: James Adomian (born January 31, 1980) is an American stand-up comedian, actor, and impressionist.  He is best known for his work on \"Comedy Bang!  Bang! \", \"Chapo Trap House\", \"Last Comic Standing\" and \"The Late Late Show with Craig Ferguson\" where he impersonated President George W. Bush until 2009.  He voices Talking Ben in the \"Talking Tom and Friends\" animated series.\n\nAbdullah Frères: The Abdullah Frères (French for \"Abdullah Brothers\"; Turkish: \"Abdullah Biraderler\" ) were a group of three Ottoman brothers of Armenian descent, Viçen Abdullahyan (1820–1902), Hovsep Abdullahyan (1830–1908), and Kevork Abdullahyan (1839–1918), who were photographers of international fame during the late Ottoman Empire.  They took pictures of scenic views and notable individuals, including sultans.  Most of their photography was of the Ottoman Empire.\n\nAdomian decomposition method: The Adomian decomposition method (ADM) is a semi-analytical method for solving ordinary and partial nonlinear differential equations.  The method was developed from the 1970s to the 1990s by George Adomian, chair of the Center for Applied Mathematics at the University of Georgia.\n\nKutila inscription of Bareilly: The Kutila inscription of Bareilly is an inscription in the Kutila script (कुटिल लिपि) dating to 992 CE that provides crucial evidence in tracing the shared descent of the Devanagari and Bengali scripts of Northern and Eastern India from the predecessor Gupta script.  The writing was found on a stone unearthed in Bareilly district in the United Provinces of Agra and Oudh (modern-day Uttar Pradesh).  The inscription proclaims that it was created by an engraver from Kannauj who was \"\"proficient in the Kutila character\"\".  It also includes the date of the inscription, Vikram Samvat 1049, which corresponds to 992 CE.\n\nGeorge Adomian: George Adomian (March 21, 1922 – June 17, 1996) was an American mathematician of Armenian descent who developed the Adomian decomposition method (ADM) for solving nonlinear differential equations, both ordinary and partial.  The method is explained, among other places, in his book \"Solving Frontier Problems in Physics: The Decomposition Method\" (Kluwer, Dordrecht, 2004).  He was a faculty member at the University of Georgia (UGA) from 1966 through 1989.  While at UGA, he started the Center for Applied Mathematics.  Adomian was also an aerospace engineer.\n\nQuestion: George Adomian and Hovsep Pushman, have which shared descent?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"individuals\": {\n      \"type\": \"array\",\n      \"description\": \"List of individuals whose shared descent is being identified.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The full name of the individual.\"\n          },\n          \"profession\": {\n            \"type\": \"string\",\n            \"description\": \"The primary profession or role of the individual.\"\n          },\n          \"descent_as_stated\": {\n            \"type\": \"string\",\n            \"description\": \"The exact phrase used in the context to describe the individual's descent.\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"profession\",\n          \"descent_as_stated\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"shared_descent_origin\": {\n      \"type\": \"string\",\n      \"description\": \"The common origin of descent shared by all listed individuals.\"\n    },\n    \"descent_category\": {\n      \"type\": \"string\",\n      \"description\": \"The category of the shared descent (e.g., ethnic, national).\"\n    }\n  },\n  \"required\": [\n    \"individuals\",\n    \"shared_descent_origin\",\n    \"descent_category\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "individuals": {
        "type": "array",
        "description": "List of individuals whose shared descent is being identified.",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The full name of the individual."
            },
            "profession": {
              "type": "string",
              "description": "The primary profession or role of the individual."
            },
            "descent_as_stated": {
              "type": "string",
              "description": "The exact phrase used in the context to describe the individual's descent."
            }
          },
          "required": [
            "name",
            "profession",
            "descent_as_stated"
          ],
          "additionalProperties": false
        }
      },
      "shared_descent_origin": {
        "type": "string",
        "description": "The common origin of descent shared by all listed individuals."
      },
      "descent_category": {
        "type": "string",
        "description": "The category of the shared descent (e.g., ethnic, national)."
      }
    },
    "required": [
      "individuals",
      "shared_descent_origin",
      "descent_category"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
