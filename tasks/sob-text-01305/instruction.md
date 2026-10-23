{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nIncrease Mather: Increase Mather (June 21, 1639 O.S. – August 23, 1723 O.S.) was a major figure in the early history of the Massachusetts Bay Colony and Province of Massachusetts Bay (now the Commonwealth of Massachusetts).  He was a Puritan minister who was involved with the government of the colony, the administration of Harvard College, and most notoriously, the Salem witch trials.  He was the son of Richard Mather, and the father of Cotton Mather, both influential Puritan ministers.\n\nKenneth Silverman: Kenneth Eugene Silverman (February 5, 1936 – July 7, 2017) was an American biographer and educator.  He won a Pulitzer Prize and a Bancroft Prize for his 1984 biography of Cotton Mather, \"The Life and Times of Cotton Mather\".  Silverman, who specialized In Colonial American literature, was a professor of English at New York University until his retirement in 2001.\n\nHistory of New England: The history of New England is the history of the New England region of North America in the current-day United States.  New England is the oldest clearly defined region of the United States, and it predates the history of the United States by over 150 years.  While New England was originally inhabited by Indigenous peoples, English Pilgrims and especially Puritans, fleeing religious persecution in England, arrived in the 1620-1660 era.  They dominated the region; their religion was later called Congregationalism.  They and their descendants are called Yankees. Farming, fishing and lumbering prospered, as did whaling, sea trading, and merchandising.\n\nWonders of the Invisible World: The Wonders of the Invisible World was a book written by Cotton Mather and published in 1693.  It was subtitled, \"Observations As well Historical as Theological, upon the Nature, the Number, and the Operations of the Devils\".  The book defended Mather's role in the witchhunt conducted in Salem, Massachusetts.  It espoused the belief that witchcraft was an evil magical power.  Mather saw witches as tools of the devil in Satan's battle to \"overturn this poor plantation, the Puritan colony\", and prosecution of witches as a way to secure God's blessings for the colony.\n\nCotton Mather: Cotton Mather, FRS (February 12, 1663 – February 13, 1728; A.B. 1678, Harvard College; A.M. 1681, honorary doctorate 1710, University of Glasgow) was a socially and politically influential New England Puritan minister, prolific author, and pamphleteer.  He left a scientific legacy due to his hybridization experiments and his promotion of inoculation for disease prevention, though he is most frequently remembered today for his vigorous support for the Salem witch trials.  He was subsequently denied the Presidency of Harvard College which his father, Increase Mather, had held.\n\nCotton Mather (band): Cotton Mather are a band that was founded by Robert Harrison of Austin, Texas in 1990.  What started as an experimental collaboration with cellist Nat Shelton, had by 1993 evolved into a guitar driven pop quartet.  They have drawn comparisons to the Beatles, Elvis Costello and the Attractions, Squeeze, and Guided by Voices.  In his 2007 book, \"Shake Some Action\", John Borack rated the \"Kon Tiki\" album at number 26 of his Top 200 Power Pop Albums of all time, comparing the album to \"Revolver\"-era Beatles, Big Star, and The Apples in Stereo. \" NME\" suggested Cotton Mather might be \"the most exciting guitar pop band since Supergrass.\"\n\nRichard Mather: Richard Mather (1596 – 22 April 1669) was a Puritan minister in colonial Boston, Massachusetts.  He was father to Increase Mather and grandfather to Cotton Mather, both celebrated Boston divines.\n\nSeptember 2, 1692 letter by Cotton Mather: In a letter dated September 2, 1692, Cotton Mather wrote to judge William Stoughton.  Among the notable things about this letter is the provenance: it seems to be the last important correspondence from Cotton Mather to surface in modern times, with the holograph manuscript not arriving in the archives for scholars to view, and authenticate, until sometime between 1978 and 1985.\n\nJohn N. Mather: John Norman Mather (June 9, 1942 – January 28, 2017) was a mathematician at Princeton University known for his work on singularity theory and Hamiltonian dynamics.  He was descended from Atherton Mather (1663-1734), a cousin of Cotton Mather.\n\nJohn Williams (minister): John Williams (10 December 1664 – 12 June 1729) was a New England Puritan minister who became famous for \"The Redeemed Captive\", his account of his captivity by the Mohawk after the Deerfield Massacre during Queen Anne's War.  He was an uncle of the notable pastor and theologian Jonathan Edwards.  <br> His first wife Eunice Mather was a niece of Rev Increase Mather and a cousin of Rev. Cotton Mather and was related to Rev. John Cotton.\n\nQuestion: Cotton Mather was politically influential in what oldest defined region in the US?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"region_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the region.\"\n    },\n    \"region_historical_status\": {\n      \"type\": \"string\",\n      \"description\": \"A description of the region's historical status in the US.\"\n    },\n    \"influential_person\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the influential person.\"\n        },\n        \"influence_types\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"Types of influence the person had in the region.\"\n        },\n        \"primary_role\": {\n          \"type\": \"string\",\n          \"description\": \"The primary role of the influential person.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"influence_types\",\n        \"primary_role\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"region_name\",\n    \"region_historical_status\",\n    \"influential_person\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "region_name": {
        "type": "string",
        "description": "The name of the region."
      },
      "region_historical_status": {
        "type": "string",
        "description": "A description of the region's historical status in the US."
      },
      "influential_person": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the influential person."
          },
          "influence_types": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Types of influence the person had in the region."
          },
          "primary_role": {
            "type": "string",
            "description": "The primary role of the influential person."
          }
        },
        "required": [
          "name",
          "influence_types",
          "primary_role"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "region_name",
      "region_historical_status",
      "influential_person"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
