{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nManifesto of the Sixteen: The Manifesto of the Sixteen (French: \"Manifeste des seize\" ), or Proclamation of the Sixteen, was a document drafted in 1916 by eminent anarchists Peter Kropotkin and Jean Grave which advocated an Allied victory over Germany and the Central Powers during the First World War.  At the outbreak of the war, Kropotkin and other anarchist supporters of the Allied cause advocated their position in the pages of the \"Freedom\" newspaper, provoking sharply critical responses.  As the war continued, anarchists across Europe campaigned in anti-war movements and wrote denunciations of the war in pamphlets and statements, including one February 1916 statement signed by prominent anarchists such as Emma Goldman and Rudolf Rocker.\n\nRedstone Old Fort: Redstone Old Fort — or Redstone Fort or (for a short time when built) Fort Burd — on the Nemacolin Trail, was the name of the French and Indian War-era wooden fort built in 1759 by Virginia militia colonel James Burd to guard the ancient Indian trail's river ford on a mound overlooking the eastern shore of the Monongahela River (colloquially, just \"the Mon\") in what is now Fayette County, Pennsylvania near, or (more likely) on the banks of Dunlap's Creek at the confluence.  The site is unlikely to be the same as an earlier fort the French document as Hangard dated to 1754 and which was confusedly, likely located on the nearby stream called Redstone Creek.  Red sandstones predominate the deposited rock column of the entire region.\n\nThe Gold Chignon: The Gold Chignon (French:Chignon d'or) is a 1916 French silent film directed by André Hugon and starring Mistinguett and Harry Baur.\n\nAnarchism: Anarchism is a political philosophy that advocates self-governed societies based on voluntary institutions.  These are often described as stateless societies, although several authors have defined them more specifically as institutions based on non-hierarchical free associations.  Anarchism holds the state to be undesirable, unnecessary and harmful.\n\nJudex (1963 film): Judex is a 1963 French-language French-Italian crime film remake of the 1916 French film serial of the same name concerning the adventures of pulp hero Judex.  Directed by French filmmaker Georges Franju, the film stars Channing Pollock as Judex/Vallieres, Édith Scob as Jacqueline and Francine Bergé as Diana.\n\nFlower of Paris: Flower of Paris (French:Fleur de Paris) is a 1916 French silent film directed by André Hugon and starring Mistinguett, Harry Baur and Louis Paglieri.\n\nAlsace (film): Alsace is a 1916 French film directed by Henri Pouctal. The film starring Gabrielle Réjane, Albert Dieudonné,Barbier, Camille Bardou, Berthe Jalabert and Francesca Flory in the lead roles.\n\nHistory of anarchism: Anarchism is a political philosophy that advocates stateless societies often defined as self-governed voluntary institutions, but that several authors have defined as more specific institutions based on non-hierarchical free associations.  Anarchism holds the state to be undesirable, unnecessary, or harmful.  While anti-statism is central, anarchism entails opposing authority or hierarchical organisation in the conduct of human relations, including, but not limited to, the state system.\n\nSpirit possession: Spirit possession is a term for the belief that animas, demons, extraterrestrials, gods, or spirits can take control of a human body.  The concept of spirit possession exists in many religions, including Christianity, Buddhism, Haitian Vodou, Wicca, Hinduism, Islam and Southeast Asian and African traditions.  In a 1969 study funded by the National Institute of Mental Health, spirit possession beliefs were found to exist in 74% of a sample of 488 societies in all parts of the world.  Depending on the cultural context in which it is found, possession may be considered voluntary or involuntary and may be considered to have beneficial or detrimental effects on the host.  Within possession cults, the belief that one is possessed by spirits is more common among women than men.\n\nConflict criminology: Largely based on the writings of Karl Marx, conflict criminology holds that crime in capitalist societies cannot be adequately understood without a recognition that such societies are dominated by a wealthy elite whose continuing dominance requires the economic exploitation of others, and that the ideas, institutions and practices of such societies are designed and managed in order to ensure that such groups remain marginalised, oppressed and vulnerable.  Members of marginalised and oppressed groups may sometimes turn to crime in order to gain the material wealth that apparently brings equality in capitalist societies, or simply in order to survive.  Conflict criminology derives its name from the fact that theorists within the area believe that there is no consensual social contract between state and citizen.\n\nQuestion: Which 1916 French document reinforces the belief that self-governed societies should be based on voluntary institutions?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"document_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the French document.\"\n    },\n    \"year_published\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the document was drafted or published.\"\n    },\n    \"document_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of the document (e.g., manifesto, proclamation).\"\n    },\n    \"key_authors\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of eminent anarchists who drafted the document.\"\n    },\n    \"reinforced_philosophy\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the political philosophy reinforced by the document.\"\n        },\n        \"description\": {\n          \"type\": \"string\",\n          \"description\": \"A description of the philosophy, specifically regarding self-governed societies and voluntary institutions.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"description\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"document_name\",\n    \"year_published\",\n    \"document_type\",\n    \"key_authors\",\n    \"reinforced_philosophy\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "document_name": {
        "type": "string",
        "description": "The name of the French document."
      },
      "year_published": {
        "type": "integer",
        "description": "The year the document was drafted or published."
      },
      "document_type": {
        "type": "string",
        "description": "The type of the document (e.g., manifesto, proclamation)."
      },
      "key_authors": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of eminent anarchists who drafted the document."
      },
      "reinforced_philosophy": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the political philosophy reinforced by the document."
          },
          "description": {
            "type": "string",
            "description": "A description of the philosophy, specifically regarding self-governed societies and voluntary institutions."
          }
        },
        "required": [
          "name",
          "description"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "document_name",
      "year_published",
      "document_type",
      "key_authors",
      "reinforced_philosophy"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
